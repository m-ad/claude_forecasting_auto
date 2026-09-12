"""v2 Monte Carlo of the SPR end-September 2026 level (million barrels), updated 2026-09-12.

Anchor moves from the week-ending-2026-08-28 print (286.604) to the week-ending-2026-09-04
print (285.400, published in the 2026-09-10 WPSR) -- a 1.204 Mb draw, sharply below the
~2.5 Mb the v1 decay-0.80 taper model implied for that week (actual decay ratio 0.386 vs
the 0.80 average of the prior four weeks). Contract balance (133.5 Mb awarded, 130.042 Mb
delivered through 09-04) is down to ~3.46 Mb -- small enough that the three v1 estimators,
which disagreed by ~6 Mb, now converge to within ~1.5 Mb of each other.
"""

from __future__ import annotations

import numpy as np

RNG = np.random.default_rng(20260912)
N = 500_000
ANCHOR = 285.400  # week ending 2026-09-04, published 2026-09-10
RESIDUAL = 3.458  # 133.5 awarded - 130.042 delivered through 09-04

# Mixture over three estimators of the 04 Sep -> 30 Sep (26-day) draw.
# A  fitted-taper continuation: geometric decay ratio 0.686 fit across all five observed
#    weekly draws (6.115, 5.268, 3.700, 3.122, 1.204) projected ~3.7 weeks forward -> ~2.1 Mb.
#    Now the central estimate (was estimator B in v1, previously in tension with the
#    contract balance; no longer is).
# B  full/near-full contract clearance by month end (the v1 "estimator A" reading) -> ~3.0 Mb.
# C  near-stop: last week's sharp deceleration is real and continues sharply -> ~0.6 Mb,
#    converging toward EIA's own (stale, Aug-vintage) STEO flat-284.8 convention.
u = RNG.random(N)
sep_draw = np.where(
    u < 0.45,
    RNG.normal(2.1, 0.9, N),
    np.where(u < 0.75, RNG.normal(3.0, 1.0, N), RNG.normal(0.6, 0.5, N)),
)
sep_draw = np.clip(sep_draw, 0.0, RESIDUAL + 1.5)  # residual is a near-hard ceiling absent a new award

# A re-offered tranche starting to lift barrels before 30 Sep: DOE news feed still silent
# through 2026-09-12 (nothing since 2026-07-09), only ~2.5 weeks left -- much less likely
# than at v1 (9%).
sep_draw += (RNG.random(N) < 0.04) * RNG.uniform(1.0, 5.0, N)

# Token refill delivery: also less likely with less time left.
sep_add = (RNG.random(N) < 0.04) * RNG.uniform(0.3, 1.2, N)

# Weekly-to-month-end mapping residual (same calibration as v1, residual SD ~0.6 Mb).
sep = ANCHOR - sep_draw + sep_add + RNG.normal(0.0, 0.5, N)

q = np.percentile(sep, [5, 10, 25, 50, 75, 90, 95])
print(
    f"SEPT 2026: p5={q[0]:.2f} p10={q[1]:.2f} p25={q[2]:.2f} MED={q[3]:.2f} "
    f"p75={q[4]:.2f} p90={q[5]:.2f} p95={q[6]:.2f}  mean={sep.mean():.2f}"
)
print(f"P(Sept < 281)  = {(sep < 281).mean():.1%}")
print(f"P(Sept > 285)  = {(sep > 285).mean():.1%}")
np.save("/tmp/sep_v2.npy", sep)
