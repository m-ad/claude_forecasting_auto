"""Monte Carlo for Serbia Oct 2026 CPI y/y from Sep 2026 y/y and the Oct 2025 base month.

y/y_Oct26 = (1 + y/y_Sep26) * (1 + m/m_Oct26) / (1 + m/m_Oct25) - 1, rounded to 0.1.
"""
import numpy as np

rng = np.random.default_rng(0)
n = 400_000
sep = rng.uniform(4.05, 4.15, n) / 100          # published 4.1 is rounded
base = 0.0049                                    # Oct 2025 m/m (+0.49%)
hike = rng.random(n) < 0.05                     # electricity tariff hike recorded in Oct 2026
# m/m without hike: typical Oct 0.26-0.49, recent 2026 months -0.2..0.5, PPI 10.5% upstream
mm = rng.normal(0.33, 0.28, n) / 100 + hike * rng.uniform(0.15, 0.35, n) / 100
yy = ((1 + sep) * (1 + mm) / (1 + base) - 1) * 100
yy = np.round(yy, 1)
for q in [5, 10, 25, 50, 75, 90, 95]:
    print(q, round(float(np.percentile(yy, q)), 2))
print("P(>4.5)", (yy > 4.5).mean())
