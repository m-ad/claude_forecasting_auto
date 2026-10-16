"""v3 (2026-10-16) numbers for Metaculus #45515: remaining-window distribution with the realised floor.

Run from the repo root: ``uv run questions/<slug>/analysis/update_2026_10_02.py``.
Reads only the 2026-10-16 snapshots in ``raw/``.
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
SNAP = "2026-10-16"
REMAIN = 49  # sessions left: Oct 16 .. Dec 24 (Thanksgiving excluded)
FLOOR = 18.01  # realised Oct 15 high (Cboe CSV and Yahoo 5-minute bars agree)


def load(series: str, col: str) -> dict[dt.date, float]:
    """Load one column of a Cboe daily-history CSV keyed by date.

    Parameters
    ----------
    series : str
        Cboe index name, e.g. ``"VIX"``.
    col : str
        Column name, e.g. ``"HIGH"``.

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


def rolling(cond: Callable[[dt.date], bool], label: str) -> np.ndarray:
    """Forward ``REMAIN``-session max HIGH (from the next session) floored at ``FLOOR``.

    Parameters
    ----------
    cond : Callable[[datetime.date], bool]
        Predicate selecting start days (the start day's close is the conditioning value).
    label : str
        Printed label.

    Returns
    -------
    numpy.ndarray
        Floored window maxima.
    """
    starts = [i for i, d in enumerate(DATES[: -REMAIN - 1]) if cond(d)]
    r = np.maximum(FLOOR, np.array([H[i + 1 : i + 1 + REMAIN].max() for i in starts]))
    episodes = 1 + sum(1 for a, b in itertools.pairwise(starts) if b - a > 40)
    pct = np.percentile(r, [5, 10, 25, 50, 75, 90, 95]).round(2)
    tails = {k: round(float((r > k).mean()), 3) for k in (20, 25, 30, 40)}
    print(f"{label}: n={len(r)} episodes~{episodes} p5..p95={pct} P(>k)={tails}")
    return r


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


def calm(lo: float, hi: float) -> Callable[[dt.date], bool]:
    """Predicate: the day's VIX close lies in [lo, hi]."""
    return lambda d: lo <= CLOSE[d] <= hi


if __name__ == "__main__":
    rolling(lambda d: d >= dt.date(1992, 1, 1) and calm(15.0, 18.0)(d), "start 15-18, 1992+")
    rolling(lambda d: d >= dt.date(2004, 1, 1) and calm(15.0, 18.0)(d), "start 15-18, 2004+")
    rolling(
        lambda d: d in VIX3M and calm(15.0, 18.0)(d) and 17.5 <= VIX3M[d] <= 19.5,
        "start 15-18 and VIX3M 17.5-19.5",
    )
    option_forwards()
