"""Monte-Carlo model for GiveWell funds raised in metrics years 2026-2028.

The question asks for 100 x (F_i - F_2026) / F_2026 for i in {2027, 2028}, where F is
GiveWell's headline "funds raised" from its annual metrics report (metrics year runs
February-January).

The model decomposes funds raised into two blocks, because they are driven by very
different processes:

1. ``CG``  - the Coefficient Giving (formerly Open Philanthropy) commitment that GiveWell
   recognises as funds raised in that metrics year. This is a discrete institutional
   decision, not a smooth series: it went 300 / 350 / 100 / 100 / 100 USDm across metrics
   years 2021-2025 and jumps to a committed ~1,000 in 2026.
2. ``IND`` - everything else (individual donors and family foundations, incl. donations
   made directly to recommended charities). This is a smoother, fast-growing series:
   295 / 253 / 255 / 315 / 516 USDm across 2021-2025.

A single latent factor ``Z`` couples the post-2026 draws. It stands for "how much of the
anticipated AI-equity philanthropy actually shows up, and how early". Without it the
model would understate the tails: the world where Anthropic/OpenAI wealth arrives late
is simultaneously bad for CG's follow-on giving and for individual giving.
"""

from __future__ import annotations

import numpy as np

RNG = np.random.default_rng(20260904)
N = 400_000

IND_2025 = 516.34  # USD m, GiveWell 2025 metrics report (funds raised excl. Coefficient Giving)


def _lognormal(median: float, sigma: float, size: int, z: np.ndarray, load: float) -> np.ndarray:
    """Lognormal draw whose log-mean is shifted by a common latent factor.

    Parameters
    ----------
    median : float
        Median of the marginal distribution when ``z`` is zero.
    sigma : float
        Total log-scale dispersion.
    size : int
        Number of draws.
    z : ndarray
        Standard-normal latent factor, shared across variables.
    load : float
        Fraction of ``sigma`` driven by the common factor (0 = independent, 1 = fully
        determined by ``z``).

    Returns
    -------
    ndarray
        Draws with the requested median and dispersion.
    """
    idio = RNG.standard_normal(size) * sigma * np.sqrt(max(0.0, 1.0 - load**2))
    return median * np.exp(z * sigma * load + idio)


z = RNG.standard_normal(N)

# --- Metrics year 2026 (Feb 2026 - Jan 2027) -------------------------------------------
# Coefficient Giving announced a 1,000 USDm allocation to GiveWell recommendations for
# 2026 (July 2026), up from the 175 committed in December 2025. GiveWell's own wording
# ("near-term funding commitment") leaves open that part is recognised in 2027 instead;
# the 2022 precedent (350 recognised in full, 128 of it retained for later grantmaking)
# argues for full recognition in the commitment year.
u = RNG.random(N)
cg26 = np.empty(N)
full = u < 0.75
split = (u >= 0.75) & (u < 0.93)
other = u >= 0.93
cg26[full] = RNG.normal(1000, 50, full.sum())
cg26[split] = RNG.uniform(500, 800, split.sum())
cg26[other] = RNG.uniform(300, 1400, other.sum())
cg26 = np.clip(cg26, 150, None)
carryover = np.where(split, 1000 - cg26, 0.0)  # the part that then lands in 2027

# Individual/other giving 2026: 2025 grew 64%; 2026 has continued aid-cut salience, the
# February 2026 Anthropic employee tender (~6bn of liquidity) and an active GiveWell
# fundraising push, against a very lumpy 1m+ donor bucket that need not repeat.
g26 = _lognormal(1.48, 0.24, N, z, load=0.45)
ind26 = IND_2025 * g26
f26 = cg26 + ind26

# --- Metrics year 2027 (Feb 2027 - Jan 2028) -------------------------------------------
# CG called the 2026 level "a one-off surge rather than a new steady state" and "a bet on
# laying the groundwork for others to emerge and pick up the baton", while separately
# planning larger total grantmaking in 2027-2028. Median 400, 80% CI ~[180, 900].
cg27 = _lognormal(430, 0.63, N, z, load=0.55) + carryover
# Anthropic is reported to be targeting a late-September/early-October 2026 listing, ahead
# of the Metaculus CP median of 2026-12-23. With the modal 135-180d lockup that puts
# employee liquidity around Feb-Apr 2027, i.e. at the very start of metrics year 2027 and
# well before the December 2027 giving season. OpenAI (CP median 2027-05-18) lands later.
g27 = _lognormal(1.48, 0.40, N, z, load=0.65)
ind27 = ind26 * g27
f27 = cg27 + ind27

# --- Metrics year 2028 (Feb 2028 - Jan 2029) -------------------------------------------
cg28 = _lognormal(550, 0.70, N, z, load=0.55)
g28 = _lognormal(1.45, 0.40, N, z, load=0.65)
ind28 = ind27 * g28
f28 = cg28 + ind28

pct27 = 100.0 * (f27 - f26) / f26
pct28 = 100.0 * (f28 - f26) / f26

QS = [5, 10, 25, 50, 75, 90, 95]


def _report(name: str, arr: np.ndarray) -> None:
    q = np.percentile(arr, QS)
    print(f"{name:>10}: " + "  ".join(f"p{p}={v:,.1f}" for p, v in zip(QS, q)))


print("--- levels, USD m ---")
for nm, a in [("F2026", f26), ("F2027", f27), ("F2028", f28),
              ("CG2026", cg26), ("CG2027", cg27), ("IND2026", ind26),
              ("IND2027", ind27), ("IND2028", ind28)]:
    _report(nm, a)

print("\n--- percentage change vs 2026 ---")
_report("2027 %", pct27)
_report("2028 %", pct28)
print(f"\nP(2027 change < 0) = {(pct27 < 0).mean():.3f}")
print(f"P(2028 change < 0) = {(pct28 < 0).mean():.3f}")
print(f"P(2027 in [0,200])  = {((pct27 >= 0) & (pct27 <= 200)).mean():.3f}")
print(f"P(2028 in [0,200])  = {((pct28 >= 0) & (pct28 <= 200)).mean():.3f}")
print(f"P(2027 > 200)       = {(pct27 > 200).mean():.3f}")
print(f"P(2028 > 200)       = {(pct28 > 200).mean():.3f}")
