"""Monte-Carlo model for Metaculus #15240 / subquestion 31308, v3 (re-analysis).

End-December-2026 SPR crude stocks as they will print in the EIA *Petroleum Supply
Monthly* (MCSSTUS1) around 2027-02-26.

Consistency constraint with the September sibling (v6):
    Dec_weekly = Sep_weekly - D(10-01..10-02) - trickle(after 10-02)
                 - tranche_lifted - escalation - mandated + returns + refill
where Sep_weekly is the *same* sampler as the sibling's v6 and D is the part of the
observed 0.784 Mb week-ending-10-02 draw that fell after 30 September. Because
Sep_weekly - D == 282.983 (the observed 10-02 level) identically, December is anchored
on the observed 10-02 level, and the September and December forecasts cannot disagree
about where the series stood on 2 October.

What changed from v2: DOE's 2026-09-29 RFP for up to 40 Mb (Big Hill, Bryan Mound;
bids due 2026-10-06; deliveries scheduled November-December 2026) turns v2's 10%
"final tranche" branch into a live award-size question. The October STEO (modelling
completed 2026-10-01) assumes the full 40 Mb lifts (Nov 262.5, Dec 242.5) and no
returns until July 2027.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path

import numpy as np

N = 1_000_000
RNG = np.random.default_rng(20261009)

# ---- September leg: the sibling's v6 sampler, loaded from its file ----------------------
_SIB = (Path(__file__).resolve().parents[2]
        / "2026-09-07-mc15240-spr-crude-barrels-september-2026/raw/scenario-model-2026-10-09.py")
_spec = importlib.util.spec_from_file_location("sep_v6", _SIB)
sep = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(sep)

sep_weekly = sep.september_weekly(RNG)
sep_monthly = sep_weekly + RNG.normal(sep.BRIDGE_MEAN, sep.BRIDGE_SD, N)
d_oct12 = sep_weekly - sep.W_1002                 # part of the 10-02 week after 30 Sept
start = sep_weekly - d_oct12                      # == 282.983 for every draw

# ---- October-December flows (Mb, positive = out of the SPR unless noted) -----------------
# 1. Residual trickle of the earlier awards after 10-02. Tally: 133.5 awarded minus
#    132.459 delivered (415.442 - 282.983) = ~1.04 Mb, but DOE says "more than 133 Mb",
#    and the run-rate has been 0.78 Mb/week for two weeks. U(0.2, 2.5).
trickle = RNG.uniform(0.2, 2.5, N)

# 2. The 40 Mb RFP of 2026-09-29. Award size: June's identical offer placed 0.5 Mb;
#    March-May offers placed 133 Mb under a steep backwardation. The front of the Brent
#    curve is again steep (Dec-Jan ~$3.6/bbl on 2026-10-01) with Brent ~$100+, which makes
#    borrowing now against 2028 returns with a ~25% premium roughly break-even-to-attractive.
#    EIA STEO assumes all 40 Mb. Mixture below (22% ~nothing, 20% 1-8, 30% 8-25, 28% 25-40).
u = RNG.random(N)
award = np.select(
    [u < 0.22, u < 0.42, u < 0.72],
    [RNG.uniform(0.0, 1.0, N), RNG.uniform(1.0, 8.0, N), RNG.uniform(8.0, 25.0, N)],
    RNG.uniform(25.0, 40.0, N),
)
# Share of the award physically lifted by 31 Dec: earlier awards trickled for months.
lifted_share = RNG.uniform(0.65, 1.0, N)
tranche = award * lifted_share

# 3. Escalation beyond the 172 Mb programme (new IEA action / emergency sale).
esc = (RNG.random(N) < 0.05) * np.clip(RNG.normal(14, 7, N), 3, 30)

# 4. Congressionally mandated sale delivered in Q4 (small).
mandated = (RNG.random(N) < 0.07) * RNG.uniform(1.0, 4.0, N)

# 5. Exchange returns before 31 Dec (up). October STEO: none until July 2027; DOE
#    scheduling 40 Mb *out* of Big Hill in Nov-Dec; earlier reports of 1 Nov returns.
returns = (RNG.random(N) < 0.18) * RNG.uniform(1.5, 8.0, N)

# 6. Refill / Venezuela swap barrels delivered in 2026 (up). Polymarket 7.5% (2026-10-09).
refill = (RNG.random(N) < 0.07) * RNG.uniform(0.5, 4.0, N)

dec_weekly = start - trickle - tranche - esc - mandated + returns + refill
# Bridge: residuals were +0.5 to +1.1 Mb in the heavy-draw months (Mar-May 2026);
# widen it when December itself carries a large lift.
heavy = (tranche + esc) > 5
bridge = np.where(heavy, RNG.normal(0.4, 0.6, N), RNG.normal(0.18, 0.38, N))
dec = dec_weekly + bridge

if __name__ == "__main__":
    for name, arr in (("SEPT (check vs sibling)", sep_monthly), ("DEC 2026", dec)):
        q = np.percentile(arr, [5, 10, 25, 50, 75, 90, 95])
        print(f"{name}: p5={q[0]:.2f} p10={q[1]:.2f} p25={q[2]:.2f} MED={q[3]:.2f} "
              f"p75={q[4]:.2f} p90={q[5]:.2f} p95={q[6]:.2f} mean={arr.mean():.2f}")
    assert np.allclose(start, sep.W_1002)
    print(f"P(Dec < 275)   = {(dec < 275).mean():.1%}")
    print(f"P(Dec < 252.4) = {(dec < 252.4).mean():.1%}")
    print(f"P(Dec > Sept)  = {(dec > sep_monthly).mean():.1%}")
    print(f"mean award {award.mean():.1f}, median award {np.median(award):.1f}, "
          f"mean lifted {tranche.mean():.1f}")
    for p in (1, 2.5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 97.5, 99):
        print(f"  p{p}: {np.percentile(dec, p):.2f}")
