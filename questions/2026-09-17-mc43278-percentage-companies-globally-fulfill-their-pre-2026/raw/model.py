"""Scenario mixture over the Chicken Watch fulfilled count on 2028-01-01 (Metaculus 43278).

The question's scaling decodes to integer fulfilled counts 4..60 against a denominator of 406,
so we model the count F and the (slowly drifting) denominator separately and read the
percentage quantiles off the mixture.
"""

from __future__ import annotations

import numpy as np

N = 600_000
# (label, weight, low, high) on the fulfilled count F at 2028-01-01
SCENARIOS = [
    ("S0 rows removed / regression", 0.04, 3, 5),
    ("S1 tracker stasis", 0.28, 5, 10),
    ("S2 slow drip (normal 2027 reporting cycle)", 0.34, 10, 19),
    ("S3 deadline-driven update pass", 0.22, 19, 36),
    ("S4 strong catch-up", 0.09, 36, 66),
    ("S5 mass reclassification", 0.03, 66, 140),
]


def main() -> None:
    rng = np.random.default_rng(43278)
    w = np.array([s[1] for s in SCENARIOS])
    idx = rng.choice(len(SCENARIOS), size=N, p=w / w.sum())
    lo = np.array([s[2] for s in SCENARIOS])[idx]
    hi = np.array([s[3] for s in SCENARIOS])[idx]
    f = np.floor(rng.uniform(lo, hi + 1)).astype(int)

    # Denominator: 406 at question creation (2026-06-20), 405 on 2026-09-17. Base case holds
    # near 400; the 10% branch is Chicken Watch purging withdrawn/lapsed rows wholesale, which
    # raises the percentage without any company doing anything.
    purge = rng.random(N) < 0.10
    denom = np.where(purge, rng.uniform(300, 385, N), rng.normal(400, 7, N))
    pct = 100.0 * f / denom

    for q in (5, 10, 25, 40, 50, 60, 75, 90, 95):
        print(f"  p{q:<3d} = {np.percentile(pct, q):6.2f}%   (F = {int(np.percentile(f, q))})")
    print(f"  mean = {pct.mean():.2f}%")
    for label, weight, a, b in SCENARIOS:
        print(f"  {label:44s} w={weight:.2f}  F {a:3d}-{b:3d}")
    for label, mask in (
        ("P(<=2.5%)", pct <= 2.5),
        ("P(<=5%)", pct <= 5),
        ("P(>10%)", pct > 10),
        ("P(>14.9%, above the open bound)", pct > 14.9),
        ("P(F<=4, at the 0.86% floor)", f <= 4),
    ):
        print(f"  {label:34s} {mask.mean():.3f}")


if __name__ == "__main__":
    main()
