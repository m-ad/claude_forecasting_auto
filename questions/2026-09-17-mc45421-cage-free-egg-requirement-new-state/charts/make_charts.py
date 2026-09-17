"""Charts for the 'additional US state cage-free requirement' forecast.

Two horizontal-bar panels, because the whole forecast turns on one visual claim:
the 2016-2021 adoption wave stopped dead, and the scenario weights follow from
believing that the stop is a regime break rather than noise.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

# First-time adoption of a genuine cage-free requirement (cage ban for in-state
# hens, or sale ban on non-cage-free eggs). Dates follow AWI's anti-confinement
# tracker and the ASPCA confinement-ban table; earlier "enriched cage" space laws
# (CA 2008, MI 2009, OR 2011, WA 2011) are excluded because they permitted cages.
ADOPTIONS: dict[int, list[str]] = {
    2016: ["MA"],
    2017: [],
    2018: ["CA", "RI"],
    2019: ["MI", "OR", "WA", "AZ"],
    2020: ["CO"],
    2021: ["NV", "UT"],
    2022: [],
    2023: [],
    2024: [],
    2025: [],
    2026: [],
}

SCENARIOS: list[tuple[str, float, str]] = [
    ("1. Status quo: bills die in committee", 0.72, "no"),
    ("2. Defensive year: rollback pressure only", 0.16, "no"),
    ("3. Blue state passes as anti-preemption move", 0.08, "yes"),
    ("4. Negotiated deal or agency rulemaking", 0.025, "yes"),
    ("5. Resolver counts an edge case", 0.015, "yes"),
]

NO_COLOR = "#8c8c8c"
YES_COLOR = "#c2410c"
WAVE_COLOR = "#0f766e"


def build(out_path: Path) -> None:
    """Render both panels into a single PNG.

    Parameters
    ----------
    out_path : Path
        Destination file; parent directory must exist.
    """
    fig, (ax_hist, ax_scen) = plt.subplots(
        2, 1, figsize=(9, 8), gridspec_kw={"height_ratios": [1.25, 1]}
    )

    years = sorted(ADOPTIONS)
    counts = [len(ADOPTIONS[y]) for y in years]
    colors = [WAVE_COLOR if c else "#d4d4d4" for c in counts]
    ax_hist.barh([str(y) for y in years], counts, color=colors)
    ax_hist.invert_yaxis()
    ax_hist.set_xlabel("states adopting a first cage-free requirement")
    ax_hist.set_title(
        "The adoption wave stopped in 2021: five straight years at zero",
        loc="left",
        fontsize=11,
        weight="bold",
    )
    ax_hist.set_xlim(0, 4.6)
    for y, c in zip(years, counts):
        label = ", ".join(ADOPTIONS[y]) if c else "none"
        ax_hist.text(c + 0.1, str(y), label, va="center", fontsize=8.5, color="#404040")
    ax_hist.spines[["top", "right"]].set_visible(False)

    labels = [s[0] for s in SCENARIOS][::-1]
    weights = [s[1] for s in SCENARIOS][::-1]
    scen_colors = [YES_COLOR if s[2] == "yes" else NO_COLOR for s in SCENARIOS][::-1]
    ax_scen.barh(labels, weights, color=scen_colors)
    ax_scen.set_xlabel("weight")
    ax_scen.set_xlim(0, 0.8)
    ax_scen.set_title(
        "Scenario weights — orange resolves YES (sums to 12.0%)",
        loc="left",
        fontsize=11,
        weight="bold",
    )
    for lbl, w in zip(labels, weights):
        ax_scen.text(w + 0.008, lbl, f"{w:.1%}", va="center", fontsize=9)
    ax_scen.spines[["top", "right"]].set_visible(False)
    ax_scen.tick_params(axis="y", labelsize=8.5)

    fig.tight_layout()
    fig.savefig(out_path, dpi=150, bbox_inches="tight")


if __name__ == "__main__":
    build(Path(__file__).with_name("overview.png"))
