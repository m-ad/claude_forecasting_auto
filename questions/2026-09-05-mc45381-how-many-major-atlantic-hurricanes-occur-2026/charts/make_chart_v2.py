"""v2 charts: (a) distribution comparison across the four live estimates,
(b) the Metaculus CP trajectory on option `0` against my own two versions.

Both panels exist to make one point visually: every independent estimate of
P(zero major hurricanes) has moved up since 5 September, and the Metaculus
community is the last one still climbing toward the others.
"""
import json
from datetime import UTC, datetime
from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # set before any figure exists; this script only writes PNGs
import matplotlib.pyplot as plt

OPTIONS = ["0", "1", "2", "3", "4+"]
# Kalshi buckets are differenced from the ">N" strike mid-prices and monotonised;
# the strikes above ">2" trade at the 1-2 cent minimum tick and are dust.
SERIES = {
    "This forecast v2 (17 Sep)": ([63.0, 26.0, 8.5, 2.0, 0.5], "#2166ac"),
    "Kalshi mid (17 Sep)": ([65.5, 19.5, 12.0, 1.5, 1.5], "#b2182b"),
    "Metaculus CP (17 Sep)": ([52.5, 35.4, 9.1, 2.0, 1.0], "#5aae61"),
    "This forecast v1 (5 Sep)": ([47.0, 31.0, 15.0, 5.0, 2.0], "#999999"),
}

fig, (ax1, ax2) = plt.subplots(
    1, 2, figsize=(12.6, 4.3), gridspec_kw={"width_ratios": [1.05, 1]}
)

# --- panel A: distribution comparison ------------------------------------
n = len(SERIES)
height = 0.78 / n
for i, (label, (probs, colour)) in enumerate(SERIES.items()):
    ys = [y + (i - (n - 1) / 2) * height for y in range(len(OPTIONS))]
    ax1.barh(ys, probs, height=height, color=colour, label=label, zorder=2)
ax1.set_yticks(range(len(OPTIONS)))
ax1.set_yticklabels(OPTIONS)
ax1.invert_yaxis()
ax1.set_xlim(0, 72)
ax1.set_xlabel("probability (%)")
ax1.set_ylabel("major hurricanes (Cat 3+)")
ax1.set_title("A · Where the four estimates sit", fontsize=11, loc="left")
ax1.legend(fontsize=8.2, loc="lower right", framealpha=0.95)
ax1.spines[["top", "right"]].set_visible(False)
ax1.grid(axis="x", alpha=0.25, zorder=1)

# --- panel B: CP trajectory on option `0` --------------------------------
raw = json.loads(Path("raw/metaculus-2026-09-17.json").read_text())
hist = raw["methods"]["recency_weighted"]["history"]
xs = [datetime.strptime(p[0], "%Y-%m-%d %H:%M").replace(tzinfo=UTC)
      for p in hist]
ys = [p[1] * 100 for p in hist]
ax2.plot(xs, ys, color="#5aae61", lw=1.9, label="Metaculus CP, option `0`", zorder=3)

ax2.axhline(65.5, color="#b2182b", ls="--", lw=1.4, label="Kalshi mid (17 Sep)", zorder=2)
ax2.axhline(63.0, color="#2166ac", ls="-", lw=1.4, label="This forecast v2", zorder=2)
ax2.axhline(47.0, color="#999999", ls=":", lw=1.6, label="This forecast v1", zorder=2)
ax2.axhline(40.0, color="#8c6bb1", ls="-.", lw=1.2, label="WeatherTiger (9 Sep)", zorder=2)

# CP reveal is where the tripwire was checked: 27.3% on option `0`, below the
# 30% threshold v1 set, which is what forced a re-analysis rather than a nudge.
reveal = datetime(2026, 9, 10, 17, 1, tzinfo=UTC)
ax2.scatter([reveal], [27.3], s=48, color="#5aae61", edgecolor="black", zorder=5)
ax2.annotate("CP reveal 27.3%\n(tripwire fired)", (reveal, 27.3),
             textcoords="offset points", xytext=(8, -26), fontsize=8.2)

ax2.set_ylim(15, 75)
ax2.set_ylabel("P(zero major hurricanes) (%)")
ax2.set_title("B · Everyone is converging upward on `0`", fontsize=11, loc="left")
ax2.legend(fontsize=8.2, loc="lower right", framealpha=0.95)
ax2.spines[["top", "right"]].set_visible(False)
ax2.grid(alpha=0.25)
fig.autofmt_xdate(rotation=30)

fig.tight_layout()
fig.savefig("charts/distribution_v2.png", dpi=150)
print("written charts/distribution_v2.png")
