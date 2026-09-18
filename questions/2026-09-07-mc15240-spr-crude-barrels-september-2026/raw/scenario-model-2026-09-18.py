"""Monte-Carlo model for Metaculus #15240 / subquestion 31307, v3.

End-September-2026 SPR crude stocks, as they will print in the EIA *Petroleum Supply
Monthly* (series MCSSTUS1) around 2026-11-30.

Two things changed from v2 and both are structural, not incremental:

1. The 2026-09-16 WPSR (week ending 09-11) showed a draw of **0.403 Mb**, the second
   consecutive collapse after 1.244 Mb. Two sub-0.5-Mb weeks in a row make "the remaining
   3.06 Mb contract balance clears by 30 September" arithmetically implausible rather than
   merely unlikely, which is what carried 30% of v2's weight.
2. The weekly -> monthly bridge is now *calibrated* rather than assumed. Regressing 36
   months of MCSSTUS1 against a linear interpolation of WCSSTUS1 at month-end gives a mean
   residual of +134 thousand barrels with SD 234 (last 12 months: +242, SD 338). v1 assumed
   SD ~600. The monthly print sits slightly ABOVE the weekly interpolation, reliably.
"""

from __future__ import annotations

import numpy as np

RNG = np.random.default_rng(20260918)
N = 1_000_000

ANCHOR = 284.957          # Mb, WCSSTUS1 week ending 2026-09-11 (released 2026-09-16)
LAST_DRAW = 0.403         # Mb, week-on-week draw into that print
DAYS_TO_EOM = 19          # 2026-09-11 -> 2026-09-30

# Bridge: monthly PSM minus linear interpolation of the weekly series at month end.
BRIDGE_MEAN = 0.18
BRIDGE_SD = 0.28


def further_draw(n: int) -> np.ndarray:
    """Draw the additional SPR drawdown between 2026-09-11 and 2026-09-30, in Mb.

    Four regimes, mixed. Weights are the scenario table in forecast.md v3.
    """
    u = RNG.random(n)
    out = np.empty(n)

    # 1) Geometric taper continues to ~zero (weekly decay ratio 0.30-0.55).
    m1 = u < 0.45
    r = RNG.uniform(0.30, 0.55, m1.sum())
    out[m1] = LAST_DRAW * (r + r**2 + (5 / 7) * r**3)

    # 2) Taper flattens at a small but persistent weekly rate.
    m2 = (u >= 0.45) & (u < 0.70)
    rate = RNG.uniform(0.25, 0.55, m2.sum())          # Mb/week
    out[m2] = rate * DAYS_TO_EOM / 7

    # 3) Programme is finished; flat, or returns begin and stocks build slightly.
    m3 = (u >= 0.70) & (u < 0.88)
    out[m3] = RNG.uniform(-0.35, 0.10, m3.sum())

    # 4) Deferred deliveries or a re-offer lift part of the 3.06 Mb residual balance.
    #    This is also the branch in which EIA's own September STEO (282.05 Mb end-Sept,
    #    contract-schedule driven) turns out to be right and the weekly series catches down.
    m4 = u >= 0.88
    out[m4] = RNG.uniform(1.2, 3.1, m4.sum())
    return out


def run(n: int = N) -> dict[str, float]:
    """Simulate the end-September monthly print, in million barrels."""
    weekly_eom = ANCHOR - further_draw(n)
    monthly = weekly_eom + RNG.normal(BRIDGE_MEAN, BRIDGE_SD, n)
    q = np.percentile(monthly, [5, 25, 50, 75, 95])
    return {
        "p5": q[0], "p25": q[1], "median": q[2], "p75": q[3], "p95": q[4],
        "mean_further_draw": float(further_draw(n).mean()),
        "P(below 283.0)": float((monthly < 283.0).mean()),
        "P(above 285.0)": float((monthly > 285.0).mean()),
    }


if __name__ == "__main__":
    for k, v in run().items():
        print(f"{k:20s} {v:,.3f}")
