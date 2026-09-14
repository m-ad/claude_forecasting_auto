#!/usr/bin/env python3
"""Append forecasts and resolutions to ``ledger/forecasts.jsonl``.

The ledger is the scoreable record: one JSON object per line, append-only.
``meta.yaml`` is kept in sync so triage and the index stay correct.

Examples
--------
    uv run scripts/log_forecast.py add <slug> --median 0.12 --lower 0.08 --upper 0.18 \
        --cp 0.09 --pro 0.07 --gold 0.08 --n-forecasters 312 \
        --thesis "..." --next-review 2026-10-31
    uv run scripts/log_forecast.py resolve <slug> --outcome yes
    uv run scripts/log_forecast.py submit <slug> --tournament minibench \\
        --payload '{"probability_yes": 0.12}' --api-status 201 --comment-posted
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common import LEDGER, find_slug, load_meta, save_meta, today

# The five points the Metaculus API wants for a continuous question. 25/50/75 are
# the IQR and the median by definition, so only the tails are asked for.
PERCENTILE_POINTS = (10, 25, 50, 75, 90)
CONTINUOUS_TYPES = {"numeric", "date", "discrete"}


def _append(record: dict[str, Any]) -> None:
    """Append one JSON record to the ledger, creating it if needed."""
    LEDGER.parent.mkdir(parents=True, exist_ok=True)
    with LEDGER.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(record, ensure_ascii=False) + "\n")


def _utc_now() -> str:
    """Current instant as a seconds-precision ISO-8601 UTC string."""
    return dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")


def _percentiles(
    p10: float | None, lower: float, median: float, upper: float, p90: float | None
) -> dict[int, float] | None:
    """Assemble the five-point CDF, or ``None`` when the tails were not given.

    The middle three points are not arguments: taking them from the forecast
    itself is what stops ``percentiles`` and ``current`` from drifting into two
    disagreeing records of the same belief.
    """
    if p10 is None and p90 is None:
        return None
    if p10 is None or p90 is None:
        sys.exit("! --p10 and --p90 go together: a CDF needs both tails")
    values = [p10, lower, median, upper, p90]
    if values != sorted(values):
        sys.exit(f"! percentiles are not monotone: {values}")
    return dict(zip(PERCENTILE_POINTS, values))


def _outcome_value(raw: str) -> float | str:
    """Coerce a resolution argument to a number where it is one."""
    low = raw.strip().lower()
    if low in {"yes", "true", "1"}:
        return 1.0
    if low in {"no", "false", "0"}:
        return 0.0
    try:
        return float(raw)
    except ValueError:
        return raw


def cmd_add(args: argparse.Namespace) -> None:
    slug = find_slug(args.slug) or sys.exit(f"! no unique question for {args.slug!r}")
    meta = load_meta(slug)
    version = int((meta.get("current") or {}).get("version") or 0) + 1

    # Validated before the append: a ledger line written and then abandoned by a
    # failed exit is exactly the drift rule 8 forbids anyone from cleaning up.
    pcts = _percentiles(args.p10, args.lower, args.median, args.upper, args.p90)
    if pcts is not None and meta.get("type") not in CONTINUOUS_TYPES:
        sys.exit(
            f"! {slug} is a {meta.get('type')} question; percentiles are for "
            f"{sorted(CONTINUOUS_TYPES)}"
        )

    record = {
        "ts": _utc_now(),
        "event": "forecast",
        "slug": slug,
        "version": version,
        "source": meta.get("source"),
        "post_id": meta.get("post_id"),
        "type": meta.get("type"),
        "median": args.median,
        "iqr": [args.lower, args.upper],
        "community": {
            "cp": args.cp,
            "pro": args.pro,
            "gold": args.gold,
            "n_forecasters": args.n_forecasters,
        },
        "thesis": args.thesis,
        "mode": args.mode,
    }
    _append(record)

    meta["current"] = {
        "version": version,
        "date": today(),
        "median": args.median,
        "iqr": [args.lower, args.upper],
        "community": {
            "cp": args.cp,
            "pro": args.pro,
            "gold": args.gold,
            "n_forecasters": args.n_forecasters,
            "as_of": today(),
        },
    }
    if pcts is not None:
        meta["percentiles"] = pcts
    if args.next_review:
        meta["next_review"] = args.next_review
    save_meta(slug, meta)
    print(f"logged v{version} for {slug}")


def _logged_submissions(slug: str) -> list[dict[str, Any]]:
    """Every ``submission`` record already in the ledger for ``slug``."""
    if not LEDGER.exists():
        return []
    out = []
    for line in LEDGER.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        try:
            rec = json.loads(line)
        except json.JSONDecodeError:
            continue
        if rec.get("event") == "submission" and rec.get("slug") == slug:
            out.append(rec)
    return out


def cmd_submit(args: argparse.Namespace) -> None:
    """Record a forecast that the Metaculus API has already accepted.

    This does not call the API - ``scripts/metaculus_submit.py`` does - it writes
    the audit trail afterwards, in both places at once so the ledger and
    ``meta.yaml`` cannot disagree about what was sent. Every guard here refuses
    rather than corrects: a second submission on a one-shot question is not
    something to reconcile, it is a bug upstream that must stop before it writes.
    """
    slug = find_slug(args.slug) or sys.exit(f"! no unique question for {args.slug!r}")
    meta = load_meta(slug)
    tour = meta.get("tournament")
    if not isinstance(tour, dict):
        sys.exit(f"! {slug} carries no tournament block - nothing to submit against")
    if args.tournament and args.tournament != tour.get("slug"):
        sys.exit(
            f"! {slug} belongs to tournament {tour.get('slug')!r}, "
            f"not {args.tournament!r}"
        )
    if not (meta.get("current") or {}).get("version"):
        sys.exit(f"! {slug} has no forecast yet - rule 7 before rule 4")
    if meta.get("question_id") is None:
        sys.exit(f"! {slug} has no question_id - the API cannot be told what to write")

    already = _logged_submissions(slug)
    if already or tour.get("submitted"):
        when = tour.get("submitted") or already[0].get("ts")
        sys.exit(f"! {slug} was already submitted at {when} - one shot means one shot")
    if tour.get("missed_window"):
        sys.exit(f"! {slug} is flagged missed_window; clear it before submitting")
    if not 200 <= args.api_status < 300:
        sys.exit(
            f"! api-status {args.api_status} is not a success - the ledger records "
            "accepted submissions only"
        )

    try:
        payload = json.loads(args.payload)
    except json.JSONDecodeError as exc:
        sys.exit(f"! --payload is not valid JSON: {exc}")
    if not isinstance(payload, dict) or not payload:
        sys.exit("! --payload must be the non-empty JSON object that was sent")

    ts = _utc_now()
    _append(
        {
            "ts": ts,
            "event": "submission",
            "slug": slug,
            "post_id": meta.get("post_id"),
            "question_id": meta.get("question_id"),
            "tournament": tour.get("slug"),
            "payload": payload,
            "comment_posted": bool(args.comment_posted),
            "api_status": args.api_status,
        }
    )
    tour["submitted"] = ts
    tour["submitted_forecast"] = payload
    tour["comment_posted"] = bool(args.comment_posted)
    save_meta(slug, meta)
    print(f"submitted {slug} to {tour.get('slug')} at {ts}")


def cmd_resolve(args: argparse.Namespace) -> None:
    slug = find_slug(args.slug) or sys.exit(f"! no unique question for {args.slug!r}")
    meta = load_meta(slug)
    outcome = _outcome_value(args.outcome)
    _append(
        {
            "ts": _utc_now(),
            "event": "resolution",
            "slug": slug,
            "type": meta.get("type"),
            "outcome": outcome,
            "resolution_source": args.source,
        }
    )
    meta["status"] = "resolved"
    meta["resolution"] = {
        "outcome": outcome,
        "date": args.date or today(),
        "source": args.source,
    }
    meta["next_review"] = None
    save_meta(slug, meta)
    print(f"resolved {slug} -> {outcome}")


def main() -> None:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    sub = ap.add_subparsers(dest="cmd", required=True)

    a = sub.add_parser("add", help="log a new forecast version")
    a.add_argument("slug")
    a.add_argument(
        "--median",
        type=float,
        required=True,
        help="probability in [0,1] for binary; native units otherwise",
    )
    a.add_argument("--lower", type=float, required=True, help="25th percentile")
    a.add_argument("--upper", type=float, required=True, help="75th percentile")
    a.add_argument("--cp", type=float, help="Metaculus community prediction")
    a.add_argument("--pro", type=float, help="Metaculus Pro aggregation")
    a.add_argument("--gold", type=float, help="Metaculus gold-medalist aggregation")
    a.add_argument("--n-forecasters", type=int)
    a.add_argument("--thesis", default="")
    a.add_argument(
        "--mode", default="initial", choices=["initial", "update", "reanalysis"]
    )
    a.add_argument(
        "--p10",
        type=float,
        help="10th percentile; numeric/date/discrete only, and requires --p90",
    )
    a.add_argument("--p90", type=float, help="90th percentile; requires --p10")
    a.add_argument("--next-review", help="YYYY-MM-DD")
    a.set_defaults(func=cmd_add)

    s = sub.add_parser("submit", help="record an accepted Metaculus submission")
    s.add_argument("slug")
    s.add_argument("--tournament", help="asserted against meta.tournament.slug")
    s.add_argument(
        "--payload", required=True, help="the JSON object sent to the API, verbatim"
    )
    s.add_argument(
        "--api-status", type=int, required=True, help="HTTP status the API returned"
    )
    s.add_argument(
        "--comment-posted",
        action="store_true",
        help="a private rationale comment went up alongside the forecast",
    )
    s.set_defaults(func=cmd_submit)

    r = sub.add_parser("resolve", help="record a resolution")
    r.add_argument("slug")
    r.add_argument("--outcome", required=True, help="yes|no|<numeric value>|<option>")
    r.add_argument("--date", help="resolution date, defaults to today")
    r.add_argument("--source", help="the resolution source consulted")
    r.set_defaults(func=cmd_resolve)

    args = ap.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
