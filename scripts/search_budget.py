#!/usr/bin/env python3
"""Hook: cap ``WebSearch`` and research-scouts per session, and track running scouts.

Registered in ``.claude/settings.ci.json`` as a ``PreToolUse`` hook for
``WebSearch|WebFetch|Agent|Task`` and as a ``SubagentStart`` / ``SubagentStop`` hook,
so it runs for every web call and spawn of the forecaster session and of its
research-scouts. One session once billed 234 searches (issue #19): five scouts searched
in parallel and nothing stopped them. The caps turn that into refusals the model can
read and act on.

Behaviour, per call:

- ``WebFetch`` is counted, never refused. Fetching is how a forecast gets its numbers
  from the source rather than a snippet; the cap is on finding pages, not reading them.
- ``Agent`` (``Task`` is its old name) from the main agent spawns a subagent; beyond
  ``MAX_SCOUTS`` spawns per session it is refused, so the per-scout allowances below
  always fit inside the session cap.
- ``WebSearch`` is counted against ``$MAX_WEB_SEARCHES`` (unset or empty:
  ``DEFAULT_MAX_SEARCHES``) for the whole session. A call from a subagent -- the hook
  input names it in ``agent_id``, which the CLI sends since 2.1.69 (its changelog; the
  2.1.317 binary checked 2026-11-03) -- is also counted against
  ``$MAX_WEB_SEARCHES_PER_SCOUT`` (unset or empty: ``DEFAULT_MAX_PER_SCOUT``) for that
  scout, and the scouts together never take the last ``$MAX_WEB_SEARCHES_PER_SCOUT``
  searches of the session that the main agent has not used yet: that share is reserved
  for the main agent's resolution source and disconfirmation searches. The main agent
  itself has no per-agent cap and may use whatever the session has left. On a CLI
  without ``agent_id`` only the session cap binds; ``no_agent_id`` in the budget file
  counts the searches that came without one, and an empty ``by_agent`` in a session that
  spawned scouts means the per-scout cap was not in force.
- An agent's first search is allowed with a note stating the caps, so the model
  learns the budget from the hook rather than from numbers copied into its
  instructions. From ``NUDGE_SHARE`` of a cap the call is allowed with a countdown
  (``additionalContext``); at the cap it is refused with a reason that tells the model
  what to do instead. ``0`` disables a search cap.
- ``SubagentStart`` / ``SubagentStop`` keep ``active_agents``, the subagents still
  running, and ``subagents_started`` counts the start events. A forecast logged with no
  subagent running proves nothing if the start events never arrived; equal
  ``subagents_started`` and ``scouts_spawned``, and no subagent left running at exit,
  show that both events reach the hook. ``log_forecast.py`` refuses a one-shot forecast while any is, outside its
  deadline waiver: the skill's "do not log before every scout has reported" is then a
  rule the code keeps, not one the model has to remember after a refusal told it to log.

These defaults are the only place the numbers live: the sweep passes the repository
variables through unset, and ``docs/configuration.md`` names the constants (a test
keeps its Default column in step with them).

State lives in ``$SEARCH_BUDGET_FILE``, a JSON object. Scouts call in parallel, so
every update holds ``flock`` on a sibling ``.lock`` file and replaces the data file
atomically (write a temporary file, ``os.replace``): a session killed mid-write leaves
the previous state, never an empty or half-written file. A file with wrongly typed
fields is repaired field by field (``normalise``) rather than trusted or discarded.
``log_forecast.py`` reads it to waive the research floor once the session cap is used
(a cap below the floor must never trap a session) and to see running scouts, and
``record_usage.py`` copies its counts into ``ledger/usage.jsonl``.

The hook fails open: without ``$SEARCH_BUDGET_FILE``, or on any error, it allows the
call and says why on stderr. It is a cost control, not a security boundary -- the
session's ``uv run python`` can rewrite the file. It runs with the project's
virtualenv interpreter (``.venv/bin/python -I``), so it gets the Python version the
project declares, not whatever the runner's system ``python3`` is; it uses only the
standard library.

The counts are of **tool calls**. Billing counts server-side search requests, and one
``WebSearch`` call can issue several (``web_searches`` in the usage record), so the
ratio of the two is what to tune the cap with.
"""

from __future__ import annotations

import datetime as dt
import fcntl
import json
import math
import os
import sys
from pathlib import Path
from typing import Any

DEFAULT_MAX_SEARCHES = 50
DEFAULT_MAX_PER_SCOUT = 8
# MAX_SCOUTS scouts at DEFAULT_MAX_PER_SCOUT each, plus the main agent's reserved share
# of one scout's allowance, fit inside DEFAULT_MAX_SEARCHES (tests/test_search_budget.py
# checks it), so no scout is cut off by the session cap before its own.
MAX_SCOUTS = 5
NUDGE_SHARE = 0.8
SPAWN_TOOLS = ("Agent", "Task")

_COUNTS = (
    "searches", "fetches", "denied", "no_agent_id", "scouts_spawned", "subagents_started"
)


def _cap(name: str, default: int) -> int:
    """A non-negative integer from the environment; ``default`` if unset or malformed."""
    try:
        value = int(os.environ.get(name, "").strip())
    except ValueError:
        return default
    return value if value >= 0 else default


def caps() -> tuple[int, int]:
    """``(session cap, per-scout cap)`` from the environment; 0 means no cap."""
    return (
        _cap("MAX_WEB_SEARCHES", DEFAULT_MAX_SEARCHES),
        _cap("MAX_WEB_SEARCHES_PER_SCOUT", DEFAULT_MAX_PER_SCOUT),
    )


def budget_path() -> Path | None:
    """The budget file named by ``$SEARCH_BUDGET_FILE``, or None when unset."""
    raw = os.environ.get("SEARCH_BUDGET_FILE", "").strip()
    return Path(raw) if raw else None


def _lock_path(path: Path) -> Path:
    return path.with_name(path.name + ".lock")


def _empty_state() -> dict[str, Any]:
    return {
        **dict.fromkeys(_COUNTS, 0),
        "by_agent": {},
        "active_agents": {},
        "cap_reached_at": None,
    }


def _count(value: Any) -> int:
    """``value`` if it is a non-negative integer, else 0."""
    ok = isinstance(value, int) and not isinstance(value, bool) and value >= 0
    return value if ok else 0


def normalise(raw: Any) -> dict[str, Any]:
    """A well-typed state from whatever the file held; bad fields fall back to empty.

    Field by field rather than all or nothing: one field a session's ``uv run python``
    wrote as ``null`` must not crash every later hook call (the hook would fail open
    for the rest of the session) nor wipe the counts that are still good.
    """
    state = _empty_state()
    if not isinstance(raw, dict):
        return state
    for key in _COUNTS:
        state[key] = _count(raw.get(key))
    for key in ("max_searches", "max_per_scout"):
        if key in raw:
            state[key] = _count(raw[key])
    if isinstance(raw.get("by_agent"), dict):
        state["by_agent"] = {
            str(k): {"searches": _count(v.get("searches")), "fetches": _count(v.get("fetches"))}
            for k, v in raw["by_agent"].items()
            if isinstance(v, dict)
        }
    if isinstance(raw.get("active_agents"), dict):
        state["active_agents"] = {str(k): str(v) for k, v in raw["active_agents"].items()}
    if isinstance(raw.get("cap_reached_at"), str):
        state["cap_reached_at"] = raw["cap_reached_at"]
    return state


def read_state(path: Path | None = None) -> dict[str, Any] | None:
    """The budget file's state, normalised; None only if there is no file.

    An existing file that cannot be parsed comes back as an empty state with
    ``unreadable: True``, so a reader can tell "the hook never ran" from "the hook ran
    and its file is damaged".
    """
    path = path or budget_path()
    if path is None:
        return None
    try:
        text = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return None
    except OSError:
        return {**_empty_state(), "unreadable": True}
    try:
        raw = json.loads(text)
    except ValueError:
        raw = None
    if not isinstance(raw, dict):
        return {**_empty_state(), "unreadable": True}
    return normalise(raw)


def session_cap_used(state: dict[str, Any] | None) -> bool:
    """Whether the session-wide search cap has been reached."""
    if not state:
        return False
    state = normalise(state)
    cap = state.get("max_searches", 0)
    return cap > 0 and state["searches"] >= cap


def running_agents(state: dict[str, Any] | None) -> dict[str, str]:
    """The subagents started and not yet stopped: ``{agent_id: agent_type}``."""
    return normalise(state)["active_agents"] if state else {}


def _nudge(used: int, cap: int) -> bool:
    return cap > 0 and used >= math.ceil(NUDGE_SHARE * cap)


def _scout_ceiling(state: dict[str, Any], max_searches: int, max_per_scout: int) -> int:
    """Session searches the scouts may reach: the cap less the main agent's unused share."""
    reserve = max(0, max_per_scout - state["no_agent_id"]) if max_per_scout else 0
    return max_searches - reserve


def _budget_note(max_searches: int, max_per_scout: int) -> str:
    session = f"{max_searches} WebSearch calls this session" if max_searches else "no session cap"
    scout = f"{max_per_scout} per scout" if max_per_scout else "no per-scout cap"
    reserve = (
        f"; the scouts leave the main agent at least {max_per_scout} of them"
        if max_searches and max_per_scout
        else ""
    )
    return (
        f"Search budget: {session}, {scout}, at most {MAX_SCOUTS} scouts{reserve}; "
        "WebFetch is not capped."
    )


def decide(
    state: dict[str, Any],
    tool: str,
    agent_id: str | None,
    max_searches: int,
    max_per_scout: int,
    now: str,
) -> dict[str, Any] | None:
    """Update ``state`` in place for one ``PreToolUse`` call; return the hook output.

    Parameters
    ----------
    state
        The budget file's content (``normalise`` shape); mutated.
    tool
        ``WebSearch``, ``WebFetch`` or ``Agent``/``Task``; anything else passes uncounted.
    agent_id
        The calling subagent, or None for the main agent (or a CLI that does not say).
    max_searches, max_per_scout
        The search caps; 0 disables one.
    now
        Timestamp recorded when the session cap is first reached.

    Returns
    -------
    dict or None
        ``hookSpecificOutput`` JSON for the CLI: a refusal, or an allowed call with a
        note. None means allow silently.
    """
    state.update({k: v for k, v in normalise(state).items() if k not in state})
    state["max_searches"], state["max_per_scout"] = max_searches, max_per_scout
    agent = None
    if agent_id:
        agent = state["by_agent"].setdefault(agent_id, {"searches": 0, "fetches": 0})

    if tool in SPAWN_TOOLS:
        if agent is not None:
            return None
        if state["scouts_spawned"] >= MAX_SCOUTS:
            state["denied"] += 1
            return _deny(
                f"Scout limit reached ({state['scouts_spawned']}/{MAX_SCOUTS} subagents "
                "spawned this session). Fold this brief into your own research instead."
            )
        state["scouts_spawned"] += 1
        return None
    if tool == "WebFetch":
        state["fetches"] += 1
        if agent is not None:
            agent["fetches"] += 1
        return None
    if tool != "WebSearch":
        return None

    if agent is None and max_searches and state["searches"] >= max_searches:
        state["denied"] += 1
        return _deny(
            f"Search budget used ({state['searches']}/{max_searches} WebSearch calls this "
            "session). Stop searching. WebFetch still works for a page you already found "
            "whose exact figure the forecast rests on. Mark planned searches you did not "
            "run as skipped in the research log. Wait until every scout has reported "
            "(log_forecast.py refuses while one is still running, except close to the "
            "deadline), then integrate, write forecast.md and log -- the research floor "
            "is waived."
        )
    if agent is not None and max_searches:
        ceiling = _scout_ceiling(state, max_searches, max_per_scout)
        if state["searches"] >= ceiling:
            state["denied"] += 1
            return _deny(
                f"The scouts' share of the session search budget is used "
                f"({state['searches']}/{max_searches}; the rest is reserved for the main "
                "agent). Stop searching and return your digest now with what you have."
            )
    if agent is not None and max_per_scout and agent["searches"] >= max_per_scout:
        state["denied"] += 1
        return _deny(
            f"Your search budget is used ({agent['searches']}/{max_per_scout} WebSearch "
            "calls for this scout). Stop searching: fetch at most the pages you already "
            "found that your brief needs, then return your digest now."
        )

    state["searches"] += 1
    if agent is not None:
        agent["searches"] += 1
    else:
        state["no_agent_id"] += 1
    if max_searches and state["searches"] >= max_searches and not state["cap_reached_at"]:
        state["cap_reached_at"] = now

    notes = []
    first = agent["searches"] == 1 if agent is not None else state["no_agent_id"] == 1
    if first:
        notes.append(_budget_note(max_searches, max_per_scout))
    # The session countdown goes to the main agent only: a scout's ceiling is lower (the
    # main agent's reserve) and its next step is its own brief, not the session's streams.
    if agent is None and _nudge(state["searches"], max_searches):
        notes.append(
            f"{state['searches']}/{max_searches} WebSearch calls of the session budget used, "
            f"{max_searches - state['searches']} left: spend them on the resolution source, "
            "markets and the disconfirmation search."
        )
    if agent is not None and _nudge(agent["searches"], max_per_scout):
        notes.append(
            f"This scout has used {agent['searches']}/{max_per_scout} of its WebSearch calls."
        )
    if not notes:
        return None
    return {
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "additionalContext": " ".join(notes),
        }
    }


def track(state: dict[str, Any], event: str, agent_id: str, agent_type: str) -> None:
    """Record a ``SubagentStart`` / ``SubagentStop`` in ``state["active_agents"]``.

    Every start event is counted in ``subagents_started``, a resumed subagent's again.
    """
    if not agent_id:
        return
    if event == "SubagentStart":
        state["subagents_started"] += 1
        state["active_agents"][agent_id] = agent_type
    elif event == "SubagentStop":
        state["active_agents"].pop(agent_id, None)


def _deny(reason: str) -> dict[str, Any]:
    return {
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": reason,
        }
    }


def _write_atomic(path: Path, state: dict[str, Any]) -> None:
    tmp = path.with_name(f".{path.name}.{os.getpid()}.tmp")
    try:
        tmp.write_text(json.dumps(state, sort_keys=True), encoding="utf-8")
        os.replace(tmp, path)
    finally:
        tmp.unlink(missing_ok=True)


def run(hook_input: dict[str, Any], path: Path) -> dict[str, Any] | None:
    """Apply one hook call to the budget file at ``path`` under an exclusive lock."""
    max_searches, max_per_scout = caps()
    agent_id = str(hook_input.get("agent_id") or "") or None
    event = str(hook_input.get("hook_event_name") or "PreToolUse")
    now = dt.datetime.now(dt.UTC).isoformat(timespec="seconds")
    path.parent.mkdir(parents=True, exist_ok=True)
    # The lock lives on its own file: os.replace swaps the data file's inode, so a lock
    # held on the data file itself would not exclude the next writer.
    with open(_lock_path(path), "a", encoding="utf-8") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        try:
            text = path.read_text(encoding="utf-8")
        except FileNotFoundError:
            text = ""
        try:
            raw = json.loads(text) if text.strip() else None
        except ValueError:
            # Unparseable (hand-edited): start over rather than block every call.
            raw = None
        state = normalise(raw)
        if event in ("SubagentStart", "SubagentStop"):
            track(state, event, agent_id or "", str(hook_input.get("agent_type") or ""))
            out = None
        else:
            out = decide(
                state, str(hook_input.get("tool_name") or ""), agent_id,
                max_searches, max_per_scout, now,
            )
        _write_atomic(path, state)
    return out


def main() -> None:
    path = budget_path()
    if path is None:
        print("search_budget: $SEARCH_BUDGET_FILE unset, not counting", file=sys.stderr)
        return
    try:
        hook_input = json.load(sys.stdin)
        out = run(hook_input if isinstance(hook_input, dict) else {}, path)
    except Exception as exc:  # noqa: BLE001 -- fail open: a broken counter must not stop research
        print(f"search_budget: failing open: {exc!r}", file=sys.stderr)
        return
    if out is not None:
        print(json.dumps(out))


if __name__ == "__main__":
    main()
