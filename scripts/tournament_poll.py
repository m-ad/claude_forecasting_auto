#!/usr/bin/env python3
"""The sweep's no-LLM gate: is there a question to forecast, and may we spend on it?

Runs every sweep cycle before any model is started, in pure Python, so a cycle
that finds nothing costs one billed Actions minute and zero tokens. In order:

1. **Budget.** Sums the trailing-7-day ``cost_usd_equiv`` in ``ledger/usage.jsonl``
   against ``WEEKLY_BUDGET_USD_EQUIV``. Over budget: no work. Above 80 %: at most
   two questions per run, soonest-closing first.
2. **Token.** One authenticated call. A refused token fails the job loudly here,
   before a model ever starts.
3. **Candidates.** Open posts in every active tournament (or the ones named on
   the command line), minus: questions this repo already submitted or closed out,
   questions closing too soon to forecast, and -- authoritatively -- questions on
   which Metaculus already holds the bot's forecast. That last check needs no
   repository state, which is what makes the gate safe after a lost commit.
4. **Order.** ``(registry priority, soonest close)``, capped at
   ``MAX_QUESTIONS_PER_RUN``.

Examples
--------
    uv run scripts/tournament_poll.py                   # human-readable
    uv run scripts/tournament_poll.py --github-output   # for the sweep workflow
    uv run scripts/tournament_poll.py --tournament bot-testing-area --max 1
    uv run scripts/tournament_poll.py --post-ids 45517
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import sys
import time
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))
import metaculus_api as mapi
from _common import all_questions
from record_usage import weekly_spend
from tournament_registry import RegistryError, active_tournaments, get

DEFAULT_MAX = 6
# A forecast session needs time to research; one started this close to the close
# would be killed mid-run, or submit after the window. Not forecasting scores 0
# peer points, which beats a rushed forecast that is worse than the field.
MIN_MINUTES_LEFT = 20
SOFT_LANDING = 0.8
SOFT_LANDING_MAX = 2


def _env_float(name: str) -> float | None:
    raw = os.environ.get(name, "").strip()
    try:
        return float(raw) if raw else None
    except ValueError:
        return None


def _parse_ts(value: str | None) -> dt.datetime | None:
    if not value:
        return None
    try:
        return dt.datetime.fromisoformat(value)
    except ValueError:
        return None


def local_state() -> dict[int, dict[str, Any]]:
    """Tournament block per post id, for questions this repository scaffolded."""
    out: dict[int, dict[str, Any]] = {}
    for _slug, meta in all_questions():
        tour = meta.get("tournament")
        if isinstance(tour, dict) and meta.get("post_id"):
            out[int(meta["post_id"])] = {**tour, "status": meta.get("status")}
    return out


def budget_cap(cap: int, budget: float | None, spent: float) -> tuple[int, str | None]:
    """Apply the weekly spend guard to the per-run cap.

    Returns
    -------
    (int, str or None)
        The effective cap, and a reason when the guard changed it.
    """
    if budget is None or budget <= 0:
        return cap, None
    if spent >= budget:
        return 0, "budget_exceeded"
    if spent >= SOFT_LANDING * budget:
        return min(cap, SOFT_LANDING_MAX), "budget_soft_landing"
    return cap, None


def candidates(
    tournaments: list[dict[str, Any]],
    now: dt.datetime,
    post_ids: list[int] | None = None,
) -> tuple[list[dict[str, Any]], list[tuple[int, str]]]:
    """Open, unforecast questions across ``tournaments``, plus why others were skipped.

    Parameters
    ----------
    tournaments : list of dict
        Registry entries to poll (``slug``, ``priority``).
    now : datetime
        The current UTC instant.
    post_ids : list of int, optional
        Only these posts (still checked against every guard).
    """
    local = local_state()
    found: list[dict[str, Any]] = []
    skipped: list[tuple[int, str]] = []
    seen: set[int] = set()
    for tour in tournaments:
        for post in mapi.list_posts(tour["slug"]):
            pid = int(post["id"])
            if pid in seen or (post_ids and pid not in post_ids):
                continue
            seen.add(pid)
            q = post.get("question")
            if not q:
                skipped.append((pid, "group post (not supported)"))
                continue
            if q.get("type") not in mapi.FORECAST_TYPES:
                skipped.append((pid, f"type {q.get('type')}"))
                continue
            mine = local.get(pid) or {}
            if mine.get("submitted") or mine.get("missed_window"):
                skipped.append((pid, "already submitted or closed out here"))
                continue
            closes = _parse_ts(q.get("scheduled_close_time") or post.get("scheduled_close_time"))
            if closes and (closes - now).total_seconds() < MIN_MINUTES_LEFT * 60:
                skipped.append((pid, f"closes in < {MIN_MINUTES_LEFT} min"))
                continue
            detail = mapi.get_post(pid, stage="poll")
            dq = detail.get("question") or {}
            if mapi.live_values(dq) is not None:
                skipped.append((pid, "Metaculus already holds the bot's forecast"))
                continue
            if not mapi.is_open(detail, dq):
                skipped.append((pid, "not open"))
                continue
            found.append(
                {
                    "post_id": pid,
                    "question_id": dq.get("id"),
                    "tournament": tour["slug"],
                    "priority": int(tour.get("priority", 99)),
                    "closes": closes.isoformat() if closes else None,
                    "type": dq.get("type"),
                    "title": (post.get("title") or "")[:90],
                }
            )
            time.sleep(0.5)  # a steady pace keeps the per-IP rate limit quiet
    found.sort(key=lambda c: (c["priority"], c["closes"] or "9999"))
    return found, skipped


def _write_github_output(values: dict[str, str]) -> None:
    path = os.environ.get("GITHUB_OUTPUT")
    if not path:
        for k, v in values.items():
            print(f"{k}={v}")
        return
    with open(path, "a", encoding="utf-8") as fh:
        for k, v in values.items():
            fh.write(f"{k}={v}\n")


def _summary(lines: list[str]) -> None:
    path = os.environ.get("GITHUB_STEP_SUMMARY")
    text = "\n".join(lines) + "\n"
    if path:
        with open(path, "a", encoding="utf-8") as fh:
            fh.write(text)
    else:
        print(text)


def main() -> None:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("--github-output", action="store_true", help="emit workflow outputs")
    ap.add_argument(
        "--tournament", action="append", default=[], help="poll this slug (repeatable)"
    )
    ap.add_argument("--post-ids", nargs="*", type=int, default=[], help="only these posts")
    ap.add_argument("--max", type=int, help="override MAX_QUESTIONS_PER_RUN")
    args = ap.parse_args()

    now = dt.datetime.now(dt.UTC)
    cap = args.max or int(_env_float("MAX_QUESTIONS_PER_RUN") or DEFAULT_MAX)
    budget = _env_float("WEEKLY_BUDGET_USD_EQUIV")
    spent = weekly_spend(now)
    cap, guard = budget_cap(cap, budget, spent)
    out = {"has_work": "false", "questions": "[]", "question_count": "0"}
    lines = ["### Sweep gate", "", f"7-day spend: ${spent:.2f}"
             + (f" of ${budget:.2f}" if budget else " (no budget set)")]
    if cap == 0:
        out["reason"] = guard or "cap_zero"
        lines.append(f"**No work: {out['reason']}.**")
        _summary(lines)
        if args.github_output:
            _write_github_output(out)
        return

    try:
        me = mapi.whoami()
        if not me.get("is_bot"):
            print(f"! token belongs to {me.get('username')!r}, which is not a bot account")
        if args.tournament:
            tours = []
            for slug in args.tournament:
                try:
                    tours.append(get(slug))
                except RegistryError:
                    tours.append({"slug": slug, "priority": 99})
        else:
            tours = active_tournaments()
        found, skipped = candidates(tours, now, args.post_ids or None)
    except mapi.MetaculusAuthError as exc:
        # Fatal for the whole run and never a per-question problem: fail the job.
        _summary([*lines, f"**Metaculus token refused**: {exc}"])
        sys.exit(f"! {exc}")

    chosen = found[:cap]
    out.update(
        {
            "has_work": "true" if chosen else "false",
            "questions": json.dumps(chosen, separators=(",", ":"), ensure_ascii=True),
            "question_count": str(len(chosen)),
            "reason": guard or ("ok" if chosen else "nothing_open"),
        }
    )
    polled = ", ".join(t["slug"] for t in tours) or "(no active tournaments)"
    lines += [f"Polled: {polled}", f"Chosen: {len(chosen)} of {len(found)} (cap {cap})", ""]
    if chosen:
        lines += ["| post | tournament | type | closes | title |", "|---|---|---|---|---|"]
        lines += [
            f"| {c['post_id']} | {c['tournament']} | {c['type']} | {c['closes']} | "
            f"{c['title'].replace('|', '/')} |"
            for c in chosen
        ]
    if skipped:
        lines += ["", "Skipped: " + "; ".join(f"{p} ({why})" for p, why in skipped[:20])]
    _summary(lines)
    if args.github_output:
        _write_github_output(out)


if __name__ == "__main__":
    main()
