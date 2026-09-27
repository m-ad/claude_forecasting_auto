"""Pool the v2 model with the Metaculus Pro + gold-medalist CDFs (linear opinion pool).

The v2 forecast is ``(1 - W) * model + W * crowd`` on the CDF scale, with the crowd CDF
the unweighted mean of the Pro and gold-medalist aggregations snapshotted on
2026-09-27. ``W`` is 0.3: the cohorts are tiny (2 and 4 forecasters), and their history
shows them still absorbing the $1bn base-year fact (Pros fell from +151% to +37% on the
2027 leg within ~36 hours of it being posted in the comments), but they carry better
track records than one model and deserve real weight.

Metaculus only reports the CDF inside the 0-200 range plus the mass outside it, so the
tails are extended linearly to -60 and to +450. That assumption touches only the
outer percentiles, not the median or the IQR reported in forecast.md.
"""

from __future__ import annotations

import json
import runpy
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
RAW = HERE.parent / "raw" / "metaculus-2026-09-27.json"
W = 0.3
PCTS = (5, 10, 25, 50, 75, 90, 95)


def crowd_cdf(snapshot: dict, qid: str, x: np.ndarray) -> np.ndarray:
    """Mean Pro + gold CDF for one subquestion, evaluated at ``x``.

    Parameters
    ----------
    snapshot : dict
        Parsed ``raw/metaculus-2026-09-27.json``.
    qid : str
        Metaculus question id of the subquestion.
    x : ndarray
        Points on the resolution scale (percent change).

    Returns
    -------
    ndarray
        CDF values in [0, 1].
    """
    grid = np.linspace(0, 200, 201)
    fvs = [
        np.asarray(snapshot["subquestions"][qid]["methods"][m]["forecast_values"])
        for m in ("metaculus_pros", "gold_medalists")
    ]
    fv = np.mean(fvs, axis=0)
    out = np.interp(x, grid, fv)
    below, above = x < 0, x > 200
    out[below] = fv[0] * np.clip((x[below] + 60) / 60, 0, 1)
    out[above] = fv[-1] + (1 - fv[-1]) * np.clip((x[above] - 200) / 250, 0, 1)
    return out


def pooled_percentiles(
    samples: np.ndarray, snapshot: dict, qid: str, w: float = W
) -> dict[int, float]:
    """Percentiles of the linear pool of model samples and the crowd CDF.

    Parameters
    ----------
    samples : ndarray
        Model Monte-Carlo draws on the resolution scale.
    snapshot : dict
        Parsed Metaculus snapshot.
    qid : str
        Subquestion id.
    w : float
        Weight on the crowd.

    Returns
    -------
    dict of int to float
        Percentile -> value, plus key ``0`` holding P(change < 0).
    """
    xs = np.linspace(-80, 600, 68001)
    srt = np.sort(samples)
    f = (1 - w) * np.searchsorted(srt, xs, side="right") / len(srt)
    f += w * crowd_cdf(snapshot, qid, xs.copy())
    out = {p: float(xs[np.searchsorted(f, p / 100)]) for p in PCTS}
    out[0] = float(f[np.searchsorted(xs, 0.0)])
    return out


if __name__ == "__main__":
    ns = runpy.run_path(str(HERE / "model_v2.py"), run_name="model_v2")
    snap = json.loads(RAW.read_text(encoding="utf-8"))
    for label, qid, arr in [("2027", "45575", ns["pct27"]), ("2028", "45576", ns["pct28"])]:
        q = pooled_percentiles(arr, snap, qid)
        body = "  ".join(f"p{p}={q[p]:+.1f}" for p in PCTS)
        print(f"{label}: {body}  P(<0)={q[0]:.3f}")
