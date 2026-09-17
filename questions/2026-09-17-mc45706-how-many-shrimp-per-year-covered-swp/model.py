"""Monte-Carlo model for SWP's headline (Shr)Impact on 2027-07-01.

The resolution source is the headline number on
https://www.shrimpwelfareproject.org/shrimpact, which SWP computes as

    headline = (sum over signed agreements of committed MT) / 14 g per shrimp

so the forecast reduces to: how much *committed tonnage* is added between
2026-09-17 (36 agreements, 86,875 MT, 6.3 bn) and whatever state the page
reflects on 2027-07-01.

Modelled in agreement-count space rather than in bn-shrimp space because the
marginal agreement is smaller than the historical average one (the programme's
own eligibility floor is 1,800-2,000 MT/producer and funding allows one stunner
per producer), so growth-rate-on-the-headline double-counts the early big deals.
"""

from __future__ import annotations

import numpy as np

RNG = np.random.default_rng(20260917)
N = 400_000

BASE_BN = 6.3  # headline on 2026-09-17, retrieved same day
# Days from 2026-09-17 to 2027-07-01.
WINDOW_MONTHS = 287 / 30.44


def simulate(n: int = N) -> np.ndarray:
    """Draw n samples of the headline (Shr)Impact in billions on 2027-07-01.

    Returns
    -------
    numpy.ndarray
        Samples, rounded to the nearest 0.1 bn as the fine print requires.
    """
    # --- deal flow -------------------------------------------------------
    # Observed agreements/month: 1.12 (Apr-25 -> Sep-26), 1.25 (12m), 1.36 (8m),
    # 1.92 (Jun-26 -> Sep-26). Median 1.35, 10-90 band ~0.7-2.4.
    rate = RNG.lognormal(mean=np.log(1.35), sigma=0.48, size=n)

    # The page is refreshed episodically. A *constant* publication lag cancels
    # out (both endpoints are published values), so only the residual timing
    # noise is modelled: 0-1.5 months of extra staleness at the check date.
    lag = RNG.uniform(0.0, 1.5, size=n)
    window = np.clip(WINDOW_MONTHS - lag, 0.0, None)

    new_agreements = np.round(rate * window)

    # Marginal bn shrimp per agreement: (6.3-4.0)/15 = 0.153 observed over the
    # last 15 agreements; eligibility floor 1,800-2,000 MT => 0.13-0.14 bn.
    per_deal = np.clip(RNG.normal(0.155, 0.018, size=n), 0.11, 0.21)

    total = BASE_BN + new_agreements * per_deal

    # --- existing partners widening their committed share -----------------
    # Only 21% of partners' own 410,546 MT is committed; Seajoy has said it
    # goes 70% -> 100% by end-2027. One stunner per producer caps this.
    total += RNG.gamma(shape=1.2, scale=0.12, size=n)

    # --- step change ("HSI 2.0", country-scale deal, or a large new funder) --
    step = RNG.random(n) < 0.10
    total += step * RNG.lognormal(mean=np.log(3.5), sigma=0.6, size=n)

    # --- methodology risk -------------------------------------------------
    # (a) SWP revises the 14 g/shrimp conversion.
    revise = RNG.random(n) < 0.10
    total *= np.where(revise, np.clip(RNG.normal(1.0, 0.17, size=n), 0.65, 1.45), 1.0)

    # (b) SWP re-bases the headline onto installed (not committed) capacity:
    #     installed/committed is 54,175/86,875 = 0.62 today.
    rebase = RNG.random(n) < 0.04
    total = np.where(rebase, total * RNG.uniform(0.55, 0.75, size=n), total)

    # (c) The page is simply never refreshed before the check.
    stale = RNG.random(n) < 0.03
    total = np.where(stale, BASE_BN + RNG.uniform(0.0, 0.6, size=n), total)

    return np.round(total, 1)


def main() -> None:
    s = simulate()
    qs = [1, 5, 10, 25, 40, 50, 60, 75, 90, 95, 99]
    print("Percentiles (bn shrimp/yr):")
    for q in qs:
        print(f"  p{q:<3d} {np.percentile(s, q):6.2f}")
    print(f"  mean  {s.mean():6.2f}")
    print()
    print(f"P(< 7.0, below Metaculus range)  = {np.mean(s < 6.95):.3f}")
    print(f"P(> 12.0, above Metaculus range) = {np.mean(s > 12.05):.3f}")
    print(f"P(<= 6.3, no growth at all)      = {np.mean(s <= 6.3):.3f}")
    print(f"P(7.0-9.0)                       = {np.mean((s >= 6.95) & (s < 9.05)):.3f}")
    print(f"P(9.0-12.0)                      = {np.mean((s >= 9.05) & (s <= 12.05)):.3f}")


if __name__ == "__main__":
    main()
