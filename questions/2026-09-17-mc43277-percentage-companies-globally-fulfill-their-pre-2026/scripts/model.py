"""Monte-Carlo model for Metaculus #43277 (cage-free commitment fulfilment, 2026-27).

The question resolves to ``fulfilled / total`` over Chicken Watch rows with
issue = Cage-Free, Victory Date 1990-2025 and Timeline >= 2026, read on
2028-01-01. Both parts move: the numerator grows as companies publish
fulfilment reports, the denominator grows as Chicken Watch back-fills
commitments it had not yet logged.

Cohorts are modelled separately because "years since the commitment's own
deadline" is the dominant driver of the fulfilment-reporting rate: almost all
reporting happens *after* a deadline passes, not before it. Cohort counts come
from ``raw/chickenwatch-cleaned-2026-09-17.csv.gz``.
"""

from __future__ import annotations

import numpy as np

RNG = np.random.default_rng(43277)
N_DRAWS = 400_000

# Cohort state on 2026-09-17, from the Chicken Watch export.
# (label, size, fulfilled_now, median gain in the 15.5 months to 2028-01-01)
#
# The gain medians are anchored on the 2025-deadline cohort's own measured path:
# ~26.8% at deadline+1.5mo (derived from Chicken Watch's published 64% for
# <=2025 and 93% for <=2024 in Feb 2026) -> 33.6% at deadline+8.5mo (measured
# today). That is ~+13pp from deadline to deadline+12mo, which is what the 2026
# cohort faces. Cohorts whose deadline has not yet passed by 2028-01-01 get
# much smaller gains, matching the near-flat 2.0-4.7% seen today across the
# 2027/2028/2030 cohorts.
COHORTS: list[tuple[str, int, int, float]] = [
    ("timeline 2026", 120, 6, 0.175),   # deadline +12 months at the read date
    ("timeline 2027", 51, 1, 0.045),    # deadline +0 months
    ("timeline 2028", 64, 3, 0.020),    # deadline -12 months
    ("timeline 2029+", 91, 2, 0.018),   # deadline -24 to -96 months
]

# Shared "tracker sweep intensity": how hard the Open Wing Alliance pushes
# verification into its Oct-2027 annual report. It moves every cohort together,
# so it -- not the idiosyncratic terms -- sets most of the interquartile width.
SWEEP_SIGMA = 0.30
COHORT_SIGMA = 0.25

# Denominator growth: 323 rows when Metaculus wrote the question, 326 today.
# Gamma(k, theta) in added rows over 15.5 months.
DEN_GAMMA_K, DEN_GAMMA_THETA = 1.6, 8.0

# Low-probability structural shock: Chicken Watch re-dates a batch of missed
# 2025 deadlines into 2027/2028, all of them "Not Reporting" -> pure dilution.
REDATE_PROB = 0.05
REDATE_MEAN = 45.0

# "Fast-sweep" regime. The Open Wing Alliance's annual report only ever covers
# deadlines of the *prior* year or earlier, so each cohort gets one dedicated
# verification sweep roughly 7-10 months after its deadline. The 2024 cohort
# (n=138) sat at ~90% about 14 months after its deadline, having had exactly one
# such sweep; the 2025 mega-cohort (n=1098) is still at 33.6% at +8.5 months and
# has not had its sweep yet. The 2026 cohort (n=120) is small like 2024's but
# shares 2025's era, backlog and headwinds, so the fast regime is the minority
# case rather than the centre.
FAST_PROB = 0.12
FAST_GAIN_2026 = 0.55
FAST_GAIN_OTHER = 2.0


def simulate(n_draws: int = N_DRAWS) -> np.ndarray:
    """Draw the resolution value (in percent) n_draws times.

    Parameters
    ----------
    n_draws : int
        Number of Monte-Carlo draws.

    Returns
    -------
    numpy.ndarray
        Simulated values of ``100 * fulfilled / total`` on 2028-01-01.
    """
    sweep = np.exp(RNG.normal(0.0, SWEEP_SIGMA, n_draws))
    fast = RNG.random(n_draws) < FAST_PROB

    numerator = np.zeros(n_draws)
    denominator = np.full(n_draws, 0.0)
    for label, size, now, gain_median in COHORTS:
        idio = np.exp(RNG.normal(0.0, COHORT_SIGMA, n_draws))
        gain = np.full(n_draws, gain_median)
        if label == "timeline 2026":
            gain = np.where(fast, FAST_GAIN_2026, gain)
        else:
            gain = np.where(fast, gain_median * FAST_GAIN_OTHER, gain)
        rate = now / size + gain * sweep * idio
        # A cohort cannot pass the ~93% plateau the mature cohorts sit at.
        rate = np.clip(rate, 0.0, 0.93)
        numerator += RNG.binomial(size, rate)
        denominator += size

    denominator += np.round(RNG.gamma(DEN_GAMMA_K, DEN_GAMMA_THETA, n_draws))

    redate = RNG.random(n_draws) < REDATE_PROB
    extra = RNG.poisson(REDATE_MEAN, n_draws) * redate
    denominator += extra
    # Re-dated rows are missed deadlines; a few still report fulfilment later.
    numerator += RNG.binomial(extra, 0.04)

    return 100.0 * numerator / denominator


def main() -> None:
    """Print the forecast distribution and the sensitivity table."""
    draws = simulate()
    qs = [5, 10, 25, 50, 75, 90, 95]
    vals = np.percentile(draws, qs)
    print("Metaculus #43277 — simulated value on 2028-01-01 (percent)")
    for q, v in zip(qs, vals):
        print(f"  p{q:02d}: {v:5.1f}%")
    print(f"  mean: {draws.mean():5.1f}%")
    print(f"  P(value <= 3.7%, i.e. no net change): {100 * (draws <= 3.72).mean():.1f}%")
    print(f"  P(value >= 30.0%, above the stated range top): {100 * (draws >= 30.03).mean():.1f}%")

    print("\nSensitivity — median under alternative assumptions:")
    base = COHORTS[0][3]
    for label, newgain in [
        ("2026 cohort gains only +7pp (Chick-fil-A-style stall)", 0.070),
        ("baseline +17.5pp", base),
        ("2026 cohort tracks the 2025 cohort fully (+28pp)", 0.280),
    ]:
        COHORTS[0] = ("timeline 2026", 120, 6, newgain)
        print(f"  {label:52s} -> {np.percentile(simulate(120_000), 50):5.1f}%")
    COHORTS[0] = ("timeline 2026", 120, 6, base)


if __name__ == "__main__":
    main()
