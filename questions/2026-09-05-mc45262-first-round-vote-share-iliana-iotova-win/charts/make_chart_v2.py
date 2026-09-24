"""Horizontal bars: v1 vs v2 forecast mass for Iotova's first-round share.

Written as a separate script so the v1 chart (iotova_first_round.png) stays exactly
as published -- past versions are append-only, their figures included.
"""
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.use("Agg")

bins = ["< 40%", "40–43%", "43–46%", "46–49%", "49–52%", "> 52%"]
v1 = [13.0, 17.0, 25.0, 21.0, 15.0, 9.0]
v2 = [9.0, 14.0, 23.0, 25.0, 17.0, 12.0]

y = np.arange(len(bins))
h = 0.38
fig, ax = plt.subplots(figsize=(7.4, 4.2))
ax.barh(y - h / 2, v1, height=h, color="#b8c7d9", label="v1 2026-09-05 — median 45.4, IQR [42.0, 48.9]")
b2 = ax.barh(y + h / 2, v2, height=h, color="#2166ac", label="v2 2026-09-24 — median 46.5, IQR [43.3, 49.7]")
for b, m in zip(b2, v2):
    ax.text(m + 0.4, b.get_y() + b.get_height() / 2, f"{m:.0f}%", va="center", fontsize=9)
ax.set_yticks(y, bins)
ax.invert_yaxis()
ax.set_xlim(0, 31)
ax.set_xlabel("probability mass (%)")
ax.set_title("Iotova — first-round vote share: v1 → v2 (GERB stands aside)\n"
             "Metaculus 2026-09-24: CP 45.4 · Pro 45.7 · Gold 45.5", fontsize=10.5, loc="left")
ax.spines[["top", "right"]].set_visible(False)
ax.grid(axis="x", alpha=0.25)
ax.legend(fontsize=8, frameon=False, loc="lower right")
fig.tight_layout()
fig.savefig("charts/iotova_first_round_v2.png", dpi=150)
print("written")
