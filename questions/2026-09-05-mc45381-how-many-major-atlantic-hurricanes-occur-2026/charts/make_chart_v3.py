"""v3 chart: P(zero major hurricanes) over time — the three Metaculus cohorts,
the Kalshi mid, and each version of this forecast.

The point of the picture: between v2 and v3 every estimate converged into a
63-70% band, so the remaining disagreement is small relative to the
hazard-rate decay that drives this update.
"""
import json
from datetime import datetime, timezone
from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # set before any figure exists; this script only writes PNGs
import matplotlib.pyplot as plt


def ts(s: str) -> datetime:
    """Parse the fetcher's 'YYYY-MM-DD HH:MM' timestamps as UTC."""
    return datetime.strptime(s, "%Y-%m-%d %H:%M").replace(tzinfo=timezone.utc)


raw = json.loads(Path("raw/metaculus-2026-09-23.json").read_text())
fig, ax = plt.subplots(figsize=(9.5, 4.4))
for method, label, colour in [
    ("recency_weighted", "Metaculus CP", "#5aae61"),
    ("metaculus_pros", "Metaculus Pros", "#e08214"),
    ("gold_medalists", "Metaculus gold", "#8073ac"),
]:
    hist = raw["methods"][method]["history"]
    ax.plot([ts(p[0]) for p in hist], [p[1] * 100 for p in hist],
            color=colour, lw=1.7, label=label)

kalshi_t = [datetime(2026, 9, 17, 3, tzinfo=timezone.utc),
            datetime(2026, 9, 23, 5, tzinfo=timezone.utc)]
ax.plot(kalshi_t, [65.5, 69.5], "s--", color="#b2182b", lw=1.2, label="Kalshi mid")

# Own versions drawn as a step: each number holds until the next version.
mine_t = [datetime(2026, 9, 5, tzinfo=timezone.utc),
          datetime(2026, 9, 17, 5, tzinfo=timezone.utc),
          datetime(2026, 9, 23, 6, tzinfo=timezone.utc),
          datetime(2026, 9, 24, tzinfo=timezone.utc)]
ax.step(mine_t, [47.0, 63.0, 67.0, 67.0], where="post", color="#2166ac",
        lw=2.2, label="This forecast (v1→v2→v3)")

ax.set_ylim(15, 80)
ax.set_ylabel("P(zero major hurricanes) (%)")
ax.set_title("Every estimate has converged into a 63–70% band on option `0`",
             fontsize=11, loc="left")
ax.legend(fontsize=8.5, loc="lower right", framealpha=0.95)
ax.spines[["top", "right"]].set_visible(False)
ax.grid(alpha=0.25)
fig.autofmt_xdate(rotation=30)
fig.tight_layout()
fig.savefig("charts/trajectory_v3.png", dpi=150)
print("written charts/trajectory_v3.png")
