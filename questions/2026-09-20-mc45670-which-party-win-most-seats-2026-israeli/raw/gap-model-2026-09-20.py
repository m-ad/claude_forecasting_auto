"""Monte-Carlo over the Likud-minus-Yashar seat gap on 2026-10-27.

The question is decided by the sign of a single quantity: the seat gap between
Likud and Yashar. Modelling the gap directly (rather than each party's seat
count) keeps the correlated component -- a swing that moves both parties in
opposite directions -- inside one random variable, which is where essentially
all of the uncertainty lives.

Three terms:

``gap_0``
    Today's house-weighted polling gap. The two Filber-lineage houses
    (Channel 14, and i24/Direct Polls -- the firm Filber founded) are pooled
    and down-weighted, because they are not independent of each other and
    Wikipedia's own polling page flags Filber's Likud affiliation.
``drift``
    Movement from five weeks out to the result, calibrated on the 2015-2022
    Israeli elections, shrunk toward zero for the usual small-sample reasons.
``house``
    Residual uncertainty about which house set is right, sized at the spread
    between a mainstream-only average and an all-houses average.

Run: uv run questions/<slug>/raw/gap-model-2026-09-20.py
"""
from __future__ import annotations

import numpy as np

RNG = np.random.default_rng(45670)
N = 2_000_000

# --- today's polling base (fieldwork 2026-09-01 .. 2026-09-17) ---------------
# Mainstream houses (Kan 11, Maariv, Ch12, Ch13, Ch16, Zman Yisrael, Walla,
# Israel Hayom): September mean (n=22) Likud 20.36 / Yashar 23.32; the six most
# recent (14-17 Sep) run Likud 19.67 / Yashar 23.00. Blend the two evenly, so the
# latest batch gets extra weight without the average being one week of noise.
MAINSTREAM_LIKUD, MAINSTREAM_YASHAR = 20.0, 23.2
# Filber-lineage houses (Channel 14 + i24/Direct Polls), September mean (n=8).
FILBER_LIKUD, FILBER_YASHAR = 29.3, 21.6
W_FILBER = 0.10

gap_0 = ((1 - W_FILBER) * MAINSTREAM_LIKUD + W_FILBER * FILBER_LIKUD) - \
        ((1 - W_FILBER) * MAINSTREAM_YASHAR + W_FILBER * FILBER_YASHAR)

# --- drift, five weeks out -> result ----------------------------------------
# Observed (Likud gap vs. its nearest rival, seats): 2015 +4.5, 2019A +4.5,
# 2019B -1.5, 2021 +1.7, 2022 ~+1.0.  Sample mean +2.0, sd 2.5.  Shrunk ~40%
# toward zero, sd inflated for parameter uncertainty and for the live campaign
# (Netanyahu's anti-Ra'am push; a possible Herzog pardon decision).
DRIFT_MEAN, DRIFT_SD = 1.2, 3.2

# --- residual house-weighting uncertainty -----------------------------------
# Mainstream-only gap -3.3 vs all-houses-equal gap -1.0 -> ~1.3 sd.
HOUSE_SD = 1.3

P_OTHER = 0.008        # a third party (realistically B'Yachad) tops the poll
P_ANNUL = 0.015        # election cancelled/postponed past 2027-01-01


def main() -> None:
    drift = RNG.normal(DRIFT_MEAN, DRIFT_SD, N)
    house = RNG.normal(0.0, HOUSE_SD, N)
    gap = np.rint(gap_0 + drift + house)           # seats are integers

    p_likud_raw = float((gap >= 1).mean())
    p_yashar_raw = float((gap <= -1).mean())
    p_tie_raw = float((gap == 0).mean())

    # Scale the two-party branch down to leave room for "Other".
    scale = 1.0 - P_OTHER
    p_likud, p_yashar, p_tie = (p * scale for p in
                                (p_likud_raw, p_yashar_raw, p_tie_raw))

    sd_total = float(np.std(gap_0 + drift + house))
    print(f"gap_0 (house-weighted)     : {gap_0:+.2f} seats")
    print(f"E[gap on election day]     : {gap_0 + DRIFT_MEAN:+.2f} seats")
    print(f"sd[gap]                    : {sd_total:.2f} seats")
    print()
    print(f"P(Likud strictly largest)  : {p_likud:6.2%}")
    print(f"P(Yashar strictly largest) : {p_yashar:6.2%}")
    print(f"P(exact tie, seats)        : {p_tie:6.2%}   <- unaddressed by the fine print")
    print(f"P(Other largest)           : {P_OTHER:6.2%}")
    print()
    # Reported vector: conditional on the question resolving at all, i.e. on no
    # tie and no annulment.  A tie or an annulment removes the question from the
    # ledger rather than favouring an option.
    denom = p_likud + p_yashar + P_OTHER
    print("Conditional on resolution (tie / postponement -> annulled):")
    print(f"  Likud  {p_likud / denom:6.2%}")
    print(f"  Yashar {p_yashar / denom:6.2%}")
    print(f"  Other  {P_OTHER / denom:6.2%}")
    print()
    print(f"P(question annulled) ~ {p_tie + P_ANNUL - p_tie * P_ANNUL:6.2%} "
          "(exact tie or no result before 2027-01-01)")

    print("\n--- sensitivity on the drift mean ---")
    for dm in (0.0, 0.6, 1.2, 1.8, 2.4):
        g = np.rint(gap_0 + RNG.normal(dm, DRIFT_SD, N) + RNG.normal(0, HOUSE_SD, N))
        pl, py = (g >= 1).mean() * scale, (g <= -1).mean() * scale
        d = pl + py + P_OTHER
        print(f"  drift={dm:+.1f}  ->  Likud {pl / d:5.1%}   Yashar {py / d:5.1%}")

    print("\n--- sensitivity on the Filber-house weight ---")
    for w in (0.0, 0.05, 0.10, 0.15, 0.25):
        g0 = ((1 - w) * MAINSTREAM_LIKUD + w * FILBER_LIKUD) - \
             ((1 - w) * MAINSTREAM_YASHAR + w * FILBER_YASHAR)
        g = np.rint(g0 + RNG.normal(DRIFT_MEAN, DRIFT_SD, N) + RNG.normal(0, HOUSE_SD, N))
        pl, py = (g >= 1).mean() * scale, (g <= -1).mean() * scale
        d = pl + py + P_OTHER
        print(f"  w_filber={w:.2f} (gap_0 {g0:+.2f})  ->  Likud {pl / d:5.1%}   Yashar {py / d:5.1%}")


if __name__ == "__main__":
    main()
