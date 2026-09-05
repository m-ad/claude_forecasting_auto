"""Horizontal bars comparing this forecast's option vector with the Kalshi board
(11 Aug 2026) and the OLBG bookmaker board (2 Sep 2026, gross of overround)."""
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Non-interactive backend: this script only ever writes a PNG. Setting it after
# the pyplot import is safe because no figure has been created yet.
matplotlib.use("Agg")

rows = [
    # option, forecast, kalshi (None = not listed), bookmaker gross (None = not listed)
    ("Other individual",            47.0, None, None),
    ("Sudan Emergency Resp. Rooms", 15.0, 25.0, 25.0),
    ("Other organization",          12.0, None, None),
    ("ICC / ICJ",                    6.5, None, None),
    ("Doctors Without Borders",      5.0, 13.0, 20.0),
    ("Yulia Navalnaya",              3.5, None, 12.5),
    ("Save the Children",            3.5, 12.0, 10.0),
    ("Mykola Kuleba / Save Ukraine", 2.5, None, None),
    ("UNRWA",                        2.5, None, 11.1),
    ("Pope Leo XIV",                 1.5, None, 11.1),
    ("Donald J. Trump",              1.0,  4.0,  7.7),
]

labels = [r[0] for r in rows]
mine = np.array([r[1] for r in rows])
y = np.arange(len(rows))

fig, ax = plt.subplots(figsize=(8.2, 4.6))
ax.barh(y, mine, height=0.55, color="#2166ac", label="this forecast", zorder=3)
for i, r in enumerate(rows):
    if r[2] is not None:
        ax.plot(r[2], i, marker="D", ms=6, color="#d6604d", zorder=4,
                label="Kalshi, 11 Aug 2026" if i == 1 else None)
    if r[3] is not None:
        ax.plot(r[3], i, marker="o", ms=6, mfc="none", mec="#7a7a7a", zorder=4,
                label="bookmakers, 2 Sep 2026 (gross)" if i == 1 else None)
    ax.text(r[1] + 0.7, i, f"{r[1]:.1f}%", va="center", fontsize=9, color="#22303f")

ax.set_yticks(y, labels, fontsize=9)
ax.invert_yaxis()
ax.set_xlim(0, 52)
ax.set_xlabel("probability (%)")
ax.set_title("2026 Nobel Peace Prize — forecast vs. market boards\n"
             "the two 'Other' buckets take 59% because the Committee's pick is\n"
             "usually not on anyone's list", fontsize=10.5, loc="left")
ax.legend(loc="lower right", fontsize=8.5, frameon=False)
ax.spines[["top", "right"]].set_visible(False)
ax.grid(axis="x", alpha=0.25, zorder=1)
fig.tight_layout()
fig.savefig("charts/nobel_2026_options.png", dpi=150)
print("written")
