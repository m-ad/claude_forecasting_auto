"""Monte-Carlo model for Metaculus #15240 / subquestion 31307, v4.

End-September-2026 SPR crude stocks as they will print in the EIA *Petroleum Supply
Monthly* (MCSSTUS1) around 2026-11-30.

What changed from v3: the 2026-09-23 WPSR (week ending 09-18) printed 284.552 Mb, a draw
of **0.405 Mb** -- identical to the prior week's 0.403. The geometric taper that v3 put
45% on has stopped; the flat "small persistent rate" regime (v3: 25%) is now the modal
one. Residual award balance: 133.5 - (415.442 - 284.552) = 2.61 Mb, which caps any
further exchange-programme draw.

The same September sampler is reused verbatim by the December sibling's model
(`2026-09-07-mc15240-spr-crude-barrels-december-2026/raw/scenario-model-2026-09-24.py`)
so the two forecasts start from one September distribution.
"""

from __future__ import annotations

import numpy as np

N = 1_000_000
ANCHOR = 284.552          # Mb, WCSSTUS1 week ending 2026-09-18 (released 2026-09-23)
LAST_DRAW = 0.405         # Mb, draw into that print (prior week 0.403)
DAYS_TO_EOM = 12          # 2026-09-18 -> 2026-09-30
RESIDUAL = 2.61           # Mb, awarded minus delivered through 09-18
BRIDGE_MEAN = 0.18        # monthly minus weekly-interpolated month end (36-month fit, v3)
BRIDGE_SD = 0.28

# Regime weights (forecast.md v4 scenario table).
W_PERSIST, W_TAPER, W_DONE, W_LIFT = 0.53, 0.25, 0.10, 0.12


def september(rng: np.random.Generator, n: int = N) -> tuple[np.ndarray, np.ndarray]:
    """Sample the further weekly-basis draw from 09-18 to 09-30 and its regime.

    Returns
    -------
    draw : np.ndarray
        Further draw in Mb (negative = build).
    regime : np.ndarray
        0 persistent, 1 taper-to-zero, 2 finished/flat, 3 residual lifts fast.
    """
    u = rng.random(n)
    draw = np.empty(n)
    regime = np.empty(n, dtype=int)
    c1, c2, c3 = W_PERSIST, W_PERSIST + W_TAPER, W_PERSIST + W_TAPER + W_DONE

    m = u < c1                                      # 0.3-0.5 Mb/week keeps trickling
    draw[m] = rng.uniform(0.30, 0.50, m.sum()) * DAYS_TO_EOM / 7
    regime[m] = 0
    m = (u >= c1) & (u < c2)                        # taper resumes toward zero
    r = rng.uniform(0.30, 0.60, m.sum())
    draw[m] = LAST_DRAW * (r + (5 / 7) * r**2)
    regime[m] = 1
    m = (u >= c2) & (u < c3)                        # finished; flat or tiny build
    draw[m] = rng.uniform(-0.30, 0.05, m.sum())
    regime[m] = 2
    m = u >= c3                                     # residual lifts fast (STEO-like path)
    draw[m] = rng.uniform(1.0, RESIDUAL, m.sum())
    regime[m] = 3
    return draw, regime


def run(n: int = N) -> dict[str, float]:
    """Simulate the end-September monthly print, in million barrels."""
    rng = np.random.default_rng(20260924)
    draw, _ = september(rng, n)
    monthly = ANCHOR - draw + rng.normal(BRIDGE_MEAN, BRIDGE_SD, n)
    q = np.percentile(monthly, [5, 25, 50, 75, 95])
    return {
        "p5": q[0], "p25": q[1], "median": q[2], "p75": q[3], "p95": q[4],
        "mean_further_draw": float(draw.mean()),
        "P(below 283.0)": float((monthly < 283.0).mean()),
        "P(above 284.7)": float((monthly > 284.7).mean()),
    }


if __name__ == "__main__":
    for k, v in run().items():
        print(f"{k:20s} {v:,.3f}")
