"""Mixture model for CBZ26 settlement on 2026-10-29 (8 trading days from 2026-10-19 ~108)."""
import numpy as np

rng = np.random.default_rng(0)
n = 400_000
spot = 108.0
# Base: no deal; ~55% annualised vol over 8 trading days (war regime), slight fat tails (t, df=4).
sd_base = 0.55 * np.sqrt(8 / 252)
t = rng.standard_t(4, n) / np.sqrt(2)  # unit variance for df=4
base = spot * np.exp(-0.005 + sd_base * t)
# Deal / Hormuz reopening path: April ceasefire analogue (Brent ~$92-95), 12% weight.
deal = 94.0 * np.exp(0.07 * rng.standard_normal(n))
w = rng.random(n) < 0.12
x = np.where(w, deal, base)
for p in (5, 10, 25, 50, 75, 90, 95):
    print(p, round(float(np.percentile(x, p)), 2))
