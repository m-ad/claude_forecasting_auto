"""Charts for Metaculus 45427 (undirected AI breach of US PII before 2028).

Two horizontal-bar panels, because the operator reads bars faster than tables:
where this forecast sits against the three Metaculus cohorts, and how the 63%
median is built out of mutually exclusive scenarios.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = Path(__file__).resolve().parent.parent / "charts"

# (label, median, lower, upper) — cohort bands are Metaculus' 25th/75th percentiles.
FORECASTERS: list[tuple[str, float, float, float]] = [
    ("This forecast (v1)", 63.0, 54.0, 72.0),
    ("Metaculus gold (n=9)", 71.0, 55.0, 80.0),
    ("Metaculus CP (n=21)", 75.0, 55.0, 84.0),
    ("Metaculus Pro (n=4)", 78.0, 75.0, 90.0),
]

# (label, weight in pp, resolves YES?)
SCENARIOS: list[tuple[str, float, bool]] = [
    ("1. Lab eval agent → US company PII system,\n    lab discloses", 36.0, True),
    ("2. Deployed agent off-task → another\n    company's ≥100k PII", 15.0, True),
    ("3. Retro-confirmation of a 2026 incident\n    (HF / Anthropic's unnamed org)", 12.0, True),
    ("4. Happens, never positively attributed\n    (or reported after 2027-12-31)", 17.0, False),
    ("5. Containment + narrow targets hold;\n    big-PII cases stay human-directed", 20.0, False),
]

YES = "#1f6f4a"
NO = "#8c2f2f"
MINE = "#2b5d8a"
CROWD = "#9aa5b1"


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    fig, (ax1, ax2) = plt.subplots(
        2, 1, figsize=(9.5, 7.6), gridspec_kw={"height_ratios": [1, 1.35]}
    )

    labels = [f[0] for f in FORECASTERS]
    ys = range(len(FORECASTERS))
    for y, (_, med, lo, hi) in zip(ys, FORECASTERS):
        colour = MINE if y == 0 else CROWD
        ax1.barh(y, hi - lo, left=lo, height=0.30, color=colour, alpha=0.30)
        ax1.plot([med], [y], "D", color=colour, markersize=9, zorder=3)
        ax1.text(hi + 1.5, y, f"{med:.0f}%", va="center", fontsize=10, color=colour)
    ax1.set_yticks(list(ys), labels, fontsize=10)
    ax1.invert_yaxis()
    ax1.set_xlim(35, 100)
    ax1.set_xlabel("P(YES), %  — diamond = median, band = IQR / Metaculus quartiles")
    ax1.set_title(
        "Where this forecast sits (all values 2026-09-10)", fontsize=11, loc="left"
    )
    ax1.grid(axis="x", alpha=0.25)
    for side in ("top", "right", "left"):
        ax1.spines[side].set_visible(False)

    slabels = [s[0] for s in SCENARIOS]
    sys_ = range(len(SCENARIOS))
    for y, (_, w, yes) in zip(sys_, SCENARIOS):
        ax2.barh(y, w, height=0.55, color=YES if yes else NO, alpha=0.85)
        ax2.text(w + 0.6, y, f"{w:.0f}pp", va="center", fontsize=10)
    ax2.set_yticks(list(sys_), slabels, fontsize=9)
    ax2.invert_yaxis()
    ax2.set_xlim(0, 45)
    ax2.set_xlabel("Scenario weight, percentage points")
    ax2.set_title(
        "Scenario decomposition — green resolves YES (63pp), red NO (37pp)",
        fontsize=11,
        loc="left",
    )
    ax2.grid(axis="x", alpha=0.25)
    for side in ("top", "right", "left"):
        ax2.spines[side].set_visible(False)

    fig.tight_layout()
    fig.savefig(OUT / "forecast-vs-cohorts-and-scenarios.png", dpi=150)


if __name__ == "__main__":
    main()
