"""Monte-Carlo model for Metaculus #40966 (Netanyahu ceases to be PM during 2026), v2.

The v1 model weighted four hand-drawn bloc scenarios. v2 re-derives them from the
mid-September poll picture, because the binding quantity turned out to be *who gets the
first government-formation mandate* — which is decided by recommendation counts, and
therefore by whether the Arab parties recommend Eisenkot, not by bloc size alone.

Structure
---------
1. Draw election seat outcomes for the three blocs from the mid-September polling average
   with a right-skew adjustment and Israeli bloc-level poll error.
2. Draw Arab-party recommendation behaviour (Ra'am and the Joint List separately).
3. Assign the first mandate to whoever has more recommendations.
4. Apply first-mandate success probabilities conditional on whether the mandate-holder
   commands >= 61 outright, and on the 28+14-day statutory deadline landing ~21-26 Dec.
"""

from __future__ import annotations

import numpy as np

RNG = np.random.default_rng(20260918)
N_DRAWS = 1_000_000

# --- 1. Election outcome -----------------------------------------------------------
# Mid-September mainstream poll average (MEF poll-of-polls 2026-09-17; JPost five-poll
# average 2026-09-17; Channel 13 2026-09-16): Netanyahu bloc ~54, anti-Netanyahu Zionist
# bloc ~53, Arab parties ~13.
O_MEAN = 53.0
A_MEAN = 13.0
# Documented Israeli right-skew in polling (2015/2020/2022 under-read the right by ~5.7
# seats; 2021 ran the other way). v1's 60% no-bias / 40% +4-seat-right mixture => -1.6.
RIGHT_SKEW = -1.6
# Bloc-level poll error 40 days out. Israeli bloc RMSE historically ~5-8 seats.
O_SD = 6.0
A_SD = 1.5

# --- 2. Arab recommendation behaviour ---------------------------------------------
# Ra'am has sat in a Zionist coalition before (2021) and Eisenkot told his slate on
# 2026-09-15 to accept a minority government resting on Arab abstention (Channel 12).
P_RAAM_RECOMMENDS = 0.60
# Hadash-Ta'al-Balad: Balad is explicitly anti-Zionist and the Joint List voted against
# the Bennett government in 2021; but the Joint List did recommend Gantz in Sept 2019.
P_JOINT_RECOMMENDS = 0.35
RAAM_SEATS_SHARE = 5.0 / 13.0

# --- 3./4. Formation success ------------------------------------------------------
P_FORM_MAJORITY = 0.80   # mandate-holder's own bloc >= 61
P_FORM_MINORITY = 0.45   # needs Arab abstention + internal discipline (defection risk)
P_YES_IF_BIBI_MANDATE = 0.04  # second mandate runs into mid-January 2027

P_ELECTION_ON_SCHEDULE = 0.96
P_NON_ELECTORAL = 0.011  # death / >=14-day incapacity / pardon-for-retirement, 3.5 months


def run(n: int = N_DRAWS) -> dict[str, float]:
    """Run the simulation and return the headline quantities."""
    o = RNG.normal(O_MEAN + RIGHT_SKEW, O_SD, n)
    a = np.clip(RNG.normal(A_MEAN, A_SD, n), 0, 20)
    nb = 120.0 - o - a

    raam = RNG.random(n) < P_RAAM_RECOMMENDS
    joint = RNG.random(n) < P_JOINT_RECOMMENDS
    arab_rec = a * (raam * RAAM_SEATS_SHARE + joint * (1 - RAAM_SEATS_SHARE))

    eisenkot_rec = o + arab_rec
    eisenkot_mandate = eisenkot_rec > nb

    o61 = o >= 61
    p_form = np.where(o61, P_FORM_MAJORITY, P_FORM_MINORITY)
    p_yes = np.where(eisenkot_mandate, p_form, P_YES_IF_BIBI_MANDATE)

    electoral = float(p_yes.mean())
    total = P_ELECTION_ON_SCHEDULE * electoral + P_NON_ELECTORAL
    return {
        "P(anti-Bibi Zionist bloc >= 61)": float(o61.mean()),
        "P(anti-Bibi bloc > Netanyahu bloc)": float((o > nb).mean()),
        "P(Eisenkot gets first mandate)": float(eisenkot_mandate.mean()),
        "P(YES | electoral path)": electoral,
        "P(YES) total": total,
    }


if __name__ == "__main__":
    for k, v in run().items():
        print(f"{k:38s} {v:.4f}")
