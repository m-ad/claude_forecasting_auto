"""Monte Carlo for Hon Hai Q3 2026 net profit attributable to parent (NT$ bn).

Revenue is known (3,026.9). Uncertain: operating margin, non-operating income,
effective tax rate, non-controlling-interest (NCI) share. Q2 2026 calibration:
94.7 op + 0.06 non-op -> tax 26.2% -> 70.0 consolidated -> NCI 10.1 -> 59.97.
"""
import numpy as np

rng = np.random.default_rng(0)
n = 200_000
rev = 3026.9
opm = rng.normal(0.0375, 0.0012, n)          # Q2 3.75%, Q3'25 3.43%, Q1 3.57%
nonop = rng.normal(8.0, 8.0, n)              # Q3'25 16.4, Q2'26 0.06; FX flat in Q3
tax = rng.normal(0.235, 0.02, n)             # Q2 26.2%; Q3'25 ~20863/(70.6+16.4)=~24%
nci = rng.normal(0.145, 0.015, n)            # Q2 14.4%; FII (84%-owned) growing share
np_parent = (rev * opm + nonop) * (1 - tax) * (1 - nci)
print({p: round(float(np.percentile(np_parent, p)), 1) for p in [5, 10, 25, 50, 75, 90, 95]})
