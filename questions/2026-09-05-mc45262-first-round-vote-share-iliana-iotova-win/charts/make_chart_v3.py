"""Horizontal bars: campaign polls (decided-voter basis) vs the v3 forecast band.

Separate script so the v1/v2 charts stay exactly as published (append-only history).
Poll values: Wikipedia's normalised table (undecided/non-voters removed), accessed
2026-10-09; raw releases cross-checked against Mediapool, Taralej, Sofia Globe, Novinite.
"""
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use("Agg")

polls = [
    ("Sova Harris (23–28 Sep)", 50.2),
    ("Market Links (26–29 Sep)", 51.6),
    ("Alpha Research (24 Sep–1 Oct)", 44.5),
    ("Trend (26 Sep–2 Oct)", 47.8),
    ("Myara (26 Sep–4 Oct)", 46.9),
    ("Gallup Int. Balkan (26 Sep–6 Oct)", 47.8),
]
labels = [p[0] for p in polls]
vals = [p[1] for p in polls]

fig, ax = plt.subplots(figsize=(7.6, 4.8))
ax.axvspan(46.0, 51.4, color="#2166ac", alpha=0.12, label="v3 IQR [46.0, 51.4]")
ax.axvline(48.6, color="#2166ac", lw=2, label="v3 median 48.6")
ax.axvline(46.5, color="#888888", lw=1.2, ls="--", label="v2 median 46.5 (24 Sep)")
ax.axvline(45.45, color="#d6604d", lw=1.2, ls=":", label="Metaculus CP 45.4 (24 Sep, stale)")
bars = ax.barh(range(len(vals)), vals, color="#92a8c4", height=0.55)
for b, v in zip(bars, vals):
    ax.text(v + 0.2, b.get_y() + b.get_height() / 2, f"{v:.1f}", va="center", fontsize=9)
ax.set_yticks(range(len(vals)), labels, fontsize=9)
ax.invert_yaxis()
ax.set_xlim(35, 56)
ax.set_xlabel("Iotova share of decided voters (%)")
ax.set_title("Iotova first round — campaign polls vs forecast (2026-10-09)\n"
             "poll mean 48.1; April 2026 polls understated PB by ~7–10 pp", fontsize=10, loc="left")
ax.spines[["top", "right"]].set_visible(False)
ax.legend(fontsize=7.5, frameon=False, loc="upper center", bbox_to_anchor=(0.45, -0.17), ncol=2)
fig.tight_layout()
fig.savefig("charts/iotova_first_round_v3.png", dpi=150)
print("written")
