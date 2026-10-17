#!/usr/bin/env python3
"""Append forecasts and resolutions to ``ledger/forecasts.jsonl``.

The ledger is the scoreable record: one JSON object per line, append-only.
``meta.yaml`` is kept in sync so triage and the index stay correct.

Examples
--------
    uv run scripts/log_forecast.py add <slug> --median 0.12 --lower 0.08 --upper 0.18 \
        --cp 0.09 --pro 0.07 --gold 0.08 --n-forecasters 312 \
        --thesis "..." --next-review 2026-10-31
    uv run scripts/log_forecast.py add <slug> --median 0.61 --lower 0.55 --upper 0.67 \
        --distribution '{"probabilities": {"Likud": 0.381, "Yashar": 0.61, "Other": 0.009}}' ...
    uv run scripts/log_forecast.py resolve <slug> --outcome yes
    uv run scripts/log_forecast.py resolve <slug> --outcome "Yashar"   # multiple choice
    uv run scripts/log_forecast.py resolve <slug> --outcome 2031-03-31 # date -> Unix seconds
    uv run scripts/log_forecast.py submit <slug> --payload '{"probability_yes": 0.12}' \
        --api-status 201 --comment-posted     # normally called by submit_metaculus.py

``--distribution`` records the full forecast next to the median and IQR, which
alone are the whole forecast only for a binary question. It is **required** for
multiple choice (the option vector) and optional for numeric/date
(``percentiles``) and discrete (``pmf`` or ``percentiles``). Pass the JSON inline
or as ``@path/to/file.json``. See ``DISTRIBUTION_SHAPES`` in ``_common.py``.

A one-shot tournament question (``tournament.mode: one_shot``) takes exactly one
forecast: ``add`` refuses a second, because a second would be a second submission,
which the bot tournaments forbid. ``submit`` and ``comment`` record what the
Metaculus API accepted; ``scripts/submit_metaculus.py`` calls them in-process so
the ledger and ``meta.yaml`` are written in one place.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import math
import re
import sys
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common import (
    LEDGER,
    QUESTIONS,
    distribution_problems,
    find_slug,
    fmt_value,
    ledger_records,
    load_meta,
    save_meta,
    today,
)


def _append(record: dict[str, Any]) -> None:
    """Append one JSON record to the ledger, creating it if needed."""
    LEDGER.parent.mkdir(parents=True, exist_ok=True)
    with LEDGER.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(record, ensure_ascii=False) + "\n")


def _utc_now() -> str:
    """Current instant as a seconds-precision ISO-8601 UTC string."""
    return dt.datetime.now(dt.UTC).isoformat(timespec="seconds")


def _is_one_shot(meta: dict[str, Any]) -> bool:
    return (meta.get("tournament") or {}).get("mode") == "one_shot"


def _forecast_records(slug: str) -> list[dict[str, Any]]:
    """The ledger's ``forecast`` records for ``slug``, in file order.

    A record with no ``event`` key predates that field and is a forecast.
    """
    return [
        rec
        for rec in ledger_records(LEDGER)
        if rec.get("slug") == slug and rec.get("event", "forecast") == "forecast"
    ]


def _count_forecasts(slug: str) -> int:
    """Number of ``forecast`` records already in the ledger for ``slug``.

    Counting rather than taking ``max(version) + 1`` keeps the ledger's
    versions-are-1..N-without-gaps invariant intact even if some record carries a
    wrong version number: a stray v3 in a two-record slug would otherwise make the
    next entry v4 and leave a permanent hole.
    """
    return len(_forecast_records(slug))


def cached_options(slug: str, post_id: int | None) -> list[str] | None:
    """Option labels from the newest cached Metaculus snapshot of *this* post.

    Matched on ``post_id`` inside the JSON, not on the file name: a folder can
    also cache snapshots of related posts. Newest is by the retrieval date every
    ``raw/`` file name carries (``test_meta.py`` enforces it). None when no
    snapshot of this post lists options.
    """
    if post_id is None:
        return None
    found: list[tuple[str, list[str]]] = []
    for path in (QUESTIONS / slug / "raw").glob("*.json"):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            continue
        if not isinstance(data, dict) or data.get("post_id") != post_id:
            continue
        opts = data.get("options")
        m = re.search(r"\d{4}-\d{2}-\d{2}", path.stem)
        if isinstance(opts, list) and opts and m:
            found.append((m.group(0), [str(o) for o in opts]))
    return max(found)[1] if found else None


def _parse_distribution(raw: str) -> Any:
    """``--distribution`` as JSON, inline or from ``@file`` (labels with quotes)."""
    try:
        text = Path(raw[1:]).read_text(encoding="utf-8") if raw.startswith("@") else raw
        return json.loads(text)
    except OSError as exc:
        sys.exit(f"! --distribution file unreadable: {exc}")
    except json.JSONDecodeError as exc:
        sys.exit(f"! --distribution is not valid JSON: {exc}")


def _last_forecast(slug: str) -> dict[str, Any] | None:
    """The latest ``forecast`` record for ``slug``, or None."""
    recs = _forecast_records(slug)
    return recs[-1] if recs else None


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


# The median of a multiple-choice record is its leading option's probability.
PROBABILITY_TYPES = {"binary", "multiple_choice"}


def _forecast_problems(
    qtype: str | None, median: float, lower: float, upper: float
) -> list[str]:
    """Reasons a median/IQR triple must not enter the ledger; empty if fine.

    Checked before the append because the ledger is append-only: a bad line
    that ``tests/test_ledger.py`` catches afterwards can never be removed.
    """
    out = []
    if not all(math.isfinite(v) for v in (median, lower, upper)):
        return ["median and IQR must be finite numbers"]
    if not lower <= median <= upper:
        out.append(f"median {median} lies outside the IQR [{lower}, {upper}]")
    if not lower < upper:
        out.append(f"IQR [{lower}, {upper}] is degenerate: lower must be < upper")
    if qtype in PROBABILITY_TYPES and not all(
        0 <= v <= 1 for v in (median, lower, upper)
    ):
        out.append(
            f"{qtype} values must be probabilities in [0, 1], not percent "
            f"(got median {median}, IQR [{lower}, {upper}])"
        )
    return out


def _resolution_outcome(slug: str, qtype: str | None, raw: str) -> float | str:
    """The outcome to record for a non-multiple-choice question, or exit.

    Binary outcomes must be yes/no: anything else (``annulled``, ``ambiguous``)
    would crash ``calibration.py`` and could never be removed from the ledger.
    Date outcomes are stored as Unix seconds, the unit their median and IQR use,
    so an ISO date is converted; left as a string it would go unscored.
    """
    outcome = _outcome_value(raw)
    if qtype == "binary" and outcome not in (0.0, 1.0):
        sys.exit(
            f"! {slug}: binary outcome must be yes or no, got {raw!r}. An annulled "
            "or ambiguous question is not a resolution: set status: dropped "
            "instead (docs/update-protocol.md)"
        )
    if qtype == "date" and isinstance(outcome, str):
        try:
            day = dt.date.fromisoformat(outcome.strip()[:10])
        except ValueError:
            sys.exit(f"! {slug}: date outcome must be YYYY-MM-DD, got {raw!r}")
        return dt.datetime(day.year, day.month, day.day, tzinfo=dt.UTC).timestamp()
    return outcome


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

    if _is_one_shot(meta) and version > 1:
        sys.exit(
            f"! {slug} is a one-shot tournament question and already has a forecast; "
            "a second one would be a second submission, which the bot tournaments "
            "forbid"
        )
    if _is_one_shot(meta) and args.next_review:
        sys.exit(f"! {slug} is one-shot: it is never revisited, so no --next-review")

    qtype = meta.get("type")
    problems = _forecast_problems(qtype, args.median, args.lower, args.upper)
    if problems:
        sys.exit(f"! {slug}: forecast rejected:\n  " + "\n  ".join(problems))
    dist = _parse_distribution(args.distribution) if args.distribution else None
    if dist is None and qtype == "multiple_choice":
        sys.exit(
            f"! {slug}: multiple-choice forecasts need --distribution "
            '\'{"probabilities": {"<exact option label>": p, ...}}\' - '
            "the median alone records only the leading option"
        )
    if dist is not None:
        options = cached_options(slug, meta.get("post_id"))
        if qtype == "multiple_choice" and options is None:
            print(
                f"! {slug}: no cached snapshot lists this question's options; "
                "labels not checked against Metaculus",
                file=sys.stderr,
            )
        problems = distribution_problems(
            qtype, dist, args.median, [args.lower, args.upper], options
        )
        if problems:
            sys.exit(f"! {slug}: --distribution rejected:\n  " + "\n  ".join(problems))

    record = {
        "ts": _utc_now(),
        "event": "forecast",
        "slug": slug,
        "version": version,
        "source": meta.get("source"),
        "post_id": meta.get("post_id"),
        "type": qtype,
        "median": args.median,
        "iqr": [args.lower, args.upper],
        **({"distribution": dist} if dist is not None else {}),
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
    _refresh_header(slug, qtype, version, args.median, args.lower, args.upper)
    print(f"logged v{version} for {slug}")


def _refresh_header(
    slug: str, qtype: str | None, version: int, med: float, lo: float, hi: float
) -> None:
    """Rewrite ``forecast.md``'s Current forecast row from what was just logged.

    The header is the one part of ``forecast.md`` rewritten in place, and the row
    must agree with ``meta.yaml`` to the decimal (``tests/test_forecast_md.py``).
    Deriving it from the logged numbers instead of trusting a hand-typed copy
    removes a formatting failure an unattended run cannot recover from.
    """
    path = QUESTIONS / slug / "forecast.md"
    if not path.exists():
        return
    row = (
        f"| **Current forecast** | Median {fmt_value(med, qtype)}, IQR "
        f"[{fmt_value(lo, qtype)}, {fmt_value(hi, qtype)}] (v{version}, {today()}) |"
    )
    text = path.read_text(encoding="utf-8")
    new = re.sub(
        r"(?m)^\|[ \t]*\*\*Current forecast\*\*[ \t]*\|.*\|[ \t]*$", row, text, count=1
    )
    if new != text:
        path.write_text(new, encoding="utf-8")


def _logged_submissions(slug: str) -> list[dict[str, Any]]:
    """Every ``submission`` record already in the ledger for ``slug``."""
    return [
        rec
        for rec in ledger_records(LEDGER)
        if rec.get("event") == "submission" and rec.get("slug") == slug
    ]


def record_submission(
    slug: str, payload: dict[str, Any], api_status: int, comment_posted: bool
) -> str:
    """Record a forecast the Metaculus API has already accepted; returns its stamp.

    Writes the ledger line and ``meta.tournament.{submitted, submitted_forecast,
    comment_posted}`` together, so the two cannot disagree about what was sent.
    Every guard refuses rather than corrects: a second submission on a one-shot
    question is not something to reconcile, it is a bug upstream that must stop.

    Raises
    ------
    ValueError
        When the record would break a ledger or one-shot invariant.
    """
    meta = load_meta(slug)
    tour = meta.get("tournament") or {}
    if not tour:
        raise ValueError(f"{slug} carries no tournament block - nothing to submit against")
    if not (meta.get("current") or {}).get("version"):
        raise ValueError(f"{slug} has no forecast yet - rule 7 before submission")
    if meta.get("question_id") is None:
        raise ValueError(f"{slug} has no question_id")
    already = _logged_submissions(slug)
    if tour.get("mode") == "one_shot" and (already or tour.get("submitted")):
        when = tour.get("submitted") or already[0].get("ts")
        raise ValueError(f"{slug} was already submitted at {when} - one shot means one shot")
    if not 200 <= api_status < 300:
        raise ValueError(f"api status {api_status} is not a success")
    if not isinstance(payload, dict) or not payload:
        raise ValueError("payload must be the non-empty JSON object that was sent")
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
            "comment_posted": bool(comment_posted),
            "api_status": api_status,
        }
    )
    tour["submitted"] = ts
    tour["submitted_forecast"] = payload
    tour["comment_posted"] = bool(comment_posted)
    save_meta(slug, meta)
    return ts


def record_late_comment(slug: str, api_status: int) -> None:
    """Record a rationale comment posted after its forecast (the sync's retry)."""
    meta = load_meta(slug)
    tour = meta.get("tournament") or {}
    if not tour.get("submitted"):
        raise ValueError(f"{slug} has no submission to attach a comment to")
    if tour.get("comment_posted"):
        raise ValueError(f"{slug} already has its comment")
    _append(
        {
            "ts": _utc_now(),
            "event": "comment",
            "slug": slug,
            "post_id": meta.get("post_id"),
            "api_status": api_status,
        }
    )
    tour["comment_posted"] = True
    save_meta(slug, meta)


def cmd_submit(args: argparse.Namespace) -> None:
    slug = find_slug(args.slug) or sys.exit(f"! no unique question for {args.slug!r}")
    try:
        payload = json.loads(args.payload)
    except json.JSONDecodeError as exc:
        sys.exit(f"! --payload is not valid JSON: {exc}")
    try:
        ts = record_submission(slug, payload, args.api_status, args.comment_posted)
    except ValueError as exc:
        sys.exit(f"! {exc}")
    print(f"recorded submission of {slug} at {ts}")


def cmd_resolve(args: argparse.Namespace) -> None:
    slug = find_slug(args.slug) or sys.exit(f"! no unique question for {args.slug!r}")
    meta = load_meta(slug)
    if meta.get("type") == "multiple_choice":
        # An option label is the outcome, verbatim: coercing would turn a "0" or
        # "1" option into a number the scorer can no longer match to its label.
        outcome: float | str = args.outcome
        last = _last_forecast(slug) or {}
        labels = list(
            (last.get("distribution") or {}).get("probabilities")
            or cached_options(slug, meta.get("post_id"))
            or []
        )
        if labels and outcome not in labels:
            sys.exit(f"! {slug}: {outcome!r} is not an option; one of {labels}")
    else:
        outcome = _resolution_outcome(slug, meta.get("type"), args.outcome)
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
    a.add_argument(
        "--distribution",
        help="full forecast as JSON or @file: required for multiple choice "
        '({"probabilities": {...}}), optional otherwise ({"percentiles": {...}} '
        'or, for discrete, {"pmf": {...}})',
    )
    a.add_argument("--thesis", default="")
    a.add_argument(
        "--mode", default="initial", choices=["initial", "update", "reanalysis"]
    )
    a.add_argument("--next-review", help="YYYY-MM-DD")
    a.set_defaults(func=cmd_add)

    s = sub.add_parser("submit", help="record an accepted Metaculus submission")
    s.add_argument("slug")
    s.add_argument("--payload", required=True, help="the JSON values sent, verbatim")
    s.add_argument("--api-status", type=int, required=True, help="HTTP status returned")
    s.add_argument(
        "--comment-posted",
        action="store_true",
        help="the private rationale comment went up alongside the forecast",
    )
    s.set_defaults(func=cmd_submit)

    r = sub.add_parser("resolve", help="record a resolution")
    r.add_argument("slug")
    r.add_argument(
        "--outcome",
        required=True,
        help="yes|no|<numeric value>|<YYYY-MM-DD>|<exact option label>",
    )
    r.add_argument("--date", help="resolution date, defaults to today")
    r.add_argument("--source", help="the resolution source consulted")
    r.set_defaults(func=cmd_resolve)

    args = ap.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
