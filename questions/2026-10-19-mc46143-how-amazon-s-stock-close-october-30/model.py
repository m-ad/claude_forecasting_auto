"""Monte Carlo for AMZN close on 2026-10-30: 9 pre-earnings sessions + one earnings jump."""
import numpy as np

rng = np.random.default_rng(0)
n = 2_000_000
# Anchor: blend of Oct 16 close (250.00) and Oct 19 premarket (255.14).
s0 = 253.0
# Pre-earnings drift: 9 sessions (Oct 19-29) at ~1.8%/day, fat-tailed (t, df=5).
pre = rng.standard_t(5, n) / np.sqrt(5 / 3) * 0.018 * np.sqrt(9)
# Earnings jump: options imply mean |move| ~7.6%; t(df=4) scaled so E|X| ~ 7.6%.
df = 4
t = rng.standard_t(df, n)
scale = 0.076 / np.mean(np.abs(rng.standard_t(df, 200_000)))
jump = t * scale
price = s0 * np.exp(pre + jump)
edges = [-np.inf, 235, 250, 265, 280, np.inf]
labels = ["<235", "235-250", "250-265", "265-280", ">=280"]
for lab, lo, hi in zip(labels, edges[:-1], edges[1:]):
    print(lab, round(float(np.mean((price >= lo) & (price < hi))), 3))
print("pctiles", np.percentile(price, [5, 25, 50, 75, 95]).round(1))
