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
from _common import LEDGER, find_slug, load_meta, save_meta, today


def _append(record: dict[str, Any]) -> None:
    """Append one JSON record to the ledger, creating it if needed."""
    LEDGER.parent.mkdir(parents=True, exist_ok=True)
    with LEDGER.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(record, ensure_ascii=False) + "\n")


def _count_forecasts(slug: str) -> int:
    """Number of ``forecast`` records already in the ledger for ``slug``.

    Counting rather than taking ``max(version) + 1`` keeps the ledger's
    versions-are-1..N-without-gaps invariant intact even if some record carries a
    wrong version number: a stray v3 in a two-record slug would otherwise make the
    next entry v4 and leave a permanent hole.

    A malformed line is skipped rather than raised on: the ledger is append-only
    and losing the ability to append because of one bad line elsewhere in the file
    is the worse failure.
    """
    if not LEDGER.exists():
        return 0
    n = 0
    for line in LEDGER.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            rec = json.loads(line)
        except json.JSONDecodeError:
            continue
        if rec.get("slug") == slug and rec.get("event", "forecast") == "forecast":
            n += 1
    return n


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
    # Derive the version from the ledger, which is the append-only record this
    # entry joins. Deriving it from meta.yaml's current.version made the number
    # depend on whether meta.yaml had already been hand-edited for this version --
    # a workflow that writes forecast.md and meta.yaml first then logged a phantom
    # extra version.
    version = _count_forecasts(slug) + 1
    meta_version = (meta.get("current") or {}).get("version")
    if meta_version is not None and int(meta_version) not in (version - 1, version):
        print(
            f"! {slug}: meta.yaml says v{meta_version} but the ledger holds "
            f"{version - 1} forecast(s); logging v{version} from the ledger",
            file=sys.stderr,
        )

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
    if args.next_review:
        meta["next_review"] = args.next_review
    save_meta(slug, meta)
    print(f"logged v{version} for {slug}")


def cmd_resolve(args: argparse.Namespace) -> None:
    slug = find_slug(args.slug) or sys.exit(f"! no unique question for {args.slug!r}")
    meta = load_meta(slug)
    outcome = _outcome_value(args.outcome)
    _append(
        {
            "ts": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
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
