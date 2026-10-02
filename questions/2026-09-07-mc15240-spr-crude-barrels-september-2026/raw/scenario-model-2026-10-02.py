"""Monte-Carlo model for Metaculus #15240 / subquestion 31307, v5.

End-September-2026 SPR crude stocks as they will print in the EIA *Petroleum Supply
Monthly* (MCSSTUS1) around 2026-11-30.

What changed from v4: the 2026-09-30 WPSR (week ending 09-25) printed 283.767 Mb, a draw
of **0.785 Mb** -- roughly double the two prior 0.40 Mb weeks. Only 5 days (Sat 09-26 to
Wed 09-30) remain to project. Residual award balance: 133.5 - (415.442 - 283.767) =
1.825 Mb caps any further draw. DOE's 2026-09-29 RFP for 40 Mb schedules deliveries for
November-December (bids due 10-06), so it contributes nothing to September.

July 2026 PSM (304,810) vs weekly 07-31 (304,809): residual +1 kb on a Friday month end,
consistent with the bridge's ~0 on Friday month ends; September 30 is a Wednesday, so the
v3 bridge N(+0.18, 0.28) Mb is kept.
"""

from __future__ import annotations

import numpy as np

N = 1_000_000
ANCHOR = 283.767          # Mb, WCSSTUS1 week ending 2026-09-25 (released 2026-09-30)
LAST_DRAW = 0.785         # Mb, draw into that print (prior weeks 0.405, 0.403)
DAYS_TO_EOM = 5           # 2026-09-25 -> 2026-09-30
RESIDUAL = 1.825          # Mb, awarded minus delivered through 09-25
BRIDGE_MEAN = 0.18        # monthly minus weekly-interpolated month end (36-month fit, v3)
BRIDGE_SD = 0.28

# Regime weights (forecast.md v5 scenario table).
W_PERSIST, W_FAST, W_TAPER, W_DONE = 0.55, 0.15, 0.20, 0.10


def september(rng: np.random.Generator, n: int = N) -> tuple[np.ndarray, np.ndarray]:
    """Sample the further weekly-basis draw from 09-25 to 09-30 and its regime.

    Returns
    -------
    draw : np.ndarray
        Further draw in Mb (negative = build).
    regime : np.ndarray
        0 persistent 0.35-0.85 Mb/wk, 1 faster 0.85-1.6 Mb/wk, 2 taper, 3 finished.
    """
    u = rng.random(n)
    draw = np.empty(n)
    regime = np.empty(n, dtype=int)
    c1, c2, c3 = W_PERSIST, W_PERSIST + W_FAST, W_PERSIST + W_FAST + W_TAPER
    f = DAYS_TO_EOM / 7

    m = u < c1                                      # trickle in the 0.4-0.8 band
    draw[m] = rng.uniform(0.35, 0.85, m.sum()) * f
    regime[m] = 0
    m = (u >= c1) & (u < c2)                        # residual lifting faster
    draw[m] = rng.uniform(0.85, 1.60, m.sum()) * f
    regime[m] = 1
    m = (u >= c2) & (u < c3)                        # taper: 0.785 was a one-off lump
    draw[m] = rng.uniform(0.05, 0.35, m.sum()) * f
    regime[m] = 2
    m = u >= c3                                     # finished; flat or tiny build
    draw[m] = rng.uniform(-0.20, 0.03, m.sum())
    regime[m] = 3
    return np.minimum(draw, RESIDUAL), regime


def run(n: int = N) -> dict[str, float]:
    """Simulate the end-September monthly print, in million barrels."""
    rng = np.random.default_rng(20261002)
    draw, _ = september(rng, n)
    monthly = ANCHOR - draw + rng.normal(BRIDGE_MEAN, BRIDGE_SD, n)
    q = np.percentile(monthly, [5, 10, 25, 50, 75, 90, 95])
    return {
        "p5": q[0], "p10": q[1], "p25": q[2], "median": q[3], "p75": q[4],
        "p90": q[5], "p95": q[6],
        "mean_further_draw": float(draw.mean()),
        "P(below 283.0)": float((monthly < 283.0).mean()),
        "P(above 284.2)": float((monthly > 284.2).mean()),
    }


if __name__ == "__main__":
    for k, v in run().items():
        print(f"{k:20s} {v:,.3f}")
