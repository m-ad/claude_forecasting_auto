"""Monte-Carlo model for Metaculus #40966 (Netanyahu ceases to be PM during 2026), v3 (2026-10-09 re-run with updated inputs; see forecast.md v3 revision table).

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

RNG = np.random.default_rng(20261009)
N_DRAWS = 1_000_000

# --- 1. Election outcome -----------------------------------------------------------
# Mid-September mainstream poll average (MEF poll-of-polls 2026-09-17; JPost five-poll
# average 2026-09-17; Channel 13 2026-09-16): Netanyahu bloc ~54, anti-Netanyahu Zionist
# bloc ~53, Arab parties ~13.
O_MEAN = 52.0   # v3: mainstream opp-Zionist avg fell 56.1 -> 55.1 (Wikipedia, latest per house 2026-10-09); keep v2 all-house offset
A_MEAN = 13.6   # v3: mainstream Arab avg 12.4 -> 13.0; disqualification overturned 2026-10-02
# Documented Israeli right-skew in polling (2015/2020/2022 under-read the right by ~5.7
# seats; 2021 ran the other way). v1's 60% no-bias / 40% +4-seat-right mixture => -1.6.
RIGHT_SKEW = -1.6
# Bloc-level poll error 40 days out. Israeli bloc RMSE historically ~5-8 seats.
O_SD = 5.0      # v3: 18 days out rather than 40
A_SD = 1.5

# --- 2. Arab recommendation behaviour ---------------------------------------------
# Ra'am has sat in a Zionist coalition before (2021) and Eisenkot told his slate on
# 2026-09-15 to accept a minority government resting on Arab abstention (Channel 12).
P_RAAM_RECOMMENDS = 0.55  # v3: Eisenkot 2026-09-24 "I do not see an Arab party that accepts my principles"
# Hadash-Ta'al-Balad: Balad is explicitly anti-Zionist and the Joint List voted against
# the Bennett government in 2021; but the Joint List did recommend Gantz in Sept 2019.
P_JOINT_RECOMMENDS = 0.30  # v3: Balad leader forced out 2026-10-02; Eisenkot rules JL out as partner
RAAM_SEATS_SHARE = 5.0 / 13.0

# --- 3./4. Formation success ------------------------------------------------------
P_FORM_MAJORITY = 0.82  # v3: 2026-09-26 five-leader pact to form a government immediately   # mandate-holder's own bloc >= 61
P_FORM_MINORITY = 0.42  # v3: Eisenkot publicly rejects Arab partners; abstention deal harder to sell   # needs Arab abstention + internal discipline (defection risk)
P_YES_IF_BIBI_MANDATE = 0.04  # second mandate runs into mid-January 2027

P_ELECTION_ON_SCHEDULE = 0.93  # v3: Polymarket on-schedule 96.5% -> 91.9% (Iran-strike/postponement talk); shaded up, 80-MK bar
P_NON_ELECTORAL = 0.009  # v3: 2.7 months left  # death / >=14-day incapacity / pardon-for-retirement, 3.5 months


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
