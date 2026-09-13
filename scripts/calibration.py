#!/usr/bin/env python3
"""Score the ledger: Brier, log score, calibration buckets, skill vs. the community.

Only resolved questions contribute. Binary questions are scored with the Brier
score (mean squared error of the probability) and the logarithmic score; numeric
and date questions are scored by interquartile-range coverage, which is the
honest check on whether stated uncertainty bands are the right width.

Examples
--------
    uv run scripts/calibration.py
    uv run scripts/calibration.py --latest-only   # score only the final version per question
    uv run scripts/calibration.py --plot calibration.png
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common import LEDGER

EPS = 1e-6  # keeps the log score finite when a forecast sits at 0 or 1


def read_ledger() -> tuple[dict[str, list[dict]], dict[str, dict]]:
    """Split the ledger into per-slug forecast lists and per-slug resolutions."""
    forecasts: dict[str, list[dict]] = defaultdict(list)
    resolutions: dict[str, dict] = {}
    if not LEDGER.exists():
        return forecasts, resolutions
    for line in LEDGER.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        rec = json.loads(line)
        if rec.get("event") == "resolution":
            resolutions[rec["slug"]] = rec
        else:
            forecasts[rec["slug"]].append(rec)
    return forecasts, resolutions


def brier(p: float, y: float) -> float:
    """Brier score for a single binary forecast (lower is better)."""
    return (p - y) ** 2


def log_score(p: float, y: float) -> float:
    """Negative log likelihood of the outcome (lower is better)."""
    p = min(max(p, EPS), 1 - EPS)
    return -(y * math.log(p) + (1 - y) * math.log(1 - p))


def summarise(pairs: list[tuple[float, float]], label: str) -> dict[str, Any] | None:
    """Aggregate ``(probability, outcome)`` pairs into scores."""
    if not pairs:
        return None
    n = len(pairs)
    b = sum(brier(p, y) for p, y in pairs) / n
    ls = sum(log_score(p, y) for p, y in pairs) / n
    base = sum(y for _, y in pairs) / n
    # Skill vs. always predicting the observed base rate: 1.0 is perfect, 0 is no skill.
    ref = sum(brier(base, y) for _, y in pairs) / n
    skill = 1 - b / ref if ref > 0 else float("nan")
    mean_p = sum(p for p, _ in pairs) / n
    return {
        "label": label,
        "n": n,
        "brier": b,
        "log_score": ls,
        "base_rate": base,
        "mean_forecast": mean_p,
        "skill_vs_base_rate": skill,
        "bias_pp": (mean_p - base) * 100,
    }


def buckets(
    pairs: list[tuple[float, float]], width: float = 0.1
) -> list[tuple[str, int, float, float]]:
    """Bin forecasts and report mean forecast vs. observed frequency per bin."""
    bins: dict[int, list[tuple[float, float]]] = defaultdict(list)
    for p, y in pairs:
        bins[min(int(p / width), int(1 / width) - 1)].append((p, y))
    out = []
    for k in sorted(bins):
        grp = bins[k]
        lo, hi = k * width, (k + 1) * width
        out.append(
            (
                f"{lo:.0%}–{hi:.0%}",
                len(grp),
                sum(p for p, _ in grp) / len(grp),
                sum(y for _, y in grp) / len(grp),
            )
        )
    return out


def main() -> None:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument(
        "--latest-only",
        action="store_true",
        help="score only the last version of each question",
    )
    ap.add_argument("--plot", help="write a calibration plot to this PNG path")
    args = ap.parse_args()

    forecasts, resolutions = read_ledger()
    if not resolutions:
        print("No resolved questions in the ledger yet — nothing to score.")
        print(
            "Resolve one with: uv run scripts/log_forecast.py resolve <slug> --outcome yes"
        )
        return

    mine: list[tuple[float, float]] = []
    community: list[tuple[float, float]] = []
    coverage: list[tuple[str, bool]] = []

    for slug, res in resolutions.items():
        versions = sorted(forecasts.get(slug, []), key=lambda r: r.get("version", 0))
        if args.latest_only:
            versions = versions[-1:]
        outcome = res.get("outcome")
        qtype = res.get("type") or "binary"
        for v in versions:
            med = v.get("median")
            if med is None or outcome is None:
                continue
            if qtype == "binary":
                mine.append((float(med), float(outcome)))
                cp = (v.get("community") or {}).get("cp")
                if cp is not None:
                    community.append((float(cp), float(outcome)))
            else:
                lo, hi = v.get("iqr") or [None, None]
                if lo is not None and hi is not None:
                    coverage.append((slug, float(lo) <= float(outcome) <= float(hi)))

    for stats in (summarise(mine, "you"), summarise(community, "Metaculus community")):
        if not stats:
            continue
        print(f"\n== {stats['label']} ==")
        print(f"  forecasts scored : {stats['n']}")
        print(f"  Brier score      : {stats['brier']:.4f}   (lower is better)")
        print(f"  log score        : {stats['log_score']:.4f}")
        print(f"  observed base rate: {stats['base_rate']:.1%}")
        print(
            f"  mean forecast    : {stats['mean_forecast']:.1%} "
            f"({stats['bias_pp']:+.1f} pp bias)"
        )
        print(f"  skill vs base rate: {stats['skill_vs_base_rate']:.3f}")

    mine_stats, cp_stats = summarise(mine, "you"), summarise(community, "cp")
    if mine_stats and cp_stats:
        bm, bc = mine_stats["brier"], cp_stats["brier"]
        verdict = "beating" if bm < bc else "losing to"
        print(
            f"\n  → You are {verdict} the community prediction "
            f"({bm:.4f} vs {bc:.4f}, Δ {bm - bc:+.4f})."
        )

    if mine:
        print("\n== calibration by bucket ==")
        print(f"  {'bin':<10} {'n':>3} {'mean fc':>8} {'observed':>9}")
        for name, n, mp, obs in buckets(mine):
            print(f"  {name:<10} {n:>3} {mp:>8.1%} {obs:>9.1%}")

    if coverage:
        hit = sum(1 for _, ok in coverage if ok)
        print("\n== interquartile coverage (numeric/date) ==")
        print(
            f"  {hit}/{len(coverage)} = {hit / len(coverage):.0%} inside the stated IQR "
            f"(well-calibrated ≈ 50%)"
        )

    if args.plot and mine:
        try:
            import matplotlib

            matplotlib.use("Agg")
            import matplotlib.pyplot as plt
        except ImportError:
            sys.exit(
                "! matplotlib not installed — it lives in the optional 'viz' group.\n"
                "  Re-run as: uv run --group viz scripts/calibration.py --plot ..."
            )
        b = buckets(mine)
        fig, ax = plt.subplots(figsize=(5, 5))
        ax.plot([0, 1], [0, 1], "--", color="grey", lw=1, label="perfect calibration")
        ax.plot([x[2] for x in b], [x[3] for x in b], "o-", label="you")
        ax.set_xlabel("mean forecast")
        ax.set_ylabel("observed frequency")
        ax.set_title(f"Calibration (n={len(mine)})")
        ax.legend()
        fig.tight_layout()
        fig.savefig(args.plot, dpi=150)
        print(f"\nwrote {args.plot}")


if __name__ == "__main__":
    main()
