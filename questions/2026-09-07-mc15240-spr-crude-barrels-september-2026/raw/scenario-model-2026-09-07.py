"""Monte-Carlo the SPR end-September and end-December 2026 levels (million barrels).

Anchor is the EIA weekly series (WCSSTUS1) for the week ending 2026-08-28, because
the resolution series (monthly MCSSTUS1) is the same stock read at month end:
interpolating the weekly path to the last calendar day reproduced the three
published 2026 drawdown months (Apr/May/Jun) to within 1.1 Mb.

Three independent estimators of the remaining September draw disagree, so the
September draw is modelled as a mixture over them rather than as one number.
"""

from __future__ import annotations

import numpy as np

RNG = np.random.default_rng(20260907)
N = 500_000
ANCHOR = 286.604  # week ending 2026-08-28

# --- September: mixture over three estimators of the 28 Aug -> 30 Sep draw ---
# A  contract arithmetic: 133.5 Mb awarded across five tranches (45.2 + 8.5 +
#    26.0 + 53.3 + 0.5) minus the 128.8 Mb already drawn from the 415.442 Mb
#    February plateau leaves ~4.7 Mb, most of which lands in September. This is
#    a hard physical constraint, so it carries the most weight.
# B  extrapolate the observed weekly taper (-6.1, -5.3, -3.7, -3.1; mean decay
#    ratio ~0.80) to 30 September.
# C  EIA's own August STEO, which puts end-September at 284.8 Mb -- i.e. the
#    programme stops almost immediately.
u = RNG.random(N)
sep_draw = np.where(
    u < 0.55,
    RNG.normal(4.3, 1.3, N),
    np.where(u < 0.75, RNG.normal(7.0, 2.0, N), RNG.normal(2.0, 1.1, N)),
)
sep_draw = np.clip(sep_draw, 0.0, None)

# A re-offered final tranche could start lifting barrels inside September.
sep_draw += (RNG.random(N) < 0.09) * RNG.uniform(1.0, 7.0, N)

# Refill/return deliveries in September: near-impossible (Big Hill LE2 unfinished,
# SPR Petroleum Account depleted) but not quite zero.
sep_add = (RNG.random(N) < 0.06) * RNG.uniform(0.3, 1.5, N)

# Weekly-to-month-end mapping residual, from the three published 2026 months.
sep = ANCHOR - sep_draw + sep_add + RNG.normal(0.0, 0.6, N)

# --- October to December ---------------------------------------------------
# Whatever the current programme still owes after September.
oct_tail = np.clip(RNG.normal(4.7, 2.2, N) - sep_draw, 0.0, None) * RNG.uniform(0.5, 1.0, N)

# Exchange returns contractually start 1 Nov 2026 (Big Hill), but that needs the
# LE2 life-extension build finished, and EIA's STEO assumes no returns before
# July 2027. Fill capability caps two months at roughly 26 Mb.
returns = (RNG.random(N) < 0.45) * np.clip(RNG.gamma(2.0, 3.0, N), 0, 26)

# Final ~38 Mb tranche re-offered, clearing, and delivering before 31 December.
tranche = (RNG.random(N) < 0.13) * np.clip(RNG.normal(18, 8, N), 3, 38)

# A fresh escalation producing releases beyond the 172 Mb programme.
esc = (RNG.random(N) < 0.07) * np.clip(RNG.normal(18, 7, N), 4, 35)

# FY2027 congressionally mandated sale (7 Mb split over FY26-27) executed in Q4.
mandated = (RNG.random(N) < 0.10) * RNG.uniform(2.0, 4.0, N)

# Refill purchases / Venezuela-swap barrels actually delivered inside 2026.
refill = (RNG.random(N) < 0.12) * RNG.uniform(0.5, 5.0, N)

dec = sep - oct_tail - tranche - esc - mandated + returns + refill + RNG.normal(0.0, 0.9, N)

for name, arr in (("SEPT 2026", sep), ("DEC 2026", dec)):
    q = np.percentile(arr, [5, 10, 25, 50, 75, 90, 95])
    print(
        f"{name}: p5={q[0]:.1f} p10={q[1]:.1f} p25={q[2]:.1f} MED={q[3]:.1f} "
        f"p75={q[4]:.1f} p90={q[5]:.1f} p95={q[6]:.1f}  mean={arr.mean():.1f}"
    )

print(f"\nP(Sept < 280)              = {(sep < 280).mean():.1%}")
print(f"P(Sept > 284)              = {(sep > 284).mean():.1%}")
print(f"P(Dec  < 275)              = {(dec < 275).mean():.1%}")
print(f"P(Dec  < 252.4)            = {(dec < 252.4).mean():.1%}")
print(f"P(Dec  > Sept)             = {(dec > sep).mean():.1%}")
print(f"P(Dec in 280-288)          = {((dec > 280) & (dec < 288)).mean():.1%}")
np.save("/tmp/claude-0/-home-user-claude-forecasting/1f0ec44f-2ac4-5f21-b2a2-13736d821084/scratchpad/sep.npy", sep)
np.save("/tmp/claude-0/-home-user-claude-forecasting/1f0ec44f-2ac4-5f21-b2a2-13736d821084/scratchpad/dec.npy", dec)
