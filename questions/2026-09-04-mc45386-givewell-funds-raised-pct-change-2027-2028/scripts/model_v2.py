"""Monte-Carlo model v2 for GiveWell funds raised in metrics years 2026-2028.

Supersedes ``model.py`` (v1, 2026-09-04), which stays in place unchanged as the record
behind forecast v1.

What changed from v1, and why
-----------------------------
1. **AI money is its own additive block.** v1 grew all non-Coefficient-Giving giving by a
   single multiplier (x1.48 a year). That treats a step change in the donor pool as a
   growth rate. The Anthropic-linked philanthropic pool is not a trend: pre-IPO
   donor-advised-fund (DAF) holdings alone were estimated at $20-40bn at a $380bn
   valuation (Longterm Wiki, data as of March 2026), and the reported IPO target is now
   ~$2tn. It unlocks at dated events (IPO-day partial sales, then a lockup expiring
   around mid-2027), so it is modelled as ``AI_t`` on top of a slower ``BASE_t``.
2. **Correlation between CG and individual giving is no longer strongly positive.** v1
   loaded CG-2027 on the same latent "AI wealth arrives" factor as individual giving
   (0.55). Coefficient Giving funds GiveWell's recommendations only while they beat its
   own bar, so AI donors filling GiveWell's gaps partly *replaces* CG money. Good
   Ventures' own Anthropic stake pushes the other way. Net loading cut to 0.15.
3. **Some AI money lands in the base year.** Insiders may sell part of their shares at
   the IPO (now expected November 2026), so part of the wave can arrive in the December
   2026 giving season - metrics year 2026, the denominator.
4. **Explicit IPO / lockup states** instead of one lognormal, so the "delayed" and
   "bust" worlds are visible and weighted.
"""

from __future__ import annotations

import numpy as np

RNG = np.random.default_rng(20260927)
N = 400_000

IND_2025 = 516.34  # USD m, GiveWell 2025 metrics report (funds raised excl. Coefficient Giving)


def _lognormal(
    median: float | np.ndarray,
    sigma: float,
    size: int,
    z: np.ndarray,
    load: float,
) -> np.ndarray:
    """Lognormal draw whose log-mean is shifted by a common latent factor.

    Parameters
    ----------
    median : float or ndarray
        Median of the marginal distribution when ``z`` is zero.
    sigma : float
        Total log-scale dispersion.
    size : int
        Number of draws.
    z : ndarray
        Standard-normal latent factor, shared across variables.
    load : float
        Fraction of ``sigma`` driven by the common factor (0 = independent).

    Returns
    -------
    ndarray
        Draws with the requested median and dispersion.
    """
    idio = RNG.standard_normal(size) * sigma * np.sqrt(max(0.0, 1.0 - load**2))
    return median * np.exp(z * sigma * load + idio)


# Latent factor: "how much AI-equity philanthropy shows up, and how early".
z = RNG.standard_normal(N)

# IPO / lockup state. Reported plan (Sep 2026): IPO November 2026, a portion of insider
# shares sellable at listing, the rest locked "well over 180 days", free around mid-2027.
# normal  - IPO by 2026-12-31, main lockup releases by ~2027-09 (inside metrics year 2027)
# delayed - IPO slips into 2027 or the lockup runs past January 2028
# bust    - IPO pulled or a deep AI de-rating; paper wealth does not convert for years
u_state = RNG.random(N)
normal = u_state < 0.72
delayed = (u_state >= 0.72) & (u_state < 0.90)
bust = u_state >= 0.90

# --- Metrics year 2026 (Feb 2026 - Jan 2027) -------------------------------------------
# CG recognition. The CG post is titled "Increasing Our 2026 Allocation"; the 2022
# precedent recognised a full-year commitment in its year even though ~$128m was spent
# later. Against that, GiveWell called it a "near-term funding commitment", and CG
# co-funds some grants directly (e.g. the $276m AMF/DRC grant), which GiveWell may book
# when granted rather than when committed. Split weight raised from 0.18 to 0.20.
u = RNG.random(N)
cg26 = np.empty(N)
full = u < 0.72
split = (u >= 0.72) & (u < 0.92)
other = u >= 0.92
cg26[full] = RNG.normal(1000, 50, full.sum())
cg26[split] = RNG.uniform(500, 850, split.sum())
cg26[other] = RNG.uniform(300, 1400, other.sum())
cg26 = np.clip(cg26, 150, None)
carryover = np.where(split, 1000 - cg26, 0.0)

# Non-AI base. 2025 (+64%) was flattered by donors pulling gifts into calendar 2025
# ahead of the One Big Beautiful Bill Act's 0.5%-of-AGI floor and 35% cap on the value
# of itemised charitable deductions (effective 2026), and by early AI-tender money. Big
# donors are also being told GiveWell's margin is now less cost-effective after the $1bn
# (EA Forum, 2026-07-24). The February 2026 Anthropic tender (~$6bn) works the other way.
base26 = IND_2025 * _lognormal(1.38, 0.22, N, z, load=0.30)
# IPO-day partial sales can fund December 2026 gifts. Only in the normal state.
ai26 = np.where(normal, _lognormal(100.0, 1.0, N, z, load=0.60), 0.0)
f26 = cg26 + base26 + ai26

# --- Metrics year 2027 (Feb 2027 - Jan 2028) -------------------------------------------
# CG: "one-off surge rather than a new steady state"; GiveWell carries a large unspent
# balance out of 2026 (raised ~$1.75bn vs grantmaking "approaching $1bn"); crowd-out by
# AI donors. Upside: CG's stated aim to "prepare for even larger growth in 2027 and
# 2028" and Good Ventures' own Anthropic stake going liquid mid-2027.
cg27 = _lognormal(350.0, 0.70, N, z, load=0.15) + carryover
base27 = base26 * _lognormal(1.12, 0.18, N, z, load=0.30)
# Incremental AI-wealth giving that GiveWell counts in metrics year 2027.
# Sizing (normal state): pre-IPO DAF holdings of $20-40bn at a $380bn valuation scale to
# ~$100-200bn at a $1.5-2tn listing; founders' 80% pledges on ~12.6% of the company add
# ~$150-200bn (non-binding). Take a liquid philanthropic pool of $150-400bn by H2 2027;
# 2-5% of it granted in the ~5-7 months of the year after the lockup; 5-15% of that to
# GiveWell-tracked giving -> $0.15-3bn, geometric centre ~$0.7bn.
ai27 = np.select(
    [normal, delayed, bust],
    [
        _lognormal(700.0, 1.05, N, z, load=0.70),
        _lognormal(150.0, 0.90, N, z, load=0.50),
        _lognormal(40.0, 0.80, N, z, load=0.30),
    ],
)
f27 = cg27 + base27 + ai27

# --- Metrics year 2028 (Feb 2028 - Jan 2029) -------------------------------------------
# Full year of Anthropic liquidity plus OpenAI (IPO postponed to 2027; lockup lands
# mostly in 2028). CG likely higher again as Good Ventures' own stake monetises.
# AI sizing: 5-10% of a $150-400bn pool granted in the year, 5-12% of that to
# GiveWell-tracked giving -> $0.4-4.8bn, geometric centre ~$1.4bn.
cg28 = _lognormal(600.0, 0.75, N, z, load=0.30)
base28 = base27 * _lognormal(1.10, 0.18, N, z, load=0.30)
ai28 = np.select(
    [normal, delayed, bust],
    [
        _lognormal(1400.0, 1.00, N, z, load=0.75),
        _lognormal(650.0, 1.00, N, z, load=0.70),
        _lognormal(120.0, 0.90, N, z, load=0.40),
    ],
)
f28 = cg28 + base28 + ai28

pct27 = 100.0 * (f27 - f26) / f26
pct28 = 100.0 * (f28 - f26) / f26

QS = [5, 10, 25, 50, 75, 90, 95]


def _report(name: str, arr: np.ndarray) -> None:
    q = np.percentile(arr, QS)
    print(f"{name:>10}: " + "  ".join(f"p{p}={v:,.1f}" for p, v in zip(QS, q)))


if __name__ == "__main__":
    print("--- levels, USD m ---")
    for nm, a in [
        ("F2026", f26),
        ("F2027", f27),
        ("F2028", f28),
        ("CG2026", cg26),
        ("CG2027", cg27),
        ("CG2028", cg28),
        ("BASE2026", base26),
        ("AI2026", ai26),
        ("AI2027", ai27),
        ("AI2028", ai28),
    ]:
        _report(nm, a)

    print("\n--- percentage change vs 2026 ---")
    _report("2027 %", pct27)
    _report("2028 %", pct28)
    for lbl, arr in [("2027", pct27), ("2028", pct28)]:
        print(
            f"{lbl}: P(<0)={(arr < 0).mean():.3f}  P(0-200)="
            f"{((arr >= 0) & (arr <= 200)).mean():.3f}  P(>100)={(arr > 100).mean():.3f}"
            f"  P(>200)={(arr > 200).mean():.3f}"
        )
    print("\n--- 2027 median by state ---")
    for nm, m in [("normal", normal), ("delayed", delayed), ("bust", bust)]:
        print(
            f"{nm:>8}: 2027 p50={np.median(pct27[m]):+.1f}  2028 p50={np.median(pct28[m]):+.1f}"
        )
    print("\n--- 2027 median by CG-2026 recognition ---")
    for nm, m in [("full", full), ("split", split), ("other", other)]:
        print(f"{nm:>8}: 2027 p50={np.median(pct27[m]):+.1f}")
