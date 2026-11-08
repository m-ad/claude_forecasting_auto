#!/usr/bin/env python3
"""Estimate the Claude subscription allowance left, and decide the sweep's research mode.

Read by the sweep gate (``scripts/tournament_poll.py``) before any model starts. Pure
Python over ``ledger/usage.jsonl``: no network, no token. MiniBench round 2 lost 21 of 59
questions because the gate kept starting full-depth sessions until the subscription
refused them; one catch-up run started 11 at once and used a whole 5-hour window in
12 minutes (issue #21). Cheap forecasts score far better than none, so as the allowance
runs low the gate switches to ``lean`` sessions, caps how many it starts, and stops
before the refusal.

Estimate, per window (``five_hour``, ``seven_day``), in percent of the window:

1. **A reading.** The newest usage record carrying the window's ``utilization``, at most
   one window length old: ``u = reading + spend since × allowance_per_usd``.
2. **A reset time without a reading.** The window is fixed (it ends at ``resets_at``),
   so ``u = spend inside it × allowance_per_usd``.
3. **A reset that has passed.** The window counts as 0 from the reset, plus what was
   spent since.
4. **Nothing.** Five-hour: ``u = trailing-5h spend × allowance_per_usd`` (the fallback,
   conservative: a trailing sum always contains the real window's share). Seven-day:
   unknown, so it does not gate. A trailing 7-day sum would block for days after the
   real reset: round 2's weekly window reset on 2026-11-03 around 23:00, while the
   trailing sum stayed above the stop line until 2026-11-09.

``allowance_per_usd`` is ``100 / ALLOWANCE_<5H|7D>_USD_EQUIV``: the API-equivalent
dollars one full window holds. Spend is attributed to a record's ``ts`` (the end of
its session). Interactive Claude use draws on the same allowance and is invisible
here; the defaults are the lowest caps round 2 observed for that reason.

Decision, first match wins:

| Condition | Decision |
|---|---|
| the newest session was refused and the reset is known and in the future | no work, ``allowance_exhausted until <reset>`` |
| ``u5 >= ALLOWANCE_STOP_5H`` or ``u7 >= ALLOWANCE_STOP_7D`` | no work, ``allowance_exhausted until <when u falls below>`` |
| ``u5 >= LEAN_AT_5H`` or ``u7 >= LEAN_AT_7D`` | ``lean`` |
| otherwise | ``deep`` |

Then the cap: ``min(max_cap, floor((stop - u) / (cost_mode × allowance_per_usd)))``
for each window that has an estimate, where ``cost_mode`` is the rolling median cost of
that mode's sessions (``PRIOR_COST`` until there are ``COST_MIN_SAMPLES``). A newest
session that was refused with no known reset (every refusal before issue #20's capture)
leaves one ``lean`` probe per sweep rather than a full batch of refusals.

What a usage record may carry (issue #20; every field optional, older records have
none): ``allowance.windows.<window>`` with ``last`` (else ``first``) and ``resets_at``;
``allowance.status`` / ``allowance.rejected``; ``rate_limit_events_raw``, the CLI's
verbatim ``rate_limit_info`` dicts (``status``, ``rateLimitType``, ``utilization``,
``resetsAt``); ``conclusion: "usage_limit"``; and ``config.mode``. A record with
``by_model == {}``, at most one turn and zero cost is a refusal the old recorder logged
as a success.

Scale: the CLI's ``utilization`` is a fraction and its ``resetsAt`` Unix seconds
(Claude Code 2.1.110, the last release shipped as JavaScript, checked 2026-11-08: it
prints ``Math.floor(utilization * 100)`` and builds ``new Date(resetsAt * 1000)``); the
SDK's usage probe reports percent and ISO-8601 times. So a value up to 1 is read as a
fraction and a larger one as percent. The CLI only reports a reading at its warning
thresholds (5 h: 90 %; 7 d: 25, 50, 75 %), which keeps percent readings above 1.

Examples
--------
    uv run scripts/allowance.py                     # the decision a sweep would make now
    uv run scripts/allowance.py replay --since 2026-11-02 --max 11
"""

from __future__ import annotations

import argparse
import datetime as dt
import math
import os
import statistics
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common import ledger_records
from record_usage import USAGE

FIVE_HOUR = "five_hour"
SEVEN_DAY = "seven_day"
WINDOW_LENGTH = {FIVE_HOUR: dt.timedelta(hours=5), SEVEN_DAY: dt.timedelta(days=7)}
MODES = ("deep", "lean")
OVERRIDES = ("auto", *MODES)

# Defaults of the repository variables, kept here only: the gate passes them through
# unset. Round 2 (2026-11-02/03) was refused after $16-24 of API-equivalent spend in a
# 5-hour window, and after about $100 in the week.
DEFAULT_ALLOWANCE_USD = {FIVE_HOUR: 16.0, SEVEN_DAY: 100.0}
DEFAULT_STOP = {FIVE_HOUR: 95.0, SEVEN_DAY: 98.0}
DEFAULT_LEAN_AT = {FIVE_HOUR: 60.0, SEVEN_DAY: 75.0}
ENV_ALLOWANCE_USD = {FIVE_HOUR: "ALLOWANCE_5H_USD_EQUIV", SEVEN_DAY: "ALLOWANCE_7D_USD_EQUIV"}
ENV_STOP = {FIVE_HOUR: "ALLOWANCE_STOP_5H", SEVEN_DAY: "ALLOWANCE_STOP_7D"}
ENV_LEAN_AT = {FIVE_HOUR: "LEAN_AT_5H", SEVEN_DAY: "LEAN_AT_7D"}

# Round 2's deep sessions cost a median of about $1.7; round 1's sessions without scouts,
# about 4 searches each, $0.55. Used until a mode has COST_MIN_SAMPLES sessions of its own.
PRIOR_COST = {"deep": 1.7, "lean": 0.6}
COST_WINDOW = 20
COST_MIN_SAMPLES = 3


def _number(value: Any) -> float | None:
    if isinstance(value, bool) or not isinstance(value, (int, float)) or math.isnan(value):
        return None
    return float(value)


def _pct(value: Any) -> float | None:
    """A utilization reading in percent: a value up to 1 is a fraction (see the module doc)."""
    num = _number(value)
    if num is None or num < 0:
        return None
    return num * 100 if num <= 1 else num


def _when(value: Any) -> dt.datetime | None:
    """A UTC instant from Unix seconds (or milliseconds) or an ISO-8601 string."""
    num = _number(value)
    if num is not None:
        # Milliseconds are 1000x larger; no Unix-seconds reset lies beyond the year 5000.
        return dt.datetime.fromtimestamp(num / 1000 if num > 1e11 else num, dt.UTC)
    if not isinstance(value, str) or not value.strip():
        return None
    try:
        out = dt.datetime.fromisoformat(value.strip())
    except ValueError:
        return None
    return out if out.tzinfo else out.replace(tzinfo=dt.UTC)


def _iso(when: dt.datetime | None) -> str:
    return when.astimezone(dt.UTC).strftime("%Y-%m-%dT%H:%MZ") if when else "-"


# ------------------------------------------------------------------- sessions
@dataclass(frozen=True)
class Session:
    """What the allowance estimate needs from one ``ledger/usage.jsonl`` line."""

    ts: dt.datetime
    cost: float
    mode: str | None = None
    refused: bool = False
    # A known reset of the window that refused the session (future or past).
    refused_until: dt.datetime | None = None
    # window -> (utilization in percent or None, resets_at or None)
    windows: dict[str, tuple[float | None, dt.datetime | None]] = field(default_factory=dict)


def _windows(rec: dict[str, Any]) -> dict[str, tuple[float | None, dt.datetime | None]]:
    """Per-window reading and reset time; the summary (``allowance.windows``) wins."""
    out: dict[str, tuple[float | None, dt.datetime | None]] = {}
    for event in rec.get("rate_limit_events_raw") or []:
        if not isinstance(event, dict) or event.get("rateLimitType") not in WINDOW_LENGTH:
            continue
        name = event["rateLimitType"]
        util, reset = out.get(name, (None, None))
        new_util = _pct(event.get("utilization"))
        out[name] = (util if new_util is None else new_util, _when(event.get("resetsAt")) or reset)
    allowance = rec.get("allowance") if isinstance(rec.get("allowance"), dict) else {}
    windows = allowance.get("windows") if isinstance(allowance.get("windows"), dict) else {}
    for name, w in windows.items():
        if name not in WINDOW_LENGTH or not isinstance(w, dict):
            continue
        util, reset = out.get(name, (None, None))
        reading = _pct(w.get("last") if w.get("last") is not None else w.get("first"))
        out[name] = (util if reading is None else reading, _when(w.get("resets_at")) or reset)
    return out


def _refusal(rec: dict[str, Any]) -> tuple[bool, dt.datetime | None]:
    """Whether the session was refused for the allowance, and the reset if the record says."""
    allowance = rec.get("allowance") if isinstance(rec.get("allowance"), dict) else {}
    rejected = [
        e for e in rec.get("rate_limit_events_raw") or []
        if isinstance(e, dict) and e.get("status") == "rejected"
    ]
    refused = (
        bool(rejected)
        or rec.get("conclusion") == "usage_limit"
        or allowance.get("rejected") is True
        or allowance.get("status") == "rejected"
        # Before issue #20 a refused session was recorded as a one-turn, zero-cost success.
        or (
            rec.get("by_model") == {}
            and _number(rec.get("num_turns")) is not None
            and (_number(rec.get("num_turns")) or 0) <= 1
            and not _number(rec.get("cost_usd_equiv"))
        )
    )
    until = _when(rejected[-1].get("resetsAt")) if rejected else None
    return refused, until or _when(allowance.get("resets_at"))


def parse_sessions(records: list[dict[str, Any]]) -> list[Session]:
    """Usage records as sessions, oldest first; lines without a parseable ``ts`` are skipped."""
    out: list[Session] = []
    for rec in records:
        ts = _when(rec.get("ts"))
        if ts is None:
            continue
        refused, until = _refusal(rec)
        config = rec.get("config") if isinstance(rec.get("config"), dict) else {}
        out.append(
            Session(
                ts=ts,
                cost=max(_number(rec.get("cost_usd_equiv")) or 0.0, 0.0),
                mode=config.get("mode") if config.get("mode") in MODES else None,
                refused=refused,
                refused_until=until,
                windows=_windows(rec),
            )
        )
    out.sort(key=lambda s: s.ts)
    return out


def load_sessions(path: Path = USAGE) -> list[Session]:
    return parse_sessions(ledger_records(path))


def _spend(sessions: list[Session], start: dt.datetime, end: dt.datetime) -> float:
    """API-equivalent spend of the sessions that ended in ``(start, end]``."""
    return sum(s.cost for s in sessions if start < s.ts <= end)


def mode_cost(sessions: list[Session], mode: str) -> float:
    """Rolling median cost of a ``mode`` session; ``PRIOR_COST`` until there are enough.

    Only sessions labelled with the mode count: before the label existed every session
    ran today's deep workflow except round 1's first, scout-less ones, which cost a lean
    session's price, so unlabelled history would blur the two.
    """
    costs = [s.cost for s in sessions if s.mode == mode and s.cost > 0][-COST_WINDOW:]
    return statistics.median(costs) if len(costs) >= COST_MIN_SAMPLES else PRIOR_COST[mode]


# ------------------------------------------------------------------- config
def _env_float(env: dict[str, str], name: str, default: float) -> float:
    try:
        value = float(env.get(name, "").strip())
    except ValueError:
        return default
    return value if value > 0 and math.isfinite(value) else default


@dataclass(frozen=True)
class Config:
    """Allowance sizes (API-equivalent USD per full window) and thresholds (percent)."""

    allowance_usd: dict[str, float] = field(default_factory=lambda: dict(DEFAULT_ALLOWANCE_USD))
    stop: dict[str, float] = field(default_factory=lambda: dict(DEFAULT_STOP))
    lean_at: dict[str, float] = field(default_factory=lambda: dict(DEFAULT_LEAN_AT))

    @classmethod
    def from_env(cls, env: dict[str, str] | None = None) -> Config:
        """The repository variables; an unset, malformed or non-positive one keeps its default."""
        env = dict(os.environ if env is None else env)
        return cls(
            allowance_usd={
                w: _env_float(env, ENV_ALLOWANCE_USD[w], DEFAULT_ALLOWANCE_USD[w])
                for w in WINDOW_LENGTH
            },
            stop={w: _env_float(env, ENV_STOP[w], DEFAULT_STOP[w]) for w in WINDOW_LENGTH},
            lean_at={w: _env_float(env, ENV_LEAN_AT[w], DEFAULT_LEAN_AT[w]) for w in WINDOW_LENGTH},
        )

    def per_usd(self, window: str) -> float:
        """Allowance points (percent of the window) one API-equivalent dollar uses."""
        return 100.0 / self.allowance_usd[window]


# ------------------------------------------------------------------- estimate
@dataclass(frozen=True)
class WindowEstimate:
    """One window's projected utilization, in percent; ``used`` None means unknown."""

    window: str
    used: float | None
    source: str  # "reading", "reset known", "reset passed", "trailing spend", "none"
    resets_at: dt.datetime | None = None
    # When ``used`` falls below the stop line if nothing more is spent.
    clears_at: dt.datetime | None = None


def _age_out(
    sessions: list[Session],
    start: dt.datetime,
    now: dt.datetime,
    per: float,
    stop: float,
    length: dt.timedelta,
) -> dt.datetime:
    """When the spend since ``start`` falls below ``stop`` as sessions leave the window.

    A session leaves a trailing window ``length`` after it ended; nothing new is spent
    meanwhile, because the gate starts nothing while the window is over the line.
    """
    inside = [s for s in sessions if start < s.ts <= now]
    total = sum(s.cost for s in inside)
    for s in inside:
        if total * per < stop:
            break
        total -= s.cost
        if total * per < stop:
            return s.ts + length
    return now


def estimate_window(
    sessions: list[Session], now: dt.datetime, window: str, cfg: Config
) -> WindowEstimate:
    """Project ``window``'s utilization to ``now`` (cases 1-4 of the module doc)."""
    length, per, stop = WINDOW_LENGTH[window], cfg.per_usd(window), cfg.stop[window]
    snaps = [s for s in sessions if s.ts <= now and window in s.windows]
    snap = snaps[-1] if snaps and now - snaps[-1].ts <= length else None
    util, reset = snap.windows[window] if snap else (None, None)
    if snap and reset is not None and reset <= now and now - reset < length:
        used = _spend(sessions, reset, now) * per
        clears = _age_out(sessions, reset, now, per, stop, length)
        return WindowEstimate(window, used, "reset passed", reset, clears)
    if snap and util is not None and (reset is None or reset > now):
        used = util + _spend(sessions, snap.ts, now) * per
        return WindowEstimate(window, used, "reading", reset, reset or snap.ts + length)
    if snap and reset is not None and reset > now:
        used = _spend(sessions, reset - length, now) * per
        return WindowEstimate(window, used, "reset known", reset, reset)
    if window == FIVE_HOUR:
        start = now - length
        used = _spend(sessions, start, now) * per
        clears = _age_out(sessions, start, now, per, stop, length)
        return WindowEstimate(window, used, "trailing spend", None, clears)
    return WindowEstimate(window, None, "none")


# ------------------------------------------------------------------- decision
@dataclass(frozen=True)
class Decision:
    """What the gate does this sweep."""

    mode: str  # the mode the sessions run in: "deep" or "lean"
    cap: int  # at most this many sessions
    reason: str | None  # None when the allowance does not restrict the sweep
    until: dt.datetime | None = None  # set when exhausted: no work before then
    windows: dict[str, WindowEstimate] = field(default_factory=dict)
    cost: float = 0.0  # cost_mode used for the cap

    @property
    def exhausted(self) -> bool:
        return self.until is not None


def decide(
    sessions: list[Session],
    now: dt.datetime,
    cfg: Config,
    max_cap: int,
    override: str = "auto",
) -> Decision:
    """The sweep's mode and cap from the allowance estimate (the module doc's table).

    ``override`` (``FORECAST_MODE``) fixes the mode; the stop rules and the cap still
    apply, so a forced deep sweep never starts sessions the allowance would refuse.
    """
    override = override if override in OVERRIDES else "auto"
    est = {w: estimate_window(sessions, now, w, cfg) for w in WINDOW_LENGTH}
    latest = next((s for s in reversed(sessions) if s.ts <= now), None)
    refused = latest is not None and latest.refused

    def stopped(until: dt.datetime) -> Decision:
        mode = override if override in MODES else "lean"
        reason = f"allowance_exhausted until {_iso(until)}"
        return Decision(mode, 0, reason, until, est, mode_cost(sessions, mode))

    if refused:
        known = latest.refused_until or min(
            (e.resets_at for e in est.values() if e.resets_at and e.resets_at > now),
            default=None,
        )
        if known and known > now:
            return stopped(known)
    over = [e for e in est.values() if e.used is not None and e.used >= cfg.stop[e.window]]
    if over:
        return stopped(max(e.clears_at or now for e in over))

    tight = any(
        e.used is not None and e.used >= cfg.lean_at[e.window] for e in est.values()
    )
    # Refused with no reset on record: one probe a sweep finds out whether the window
    # is back, at a fraction of the refusals a full batch would collect.
    probe = refused and not (latest.refused_until and latest.refused_until <= now)
    mode = override if override in MODES else ("lean" if tight or probe else "deep")
    cost = mode_cost(sessions, mode)
    cap = max_cap
    for e in est.values():
        if e.used is not None:
            room = (cfg.stop[e.window] - e.used) / (cost * cfg.per_usd(e.window))
            cap = min(cap, math.floor(room))
    reason = "allowance_lean" if mode == "lean" and override == "auto" else None
    if probe:
        cap, reason = min(cap, 1), "allowance_refused_probe"
    if cap <= 0:
        cap, reason = 0, "allowance_low"
    return Decision(mode, max(cap, 0), reason, None, est, cost)


def describe(decision: Decision, cfg: Config) -> list[str]:
    """Markdown lines for the gate's Step Summary."""
    lines = []
    for w, label in ((FIVE_HOUR, "5-hour"), (SEVEN_DAY, "7-day")):
        e = decision.windows.get(w)
        if e is None:
            continue
        used = "unknown" if e.used is None else f"{e.used:.0f} %"
        lines.append(
            f"- {label} allowance: {used} ({e.source}; lean at {cfg.lean_at[w]:.0f} %, "
            f"stop at {cfg.stop[w]:.0f} %, window = ${cfg.allowance_usd[w]:.0f}), "
            f"resets {_iso(e.resets_at)}"
        )
    lines.append(
        f"- Mode: **{decision.mode}**, cap {decision.cap} "
        f"(${decision.cost:.2f} per session), reason: {decision.reason or 'ok'}"
    )
    return lines


# ------------------------------------------------------------------- replay
def replay(
    records: list[dict[str, Any]],
    cfg: Config,
    max_cap: int,
    since: dt.datetime | None = None,
    setup: dt.timedelta = dt.timedelta(minutes=2),
) -> list[dict[str, Any]]:
    """The decision the gate would have made before each past sweep run.

    A run's gate time is its earliest session start (``ts - duration_s``) less
    ``setup``; the decision sees only the sessions recorded before it. History is what
    really happened, not what the new gate would have caused.
    """
    sessions = parse_sessions(records)
    runs: dict[str, list[dict[str, Any]]] = {}
    for rec in records:
        if _when(rec.get("ts")):
            runs.setdefault(str(rec.get("run_id")), []).append(rec)
    out = []
    for run_id, recs in runs.items():
        starts = [
            _when(r["ts"]) - dt.timedelta(seconds=_number(r.get("duration_s")) or 0)
            for r in recs
        ]
        gate = min(starts) - setup
        if since and gate < since:
            continue
        before = [s for s in sessions if s.ts < gate]
        d = decide(before, gate, cfg, max_cap)
        refused = sum(s.refused for s in parse_sessions(recs))
        out.append(
            {
                "gate": gate, "run_id": run_id, "started": len(recs), "refused": refused,
                "u5": d.windows[FIVE_HOUR].used, "mode": d.mode, "cap": d.cap,
                "reason": d.reason or "ok",
            }
        )
    out.sort(key=lambda r: r["gate"])
    return out


def _replay_table(rows: list[dict[str, Any]]) -> str:
    lines = [
        "| gate (UTC) | sessions started | of them refused | u5 (est.) | mode | cap | reason |",
        "|---|---|---|---|---|---|---|",
    ]
    for r in rows:
        u5 = "-" if r["u5"] is None else f"{r['u5']:.0f} %"
        flag = " **over cap**" if r["started"] > r["cap"] else ""
        lines.append(
            f"| {_iso(r['gate'])} | {r['started']}{flag} | {r['refused']} | {u5} | "
            f"{r['mode']} | {r['cap']} | {r['reason']} |"
        )
    return "\n".join(lines)


def main() -> None:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    sub = ap.add_subparsers(dest="cmd")
    st = sub.add_parser("status", help="the decision a sweep would make now (default)")
    st.add_argument("--max", type=int, default=6, help="MAX_QUESTIONS_PER_RUN")
    st.add_argument("--mode", default=os.environ.get("FORECAST_MODE", "auto"), choices=OVERRIDES)
    rp = sub.add_parser("replay", help="the decision before each past sweep run")
    rp.add_argument("--since", help="first day to replay (YYYY-MM-DD)")
    rp.add_argument("--max", type=int, default=6, help="MAX_QUESTIONS_PER_RUN")
    args = ap.parse_args()
    cfg = Config.from_env()
    if args.cmd == "replay":
        since = _when(args.since) if args.since else None
        print(_replay_table(replay(ledger_records(USAGE), cfg, args.max, since)))
        return
    max_cap = getattr(args, "max", 6)
    override = getattr(args, "mode", os.environ.get("FORECAST_MODE", "auto"))
    now = dt.datetime.now(dt.UTC)
    print("\n".join(describe(decide(load_sessions(), now, cfg, max_cap, override), cfg)))


if __name__ == "__main__":
    main()
