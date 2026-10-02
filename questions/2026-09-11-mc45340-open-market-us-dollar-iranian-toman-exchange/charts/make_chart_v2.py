"""Chart for v2: Bonbast path since August and the end-December bracket distribution.

Run from the repo root:
    uv run questions/2026-09-11-mc45340-open-market-us-dollar-iranian-toman-exchange/charts/make_chart_v2.py
"""

import json
from datetime import date
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

HERE = Path(__file__).resolve().parent
RAW = HERE.parent / "raw"

series = json.loads((RAW / "bonbast-graph-usd-2026-10-02.json").read_text())["series"]
days = [date.fromisoformat(d) for d in series]
vals = np.array(list(series.values())) / 1000

brackets = ["< 200k", "200–250k", "250–300k", "300–350k", "350–400k", "> 400k"]
v1 = [8.3, 26.4, 31.3, 18.1, 7.3, 8.6]
v2 = [5.7, 16.3, 38.1, 25.2, 6.5, 8.2]
# Polymarket book sums to 102.6%; normalised so the bars compare like with like.
pm_raw = [10.5, 19.5, 26.5, 29.5, 11.4, 5.15]
pm = [100 * x / sum(pm_raw) for x in pm_raw]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4.6), gridspec_kw={"width_ratios": [1.3, 1]})

ax1.plot(days, vals, color="#2c6fbb", lw=2)
ax1.axhline(250, color="#b33", ls="--", lw=1)
ax1.text(days[1], 251.5, "question's upper bound 250k (open)", color="#b33", fontsize=8)
ax1.axhline(288, color="#555", ls=":", lw=1)
ax1.text(days[1], 289.5, "v2 median for 31 Dec: 288k", color="#555", fontsize=8)
ax1.annotate("v1 (11 Sep): 237.5k", xy=(date(2026, 9, 11), 237.5), xytext=(date(2026, 8, 12), 228),
             arrowprops={"arrowstyle": "->", "color": "#333"}, fontsize=8)
ax1.annotate("1 Oct: 258.7k", xy=(date(2026, 10, 1), 258.7), xytext=(date(2026, 9, 8), 268),
             arrowprops={"arrowstyle": "->", "color": "#333"}, fontsize=8)
ax1.set_ylabel("thousand toman per USD (Bonbast sell)")
ax1.set_title("Bonbast USD, 3 Aug – 1 Oct 2026", fontsize=10)
ax1.tick_params(axis="x", labelrotation=30, labelsize=8)
ax1.set_ylim(180, 300)

y = np.arange(len(brackets))
h = 0.27
ax2.barh(y - h, v1, h, label="v1 (12 Sep)", color="#bbbbbb")
ax2.barh(y, v2, h, label="v2 (2 Oct)", color="#2c6fbb")
ax2.barh(y + h, pm, h, label="Polymarket (2 Oct, normalised)", color="#e39b2e")
ax2.set_yticks(y, brackets)
ax2.invert_yaxis()
ax2.set_xlabel("probability, %")
ax2.set_title("31 Dec 2026 rate, by bracket (toman)", fontsize=10)
ax2.legend(fontsize=8, loc="lower right")

fig.tight_layout()
fig.savefig(HERE / "path-and-distribution-v2.png", dpi=130)
print("wrote", HERE / "path-and-distribution-v2.png")
