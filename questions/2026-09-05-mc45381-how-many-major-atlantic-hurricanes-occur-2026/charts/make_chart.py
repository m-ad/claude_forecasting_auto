"""Horizontal bar chart of the forecast distribution over major-hurricane counts,
with the NOAA August-2026 70% range shaded for comparison."""
import matplotlib
import matplotlib.pyplot as plt

# Non-interactive backend: this script only ever writes a PNG. Setting it after
# the pyplot import is safe because no figure has been created yet.
matplotlib.use("Agg")

options = ["0", "1", "2", "3", "4+"]
probs = [47.0, 31.0, 15.0, 5.0, 2.0]

fig, ax = plt.subplots(figsize=(7.2, 3.4))
# NOAA's Aug-2026 outlook gave 0-2 major hurricanes at 70% confidence; shading it
# shows the forecast sits inside the official range rather than fighting it.
ax.axhspan(-0.5, 2.5, color="#9ecae1", alpha=0.22, zorder=0)
bars = ax.barh(options, probs, color="#2166ac", height=0.62, zorder=2)
for b, p in zip(bars, probs):
    ax.text(p + 0.9, b.get_y() + b.get_height() / 2, f"{p:.1f}%",
            va="center", fontsize=10, color="#22303f")
ax.invert_yaxis()
ax.set_xlim(0, 55)
ax.set_xlabel("probability (%)")
ax.set_ylabel("major hurricanes (Cat 3+)")
ax.set_title("2026 Atlantic major hurricanes — forecast distribution\n"
             "shaded band = NOAA August-2026 outlook range (0–2, 70% conf.)",
             fontsize=10.5, loc="left")
ax.spines[["top", "right"]].set_visible(False)
ax.grid(axis="x", alpha=0.25, zorder=1)
fig.tight_layout()
fig.savefig("major_hurricane_distribution.png", dpi=150)
print("written")
