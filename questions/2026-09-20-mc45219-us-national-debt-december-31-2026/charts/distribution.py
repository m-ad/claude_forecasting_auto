"""Build the scenario mixture for MC45219 (US national debt on 2026-12-31) and plot it.

The mixture is a weighted sum of truncated normals, one per scenario, hard-capped at the
effective debt-ceiling level for Total Public Debt Outstanding (statutory limit plus the
~$195bn of debt not subject to limit). Run: uv run <this file>
"""

from __future__ import annotations

import matplotlib
import numpy as np

matplotlib.use("Agg")
import matplotlib.pyplot as plt

RNG = np.random.default_rng(20260920)
N = 400_000

# Effective cap on Total Public Debt Outstanding. The statutory limit ($41.103996T on
# 2026-09-17) binds *debt subject to limit*; TPDO sits ~$196bn above that (unamortized
# discount, FFB, other non-limit debt, drifting up ~$2bn/month). Treasury never runs to the
# hard edge -- it needs operating room for auction settlement -- so the practical cap used
# here is the arithmetic cap less a ~$20bn working buffer.
CAP = 41.104 + 0.196 - 0.020

# (name, weight, centre $T, sigma $T)
SCENARIOS: list[tuple[str, float, float, float]] = [
    ("Treasury plan roughly delivered", 0.46, 41.16, 0.065),
    ("Softer borrowing / Dec shutdown", 0.26, 41.02, 0.080),
    ("Heavier borrowing, ceiling-managed", 0.22, 41.23, 0.050),
    ("New year-end fiscal legislation", 0.04, 41.24, 0.040),
    ("Long shutdown + deep cash drawdown", 0.02, 40.88, 0.080),
]

w = np.array([s[1] for s in SCENARIOS])
assert abs(w.sum() - 1.0) < 1e-9

pick = RNG.choice(len(SCENARIOS), size=N, p=w)
mu = np.array([s[2] for s in SCENARIOS])[pick]
sd = np.array([s[3] for s in SCENARIOS])[pick]
draws = np.minimum(RNG.normal(mu, sd), CAP)

qs = np.percentile(draws, [5, 10, 25, 50, 75, 90, 95])
labels = ["p05", "p10", "p25", "p50", "p75", "p90", "p95"]
for lab, q in zip(labels, qs):
    print(f"{lab}: {q:.4f}T")
print(f"P(above statutory-limit cap {CAP:.3f}T) = {(draws >= CAP - 1e-9).mean():.3%}")
print(f"P(< 41.0T) = {(draws < 41.0).mean():.1%}   P(> 41.3T) = {(draws > 41.3).mean():.1%}")

# ---------------------------------------------------------------- figure
plt.rcParams["axes.formatter.use_mathtext"] = False
fig, (ax0, ax1) = plt.subplots(
    2, 1, figsize=(11, 7.4), gridspec_kw={"height_ratios": [0.75, 1]}
)

# Panel 0 -- decomposition of the 2026-09-17 -> 2026-12-31 increment.
parts = [
    ("", 40.093, "#3B5BDB"),
    ("Sep 18-30\nstub", 0.130, "#748FFC"),
    ("Oct-Dec debt\nheld by public", 0.653, "#F59F00"),
    ("Oct-Dec intra-\ngovernmental", 0.285, "#E8590C"),
]
left = 0.0
for name, val, colour in parts:
    ax0.barh([0], [val], left=left, color=colour, edgecolor="white", height=0.5)
    ax0.text(left + val / 2, 0, f"{name}\n+{val:,.3f}" if left else f"{name}\n{val:,.3f}",
             ha="center", va="center", fontsize=8, color="white", fontweight="bold")
    left += val
ax0.text(40.02, 0, "level\n2026-09-17\n40.093", ha="center", va="center", fontsize=7.5,
         color="white", fontweight="bold")
ax0.axvline(CAP, color="#C92A2A", ls="--", lw=1.6)
ax0.text(CAP, -0.28, f"ceiling cap {CAP:.2f} ", ha="right", va="center",
         color="#C92A2A", fontsize=8.5, fontweight="bold")
ax0.set_yticks([])
ax0.set_xlim(39.95, 41.50)
ax0.set_xlabel("Total Public Debt Outstanding, USD trillion")
ax0.set_title("Central path: 40.09tn on 17 Sep 2026 -> 41.16tn on 31 Dec 2026", fontsize=11)

# Panel 1 -- scenario bands (bar = that scenario's IQR, height proportional to weight).
ypos = np.arange(len(SCENARIOS))[::-1]
for y, (name, weight, centre, sigma) in zip(ypos, SCENARIOS):
    lo, hi = centre - 0.674 * sigma, min(centre + 0.674 * sigma, CAP)
    ax1.barh([y], [hi - lo], left=lo, height=0.18 + 0.5 * weight, color="#495057", alpha=0.8)
    ax1.plot([centre], [y], "o", color="#212529", ms=5)
ax1.axvspan(qs[2], qs[4], color="#4C6EF5", alpha=0.13, zorder=0)
ax1.axvline(qs[3], color="#4C6EF5", lw=2, zorder=1)
ax1.axvline(CAP, color="#C92A2A", ls="--", lw=1.6)
ax1.set_yticks(ypos)
ax1.set_yticklabels([f"{n}  ({w:.0%})" for n, w, _, _ in SCENARIOS], fontsize=9)
ax1.set_xlim(40.78, 41.34)
ax1.set_ylim(-0.75, len(SCENARIOS) - 0.25)
ax1.set_xlabel("Total Public Debt Outstanding on 2026-12-31, USD trillion")
ax1.set_title(
    f"Scenario bands -> mixture median {qs[3]:.2f}tn, IQR [{qs[2]:.2f}, {qs[4]:.2f}]",
    fontsize=11,
)
ax0.spines[["top", "right", "left"]].set_visible(False)
ax1.spines[["top", "right"]].set_visible(False)
fig.subplots_adjust(left=0.28, right=0.975, top=0.93, bottom=0.085, hspace=0.62)
out = __file__.replace(".py", ".png")
fig.savefig(out, dpi=150)
print("wrote", out)
