"""Monte-Carlo model for Metaculus #15240 / subquestion 31308, v2.

End-December-2026 SPR crude stocks as they will print in the EIA *Petroleum Supply
Monthly* (MCSSTUS1) around 2027-02-26.

Consistency constraint: the September leg is the *same* sampler as the September
sibling's v4 model (anchor 284.552 Mb at 2026-09-18, four regimes, same weights), copied
here verbatim so the December distribution starts from the September distribution
actually forecast -- not from v1's stale 282.3 Mb.
"""

from __future__ import annotations

import numpy as np

N = 1_000_000
RNG = np.random.default_rng(20260924)

# ---- September leg: identical to the September sibling's v4 model -------------------
ANCHOR, LAST_DRAW, DAYS_TO_EOM, RESIDUAL = 284.552, 0.405, 12, 2.61
BRIDGE_MEAN, BRIDGE_SD = 0.18, 0.28
W_PERSIST, W_TAPER, W_DONE, W_LIFT = 0.53, 0.25, 0.10, 0.12

u = RNG.random(N)
c1, c2, c3 = W_PERSIST, W_PERSIST + W_TAPER, W_PERSIST + W_TAPER + W_DONE
sep_draw = np.empty(N)
regime = np.empty(N, dtype=int)
m = u < c1
sep_draw[m] = RNG.uniform(0.30, 0.50, m.sum()) * DAYS_TO_EOM / 7
regime[m] = 0
m = (u >= c1) & (u < c2)
r = RNG.uniform(0.30, 0.60, m.sum())
sep_draw[m] = LAST_DRAW * (r + (5 / 7) * r**2)
regime[m] = 1
m = (u >= c2) & (u < c3)
sep_draw[m] = RNG.uniform(-0.30, 0.05, m.sum())
regime[m] = 2
m = u >= c3
sep_draw[m] = RNG.uniform(1.0, RESIDUAL, m.sum())
regime[m] = 3
sep_weekly = ANCHOR - sep_draw                       # true end-Sept level, weekly basis
sep_monthly = sep_weekly + RNG.normal(BRIDGE_MEAN, BRIDGE_SD, N)

# ---- October-December ---------------------------------------------------------------
# 1. The rest of the awarded exchange balance. In the persistent-trickle and fast-lift
#    regimes it keeps going until the balance is gone; in the taper regime a little
#    more lands; in the finished regime nothing. Award-tally uncertainty (the trickle
#    may be something other than exchange barrels, e.g. mandated-sale deliveries) adds
#    up to ~1.5 Mb in the trickle regime.
left = np.clip(RESIDUAL - np.clip(sep_draw, 0, None), 0, None)
frac = np.select(
    [regime == 0, regime == 1, regime == 2, regime == 3],
    [RNG.uniform(0.6, 1.0, N), RNG.uniform(0.0, 0.3, N), np.zeros(N), np.ones(N)],
)
oct_dec_tail = left * frac + (regime == 0) * RNG.uniform(0.0, 1.5, N)

# 2. Exchange returns (up). Secondary sources still say returns start 2026-11-01 at Big
#    Hill; GAO (May 2026) had Big Hill LE2 finishing in early 2028 and EIA's STEO models
#    no returns before mid-2027; the June-RFP write-up puts returns "primarily throughout
#    2027". v1: 45%. v2: 38%. Nov+Dec volume if they start: 2-10 Mb.
returns = (RNG.random(N) < 0.38) * RNG.uniform(2.0, 10.0, N)

# 3. Final ~38 Mb tranche re-offered and delivering before 31 Dec (down). DOE silent
#    since 2026-07-09 even through Brent at $104.8 (2026-09-17) and record diesel.
#    Less runway than at v1 (an RFP now needs ~3 weeks to award, then weeks to lift).
tranche = (RNG.random(N) < 0.10) * np.clip(RNG.normal(16, 7, N), 3, 38)

# 4. Fresh escalation -> releases beyond the 172 Mb programme (down). Hormuz still
#    restricted, Brent $103 on 2026-09-23, record diesel: nudged up from 7% to 8%.
esc = (RNG.random(N) < 0.08) * np.clip(RNG.normal(16, 7, N), 4, 35)

# 5. FY2027 congressionally mandated sale executed in Q4 (down, small).
mandated = (RNG.random(N) < 0.10) * RNG.uniform(1.0, 4.0, N)

# 6. Refill purchases / Venezuela heavy-for-light swap barrels delivered in 2026 (up).
#    Polymarket "Venezuelan oil added to SPR by Dec 31" 7.5% (2026-09-24).
refill = (RNG.random(N) < 0.08) * RNG.uniform(0.5, 4.0, N)

dec_weekly = sep_weekly - oct_dec_tail - tranche - esc - mandated + returns + refill
dec = dec_weekly + RNG.normal(BRIDGE_MEAN, BRIDGE_SD + 0.1, N)

if __name__ == "__main__":
    for name, arr in (("SEPT (check vs sibling)", sep_monthly), ("DEC 2026", dec)):
        q = np.percentile(arr, [5, 10, 25, 50, 75, 90, 95])
        print(f"{name}: p5={q[0]:.2f} p10={q[1]:.2f} p25={q[2]:.2f} MED={q[3]:.2f} "
              f"p75={q[4]:.2f} p90={q[5]:.2f} p95={q[6]:.2f} mean={arr.mean():.2f}")
    print(f"P(Dec < 275)   = {(dec < 275).mean():.1%}")
    print(f"P(Dec < 252.4) = {(dec < 252.4).mean():.1%}")
    print(f"P(Dec > Sept)  = {(dec > sep_monthly).mean():.1%}")
    print(f"P(Dec > 285)   = {(dec > 285).mean():.1%}")
    print(f"mean Oct-Dec programme tail = {oct_dec_tail.mean():.2f} Mb")
