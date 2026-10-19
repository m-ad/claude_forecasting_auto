"""Monte Carlo for the week-44 (Oct 19-25, 2026) school-closure facility count.

Mixture of two readings of the resolution value: the cumulative 累計 total (what the
criteria literally ask for) and the weekly 今週 total (what the question text mistook
for the cumulative figure: 937 and 1,703 are weekly counts in the JIHS reports).
"""

import numpy as np

rng = np.random.default_rng(46152)
n = 200_000

cum_wk41 = 4793  # JIHS report no.6, total row, cumulative (accessed 2026-10-19)
wk41 = 1703  # same report, this-week total
# Upward revisions of earlier weeks are folded into each report's cumulative (+17 in wk41).
revisions = rng.uniform(0, 60, n)

# Weekly log-growth of the underlying epidemic; sentinel grew x1.13 wk40->41, Mie
# prefecture's own count fell in wk42. Per-path drift plus per-week noise.
drift = rng.normal(0.03, 0.15, n)
noise = rng.normal(0, 0.10, (n, 3))
log_g = drift[:, None] + noise
level = wk41 * np.exp(np.cumsum(log_g, axis=1))
# Week 42 has the Sports Day holiday (Mon Oct 12): four school days.
holiday = rng.uniform(0.80, 0.95, n)
level[:, 0] *= holiday

weekly44 = level[:, 2]
cumulative44 = cum_wk41 + revisions + level.sum(axis=1)

p_cum = 0.65
pick = rng.random(n) < p_cum
mix = np.where(pick, cumulative44, weekly44)

qs = [5, 10, 25, 50, 75, 90, 95]
for name, arr in [("weekly44", weekly44), ("cumulative44", cumulative44), ("mixture", mix)]:
    print(name, {q: round(float(np.percentile(arr, q))) for q in qs})
