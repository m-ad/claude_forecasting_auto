"""Compare the submitter's linear-knot density with a PCHIP interior for logged questions.

Run from the repository root:
    uv run --with matplotlib python plot_interp.py mc46176 mc46154 mc46161
"""
import glob
import json
import sys

import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import PchipInterpolator

sys.path.insert(0, "scripts")
import submit_metaculus as sm

OUT = "interp_compare.png"


def load(tag: str) -> tuple[str, dict, dict, float | None]:
    """Latest forecast percentiles, question scaling and outcome for a slug fragment."""
    with open("ledger/forecasts.jsonl", encoding="utf-8") as fh:
        led = [json.loads(line) for line in fh]
    fc = next(r for r in reversed(led) if r["event"] == "forecast" and tag in r["slug"])
    slug = fc["slug"]
    outcome = next((r["outcome"] for r in led
                    if r["event"] == "resolution" and r["slug"] == slug), None)
    # The snapshots are named with an ISO date, so the lexicographic minimum is the
    # earliest: the question text as it stood when the forecast was made.
    raw = min(glob.glob(f"questions/{slug}/raw/metaculus-question-*.json"))
    with open(raw, encoding="utf-8") as fh:
        scaling = json.load(fh)["question"]["scaling"]
    return slug, fc["distribution"]["percentiles"], scaling, outcome


def cdfs(pct: dict, scaling: dict) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Grid, current CDF, and CDF with a PCHIP interior (tails and floor unchanged)."""
    knots = sorted((float(k) / 100, float(v)) for k, v in pct.items())
    xs = np.array(sm._grid(scaling))
    lin = np.array(sm.continuous_cdf(knots, scaling))
    vs, ps = [v for _, v in knots], [p for p, _ in knots]
    if len(set(vs)) < len(vs):  # tied knots = point mass; PCHIP needs strictly increasing x
        return xs, lin, lin
    curve, orig = PchipInterpolator(vs, ps), sm.cdf_from_knots
    # monkeypatch the module global so continuous_cdf keeps its own tails, floor and caps
    sm.cdf_from_knots = lambda x, kn: float(curve(x)) if vs[0] <= x < vs[-1] else orig(x, kn)
    try:
        smooth = np.array(sm.continuous_cdf(knots, scaling))
    finally:
        sm.cdf_from_knots = orig
    return xs, lin, smooth


def main(tags: list[str]) -> None:
    fig, axes = plt.subplots(len(tags), 1, figsize=(9, 3.2 * len(tags)), squeeze=False)
    for ax, tag in zip(axes[:, 0], tags):
        slug, pct, scaling, outcome = load(tag)
        xs, lin, smooth = cdfs(pct, scaling)
        mid, w = (xs[1:] + xs[:-1]) / 2, np.diff(xs)
        ax.step(mid, np.diff(lin) / w, where="mid", label="current: linear between knots")
        ax.plot(mid, np.diff(smooth) / w, label="suggested: PCHIP interior")
        for v in pct.values():
            ax.axvline(float(v), color="grey", lw=0.5, ls=":")
        if isinstance(outcome, (int, float)):
            ax.axvline(outcome, color="black", lw=1.2, label=f"outcome {outcome:g}")
        ax.set_title(slug[11:70], fontsize=9)
        ax.set_ylabel("density per unit")
        ax.legend(fontsize=7)
    fig.tight_layout()
    fig.savefig(OUT, dpi=130)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main(sys.argv[1:] or ["mc46176", "mc46154", "mc46161"])
