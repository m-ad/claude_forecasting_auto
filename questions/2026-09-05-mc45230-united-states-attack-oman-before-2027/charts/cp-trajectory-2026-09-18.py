"""Metaculus CP trajectory for #45230 against my three versions."""
import datetime as dt
import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

SNAPSHOT = Path(__file__).resolve().parent.parent / "raw" / "metaculus-2026-09-18.json"
with SNAPSHOT.open(encoding="utf-8") as fh:
    d = json.load(fh)
def series(name):
    xs, ys, seen = [], [], set()
    for t, v in d["methods"][name]["history"]:
        day = t[:10]
        if day in seen:
            continue
        seen.add(day)
        xs.append(dt.date.fromisoformat(day)); ys.append(v * 100)
    return xs, ys

fig, ax = plt.subplots(figsize=(9.5, 4.4))
for name, lbl, c in [("recency_weighted", "Community (CP)", "#3f6f8f"),
                     ("gold_medalists", "Gold medalists", "#c9a227"),
                     ("metaculus_pros", "Metaculus Pro", "#8a6fa8")]:
    xs, ys = series(name)
    ax.plot(xs, ys, marker="o", ms=3.5, lw=1.6, label=lbl, color=c)

mine = [(dt.date(2026, 9, 5), 12.0, "v1"), (dt.date(2026, 9, 10), 8.4, "v2"), (dt.date(2026, 9, 18), 5.5, "v3")]
ax.plot([m[0] for m in mine], [m[1] for m in mine], marker="D", ms=7, lw=2.0,
        color="#c1666b", label="my forecast")
for x, y, t in mine:
    ax.annotate(t, (x, y), textcoords="offset points", xytext=(4, 7), fontsize=9, color="#8c3f44")

ax.axvline(dt.date(2026, 9, 7), color="#555", ls="--", lw=1.1)
ax.text(dt.date(2026, 9, 7), 15.6, "  fine print amended:\n  target-or-harm requirement added",
        fontsize=8.5, color="#333", va="top")
ax.set_ylabel("P(US attacks Oman before 2027), %")
ax.set_ylim(0, 16.5)
ax.set_title("The crowd repriced within four days of the resolution criteria being tightened",
             fontsize=11, pad=12)
ax.legend(fontsize=9, frameon=False, loc="upper right")
ax.spines[["top", "right"]].set_visible(False)
fig.autofmt_xdate()
fig.tight_layout()
fig.savefig("questions/2026-09-05-mc45230-united-states-attack-oman-before-2027/charts/cp-trajectory-2026-09-18.png", dpi=150)
print("ok")
