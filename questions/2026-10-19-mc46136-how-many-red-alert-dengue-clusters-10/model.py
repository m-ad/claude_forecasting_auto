"""Red-cluster count on the first NEA snapshot dated >= 2026-10-29.

Existing Red clusters survive independently with judged probabilities; new Reds
(yellow upgrades or fresh clusters crossing 10 cases) arrive as a Poisson count.
"""

import numpy as np

survive = {"Lentor Gardens/Tung Po Ave": 0.88, "Bishan St 12": 0.72, "Ho Ching Rd": 0.68}
new_red_mean = 0.45

dist = np.array([1.0])
for p in survive.values():
    dist = np.convolve(dist, [1 - p, p])
k = np.arange(12)
pois = np.exp(-new_red_mean) * new_red_mean**k / np.array([np.math.factorial(int(i)) if hasattr(np, "math") else 1 for i in k]) if False else None
from math import exp, factorial  # noqa: E402

pois = np.array([exp(-new_red_mean) * new_red_mean**i / factorial(i) for i in k])
total = np.convolve(dist, pois)[:12]
total /= total.sum()
cdf = np.cumsum(total)
for i, (p, c) in enumerate(zip(total, cdf)):
    print(f"{i}: {p:.3f}  cdf {c:.3f}")
print("mean", (np.arange(len(total)) * total).sum())
