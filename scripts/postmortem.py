#!/usr/bin/env python3
"""Post-mortem tools: PIT, replay of distribution rules, sample selection, sync report.

Everything here reads what the bot already holds (ledger, ``meta.yaml``, the cached
question snapshot) and changes nothing. It is the deterministic half of the post-mortem
procedure in ``docs/postmortem.md``; the per-question analysis is done by subagents.

``pit``
    Where each resolved numeric/discrete/date outcome fell in the CDF the bot
    *submitted* (the probability integral transform, PIT). Calibrated forecasts give
    PITs spread evenly over [0, 1]: half inside the IQR, a tenth outside 5-95 %.
``replay``
    Rebuild every resolved submission from its ledger percentiles under alternative
    rules (interpolation, uniform floor) and report the change in log score at the
    outcome against what was actually submitted, in nats. With the other bots' forecasts
    fixed, the peer score moves by about 100 * c * delta (c is Metaculus' scaling for
    continuous questions, between 0.5 and 1). In-sample: judge a rule change on
    questions resolved *after* it, with ``--since``.
``sample``
    The worst N questions by official peer score plus N random positive-score controls,
    matched on question type (the strongest confounder: numeric questions scored far
    below binaries in the first round). Reproducible with ``--seed``.
``report``
    A markdown summary for the daily sync's run summary.

Examples
--------
    uv run scripts/postmortem.py pit
    uv run scripts/postmortem.py replay --detail
    uv run scripts/postmortem.py sample --worst 6 --controls 6 --seed 20261101
    uv run scripts/postmortem.py report --since 2026-11-02
"""

from __future__ import annotations

import argparse
import json
import math
import random
import statistics
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
import submit_metaculus as sm
from _common import LEDGER, QUESTIONS, ledger_records

CONTINUOUS_TYPES = {"numeric", "discrete", "date"}
DEFAULT_SEED = 20261101

# The rule sets the submitter has used, by name; every submitted CDF in the ledger must
# be reproduced by one of them (a test checks it), or a replay compares against noise.
RULE_SETS: dict[str, dict[str, Any]] = {
    "legacy: linear, floor 2 %": {"smooth": False, "mix": 0.02},  # until 2026-11-01
    "current": {},  # submit_metaculus defaults: PCHIP, UNIFORM_MIX
}
# What ``replay`` compares against the submission. Keep the legacy and current entries:
# the difference between them is the effect of the 2026-11 change on old questions.
VARIANTS: dict[str, dict[str, Any]] = {
    **RULE_SETS,
    "current, floor 2 %": {"mix": 0.02},
    "current, floor 10 %": {"mix": 0.10},
    "linear, current floor": {"smooth": False},
}


@dataclass
class Row:
    """One resolved question, joined from the ledger, ``meta.yaml`` and its snapshot."""

    slug: str
    qtype: str
    peer: float | None
    outcome: Any
    forecast: dict[str, Any]
    submitted_cdf: list[float] | None
    scaling: dict[str, Any] | None

    @property
    def date(self) -> str:
        """Day of the forecast (UTC), ``YYYY-MM-DD``."""
        return str(self.forecast.get("ts", ""))[:10]

    @property
    def continuous(self) -> bool:
        """True if PIT and replay apply: a CDF, its grid and a numeric outcome."""
        return (
            self.qtype in CONTINUOUS_TYPES
            and bool(self.submitted_cdf)
            and self.scaling is not None
            and isinstance(self.outcome, int | float)
        )


# ------------------------------------------------------------------ loading
def _snapshot_scaling(folder: Path) -> dict[str, Any] | None:
    """``scaling`` from the earliest cached question snapshot: the one forecast on."""
    snaps = sorted((folder / "raw").glob("metaculus-question-*.json"))
    if not snaps:
        return None
    question = json.loads(snaps[0].read_text(encoding="utf-8")).get("question") or {}
    return question.get("scaling")


def load_rows(questions: Path = QUESTIONS, ledger: Path = LEDGER) -> list[Row]:
    """Every resolved question with its latest forecast and submission, sorted by slug."""
    forecasts: dict[str, dict[str, Any]] = {}
    submissions: dict[str, dict[str, Any]] = {}
    resolutions: dict[str, dict[str, Any]] = {}
    for rec in ledger_records(ledger):
        bucket = {"forecast": forecasts, "submission": submissions,
                  "resolution": resolutions}.get(rec.get("event"))
        if bucket is not None:
            bucket[rec["slug"]] = rec  # the ledger is in time order: the last one wins
    rows = []
    for slug in sorted(resolutions):
        folder = questions / slug
        meta_path = folder / "meta.yaml"
        meta = yaml.safe_load(meta_path.read_text(encoding="utf-8")) if meta_path.exists() else {}
        payload = (submissions.get(slug) or {}).get("payload") or {}
        rows.append(Row(
            slug=slug,
            qtype=meta.get("type") or resolutions[slug].get("type", ""),
            peer=(meta.get("tournament") or {}).get("official_score"),
            outcome=resolutions[slug].get("outcome"),
            forecast=forecasts.get(slug, {}),
            submitted_cdf=payload.get("continuous_cdf"),
            scaling=_snapshot_scaling(folder) if folder.exists() else None,
        ))
    return rows


def knots_of(forecast: dict[str, Any]) -> list[tuple[float, float]] | None:
    """The quantile knots ``build_payload`` submits for this forecast; None for a pmf."""
    dist = forecast.get("distribution") or {}
    if "pmf" in dist:
        return None
    if "percentiles" in dist:
        return sorted((float(k) / 100, float(v)) for k, v in dist["percentiles"].items())
    if "median" in forecast and forecast.get("iqr"):
        lo, hi = forecast["iqr"]
        return [(0.25, float(lo)), (0.5, float(forecast["median"])), (0.75, float(hi))]
    return None


# ------------------------------------------------------------------ PIT
def outcome_mass(cdf: list[float], xs: list[float], outcome: float) -> float:
    """Probability the CDF gives the outcome's bin (or the tail beyond the range)."""
    if outcome < xs[0]:
        return cdf[0]
    if outcome > xs[-1]:
        return 1 - cdf[-1]
    for i in range(len(xs) - 1):
        if xs[i] <= outcome < xs[i + 1]:
            return cdf[i + 1] - cdf[i]
    return cdf[-1] - cdf[-2]  # exactly on the upper edge


def pit(cdf: list[float], xs: list[float], outcome: float) -> float:
    """CDF at the outcome, linear within its bin; the bound's value outside the range."""
    if outcome <= xs[0]:
        return cdf[0]
    if outcome >= xs[-1]:
        return cdf[-1]
    for i in range(len(xs) - 1):
        if xs[i] <= outcome < xs[i + 1]:
            w = (outcome - xs[i]) / (xs[i + 1] - xs[i])
            return cdf[i] + w * (cdf[i + 1] - cdf[i])
    raise AssertionError("unreachable")


def pit_summary(pits: list[float]) -> dict[str, Any]:
    """Coverage counts and a decile histogram of PIT values."""
    deciles = [0] * 10
    for p in pits:
        deciles[min(int(p * 10), 9)] += 1
    return {
        "n": len(pits),
        "inside_iqr": sum(0.25 <= p <= 0.75 for p in pits),
        "outside_90": sum(p < 0.05 or p > 0.95 for p in pits),
        "above_p75": sum(p > 0.75 for p in pits),
        "below_p25": sum(p < 0.25 for p in pits),
        "deciles": deciles,
    }


def pit_rows(rows: list[Row]) -> list[tuple[Row, float, float]]:
    """(row, PIT, ln of the outcome's mass relative to a uniform forecast) per question."""
    out = []
    for r in rows:
        if not r.continuous:
            continue
        xs = sm._grid(r.scaling)
        mass = outcome_mass(r.submitted_cdf, xs, r.outcome)
        out.append((r, pit(r.submitted_cdf, xs, r.outcome),
                    math.log(max(mass, 1e-12) * (len(xs) - 1))))
    return out


# ------------------------------------------------------------------ replay
def replay(
    rows: list[Row], variants: dict[str, dict[str, Any]] = VARIANTS
) -> dict[str, list[tuple[str, float]]]:
    """Per variant, (slug, ln(mass at outcome) - ln(submitted mass)) per question."""
    out: dict[str, list[tuple[str, float]]] = {name: [] for name in variants}
    for r in rows:
        knots = knots_of(r.forecast) if r.continuous else None
        if not knots:
            continue
        xs = sm._grid(r.scaling)
        base = max(outcome_mass(r.submitted_cdf, xs, r.outcome), 1e-12)
        for name, rules in variants.items():
            try:
                cdf = sm.continuous_cdf(knots, r.scaling, **rules)
            except sm.SubmitError:
                continue
            mass = max(outcome_mass(cdf, xs, r.outcome), 1e-12)
            out[name].append((r.slug, math.log(mass / base)))
    return out


def replay_summary(deltas: list[tuple[str, float]]) -> dict[str, float]:
    """Total, median, count and size of losses, and the total without the 3 best gains."""
    ds = [d for _, d in deltas]
    if not ds:
        return {}
    return {
        "n": len(ds),
        "total": sum(ds),
        "median": statistics.median(ds),
        "worse": sum(d < -1e-12 for d in ds),
        "worst": min(ds),
        "best": max(ds),
        "without_top3": sum(ds) - sum(sorted(ds)[-3:]),
    }


# ------------------------------------------------------------------ sample
def sample(
    rows: list[Row],
    worst: int = 6,
    controls: int = 6,
    seed: int = DEFAULT_SEED,
    match_types: bool = True,
) -> tuple[list[Row], list[Row]]:
    """The ``worst`` lowest peer scores and ``controls`` random positive-score questions.

    Controls are drawn per question type in the proportions of the worst set, so the
    contrast is not driven by type; a type with too few positives is filled from the
    others. Types are drawn in the order they first appear among the worst, each from
    its positives in slug order, which is how the 2026-11 sample was drawn: seed
    20261101 reproduces it.
    """
    scored = sorted((r for r in rows if r.peer is not None), key=lambda r: (r.peer, r.slug))
    bad = scored[:worst]
    taken = {r.slug for r in bad}
    pool = sorted((r for r in scored if r.peer > 0 and r.slug not in taken),
                  key=lambda r: r.slug)
    rng = random.Random(seed)
    picked: list[Row] = []
    if match_types:
        for qtype, k in Counter(r.qtype for r in bad).items():  # first-appearance order
            of_type = [r for r in pool if r.qtype == qtype]
            picked += rng.sample(of_type, min(k, len(of_type)))
    rest = [r for r in pool if r not in picked]
    picked += rng.sample(rest, min(controls - len(picked), len(rest)))
    return bad, picked[:controls]


# ------------------------------------------------------------------ report
def _by_type(rows: list[Row]) -> list[str]:
    lines = ["| type | n | sum | mean | negative |", "|---|---|---|---|---|"]
    scored = [r for r in rows if r.peer is not None]
    for qtype in sorted({r.qtype for r in scored}):
        sc = [r.peer for r in scored if r.qtype == qtype]
        lines.append(f"| {qtype} | {len(sc)} | {sum(sc):+.1f} | {statistics.mean(sc):+.1f} "
                     f"| {sum(s < 0 for s in sc)} |")
    if scored:
        sc = [r.peer for r in scored]
        lines.append(f"| **all** | {len(sc)} | {sum(sc):+.1f} | {statistics.mean(sc):+.1f} "
                     f"| {sum(s < 0 for s in sc)} |")
    return lines


def report(rows: list[Row]) -> str:
    """Markdown: peer score by type, PIT coverage, the replay of each rule variant."""
    out = [f"### Post-mortem: {len(rows)} resolved question(s)", ""]
    if not rows:
        out.append("There is no resolved question yet.")
        return "\n".join(out) + "\n"
    out += ["Official spot peer score by question type:", "", *_by_type(rows), ""]
    pits = [p for _, p, _ in pit_rows(rows)]
    if pits:
        s = pit_summary(pits)
        out += [
            (f"**PIT** (where the outcome fell in the submitted CDF), {s['n']} numeric/discrete: "
            f"{s['inside_iqr']} inside the IQR (calibrated: {s['n'] / 2:.1f}), "
            f"{s['outside_90']} outside 5-95 % ({s['n'] / 10:.1f}); "
            f"{s['above_p75']} above p75 vs {s['below_p25']} below p25."),
            "",
            "```",
            *(f"{i / 10:.1f}-{(i + 1) / 10:.1f} {'#' * c} {c}"
              for i, c in enumerate(s["deciles"])),
            "```",
            "",
        ]
    rep = {name: replay_summary(d) for name, d in replay(rows).items()}
    rep = {k: v for k, v in rep.items() if v}
    if rep:
        out += [
            ("**Replay** (change in log score at the outcome vs as submitted, nats; "
            "about 100 * c peer points each, c = 0.5-1):"),
            "",
            "| rule | n | total | median | worse | worst | total without top 3 |",
            "|---|---|---|---|---|---|---|",
            *(f"| {k} | {v['n']} | {v['total']:+.2f} | {v['median']:+.3f} | {v['worse']} "
              f"| {v['worst']:+.2f} | {v['without_top3']:+.2f} |" for k, v in rep.items()),
            "",
            ("In-sample for every question resolved before a rule changed; see "
            "`docs/postmortem.md`."),
        ]
    return "\n".join(out) + "\n"


# ------------------------------------------------------------------ CLI
def main() -> None:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("--since", help="only questions forecast on or after YYYY-MM-DD")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("pit", help="PIT per resolved continuous question, and coverage")
    rp = sub.add_parser("replay", help="replay the submissions under alternative rules")
    rp.add_argument("--detail", action="store_true", help="per-question deltas too")
    sp = sub.add_parser("sample", help="worst questions plus type-matched controls")
    sp.add_argument("--worst", type=int, default=6)
    sp.add_argument("--controls", type=int, default=6)
    sp.add_argument("--seed", type=int, default=DEFAULT_SEED)
    sp.add_argument("--no-match-types", action="store_true")
    sub.add_parser("report", help="markdown summary (the daily sync's run summary)")
    args = ap.parse_args()

    rows = load_rows()
    if args.since:
        rows = [r for r in rows if r.date >= args.since]

    if args.cmd == "pit":
        for r, p, rel in sorted(pit_rows(rows), key=lambda t: t[1]):
            peer = "—" if r.peer is None else f"{r.peer:+.1f}"
            print(f"{p:6.3f}  ln(mass/uniform) {rel:+6.2f}  peer {peer:>6}  {r.qtype:9s} {r.slug}")
        print(json.dumps(pit_summary([p for _, p, _ in pit_rows(rows)])))
    elif args.cmd == "replay":
        for name, deltas in replay(rows).items():
            s = replay_summary(deltas)
            if not s:
                continue
            print(f"{name:28s} n={s['n']:3d} total {s['total']:+6.2f}  median {s['median']:+.3f}"
                  f"  worse {s['worse']:2d}  worst {s['worst']:+.2f}"
                  f"  without top 3 {s['without_top3']:+.2f}")
            if args.detail:
                for slug, d in deltas:
                    print(f"    {d:+.3f}  {slug}")
    elif args.cmd == "sample":
        bad, ctl = sample(rows, args.worst, args.controls, args.seed, not args.no_match_types)
        print(f"# worst {len(bad)}")
        for r in bad:
            print(f"{r.peer:+7.1f}  {r.qtype:15s} {r.slug}")
        print(f"# controls {len(ctl)} (seed {args.seed})")
        for r in ctl:
            print(f"{r.peer:+7.1f}  {r.qtype:15s} {r.slug}")
    else:
        print(report(rows), end="")


if __name__ == "__main__":
    main()
