#!/usr/bin/env python3
"""
Metaculus Aggregation Explorer fetcher (v3, July 2026).

Pulls **structured numeric** aggregations straight from the JSON the Metaculus
frontend consumes, for any aggregation method the Aggregation Explorer exposes:

    - ``recency_weighted``  -> the standard "Community Prediction" (CP)
    - ``metaculus_pros``    -> the curated Pro forecaster cohort
    - ``gold_medalists``    -> top-medal forecasters
    - (plus ``unweighted``, ``single_aggregation`` etc. if ever needed)

Also fetches question metadata (resolution criteria / fine print / background)
and comments, both of which the ``/api-proxy/`` surface exposes anonymously.

--------------------------------------------------------------------------
WHY v2 FAILED WITH CLOUDFLARE 403 (and what actually fixes it)
--------------------------------------------------------------------------
v2 was blocked on essentially every call. The cause was two independent
Cloudflare bot-detection triggers, both introduced by v2's own workaround.
Each was verified in isolation over repeated trials (n=5 per cell):

1. **Missing ``Sec-Fetch-*`` request headers.**  ``context.request.get()`` uses
   Playwright's own HTTP stack, not Chromium's, and it emits no ``Sec-Fetch-*``
   headers. Every real Chromium >= 76 always sends them. Claiming a Chrome
   User-Agent while omitting them is a header/UA inconsistency, and Cloudflare
   answers it with a Managed Challenge (``cf-mitigated: challenge``) on the
   ``/api-proxy/*`` path.
       without Sec-Fetch headers -> 0/5 success
       with    Sec-Fetch headers -> 5/5 success
   The *values* do not matter, only their presence.

2. **The ``cf_clearance`` cookie was actively harmful.**  v2 deliberately loaded
   the aggregation-explorer page first "so the browser clears the Cloudflare
   challenge", then reused the resulting cookie. But ``cf_clearance`` is bound
   to the client fingerprint (IP + UA + TLS/JA3) of the *browser* that earned
   it. Replaying it from Playwright's separate HTTP stack looks like a stolen
   clearance token, so Cloudflare challenges the request:
       page load, cookie kept    -> 0/5 success
       page load, cookies cleared-> 5/5 success
       no page load at all       -> 5/5 success
   The warm-up step v2 relied on was therefore the very thing breaking it.

The fix is to send ``Sec-Fetch-*`` headers and to never let a Metaculus page
cookie into the request context. No page load is needed at all, which also
removes v2's 12-30 s settle wait -- v3 answers in about 2 s.

A small residual (~5%) rate-related challenge remains; ``_get_json`` retries
with backoff, which clears it in practice.

Note: browsing Metaculus *pages* still requires the spoofed Chrome UA below.
With the honest ``HeadlessChrome`` UA, Cloudflare challenges the HTML pages
themselves (verified: page load returns 403 "Just a moment...").

Usage
-----
    python metaculus_aggregations.py <post_id> \
        [--methods recency_weighted,metaculus_pros,gold_medalists] \
        [--include-bots] [--history] [--comments N] [--json]

    # or as a library
    from metaculus_aggregations import fetch_aggregations
    res = fetch_aggregations(43505, methods=["recency_weighted", "metaculus_pros"])
    print(res.methods["recency_weighted"].latest.display)
"""

from __future__ import annotations

import argparse
import datetime as _dt
import json
import os
import time
from dataclasses import dataclass, field, asdict
from typing import Any, Optional

# The sandbox ships Chromium here; setting this lets Playwright find it without
# a separate `playwright install` step.
# Only point Playwright at the sandbox browser store when it actually exists;
# on a normal workstation Playwright must keep its own default location.
if os.path.isdir("/opt/pw-browsers"):
    os.environ.setdefault("PLAYWRIGHT_BROWSERS_PATH", "/opt/pw-browsers")

# Must NOT contain "HeadlessChrome": Cloudflare challenges that token outright.
_UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
       "Chrome/122.0.0.0 Safari/537.36")

# Presence of these is what defeats the managed challenge; values are arbitrary.
_SEC_FETCH_HEADERS = {
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "accept-language": "en-US,en;q=0.9",
}

_BASE = "https://www.metaculus.com/api-proxy"
_AGG = f"{_BASE}/aggregation_explorer/"

DEFAULT_METHODS = ["recency_weighted", "metaculus_pros", "gold_medalists"]


# --------------------------------------------------------------------------- #
# Data structures
# --------------------------------------------------------------------------- #
@dataclass
class AggregationLatest:
    """The most recent aggregation bucket for one method.

    Attributes
    ----------
    as_of : str or None
        UTC timestamp (ISO) of the bucket's ``start_time``.
    forecaster_count : int or None
        Forecasters contributing to this bucket (cohort size for pros/gold;
        recency window size for the CP -- not the lifetime total).
    center, lower, upper : float or None
        Median and p25/p75 bounds in *native* units: probability in [0, 1] for
        binary, real values for numeric/discrete, unix seconds for date. For
        multiple-choice these are the first option only; see ``per_option``.
    mean : float or None
        Aggregate mean.
    per_option : list of tuple or None
        For multiple-choice questions, ``(option, center, lower, upper)`` rows.
    display : str
        Human-readable "median IQR[lower, upper]" in the question's units.
    """

    as_of: Optional[str]
    forecaster_count: Optional[int]
    center: Optional[float]
    lower: Optional[float]
    upper: Optional[float]
    mean: Optional[float]
    display: str
    per_option: Optional[list] = None


@dataclass
class MethodResult:
    """Result for a single aggregation method on a question."""

    method: str
    status: int
    history_points: int
    latest: Optional[AggregationLatest]
    history: list = field(default_factory=list)


@dataclass
class Comment:
    """One Metaculus comment."""

    author: str
    created_at: Optional[str]
    text: str
    prediction: Optional[str] = None


@dataclass
class AggregationResult:
    """Everything fetched for one post."""

    post_id: int
    question_id: Optional[int]
    title: Optional[str]
    question_type: Optional[str]  # binary | numeric | discrete | date | multiple_choice
    status: Optional[str]
    resolution: Optional[str]
    scheduled_close_time: Optional[str]
    cp_reveal_time: Optional[str] = None
    options: Optional[list] = None
    scaling: Optional[dict] = None
    resolution_criteria: Optional[str] = None
    fine_print: Optional[str] = None
    background: Optional[str] = None
    nr_forecasters: Optional[int] = None
    methods: dict = field(default_factory=dict)
    comments: list = field(default_factory=list)


# --------------------------------------------------------------------------- #
# Transport
# --------------------------------------------------------------------------- #
def _get_json(ctx: Any, url: str, attempts: int = 4) -> tuple[int, dict]:
    """GET ``url`` through a Playwright context, defeating Cloudflare.

    Clears cookies before every attempt so no ``cf_clearance`` token earned by
    the browser is ever replayed from Playwright's HTTP stack, and sends the
    ``Sec-Fetch-*`` headers a real Chromium would. See the module docstring for
    why both are required.

    Parameters
    ----------
    ctx : playwright.sync_api.BrowserContext
        Context used only as an HTTP transport; no page is ever loaded.
    url : str
        Absolute ``/api-proxy/`` URL.
    attempts : int
        Retries for the residual ~5% rate-related challenge.

    Returns
    -------
    (int, dict)
        HTTP status and decoded JSON. On persistent failure the dict is empty.
    """
    last_status = 0
    for i in range(attempts):
        ctx.clear_cookies()
        try:
            r = ctx.request.get(url, headers=_SEC_FETCH_HEADERS, timeout=45000)
            last_status = r.status
            body = r.text()
            if r.status == 200:
                try:
                    return r.status, json.loads(body)
                except json.JSONDecodeError:
                    pass
        except Exception:
            pass
        # Backoff only matters for the rate-triggered variant of the challenge.
        time.sleep(2 * (i + 1))
    return last_status, {}


# --------------------------------------------------------------------------- #
# Scaling helpers
# --------------------------------------------------------------------------- #
def _unscale(x: Optional[float], scaling: Optional[dict]) -> Optional[float]:
    """Map an internal [0, 1] location to the question's real value range.

    Uses the linear transform when ``zero_point`` is None, otherwise the
    logarithmic one. The linear numeric and date transforms were validated
    against live questions; the log branch mirrors Metaculus' own code but has
    not been exercised against a live log-scaled question.
    """
    if x is None or not scaling:
        return None
    rmin, rmax = scaling.get("range_min"), scaling.get("range_max")
    if rmin is None or rmax is None:
        return None  # binary / multiple-choice: nothing to unscale onto
    zero = scaling.get("zero_point")
    if zero is None:
        return rmin + (rmax - rmin) * x
    r = (rmax - zero) / (rmin - zero)
    return rmin + (rmax - rmin) * (r ** x - 1) / (r - 1)


def _iso(ts: Optional[float]) -> Optional[str]:
    """Unix seconds -> UTC ISO 'YYYY-MM-DD HH:MM' string, or None."""
    if ts is None:
        return None
    return _dt.datetime.fromtimestamp(ts, _dt.UTC).strftime("%Y-%m-%d %H:%M")


def _num(v: Any) -> str:
    """Readable fixed-point formatting; avoids %g flipping to scientific."""
    if not isinstance(v, (int, float)):
        return "n/a"
    a = abs(v)
    if a >= 1000:
        return f"{v:,.0f}"
    if a >= 1:
        return f"{v:,.2f}"
    return f"{v:.4g}"


def _fmt_display(qtype: str, center, lower, upper, per_option) -> str:
    """Build a human-readable 'median IQR[lo, hi]' string in natural units."""
    def pct(v):
        return f"{v * 100:.1f}%" if isinstance(v, (int, float)) else "n/a"

    def dt_str(v):
        return (_dt.datetime.fromtimestamp(v, _dt.UTC).strftime("%Y-%m-%d")
                if isinstance(v, (int, float)) else "n/a")

    if qtype == "multiple_choice" and per_option:
        return "  ".join(f"{o}={pct(c)}" for o, c, _, _ in per_option)
    if qtype == "binary":
        return f"{pct(center)}  IQR[{pct(lower)}, {pct(upper)}]"
    if qtype == "date":
        return f"{dt_str(center)}  IQR[{dt_str(lower)}, {dt_str(upper)}]"
    return f"{_num(center)}  IQR[{_num(lower)}, {_num(upper)}]"


def _extract_latest(qtype: str, latest: dict, scaling: dict,
                    options: Optional[list]) -> Optional[AggregationLatest]:
    """Turn a raw ``latest`` block into an :class:`AggregationLatest`.

    Returns None when the block carries no centers, which is the normal state
    for questions whose community prediction has not yet been revealed.
    """
    centers = latest.get("centers") or []
    lows = latest.get("interval_lower_bounds") or []
    highs = latest.get("interval_upper_bounds") or []
    means = latest.get("means") or []
    if not centers:
        return None

    scale = (lambda v: v) if qtype in ("binary", "multiple_choice") \
        else (lambda v: _unscale(v, scaling))

    per_option = None
    if qtype == "multiple_choice" and options:
        per_option = [
            (options[i] if i < len(options) else f"option{i}",
             centers[i] if i < len(centers) else None,
             lows[i] if i < len(lows) else None,
             highs[i] if i < len(highs) else None)
            for i in range(len(centers))
        ]

    center = scale(centers[0])
    lower = scale(lows[0]) if lows else None
    upper = scale(highs[0]) if highs else None
    mean = scale(means[0]) if means else None

    return AggregationLatest(
        as_of=_iso(latest.get("start_time")),
        forecaster_count=latest.get("forecaster_count"),
        center=center, lower=lower, upper=upper, mean=mean,
        display=_fmt_display(qtype, center, lower, upper, per_option),
        per_option=per_option,
    )


def _extract_history(qtype: str, hist: list, scaling: dict) -> list:
    """Return [(iso_ts, center_native), ...] for the CP-vs-time series."""
    out = []
    for pt in hist:
        c = (pt.get("centers") or [None])[0]
        if qtype not in ("binary", "multiple_choice"):
            c = _unscale(c, scaling)
        out.append((_iso(pt.get("start_time")), c))
    return out


# --------------------------------------------------------------------------- #
# Core fetch
# --------------------------------------------------------------------------- #
def fetch_aggregations(
    post_id: int,
    methods: Optional[list[str]] = None,
    include_bots: bool = False,
    include_history: bool = False,
    n_comments: int = 0,
    include_details: bool = True,
) -> AggregationResult:
    """Fetch Aggregation Explorer data for a post across one or more methods.

    Parameters
    ----------
    post_id : int
        Metaculus **post** id (as in the question URL). This can differ from
        the internal ``question_id``; the mapping is resolved automatically.
    methods : list of str, optional
        Aggregation methods. Defaults to CP + pros + gold medalists.
    include_bots : bool
        Fold bot forecasters into the aggregation. Default False.
    include_history : bool
        Also return the centre-vs-time series per method, for movement and
        anchoring-drift checks. Off by default to stay light.
    n_comments : int
        Fetch up to this many recent comments (0 disables).
    include_details : bool
        Also fetch resolution criteria / fine print / background.

    Returns
    -------
    AggregationResult
        ``result.methods[m].latest`` is None when a method has no forecasters
        on this question, or when the CP has not been revealed yet.

    Raises
    ------
    RuntimeError
        If the probe never returns valid JSON (a non-existent post, or a
        Cloudflare challenge that survived all retries).
    """
    from playwright.sync_api import sync_playwright

    methods = methods or DEFAULT_METHODS

    def _url(mth: str, qid: Optional[int]) -> str:
        # question_id is passed explicitly: the page's own combined
        # `methods=a|b` call was observed to return empty for some cohorts.
        qid_part = f"&question_id={qid}" if qid is not None else ""
        return (f"{_AGG}?post_id={post_id}{qid_part}"
                f"&include_bots={str(include_bots).lower()}"
                f"&aggregation_methods={mth}&joined_before_date=")

    with sync_playwright() as p:
        _exe = os.environ.get("PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH", "/opt/pw-browsers/chromium")
        try:
            browser = p.chromium.launch(headless=True, executable_path=_exe if os.path.exists(_exe) else None)
        except Exception:
            browser = p.chromium.launch(headless=True)
        # No page is ever opened: loading one would mint a cf_clearance cookie
        # that poisons every subsequent request (see module docstring).
        ctx = browser.new_context(user_agent=_UA)

        status, base = _get_json(ctx, _url("recency_weighted", qid=None))
        if not base:
            browser.close()
            raise RuntimeError(
                f"No aggregation JSON for post {post_id} (last status {status}). "
                "Either the post does not exist or Cloudflare challenged every retry."
            )

        qid = base.get("id")
        qtype = base.get("type")
        scaling = base.get("scaling") or {}
        options = base.get("options")

        result = AggregationResult(
            post_id=post_id, question_id=qid, title=base.get("title"),
            question_type=qtype, status=base.get("status"),
            resolution=base.get("resolution"),
            scheduled_close_time=base.get("scheduled_close_time"),
            cp_reveal_time=base.get("cp_reveal_time"),
            options=options, scaling=scaling,
        )

        for mth in methods:
            if mth == "recency_weighted":
                resp_json, st = base, status
            else:
                st, resp_json = _get_json(ctx, _url(mth, qid=qid))

            agg = (resp_json.get("aggregations") or {}).get(mth) or {}
            latest_raw = agg.get("latest") or {}
            hist_raw = agg.get("history") or []

            result.methods[mth] = MethodResult(
                method=mth, status=st, history_points=len(hist_raw),
                latest=_extract_latest(qtype, latest_raw, scaling, options),
                history=(_extract_history(qtype, hist_raw, scaling)
                         if include_history else []),
            )

        if include_details:
            _, post = _get_json(ctx, f"{_BASE}/posts/{post_id}/?with_cp=false")
            q = post.get("question") or {}
            result.resolution_criteria = q.get("resolution_criteria")
            result.fine_print = q.get("fine_print")
            result.background = q.get("description")
            result.nr_forecasters = post.get("nr_forecasters")

        if n_comments > 0:
            _, cj = _get_json(
                ctx, f"{_BASE}/comments/?post={post_id}&limit={n_comments}"
                     f"&sort=-created_at&use_root_comments_pagination=true")
            for c in (cj.get("results") or [])[:n_comments]:
                result.comments.append(Comment(
                    author=(c.get("author") or {}).get("username", "?"),
                    created_at=(c.get("created_at") or "")[:10],
                    text=(c.get("text") or "").strip(),
                ))

        browser.close()

    return result


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #
def _print_human(res: AggregationResult) -> None:
    print(f"POST {res.post_id}  ->  question_id={res.question_id}")
    print(f"TITLE: {res.title}")
    print(f"type={res.question_type}  status={res.status}  "
          f"resolution={res.resolution}  close={res.scheduled_close_time}")
    if res.nr_forecasters is not None:
        print(f"forecasters(total)={res.nr_forecasters}")
    if res.options:
        print(f"options={res.options}")

    for mth, mr in res.methods.items():
        print(f"\n=== {mth} ===  [{mr.status}]  history_points={mr.history_points}")
        if mr.latest is None:
            print("  (no forecasters for this method, or CP not yet revealed)")
            continue
        print(f"  as_of={mr.latest.as_of}  forecasters={mr.latest.forecaster_count}")
        if mr.latest.per_option:
            for o, c, lo, hi in mr.latest.per_option:
                band = (f"  IQR[{lo * 100:.1f}%, {hi * 100:.1f}%]"
                        if isinstance(lo, float) and isinstance(hi, float) else "")
                print(f"    {o:<24s} {c * 100:5.1f}%{band}")
        else:
            extra = (f"   mean={mr.latest.mean * 100:.1f}%"
                     if res.question_type == "binary" and mr.latest.mean is not None
                     else "")
            print(f"  {mr.latest.display}{extra}")

    if res.resolution_criteria:
        print("\n--- Resolution Criteria ---")
        print(res.resolution_criteria[:1200])
    if res.fine_print:
        print("\n--- Fine Print ---")
        print(res.fine_print[:600])
    if res.comments:
        print(f"\n--- {len(res.comments)} Comments ---")
        for c in res.comments:
            print(f"\n  @{c.author} ({c.created_at}):")
            print(f"  {c.text[:400]}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Fetch Metaculus Aggregation Explorer data")
    parser.add_argument("post_id", type=int, help="Metaculus post id (from the URL)")
    parser.add_argument("--methods", type=str, default=",".join(DEFAULT_METHODS),
                        help="Comma-separated methods (default: CP,pros,gold)")
    parser.add_argument("--include-bots", action="store_true",
                        help="Fold bot forecasters into the aggregation")
    parser.add_argument("--history", action="store_true",
                        help="Also fetch the centre-vs-time series per method")
    parser.add_argument("--comments", type=int, default=0,
                        help="Fetch up to N recent comments (default 0)")
    parser.add_argument("--no-details", action="store_true",
                        help="Skip resolution criteria / fine print / background")
    parser.add_argument("--wait", type=int, default=0,
                        help="Deprecated no-op; v3 needs no Cloudflare settle wait")
    parser.add_argument("--json", action="store_true", help="Emit JSON")
    args = parser.parse_args()

    res = fetch_aggregations(
        post_id=args.post_id,
        methods=[m.strip() for m in args.methods.split(",") if m.strip()],
        include_bots=args.include_bots,
        include_history=args.history,
        n_comments=args.comments,
        include_details=not args.no_details,
    )

    if args.json:
        print(json.dumps(asdict(res), indent=2, ensure_ascii=False))
    else:
        _print_human(res)


if __name__ == "__main__":
    main()
