"""Simulate UNESCO verified-damaged count shown at end of 2026 (563 as of 2026-09-29)."""
import json

import numpy as np

rng = np.random.default_rng(7)
N = 200_000
base = 563
# months between 29 Sep and the as-of date of the last update published in 2026
no_update = rng.random(N) < 0.08
dt = rng.uniform(1.4, 2.7, N)
dt[no_update] = 0.0
# monthly verification rate: 5.0 (12-mo), 6.1 (since Mar), 7.7 (since May); intensifying strikes -> 7.0 median
rate = rng.lognormal(np.log(7.0), 0.35, N)
# lumpy batches: gamma-Poisson with dispersion k
k = 4.0
lam = rate * dt
inc = rng.poisson(rng.gamma(k, np.maximum(lam, 1e-9) / k))
x = base + inc
pct = {p: int(np.percentile(x, p)) for p in (5, 10, 25, 50, 75, 90, 95)}
print(pct, "mean", x.mean().round(1), "P(>660)", (x > 660).mean())
vals, cnt = np.unique(np.clip(x, 560, 661), return_counts=True)
pmf = {int(v): round(c / N, 4) for v, c in zip(vals, cnt)}
print(pmf)
vals, cnt = np.unique(x, return_counts=True)
pm = {}
for v, c in zip(vals, cnt):
    key = str(int(min(v, 661)))
    pm[key] = pm.get(key, 0) + c / N
pm = {k: round(p, 5) for k, p in pm.items() if p >= 5e-6}
s = sum(pm.values())
pm = {k: round(p / s, 5) for k, p in pm.items()}
with open("unesco_pmf.json", "w") as fh:
    json.dump({"pmf": pm}, fh)
