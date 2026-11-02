"""Band probabilities for Rosstat's Oct-2026 y/y CPI.

annual = 1.0635 * (1 + m_oct26) / 1.0050 - 1, where m_oct26 is the monthly m/m print.
m_oct26 = weekly-implied (1.14 to 26 Oct + ~0.06 for 27-31 Oct) + monthly-minus-weekly gap.
"""
import numpy as np
from scipy import stats

rng = np.random.default_rng(0)
n = 2_000_000
weekly_implied = rng.normal(1.20, 0.03, n)          # uncertainty on last 5 days
gap = stats.t.rvs(df=5, loc=-0.10, scale=0.16, size=n, random_state=1)  # monthly - weekly, pp
m = weekly_implied + gap
annual = (1.0635 * (1 + m / 100) / 1.0050 - 1) * 100
annual = np.round(annual, 2)
edges = [-np.inf, 6.895, 6.995, 7.095, 7.195, 7.295, np.inf]
labels = ["Below 6.90%", "6.90% to 6.99%", "7.00% to 7.09%", "7.10% to 7.19%",
          "7.20% to 7.29%", "7.30% or above"]
h, _ = np.histogram(annual, bins=edges)
for lab, p in zip(labels, h / n):
    print(f"{lab:16s} {p:.3f}")
print("median annual", np.median(annual), "IQR", np.percentile(annual, [25, 75]))
