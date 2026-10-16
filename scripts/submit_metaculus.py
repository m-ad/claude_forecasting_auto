#!/usr/bin/env python3
"""Submit the current ledger forecast to Metaculus as the bot account.

**Operator-invoked only.** This script posts to a live tournament under the bot
account behind ``METACULUS_API_KEY``. Run it only when the operator explicitly
asks for a submission; no other workflow (``/forecast``, ``/update``,
``/resolve``, ``/status --act``) calls it. CI calls it after a pull request is
merged into ``main`` (``.github/workflows/submit-metaculus.yml``): the merge is
the operator's approval. It never writes to the repository:
the ledger, ``meta.yaml`` and ``forecast.md`` stay untouched.

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
import os
import sys
import time
import urllib.error
import urllib.request
from dataclasses import dataclass
from itertools import pairwise
from pathlib import Path
from typing import Any
from urllib.parse import parse_qs, urlparse

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common import all_questions, distribution_problems, find_slug, load_meta
from calibration import read_ledger

API = "https://www.metaculus.com/api"
USER_AGENT = "claude-forecasting/0.1 (submit_metaculus)"
# Metaculus rate-limits by IP, and a tripped limit blocks every surface for ~2
# minutes; a steady pace is cheaper than recovering from a 429.
PAUSE_S = 4.0
RETRY_WAITS_S = (30.0, 60.0, 120.0)

# Bounds Metaculus enforces on submitted values.
P_MIN, P_MAX = 0.001, 0.999
OPEN_BOUND_MASS = 0.001  # minimum tail mass outside an open bound
MIN_STEP_PER_BIN = 0.01  # CDF must rise by >= this / inbound_outcome_count per bin
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
        return [
            {
                "question": self.question_id,
                "probability_yes": self.values.get("probability_yes"),
                "probability_yes_per_category": self.values.get(
                    "probability_yes_per_category"
                ),
                "continuous_cdf": self.values.get("continuous_cdf"),
            }
        ]


# ------------------------------------------------------------------ transport
def _request(method: str, path: str, body: Any = None) -> Any:
    """Call the Metaculus API with the bot key, backing off on 429.

    Raises
    ------
    SubmitError
        On any non-2xx answer other than a 429 that outlasts the retries.
    """
    key = os.environ.get("METACULUS_API_KEY")
    if not key:
        raise SubmitError("METACULUS_API_KEY is not set")
    data = json.dumps(body).encode() if body is not None else None
    for wait in (*RETRY_WAITS_S, None):
        req = urllib.request.Request(
            f"{API}/{path}",
            data=data,
            method=method,
            headers={
                "Authorization": f"Token {key}",
                "Accept": "application/json",
                "Content-Type": "application/json",
                "User-Agent": USER_AGENT,
            },
        )
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                raw = resp.read()
                return json.loads(raw) if raw else {}
        except urllib.error.HTTPError as exc:
            if exc.code == 429 and wait is not None:
                print(f"  (429 rate-limited; waiting {wait:.0f}s)", file=sys.stderr)
                time.sleep(wait)
                continue
            detail = exc.read()[:500].decode("utf-8", "replace")
            raise SubmitError(f"HTTP {exc.code} on {method} {path}: {detail}") from exc
        except OSError as exc:
            raise SubmitError(f"{method} {path} failed: {exc}") from exc
    raise AssertionError("unreachable")


def fetch_post(post_id: int) -> dict[str, Any]:
    """``/api/posts/<id>/`` as the bot, including its own ``my_forecasts``."""
    return _request("GET", f"posts/{post_id}/")


def post_forecast(payload: Payload) -> None:
    """Submit one forecast; raises SubmitError on rejection."""
    _request("POST", "questions/forecast/", payload.body())


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
    """
    ps = [p for p, _ in knots]
    xs = [v for _, v in knots]
    if x <= xs[0]:
        scale = ps[0] * (xs[1] - xs[0]) / (ps[1] - ps[0])
        return ps[0] * math.exp((x - xs[0]) / scale)
    if x >= xs[-1]:
        scale = (1 - ps[-1]) * (xs[-1] - xs[-2]) / (ps[-1] - ps[-2])
        return 1 - (1 - ps[-1]) * math.exp(-(x - xs[-1]) / scale)
    for i in range(len(xs) - 1):
        if xs[i] <= x <= xs[i + 1]:
            if xs[i + 1] == xs[i]:
                return ps[i + 1]
            return ps[i] + (ps[i + 1] - ps[i]) * (x - xs[i]) / (xs[i + 1] - xs[i])
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


def continuous_cdf(
    knots: list[tuple[float, float]], scaling: dict[str, Any]
) -> list[float]:
    """Metaculus CDF for a numeric or date question from quantile knots."""
    knots = sorted(knots)
    if len(knots) < 2:
        raise SubmitError("need at least two percentiles to build a CDF")
    if any(b[1] < a[1] for a, b in pairwise(knots)):
        raise SubmitError(f"percentile values are not monotone: {knots}")
    raw = [cdf_from_knots(x, knots) for x in _grid(scaling)]
    return _fit_to_bounds(raw, scaling)


def discrete_cdf(pmf: dict[str, float], scaling: dict[str, Any]) -> list[float]:
    """Metaculus CDF for a discrete question from a PMF keyed by outcome value.

    Every in-range outcome gets at least the minimum step, so a PMF that leaves
    a value at 0 still validates; the mass is then renormalised.
    """
    n = int(scaling["inbound_outcome_count"])
    edges = _grid(scaling)
    centres = [(a + b) / 2 for a, b in pairwise(edges)]
    table = {float(k): float(v) for k, v in pmf.items()}
    unknown = [k for k in table if not any(abs(k - c) < 1e-9 for c in centres)]
    if unknown:
        raise SubmitError(f"pmf keys {unknown} are not outcomes of this question")
    floor = MIN_STEP_PER_BIN / n * 1.1
    mass = [max(table.get(c, 0.0), floor) for c in centres]
    total = sum(mass)
    out, run = [0.0], 0.0
    for m in mass:
        run += m / total
        out.append(run)
    out[-1] = 1.0
    if scaling.get("open_lower_bound") or scaling.get("open_upper_bound"):
        return _fit_to_bounds(out, scaling)
    return out


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


def live_values(q: dict[str, Any]) -> list[float] | None:
    """The bot's current forecast on this question, as Metaculus stores it."""
    latest = (q.get("my_forecasts") or {}).get("latest")
    if not latest or latest.get("end_time"):
        return None
    return latest.get("forecast_values")


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
            post_forecast(payload)
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
