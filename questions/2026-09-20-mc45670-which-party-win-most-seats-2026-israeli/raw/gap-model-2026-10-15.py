"""v4 gap model for Metaculus #45670 (largest party, 2026 Israeli election).

Same closed-form structure as v3 (`gap-model-2026-10-09.py`):
G = Likud seats - Yashar seats, treated as continuous then rounded:
G ~ N(gap0 + drift, sqrt(drift_sd^2 + house_sd^2)).
P(Yashar) = P(G <= -0.5) + P(|G| < 0.5) * P(Yashar | tie).

Inputs (2026-10-15):
- gap0: latest poll per mainstream publisher, 8 publishers (Walla/Lazar is back with a
  13 Oct poll; v3 had 7 because Walla had not polled since September):
    Channel 13 (14 Oct) 18-20 = -2      Midgam/Ch12 (12 Oct) 20-23 = -3
    Kantar/Kan (11 Oct) 20-22 = -2      Lazar/Walla (13 Oct) 20-22 = -2
    Lazar/Maariv (7-8 Oct) 20-21 = -1   Tatika/Zman Yisrael (7-8 Oct) 20-24 = -4
    Kantar/Israel Hayom (7-8 Oct) 21-22 = -1   Maagar Mochot/Ch16 (29 Sep) 19-21 = -2
  mean -17/8 = -2.125 (v3: -1.29). Weighted 0.9, plus the Filber/Direct-Polls houses
  (Channel 14 12 Oct 29-20 = +9; i24/Direct Polls 13 Oct 27-21 = +6; mean +7.5) at 0.1.
  Treating Lazar as one house (Walla only) instead gives -2.29; difference < 0.15 seat.
- drift: +0.6 kept from v3. The early-October move toward Likud (+2.1) partly reversed
  (-0.8), so the mainstream gap is now ~+1.1 seats above v1's 20 Sep level (-3.2), i.e.
  roughly v1's whole expected 5-week drift (+1.2) is already in. What remains is the
  final-polls-to-result error, +0.4 ex-2015 and ~+2 with 2015, shrunk -> +0.6.
- drift_sd 2.5 -> 2.3 for a 12-day horizon (v3: 18 days).
- house_sd 1.3 (v1).
- P(Yashar | tie) 0.50 -> 0.55: the tie rule is "party of the PM of the first government
  formed", else the tied party with a minister, else most votes. Polymarket's deep
  next-PM market (USD 46M) has Netanyahu 27.5% (was 35.5% on 10-09); conditioning on a tie
  (which sits near the centre of G now) lifts that to ~0.33, and no-government/unity
  branches (~0.2) fall back to votes (~50/50). 0.47 + 0.2*0.5 = 0.57, shaded to 0.55.
- p_other 0.006 (Polymarket Together 0.45%).
- Unmodelled, entered as explicit mean shifts on G in the variants below (speculative):
  Iran strike before the vote (Polymarket ceasefire-holds ~87% through 27 Oct, so ~0.12)
  times a ~+1.7-seat rally for Likud (Channel 12 had Likud +4 during the June 2025 war; shaded for war fatigue and
  the Axios framing of a pre-election strike) -> +0.2; unpolled Urich/Qatar report
  (Channel 12, 14 Oct) -> -0.2. They cancel, so the central run keeps drift +0.6.
"""
from math import erf, sqrt


def phi(x: float) -> float:
    """Standard normal CDF."""
    return 0.5 * (1 + erf(x / sqrt(2)))


def run(gap0: float, drift: float, drift_sd: float, house_sd: float = 1.3,
        p_yashar_tie: float = 0.55, p_other: float = 0.006) -> dict[str, float]:
    """Return the option vector for given inputs.

    Parameters
    ----------
    gap0 : float
        House-weighted Likud-minus-Yashar seat gap today.
    drift : float
        Expected remaining movement of the gap toward Likud (seats).
    drift_sd : float
        Standard deviation of that movement (seats).
    house_sd : float
        Extra standard deviation for house-weighting error (seats).
    p_yashar_tie : float
        Probability an exact seat tie resolves Yashar under the Metaculus tie rule.
    p_other : float
        Probability a third list is largest.

    Returns
    -------
    dict[str, float]
        Yashar, Likud, Other probabilities plus the raw outright/tie branch masses.
    """
    mu = gap0 + drift
    sd = sqrt(drift_sd**2 + house_sd**2)
    p_y = phi((-0.5 - mu) / sd)
    p_tie = phi((0.5 - mu) / sd) - p_y
    p_l = 1 - p_y - p_tie
    y = p_y + p_tie * p_yashar_tie
    l = p_l + p_tie * (1 - p_yashar_tie)
    return {"Yashar": round(y * (1 - p_other), 4), "Likud": round(l * (1 - p_other), 4),
            "Other": p_other, "P(Y out)": round(p_y, 4), "P(tie)": round(p_tie, 4),
            "P(L out)": round(p_l, 4), "E[G]": round(mu, 2), "sd[G]": round(sd, 2)}


MAIN = [-2, -3, -2, -2, -1, -4, -1, -2]   # latest per mainstream publisher
FILBER = [9, 6]                           # Channel 14, i24/Direct Polls


def gap0_for(w_filber: float, main: list[int] = MAIN) -> float:
    """House-weighted gap with weight w_filber on the Filber/Direct-Polls pair."""
    return (1 - w_filber) * sum(main) / len(main) + w_filber * sum(FILBER) / len(FILBER)


if __name__ == "__main__":
    g = gap0_for(0.10)
    print("gap0", round(g, 2))
    print("v3 inputs re-run on v3 gap0 (-0.46) [check]", run(0.9 * (-9 / 7) + 0.1 * 7.0, 0.6, 2.5,
                                                         p_yashar_tie=0.50))
    print("step 1: new polls only (v3 drift/sd/tie)", run(g, 0.6, 2.5, p_yashar_tie=0.50))
    print("step 2: + horizon sd 2.3", run(g, 0.6, 2.3, p_yashar_tie=0.50))
    print("step 3: + tie split 0.55", run(g, 0.6, 2.3))
    print("step 4: + Iran tail +0.2", run(g, 0.8, 2.3))
    print("v4 central: + Urich -0.2 (net drift +0.6)", run(g, 0.6, 2.3))
    print("--- sensitivity (on v4 central) ---")
    print("no remaining drift (0.0)", run(g, 0.0, 2.3))
    print("full v1 drift again (+1.2)", run(g, 1.2, 2.3))
    print("Filber weight 0", run(gap0_for(0.0), 0.6, 2.3))
    print("Filber weight 0.25", run(gap0_for(0.25), 0.6, 2.3))
    print("Lazar as one house (Walla only)", run(gap0_for(0.10, [-2, -3, -2, -2, -4, -1, -2]), 0.6, 2.3))
    print("tie split 0.45", run(g, 0.6, 2.3, p_yashar_tie=0.45))
    print("drift sd 3.2 (v1)", run(g, 0.6, 3.2))
    print("Polymarket-equivalent (tie on votes, 0.50)", run(g, 0.6, 2.3, p_yashar_tie=0.50))
