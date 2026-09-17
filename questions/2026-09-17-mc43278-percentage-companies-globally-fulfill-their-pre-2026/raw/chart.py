"""Figure for Metaculus 43278: reference-class rates (left) and scenario weights (right).

Horizontal bars throughout. Run from anywhere; the output path is resolved from this file.
"""

from __future__ import annotations

import pathlib

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = pathlib.Path(__file__).resolve().parent.parent / "charts" / "base-rates-and-scenarios.png"

# Chicken Watch's own "Reporting Fulfilled" share, forward-looking pledges only, 2026-09-17.
CLASSES = [
    ("Cage-free, Europe, deadline passed\n(275/613)", 44.86, "ref"),
    ("Cage-free, global, deadline passed\n(488/1285)", 37.98, "ref"),
    ("Broiler, Europe, deadline passed\n(2/21)", 9.52, "ref"),
    ("Broiler, global, deadline passed\n(7/226)", 3.10, "ref"),
    ("Broiler, North America, deadline passed\n(5/205)", 2.44, "ref"),
    ("THIS QUESTION today (4/405)", 0.99, "now"),
]
SCENARIOS = [
    ("S5 mass reclassification\nF 66-140", 3),
    ("S4 strong catch-up\nF 36-66", 9),
    ("S3 deadline-driven update pass\nF 19-36", 22),
    ("S2 slow drip / normal cycle\nF 10-19", 34),
    ("S1 tracker stasis\nF 5-10", 28),
    ("S0 rows removed / regression\nF 3-5", 4),
]
MEDIAN, LOWER, UPPER = 3.75, 2.26, 6.56
COLOUR = {"ref": "#8c9bab", "now": "#c0392b", "forecast": "#1f6f4a"}


def main() -> None:
    fig, (ax1, ax2) = plt.subplots(
        1, 2, figsize=(13.5, 5.4), gridspec_kw={"width_ratios": [1.45, 1]}
    )

    labels = [c[0] for c in CLASSES] + ["FORECAST v1 median\n(IQR whisker)"]
    values = [c[1] for c in CLASSES] + [MEDIAN]
    colours = [COLOUR[c[2]] for c in CLASSES] + [COLOUR["forecast"]]
    ax1.barh(range(len(labels)), values, color=colours, height=0.62)
    ax1.errorbar(
        [MEDIAN],
        [len(labels) - 1],
        xerr=[[MEDIAN - LOWER], [UPPER - MEDIAN]],
        fmt="none",
        ecolor="#112233",
        capsize=5,
        lw=1.8,
    )
    for i, v in enumerate(values):
        # the forecast bar carries an IQR whisker, so its label sits clear of the upper cap
        x = UPPER + 1.2 if i == len(values) - 1 else v + 0.7
        ax1.text(x, i, f"{v:.1f}%", va="center", fontsize=9)
    ax1.set_yticks(range(len(labels)))
    ax1.set_yticklabels(labels, fontsize=8.5)
    ax1.invert_yaxis()
    ax1.set_xlim(0, 52)
    ax1.set_xlabel(
        'share of forward-looking commitments marked "Reporting Fulfilled" (%)', fontsize=9
    )
    ax1.set_title(
        "Reference classes - Chicken Watch tracker, 2026-09-17\n"
        "(forward-looking pledges only: victory date < deadline)",
        fontsize=10.5,
        loc="left",
    )

    ax2.barh(range(len(SCENARIOS)), [s[1] for s in SCENARIOS], color="#3d6f9e", height=0.6)
    for i, (_, weight) in enumerate(SCENARIOS):
        ax2.text(weight + 0.5, i, f"{weight}%", va="center", fontsize=9)
    ax2.set_yticks(range(len(SCENARIOS)))
    ax2.set_yticklabels([s[0] for s in SCENARIOS], fontsize=8.5)
    ax2.set_xlim(0, 42)
    ax2.set_xlabel("scenario weight (%)", fontsize=9)
    ax2.set_title(
        "Scenario weights on the fulfilled count F\n(denominator ~400 on 2028-01-01)",
        fontsize=10.5,
        loc="left",
    )

    for ax in (ax1, ax2):
        ax.grid(axis="x", alpha=0.25)
        ax.set_axisbelow(True)
    fig.tight_layout()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT, dpi=150)
    print("wrote", OUT)


if __name__ == "__main__":
    main()
