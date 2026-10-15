"""v4 chart: how each pollster's Likud-Yashar gap moved between v3 and v4, and the forecast path.

Panel 1 is the evidence behind the v4 revision: the latest poll per publisher as of
2026-10-09 (v3) against 2026-10-15 (v4). Panel 2 puts P(Yashar) by version next to the
Polymarket Yashar price on the same dates.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = ("questions/2026-09-20-mc45670-which-party-win-most-seats-2026-israeli/"
       "charts/gap-shift-2026-10-15.png")

INK, INK2, GRID = "#0b0b0b", "#52514e", "#e4e3df"
NEW, OLD = "#2a78d6", "#8f8e88"    # 15 Oct (v4) filled blue; 9 Oct (v3) hollow grey

# Likud minus Yashar, latest poll per publisher (raw/wikipedia-polling-wikitext-2026-10-09.txt
# and -2026-10-15.txt, plus Walla 13 Oct and i24 13 Oct from the outlets' own reports).
# None = no poll in the v3 window used.
rows = [
    ("Channel 14 (Filber)", 8, 9, True),
    ("i24 (Direct Polls)", 6, 6, True),
    ("Israel Hayom (Kantar)", -1, -1, False),
    ("Maariv (Lazar)", -2, -1, False),
    ("Channel 13", 0, -2, False),
    ("Walla (Lazar)", None, -2, False),
    ("Kan 11 (Kantar)", -2, -2, False),
    ("Channel 16 (Maagar Mochot)", -2, -2, False),
    ("Channel 12 (Midgam)", -2, -3, False),
    ("Zman Yisrael (Tatika)", 0, -4, False),
    ("Mainstream mean", -1.29, -2.13, False),
    ("Model gap₀ (10% Filber)", -0.46, -1.16, False),
]
rows.reverse()

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13.0, 5.6), gridspec_kw={"width_ratios": [1.3, 1]})
fig.patch.set_facecolor("#fcfcfb")
for ax in (ax1, ax2):
    ax.set_facecolor("#fcfcfb")
    ax.spines[["top", "right", "left"]].set_visible(False)
    ax.spines["bottom"].set_color(INK2)
    ax.tick_params(colors=INK2, labelsize=8.5)

for i, (name, old, new, filber) in enumerate(rows):
    if old is not None:
        ax1.plot([old, new], [i, i], color=GRID, lw=2, zorder=1)
        ax1.scatter(old, i, s=60, facecolor="#fcfcfb", edgecolor=OLD, lw=2, zorder=2,
                    label="latest poll as of 9 Oct (v3)" if i == len(rows) - 1 else None)
    ax1.scatter(new, i, s=64, color=NEW, edgecolor="#fcfcfb", lw=2, zorder=3,
                label="latest poll as of 15 Oct (v4)" if i == len(rows) - 1 else None)
    ax1.text(new + (0.35 if (old is None or new >= old) else -0.35), i, f"{new:+g}",
             va="center", ha="left" if (old is None or new >= old) else "right",
             fontsize=8, color=INK)
ax1.set_yticks(range(len(rows)))
ax1.set_yticklabels([r[0] for r in rows], fontsize=8.5, color=INK)
for tick, r in zip(ax1.get_yticklabels(), rows):
    if r[3]:
        tick.set_color("#b03a2e")
    if r[0].startswith(("Mainstream", "Model")):
        tick.set_fontweight("bold")
ax1.axvline(0, color=INK2, lw=0.8, ls=":")
ax1.axhline(1.5, color=GRID, lw=1)
ax1.set_xlim(-5.5, 10.5)
ax1.set_xlabel("Likud seats − Yashar seats (left of 0 = Yashar ahead)", color=INK2)
ax1.set_title("Three mainstream houses moved toward Yashar, one moved 1 seat to Likud;\n"
              "the mainstream mean widened from -1.3 to -2.1 seats", fontsize=10.5, loc="left",
              color=INK, pad=10)
ax1.legend(loc="lower right", fontsize=8, frameon=False, labelcolor=INK2)
ax1.grid(axis="x", color=GRID, lw=0.6)
ax1.set_axisbelow(True)

# --- panel 2: P(Yashar) by version vs Polymarket ------------------------------------
vers = ["v1  20 Sep", "v2  26 Sep", "v3  9 Oct", "v4  15 Oct"]
mine = [61.0, 61.5, 48.5, 58.7]
poly = [61.0, 59.0, 48.5, 61.75]
y = list(range(len(vers)))[::-1]
ax2.barh(y, mine, height=0.5, color=NEW, label="this forecast, P(Yashar)")
ax2.scatter(poly, y, marker="D", s=46, color="#eb6834", edgecolor="#fcfcfb", lw=1.5, zorder=3,
            label="Polymarket Yashar (ties on votes)")
for yi, m in zip(y, mine):
    ax2.text(1.0, yi, f"{m:.1f}%", va="center", ha="left", fontsize=8.5, color="#ffffff",
             fontweight="bold")
ax2.set_yticks(y)
ax2.set_yticklabels(vers, fontsize=8.5, color=INK)
ax2.axvline(50, color=INK2, lw=0.8, ls=":")
ax2.set_xlim(0, 75)
ax2.set_xlabel("probability Yashar wins the most seats (%)", color=INK2)
ax2.set_title("Back to a Yashar lean, ~3pp short of the market", fontsize=10.5, loc="left",
              color=INK, pad=10)
ax2.legend(loc="lower right", fontsize=8, frameon=False, labelcolor=INK2,
           bbox_to_anchor=(1.0, -0.32))
ax2.grid(axis="x", color=GRID, lw=0.6)
ax2.set_axisbelow(True)

fig.text(0.01, -0.02, "Red labels: Shlomo Filber's lineage (Channel 14; Direct Polls for i24), "
         "weighted 10% in the model. Mainstream mean = 8 publishers on 15 Oct (Walla returns), "
         "7 on 9 Oct.", fontsize=7.5, color=INK2)
fig.tight_layout()
fig.savefig(OUT, dpi=150, bbox_inches="tight", facecolor=fig.get_facecolor())
print("wrote", OUT)
