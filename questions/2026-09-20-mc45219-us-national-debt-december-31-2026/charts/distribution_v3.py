"""v3 (2026-10-15) scenario mixture for MC45219 (US national debt on 2026-12-31), plotted
against the v2 (2026-10-09) mixture.

Each scenario is a normal in $T; the mixture is sampled. The debt-ceiling cap
(~$41.28T on TPDO) is far in the right tail now and is kept only for completeness.
Run: uv run <this file>
"""

from __future__ import annotations

import matplotlib
import numpy as np

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402  (backend must be set first)

N = 600_000
# Statutory limit + the ~$198bn of TPDO not subject to limit (DTS 2026-10-13), less a
# ~$20bn settlement buffer. Irrelevant to the central mass in v3; kept for completeness.
CAP = 41.104 + 0.198 - 0.020

# (name, weight, centre $T, sigma $T)
V2: list[tuple[str, float, float, float]] = [
    ("Treasury plan, adjusted", 0.52, 40.92, 0.065),
    ("Softer deficit / low TGA", 0.27, 40.85, 0.070),
    ("Deferred Oct-1 intragov credit lands", 0.15, 41.01, 0.070),
    ("Heavier borrowing", 0.04, 41.08, 0.060),
    ("CR lapse + deep TGA drawdown", 0.02, 40.78, 0.070),
]
# v3 centres are built bottom-up from the 2026-10-13 Debt to the Penny print
# (public $32,483.6bn, intragov $7,860.2bn): see forecast.md v3 "Inside view".
V3: list[tuple[str, float, float, float]] = [
    ("Treasury plan, adjusted", 0.45, 40.922, 0.055),
    ("Bottom-up deficit path (~$720bn Q1)", 0.27, 40.889, 0.055),
    ("Softer deficit and/or TGA <= $820bn", 0.10, 40.820, 0.060),
    ("Heavier: refunding revised up / TGA ~$900-950bn", 0.13, 41.000, 0.060),
    ("Unexplained one-off intragov credit", 0.03, 41.020, 0.060),
    ("CR lapse + deep TGA drawdown", 0.02, 40.780, 0.060),
]
PCTS = [1, 5, 10, 25, 50, 75, 90, 95, 99]


def mixture(scen: list[tuple[str, float, float, float]], seed: int) -> np.ndarray:
    """Sample the scenario mixture.

    Parameters
    ----------
    scen : list of (name, weight, centre, sigma)
        Scenario table; weights must sum to 1.
    seed : int
        RNG seed, fixed so the printed quantiles are reproducible.

    Returns
    -------
    np.ndarray
        N draws of TPDO on 2026-12-31 in $T, capped at the debt-ceiling level.
    """
    rng = np.random.default_rng(seed)
    w = np.array([s[1] for s in scen])
    assert abs(w.sum() - 1.0) < 1e-9
    pick = rng.choice(len(scen), size=N, p=w)
    mu = np.array([s[2] for s in scen])[pick]
    sd = np.array([s[3] for s in scen])[pick]
    return np.minimum(rng.normal(mu, sd), CAP)


d2 = mixture(V2, 20261009)
d3 = mixture(V3, 20261015)
q2 = dict(zip(PCTS, np.percentile(d2, PCTS)))
q3 = dict(zip(PCTS, np.percentile(d3, PCTS)))
for p in PCTS:
    print(f"p{p:02d}: v2 {q2[p]:.4f}T   v3 {q3[p]:.4f}T")
print(f"P(> 41.0T): v2 {(d2 > 41.0).mean():.1%}   v3 {(d3 > 41.0).mean():.1%}")

# ---------------------------------------------------------------- figure
BLUE, ORANGE, INK, MUTED = "#2a78d6", "#eb6834", "#0b0b0b", "#52514e"
plt.rcParams["axes.formatter.use_mathtext"] = False
fig, ax = plt.subplots(figsize=(11, 5.6))
fig.patch.set_facecolor("#fcfcfb")
ax.set_facecolor("#fcfcfb")

ypos = np.arange(len(V3))[::-1]
for y, (_, weight, centre, sigma) in zip(ypos, V3):
    lo, hi = centre - 0.674 * sigma, centre + 0.674 * sigma
    ax.barh([y], [hi - lo], left=lo, height=0.16 + 0.55 * weight, color=BLUE, alpha=0.85)
    ax.plot([centre], [y], "o", color=INK, ms=5)

# Mixture IQR + median, v2 (orange, hatched outline) vs v3 (blue fill).
plt.rcParams["hatch.linewidth"] = 0.6
ax.axvspan(q2[25], q2[75], facecolor="none", edgecolor=(0.92, 0.41, 0.20, 0.45), hatch="///",
           lw=0, zorder=0)
ax.axvline(q2[50], color=ORANGE, lw=2, ls="--", zorder=1)
ax.axvspan(q3[25], q3[75], color=BLUE, alpha=0.12, zorder=0)
ax.axvline(q3[50], color=BLUE, lw=2, zorder=1)
top = len(V3) - 0.35
ax.text(q2[50] + 0.004, top, f"v2 median {q2[50]:.3f}", color=MUTED, fontsize=8.5,
        va="bottom", ha="left")
ax.text(q3[50] - 0.004, top, f"v3 median {q3[50]:.3f}", color=INK, fontsize=8.5,
        va="bottom", ha="right")

ax.set_yticks(ypos)
ax.set_yticklabels([f"{n}  ({w:.0%})" for n, w, _, _ in V3], fontsize=9, color=INK)
ax.set_xlim(40.70, 41.10)
ax.set_ylim(-0.75, len(V3) - 0.05)
ax.set_xlabel("Total Public Debt Outstanding on 2026-12-31, USD trillion", color=MUTED)
ax.set_title(
    f"US debt on 2026-12-31: v3 mixture IQR [{q3[25]:.3f}, {q3[75]:.3f}] (blue fill) vs "
    f"v2 [{q2[25]:.3f}, {q2[75]:.3f}] (orange hatch)\n"
    "bars = each v3 scenario's IQR, bar height ~ weight",
    fontsize=10,
    color=INK,
    loc="left",
)
ax.grid(axis="x", color="#e4e3df", lw=0.8)
ax.set_axisbelow(True)
ax.spines[["top", "right"]].set_visible(False)
fig.subplots_adjust(left=0.36, right=0.975, top=0.87, bottom=0.11)
out = __file__.replace(".py", ".png")
fig.savefig(out, dpi=150, facecolor=fig.get_facecolor())
print("wrote", out)
