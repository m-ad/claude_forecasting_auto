"""Charts for the SWP (Shr)Impact forecast: observed trajectory + outcome bands."""

from __future__ import annotations

import datetime as dt
import itertools
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from model import simulate  # imported after the sys.path insert above

INK, ACC, BAND = "#1b2a41", "#c1553b", "#8fb6c9"

# (date, headline bn, agreements, source label)
HIST = [
    (dt.date(2025, 4, 15), 3.3, 17, "EA Forum 2030-vision post / ACE review"),
    (dt.date(2025, 9, 16), 4.0, 21, "SWP press release (21st MOU)"),
    (dt.date(2025, 11, 21), 4.5, 24, "EA Forum marginal-funding post"),
    (dt.date(2026, 1, 14), 4.7, 25, "SWP press release (25th MOU, inferred bn)"),
    (dt.date(2026, 6, 29), 5.6, 31, "Aqua Culture Asia Pacific (inferred bn)"),
    (dt.date(2026, 9, 17), 6.3, 36, "shrimpwelfareproject.org/shrimpact"),
]
TARGET = dt.date(2027, 7, 1)


def main() -> None:
    s = simulate()
    p25, p50, p75 = (float(np.percentile(s, q)) for q in (25, 50, 75))
    p10, p90 = (float(np.percentile(s, q)) for q in (10, 90))

    fig, (ax1, ax2) = plt.subplots(
        2, 1, figsize=(9.5, 8.4), gridspec_kw={"height_ratios": [1.25, 1]}
    )

    # --- panel 1: trajectory ---------------------------------------------
    xs = [d for d, *_ in HIST]
    ys = [v for _, v, *_ in HIST]
    ax1.plot(xs, ys, "o-", color=INK, lw=2, ms=6, label="published headline (Shr)Impact")
    for d, v, a, _ in HIST:
        ax1.annotate(f"{a}", (d, v), textcoords="offset points", xytext=(0, -14),
                     ha="center", fontsize=7.5, color="#5a6a7a")

    ax1.plot([xs[-1], TARGET], [ys[-1], p50], "--", color=ACC, lw=1.6)
    ax1.errorbar([TARGET], [p50], yerr=[[p50 - p25], [p75 - p50]], fmt="D",
                 color=ACC, ms=8, capsize=6, lw=2.4, label="forecast: median, IQR")
    ax1.errorbar([TARGET], [p50], yerr=[[p50 - p10], [p90 - p50]], fmt="none",
                 color=ACC, alpha=0.4, capsize=3, lw=1.2)
    ax1.axhspan(6.95, 12.05, color=BAND, alpha=0.18, zorder=0)
    ax1.text(dt.date(2025, 5, 1), 7.25, "Metaculus bin range 7.0–12.0 bn (both bounds open)",
             fontsize=8, color="#48707f")

    ax1.set_ylabel("headline (Shr)Impact, bn shrimp/yr")
    ax1.set_title("SWP Humane Slaughter Initiative: committed shrimp per year\n"
                  "(small numbers = signed agreements)", fontsize=11, color=INK)
    ax1.set_ylim(0, 13)
    ax1.grid(alpha=0.25, ls=":")
    ax1.legend(fontsize=8.5, loc="lower right")

    # --- panel 2: horizontal probability bands ---------------------------
    edges = [0, 6.95, 7.55, 8.05, 8.55, 9.05, 10.05, 12.05, np.inf]
    labels = ["< 7.0  (below range)", "7.0 – 7.5", "7.5 – 8.0", "8.0 – 8.5",
              "8.5 – 9.0", "9.0 – 10.0", "10.0 – 12.0", "> 12.0  (above range)"]
    probs = [float(np.mean((s >= lo) & (s < hi))) for lo, hi in itertools.pairwise(edges)]
    ypos = np.arange(len(labels))[::-1]
    bars = ax2.barh(ypos, probs, color=[ACC if 7.55 <= e < 9.05 else INK for e in edges[1:-1]] + [INK],
                    alpha=0.85, height=0.62)
    for b, p in zip(bars, probs):
        ax2.text(b.get_width() + 0.004, b.get_y() + b.get_height() / 2,
                 f"{p * 100:.1f}%", va="center", fontsize=8.5, color=INK)
    ax2.set_yticks(ypos, labels, fontsize=9)
    ax2.set_xlabel("probability")
    ax2.set_xlim(0, max(probs) * 1.22)
    ax2.set_title("Where the 2027-07-01 headline lands (orange = the IQR core)",
                  fontsize=10.5, color=INK)
    ax2.grid(axis="x", alpha=0.25, ls=":")
    for sp in ("top", "right"):
        ax2.spines[sp].set_visible(False)
        ax1.spines[sp].set_visible(False)

    fig.tight_layout()
    out = Path(__file__).resolve().parent / "shrimpact-trajectory-and-bands.png"
    fig.savefig(out, dpi=160)
    print("wrote", out)


if __name__ == "__main__":
    main()
