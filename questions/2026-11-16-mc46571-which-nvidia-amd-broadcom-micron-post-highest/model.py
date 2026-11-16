"""Monte Carlo: which of NVDA, AMD, AVGO, MU has the highest 10-session return.

Assumptions (speculative, from search snippets dated 2026-11): annualised vols
NVDA 60 % + an earnings jump (sd 9 %, with 50 % pass-through to peers),
AMD 80 %, MU 70 %, AVGO 60 %; pairwise correlation 0.65; zero drift.
"""
import numpy as np

rng = np.random.default_rng(0)
n = 400_000
days = 9.5  # Nov 16-25 (8 sessions) + Nov 27 half session, Nov 13 close is the base
vols = np.array([0.60, 0.80, 0.60, 0.70])  # NVDA, AMD, AVGO, MU
sd = vols * np.sqrt(days / 252)
rho = 0.65
cov = np.full((4, 4), rho) * np.outer(sd, sd)
np.fill_diagonal(cov, sd**2)
r = rng.multivariate_normal(np.zeros(4), cov, size=n)
jump = rng.standard_t(4, size=n) * 0.09 / np.sqrt(2)
r[:, 0] += jump
r[:, 1:] += 0.5 * jump[:, None]
win = np.bincount(r.argmax(axis=1), minlength=4) / n
for name, p in zip(["NVDA", "AMD", "AVGO", "MU"], win):
    print(f"{name}: {p:.3f}")
