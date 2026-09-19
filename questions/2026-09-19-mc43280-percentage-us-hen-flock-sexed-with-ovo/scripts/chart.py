"""Chart for the US in-ovo sexing penetration question (Metaculus 43280).

A bottom-up build of the US standing layer flock that will have been sexed
in-ovo by mid-2027, producer by producer, against a 307.9 M-hen table-egg flock
(USDA, 1 Feb 2026). Horizontal, because the point is the size of each block and
how little of the flock they add up to — not a time trend.

Hen counts are the working estimates argued in research.md; they are uncertain
to roughly +/-40% each, which is why the forecast band is wide relative to the
median.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT = Path(__file__).resolve().parents[1] / "charts"
OUT.mkdir(exist_ok=True)

US_FLOCK = 307.9  # million table-egg layers, USDA Chickens and Eggs, 1 Feb 2026

# label, hens already in-ovo sexed at Jun 2026, added by ~Jun 2027
ROWS = [
    ("NestFresh (Hidden Villa Ranch)\n100% converted Jun 2026", 0.8, 0.1),
    ("Sauder's Eggs\nspecialty lines from Aug 2026", 0.3, 0.4),
    ("Kipster USA\nown brand launches early 2027", 0.2, 0.1),
    ("Vital Farms\nfirst in-ovo birds arrive early 2027", 0.0, 2.0),
    ("McLean Farms and other\nearly adopters", 0.4, 0.3),
    ("Unattributed hatchery volume\nimplied by IAA's <1% Jun-2026 base", 0.9, 1.2),
]

fig, ax = plt.subplots(figsize=(10, 5.4))
y = np.arange(len(ROWS))[::-1]
base = [r[1] for r in ROWS]
add = [r[2] for r in ROWS]

ax.barh(y, base, color="#1f4e79", height=0.55, label="in the standing flock at Jun 2026")
ax.barh(y, add, left=base, color="#5dade2", height=0.55, label="added by ~Jun 2027")
for yi, (lab, b, a) in zip(y, ROWS):
    ax.annotate(f"{b + a:.1f}M hens = {100 * (b + a) / US_FLOCK:.2f}%", (b + a, yi),
                textcoords="offset points", xytext=(7, -3), fontsize=9)

ax.set_yticks(y)
ax.set_yticklabels([r[0] for r in ROWS], fontsize=8.5)
ax.set_xlim(0, 3.2)
ax.set_xlabel("million hens (US table-egg flock = 307.9 M, USDA 1 Feb 2026)")
ax.grid(axis="x", alpha=0.25)
ax.legend(fontsize=9, loc="upper right", framealpha=0.95)

total = sum(base) + sum(add)
ax.set_title(
    f"US bottom-up: ~{total:.1f}M hens = {100 * total / US_FLOCK:.1f}% by mid-2027\n"
    f"my median 2.4%  ·  Metaculus CP 3.2%  ·  Pro 3.6%",
    fontsize=11,
)
fig.tight_layout()
fig.savefig(OUT / "us-bottom-up-buildup.png", dpi=150)
print("wrote", OUT / "us-bottom-up-buildup.png")
