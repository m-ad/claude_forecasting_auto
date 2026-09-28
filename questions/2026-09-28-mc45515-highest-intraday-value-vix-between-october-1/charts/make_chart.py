"""Chart: Oct 1–Dec 24 VIX intraday maxima in years that started from a calm VIX, vs. the v1 forecast band."""
import csv
import datetime as dt

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

Q = "questions/2026-09-28-mc45515-highest-intraday-value-vix-between-october-1"
with open(f"{Q}/raw/VIX_History-2026-09-28.csv") as fh:
    rows = [
        (dt.date(int(r["DATE"][6:]), int(r["DATE"][:2]), int(r["DATE"][3:5])), float(r["HIGH"]), float(r["CLOSE"]))
        for r in csv.DictReader(fh)
    ]
years, maxes = [], []
for y in range(1992, 2026):  # 1992: first year with true intraday highs in the Cboe file
    sep = [r for r in rows if dt.date(y, 9, 1) <= r[0] <= dt.date(y, 9, 28)]
    win = [r for r in rows if dt.date(y, 10, 1) <= r[0] <= dt.date(y, 12, 24)]
    # Only calm-start years are comparable to the current VIX of ~15.
    if 11.5 <= sep[-1][2] <= 18.5:
        years.append(str(y))
        maxes.append(max(r[1] for r in win))

fig, ax = plt.subplots(figsize=(7.5, 6.5), facecolor="#fcfcfb")
ax.set_facecolor("#fcfcfb")
ax.axvspan(20.0, 28.5, color="#2a78d6", alpha=0.12, lw=0, label="v1 forecast IQR [20.0, 28.5]")
ax.axvline(23.3, color="#0b0b0b", lw=1.5, ls="--", label="v1 median 23.3")
ax.barh(years, maxes, color="#2a78d6", height=0.7)
for yv, m in zip(years, maxes):
    ax.text(m + 0.4, yv, f"{m:.1f}", va="center", fontsize=8, color="#52514e")
ax.invert_yaxis()
ax.set_xlabel("Highest intraday VIX, Oct 1 – Dec 24", color="#52514e")
ax.set_title(
    "Q4 VIX peaks in years where late-September VIX was 11.5–18.5\n(Cboe daily history; 2026 starts at 14.87)",
    fontsize=11, color="#0b0b0b", loc="left",
)
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
ax.grid(axis="x", color="#e5e4df", lw=0.8)
ax.set_axisbelow(True)
ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.09), ncol=2, frameon=False, fontsize=9)
fig.tight_layout()
fig.savefig(f"{Q}/charts/q4-vix-peaks-calm-start-years.png", dpi=150)
print(list(zip(years, maxes)))
