#!/usr/bin/env python3
"""Score the ledger: Brier, log score, calibration buckets, skill vs. the community.

Only resolved questions contribute. Binary questions are scored with the Brier
score (mean squared error of the probability) and the logarithmic score; numeric
and date questions are scored by interquartile-range coverage, which is the
honest check on whether stated uncertainty bands are the right width.

Multiple-choice questions are scored from each version's recorded option vector
(the ledger's ``distribution.probabilities``) with the multi-class Brier score
and the log score of the option that happened. Versions logged before that field
existed record only the leading option's probability, not which option led, so
they cannot be scored and are counted separately instead.

Examples
--------
    uv run scripts/calibration.py
    uv run scripts/calibration.py --latest-only   # score only the final version per question

Text output only. The bot has no human watching a plot appear, so there is no
plotting path and no plotting dependency.
"""

from __future__ import annotations

import argparse
import math
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common import LEDGER, ledger_records

EPS = 1e-6  # keeps the log score finite when a forecast sits at 0 or 1


def read_ledger() -> tuple[dict[str, list[dict]], dict[str, dict]]:
    """Split the ledger into per-slug forecast lists and per-slug resolutions."""
    forecasts: dict[str, list[dict]] = defaultdict(list)
    resolutions: dict[str, dict] = {}
    for rec in ledger_records(LEDGER):
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


def mc_brier(probs: dict[str, float], outcome: str) -> float:
    """Multi-class Brier score: squared error summed over options.

    0 is perfect and 2 is maximally wrong; a uniform guess over K options scores
    1 - 1/K. The vector is renormalised first, because one-decimal percentages
    need not sum to exactly 1.
    """
    total = sum(probs.values())
    return sum(
        (p / total - (1.0 if k == outcome else 0.0)) ** 2 for k, p in probs.items()
    )


def mc_log_score(probs: dict[str, float], outcome: str) -> float:
    """Negative log probability given to the option that happened."""
    p = probs.get(outcome, 0.0) / sum(probs.values())
    return -math.log(min(max(p, EPS), 1.0))


def mc_label(outcome: Any, labels: list[str]) -> str | None:
    """The option label a resolution names, or None if it names none of them.

    Tolerates the one legacy mis-coding: before labels were stored verbatim,
    ``log_forecast.py resolve`` turned a numeric option label such as "0" or "2"
    into the float 0.0 or 2.0.
    """
    if str(outcome) in labels:
        return str(outcome)
    if (
        isinstance(outcome, float)
        and outcome.is_integer()
        and str(int(outcome)) in labels
    ):
        return str(int(outcome))
    return None


def summarise_mc(items: list[tuple[dict[str, float], str]]) -> dict[str, Any] | None:
    """Aggregate ``(option vector, outcome label)`` pairs into scores."""
    if not items:
        return None
    n = len(items)
    b = sum(mc_brier(p, y) for p, y in items) / n
    # Skill vs. a uniform guess over each question's options.
    ref = sum(1 - 1 / len(p) for p, _ in items) / n
    return {
        "n": n,
        "brier": b,
        "log_score": sum(mc_log_score(p, y) for p, y in items) / n,
        "skill_vs_uniform": 1 - b / ref if ref > 0 else float("nan"),
        "hit_rate": sum(1 for p, y in items if max(p, key=p.get) == y) / n,
    }


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
    mc: list[tuple[dict[str, float], str]] = []
    unscored: dict[str, int] = defaultdict(int)

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
            elif qtype == "multiple_choice":
                probs = (v.get("distribution") or {}).get("probabilities")
                label = mc_label(outcome, list(probs)) if probs else None
                if label is None:
                    reason = (
                        "no option vector" if not probs else "outcome not an option"
                    )
                    unscored[f"multiple choice ({reason})"] += 1
                    continue
                mc.append((probs, label))
            else:
                lo, hi = v.get("iqr") or [None, None]
                try:
                    inside = float(lo) <= float(outcome) <= float(hi)
                except (TypeError, ValueError):
                    # e.g. "above upper bound" or an ISO date: not comparable here.
                    unscored[f"{qtype} (non-numeric outcome or IQR)"] += 1
                    continue
                coverage.append((slug, inside))

    mine_stats = summarise(mine, "you")
    cp_stats = summarise(community, "Metaculus community")
    for stats in (mine_stats, cp_stats):
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

    mc_stats = summarise_mc(mc)
    if mc_stats:
        print("\n== multiple choice ==")
        print(f"  forecasts scored : {mc_stats['n']}")
        print(f"  Brier (multi-class): {mc_stats['brier']:.4f}   (0 best, 2 worst)")
        print(f"  log score        : {mc_stats['log_score']:.4f}")
        print(f"  skill vs uniform : {mc_stats['skill_vs_uniform']:.3f}")
        print(f"  leading option won: {mc_stats['hit_rate']:.0%}")

    if unscored:
        print("\n== not scored ==")
        for why, n in sorted(unscored.items()):
            print(f"  {n} version(s): {why}")



if __name__ == "__main__":
    main()
