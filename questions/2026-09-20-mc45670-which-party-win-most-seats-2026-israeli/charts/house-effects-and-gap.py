"""Two panels: the pollster house split, and the resulting seat-gap distribution.

The house split is the whole question. Every mainstream Israeli house puts
Yashar 2-4 seats ahead of Likud; the two Filber-lineage houses put Likud 5-9
ahead. Panel 2 shows what a 10% weight on the latter does to the gap.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT = ("questions/2026-09-20-mc45670-which-party-win-most-seats-2026-israeli/"
       "charts/house-effects-and-gap.png")

# Mean Likud / Yashar seats per publisher, polls with fieldwork 2026-08-01..09-17,
# parsed from the Wikipedia polling table (raw/wikipedia-polling-wikitext-2026-09-20.txt).
houses = [
    ("Channel 14 (Filber)", 31.1, 22.3, 10, True),
    ("i24 (Direct Polls)", 28.0, 22.7, 7, True),
    ("Zman Yisrael", 21.7, 23.7, 7, False),
    ("Kan 11 (Kantar)", 21.9, 23.6, 9, False),
    ("Israel Hayom (Kantar)", 21.5, 23.0, 4, False),
    ("HaHadashot 12 (Midgam)", 21.8, 24.0, 8, False),
    ("Walla (Lazar)", 21.3, 24.7, 3, False),
    ("Channel 16 (Maagar)", 20.8, 22.2, 6, False),
    ("Channel 13", 20.4, 23.1, 7, False),
    ("Maariv (Lazar)", 20.0, 24.1, 8, False),
]
houses.sort(key=lambda h: h[1] - h[2])

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13.5, 5.4),
                               gridspec_kw={"width_ratios": [1.25, 1]})

y = np.arange(len(houses))
h = 0.36
likud = [x[1] for x in houses]
yashar = [x[2] for x in houses]
labels = [f"{x[0]}  (n={x[3]})" for x in houses]

ax1.barh(y + h / 2, likud, h, color="#2b4f81", label="Likud")
ax1.barh(y - h / 2, yashar, h, color="#d98c2b", label="Yashar")
for yi, (lk, ys) in enumerate(zip(likud, yashar)):
    ax1.text(lk + 0.35, yi + h / 2, f"{lk:.1f}", va="center", fontsize=8, color="#2b4f81")
    ax1.text(ys + 0.35, yi - h / 2, f"{ys:.1f}", va="center", fontsize=8, color="#a9691d")
ax1.set_yticks(y)
ax1.set_yticklabels(labels, fontsize=8.5)
for tick, x in zip(ax1.get_yticklabels(), houses):
    if x[4]:                       # Filber-lineage houses, flagged in red
        tick.set_color("#b03a2e")
ax1.set_xlim(0, 36)
ax1.set_xlabel("mean projected Knesset seats, fieldwork 1 Aug – 17 Sep 2026")
ax1.set_title("Every mainstream house has Yashar ahead.\nThe two that do not share one pollster's lineage",
              fontsize=10.5, pad=10, loc="left")
ax1.legend(loc="lower right", fontsize=9, frameon=False)
ax1.spines[["top", "right"]].set_visible(False)
ax1.text(0.02, -0.155, "Red: Shlomo Filber founded Direct Polls (2018) and has polled for "
                       "Channel 14 since June 2025; Wikipedia's polling page flags his Likud ties.",
         transform=ax1.transAxes, fontsize=7.5, color="#b03a2e")

# --- panel 2: the modelled gap -------------------------------------------------
rng = np.random.default_rng(45670)
gap = np.rint(-2.11 + rng.normal(1.2, 3.2, 400_000) + rng.normal(0, 1.3, 400_000))
vals, counts = np.unique(gap, return_counts=True)
frac = counts / counts.sum()
keep = (vals >= -12) & (vals <= 10)
colors = ["#d98c2b" if v < 0 else ("#8d8d8d" if v == 0 else "#2b4f81") for v in vals[keep]]
ax2.bar(vals[keep], frac[keep] * 100, width=0.9, color=colors)
ax2.axvline(0, color="#333", lw=0.8, ls=":")
ax2.set_xlabel("Likud seats − Yashar seats on 2026-10-27 (modelled)")
ax2.set_ylabel("probability (%)")
ax2.set_title("Yashar largest 61.0%  ·  Likud 38.1%  ·  exact tie 11.1%\n"
              "(vector below is conditional on the question resolving)",
              fontsize=10.5, pad=10, loc="left")
ax2.spines[["top", "right"]].set_visible(False)
ax2.set_ylim(0, 15.5)
ax2.annotate("exact tie → resolution\nnot defined in the fine print",
             xy=(0.35, frac[vals == 0][0] * 100), xytext=(3.0, 13.2), fontsize=8, color="#555",
             arrowprops={"arrowstyle": "->", "color": "#555", "lw": 0.8})

fig.tight_layout()
fig.savefig(OUT, dpi=150, bbox_inches="tight")
print("wrote", OUT)
