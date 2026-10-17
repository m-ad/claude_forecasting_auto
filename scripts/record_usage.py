#!/usr/bin/env python3
"""Record what a Claude Code run spent, and report rolling spend.

The sweep runs ``claude -p ... --output-format json``; the final JSON object
carries ``total_cost_usd``, ``usage`` (input, output, cache read/write tokens),
``num_turns``, ``duration_ms`` and a per-model ``modelUsage`` breakdown. ``record``
turns that into one line of ``ledger/usage.jsonl`` and a small table for the
run's GitHub Step Summary; ``report`` prints the rolling 7/30-day view; the gate
reads ``weekly_spend()`` for the budget guard.

Two honest limitations:

- ``total_cost_usd`` is the **API-equivalent** price. On a subscription token it
  is not billed; it is the best available proxy for how much allowance a run used.
- Remaining subscription allowance is not exposed to CI, so the guard is a
  cumulative weekly budget the operator sets, not a reading of what is left.

Parsing is defensive by design: a missing or truncated file (a run killed by its
timeout) records ``parse_failed: true`` and zero cost, and never fails the job.

Examples
--------
    uv run scripts/record_usage.py record --result claude.json --job sweep \\
        --slug 2026-10-19-mc46101-x --run-id 123 --summary >> "$GITHUB_STEP_SUMMARY"
    uv run scripts/record_usage.py report
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common import REPO, ledger_records

USAGE = REPO / "ledger" / "usage.jsonl"


def _num(value: Any) -> float:
    return float(value) if isinstance(value, (int, float)) and not isinstance(value, bool) else 0.0


def parse_result(text: str) -> dict[str, Any] | None:
    """The ``result`` object from ``claude -p --output-format json`` output, or None.

    Accepts a single object, a JSON array of messages, or JSON Lines (stream
    output), and takes the last ``type: result`` record found.
    """
    text = text.strip()
    if not text:
        return None
    candidates: list[Any] = []
    try:
        doc = json.loads(text)
        candidates = doc if isinstance(doc, list) else [doc]
    except json.JSONDecodeError:
        for line in text.splitlines():
            try:
                candidates.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    results = [c for c in candidates if isinstance(c, dict) and c.get("type") == "result"]
    return results[-1] if results else None


def usage_record(
    result: dict[str, Any] | None,
    *,
    job: str,
    run_id: str | None,
    slug: str | None,
    model: str | None,
    exit_code: int | None = None,
) -> dict[str, Any]:
    """One ``ledger/usage.jsonl`` line from a parsed result (or its absence)."""
    rec: dict[str, Any] = {
        "ts": dt.datetime.now(dt.UTC).isoformat(timespec="seconds"),
        "job": job,
        "run_id": run_id,
        "slug": slug,
        "model": model,
    }
    if result is None:
        return {
            **rec,
            "conclusion": "timeout" if exit_code in (124, 137, 143) else "no_result",
            "parse_failed": True,
            "cost_usd_equiv": 0.0,
        }
    usage = result.get("usage") or {}
    by_model = {
        name: round(_num((m or {}).get("costUSD")), 4)
        for name, m in (result.get("modelUsage") or {}).items()
    }
    return {
        **rec,
        "conclusion": result.get("subtype") or ("error" if result.get("is_error") else "success"),
        "parse_failed": False,
        "duration_s": round(_num(result.get("duration_ms")) / 1000, 1),
        "num_turns": int(_num(result.get("num_turns"))),
        "cost_usd_equiv": round(_num(result.get("total_cost_usd")), 4),
        "tokens": {
            "input": int(_num(usage.get("input_tokens"))),
            "output": int(_num(usage.get("output_tokens"))),
            "cache_read": int(_num(usage.get("cache_read_input_tokens"))),
            "cache_write": int(_num(usage.get("cache_creation_input_tokens"))),
        },
        "web_searches": int(_num((usage.get("server_tool_use") or {}).get("web_search_requests"))),
        "permission_denials": len(result.get("permission_denials") or []),
        "by_model": by_model,
    }


def append(rec: dict[str, Any], path: Path = USAGE) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(rec, ensure_ascii=False) + "\n")


def spend_since(since: dt.datetime, path: Path = USAGE) -> tuple[float, int, int]:
    """``(cost, runs, slugs)`` over usage records at or after ``since``."""
    cost, runs, slugs = 0.0, 0, set()
    for rec in ledger_records(path):
        try:
            ts = dt.datetime.fromisoformat(str(rec.get("ts")))
        except ValueError:
            continue
        if ts >= since:
            cost += _num(rec.get("cost_usd_equiv"))
            runs += 1
            if rec.get("slug"):
                slugs.add(rec["slug"])
    return cost, runs, len(slugs)


def weekly_spend(now: dt.datetime | None = None, path: Path = USAGE) -> float:
    """Cost-equivalent spent over the trailing seven days -- the gate's budget input."""
    now = now or dt.datetime.now(dt.UTC)
    return spend_since(now - dt.timedelta(days=7), path)[0]


def summary_table(rec: dict[str, Any]) -> str:
    """Markdown for the GitHub Step Summary: the run's cost without opening a file."""
    tok = rec.get("tokens") or {}
    rows = [
        ("question", rec.get("slug") or "-"),
        ("model", rec.get("model") or "-"),
        ("conclusion", rec.get("conclusion")),
        ("cost (API-equivalent)", f"${rec.get('cost_usd_equiv', 0):.2f}"),
        ("turns", rec.get("num_turns", "-")),
        ("duration", f"{rec.get('duration_s', '-')} s"),
        (
            "tokens in/out/cache-read/cache-write",
            (
                f"{tok.get('input', 0)}/{tok.get('output', 0)}/"
                f"{tok.get('cache_read', 0)}/{tok.get('cache_write', 0)}"
            ),
        ),
        ("web searches", rec.get("web_searches", "-")),
        ("permission denials", rec.get("permission_denials", "-")),
    ]
    week = weekly_spend()
    return "\n".join(
        ["### Claude usage", "", "| | |", "|---|---|"]
        + [f"| {k} | {v} |" for k, v in rows]
        + ["", f"Trailing 7-day spend: ${week:.2f}", ""]
    )


def report(now: dt.datetime | None = None) -> str:
    now = now or dt.datetime.now(dt.UTC)
    lines = [f"{'window':<8} {'runs':>5} {'questions':>9} {'cost-equiv':>11} {'per question':>13}"]
    for days in (7, 30):
        cost, runs, n = spend_since(now - dt.timedelta(days=days))
        per = f"${cost / n:.2f}" if n else "-"
        lines.append(f"{days:>2} days  {runs:>5} {n:>9} {'$' + format(cost, '.2f'):>11} {per:>13}")
    return "\n".join(lines)


def main() -> None:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("record", help="append one run to ledger/usage.jsonl")
    r.add_argument("--result", type=Path, required=True, help="claude -p JSON output")
    r.add_argument("--job", required=True)
    r.add_argument("--run-id")
    r.add_argument("--slug")
    r.add_argument("--model")
    r.add_argument("--exit-code", type=int, help="the claude step's exit code")
    r.add_argument("--summary", action="store_true", help="print a Markdown table")
    sub.add_parser("report", help="rolling 7/30-day spend")
    args = ap.parse_args()

    if args.cmd == "report":
        print(report())
        return
    try:
        text = args.result.read_text(encoding="utf-8", errors="replace")
    except OSError:
        text = ""
    rec = usage_record(
        parse_result(text),
        job=args.job,
        run_id=args.run_id,
        slug=args.slug,
        model=args.model,
        exit_code=args.exit_code,
    )
    append(rec)
    if args.summary:
        print(summary_table(rec))


if __name__ == "__main__":
    main()
