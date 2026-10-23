#!/usr/bin/env python3
"""Submit the current ledger forecast to Metaculus as the bot account.

Two paths, chosen per question by ``meta.yaml``, never by a flag:

- **One-shot tournament questions** (``tournament.mode: one_shot`` -- MiniBench,
  FutureEval). Called by the sweep workflow right after the forecaster has logged
  its forecast, with no human in between (the tournaments forbid one). Four guards
  run before anything is sent: ``meta.tournament.submitted``, a ``submission``
  record in the ledger, the bot's live forecast on Metaculus, and the question
  still being open. Then it posts the forecast, posts the **private** rationale
  comment the rules require (the newest version of ``forecast.md``, extracted
  mechanically), and records both in the ledger and ``meta.yaml``. A closed
  window is a normal outcome (``missed_window``), not a crash; a forecast that went
  up without its comment is recorded as such and retried by the daily sync.
- **Everything else** (individual questions the maintainer added, ``updatable``
  tournaments such as the Metaculus Cup). No automation runs this path yet; it is
  kept for manual use from upstream. It skips a question whose live forecast
  already matches and writes nothing to the repository.

What gets submitted is the latest ``forecast`` record in the ledger for each
target slug:

- binary: the ledger median.
- multiple_choice: the record's ``distribution.probabilities`` (exact Metaculus
  option labels).
- numeric / date / discrete: the record's ``distribution`` (``percentiles``, or
  ``pmf`` for discrete) when it has one; otherwise the ledger quartiles, with
  exponential tails matched to the edge densities -- a weaker approximation,
  flagged in the output.

Records logged before the ledger had a ``distribution`` field carry only the
median and IQR. For those -- and only those -- a JSON *spec* file supplies the
distribution in the same shapes, plus the version it was read from::

    {
      "<slug>": {"version": 3, "probabilities": {"<option>": 0.67, ...}},
      "<slug>": {"version": 1, "percentiles": {"5": 186000, "50": 272000, ...}},
      "<slug>": {"version": 1, "pmf": {"0": 0.001, "1": 0.012, ...}}
    }

A spec entry's ``version`` must equal the ledger's latest version, so a vector
extracted from an older ``forecast.md`` block cannot be submitted by mistake,
and a spec entry for a record that already carries a distribution is refused:
the ledger is the record, a spec only fills its gaps. Both sources pass the
same validation as ``log_forecast.py`` (``distribution_problems``).

Group-of-questions posts (one post, one sub-question per year, say) are
submitted per slug: the ``?sub-question=<id>`` in the slug's ``meta.yaml`` URL
names the sub-question, and a group slug whose URL lacks it is refused rather
than guessed. Each post is fetched once per run, however many of its
sub-questions are targets.

Examples
--------
    uv run scripts/submit_metaculus.py 2026-10-19-mc46101-some-minibench-question --dry-run
    uv run scripts/submit_metaculus.py 2026-09-05-mc45230-united-states-attack-oman-before-2027
    uv run scripts/submit_metaculus.py 45230 45464 --dry-run
    uv run scripts/submit_metaculus.py "https://www.metaculus.com/questions/21095/x/?sub-question=21098"
    uv run scripts/submit_metaculus.py --all --project "Metaculus Cup Fall 2026" --spec spec.json
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import math
import re
import sys
import time
from dataclasses import dataclass
from itertools import pairwise
from pathlib import Path
from typing import Any
from urllib.parse import parse_qs, urlparse

sys.path.insert(0, str(Path(__file__).resolve().parent))
import metaculus_api as mapi
from _common import (
    QUESTIONS,
    all_questions,
    distribution_problems,
    find_slug,
    load_meta,
    save_meta,
    set_forecast_header,
)
from calibration import read_ledger
from log_forecast import _logged_submissions, record_submission

# Metaculus rate-limits by IP; a steady pace is cheaper than recovering from a 429.
PAUSE_S = 4.0
# The comment is the newest forecast.md version; long ones are cut in the middle so
# the closing summary block (the final decision) always survives.
MAX_COMMENT_CHARS = 9000

# Bounds Metaculus enforces on submitted values.
P_MIN, P_MAX = 0.001, 0.999
OPEN_BOUND_MASS = 0.001  # minimum tail mass outside an open bound
MIN_STEP_PER_BIN = 0.01  # CDF must rise by >= this / inbound_outcome_count per bin
MAX_STEP_PER_BIN = 40.0  # ... and by <= this / inbound_outcome_count (0.2 at 200)
UNIFORM_MIX = 0.02  # default uniform mixture that guarantees the minimum step
CLOSED_STATUSES = {"closed", "resolved", "deleted"}


class SubmitError(Exception):
    """A target that cannot be submitted; the message says why."""


@dataclass
class Payload:
    """One question's submission, in the shape ``/questions/forecast/`` takes."""

    slug: str
    post_id: int
    question_id: int
    qtype: str
    values: dict[str, Any]
    note: str = ""

    def body(self) -> list[dict[str, Any]]:
        """JSON body for ``POST /api/questions/forecast/``."""
        return mapi.forecast_body(self.question_id, self.values)

    def post(self) -> int:
        """Submit to ``POST /api/questions/forecast/``; returns the HTTP status."""
        try:
            return mapi.submit_forecast(self.question_id, self.values)
        except mapi.MetaculusError as exc:
            raise SubmitError(str(exc)) from exc


# ------------------------------------------------------------------ transport
def fetch_post(post_id: int) -> dict[str, Any]:
    """``/api/posts/<id>/`` as the bot, including its own ``my_forecasts``."""
    try:
        return mapi.get_post(post_id, stage="submit")
    except mapi.MetaculusError as exc:
        raise SubmitError(str(exc)) from exc


def project_names(post: dict[str, Any]) -> set[str]:
    """Names of every tournament, series and project a post belongs to."""
    names: set[str] = set()
    for entry in (post.get("projects") or {}).values():
        for proj in entry if isinstance(entry, list) else [entry]:
            if isinstance(proj, dict) and proj.get("name"):
                names.add(proj["name"])
    return names


def subquestion_id(url: str | None) -> int | None:
    """The sub-question a Metaculus URL pins with ``?sub-question=<id>``, if any."""
    raw = parse_qs(urlparse(url or "").query).get("sub-question")
    if not raw:
        return None
    try:
        return int(raw[0])
    except ValueError:
        raise SubmitError(f"sub-question {raw[0]!r} in {url} is not an id") from None


def select_question(post: dict[str, Any], sub_id: int | None) -> dict[str, Any]:
    """The question a slug forecasts: the post's own, or one of its group's.

    A group post has no top-level ``question``; picking a sub-question by
    position or label would silently submit to the wrong year, so the id must
    be pinned explicitly.
    """
    q = post.get("question")
    if q:
        if sub_id is not None and sub_id != q["id"]:
            raise SubmitError(
                f"URL pins sub-question {sub_id}, but post {post['id']} is the "
                f"single question {q['id']}"
            )
        return q
    group = (post.get("group_of_questions") or {}).get("questions") or []
    if not group:
        raise SubmitError(f"post {post['id']} has no question to forecast")
    if sub_id is None:
        ids = ", ".join(f"{g.get('label')}={g['id']}" for g in group)
        raise SubmitError(
            "group-of-questions post; add ?sub-question=<id> to the url in "
            f"meta.yaml ({ids})"
        )
    for g in group:
        if g["id"] == sub_id:
            return g
    raise SubmitError(f"sub-question {sub_id} is not in post {post['id']}")


# ------------------------------------------------------------------ geometry
def cdf_from_knots(x: float, knots: list[tuple[float, float]]) -> float:
    """CDF at ``x`` through ``(probability, value)`` quantile knots.

    Linear between knots. Beyond the outer knots the tails are exponential with
    the density of the adjacent segment, so the curve stays smooth at the knot
    and the tail mass decays instead of stopping dead at an arbitrary point.
    Knots that share a value are a point mass there (e.g. a record close the
    answer cannot fall below): the CDF jumps from their lowest probability to
    their highest, and the tails take the density of the nearest sloped segment.
    """
    # (value, P just below it, P at it); merging ties keeps every segment sloped
    pts: list[tuple[float, float, float]] = []
    for p, v in knots:
        if pts and pts[-1][0] == v:
            pts[-1] = (v, pts[-1][1], p)
        else:
            pts.append((v, p, p))
    (x0, below0, at0), (x1, below1, _) = pts[0], pts[1]
    if x < x0:
        scale = below0 * (x1 - x0) / (below1 - at0)
        return below0 * math.exp((x - x0) / scale)
    (xm, _, atm), (xn, belown, atn) = pts[-2], pts[-1]
    if x >= xn:
        scale = (1 - atn) * (xn - xm) / (belown - atm)
        return 1 - (1 - atn) * math.exp(-(x - xn) / scale)
    for (a, _, pa), (b, pb, _) in pairwise(pts):
        if a <= x < b:
            return pa + (pb - pa) * (x - a) / (b - a)
    raise AssertionError("unreachable")


def _as_seconds(v: float | str) -> float:
    """A grid point as a float; date questions serve ISO timestamps, not numbers.

    The ledger stores date forecasts in Unix seconds, the unit ``range_min`` and
    ``range_max`` already use, so ISO points are converted to match.
    """
    if isinstance(v, str):
        try:
            return float(v)
        except ValueError:
            return dt.datetime.fromisoformat(v).timestamp()
    return float(v)


def _grid(scaling: dict[str, Any]) -> list[float]:
    """The ``inbound_outcome_count + 1`` real-valued CDF evaluation points."""
    if scaling.get("continuous_range"):
        return [_as_seconds(v) for v in scaling["continuous_range"]]
    n = int(scaling["inbound_outcome_count"])
    rmin, rmax = float(scaling["range_min"]), float(scaling["range_max"])
    zero = scaling.get("zero_point")
    out = []
    for i in range(n + 1):
        t = i / n
        if zero is None:
            out.append(rmin + (rmax - rmin) * t)
        else:  # Metaculus' log scaling
            r = (rmax - zero) / (rmin - zero)
            out.append(rmin + (rmax - rmin) * (r**t - 1) / (r - 1))
    return out


def _fit_to_bounds(raw: list[float], scaling: dict[str, Any]) -> list[float]:
    """Pin the end points to the bound rules and enforce the minimum step.

    The interior shape is kept and mixed with a small uniform component, which
    is what guarantees every bin its minimum mass without distorting quartiles
    visibly. The mixture weight grows only when little mass falls inside the
    range (e.g. a forecast that sits mostly above an open upper bound).
    """
    n = len(raw) - 1
    lo = max(raw[0], OPEN_BOUND_MASS) if scaling.get("open_lower_bound") else 0.0
    hi = min(raw[-1], 1 - OPEN_BOUND_MASS) if scaling.get("open_upper_bound") else 1.0
    if hi - lo < MIN_STEP_PER_BIN:
        raise SubmitError(
            f"only {hi - lo:.4f} of the mass falls inside the question's range; "
            "this forecast cannot be expressed on it"
        )
    span = raw[-1] - raw[0]
    shape = [(v - raw[0]) / span if span > 0 else i / n for i, v in enumerate(raw)]
    mix = max(UNIFORM_MIX, 1.2 * MIN_STEP_PER_BIN / (hi - lo))
    return [lo + (hi - lo) * ((1 - mix) * s + mix * i / n) for i, s in enumerate(shape)]


def _cap_steps(cdf: list[float], scaling: dict[str, Any]) -> list[float]:
    """Spread any bin above Metaculus' maximum step into the bins above it.

    A point mass (tied percentiles) lands in a single bin. Its excess moves
    upward because ties usually mark a floor, such as a record close the answer
    cannot fall below; only what would overflow the top bin goes back down.
    """
    n = len(cdf) - 1
    # headroom for the rounding Metaculus applies before comparing
    cap = MAX_STEP_PER_BIN / int(scaling["inbound_outcome_count"]) * (1 - 1e-6)
    steps = [b - a for a, b in pairwise(cdf)]
    if max(steps) <= cap:
        return cdf
    carry = 0.0
    for i in [*range(n), *reversed(range(n))]:
        steps[i] += carry
        carry = max(steps[i] - cap, 0.0)
        steps[i] -= carry
    out = [cdf[0]]
    for step in steps:
        out.append(out[-1] + step)
    out[-1] = cdf[-1]  # keep a closed bound at exactly 1 despite float drift
    return out


def continuous_cdf(
    knots: list[tuple[float, float]], scaling: dict[str, Any]
) -> list[float]:
    """Metaculus CDF for a numeric or date question from quantile knots."""
    knots = sorted(knots)
    if len({v for _, v in knots}) < 2:
        raise SubmitError("need percentiles on at least two distinct values")
    if any(b[1] < a[1] for a, b in pairwise(knots)):
        raise SubmitError(f"percentile values are not monotone: {knots}")
    raw = [cdf_from_knots(x, knots) for x in _grid(scaling)]
    return _cap_steps(_fit_to_bounds(raw, scaling), scaling)


def discrete_cdf(pmf: dict[str, float], scaling: dict[str, Any]) -> list[float]:
    """Metaculus CDF for a discrete question from a PMF keyed by outcome value.

    Every in-range outcome gets at least the minimum step, so a PMF that leaves
    a value at 0 still validates; the mass is then renormalised. A key beyond an
    open bound (``"661"`` for "above 660") is that tail's mass. An outcome above
    Metaculus' maximum step is pinned at it (see ``_cap_outcomes``).
    """
    n = int(scaling["inbound_outcome_count"])
    edges = _grid(scaling)
    centres = [(a + b) / 2 for a, b in pairwise(edges)]
    found = [0.0] * n
    below = above = 0.0
    unknown = []
    for k, v in pmf.items():
        k, v = float(k), float(v)
        # Matched by tolerance, not dict lookup: on a fractional grid the centres
        # are float-arithmetic values (0.20000000000000004 for a logged "0.2").
        i = next((j for j, c in enumerate(centres) if abs(k - c) < 1e-9), None)
        if i is not None:
            found[i] += v
        elif k < edges[0] and scaling.get("open_lower_bound"):
            below += v
        elif k > edges[-1] and scaling.get("open_upper_bound"):
            above += v
        else:
            unknown.append(k)
    if unknown:
        raise SubmitError(f"pmf keys {unknown} are not outcomes of this question")
    floor = MIN_STEP_PER_BIN / n * 1.1
    mass = [max(m, floor) for m in found]
    total = below + sum(mass) + above
    probs = _cap_outcomes([below / total, *(m / total for m in mass), above / total], n)
    out, run = [probs[0]], probs[0]
    for m in probs[1:-1]:
        run += m
        out.append(run)
    out[-1] = 1.0 - probs[-1]
    if scaling.get("open_lower_bound") or scaling.get("open_upper_bound"):
        return _fit_to_bounds(out, scaling)
    return out


def _cap_outcomes(probs: list[float], n: int) -> list[float]:
    """Pin in-range outcomes above Metaculus' maximum step at it; rescale the rest.

    ``probs`` is ``[below, outcome_1 .. outcome_n, above]`` summing to 1; the two
    tails are uncapped. Under a log score the best forecast Metaculus accepts
    keeps the other outcomes' ratios and scales them by one common factor (the
    KL-closest feasible PMF), rather than piling the excess onto the neighbours
    as ``_cap_steps`` does for a continuous point mass.
    """
    # headroom for the rounding Metaculus applies before comparing
    cap = MAX_STEP_PER_BIN / n * (1 - 1e-6)
    pinned: set[int] = set()
    while True:
        free = sum(p for i, p in enumerate(probs) if i not in pinned)
        scale = (1 - cap * len(pinned)) / free
        over = {
            i for i in range(1, n + 1) if i not in pinned and probs[i] * scale > cap
        }
        if not over:
            return [cap if i in pinned else p * scale for i, p in enumerate(probs)]
        pinned |= over


def mc_probabilities(probs: dict[str, float], options: list[str]) -> dict[str, float]:
    """Validate labels against Metaculus' options, floor at P_MIN, renormalise."""
    missing = [o for o in options if o not in probs]
    extra = [k for k in probs if k not in options]
    if missing or extra:
        raise SubmitError(
            f"option labels must match Metaculus exactly; missing {missing}, "
            f"unknown {extra}"
        )
    total = sum(probs.values())
    if abs(total - 1) > 0.02:
        raise SubmitError(f"option probabilities sum to {total:.3f}, not 1")
    floored = {o: max(float(probs[o]), P_MIN) for o in options}
    s = sum(floored.values())
    return {o: v / s for o, v in floored.items()}


def validate_cdf(cdf: list[float], scaling: dict[str, Any]) -> None:
    """Local copy of the rules Metaculus enforces, to fail before the POST."""
    n = int(scaling["inbound_outcome_count"])
    if len(cdf) != n + 1:
        raise SubmitError(f"CDF has {len(cdf)} points, question needs {n + 1}")
    steps = [b - a for a, b in pairwise(cdf)]
    if min(steps) < MIN_STEP_PER_BIN / n - 1e-12:
        raise SubmitError(
            f"CDF step {min(steps):.2e} is below {MIN_STEP_PER_BIN / n:.2e}"
        )
    if max(steps) > MAX_STEP_PER_BIN / n + 1e-12:
        raise SubmitError(
            f"CDF step {max(steps):.3f} is above {MAX_STEP_PER_BIN / n:.3f}"
        )
    if scaling.get("open_lower_bound"):
        if cdf[0] < OPEN_BOUND_MASS - 1e-12:
            raise SubmitError("open lower bound needs cdf[0] >= 0.001")
    elif cdf[0] != 0.0:
        raise SubmitError("closed lower bound needs cdf[0] == 0")
    if scaling.get("open_upper_bound"):
        if cdf[-1] > 1 - OPEN_BOUND_MASS + 1e-12:
            raise SubmitError("open upper bound needs cdf[-1] <= 0.999")
    elif cdf[-1] != 1.0:
        raise SubmitError("closed upper bound needs cdf[-1] == 1")


def quantile(cdf: list[float], scaling: dict[str, Any], p: float) -> float | None:
    """Invert a submitted CDF, for the dry-run echo; None if ``p`` is off-range."""
    xs = _grid(scaling)
    for i in range(len(cdf) - 1):
        if cdf[i] <= p <= cdf[i + 1]:
            return xs[i] + (xs[i + 1] - xs[i]) * (p - cdf[i]) / (cdf[i + 1] - cdf[i])
    return None


# ------------------------------------------------------------------ payloads
def build_payload(
    slug: str,
    record: dict[str, Any],
    post: dict[str, Any],
    spec: dict[str, Any] | None,
    sub_id: int | None = None,
) -> Payload:
    """Turn the latest ledger record (+ optional spec entry) into a submission.

    ``sub_id`` pins the sub-question of a group post (see ``select_question``).
    """
    q = select_question(post, sub_id)
    qtype = q["type"]
    if qtype != record.get("type"):
        raise SubmitError(
            f"ledger says {record.get('type')!r}, Metaculus says {qtype!r}"
        )
    dist = record.get("distribution")
    if spec is not None:
        if dist is not None:
            raise SubmitError(
                f"the ledger already records v{record['version']}'s distribution; "
                "drop this slug from the spec"
            )
        if spec.get("version") != record["version"]:
            raise SubmitError(
                f"spec is for v{spec.get('version')}, the ledger's latest is "
                f"v{record['version']}; re-extract it from forecast.md"
            )
        dist = {k: v for k, v in spec.items() if k != "version"}
    if dist:
        problems = distribution_problems(
            qtype, dist, record["median"], record["iqr"], q.get("options")
        )
        if problems:
            raise SubmitError("distribution rejected: " + "; ".join(problems))
    dist = dist or {}
    base = {"slug": slug, "post_id": post["id"], "question_id": q["id"], "qtype": qtype}

    if qtype == "binary":
        p = min(max(float(record["median"]), P_MIN), P_MAX)
        return Payload(**base, values={"probability_yes": p})

    if qtype == "multiple_choice":
        if "probabilities" not in dist:
            raise SubmitError(
                f"v{record['version']} predates the ledger's distribution field; "
                f"supply its option vector in a spec (options: {q['options']})"
            )
        probs = mc_probabilities(dist["probabilities"], q["options"])
        return Payload(**base, values={"probability_yes_per_category": probs})

    if qtype not in {"numeric", "date", "discrete"}:
        raise SubmitError(f"unsupported question type {qtype!r}")
    scaling = q["scaling"]
    note = ""
    if qtype == "discrete" and "pmf" in dist:
        cdf = discrete_cdf(dist["pmf"], scaling)
    else:
        if "percentiles" in dist:
            knots = [(float(k) / 100, float(v)) for k, v in dist["percentiles"].items()]
        else:
            lo, hi = record["iqr"]
            knots = [
                (0.25, float(lo)),
                (0.5, float(record["median"])),
                (0.75, float(hi)),
            ]
            note = "quartiles only: tails extrapolated"
        cdf = continuous_cdf(knots, scaling)
    validate_cdf(cdf, scaling)
    return Payload(**base, values={"continuous_cdf": cdf}, note=note)


live_values = mapi.live_values


def as_forecast_values(payload: Payload, q: dict[str, Any]) -> list[float]:
    """The payload in Metaculus' ``forecast_values`` layout, for comparison."""
    v = payload.values
    if "probability_yes" in v:
        return [1 - v["probability_yes"], v["probability_yes"]]
    if "probability_yes_per_category" in v:
        return [v["probability_yes_per_category"][o] for o in q["options"]]
    return v["continuous_cdf"]


def unchanged(payload: Payload, q: dict[str, Any], tol: float = 1e-4) -> bool:
    """True when the bot's live forecast on question ``q`` equals this payload."""
    live = live_values(q)
    new = as_forecast_values(payload, q)
    return (
        live is not None
        and len(live) == len(new)
        and all(abs(a - b) <= tol for a, b in zip(live, new))
    )


def describe(payload: Payload, q: dict[str, Any]) -> str:
    """One-line human summary of what would be submitted."""
    v = payload.values
    if "probability_yes" in v:
        return f"P(yes) = {v['probability_yes']:.3f}"
    if "probability_yes_per_category" in v:
        return " · ".join(
            f"{o}: {p:.3f}" for o, p in v["probability_yes_per_category"].items()
        )
    scaling = q["scaling"]
    qs = [quantile(v["continuous_cdf"], scaling, p) for p in (0.25, 0.5, 0.75)]
    fmt = ["off-range" if x is None else f"{x:.6g}" for x in qs]
    cdf = v["continuous_cdf"]
    return (
        f"q25 {fmt[0]} · q50 {fmt[1]} · q75 {fmt[2]} "
        f"(P<min {cdf[0]:.3f}, P>max {1 - cdf[-1]:.3f})"
    )


# ------------------------------------------------------------------ one shot
def comment_text(slug: str) -> str:
    """The private rationale comment: the newest version of ``forecast.md``.

    Metaculus requires a comment on every forecast that "accurately represents the
    reasoning process and final decision". The newest version block is exactly
    that, already written; extracting it mechanically means no model is asked to
    describe its reasoning twice. Over ``MAX_COMMENT_CHARS`` the middle is cut,
    never the closing summary block.
    """
    text = (QUESTIONS / slug / "forecast.md").read_text(encoding="utf-8")
    marks = list(re.finditer(r"(?m)^## v\d+\s", text))
    if not marks:
        raise SubmitError(f"{slug}: forecast.md has no version section to comment with")
    start = marks[0].start()
    stop = re.search(r"(?m)^## (?:v\d+\s|Resolution)", text[marks[0].end() :])
    block = text[start : marks[0].end() + stop.start() if stop else len(text)].strip()
    block = re.sub(r"<!--.*?-->", "", block, flags=re.DOTALL)
    cut = re.search(r"(?m)^\*\*(?:Question|Date)\*\*:", block)
    body, summary = (block[: cut.start()], block[cut.start() :]) if cut else (block, "")
    if not re.search(r"\*\*Thesis\*\*:\s*\S", summary):
        raise SubmitError(f"{slug}: the newest version has no filled-in summary block")
    room = MAX_COMMENT_CHARS - len(summary) - 40
    if len(body) > room:
        body = body[:room].rstrip() + "\n\n[... truncated ...]\n\n"
    return (body + summary).strip()


def mark_missed_window(slug: str) -> None:
    """Close out a one-shot question whose window ended with nothing submitted."""
    meta = load_meta(slug)
    tour = meta.get("tournament") or {}
    if tour.get("submitted"):
        return
    tour["missed_window"] = True
    meta["status"] = "dropped"
    meta["next_review"] = None
    save_meta(slug, meta)
    set_forecast_header(slug, "Status", "dropped")


def submit_one_shot(slug: str, rec: dict[str, Any] | None, dry_run: bool) -> str:
    """Run the one-shot path for one slug; returns the outcome word.

    Outcomes: ``submitted``, ``submitted-no-comment``, ``would submit``,
    ``already submitted``, ``already live``, ``missed window``, ``no forecast``.
    Raises ``SubmitError`` for anything that should fail the job.
    """
    meta = load_meta(slug)
    tour = meta.get("tournament") or {}
    if tour.get("submitted") or _logged_submissions(slug):
        print(f"- {slug}: already submitted at {tour.get('submitted')} (one shot)")
        return "already submitted"
    post = fetch_post(int(meta["post_id"]))
    q = select_question(post, subquestion_id(meta.get("url")))
    if live_values(q) is not None:
        # Submitted by an earlier run whose record was lost. Sending again would be
        # the second forecast the rules forbid, whatever the local record says.
        print(f"! {slug}: Metaculus already holds a bot forecast; not resubmitting")
        return "already live"
    if not mapi.is_open(post, q):
        print(f"- {slug}: question is {q.get('status') or post.get('status')}; window missed")
        if not dry_run:
            mark_missed_window(slug)
        return "missed window"
    if rec is None or rec.get("slug") != slug:
        print(f"- {slug}: no forecast logged; nothing to submit")
        return "no forecast"
    if rec.get("version") != 1:
        raise SubmitError(f"{slug}: one-shot question at v{rec.get('version')}, expected v1")
    if meta.get("question_id") not in (None, q["id"]):
        raise SubmitError(
            f"{slug}: meta question_id {meta.get('question_id')} != Metaculus {q['id']}"
        )
    payload = build_payload(slug, rec, post, None, subquestion_id(meta.get("url")))
    comment = comment_text(slug)
    print(f"{slug} v1 (q{payload.question_id}, {payload.qtype}): {describe(payload, q)}")
    if payload.note:
        print(f"  [{payload.note}]")
    if dry_run:
        print(f"  comment: {len(comment)} chars, private")
        return "would submit"
    status = payload.post()
    print(f"  -> forecast accepted (HTTP {status})")
    commented = False
    try:
        time.sleep(1.0)
        mapi.post_comment(payload.post_id, comment, private=True)
        commented = True
        print("  -> private comment posted")
    except mapi.MetaculusError as exc:
        # The forecast is in and cannot be redone; the daily sync retries the comment.
        print(f"  ! comment failed, recorded for retry: {exc}")
    record_submission(slug, payload.values, status, commented)
    return "submitted" if commented else "submitted-no-comment"


# ------------------------------------------------------------------ targets
def latest_records() -> dict[str, dict[str, Any]]:
    """Latest forecast record per unresolved, Metaculus-sourced slug."""
    forecasts, resolutions = read_ledger()
    return {
        slug: recs[-1]
        for slug, recs in forecasts.items()
        if recs and slug not in resolutions and recs[-1].get("source") == "metaculus"
    }


def resolve_targets(args: argparse.Namespace, records: dict[str, dict]) -> list[str]:
    """Slugs to consider, in folder order."""
    if args.all:
        open_slugs = {s for s, m in all_questions() if m.get("status") == "open"}
        return sorted(s for s in records if s in open_slugs)
    out = []
    for needle in args.slugs:
        slug = find_slug(needle)
        if slug is None:
            sys.exit(f"! no unique question for {needle!r}")
        out.append(slug)
    return out


def main() -> None:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("slugs", nargs="*", help="slug, post id or URL (one or more)")
    ap.add_argument(
        "--all", action="store_true", help="every open Metaculus question in the ledger"
    )
    ap.add_argument(
        "--project",
        help="only posts in this tournament/series (exact name, e.g. "
        "'Metaculus Cup Fall 2026')",
    )
    ap.add_argument(
        "--spec",
        type=Path,
        help="JSON file with distributions for records that predate the ledger field",
    )
    ap.add_argument(
        "--dry-run", action="store_true", help="build and show, do not POST"
    )
    ap.add_argument(
        "--force",
        action="store_true",
        help="resubmit even if the live forecast matches",
    )
    args = ap.parse_args()
    if bool(args.all) == bool(args.slugs):
        ap.error("give either one or more slugs or --all")

    records = latest_records()
    targets = resolve_targets(args, records)
    specs: dict[str, Any] = (
        json.loads(args.spec.read_text(encoding="utf-8")) if args.spec else {}
    )
    unknown = [s for s in specs if s not in records]
    if unknown:
        print(f"! spec entries with no open ledger forecast, ignored: {unknown}")

    # Sibling slugs of a group share one post; fetching it once per run keeps
    # the IP rate limit quiet and needs no refresh, since a submission only
    # changes the sub-question it targets.
    posts: dict[int, dict[str, Any]] = {}
    tally = {
        "submitted": 0,
        "would submit": 0,
        "unchanged": 0,
        "skipped": 0,
        "failed": 0,
    }
    for i, slug in enumerate(targets):
        if i:
            time.sleep(PAUSE_S)
        rec = records.get(slug)
        if (load_meta(slug).get("tournament") or {}).get("mode") == "one_shot":
            try:
                outcome = submit_one_shot(slug, rec, args.dry_run)
            except (SubmitError, mapi.MetaculusError, ValueError) as exc:
                print(f"! {slug}: {exc}")
                tally["failed"] += 1
                continue
            key = {"submitted-no-comment": "submitted"}.get(outcome, outcome)
            tally[key] = tally.get(key, 0) + 1
            continue
        if rec is None:
            print(f"- {slug}: no unresolved Metaculus forecast in the ledger")
            tally["skipped"] += 1
            continue
        try:
            sub_id = subquestion_id(load_meta(slug).get("url"))
            pid = int(rec["post_id"])
            if pid not in posts:
                posts[pid] = fetch_post(pid)
            post = posts[pid]
            if args.project and args.project not in project_names(post):
                continue
            if post.get("status") in CLOSED_STATUSES:
                print(f"- {slug}: post is {post.get('status')}")
                tally["skipped"] += 1
                continue
            q = select_question(post, sub_id)
            # A group post stays open while its earlier sub-questions close.
            if q.get("status") in CLOSED_STATUSES:
                print(f"- {slug}: sub-question {q['id']} is {q.get('status')}")
                tally["skipped"] += 1
                continue
            payload = build_payload(slug, rec, post, specs.get(slug), sub_id)
        except SubmitError as exc:
            print(f"! {slug}: {exc}")
            tally["failed"] += 1
            continue
        head = f"{slug} v{rec['version']} (q{payload.question_id}, {payload.qtype})"
        note = f"  [{payload.note}]" if payload.note else ""
        print(f"{head}: {describe(payload, q)}{note}")
        if not args.force and unchanged(payload, q):
            print("  = already live, not resubmitted")
            tally["unchanged"] += 1
            continue
        if args.dry_run:
            tally["would submit"] += 1
            continue
        time.sleep(PAUSE_S)
        try:
            payload.post()
        except SubmitError as exc:
            print(f"  ! rejected: {exc}")
            tally["failed"] += 1
            continue
        print("  → submitted")
        tally["submitted"] += 1

    print("\n" + " · ".join(f"{k} {v}" for k, v in tally.items() if v))
    if tally["failed"]:
        sys.exit(1)


if __name__ == "__main__":
    main()
