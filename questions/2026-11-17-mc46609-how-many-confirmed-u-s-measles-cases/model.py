"""Monte Carlo: CDC 2026 measles total in the update governing Nov 27, 2026."""
import numpy as np

rng = np.random.default_rng(1)
n = 200_000
base = 5412
# weekly increment: lognormal around ~255, recent 230-330, Oct avg ~240
def inc(size, med=255, s=0.28):
    return med * np.exp(rng.normal(0, s, size))

# common level shock (trend persistence across weeks)
level = np.exp(rng.normal(0, 0.18, n))
w1 = inc(n) * level
w2 = inc(n) * level
w3 = inc(n) * level
holiday = rng.uniform(0.6, 1.0, n)  # Thanksgiving-week reporting lag on 2nd increment

u = rng.uniform(size=n)
# 60%: published Fri Nov 27 (2 increments, second holiday-depressed)
# 10%: published Mon/Tue Nov 30-Dec 1 with Wed Nov 25 cutoff (2 increments, mild depression)
# 30%: no Nov 27 update (published Nov 25 or skipped) -> Dec 4 update governs (3 increments)
two = base + w1 + w2 * holiday
two_b = base + w1 + w2 * np.maximum(holiday, 0.85)
three = base + w1 + w2 * holiday + w3
total = np.where(u < 0.60, two, np.where(u < 0.70, two_b, three))
for p in [5, 10, 25, 50, 75, 90, 95]:
    print(p, round(float(np.percentile(total, p))))
