"""Render the v1 -> v2 driver waterfall for Metaculus #45230.

Horizontal bars are used per the operator's stated preference; the waterfall
form is chosen because the whole point of the update is *which* driver moved
the number, not the endpoint.
"""

from __future__ import annotations

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

DRIVERS: list[tuple[str, float]] = [
    ("Prior — v1, 2026-09-05", 12.0),
    ("US strike log: 18 engagements,\nnone in Omani territorial waters", -3.5),
    ("Project Freedom is a 1-day\npaused op, not a standing escort", -1.0),
    ("Hormuz traffic collapse\n(85 → ~6–10 transits/day)", -0.8),
    ("Oman *consents* to Western\nnaval activity in its waters", -1.0),
    ("24 quiet days since the\nAug-17 threat; Oman off the story", -0.6),
    ("Time decay (117 → 113 days)", -0.3),
    ("September escalation\n(BMs at a US carrier, 'prohibited zone')", +1.0),
    ("Locatability higher than assumed\n(JMIC publishes nm-from-coast)", +0.3),
    ("Smaller ambiguity haircut needed\n(literal-reading path shrank)", +2.3),
    ("New forecast — v2, 2026-09-10", 8.4),
]

fig, ax = plt.subplots(figsize=(10.5, 6.4))

running = 0.0
ypos = list(range(len(DRIVERS)))[::-1]

for y, (label, val) in zip(ypos, DRIVERS):
    terminal = label.startswith(("Prior", "New forecast"))
    if terminal:
        ax.barh(y, val, left=0, color="#2f4b7c", height=0.62)
        ax.text(val + 0.25, y, f"{val:.1f}%", va="center", fontsize=9,
                fontweight="bold", color="#2f4b7c")
        running = val
    else:
        start = running
        running += val
        ax.barh(y, val, left=start, height=0.55,
                color="#c0392b" if val > 0 else "#3d7a5a")
        ax.text(max(start, running) + 0.25, y, f"{val:+.1f} pp", va="center",
                fontsize=9, color="#c0392b" if val > 0 else "#3d7a5a")

ax.set_yticks(ypos)
ax.set_yticklabels([lab for lab, _ in DRIVERS], fontsize=8.5)
ax.set_xlabel("P(United States attacks Oman before 2027)  —  %")
ax.set_xlim(0, 16)
ax.axvline(0, color="#999", linewidth=0.8)
ax.set_title(
    "Metaculus #45230 — what moved the forecast, v1 → v2\n"
    "green = downward driver, red = upward driver",
    fontsize=11,
)
ax.grid(axis="x", alpha=0.25)
ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
fig.savefig(
    "questions/2026-09-05-mc45230-united-states-attack-oman-before-2027/"
    "charts/v1-to-v2-waterfall.png",
    dpi=160,
)
