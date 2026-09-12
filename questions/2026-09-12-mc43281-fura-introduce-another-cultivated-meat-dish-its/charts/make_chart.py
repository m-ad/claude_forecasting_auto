"""Horizontal bar chart of each path's contribution to P(YES), plus the comparison anchors."""

from __future__ import annotations

import sys
from pathlib import Path as FsPath

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, str(FsPath(__file__).resolve().parents[1] / "scripts"))
from model import P_CLOSURE, PATHS, p_yes

OUT = FsPath(__file__).resolve().parent / "path-decomposition.png"


def main() -> None:
    labels = [
        "Parima (duck/foie gras, chicken)\nlive in SG by 2027-03-31",
        "Parima live 2027-04 to mid-06\n(little runway left)",
        "Aleph Farms beef\nlive before mid-2027",
        "Other (Eat Just return, Hoxton\ncultivated fat, surprise approval)",
    ]
    values = [path.p * 100 for path in PATHS]
    raw = p_yes(PATHS)
    mine = 100 * raw / (1.0 - P_CLOSURE * (1.0 - raw))

    fig, (ax_top, ax_bot) = plt.subplots(
        2, 1, figsize=(9, 6.4), gridspec_kw={"height_ratios": [3, 2]}
    )

    ypos = range(len(labels))
    ax_top.barh(list(ypos), values, color="#4c72b0", height=0.62)
    ax_top.set_yticks(list(ypos))
    ax_top.set_yticklabels(labels, fontsize=8.5)
    ax_top.invert_yaxis()
    ax_top.set_xlabel("contribution to P(YES), percentage points")
    ax_top.set_xlim(0, 30)
    ax_top.set_title(
        "Where P(YES) comes from: FURA adds a non-quail cultivated meat\nbefore 2027-07-01",
        fontsize=10.5,
    )
    for y, v in zip(ypos, values):
        ax_top.text(v + 0.4, y, f"{v:.1f}pp", va="center", fontsize=8.5)
    ax_top.grid(axis="x", alpha=0.3)

    anchors = [
        ("My forecast", mine, "#c44e52"),
        ("Metaculus gold medalists", 42.0, "#937860"),
        ("Metaculus CP", 42.0, "#8172b3"),
        ("Metaculus Pro", 40.0, "#55a868"),
    ]
    ax_bot.barh(
        [a[0] for a in anchors],
        [a[1] for a in anchors],
        color=[a[2] for a in anchors],
        height=0.6,
    )
    for i, (_, v, _c) in enumerate(anchors):
        ax_bot.text(v + 0.6, i, f"{v:.1f}%", va="center", fontsize=8.5)
    ax_bot.set_xlim(0, 60)
    ax_bot.set_xlabel("P(YES), % — all figures as of 2026-09-12")
    ax_bot.grid(axis="x", alpha=0.3)
    ax_bot.tick_params(labelsize=8.5)

    fig.tight_layout()
    fig.savefig(OUT, dpi=150)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
