"""The search-budget hook (``scripts/search_budget.py``) and its wiring into CI.

The hook is the only thing that stops a session from billing hundreds of searches
(issue #19), and it runs inside the CLI where a crash or a wrong JSON shape fails
silently. So it is tested both as functions and as the subprocess the CLI starts.
"""

from __future__ import annotations

import json
import math
import os
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import pytest
import search_budget as sb
import yaml
from conftest import REPO

HOOK = REPO / "scripts" / "search_budget.py"
NOW = "2026-11-03T12:00:00+00:00"


def _call(state, tool="WebSearch", agent=None, cap=50, per_scout=8):
    return sb.decide(state, tool, agent, cap, per_scout, NOW)


def _denied(out) -> bool:
    return bool(out) and out["hookSpecificOutput"].get("permissionDecision") == "deny"


def test_searches_are_refused_at_the_session_cap_and_fetches_never():
    state: dict = {}
    outs = [_call(state, cap=5) for _ in range(5)]
    assert not any(_denied(o) for o in outs)
    assert state["searches"] == 5 and state["cap_reached_at"] == NOW
    refusal = _call(state, cap=5)
    assert _denied(refusal)
    reason = refusal["hookSpecificOutput"]["permissionDecisionReason"]
    assert "5/5" in reason and "waived" in reason
    assert "every scout has reported" in reason, "the cap must not invite logging early"
    assert state["searches"] == 5 and state["denied"] == 1, "a refused call is not a search"
    # Reading pages the session already found stays possible after the cap.
    assert _call(state, tool="WebFetch", cap=5) is None
    assert state["fetches"] == 1 and state["denied"] == 1


def test_other_tools_pass_uncounted():
    state: dict = {}
    assert _call(state, tool="Read") is None
    assert state["searches"] == 0 and state["fetches"] == 0


def test_the_first_search_of_each_agent_states_the_caps():
    state: dict = {}
    for agent in (None, "a1"):
        note = _call(state, agent=agent, cap=30, per_scout=6)["hookSpecificOutput"]
        assert "permissionDecision" not in note
        assert "30 WebSearch calls this session, 6 per scout" in note["additionalContext"]
    assert _call(state, agent="a1", cap=30, per_scout=6) is None, "said once per agent"
    assert "no session cap" in str(_call({}, cap=0, per_scout=0))


def test_a_countdown_from_the_nudge_share_of_the_cap_allows_the_call():
    state: dict = {}
    cap = 10
    outs = [_call(state, cap=cap) for _ in range(cap)]
    start = math.ceil(sb.NUDGE_SHARE * cap)
    assert all(o is None for o in outs[1 : start - 1]), "silent between the note and the share"
    nudges = outs[start - 1 :]
    for out in nudges:
        spec = out["hookSpecificOutput"]
        assert spec["hookEventName"] == "PreToolUse"
        assert "permissionDecision" not in spec, "a nudge must not deny"
    assert f"{start}/{cap}" in nudges[0]["hookSpecificOutput"]["additionalContext"]
    assert f"{cap - start} left" in nudges[0]["hookSpecificOutput"]["additionalContext"]


def test_one_scout_cannot_spend_the_budget_of_the_others():
    state: dict = {}
    for _ in range(3):
        assert not _denied(_call(state, agent="a1", per_scout=3))
    refusal = _call(state, agent="a1", per_scout=3)
    assert _denied(refusal)
    assert "return your digest" in refusal["hookSpecificOutput"]["permissionDecisionReason"]
    assert not _denied(_call(state, agent="a2", per_scout=3))
    assert not _denied(_call(state, agent=None, per_scout=3)), "the main agent has no scout cap"
    assert state["by_agent"] == {
        "a1": {"searches": 3, "fetches": 0},
        "a2": {"searches": 1, "fetches": 0},
    }
    assert state["searches"] == 5 and state["no_agent_id"] == 1


def test_a_scout_at_the_session_cap_is_told_to_return_its_digest():
    state: dict = {}
    _call(state, cap=1)
    refusal = _call(state, agent="a1", cap=1)
    assert _denied(refusal)
    assert "return your digest" in refusal["hookSpecificOutput"]["permissionDecisionReason"]


def test_the_scouts_leave_the_main_agent_one_scouts_allowance():
    state: dict = {}
    cap, per_scout = 20, 4
    for scout in ("a1", "a2", "a3", "a4"):
        for _ in range(per_scout):
            assert not _denied(_call(state, agent=scout, cap=cap, per_scout=per_scout))
    assert state["searches"] == cap - per_scout
    refusal = _call(state, agent="a5", cap=cap, per_scout=per_scout)
    assert _denied(refusal), "the reserve belongs to the main agent"
    assert "reserved for the main" in refusal["hookSpecificOutput"]["permissionDecisionReason"]
    for _ in range(per_scout):
        assert not _denied(_call(state, cap=cap, per_scout=per_scout))
    assert _denied(_call(state, cap=cap, per_scout=per_scout)), "the session cap still binds"


def test_the_reserve_shrinks_as_the_main_agent_uses_it():
    state: dict = {}
    _call(state, cap=10, per_scout=4)
    _call(state, cap=10, per_scout=4)
    outs = [_call(state, agent=f"a{i}", cap=10, per_scout=4) for i in range(8)]
    # Main used 2 of its 4: the scouts may bring the session to 10 - 2 = 8.
    assert sum(not _denied(o) for o in outs) == 6 and state["searches"] == 8


def test_the_main_agent_has_no_per_agent_cap():
    state: dict = {}
    outs = [_call(state, cap=30, per_scout=4) for _ in range(30)]
    assert not any(_denied(o) for o in outs), "the main agent may use what the scouts leave"


def test_spawns_beyond_max_scouts_are_refused():
    state: dict = {}
    tools = ["Agent", "Task"] * sb.MAX_SCOUTS
    assert not any(_denied(_call(state, tool=t)) for t in tools[: sb.MAX_SCOUTS])
    refusal = _call(state, tool="Agent")
    assert _denied(refusal) and f"{sb.MAX_SCOUTS}/{sb.MAX_SCOUTS}" in str(refusal)
    assert state["scouts_spawned"] == sb.MAX_SCOUTS and state["denied"] == 1
    assert _call(state, tool="Agent", agent="a1") is None, "a subagent's spawn is not counted"


def test_the_default_caps_fit_the_scouts_and_the_main_reserve():
    # Otherwise the last scouts would be cut off by the scouts' share before their own cap.
    assert (sb.MAX_SCOUTS + 1) * sb.DEFAULT_MAX_PER_SCOUT <= sb.DEFAULT_MAX_SEARCHES


def test_without_agent_id_only_the_session_cap_binds():
    # A CLI before 2.1.69 sends no agent_id: its scouts look like the main agent.
    state: dict = {}
    outs = [_call(state, cap=20, per_scout=2) for _ in range(10)]
    assert not any(_denied(o) for o in outs)
    assert state["by_agent"] == {} and state["no_agent_id"] == 10


def test_zero_disables_a_cap():
    state: dict = {}
    assert not any(_denied(_call(state, agent="a", cap=0, per_scout=0)) for _ in range(200))
    assert state["searches"] == 200 and state["cap_reached_at"] is None
    assert not sb.session_cap_used(state)


DEFAULT = sb.DEFAULT_MAX_SEARCHES


@pytest.mark.parametrize(
    ("raw", "expected"),
    [(None, DEFAULT), ("", DEFAULT), ("12", 12), ("0", 0), ("-3", DEFAULT), ("x", DEFAULT)],
)
def test_caps_come_from_the_environment_with_defaults(monkeypatch, raw, expected):
    monkeypatch.delenv("MAX_WEB_SEARCHES_PER_SCOUT", raising=False)
    if raw is None:
        monkeypatch.delenv("MAX_WEB_SEARCHES", raising=False)
    else:
        monkeypatch.setenv("MAX_WEB_SEARCHES", raw)
    assert sb.caps() == (expected, sb.DEFAULT_MAX_PER_SCOUT)


def test_session_cap_used_reads_the_file_state():
    assert not sb.session_cap_used(None)
    assert not sb.session_cap_used({"searches": 49, "max_searches": 50})
    assert sb.session_cap_used({"searches": 50, "max_searches": 50})
    assert not sb.session_cap_used({"searches": 50, "max_searches": 0})
    assert not sb.session_cap_used({"searches": "many", "max_searches": 50}), "no crash"


def test_normalise_repairs_each_bad_field_and_keeps_the_good_ones():
    state = sb.normalise({"searches": None, "fetches": 7, "denied": True, "by_agent": [],
                          "active_agents": 3, "scouts_spawned": -1, "max_searches": 50})
    assert state["searches"] == 0 and state["fetches"] == 7 and state["denied"] == 0
    assert state["by_agent"] == {} and state["active_agents"] == {}
    assert state["scouts_spawned"] == 0 and state["max_searches"] == 50
    assert sb.normalise([1, 2]) == sb.normalise(None)


def test_read_state_tells_a_missing_file_from_a_damaged_one(tmp_path):
    path = tmp_path / "budget.json"
    assert sb.read_state(path) is None
    path.write_text("")
    assert sb.read_state(path)["unreadable"] is True
    path.write_text('{"searches": 3}')
    state = sb.read_state(path)
    assert state["searches"] == 3 and "unreadable" not in state


# ---------------------------------------------------------- as the CLI runs it
def _hook(path: Path | None, payload: dict, **env: str) -> subprocess.CompletedProcess:
    full = {k: v for k, v in os.environ.items() if k not in {"SEARCH_BUDGET_FILE"}}
    if path is not None:
        full["SEARCH_BUDGET_FILE"] = str(path)
    full.update(env)
    return subprocess.run(
        [sys.executable, "-I", str(HOOK)],
        input=json.dumps(payload),
        capture_output=True,
        text=True,
        env=full,
        check=False,
    )


def _payload(tool: str = "WebSearch", **extra: str) -> dict:
    return {
        "session_id": "s",
        "transcript_path": "/x",
        "cwd": str(REPO),
        "hook_event_name": "PreToolUse",
        "tool_name": tool,
        "tool_input": {"query": "q"},
        "tool_use_id": "t",
        **extra,
    }


def test_the_hook_prints_a_refusal_the_cli_accepts(tmp_path):
    path = tmp_path / "budget.json"
    first = _hook(path, _payload(), MAX_WEB_SEARCHES="1")
    assert first.returncode == 0
    nudge = json.loads(first.stdout)["hookSpecificOutput"]
    assert set(nudge) == {"hookEventName", "additionalContext"} and "1/1" in str(nudge)
    second = _hook(path, _payload(), MAX_WEB_SEARCHES="1")
    assert second.returncode == 0
    spec = json.loads(second.stdout)["hookSpecificOutput"]
    assert set(spec) == {"hookEventName", "permissionDecision", "permissionDecisionReason"}
    assert spec["permissionDecision"] == "deny"
    state = json.loads(path.read_text())
    assert state["searches"] == 1 and state["denied"] == 1 and state["max_searches"] == 1


def test_parallel_scouts_are_counted_exactly(tmp_path):
    path = tmp_path / "budget.json"
    with ThreadPoolExecutor(max_workers=12) as pool:
        runs = list(pool.map(
            lambda i: _hook(
                path, _payload(agent_id=f"a{i % 4}"),
                MAX_WEB_SEARCHES="0", MAX_WEB_SEARCHES_PER_SCOUT="0",
            ),
            range(40),
        ))
    assert all(r.returncode == 0 and "deny" not in r.stdout for r in runs)
    state = json.loads(path.read_text())
    assert state["searches"] == 40, "a lost update under parallel scouts"
    assert {k: v["searches"] for k, v in state["by_agent"].items()} == {
        "a0": 10, "a1": 10, "a2": 10, "a3": 10
    }


@pytest.mark.parametrize("where", ["unset", "unwritable"])
def test_the_hook_fails_open(tmp_path, where):
    path = None if where == "unset" else tmp_path / "a-directory"
    if path is not None:
        path.mkdir()
    run = _hook(path, _payload())
    assert run.returncode == 0 and run.stdout == "", "a broken counter must allow the call"
    assert "search_budget" in run.stderr


def test_a_corrupt_budget_file_restarts_the_count(tmp_path):
    path = tmp_path / "budget.json"
    path.write_text("{not json")
    assert _hook(path, _payload()).returncode == 0
    assert json.loads(path.read_text())["searches"] == 1


def test_a_wrongly_typed_budget_file_is_repaired_not_failed_open(tmp_path):
    path = tmp_path / "budget.json"
    path.write_text(json.dumps({"searches": None, "by_agent": [], "fetches": 7}))
    run = _hook(path, _payload(agent_id="a1"))
    assert run.returncode == 0 and "failing open" not in run.stderr
    state = json.loads(path.read_text())
    assert state["searches"] == 1 and state["fetches"] == 7
    assert state["by_agent"] == {"a1": {"searches": 1, "fetches": 0}}


def test_a_write_killed_midway_leaves_the_previous_state(tmp_path, monkeypatch):
    path = tmp_path / "budget.json"
    monkeypatch.setenv("MAX_WEB_SEARCHES", "50")
    sb.run(_payload(), path)
    before = path.read_text()

    def killed(src, dst):
        raise KeyboardInterrupt  # stands in for the step timeout killing the CLI

    monkeypatch.setattr(sb.os, "replace", killed)
    with pytest.raises(KeyboardInterrupt):
        sb.run(_payload(), path)
    assert path.read_text() == before, "the data file is replaced whole or not at all"
    names = sorted(p.name for p in tmp_path.iterdir())
    assert names == ["budget.json", "budget.json.lock"], "no temporary file left behind"


def test_running_subagents_are_tracked_from_start_to_stop(tmp_path):
    path = tmp_path / "budget.json"
    for event, agent in (("SubagentStart", "a1"), ("SubagentStart", "a2"),
                         ("SubagentStop", "a1")):
        run = _hook(path, {"hook_event_name": event, "agent_id": agent,
                           "agent_type": "research-scout", "session_id": "s"})
        assert run.returncode == 0 and run.stdout == ""
    assert sb.running_agents(sb.read_state(path)) == {"a2": "research-scout"}
    assert sb.read_state(path)["subagents_started"] == 2, "a stop does not undo a start"


# ------------------------------------------------------------------- wiring
def test_ci_settings_register_the_hook_for_web_calls_spawns_and_subagents():
    settings = json.loads((REPO / ".claude" / "settings.ci.json").read_text("utf-8"))
    for event in ("PreToolUse", "SubagentStart", "SubagentStop"):
        entry = next(
            e for e in settings["hooks"][event]
            if "scripts/search_budget.py" in e["hooks"][0]["command"]
        )
        # The venv's interpreter, not the runner's python3: the project's Python version.
        assert entry["hooks"][0]["command"].startswith(
            '"$CLAUDE_PROJECT_DIR/.venv/bin/python" -I '
        ), event
        if event == "PreToolUse":
            assert set(entry["matcher"].split("|")) == {"WebSearch", "WebFetch", "Agent", "Task"}
        else:
            assert "matcher" not in entry, "every subagent counts as running"


def test_the_sweep_gives_the_session_its_caps_and_records_the_counts():
    wf = yaml.safe_load((REPO / ".github" / "workflows" / "tournament-sweep.yml").read_text())
    steps = wf["jobs"]["forecast"]["steps"]
    env = next(s for s in steps if s.get("id") == "claude")["env"]
    # Passed through raw in deep mode, so the defaults live only in search_budget.py;
    # lean mode's cap of 10 sits with its other knobs (tests/test_bot.py checks them).
    assert env["MAX_WEB_SEARCHES"] == (
        "${{ matrix.q.mode == 'lean' && '10' || vars.MAX_WEB_SEARCHES }}"
    )
    assert env["MAX_WEB_SEARCHES_PER_SCOUT"] == "${{ vars.MAX_WEB_SEARCHES_PER_SCOUT }}"
    assert env["SEARCH_BUDGET_FILE"] == "${{ runner.temp }}/search-budget.json"
    usage = next(s for s in steps if s.get("name") == "Record token usage")
    assert '--search-budget "$RUNNER_TEMP/search-budget.json"' in usage["run"]
    upload = next(s for s in steps if s.get("name") == "Upload the dry-run folder")
    assert "${{ runner.temp }}/search-budget.json" in upload["with"]["path"]


def test_the_documented_defaults_are_the_constants():
    doc = (REPO / "docs" / "configuration.md").read_text("utf-8")
    for var, const in (
        ("MAX_WEB_SEARCHES", "DEFAULT_MAX_SEARCHES"),
        ("MAX_WEB_SEARCHES_PER_SCOUT", "DEFAULT_MAX_PER_SCOUT"),
    ):
        row = f"| `{var}` | `{getattr(sb, const)}` (`{const}` in `scripts/search_budget.py`) |"
        assert row in doc, f"docs/configuration.md: {var} default must be {const}"


def test_the_scout_limit_is_the_same_everywhere():
    skill = (REPO / ".claude" / "skills" / "tournament-forecast" / "SKILL.md").read_text()
    assert f"use **up to {sb.MAX_SCOUTS}** (`MAX_SCOUTS`" in skill
    doc = (REPO / "docs" / "configuration.md").read_text("utf-8")
    assert f"`MAX_SCOUTS` = `{sb.MAX_SCOUTS}`" in doc
    words = {5: "five"}
    for rel in ("AGENTS.md", "CLAUDE.md", "SKILLS.md", ".claude/agents/research-scout.md"):
        text = (REPO / rel).read_text("utf-8").lower()
        assert f"up to {sb.MAX_SCOUTS}" in text or f"up to {words[sb.MAX_SCOUTS]}" in text, rel
