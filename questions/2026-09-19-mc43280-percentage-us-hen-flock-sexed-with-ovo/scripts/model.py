"""Scenario mixture for the EU and US in-ovo sexing questions (MC 43279 / 43280).

The two questions share a resolver (Innovate Animal Ag) and therefore share the
same dominant uncertainty: *which* 2027 publication is used and what as-of date
it carries. Each scenario is a normal on the resolving value; the weights are
the probability of that publication path. Sampling rather than analytic
quantiles because the EU mixture is genuinely bimodal — a restatement of the
June-2026 figure sits ~4 pp below any fresh 2027 measurement.

The EU branch also carries a denominator-rebasing shock: IAA restated its
April-2025 figure from 28% to 34% between the 2025 and 2026 reports purely by
narrowing the flock estimate, so the printed number has measurement risk on top
of adoption risk. A restated 2026 figure cannot be re-based, hence the mask.

Run: uv run questions/<eu-slug>/scripts/model.py
"""

from __future__ import annotations

import numpy as np

N = 2_000_000
P_REBASE = 0.15      # chance the 2027 EU print carries another denominator revision
REBASE_SD = 3.0      # pp, either direction

# weight, centre, sd
EU: list[tuple[float, float, float]] = [
    (0.25, 40.4, 1.0),   # Jan-2027 Yearly Recap used: restates 40%, or a light end-2026 update
    (0.25, 43.5, 2.2),   # 2027 annual report, as-of 1 Apr 2027
    (0.35, 44.6, 2.4),   # 2027 annual report, as-of 1 Jun 2027 (2026's timing repeated)
    (0.15, 46.0, 2.9),   # report slips to H2 2027
]
EU_REBASE_EXPOSED = [False, True, True, True]

US: list[tuple[float, float, float]] = [
    (0.20, 1.6, 0.5),    # strict Q1-2027 as-of date
    (0.45, 2.3, 0.8),    # as-of ~Apr-Jun 2027
    (0.25, 3.0, 1.1),    # as-of mid/late 2027, Vital Farms ramp further along
    (0.10, 5.0, 2.0),    # fast commodity adoption, or a chicks-hatched (flow) basis
]

# Sensitivity variants, keyed by the row they produce in forecast.md.
EU_VARIANTS: dict[str, list[tuple[float, float, float]]] = {
    "recap weight -> 0.05": [(0.05, 40.4, 1.0), (0.30, 43.5, 2.2), (0.45, 44.6, 2.4), (0.20, 46.0, 2.9)],
    "recap weight -> 0.50": [(0.50, 40.4, 1.0), (0.17, 43.5, 2.2), (0.23, 44.6, 2.4), (0.10, 46.0, 2.9)],
    "pace 2.5pp/yr": [(0.25, 40.2, 1.0), (0.25, 42.1, 2.2), (0.35, 42.5, 2.4), (0.15, 43.3, 2.9)],
    "pace 9pp/yr": [(0.25, 40.8, 1.0), (0.25, 47.5, 2.2), (0.35, 49.0, 2.4), (0.15, 51.0, 2.9)],
}


def sample(
    scenarios: list[tuple[float, float, float]],
    rng: np.random.Generator,
    rebase_exposed: list[bool] | None = None,
    lo: float | None = None,
) -> np.ndarray:
    """Draw ``N`` values from a weighted mixture of normals.

    Parameters
    ----------
    scenarios
        ``(weight, centre, sd)`` triples; weights are normalised.
    rng
        Seeded generator, so the numbers quoted in ``forecast.md`` reproduce.
    rebase_exposed
        Per-scenario flag for whether a denominator revision can hit it.
    lo
        Lower clip, for the US question's closed 0% bound.

    Returns
    -------
    numpy.ndarray
        Draws of the resolving percentage.
    """
    w = np.array([s[0] for s in scenarios], dtype=float)
    w /= w.sum()
    idx = rng.choice(len(scenarios), size=N, p=w)
    x = rng.normal(np.array([s[1] for s in scenarios])[idx], np.array([s[2] for s in scenarios])[idx])
    if rebase_exposed is not None:
        hit = (rng.random(N) < P_REBASE) & np.array(rebase_exposed, dtype=bool)[idx]
        x = x + hit * rng.normal(0.0, REBASE_SD, N)
    if lo is not None:
        x = np.clip(x, lo, None)
    return x


def quantiles(x: np.ndarray) -> dict[str, float]:
    """Return the percentiles quoted in the forecast files."""
    p5, p25, p50, p75, p95 = np.percentile(x, [5, 25, 50, 75, 95])
    return {"p5": p5, "p25": p25, "median": p50, "p75": p75, "p95": p95}


def main() -> None:
    rng = np.random.default_rng(20260919)
    eu = quantiles(sample(EU, rng, rebase_exposed=EU_REBASE_EXPOSED))
    us = quantiles(sample(US, rng, lo=0.0))
    print("EU 43279  " + "  ".join(f"{k}={v:.2f}" for k, v in eu.items()))
    print("US 43280  " + "  ".join(f"{k}={v:.2f}" for k, v in us.items()))
    print("\nEU sensitivity (median and IQR):")
    for label, scen in EU_VARIANTS.items():
        q = quantiles(sample(scen, rng, rebase_exposed=EU_REBASE_EXPOSED))
        print(f"  {label:<22} median={q['median']:.1f}  IQR[{q['p25']:.1f}, {q['p75']:.1f}]")


if __name__ == "__main__":
    main()
