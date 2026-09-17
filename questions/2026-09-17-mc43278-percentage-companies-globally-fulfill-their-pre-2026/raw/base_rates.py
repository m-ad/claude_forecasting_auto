"""Reference-class base rates for Metaculus 43278, from the committed tracker snapshot.

Reads ``chickenwatch-broiler-<date>.csv`` (written by ``chickenwatch_pull.py``), so it runs
offline and reproduces every number quoted in ``forecast.md``.

The one non-obvious cut is ``victory_date < timeline``. Chicken Watch logs some pledges as
already met on the day they were recorded (victory date >= timeline); those are ~93% fulfilled
and would inflate any naive base rate. This question's filter excludes them by construction,
so the honest reference class must too.
"""

from __future__ import annotations

import collections
import csv
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
FULFILLED = "Reporting Fulfilled"


def load() -> list[dict[str, str]]:
    """Read the most recent committed broiler snapshot."""
    path = max(HERE.glob("chickenwatch-broiler-*.csv"))
    print(f"snapshot: {path.name}\n")
    with path.open() as fh:
        return list(csv.DictReader(fh))


def year(value: str) -> float | None:
    """Sheet years arrive as floats-as-text ('2026.0') and are blank when unknown."""
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def rate(rows: list[dict[str, str]], label: str) -> None:
    if not rows:
        print(f"  {label:52s} n=0")
        return
    f = sum(1 for r in rows if r["status"] == FULFILLED)
    rep = sum(1 for r in rows if r["status"] == "Reporting")
    print(f"  {label:52s} n={len(rows):5d} fulfilled={f:4d} ({100 * f / len(rows):5.2f}%) reporting={rep:4d}")


def main() -> None:
    rows = load()
    for r in rows:
        r["_vd"], r["_tl"] = year(r["victory_date"]), year(r["timeline"])
    dated = [r for r in rows if r["_vd"] is not None and r["_tl"] is not None]

    def eu(r: dict[str, str]) -> bool:
        return "Europe" in r["continent"]

    def na(r: dict[str, str]) -> bool:
        return "North America" in r["continent"] and "Europe" not in r["continent"]

    print("=== the question's own filter (Victory Date 1990-2025, Timeline >= 2026) ===")
    sel = [r for r in dated if 1990 <= r["_vd"] <= 2025 and r["_tl"] >= 2026]
    rate(sel, "denominator")
    print("  status:", dict(collections.Counter(r["status"] for r in sel)))
    print("  fulfilled:", [r["company"] for r in sel if r["status"] == FULFILLED])
    print(f"  mean lead time: {sum(r['_tl'] - r['_vd'] for r in sel) / len(sel):.2f} years")
    print("  by deadline year:")
    for tl in sorted({r["_tl"] for r in sel}):
        rate([r for r in sel if r["_tl"] == tl], f"    Timeline {int(tl)}")
    print("  by policy version:", dict(collections.Counter(r["policy_version"] for r in sel)))

    print("\n=== reference class: FORWARD-LOOKING pledges (VD < TL) whose deadline has passed ===")
    fwd = [r for r in dated if r["_vd"] < r["_tl"] <= 2025]
    rate(fwd, "all regions")
    rate([r for r in fwd if eu(r)], "Europe")
    rate([r for r in fwd if na(r)], "North America")
    c24 = [r for r in dated if r["_tl"] == 2024]
    rate(c24, "2024-deadline cohort, all regions")
    rate([r for r in c24 if na(r)], "2024-deadline cohort, US BCC (North America only)")

    print("\n=== excluded by the filter: pledges logged as already met (VD >= TL) ===")
    rate([r for r in dated if r["_vd"] >= r["_tl"]], "VD >= TL")


if __name__ == "__main__":
    main()
