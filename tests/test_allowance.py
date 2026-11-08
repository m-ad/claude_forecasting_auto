"""The allowance estimate and the sweep's mode decision (``scripts/allowance.py``).

Table-driven over hand-built usage records, so the parsing of each record shape is
exercised too, plus a replay of MiniBench round 2's real ``ledger/usage.jsonl``: the
acceptance check of issue #21, kept as a test so a retuned rule cannot quietly undo it.
"""

from __future__ import annotations

import datetime as dt
import json
import sys

import allowance as al
import pytest
import tournament_poll as tp
from _common import ledger_records
from conftest import REPO
from record_usage import USAGE

NOW = dt.datetime(2026, 11, 2, 12, 0, tzinfo=dt.UTC)
# 10 allowance points per dollar: every edge below is an exact float.
TEN = {"ALLOWANCE_5H_USD_EQUIV": "10"}


def _ts(minutes_ago: float, now: dt.datetime = NOW) -> str:
    return (now - dt.timedelta(minutes=minutes_ago)).isoformat()


def _epoch(minutes_ahead: float) -> int:
    return int((NOW + dt.timedelta(minutes=minutes_ahead)).timestamp())


def rec(minutes_ago: float, cost: float = 1.0, now: dt.datetime = NOW, **extra) -> dict:
    """A completed session, as record_usage.py writes it."""
    return {
        "ts": _ts(minutes_ago, now),
        "cost_usd_equiv": cost,
        "num_turns": 30,
        "by_model": {"claude-opus-x": cost},
        "conclusion": "success",
        **extra,
    }


def refused(minutes_ago: float, **extra) -> dict:
    """A refused session as the recorder logged it before issue #20: a 1-turn success."""
    return {
        "ts": _ts(minutes_ago),
        "cost_usd_equiv": 0.0,
        "num_turns": 1,
        "by_model": {},
        "conclusion": "success",
        **extra,
    }


def snap(minutes_ago, cost=1.0, window="five_hour", last=None, resets_at=None, **extra):
    """A session carrying issue #20's allowance summary for one window."""
    w = {"first": None, "last": last, "resets_at": resets_at}
    return rec(minutes_ago, cost, allowance={"windows": {window: w}}, **extra)


def decide(records, *, env=None, max_cap=6, override="auto", now=NOW):
    cfg = al.Config.from_env(env or {})
    return al.decide(al.parse_sessions(records), now, cfg, max_cap, override)


# ------------------------------------------------------------ decision table
CASES = [
    # id, records, env, override, (mode, cap, reason)
    ("no snapshot, nothing spent", [], {}, "auto", ("deep", 6, None)),
    # fallback: 8 USD x 6.25 = 50 %; floor(45 / (1.7 x 6.25)) = 4
    ("fallback caps deep", [rec(60, 8.0)], {}, "auto", ("deep", 4, None)),
    ("fallback ignores spend older than 5 h", [rec(301, 50.0), rec(60, 8.0)], {}, "auto",
     ("deep", 4, None)),
    # threshold edges at 10 points per dollar
    ("59 % stays deep", [rec(60, 5.9)], TEN, "auto", ("deep", 2, None)),
    ("60 % is lean", [rec(60, 6.0)], TEN, "auto", ("lean", 5, "allowance_lean")),
    ("94 % has no room for one lean session", [rec(60, 9.4)], TEN, "auto",
     ("lean", 0, "allowance_low")),
    ("95 % stops until the spend ages out", [rec(60, 9.5)], TEN, "auto",
     ("lean", 0, "allowance_exhausted until 2026-11-02T16:00Z")),
    ("a lower stop line from the environment", [rec(60, 8.0)],
     {**TEN, "ALLOWANCE_STOP_5H": "80"}, "auto",
     ("lean", 0, "allowance_exhausted until 2026-11-02T16:00Z")),
    ("a higher lean line from the environment", [rec(60, 6.0)],
     {**TEN, "LEAN_AT_5H": "70"}, "auto", ("deep", 2, None)),
    # stale vs fresh snapshot: a 50 % reading plus $2 spent since (12.5 points)
    ("a snapshot over 5 h old falls back", [snap(360, last=0.5), rec(60, 2.0)], {}, "auto",
     ("deep", 6, None)),
    ("a fresh reading is projected", [snap(240, last=0.5), rec(60, 2.0)], {}, "auto",
     ("lean", 6, "allowance_lean")),
    # a known reset time anchors the fixed window: the $9 before its start is outside
    ("a known reset anchors the window",
     [rec(270, 9.0), snap(200, resets_at=_epoch(60)), rec(30, 2.0)], {}, "auto",
     ("deep", 6, None)),
    # $12 x 6.25 = 75 %: floor(20 / (0.6 x 6.25)) = 5
    ("the same spend without the anchor is lean", [rec(270, 9.0), rec(200), rec(30, 2.0)],
     {}, "auto", ("lean", 5, "allowance_lean")),
    ("a reading whose reset has passed counts 0 from the reset",
     [snap(120, last=0.97, resets_at=_epoch(-30)), rec(10, 1.0)], {}, "auto",
     ("deep", 6, None)),
    # rejected sessions
    ("rejected, reset in the future: no work until then",
     [rec(90), refused(5, rate_limit_events_raw=[
         {"status": "rejected", "rateLimitType": "five_hour", "resetsAt": _epoch(90)}])],
     {}, "auto", ("lean", 0, "allowance_exhausted until 2026-11-02T13:30Z")),
    ("rejected, reset passed: back to normal",
     [refused(60, rate_limit_events_raw=[
         {"status": "rejected", "rateLimitType": "five_hour", "resetsAt": _epoch(-10)}])],
     {}, "auto", ("deep", 6, None)),
    ("usage_limit with the reset only in the window summary",
     [rec(60, 1.0, conclusion="usage_limit", allowance={
         "status": "rejected",
         "windows": {"five_hour": {"last": None, "resets_at": "2026-11-02T13:30:00Z"}}})],
     {}, "auto", ("lean", 0, "allowance_exhausted until 2026-11-02T13:30Z")),
    ("refused with no reset on record: one lean probe", [rec(120, 2.0), refused(30)], {},
     "auto", ("lean", 1, "allowance_refused_probe")),
    ("a probe keeps a forced deep mode", [refused(30)], {}, "deep",
     ("deep", 1, "allowance_refused_probe")),
    ("a stop beats the probe", [rec(120, 16.0), refused(30)], {}, "auto",
     ("lean", 0, "allowance_exhausted until 2026-11-02T15:00Z")),
    ("a success after the refusal ends the probe", [refused(60), rec(30, 1.0)], {}, "auto",
     ("deep", 6, None)),
    # seven-day window: only a reading or a reset time gates it
    ("a 75 % weekly reading is lean",
     [snap(60, window="seven_day", last=0.75, resets_at=_epoch(2 * 24 * 60))], {}, "auto",
     ("lean", 6, "allowance_lean")),
    ("a 98 % weekly reading stops until the weekly reset",
     [snap(60, window="seven_day", last=98.0, resets_at=_epoch(2 * 24 * 60))], {}, "auto",
     ("lean", 0, "allowance_exhausted until 2026-11-04T12:00Z")),
    ("no weekly anchor: a big week does not gate", [rec(2 * 24 * 60, 200.0)], {}, "auto",
     ("deep", 6, None)),
    # overrides
    ("forced deep at 60 %", [rec(60, 6.0)], TEN, "deep", ("deep", 2, None)),
    ("forced lean with room", [], {}, "lean", ("lean", 6, None)),
    ("forced lean still stops", [rec(60, 9.5)], TEN, "lean",
     ("lean", 0, "allowance_exhausted until 2026-11-02T16:00Z")),
    ("an unknown override means auto", [rec(60, 6.0)], TEN, "turbo",
     ("lean", 5, "allowance_lean")),
]


@pytest.mark.parametrize(
    ("records", "env", "override", "expected"),
    [c[1:] for c in CASES],
    ids=[c[0] for c in CASES],
)
def test_decision_table(records, env, override, expected):
    d = decide(records, env=env, override=override)
    assert (d.mode, d.cap, d.reason) == expected
    assert d.exhausted == bool(d.reason and d.reason.startswith("allowance_exhausted"))


def test_the_estimate_names_its_source():
    est = decide([snap(240, last=0.5), rec(60, 2.0)]).windows
    assert (est["five_hour"].source, est["five_hour"].used) == ("reading", 62.5)
    assert (est["seven_day"].source, est["seven_day"].used) == ("none", None)
    assert decide([rec(60, 2.0)]).windows["five_hour"].source == "trailing spend"
    anchored = decide([snap(200, resets_at=_epoch(60))]).windows["five_hour"]
    assert (anchored.source, anchored.resets_at) == ("reset known", NOW + dt.timedelta(hours=1))


# --------------------------------------------------------------- cap arithmetic
def test_the_cap_uses_the_rolling_median_cost_of_the_mode():
    # three labelled lean sessions at $0.5 make room for floor(35 / (0.5 x 10)) = 7
    lean = [rec(400 + i, 0.5, config={"mode": "lean"}) for i in range(3)]
    d = decide([*lean, rec(60, 6.0)], env=TEN, max_cap=10)
    assert (d.mode, d.cost, d.cap) == ("lean", 0.5, 7)
    # with two the prior ($0.6) still stands: floor(35 / 6) = 5
    d = decide([*lean[:2], rec(60, 6.0)], env=TEN, max_cap=10)
    assert (d.cost, d.cap) == (0.6, 5)


def test_the_cap_never_exceeds_max_questions_per_run():
    assert decide([], max_cap=2).cap == 2
    assert decide([], max_cap=99).cap == 8  # floor(95 / (1.7 x 6.25))


def test_mode_cost_counts_only_labelled_paid_sessions():
    sessions = al.parse_sessions(
        [rec(100 + i, c, config={"mode": "deep"}) for i, c in enumerate([1.0, 2.0, 9.0])]
        + [rec(10, 50.0), rec(5, 0.0, config={"mode": "deep"}),
           rec(4, 3.0, config={"mode": "turbo"})]
    )
    assert al.mode_cost(sessions, "deep") == 2.0
    assert al.mode_cost(sessions, "lean") == al.PRIOR_COST["lean"]
    many = al.parse_sessions(
        [rec(1000 - i, float(i), config={"mode": "lean"}) for i in range(1, 31)]
    )
    assert al.mode_cost(many, "lean") == 20.5  # median of the last 20: 11..30


# ----------------------------------------------------------- parsing and scale
@pytest.mark.parametrize(
    ("raw", "pct"), [(0.9, 90.0), (1, 100.0), (90, 90.0), (0, 0.0), (None, None),
                     (-1, None), (True, None), ("90", None)],
)
def test_utilization_up_to_one_is_a_fraction(raw, pct):
    assert al._pct(raw) == pct


@pytest.mark.parametrize(
    "raw",
    [int(NOW.timestamp()), int(NOW.timestamp()) * 1000, "2026-11-02T12:00:00Z",
     "2026-11-02T12:00:00+00:00", "2026-11-02T12:00:00"],
    ids=["unix-seconds", "unix-ms", "iso-z", "iso-offset", "iso-naive"],
)
def test_reset_times_parse_in_every_shape(raw):
    assert al._when(raw) == NOW


@pytest.mark.parametrize("raw", [None, "", "soon", [], True])
def test_unparseable_reset_times_are_unknown(raw):
    assert al._when(raw) is None


def test_old_and_new_refusal_shapes_are_recognised():
    sessions = al.parse_sessions([
        refused(9),
        rec(8, 0.0, conclusion="usage_limit"),
        rec(7, allowance={"rejected": True}),
        rec(6, rate_limit_events_raw=[{"status": "rejected"}]),
        rec(5),  # an ordinary session
        {"ts": _ts(4), "conclusion": "timeout", "parse_failed": True, "cost_usd_equiv": 0.0},
        {"ts": "not a time", "cost_usd_equiv": 5.0},
    ])
    assert [s.refused for s in sessions] == [True, True, True, True, False, False]


def test_raw_events_fill_in_what_the_summary_lacks():
    (s,) = al.parse_sessions([rec(10, rate_limit_events_raw=[
        {"status": "allowed", "rateLimitType": "five_hour", "resetsAt": _epoch(60)},
        {"status": "allowed_warning", "rateLimitType": "five_hour", "utilization": 0.91},
        {"status": "allowed", "rateLimitType": "overage"},
    ], allowance={"windows": {"seven_day": {"last": 40.0, "resets_at": None}}})])
    assert s.windows == {
        "five_hour": (91.0, NOW + dt.timedelta(hours=1)),
        "seven_day": (40.0, None),
    }


@pytest.mark.parametrize("raw", ["0", "-5", "abc", "nan", "inf", ""])
def test_a_bad_variable_keeps_its_default(raw):
    cfg = al.Config.from_env({"ALLOWANCE_5H_USD_EQUIV": raw, "LEAN_AT_7D": raw})
    assert cfg == al.Config()
    assert al.Config.from_env({"ALLOWANCE_5H_USD_EQUIV": "20"}).per_usd("five_hour") == 5.0


def test_the_documented_defaults_are_the_constants():
    doc = (REPO / "docs" / "configuration.md").read_text("utf-8")
    for env, const in (
        (al.ENV_ALLOWANCE_USD, "DEFAULT_ALLOWANCE_USD"),
        (al.ENV_STOP, "DEFAULT_STOP"),
        (al.ENV_LEAN_AT, "DEFAULT_LEAN_AT"),
    ):
        for window, var in env.items():
            value = getattr(al, const)[window]
            row = f"| `{var}` | `{value:g}` (`{const}` in `scripts/allowance.py`) |"
            assert row in doc, f"docs/configuration.md: {var} default must be {value:g}"
    assert f"deep ${al.PRIOR_COST['deep']:g}, lean ${al.PRIOR_COST['lean']:g}" in doc
    assert f"`COST_WINDOW` = `{al.COST_WINDOW}`" in doc
    assert f"`COST_MIN_SAMPLES` = `{al.COST_MIN_SAMPLES}`" in doc


def test_the_summary_names_both_windows_the_mode_and_the_reason():
    text = "\n".join(al.describe(decide([rec(60, 6.0)], env=TEN), al.Config.from_env(TEN)))
    assert "5-hour allowance: 60 % (trailing spend" in text
    assert "7-day allowance: unknown" in text
    assert "Mode: **lean**, cap 5" in text and "reason: allowance_lean" in text


# ------------------------------------------------------------ the gate itself
@pytest.fixture
def gate(monkeypatch, tmp_path):
    """Run tournament_poll.main() offline; returns a function of the usage records."""
    for var in ("FORECAST_MODE", "MAX_QUESTIONS_PER_RUN", "WEEKLY_BUDGET_USD_EQUIV",
                *al.ENV_ALLOWANCE_USD.values(), *al.ENV_STOP.values(),
                *al.ENV_LEAN_AT.values()):
        monkeypatch.delenv(var, raising=False)
    out = tmp_path / "github-output"
    monkeypatch.setenv("GITHUB_OUTPUT", str(out))
    monkeypatch.setenv("GITHUB_STEP_SUMMARY", str(tmp_path / "summary.md"))
    monkeypatch.setattr(tp, "weekly_spend", lambda now: 0.0)
    monkeypatch.setattr(tp, "active_tournaments", lambda: [{"slug": "minibench", "priority": 1}])
    found = [{"post_id": i, "tournament": "minibench", "closes": None, "type": "binary",
              "title": f"Q{i}"} for i in range(1, 9)]
    calls = []

    def whoami():
        calls.append("whoami")
        return {"is_bot": True}

    monkeypatch.setattr(tp.mapi, "whoami", whoami)
    monkeypatch.setattr(tp, "candidates", lambda tours, now, ids: (found, []))

    def run(records, *argv):
        monkeypatch.setattr(tp.allowance, "load_sessions", lambda: al.parse_sessions(records))
        monkeypatch.setattr(sys, "argv", ["tournament_poll.py", "--github-output", *argv])
        out.write_text("")
        tp.main()
        values = dict(line.split("=", 1) for line in out.read_text().splitlines())
        return values, calls, (tmp_path / "summary.md").read_text()

    return run


def test_the_gate_tags_every_question_with_the_mode_and_caps_the_run(gate):
    now = dt.datetime.now(dt.UTC)
    values, calls, summary = gate([rec(30, 13.0, now=now)])  # 81 %: lean, room for 3
    questions = json.loads(values["questions"])
    assert [q["mode"] for q in questions] == ["lean"] * 3
    assert [q["post_id"] for q in questions] == [1, 2, 3], "soonest-closing first"
    assert (values["mode"], values["reason"], values["exhausted_until"]) == (
        "lean", "allowance_lean", ""
    )
    assert "5-hour allowance: 81 %" in summary and "Mode: **lean**, cap 3" in summary
    assert calls == ["whoami"]


def test_the_gate_stops_before_calling_metaculus_when_exhausted(gate):
    now = dt.datetime.now(dt.UTC)
    values, calls, summary = gate([rec(30, 20.0, now=now)])
    assert values["has_work"] == "false" and values["questions"] == "[]"
    assert values["reason"].startswith("allowance_exhausted until ")
    assert values["exhausted_until"], "the bot-health job keys its one comment on it"
    assert calls == [], "no Metaculus call while the allowance is out"
    assert "**No work: allowance_exhausted until" in summary


def test_the_mode_flag_overrides_the_variable(gate, monkeypatch, capsys):
    monkeypatch.setenv("FORECAST_MODE", "lean")
    values, _, _ = gate([])
    assert {q["mode"] for q in json.loads(values["questions"])} == {"lean"}
    values, _, _ = gate([], "--mode", "deep")
    assert values["mode"] == "deep"
    monkeypatch.setenv("FORECAST_MODE", "turbo")
    values, _, _ = gate([])
    assert values["mode"] == "deep" and "is not one of" in capsys.readouterr().out


# --------------------------------------------------------- round 2, replayed
ROUND_2 = al.Config(
    allowance_usd={"five_hour": 16.0, "seven_day": 100.0},
    stop={"five_hour": 95.0, "seven_day": 98.0},
    lean_at={"five_hour": 60.0, "seven_day": 75.0},
)


def test_round_two_replayed_leans_before_each_refusal_and_never_bursts():
    """Issue #21's acceptance check over the real ledger.

    Each refusal episode of 2026-11-02 began after a run the new gate would have run
    lean or stopped, every refusing run gets at most the one probe, and the 11-session
    catch-up at 07:08 gets one session instead of eleven. The replay sees only records
    written before each gate, so the append-only ledger keeps the result fixed.
    """
    since = dt.datetime(2026, 11, 2, tzinfo=dt.UTC)
    until = dt.datetime(2026, 11, 3, tzinfo=dt.UTC)
    rows = [r for r in al.replay(ledger_records(USAGE), ROUND_2, 11, since) if r["gate"] < until]
    by_time = {al._iso(r["gate"]): r for r in rows}
    assert by_time["2026-11-02T04:07Z"]["mode"] == "lean", "lean before the 05:07 refusals"
    assert by_time["2026-11-02T07:08Z"]["started"] == 11
    assert by_time["2026-11-02T07:08Z"]["cap"] <= 1, "the burst becomes one probe"
    assert by_time["2026-11-02T14:08Z"]["cap"] == 0, "stopped before the 15:07 refusals"
    for r in rows:
        if r["refused"]:
            assert r["cap"] <= 1, f"{al._iso(r['gate'])}: refusals met a cap of {r['cap']}"
