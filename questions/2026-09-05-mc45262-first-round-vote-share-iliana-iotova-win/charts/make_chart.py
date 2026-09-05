"""Horizontal bars: forecast probability mass for Iotova's first-round share,
with the historical Bulgarian first-round winner shares marked for context."""
import matplotlib
import matplotlib.pyplot as plt

# Non-interactive backend: this script only ever writes a PNG. Setting it after
# the pyplot import is safe because no figure has been created yet.
matplotlib.use("Agg")

bins = ["< 40%", "40–43%", "43–46%", "46–49%", "49–52%", "> 52%"]
mass = [13.0, 17.0, 25.0, 21.0, 15.0, 9.0]

fig, (ax, ax2) = plt.subplots(2, 1, figsize=(7.4, 5.0),
                              gridspec_kw={"height_ratios": [3, 1.15]})

bars = ax.barh(bins, mass, color="#2166ac", height=0.62)
for b, m in zip(bars, mass):
    ax.text(m + 0.5, b.get_y() + b.get_height() / 2, f"{m:.0f}%",
            va="center", fontsize=10, color="#22303f")
ax.invert_yaxis()
ax.set_xlim(0, 31)
ax.set_xlabel("probability mass (%)")
ax.set_title("Iotova — first-round vote share, 2026 Bulgarian presidential election\n"
             "median 45.4%, IQR [42.0%, 48.9%]", fontsize=10.5, loc="left")
ax.spines[["top", "right"]].set_visible(False)
ax.grid(axis="x", alpha=0.25)

# Every previous Bulgarian first-round winner, to show where 45% sits historically.
hist = {"Zhelev '92": 44.66, "Stoyanov '96": 44.07, "Parvanov '01": 36.39,
        "Parvanov '06": 64.05, "Plevneliev '11": 40.11, "Radev '16": 25.44,
        "Radev '21": 49.42}
ax2.scatter(list(hist.values()), [0] * len(hist), s=46, color="#7f7f7f", zorder=3)
for k, v in hist.items():
    ax2.annotate(k, (v, 0), textcoords="offset points", xytext=(0, 9),
                 ha="center", fontsize=7.2, rotation=32, color="#4a4a4a")
ax2.axvspan(42.0, 48.9, color="#2166ac", alpha=0.18, zorder=1)
ax2.axvline(45.4, color="#2166ac", lw=2, zorder=2)
ax2.set_xlim(20, 70)
ax2.set_yticks([])
ax2.set_xlabel("first-round winner's vote share (%) — past elections, grey; this forecast, blue")
ax2.spines[["top", "right", "left"]].set_visible(False)

fig.tight_layout()
fig.savefig("charts/iotova_first_round.png", dpi=150)
print("written")
