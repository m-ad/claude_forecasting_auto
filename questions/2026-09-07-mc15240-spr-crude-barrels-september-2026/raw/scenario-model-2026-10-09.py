"""Monte-Carlo model for Metaculus #15240 / subquestion 31307, v6.

End-September-2026 SPR crude stocks as they will print in the EIA *Petroleum Supply
Monthly* (MCSSTUS1) around 2026-11-30.

What changed from v5: the 2026-10-07 WPSR printed the week ending 2026-10-02 at
282.983 Mb, a draw of 0.784 Mb (same size as the week before). End-September is now
*bracketed* by two observed weekly levels: 283.767 (09-25) and 282.983 (10-02). The only
unknown on the weekly basis is what share f of that week's 0.784 Mb landed after the
30 September cut. Calendar-linear interpolation gives f = 2/7 (-> 283.207). Lifts are
lumpy (cargo-sized), so f gets a smooth component around 2/7 and a lumpy U(0, 1)
component. The monthly print is then weekly-basis + bridge N(+0.18, 0.28) Mb, unchanged
from v3-v5 (August PSM, the first mid-week test since June, prints ~2026-10-30).
"""

from __future__ import annotations

import numpy as np

N = 1_000_000
W_0925 = 283.767          # Mb, WCSSTUS1 week ending 2026-09-25
W_1002 = 282.983          # Mb, WCSSTUS1 week ending 2026-10-02 (released 2026-10-07)
WEEK_DRAW = W_0925 - W_1002
BRIDGE_MEAN, BRIDGE_SD = 0.18, 0.28
W_SMOOTH = 0.60           # weight on near-linear intra-week profile


def september_weekly(rng: np.random.Generator, n: int = N) -> np.ndarray:
    """Sample the true end-September level on the weekly basis (Mb).

    Parameters
    ----------
    rng : np.random.Generator
        Random generator.
    n : int
        Number of draws.

    Returns
    -------
    np.ndarray
        End-September weekly-basis level, bounded by the two observed weekly prints.
    """
    smooth = rng.random(n) < W_SMOOTH
    # f = share of the week's draw that happened after 30 September.
    f = np.where(smooth, rng.uniform(0.10, 0.46, n), rng.uniform(0.0, 1.0, n))
    return W_1002 + WEEK_DRAW * f


def september_monthly(rng: np.random.Generator, n: int = N) -> np.ndarray:
    """Weekly-basis level plus the weekly->monthly bridge."""
    return september_weekly(rng, n) + rng.normal(BRIDGE_MEAN, BRIDGE_SD, n)


if __name__ == "__main__":
    rng = np.random.default_rng(20261009)
    s = september_monthly(rng)
    q = np.percentile(s, [5, 10, 25, 50, 75, 90, 95])
    print("SEPT: " + " ".join(f"p{p}={v:.3f}" for p, v in zip([5, 10, 25, 50, 75, 90, 95], q)))
    print(f"mean={s.mean():.3f}  P(<283.0)={(s < 283.0).mean():.1%}  P(>283.8)={(s > 283.8).mean():.1%}")
    rng = np.random.default_rng(1)
    s0 = september_weekly(rng) + rng.normal(0.0, BRIDGE_SD, N)
    print(f"sensitivity, unbiased bridge: median={np.median(s0):.3f} "
          f"IQR=[{np.percentile(s0, 25):.3f}, {np.percentile(s0, 75):.3f}]")
