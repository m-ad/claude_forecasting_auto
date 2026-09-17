"""Two-panel figure for Metaculus #43277.

Top: measured "Reporting Fulfilled" share by deadline-year cohort on Chicken
Watch (2026-09-17). It is the whole argument in one picture -- reporting happens
*after* a deadline passes, and the 2025 mega-cohort broke the pattern the small
2020-2024 cohorts set.

Bottom: what the resolution value becomes under each load-bearing assumption
about the 2026 cohort.

Every bar is direct-labelled: the orange fill sits below 3:1 against the surface,
so identity and value must not rest on the fill alone.
"""

from __future__ import annotations

import sys
from pathlib import Path as FsPath

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(FsPath(__file__).resolve().parents[1] / "scripts"))
import model

OUT = FsPath(__file__).resolve().parent / "cohort-fulfilment-and-scenarios.png"

PAST = "#2f6f9f"      # deadline already passed on 2026-09-17
FUTURE = "#d1892f"    # deadline still ahead
MINE = "#b03a48"      # my forecast
INK = "#2b2b2b"
MUTED = "#6b6b6b"

# (deadline year, n, % Reporting Fulfilled) -- measured from the Chicken Watch export.
COHORTS = [
    (2020, 187, 89.8), (2021, 132, 97.0), (2022, 120, 82.5), (2023, 103, 77.7),
    (2024, 138, 92.0), (2025, 1098, 33.6), (2026, 120, 5.0), (2027, 51, 2.0),
    (2028, 64, 4.7), (2030, 69, 2.9),
]


def main() -> None:
    """Render the figure to charts/cohort-fulfilment-and-scenarios.png."""
    fig, (ax_top, ax_bot) = plt.subplots(
        2, 1, figsize=(9.2, 8.2), gridspec_kw={"height_ratios": [5, 3], "hspace": 0.42}
    )
    fig.patch.set_facecolor("#fcfcfb")

    # ---- top panel: fulfilment by cohort -------------------------------- #
    labels = [f"{y}  (n={n:,})" for y, n, _ in COHORTS]
    vals = [v for _, _, v in COHORTS]
    colors = [PAST if y <= 2025 else FUTURE for y, _, _ in COHORTS]
    ypos = np.arange(len(COHORTS))

    ax_top.barh(ypos, vals, color=colors, height=0.66)
    ax_top.set_yticks(ypos)
    ax_top.set_yticklabels(labels, fontsize=9)
    ax_top.invert_yaxis()
    ax_top.set_xlim(0, 108)
    ax_top.set_xlabel('share marked "Reporting Fulfilled" on Chicken Watch, %', fontsize=9)
    ax_top.set_title(
        "Cage-free fulfilment reporting happens after the deadline, not before\n"
        "Chicken Watch, commitments won 1990–2025, measured 2026-09-17",
        fontsize=11, color=INK, loc="left",
    )
    for y, v in zip(ypos, vals):
        ax_top.text(v + 1.4, y, f"{v:.1f}%", va="center", fontsize=9, color=INK)
    ax_top.grid(axis="x", alpha=0.25, linewidth=0.8)
    ax_top.set_axisbelow(True)
    for side in ("top", "right"):
        ax_top.spines[side].set_visible(False)

    ax_top.annotate(
        "the 2025 mega-cohort broke the pattern:\n8× the size, one third the fulfilment",
        xy=(34.5, 5.30), xytext=(44, 5.95), fontsize=8.5, color=MUTED,
        arrowprops={"arrowstyle": "->", "color": MUTED, "linewidth": 0.9},
    )
    ax_top.annotate(
        "the question's numerator lives\nentirely in these four rows",
        xy=(7.5, 7.5), xytext=(30, 8.35), fontsize=8.5, color=MUTED,
        arrowprops={"arrowstyle": "->", "color": MUTED, "linewidth": 0.9},
    )
    ax_top.legend(
        handles=[
            plt.Rectangle((0, 0), 1, 1, color=PAST),
            plt.Rectangle((0, 0), 1, 1, color=FUTURE),
        ],
        labels=["deadline passed by 2026-09-17", "deadline still ahead"],
        fontsize=8.5, loc="lower right", frameon=False,
    )

    # ---- bottom panel: scenarios ---------------------------------------- #
    base = model.COHORTS[0][3]
    rows = []
    for label, gain in [
        ("2026 cohort stalls (+7pp)\nChick-fil-A / HPAI case", 0.070),
        ("Central: +17.5pp,\nthe 2025 cohort's own post-deadline rate", base),
        ("2026 cohort matches the 2025\ncohort's full first-year gain (+28pp)", 0.280),
    ]:
        model.COHORTS[0] = ("timeline 2026", 120, 6, gain)
        rows.append((label, float(np.percentile(model.simulate(120_000), 50))))
    model.COHORTS[0] = ("timeline 2026", 120, 6, base)

    rows.append(("Fast-sweep regime\n(2026 behaves like the 2024 cohort)", 34.0))
    names = [r[0] for r in rows]
    vs = [r[1] for r in rows]
    ypos2 = np.arange(len(rows))
    ax_bot.barh(ypos2, vs, color=[MINE if i == 1 else PAST for i in range(len(rows))], height=0.6)
    ax_bot.set_yticks(ypos2)
    ax_bot.set_yticklabels(names, fontsize=8.5)
    ax_bot.invert_yaxis()
    ax_bot.set_xlim(0, 40)
    ax_bot.set_xlabel("resolution value on 2028-01-01, %", fontsize=9)
    ax_bot.set_title("What the assumption about the 2026 cohort is worth", fontsize=10.5,
                     color=INK, loc="left")
    for y, v in zip(ypos2, vs):
        ax_bot.text(v + 0.5, y, f"{v:.1f}%", va="center", fontsize=9, color=INK)
    ax_bot.set_ylim(3.62, -0.92)
    ax_bot.axvline(3.68, color=MUTED, linestyle="--", linewidth=1.1)
    ax_bot.text(4.1, -0.72, "today: 3.7%", fontsize=8.5, color=MUTED, va="center")
    ax_bot.grid(axis="x", alpha=0.25, linewidth=0.8)
    ax_bot.set_axisbelow(True)
    for side in ("top", "right"):
        ax_bot.spines[side].set_visible(False)

    fig.subplots_adjust(left=0.30, right=0.97, top=0.92, bottom=0.08)
    fig.savefig(OUT, dpi=170, facecolor=fig.get_facecolor())
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
