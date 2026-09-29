"""Reproduce the v1 outside-view numbers for Metaculus #45515 (Q4 2026 VIX intraday peak).

Run from the repo root: ``uv run questions/<slug>/analysis/base_rates.py``.
Reads only the dated Cboe snapshots in ``raw/`` so the numbers stay reproducible.
"""

import collections
import csv
import datetime as dt
import itertools
import json
import re
from collections.abc import Callable
from pathlib import Path

import numpy as np

RAW = Path(__file__).resolve().parent.parent / "raw"
SNAP = "2026-09-28"
WINDOW = 59  # regular sessions from 2026-10-01 to 2026-12-24
SKIP = 3  # sessions between the last close (Sep 25) and the window start (Sep 28-30)


def load(series: str, col: str) -> dict[dt.date, float]:
    """Load one column of a Cboe daily-history CSV keyed by date.

    Parameters
    ----------
    series : str
        Cboe index name, e.g. ``"VIX"`` or ``"VIX3M"``.
    col : str
        Column to read, e.g. ``"HIGH"`` or ``"CLOSE"``.

    Returns
    -------
    dict[datetime.date, float]
        Date to value.
    """
    with open(RAW / f"{series}_History-{SNAP}.csv") as fh:
        return {
            dt.date(int(r["DATE"][6:]), int(r["DATE"][:2]), int(r["DATE"][3:5])): float(r[col])
            for r in csv.DictReader(fh)
        }


HIGH, CLOSE, VIX3M = load("VIX", "HIGH"), load("VIX", "CLOSE"), load("VIX3M", "CLOSE")
DATES = sorted(HIGH)
H = np.array([HIGH[d] for d in DATES])
C = np.array([CLOSE[d] for d in DATES])


def q4_table() -> None:
    """Print Oct 1-Dec 24 max HIGH per year against the last September close."""
    ratios = []
    for y in range(1990, 2026):
        sep = [d for d in DATES if dt.date(y, 9, 1) <= d <= dt.date(y, 9, 28)]
        win = [d for d in DATES if dt.date(y, 10, 1) <= d <= dt.date(y, 12, 24)]
        mx = max(HIGH[d] for d in win)
        ratios.append(mx / CLOSE[sep[-1]])
        print(f"{y} last-Sep close {CLOSE[sep[-1]]:6.2f}  Q4 max HIGH {mx:6.2f}")
    print("ratio p10/25/50/75/90:", np.percentile(ratios, [10, 25, 50, 75, 90]).round(3))


def rolling(cond: Callable[[dt.date], bool], label: str) -> None:
    """Print the forward 59-session max-HIGH distribution over start days matching ``cond``.

    Parameters
    ----------
    cond : Callable[[datetime.date], bool]
        Predicate selecting start days.
    label : str
        Printed label.
    """
    starts = [i for i, d in enumerate(DATES[: -SKIP - WINDOW]) if cond(d)]
    r = np.array([H[i + SKIP + 1 : i + SKIP + 1 + WINDOW].max() for i in starts])
    # Overlapping windows inflate n; count separated episodes as a rough effective sample.
    episodes = 1 + sum(1 for a, b in itertools.pairwise(starts) if b - a > 40)
    pct = np.percentile(r, [5, 10, 25, 50, 75, 90, 95]).round(2)
    tails = {k: round(float((r > k).mean()), 3) for k in (20, 25, 30, 40)}
    print(f"{label}: n={len(r)} episodes~{episodes} p5..p95={pct} P(>k)={tails}")


def option_forwards() -> None:
    """Print VIX forwards (put-call parity) and call-spread digitals per option expiry."""
    with open(RAW / f"cboe-vix-options-{SNAP}.json") as fh:
        opts = json.load(fh)["data"]["options"]
    chain: dict[str, dict[float, dict[str, float]]] = collections.defaultdict(dict)
    for o in opts:
        m = re.match(r"VIXW?(\d{6})([CP])(\d{8})", o["option"])
        if m and o["ask"] > 0:
            chain[m.group(1)].setdefault(int(m.group(3)) / 1000, {})[m.group(2)] = (o["bid"] + o["ask"]) / 2
    for exp in sorted(e for e in chain if e.startswith("26")):
        ks = chain[exp]
        fw = sorted(k + v["C"] - v["P"] for k, v in ks.items() if "C" in v and "P" in v and 14 <= k <= 22)
        dig = {
            k: round((ks[k - 1]["C"] - ks[k + 1]["C"]) / 2, 3)
            for k in (20, 25, 30, 35)
            if "C" in ks.get(k - 1, {}) and "C" in ks.get(k + 1, {})
        }
        print(f"expiry 20{exp}: forward~{fw[len(fw) // 2]:.2f}  risk-neutral P(>k)={dig}")


if __name__ == "__main__":
    q4_table()
    calm = lambda lo, hi: lambda d: lo <= CLOSE[d] <= hi
    rolling(lambda d: d >= dt.date(1992, 1, 1) and calm(13.5, 16.5)(d), "start 13.5-16.5, 1992+")
    rolling(lambda d: d >= dt.date(2004, 1, 1) and calm(13.5, 16.5)(d), "start 13.5-16.5, 2004+")
    rolling(
        lambda d: d in VIX3M and calm(13.5, 16.5)(d) and 16.9 <= VIX3M[d] <= 18.9,
        "start 13.5-16.5 and VIX3M 16.9-18.9",
    )
    option_forwards()
