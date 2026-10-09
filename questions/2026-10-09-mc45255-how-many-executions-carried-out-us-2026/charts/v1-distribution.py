"""Chart for mc45255 v1: option probabilities and where the remaining executions come from."""
from pathlib import Path

import matplotlib.pyplot as plt

OUT = Path(__file__).with_name("v1-distribution.png")
BLUE, INK, MUTED, SURF = "#2a78d6", "#0b0b0b", "#6b6b68", "#fcfcfb"

options = ["Fewer than 39", "39", "40", "41", "More than 41"]
probs = [13.5, 13.0, 18.0, 19.5, 36.0]

# Expected additional executions after 2026-10-08, by source (model means)
src = [
    ("FL: 3 scheduled (Robertson, Reaves, Guardado)", 0.96 + 0.93 + 0.92),
    ("FL: new warrants for Nov 6 – Dec 31", 3.62 * 0.93),
    ("TX: Rubio, Dennes", 0.72 + 0.82),
    ("AL Taylor + OK Pavatt + IN Weisheit", 0.87 + 0.72 + 0.72),
    ("Military: Hasan (Dec 3)", 0.40),
    ("Other states, not yet scheduled", 0.45),
]

fig, (a1, a2) = plt.subplots(2, 1, figsize=(8, 6.4), gridspec_kw={"height_ratios": [5, 6]})
fig.patch.set_facecolor(SURF)
for ax in (a1, a2):
    ax.set_facecolor(SURF)
    for s in ("top", "right", "left"):
        ax.spines[s].set_visible(False)
    ax.spines["bottom"].set_color(MUTED)
    ax.tick_params(colors=MUTED, length=0)

a1.barh(options[::-1], probs[::-1], color=BLUE, height=0.6)
for y, p in enumerate(probs[::-1]):
    a1.text(p + 0.6, y, f"{p:.1f}%", va="center", color=INK, fontsize=9)
a1.set_xlim(0, 42)
a1.set_title("v1 forecast: 2026 US executions (30 done as of Oct 8)", loc="left", color=INK, fontsize=11)
a1.set_xlabel("probability (%)", color=MUTED)

labels, vals = zip(*src)
a2.barh(labels[::-1], vals[::-1], color=BLUE, height=0.6)
for y, v in enumerate(vals[::-1]):
    a2.text(v + 0.04, y, f"{v:.1f}", va="center", color=INK, fontsize=9)
a2.set_xlim(0, 4.2)
a2.set_title(f"Expected additional executions by source (total ≈ {sum(vals):.1f})",
             loc="left", color=INK, fontsize=11)
a2.set_xlabel("expected executions", color=MUTED)

fig.tight_layout()
fig.savefig(OUT, dpi=150, facecolor=SURF)
