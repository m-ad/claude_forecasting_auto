"""Charts for the GiveWell funds-raised question.

Two panels, both horizontal (easier to read long year labels than rotated ticks):

* top  - decomposition of funds raised into the Coefficient Giving commitment and
  everything else, 2021-2025 actual and 2026-2028 model medians. The point of the panel
  is that the 2026 bar is inflated by a single institutional decision.
* bottom - the forecast bands for the two subquestions, on the resolution scale.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT = Path(__file__).resolve().parents[1] / "charts"
OUT.mkdir(exist_ok=True)

# Actuals from GiveWell metrics reports 2021, 2022, 2024, 2025; model medians thereafter.
YEARS = ["2021", "2022", "2023", "2024", "2025", "2026 (m)", "2027 (m)", "2028 (m)"]
CG = [300.0, 350.0, 100.0, 100.0, 100.0, 983.3, 497.8, 550.0]
IND = [295.5, 252.9, 255.1, 314.9, 516.3, 763.9, 1130.4, 1639.3]
TOT_IQR = [
    None,
    None,
    None,
    None,
    None,
    (1562.8, 1871.3),
    (1234.2, 2315.2),
    (1459.9, 3673.6),
]

fig, (ax1, ax2) = plt.subplots(
    2, 1, figsize=(10, 8.6), gridspec_kw={"height_ratios": [2.4, 1]}
)

y = np.arange(len(YEARS))[::-1]
ax1.barh(
    y, CG, color="#c0392b", label="Coefficient Giving / Open Philanthropy commitment"
)
ax1.barh(
    y, IND, left=CG, color="#2980b9", label="Individual donors and all other channels"
)
for yi, band in zip(y, TOT_IQR):
    if band:
        ax1.plot(
            band, [yi, yi], color="#2c3e50", lw=1.6, solid_capstyle="butt", zorder=5
        )
        for x in band:
            ax1.plot([x, x], [yi - 0.16, yi + 0.16], color="#2c3e50", lw=1.6, zorder=5)
ax1.set_yticks(y, YEARS)
ax1.set_xlabel("Funds raised, USD millions (metrics year, February-January)")
ax1.set_title(
    "GiveWell funds raised: the 2026 base year is inflated by a one-off\n"
    "(bars 2026-2028 are model medians; whisker = modelled interquartile range of the total)",
    fontsize=11,
)
ax1.legend(loc="upper right", fontsize=9, framealpha=0.95)
ax1.grid(axis="x", alpha=0.25)
ax1.set_axisbelow(True)
for yi, c, i, band in zip(y, CG, IND, TOT_IQR):
    # place the total to the right of whatever extends furthest, bar or whisker
    x = max(c + i, band[1] if band else 0) + 60
    ax1.text(x, yi, f"{c + i:,.0f}", va="center", fontsize=9, color="#2c3e50")
ax1.set_xlim(0, 4400)

# --- forecast bands ---------------------------------------------------------------
bands = [
    ("2028 vs 2026", -39.2, -10.9, 36.5, 110.3, 212.2),
    ("2027 vs 2026", -43.7, -26.1, 0.2, 35.1, 75.2),
]
yy = np.arange(len(bands))
for yi, (lbl, p10, p25, p50, p75, p90) in zip(yy, bands):
    ax2.plot([p10, p90], [yi, yi], color="#7f8c8d", lw=2, zorder=2)
    ax2.barh(yi, p75 - p25, left=p25, height=0.34, color="#16a085", zorder=3)
    ax2.plot([p50, p50], [yi - 0.22, yi + 0.22], color="#0b3d36", lw=3, zorder=4)
    ax2.text(
        p90 + 6, yi, f"median {p50:+.1f}%", va="center", fontsize=9, color="#0b3d36"
    )
ax2.axvline(0, color="#c0392b", lw=1.2, ls="--", zorder=1)
ax2.set_yticks(yy, [b[0] for b in bands])
ax2.set_xlabel(
    "Percentage change in funds raised vs metrics year 2026 (question resolution scale)"
)
ax2.set_title("Forecast: thick bar = IQR (25-75), thin line = 10-90", fontsize=11)
ax2.grid(axis="x", alpha=0.25)
ax2.set_axisbelow(True)
ax2.set_xlim(-60, 300)

fig.tight_layout()
fig.savefig(OUT / "funds-raised-decomposition.png", dpi=150)
print("wrote", OUT / "funds-raised-decomposition.png")
