"""Monte Carlo for Brent front-month settle on 2026-10-30.

Start ~$109.6 (Dec-26, early Oct 21), 8 settlements ahead, annualised vol ~48%
(OVX ~50, Brent usually a bit below WTI vol), Student-t(4) shocks for headline jumps,
and a 35% chance Barchart's CB*0 already shows Jan-27 on Dec's expiry day
(Dec-Jan backwardation ~$3, uncertain).
"""
import numpy as np

rng = np.random.default_rng(0)
n = 400_000
s0, vol, days = 109.6, 0.48, 8
sd = vol * np.sqrt(days / 252)
t = rng.standard_t(4, n) / np.sqrt(2.0)  # unit variance t(4)
price = s0 * np.exp(sd * t - 0.5 * sd**2)
roll = rng.random(n) < 0.35
spread = rng.normal(3.0, 1.0, n).clip(0.5, 6)
price = np.where(roll, price - spread, price)
for p in (5, 10, 25, 50, 75, 90, 95):
    print(p, round(float(np.percentile(price, p)), 1))
print("P<80", (price < 80).mean(), "P>135", (price > 135).mean())
