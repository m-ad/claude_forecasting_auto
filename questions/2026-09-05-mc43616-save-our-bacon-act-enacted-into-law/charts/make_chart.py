"""Two-panel figure for the Save Our Bacon Act forecast (Metaculus #43616).

Left: Metaculus cohort trajectory with the two events that moved it.
Right: horizontal decomposition of the forecast by enactment path.
Horizontal bars are used per the repo's house style (AGENTS.md section 7).

Run from the repository root: ``uv run questions/<slug>/charts/make_chart.py``.
"""

from __future__ import annotations

import json
from datetime import date
from pathlib import Path

import matplotlib
import matplotlib.dates as mdates
import matplotlib.pyplot as plt

# Non-interactive backend: this script only ever writes a PNG. Setting it after
# the pyplot import is safe because no figure has been created yet.
matplotlib.use("Agg")

SLUG_DIR = Path(__file__).resolve().parent.parent
SNAPSHOT = SLUG_DIR / "raw" / "metaculus-2026-09-05.json"

with SNAPSHOT.open(encoding="utf-8") as fh:
    data = json.load(fh)


def series(method: str) -> tuple[list[date], list[float]]:
    """Extract a (dates, percentages) pair from one aggregation cohort.

    Parameters
    ----------
    method : str
        Aggregation key in the snapshot, e.g. ``"recency_weighted"``.

    Returns
    -------
    tuple of (list of datetime.date, list of float)
        Calendar dates and the cohort's central probability in percent.

    Notes
    -----
    History points carry a ``"YYYY-MM-DD HH:MM"`` timestamp, but the axis spans
    three months, so the intraday part is dropped and plain dates are used.
    """
    points = [p for p in data["methods"][method]["history"] if p[1] is not None]
    return (
        [date.fromisoformat(ts[:10]) for ts, _ in points],
        [value * 100 for _, value in points],
    )


fig, (ax0, ax1) = plt.subplots(
    1, 2, figsize=(13.5, 5.2), gridspec_kw={"width_ratios": [1.45, 1]}
)

cohorts = [
    ("recency_weighted", "Community (recency-weighted)", "#4C72B0", 2.0),
    ("gold_medalists", "Gold medalists", "#C8A415", 1.6),
    ("metaculus_pros", "Metaculus Pros", "#55A868", 1.6),
]
for method, label, colour, width in cohorts:
    xs, ys = series(method)
    ax0.plot(xs, ys, label=label, color=colour, lw=width)

# The two step-downs the community priced in. Both are Senate exclusions of the
# language, not new arguments about the underlying policy.
events = [
    (date(2026, 6, 23), "Senate draft\nomits SOB"),
    (date(2026, 8, 6), "Senate Ag markup\nfails 10-11"),
]
for when, label in events:
    ax0.axvline(when, color="#888888", ls="--", lw=1)
    ax0.annotate(
        label,
        xy=(when, 34),
        xytext=(6, 0),
        textcoords="offset points",
        fontsize=8.5,
        color="#555555",
        va="top",
    )

ax0.axhline(3.0, color="#C44E52", lw=1.8, ls=":")
ax0.annotate(
    "my forecast 3.0%",
    xy=(date(2026, 7, 5), 3.0),
    xytext=(0, 6),
    textcoords="offset points",
    fontsize=9,
    color="#C44E52",
    weight="bold",
)

ax0.set_ylim(0, 44)
ax0.set_ylabel("P(enacted before 2027-07-01), %")
ax0.set_title("Metaculus cohorts, 2026-06-12 to 2026-09-04", fontsize=11, loc="left")
ax0.xaxis.set_major_formatter(mdates.DateFormatter("%b %d"))
ax0.legend(fontsize=9, frameon=False)
ax0.grid(axis="y", alpha=0.25)
for side in ("top", "right"):
    ax0.spines[side].set_visible(False)

paths = [
    ("Model error / unknown unknowns", 0.4, "#BBBBBB"),
    ("Reconciliation (Byrd rule)", 0.3, "#8172B2"),
    ("120th Congress, Jan-Jun 2027", 0.5, "#937860"),
    ("Dec-2026 approps / NDAA rider", 0.8, "#DD8452"),
    ("Farm bill in 119th, clean text", 0.9, "#4C72B0"),
]
bars = ax1.barh(
    [name for name, _, _ in paths],
    [value for _, value, _ in paths],
    color=[colour for _, _, colour in paths],
    height=0.6,
)
for bar, (_, value, _) in zip(bars, paths):
    ax1.text(
        value + 0.03,
        bar.get_y() + bar.get_height() / 2,
        f"{value:.1f} pp",
        va="center",
        fontsize=9.5,
    )

ax1.set_xlim(0, 1.35)
ax1.set_xlabel("contribution to P(YES), percentage points")
ax1.set_title("Where the 3.0% comes from", fontsize=11, loc="left")
ax1.grid(axis="x", alpha=0.25)
for side in ("top", "right"):
    ax1.spines[side].set_visible(False)

fig.suptitle(
    "Save Our Bacon Act enacted before July 2027 - Metaculus #43616",
    fontsize=13,
    x=0.01,
    ha="left",
    weight="bold",
)
fig.tight_layout(rect=(0, 0, 1, 0.95))
OUT = SLUG_DIR / "charts" / "decomposition.png"
fig.savefig(OUT, dpi=150)
print(f"wrote {OUT}")
