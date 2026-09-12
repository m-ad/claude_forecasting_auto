"""Path model for: will FURA put a non-quail cultivated meat on its menu before 2027-07-01?

The binding constraint is supply, not FURA's willingness: as of 2026-09-12 the only
cultivated meat actually on sale anywhere in Singapore is Vow's cultured Japanese quail,
which the question excludes. So each path is decomposed as
`P(supplier commercially live in Singapore in window) x P(FURA places it on its menu in time)`
and the paths are combined with the independence complement.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Path:
    """One route to YES.

    Parameters
    ----------
    name
        Short label for the supplier / route.
    p_supply
        Probability the product is commercially available to Singapore foodservice
        inside the sub-window this path describes.
    p_fura
        Probability FURA lists it on its own menu before 2027-07-01, given supply.
        Falls with the amount of runway left, since menu changes are not instant.
    """

    name: str
    p_supply: float
    p_fura: float

    @property
    def p(self) -> float:
        """Unconditional contribution of this path to P(YES)."""
        return self.p_supply * self.p_fura


# Parima (Gourmey duck/foie gras, Vital Meat chicken) is split by arrival time because
# a launch in, say, May 2027 leaves too little runway for a menu placement by 1 July.
PATHS: list[Path] = [
    Path("Parima live by 2027-03-31", 0.40, 0.60),
    Path("Parima live 2027-04-01..06-15", 0.15, 0.33),
    Path("Aleph Farms beef live before 2027-06-15", 0.28, 0.16),
    Path("Other (Eat Just return, Hoxton fat, surprise)", 1.00, 0.05),
]

# Annulment: the question is voided if FURA ceases operations before resolution.
# Closure worlds are almost all NO worlds, so removing them lifts P(YES | resolves).
P_CLOSURE = 0.05


def p_yes(paths: list[Path]) -> float:
    """Combine independent paths via the complement rule."""
    p_no = 1.0
    for path in paths:
        p_no *= 1.0 - path.p
    return 1.0 - p_no


def main() -> None:
    raw = p_yes(PATHS)
    conditional = raw / (1.0 - P_CLOSURE * (1.0 - raw))
    for path in PATHS:
        print(f"{path.name:48s} {path.p_supply:5.2f} x {path.p_fura:5.2f} = {path.p:6.3f}")
    print(f"{'P(YES), raw':48s} {raw:26.3f}")
    print(f"{'P(YES | not annulled)':48s} {conditional:26.3f}")


if __name__ == "__main__":
    main()
