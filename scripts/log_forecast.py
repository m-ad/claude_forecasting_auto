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
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common import LEDGER, find_slug, load_meta, save_meta, today  # noqa: E402


def _append(record: dict[str, Any]) -> None:
    """Append one JSON record to the ledger, creating it if needed."""
    LEDGER.parent.mkdir(parents=True, exist_ok=True)
    with LEDGER.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(record, ensure_ascii=False) + "\n")


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

    record = {
        "ts": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
        "event": "forecast",
        "slug": slug,
        "version": version,
        "source": meta.get("source"),
        "post_id": meta.get("post_id"),
        "type": meta.get("type"),
        "median": args.median,
        "iqr": [args.lower, args.upper],
        "community": {"cp": args.cp, "pro": args.pro, "gold": args.gold,
                      "n_forecasters": args.n_forecasters},
        "thesis": args.thesis,
        "mode": args.mode,
    }
    _append(record)

    meta["current"] = {
        "version": version,
        "date": today(),
        "median": args.median,
        "iqr": [args.lower, args.upper],
        "community": {"cp": args.cp, "pro": args.pro, "gold": args.gold,
                      "n_forecasters": args.n_forecasters, "as_of": today()},
    }
    if args.next_review:
        meta["next_review"] = args.next_review
    save_meta(slug, meta)
    print(f"logged v{version} for {slug}")


def cmd_resolve(args: argparse.Namespace) -> None:
    slug = find_slug(args.slug) or sys.exit(f"! no unique question for {args.slug!r}")
    meta = load_meta(slug)
    outcome = _outcome_value(args.outcome)
    _append({
        "ts": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
        "event": "resolution",
        "slug": slug,
        "type": meta.get("type"),
        "outcome": outcome,
        "resolution_source": args.source,
    })
    meta["status"] = "resolved"
    meta["resolution"] = {"outcome": outcome, "date": args.date or today(),
                          "source": args.source}
    meta["next_review"] = None
    save_meta(slug, meta)
    print(f"resolved {slug} -> {outcome}")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    a = sub.add_parser("add", help="log a new forecast version")
    a.add_argument("slug")
    a.add_argument("--median", type=float, required=True,
                   help="probability in [0,1] for binary; native units otherwise")
    a.add_argument("--lower", type=float, required=True, help="25th percentile")
    a.add_argument("--upper", type=float, required=True, help="75th percentile")
    a.add_argument("--cp", type=float, help="Metaculus community prediction")
    a.add_argument("--pro", type=float, help="Metaculus Pro aggregation")
    a.add_argument("--gold", type=float, help="Metaculus gold-medalist aggregation")
    a.add_argument("--n-forecasters", type=int)
    a.add_argument("--thesis", default="")
    a.add_argument("--mode", default="initial",
                   choices=["initial", "update", "reanalysis"])
    a.add_argument("--next-review", help="YYYY-MM-DD")
    a.set_defaults(func=cmd_add)

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
