"""Horizontal dot plot: campaign polls as published (decided basis) vs a CIK-basis estimate, with the v4 band.

Separate script so the v1-v3 charts stay exactly as published (append-only history).
CIK resolves on all valid votes *including* "I support no one" (NOTA). Trend, Alpha and Myara
already carry NOTA in their base, so they are unchanged; Gallup, Market Links and Sova Harris
report no NOTA, so they are rescaled by 0.975 (an assumed ~2.5% NOTA, the 2021 first-round level).
Poll values: Wikipedia's normalised table and primary write-ups, accessed 2026-10-09 / 2026-10-15.
"""
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use("Agg")

# (label, published decided-basis share, CIK-basis estimate)
polls = [
    ("Sova Harris (23–28 Sep)", 50.2, 48.9),
    ("Market Links (26–29 Sep)", 51.6, 50.3),
    ("Alpha Research (24 Sep–1 Oct)", 44.5, 44.5),
    ("Trend (26 Sep–2 Oct)", 47.8, 47.8),
    ("Myara (26 Sep–4 Oct)", 46.9, 46.9),
    ("Gallup Int. Balkan (26 Sep–6 Oct)", 47.8, 46.6),
]
labels = [p[0] for p in polls]
published = [p[1] for p in polls]
cik = [p[2] for p in polls]

# Validated categorical slots 1-2 (dataviz validator: all checks pass on light surface).
C_PUB, C_CIK = "#2a78d6", "#eb6834"
y = list(range(len(polls)))

fig, ax = plt.subplots(figsize=(7.8, 5.0))
ax.axvspan(45.1, 50.4, color="#2a78d6", alpha=0.10, label="v4 IQR [45.1, 50.4]")
ax.axvline(47.7, color="#1c5cab", lw=2, label="v4 median 47.7")
ax.axvline(48.6, color="#888888", lw=1.2, ls="--", label="v3 median 48.6 (9 Oct)")
# Dot plot, not bars: the axis does not start at zero, and bars would exaggerate gaps.
for i, (a, b) in enumerate(zip(published, cik)):
    ax.plot([a, b], [i, i], color="#bbbbbb", lw=2, zorder=2)
ax.scatter(published, y, s=70, color=C_PUB, edgecolor="white", linewidth=2, zorder=3,
           label="published (decided voters)")
ax.scatter(cik, y, s=70, color=C_CIK, edgecolor="white", linewidth=2, zorder=4,
           label="CIK basis est. (NOTA in denominator)")
for i, (a, b) in enumerate(zip(published, cik)):
    if abs(a - b) < 0.05:
        ax.text(a + 0.25, i, f"{a:.1f}", va="center", fontsize=8, color="#333333")
    else:
        ax.text(max(a, b) + 0.25, i, f"{a:.1f} → {b:.1f}", va="center", fontsize=8,
                color="#333333")
ax.set_yticks(y, labels, fontsize=9)
ax.invert_yaxis()
ax.set_xlim(40, 54)
ax.set_xlabel("Iotova first-round share (%)")
ax.set_title("Iotova first round — polls on the resolution basis vs forecast (2026-10-15)\n"
             "no poll fielded after 6 Oct yet; NOTA-adjusted mean 47.5 vs published 48.1",
             fontsize=10, loc="left")
ax.spines[["top", "right"]].set_visible(False)
ax.grid(axis="x", color="#e5e5e5", lw=0.6)
ax.set_axisbelow(True)
ax.legend(fontsize=7.5, frameon=False, loc="upper center", bbox_to_anchor=(0.42, -0.14), ncol=2)
fig.tight_layout()
fig.savefig("charts/iotova_first_round_v4.png", dpi=150)
print("written")
