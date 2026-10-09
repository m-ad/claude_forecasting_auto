"""v3 gap model for Metaculus #45670 (largest party, 2026 Israeli election).

G = Likud seats - Yashar seats, treated as continuous then rounded:
G ~ N(gap0 + drift, sqrt(drift_sd^2 + house_sd^2)).
P(Yashar) = P(G <= -0.5) + P(|G| < 0.5) * P(Yashar | tie).

Inputs (2026-10-09):
- gap0: latest poll per house, 7 mainstream houses avg -1.29 (Kantar/IH -1, Ch13 0,
  Midgam -2, Kantar/Kan -2, Zman Yisrael 0, Maariv -2, Maagar Mochot -2), weighted 0.9,
  plus the Filber/Direct-Polls houses (Ch14 +8, i24 +6, mean +7) weighted 0.1 (v1 weight).
- drift: v1's +1.2 seats over 5 weeks; ~+2.1 has already shown up in two weeks, so only
  half (+0.6) is kept for the remaining 18 days. drift_sd 3.2 -> 2.5 for the shorter horizon.
- house_sd 1.3 (v1).
- P(Yashar | tie) = 0.50, matched to P(Eisenkot takes the first mandate) ~0.49 in the
  sister question's model (40966 v3), since the tie-break is "party of the next PM".
"""
from math import erf, sqrt


def phi(x: float) -> float:
    """Standard normal CDF."""
    return 0.5 * (1 + erf(x / sqrt(2)))


def run(gap0: float, drift: float, drift_sd: float, house_sd: float = 1.3,
        p_yashar_tie: float = 0.50, p_other: float = 0.006) -> dict[str, float]:
    """Return the option vector for given inputs."""
    mu = gap0 + drift
    sd = sqrt(drift_sd**2 + house_sd**2)
    p_y = phi((-0.5 - mu) / sd)
    p_tie = phi((0.5 - mu) / sd) - p_y
    p_l = 1 - p_y - p_tie
    y = p_y + p_tie * p_yashar_tie
    l = p_l + p_tie * (1 - p_yashar_tie)
    return {"Yashar": y * (1 - p_other), "Likud": l * (1 - p_other), "Other": p_other,
            "P(tie)": p_tie}


if __name__ == "__main__":
    gap0 = 0.9 * (-9 / 7) + 0.1 * 7.0
    print("gap0", round(gap0, 2))
    print("v3 central", run(gap0, 0.6, 2.5))
    print("old drift/sd, tie 0.55", run(gap0, 1.2, 3.2, p_yashar_tie=0.55))
    print("no remaining drift", run(gap0, 0.0, 2.5))
    print("full drift +1.2", run(gap0, 1.2, 2.5))
    print("Filber weight 0", run(-9 / 7, 0.6, 2.5))
    print("Filber weight 0.25", run(0.75 * (-9 / 7) + 0.25 * 7.0, 0.6, 2.5))
