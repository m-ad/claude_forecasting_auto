"""Chart for forecast v2 of the GiveWell funds-raised question.

Two horizontal panels:

* top - funds raised split into the Coefficient Giving block, the non-AI donor base and
  the AI-wealth increment (2021-2025 actual; 2026-2028 v2 model medians, so the blocks
  do not sum exactly to the median total, which the whisker's label reports).
* bottom - where v2 sits against v1 and the three Metaculus cohorts on both legs, as
  median + interquartile range on the resolution scale. Metaculus reports quartiles
  clipped to its 0-200% range, so a cohort bar that starts at 0% or ends at 200% has
  its true quartile beyond that edge.

``chart.py`` (v1) is left untouched; this writes a separate PNG.
"""

from __future__ import annotations

import json
import runpy
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

HERE = Path(__file__).resolve().parent
OUT = HERE.parent / "charts"
OUT.mkdir(exist_ok=True)

# Categorical slots 1-3 of the reference palette, fixed order.
C_CG, C_BASE, C_AI = "#2a78d6", "#eb6834", "#1baf7a"
INK, MUTED = "#0b0b0b", "#52514e"

ns = runpy.run_path(str(HERE / "model_v2.py"), run_name="model_v2")
med = {k: float(np.median(ns[k])) for k in ("cg26", "cg27", "cg28", "base26", "base27",
                                            "base28", "ai26", "ai27", "ai28")}
tot = {y: np.percentile(ns[f"f{y}"], [25, 50, 75]) for y in ("26", "27", "28")}

YEARS = ["2021", "2022", "2023", "2024", "2025", "2026 (model)", "2027 (model)",
         "2028 (model)"]
CG = [300.0, 350.0, 100.0, 100.0, 100.0, med["cg26"], med["cg27"], med["cg28"]]
BASE = [295.5, 252.9, 255.1, 314.9, 516.3, med["base26"], med["base27"], med["base28"]]
AI = [0, 0, 0, 0, 0, med["ai26"], med["ai27"], med["ai28"]]
BANDS = [None] * 5 + [tot["26"], tot["27"], tot["28"]]

fig, (ax1, ax2) = plt.subplots(
    2, 1, figsize=(10.5, 10), gridspec_kw={"height_ratios": [2.1, 1.6]}
)

y = np.arange(len(YEARS))[::-1]
ax1.barh(y, CG, color=C_CG, label="Coefficient Giving commitment", edgecolor="white",
         linewidth=1)
ax1.barh(y, BASE, left=CG, color=C_BASE, label="Other donors, non-AI base",
         edgecolor="white", linewidth=1)
left_ai = [c + b for c, b in zip(CG, BASE)]
ax1.barh(y, AI, left=left_ai, color=C_AI,
         label="AI-wealth increment (IPO / lockup driven)", edgecolor="white", linewidth=1)
for yi, band, c, b, a in zip(y, BANDS, CG, BASE, AI):
    if band is not None:
        ax1.plot([band[0], band[2]], [yi, yi], color=INK, lw=1.4, zorder=5)
        for x in (band[0], band[2]):
            ax1.plot([x, x], [yi - 0.15, yi + 0.15], color=INK, lw=1.4, zorder=5)
        ax1.text(band[2] + 60, yi, f"median total {band[1]:,.0f}", va="center",
                 fontsize=8.5, color=MUTED)
    else:
        ax1.text(c + b + 60, yi, f"{c + b:,.0f}", va="center", fontsize=8.5, color=MUTED)
ax1.set_yticks(y, YEARS)
ax1.set_xlim(0, 5300)
ax1.set_xlabel("Funds raised, USD millions (GiveWell metrics year, February-January)")
ax1.set_title("GiveWell funds raised: actuals 2021-2025, v2 model 2026-2028\n"
              "(blocks = medians of each component; whisker = IQR of the total)",
              fontsize=11, color=INK)
ax1.legend(loc="upper right", fontsize=9, framealpha=0.95)
ax1.grid(axis="x", alpha=0.25)
ax1.set_axisbelow(True)

# --- forecast comparison -----------------------------------------------------------
snap = json.loads((HERE.parent / "raw" / "metaculus-2026-09-27.json").read_text("utf-8"))


def _cohort(qid: str, method: str) -> tuple[float, float, float]:
    lat = snap["subquestions"][qid]["methods"][method]["latest"]
    return lat["lower"], lat["center"], lat["upper"]


rows = [
    # label, 2027 (p25, p50, p75), 2028 (p25, p50, p75), colour
    ("v1 (2026-09-04)", (-26.0, 0.0, 35.0), (-11.0, 36.5, 110.0), "#b5b3ad"),
    ("v2 (2026-09-27)", (-17.2, 14.2, 67.1), (17.1, 67.3, 152.7), C_CG),
    ("Metaculus Pros (n=2)", _cohort("45575", "metaculus_pros"),
     _cohort("45576", "metaculus_pros"), C_BASE),
    ("Metaculus gold (n=4)", _cohort("45575", "gold_medalists"),
     _cohort("45576", "gold_medalists"), C_BASE),
    ("Metaculus CP (n=5)", _cohort("45575", "recency_weighted"),
     _cohort("45576", "recency_weighted"), C_BASE),
]
labels = []
ypos = []
k = 0
for leg_i, leg in enumerate(("2027", "2028")):
    for r in rows:
        lo, mid, hi = r[1 + leg_i]
        yi = -k
        ax2.barh(yi, hi - lo, left=lo, height=0.55, color=r[3], alpha=0.85, zorder=3)
        ax2.plot([mid, mid], [yi - 0.36, yi + 0.36], color=INK, lw=2.2, zorder=4)
        ax2.text(max(hi, mid) + 4, yi, f"{mid:+.0f}%", va="center", fontsize=8.5,
                 color=MUTED)
        labels.append(f"{leg}  {r[0]}")
        ypos.append(yi)
        k += 1
    k += 0.6
ax2.axvline(0, color=MUTED, lw=1, ls="--", zorder=1)
ax2.set_yticks(ypos, labels, fontsize=9)
ax2.set_xlim(-40, 240)
ax2.set_xlabel("Percentage change in funds raised vs metrics year 2026 (resolution scale)")
ax2.set_title("Median (tick) and interquartile range, v1 vs v2 vs Metaculus cohorts\n"
              "(Metaculus quartiles are clipped to its 0-200% range)",
              fontsize=11, color=INK)
ax2.grid(axis="x", alpha=0.25)
ax2.set_axisbelow(True)

fig.tight_layout()
fig.savefig(OUT / "funds-raised-v2.png", dpi=150)
print("wrote", OUT / "funds-raised-v2.png")
