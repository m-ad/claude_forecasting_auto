"""Charts for the mc45467 weight-exfiltration forecast.

Two panels, because the central claim of the forecast is a claim about *why* the
Metaculus cohorts moved, and that claim is only legible against the trajectory:

1. Left: where each forecaster sits today (horizontal bars, per AGENTS.md §7).
2. Right: the three cohort trajectories since the community prediction was revealed,
   annotated with the two candidate causes of the 2026-09-10..13 drift.
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.dates as mdates
import matplotlib.pyplot as plt

QDIR = Path(__file__).resolve().parent.parent
RAW = QDIR / "raw" / "metaculus-2026-09-13.json"
OUT = QDIR / "charts"

INK = "#1b1b1b"
MINE = "#b5451a"
GREY = "#8a8a8a"
COHORT_COLOURS = {
    "recency_weighted": "#2f6f9f",
    "gold_medalists": "#c99700",
    "metaculus_pros": "#6b4c9a",
}
COHORT_LABELS = {
    "recency_weighted": "Community (CP)",
    "gold_medalists": "Gold medalists",
    "metaculus_pros": "Metaculus Pro",
}


def _history(data: dict, method: str) -> tuple[list[datetime], list[float]]:
    """Return (timestamps, probabilities in %) for one aggregation method.

    Parameters
    ----------
    data : dict
        Parsed output of ``metaculus_aggregations.py --json``.
    method : str
        One of ``recency_weighted``, ``metaculus_pros``, ``gold_medalists``.

    Returns
    -------
    tuple of (list of datetime, list of float)
        UTC-aware timestamps and centre values expressed in percent.
        Metaculus reports aggregation ``as_of`` stamps in UTC.
    """
    points = data["methods"][method]["history"]
    xs = [
        datetime.strptime(p[0], "%Y-%m-%d %H:%M").replace(tzinfo=timezone.utc)
        for p in points
    ]
    ys = [p[1] * 100 for p in points]
    return xs, ys


def main() -> None:
    """Render ``charts/cohorts-and-trajectory.png``."""
    data = json.loads(RAW.read_text())
    OUT.mkdir(exist_ok=True)

    fig, (ax_bar, ax_traj) = plt.subplots(
        1, 2, figsize=(12.4, 4.5), gridspec_kw={"width_ratios": [1, 1.45]}
    )

    # --- panel 1: horizontal bars -------------------------------------------------
    rows = [
        ("This forecast (v1)", 3.5, (2.5, 6.5), MINE),
        ("Community CP (n=19)", 7.0, (3.0, 20.0), COHORT_COLOURS["recency_weighted"]),
        ("Gold medalists (n=12)", 10.0, (3.0, 20.0), COHORT_COLOURS["gold_medalists"]),
        ("Metaculus Pro (n=5)", 30.0, (30.0, 30.0), COHORT_COLOURS["metaculus_pros"]),
        ("CP before 2026-09-11", 3.0, None, GREY),
    ]
    ypos = list(range(len(rows)))[::-1]
    for y, (label, centre, iqr, colour) in zip(ypos, rows):
        ax_bar.barh(y, centre, height=0.56, color=colour, alpha=0.88)
        if iqr and iqr[0] != iqr[1]:
            ax_bar.plot(iqr, [y, y], color=INK, lw=1.3, alpha=0.75)
            for xb in iqr:
                ax_bar.plot([xb, xb], [y - 0.16, y + 0.16], color=INK, lw=1.3, alpha=0.75)
        anchor = max(centre, iqr[1] if iqr else centre)
        ax_bar.text(anchor + 1.0, y, f"{centre:.1f}%", va="center", fontsize=9.5, color=INK)
        _ = label
    ax_bar.set_yticks(ypos)
    ax_bar.set_yticklabels([r[0] for r in rows], fontsize=9.5)
    ax_bar.set_xlim(0, 38)
    ax_bar.set_xlabel("P(confirmed before 2027) — %", fontsize=9.5)
    ax_bar.set_title("Where everyone sits, 2026-09-13\n(bars = median, whiskers = IQR)",
                     fontsize=10.5, loc="left")
    ax_bar.grid(axis="x", alpha=0.22)
    ax_bar.set_axisbelow(True)
    for spine in ("top", "right"):
        ax_bar.spines[spine].set_visible(False)

    # --- panel 2: trajectories ----------------------------------------------------
    for method in ("recency_weighted", "gold_medalists", "metaculus_pros"):
        xs, ys = _history(data, method)
        ax_traj.plot(xs, ys, lw=1.8, color=COHORT_COLOURS[method],
                     label=COHORT_LABELS[method])

    ax_traj.axhline(3.5, color=MINE, lw=1.6, ls="--", label="This forecast (3.5%)")

    senate = datetime(2026, 9, 10, 16, 55, tzinfo=timezone.utc)
    ax_traj.annotate(
        "Sep 10: Hawley/Blumenthal probes\nreported (no weights question)",
        xy=(senate, 15), xytext=(datetime(2026, 9, 4, 16, 0, tzinfo=timezone.utc), 24.0),
        fontsize=8.2, color=GREY,
        arrowprops={"arrowstyle": "->", "color": GREY, "lw": 0.9},
    )
    lw_post = datetime(2026, 9, 12, 21, 33, tzinfo=timezone.utc)
    ax_traj.annotate(
        "Sep 11-12: RubyGems scoop (external\ntargets) + LessWrong roundup quoting\n"
        '"12%" — the CP *mean*, not its median',
        xy=(lw_post, 9.6), xytext=(datetime(2026, 9, 4, 16, 0, tzinfo=timezone.utc), 34.5),
        fontsize=8.2, color=INK,
        arrowprops={"arrowstyle": "->", "color": INK, "lw": 0.9},
    )

    ax_traj.set_ylim(0, 39)
    ax_traj.set_ylabel("P(YES) — %", fontsize=9.5)
    ax_traj.set_title(
        "No weights-relevant news landed in the window the cohorts moved",
        fontsize=10.5, loc="left",
    )
    ax_traj.xaxis.set_major_formatter(mdates.DateFormatter("%b %d"))
    ax_traj.xaxis.set_major_locator(mdates.DayLocator(interval=2))
    ax_traj.grid(alpha=0.22)
    ax_traj.set_axisbelow(True)
    ax_traj.legend(fontsize=8.2, ncol=4, loc="lower center",
                   bbox_to_anchor=(0.5, -0.30), frameon=False)
    for spine in ("top", "right"):
        ax_traj.spines[spine].set_visible(False)

    fig.tight_layout()
    fig.savefig(OUT / "cohorts-and-trajectory.png", dpi=155)
    print("wrote", OUT / "cohorts-and-trajectory.png")


if __name__ == "__main__":
    main()
