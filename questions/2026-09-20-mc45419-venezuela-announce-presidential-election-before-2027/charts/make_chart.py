"""Chart for MC 45419: scenario weights and how the estimates compare.

Two horizontal-bar panels, per the repo's preference for horizontal bars: the left
panel is where the 9.5% comes from (weights of mutually exclusive scenarios, YES ones
highlighted), the right panel places that number among the other estimates, with the
two market/model figures restated on *this* question's stricter criterion.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # headless: no display in CI or the container

import matplotlib.pyplot as plt  # imported after the backend is fixed

OUT = Path(__file__).with_name("scenarios-and-comparison-v1.png")

scenarios = [
    ("5. A date, but for 2028+ or a\nnon-presidential vote", 4.0, False),
    ("4. Top-down announcement\n(US deal / falta absoluta)", 3.0, True),
    ("3. New CNE + 2027 calendar\npublished before 31 Dec", 6.5, True),
    ("2. New CNE seated, calendar\ndeferred to 2027", 14.5, False),
    ("1. Status-quo drift:\nno CNE, no date in 2026", 72.0, False),
]

# Market/model rows are restated on the Metaculus criterion (vote before 2028) by the
# 0.80 factor derived in research.md; the raw prices are kept in the labels.
comparison = [
    ("Kalshi: vote *held* before\n2027-06-01 (thin, longshot-rich)", 21.5, "raw"),
    ("Polymarket 16¢ → this\nquestion's criterion", 12.8, "derived"),
    ("Inside-view decomposition", 10.4, "mine"),
    ("Octagon model 11.4% → this\nquestion's criterion", 9.1, "derived"),
    ("Outside view, conditional\nhazard at t=8.5 months", 8.0, "mine"),
]

FG = "#1b3a4b"
YES = "#c2543d"
NO = "#a8b8c0"
DERIVED = "#7b93a3"

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13.5, 5.4))

labels = [s[0] for s in scenarios]
vals = [s[1] for s in scenarios]
cols = [YES if s[2] else NO for s in scenarios]
ax1.barh(range(len(vals)), vals, color=cols, height=0.62)
ax1.set_yticks(range(len(vals)), labels, fontsize=8.5)
ax1.set_xlim(0, 80)
ax1.set_xlabel("weight (%)", fontsize=9)
ax1.set_title("Scenario weights — YES branches in red sum to 9.5%", fontsize=10.5, color=FG)
for i, v in enumerate(vals):
    ax1.text(v + 1.2, i, f"{v:.1f}", va="center", fontsize=8.5, color=FG)

labels2 = [c[0] for c in comparison]
vals2 = [c[1] for c in comparison]
cols2 = {"raw": NO, "derived": DERIVED, "mine": FG}
ax2.barh(range(len(vals2)), vals2, color=[cols2[c[2]] for c in comparison], height=0.62)
ax2.set_yticks(range(len(vals2)), labels2, fontsize=8.5)
ax2.set_xlim(0, 25)
ax2.set_xlabel("probability (%)", fontsize=9)
ax2.set_title("Estimates, restated on this question's criterion", fontsize=10.5, color=FG)
for i, v in enumerate(vals2):
    ax2.text(v + 0.4, i, f"{v:.1f}", va="center", fontsize=8.5, color=FG)
ax2.axvline(9.5, color=YES, lw=1.6, ls="--")
ax2.text(9.9, 4.35, "forecast 9.5%", color=YES, fontsize=9)

for ax in (ax1, ax2):
    ax.spines[["top", "right", "left"]].set_visible(False)
    ax.tick_params(axis="y", length=0)
    ax.xaxis.grid(True, color="#e2e8ec", lw=0.8)
    ax.set_axisbelow(True)

fig.suptitle(
    "Will Venezuela announce a presidential election before 2027? (Metaculus 45419) — 2026-09-20",
    fontsize=11.5, color=FG, y=0.99,
)
fig.tight_layout(rect=(0, 0, 1, 0.94))
fig.savefig(OUT, dpi=160)
print(f"wrote {OUT}")
