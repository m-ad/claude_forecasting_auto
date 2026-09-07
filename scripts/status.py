#!/usr/bin/env python3
"""Triage open forecasts: what is due for review, resolving soon, or stale.

Examples
--------
    uv run scripts/status.py                 # urgency-ordered table
    uv run scripts/status.py --all           # include resolved questions
    uv run scripts/status.py --index         # (re)write INDEX.md
    uv run scripts/status.py --find "recession"
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common import (
    REPO,
    all_questions,
    days_until,
    find_slug,
    fmt_forecast,
    fmt_number,
    today,
)


def urgency(meta: dict[str, Any]) -> tuple[int, str]:
    """Score a question's need for attention.

    Returns
    -------
    tuple[int, str]
        ``(score, reason)`` where a higher score is more urgent. Scores are
        additive so that "overdue AND resolving next week" outranks either alone.
    """
    if meta.get("status") == "resolved":
        return (-1, "resolved")

    score, reasons = 0, []
    cur = meta.get("current") or {}

    if not cur.get("version"):
        return (100, "never forecast")

    d_review = days_until(meta.get("next_review"))
    if d_review is not None and d_review <= 0:
        score += 40 + min(-d_review, 30)
        reasons.append(f"review {-d_review}d overdue")
    elif d_review is not None and d_review <= 3:
        score += 15
        reasons.append(f"review in {d_review}d")

    d_res = days_until(
        (meta.get("dates") or {}).get("resolves")
        or (meta.get("dates") or {}).get("closes")
    )
    if d_res is not None and 0 <= d_res <= 7:
        score += 35
        reasons.append(f"resolves in {d_res}d")
    elif d_res is not None and 0 <= d_res <= 30:
        score += 15
        reasons.append(f"resolves in {d_res}d")
    elif d_res is not None and d_res < 0:
        score += 50
        reasons.append("past resolution date — check outcome")

    age = days_until(cur.get("date"))
    if age is not None and -age > 90:
        score += 10
        reasons.append(f"last version {-age}d old")

    # A wide gap to the community is a standing invitation to re-check your work.
    com = cur.get("community") or {}
    med, cp = cur.get("median"), com.get("cp")
    if meta.get("type") == "binary" and med is not None and cp is not None:
        gap = abs(med - cp)
        if gap >= 0.10:
            score += 12
            reasons.append(f"{gap:.0%} from CP")

    return (score, "; ".join(reasons) or "ok")


def rows(include_resolved: bool = False) -> list[tuple[int, str, dict, str]]:
    out = []
    for slug, meta in all_questions():
        score, reason = urgency(meta)
        if score < 0 and not include_resolved:
            continue
        out.append((score, slug, meta, reason))
    return sorted(out, key=lambda r: -r[0])


def print_table(include_resolved: bool = False) -> None:
    data = rows(include_resolved)
    if not data:
        print("No questions yet. Scaffold one with scripts/new_question.py")
        return
    print(
        f"{'urg':>4}  {'forecast':<22} {'v':>2} {'last':>6} {'resolves':>9}  slug / reason"
    )
    print("-" * 100)
    for score, slug, meta, reason in data:
        cur = meta.get("current") or {}
        age = days_until(cur.get("date"))
        d_res = days_until((meta.get("dates") or {}).get("resolves"))
        print(
            f"{score:>4}  {fmt_forecast(meta):<22} {cur.get('version') or 0:>2} "
            f"{(str(-age) + 'd') if age is not None else '—':>6} "
            f"{(str(d_res) + 'd') if d_res is not None else '—':>9}  {slug}"
        )
        print(f"{'':>4}  → {reason}")


def write_index() -> None:
    """Regenerate ``INDEX.md`` — the human entry point to the question set."""
    lines = [
        "# Question index",
        "",
        f"_Regenerated {today()} by `scripts/status.py --index`._",
        "",
        "| Question | Type | Current | v | Community (CP) | Resolves | Next review | Status |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for _, slug, meta, _ in rows(include_resolved=True):
        cur = meta.get("current") or {}
        com = cur.get("community") or {}
        cp = com.get("cp")
        cp_s = (
            f"{cp:.1%}"
            if isinstance(cp, float) and meta.get("type") == "binary"
            else (fmt_number(cp) if cp is not None else "—")
        )
        title = str(meta.get("title") or slug).replace("|", "\\|")
        lines.append(
            f"| [{title}](questions/{slug}/forecast.md) | {meta.get('type', '—')} | "
            f"{fmt_forecast(meta)} | {cur.get('version') or 0} | {cp_s} | "
            f"{(meta.get('dates') or {}).get('resolves') or '—'} | "
            f"{meta.get('next_review') or '—'} | {meta.get('status', '—')} |"
        )
    (REPO / "INDEX.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote {REPO / 'INDEX.md'}")


def main() -> None:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("--all", action="store_true", help="include resolved questions")
    ap.add_argument("--index", action="store_true", help="regenerate INDEX.md")
    ap.add_argument("--find", help="resolve a slug/url/id/title fragment to a slug")
    ap.add_argument(
        "--act",
        action="store_true",
        help="no-op flag consumed by the /status slash command",
    )
    args = ap.parse_args()

    if args.find:
        slug = find_slug(args.find)
        print(slug or "! no unique match")
        return
    if args.index:
        write_index()
        return
    print_table(args.all)


if __name__ == "__main__":
    main()
