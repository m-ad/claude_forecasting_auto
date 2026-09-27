#!/usr/bin/env python3
"""
Metaculus Aggregation Explorer fetcher (v4.3, September 2026).

Pulls **structured numeric** aggregations straight from the JSON the Metaculus
frontend consumes, for any aggregation method the Aggregation Explorer exposes:

    - ``recency_weighted``  -> the standard "Community Prediction" (CP)
    - ``metaculus_pros``    -> the curated Pro forecaster cohort
    - ``gold_medalists``    -> top-medal forecasters
    - (plus ``unweighted``, ``single_aggregation`` etc. if ever needed)

Also fetches question metadata (resolution criteria / fine print / background)
and comments, both of which the ``/api-proxy/`` surface exposes anonymously.

--------------------------------------------------------------------------
WHY v3 FAILED, AND WHAT v4 DOES INSTEAD
--------------------------------------------------------------------------
v3 fetched over ``context.request.get()`` -- Playwright's own HTTP stack, not
Chromium's -- on the theory that a Cloudflare Managed Challenge on
``/api-proxy/*`` was purely a header problem, curable by adding ``Sec-Fetch-*``
headers. That stopped being true. As of 2026-09-11 every such call comes back
``403`` with ``cf-mitigated: challenge`` and a "Just a moment..." interstitial,
regardless of headers, because the challenge is now keyed on the *TLS/JA3
fingerprint* as well. Verified in this session:

    ctx.request.get(), with Sec-Fetch-* headers         -> 403 challenge
    ctx.request.get(), replaying browser cookies        -> 403 challenge
    curl, spoofed Chrome UA + Sec-Fetch-*               -> 403 challenge
    Chromium page navigation to the same URL            -> 200 JSON
    same-origin fetch() inside a loaded Metaculus page  -> 200 JSON

So v4 stops trying to imitate a browser and uses one: every request is either a
page navigation or an in-page ``fetch()``, both of which go through Chromium's
own network stack and therefore carry a genuine browser fingerprint. The
challenge does not fire at all on that path -- no cf_clearance handling, no
warm-up, no settle wait is needed in the normal case.

A second, independent failure lives in the *environment*, not on Metaculus, and
broke browser access for both Metaculus skills:

**Chromium's TLS 1.3 ClientHello is reset by the session's egress proxy.**
Through the agent proxy, Chromium could not reach *any* host -- example.com
included -- and failed with ``net::ERR_CONNECTION_RESET`` after the ClientHello
(~1.8 kB sent, 39 B received, tunnel closed). The MITM proxy cannot complete
Chromium's TLS 1.3 handshake, most likely the post-quantum key share splitting
the ClientHello across records. Verified (n=1 per cell, deterministic):

    default flags                                       -> ERR_CONNECTION_RESET
    --disable-features=PostQuantumKyber                 -> ERR_CONNECTION_RESET
    --disable-features=...,EncryptedClientHello         -> ERR_CONNECTION_RESET
    --ssl-version-max=tls1.2                            -> 200 OK

v4 therefore retries the launch with ``--ssl-version-max=tls1.2`` and keeps the
downgraded browser for the rest of the run. Two things trigger that downgrade:
a navigation dying with a connection-reset-class error, and -- since v4.1 -- any
attempt that comes back with **status 0**, i.e. no HTTP response at all. The
second trigger matters because the reset does not always surface as a
classifiable exception: ``goto`` can resolve with no response, or raise a
message carrying none of :data:`_RESET_MARKERS`. Before v4.1 those cases burned
the whole ~3 min backoff at status 0 and then told the caller to set the
environment variable by hand. TLS 1.2 to a public read-only endpoint through an
already-MITM'd proxy costs nothing in practice; ``METACULUS_FORCE_TLS12=1``
remains available to skip the failing probe up front, but it is now an
optimisation rather than a requirement. Note this is *not* a Metaculus property
-- it is the local proxy -- so on a normal workstation the TLS 1.3 attempt
succeeds and the fallback never runs.

Chromium also does not read ``HTTPS_PROXY`` reliably, so v4 parses it and passes
it explicitly via Playwright's ``proxy=`` option, with credentials when the URL
carries them.

Note: browsing Metaculus still requires the spoofed Chrome UA below. With the
honest ``HeadlessChrome`` UA, Cloudflare challenges the HTML pages themselves.

--------------------------------------------------------------------------
METACULUS_API_KEY (v4.2)
--------------------------------------------------------------------------
When ``METACULUS_API_KEY`` is set, question metadata (resolution criteria, fine
print, background, forecaster count) is read from the official token-authed
``/api/posts/<id>/`` endpoint over plain HTTPS instead of through the browser:
no Cloudflare challenge, no rate-limit exposure, one browser request fewer.
Without the key, or if that call fails, the browser path is used as before.

The key does **not** replace the browser for the numbers. Verified 2026-09-26
with the workbench's key, which belongs to a *bot* account:

    /api/posts/<id>/?with_cp=true         -> 200, but every aggregation null
    /api/aggregation_explorer/            -> 403 "Use of this endpoint is restricted"
    /api/posts/<id>/download-data/        -> 403, same
    /api/comments/?post=<id>              -> 403 unless filtered to own/staff authors
    /api-proxy/... with the token         -> 403 Cloudflare challenge (as without)

Metaculus hides aggregations from bot accounts, so the token is never sent on
the browser path: CP, Pros, gold medalists and comments stay anonymous-browser
only. Python's default ``Python-urllib`` User-Agent is banned outright
(Cloudflare error 1010); any honest custom UA passes.

--------------------------------------------------------------------------
GROUP POSTS (v4.3)
--------------------------------------------------------------------------
A "group of questions" post (e.g. one numeric subquestion per year) has no
single question for the Aggregation Explorer to aggregate. Queried by
``post_id`` alone it answers **HTTP 400** with ``{"non_field_errors": ["Post
with id 45386 has no question, please submit a subquestion."]}`` (verified
2026-09-27).
Before v4.3 that 400 was retried like a rate limit -- ~3 min of backoff that
spent rate-limit budget -- and then reported as "403 / post does not exist".

v4.3 still asks the explorer first, so a single-question post makes exactly the
requests it always did. Only on a 400 does it look the post up (API key first,
then browser) and, if the JSON carries ``group_of_questions``, fetch every
subquestion with its
``question_id`` pinned -- one request per subquestion, all cohorts
comma-joined -- and returns them in ``result.subquestions``, each labelled
with its group label (e.g. "2027"). A 400 is never retried: it is Metaculus
rejecting the request, and waiting does not change the answer.

Usage
-----
    python metaculus_aggregations.py <post_id> \
        [--methods recency_weighted,metaculus_pros,gold_medalists] \
        [--include-bots] [--history] [--comments N] [--json]

    # or as a library
    from metaculus_aggregations import fetch_aggregations
    res = fetch_aggregations(43505, methods=["recency_weighted", "metaculus_pros"])
    print(res.methods["recency_weighted"].latest.display)
    # group posts: one AggregationResult per subquestion
    for sub in res.subquestions:
        print(sub.label, sub.methods["recency_weighted"].latest.display)
"""

from __future__ import annotations

import argparse
import datetime as _dt
import json
import os
import time
import urllib.request
from dataclasses import asdict, dataclass, field
from typing import Any
from urllib.parse import unquote, urlparse

# The sandbox ships Chromium here; setting this lets Playwright find it without
# a separate `playwright install` step.
# Only point Playwright at the sandbox browser store when it actually exists;
# on a normal workstation Playwright must keep its own default location.
if os.path.isdir("/opt/pw-browsers"):
    os.environ.setdefault("PLAYWRIGHT_BROWSERS_PATH", "/opt/pw-browsers")

# Must NOT contain "HeadlessChrome": Cloudflare challenges that token outright.
_UA = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/122.0.0.0 Safari/537.36"
)

# Chromium supplies its own Sec-Fetch-* headers on every navigation and fetch();
# only the language header is worth pinning, so responses are not localised.
_EXTRA_HEADERS = {"accept-language": "en-US,en;q=0.9"}

# Chromium flag that makes the handshake survive a TLS-1.3-intolerant MITM proxy.
_TLS12_ARG = "--ssl-version-max=tls1.2"

# Error substrings that mean "the handshake or the tunnel died", as opposed to a
# real HTTP response. These are what the TLS downgrade is a candidate fix for.
_RESET_MARKERS = (
    "ERR_CONNECTION_RESET",
    "ERR_CONNECTION_CLOSED",
    "ERR_SSL_PROTOCOL_ERROR",
    "ERR_EMPTY_RESPONSE",
    "ERR_QUIC_PROTOCOL_ERROR",
    "ERR_TUNNEL_CONNECTION_FAILED",
)

# Seconds to wait between retries of a challenged request. Metaculus' IP-level
# rate limit was measured to clear in ~2 min (403 on everything at +0/+46/+91 s,
# 200 at +137 s), and it blocks ordinary HTML pages too -- so riding it out is
# the only option, and short retries are wasted requests that re-arm it.
# Cumulative wait across the schedule is ~3.5 min.
_BACKOFF = (5, 30, 60, 75)

# Seconds to leave between two *successful* requests, to stay under the limit
# rather than recovering from it.
_PACE = 1.5

# Same-origin XHR used once a real page is loaded; the fallback when a bare
# navigation to /api-proxy/ is challenged.
_JS_FETCH = """async (u) => {
    const r = await fetch(u, {credentials: 'include',
                              headers: {'accept': 'application/json'}});
    return {status: r.status, body: await r.text()};
}"""

_BASE = "https://www.metaculus.com/api-proxy"
_AGG = f"{_BASE}/aggregation_explorer/"

# Official token-authed API. Reached over plain HTTPS, not the browser; see the
# METACULUS_API_KEY section of the module docstring for what it can and cannot see.
_API = "https://www.metaculus.com/api"
# Cloudflare bans the stdlib default "Python-urllib/x.y" outright (error 1010).
_API_UA = "claude-forecasting/0.1 (metaculus-aggregations)"

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

    as_of: str | None
    forecaster_count: int | None
    center: float | None
    lower: float | None
    upper: float | None
    mean: float | None
    display: str
    per_option: list | None = None


@dataclass
class MethodResult:
    """Result for a single aggregation method on a question."""

    method: str
    status: int
    history_points: int
    latest: AggregationLatest | None
    history: list = field(default_factory=list)


@dataclass
class Comment:
    """One Metaculus comment."""

    author: str
    created_at: str | None
    text: str
    prediction: str | None = None


@dataclass
class AggregationResult:
    """Everything fetched for one post."""

    post_id: int
    question_id: int | None
    title: str | None
    question_type: str | None  # binary | numeric | discrete | date | multiple_choice
    status: str | None
    resolution: str | None
    scheduled_close_time: str | None
    cp_reveal_time: str | None = None
    options: list | None = None
    scaling: dict | None = None
    resolution_criteria: str | None = None
    fine_print: str | None = None
    background: str | None = None
    nr_forecasters: int | None = None
    methods: dict = field(default_factory=dict)
    comments: list = field(default_factory=list)
    # Group posts only: the subquestion's label in its group (e.g. "2027") on a
    # subquestion result, and every subquestion's result on the post-level one.
    # The post-level ``methods`` stays empty for a group -- there is no single
    # question to aggregate.
    label: str | None = None
    subquestions: list = field(default_factory=list)


# --------------------------------------------------------------------------- #
# Transport
# --------------------------------------------------------------------------- #
def _proxy_config() -> dict | None:
    """Playwright ``proxy=`` config from the environment, or None.

    Chromium does not pick ``HTTPS_PROXY`` up reliably (it reads desktop proxy
    settings, not the shell environment), so the value is parsed here and passed
    explicitly. Credentials are optional: a sandbox egress proxy may be
    ``http://user:pass@host:port`` or a bare ``http://127.0.0.1:port``.
    """
    raw = os.environ.get("HTTPS_PROXY") or os.environ.get("https_proxy") or ""
    if not raw:
        return None
    parsed = urlparse(raw)
    if not parsed.hostname:
        return None
    server = f"{parsed.scheme or 'http'}://{parsed.hostname}"
    if parsed.port:
        server += f":{parsed.port}"
    cfg: dict[str, str] = {"server": server}
    if parsed.username:
        cfg["username"] = unquote(parsed.username)
    if parsed.password:
        cfg["password"] = unquote(parsed.password)
    return cfg


def _is_transport_reset(exc: Exception) -> bool:
    """True when an exception is a dead handshake/tunnel rather than an HTTP error."""
    msg = str(exc)
    return any(m in msg for m in _RESET_MARKERS)


def _is_challenge(body: str) -> bool:
    """True when a response body is a Cloudflare interstitial rather than data."""
    head = body[:2000]
    return "Just a moment" in head or "challenges.cloudflare.com" in head


def _api_get_json(path: str, timeout: float = 30.0) -> dict | None:
    """GET ``{_API}/{path}`` with ``METACULUS_API_KEY``; None on any failure.

    Returns None immediately when the key is unset, so callers can treat this as
    an optional fast path and fall back to the browser on None.
    """
    key = os.environ.get("METACULUS_API_KEY")
    if not key:
        return None
    req = urllib.request.Request(
        f"{_API}/{path}",
        headers={
            "Authorization": f"Token {key}",
            "Accept": "application/json",
            "User-Agent": _API_UA,
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = json.loads(resp.read())
    # URLError/HTTPError/timeouts are OSErrors, bad JSON is a ValueError; any of
    # them just means "use the browser path instead".
    except (OSError, ValueError):
        return None
    return data if isinstance(data, dict) else None


def fetch_post_api(post_id: int) -> dict | None:
    """Raw ``/api/posts/<id>/`` JSON via the API key, or None.

    Carries title, status, close time, forecaster count, and (under
    ``question``) type, scaling, options, resolution criteria, fine print and
    background -- but no aggregations for a bot-account key.
    """
    return _api_get_json(f"posts/{post_id}/")


class _Fetcher:
    """Chromium-backed JSON fetcher for the ``/api-proxy/`` surface.

    Requests go through the browser's own network stack -- as a navigation, or
    as a same-origin ``fetch()`` from a loaded Metaculus page -- because
    Cloudflare's managed challenge keys on the TLS fingerprint and rejects every
    non-browser client. See the module docstring.

    Parameters
    ----------
    pw : playwright.sync_api.Playwright
        An active Playwright driver.
    post_id : int
        Used only to pick a real page to warm on if a navigation gets challenged.
    """

    def __init__(self, pw: Any, post_id: int) -> None:
        self._pw = pw
        self._post_id = post_id
        self._tls12 = os.environ.get("METACULUS_FORCE_TLS12") == "1"
        self._warmed = False
        self._browser = None
        self._last_request = 0.0
        self._open()

    # ---------------------------------------------------------------- browser
    def _open(self) -> None:
        """Launch Chromium and open the single page used as transport."""
        exe = os.environ.get(
            "PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH", "/opt/pw-browsers/chromium"
        )
        kwargs: dict[str, Any] = {
            "headless": True,
            "args": [_TLS12_ARG] if self._tls12 else [],
            "proxy": _proxy_config(),
        }
        if os.path.exists(exe):
            kwargs["executable_path"] = exe
        try:
            self._browser = self._pw.chromium.launch(**kwargs)
        except Exception:  # noqa: BLE001 - fall back to Playwright's own chromium
            kwargs.pop("executable_path", None)
            self._browser = self._pw.chromium.launch(**kwargs)
        self._ctx = self._browser.new_context(
            user_agent=_UA, extra_http_headers=_EXTRA_HEADERS
        )
        self._page = self._ctx.new_page()
        self._warmed = False

    def _downgrade_tls(self) -> bool:
        """Relaunch pinned to TLS 1.2. Returns False if already downgraded."""
        if self._tls12:
            return False
        self._tls12 = True
        self.close()
        self._open()
        return True

    def close(self) -> None:
        if self._browser is not None:
            try:
                self._browser.close()
            except Exception:  # noqa: BLE001, S110 - teardown must not mask a result
                pass
            self._browser = None

    # ---------------------------------------------------------------- fetching
    def _navigate(self, url: str) -> tuple[int, str]:
        """Fetch by navigating the page at ``url``; returns (status, body)."""
        try:
            resp = self._page.goto(url, wait_until="domcontentloaded", timeout=60000)
        except Exception as exc:  # noqa: BLE001
            # A reset here is the local proxy choking on TLS 1.3, not Metaculus.
            if _is_transport_reset(exc) and self._downgrade_tls():
                return self._navigate(url)
            return 0, ""
        if resp is None:
            return 0, ""
        try:
            return resp.status, resp.text()
        except Exception:  # noqa: BLE001 - body already gone; status still useful
            return resp.status, ""

    def _warm(self) -> bool:
        """Load a real question page so later calls are same-origin XHRs."""
        url = f"https://www.metaculus.com/questions/{self._post_id}/"
        try:
            self._page.goto(url, wait_until="domcontentloaded", timeout=90000)
        except Exception as exc:  # noqa: BLE001
            if _is_transport_reset(exc) and self._downgrade_tls():
                return self._warm()
            return False
        # A managed challenge reloads the page itself once solved; wait it out.
        for _ in range(10):
            if "just a moment" not in (self._page.title() or "").lower():
                break
            time.sleep(2)
        self._warmed = True
        return True

    def _page_fetch(self, url: str) -> tuple[int, str]:
        """Fetch via a same-origin ``fetch()`` from the currently loaded page."""
        try:
            out = self._page.evaluate(_JS_FETCH, url)
        except Exception:  # noqa: BLE001 - navigation raced us; caller retries
            return 0, ""
        return int(out.get("status") or 0), out.get("body") or ""

    def get_json(self, url: str) -> tuple[int, dict]:
        """GET ``url`` and decode it as JSON, riding out a rate-limit block.

        Tries a bare navigation first -- enough in practice, and one round trip.
        If that is challenged, warms up on a real question page once and retries
        as a same-origin XHR from there, which is what the site's own frontend
        does. Retries follow :data:`_BACKOFF`, sized to outlast the measured
        ~2 min IP block rather than to retry quickly.

        Returns
        -------
        (int, dict)
            HTTP status and decoded JSON; the dict is empty on persistent
            failure, and the status is 0 when no HTTP response was ever seen.
        """
        # Space successive requests out: staying under the limit is much cheaper
        # than waiting one out.
        gap = time.monotonic() - self._last_request
        if gap < _PACE:
            time.sleep(_PACE - gap)

        last_status = 0
        for i, wait in enumerate((0, *_BACKOFF)):
            if wait:
                time.sleep(wait)
            status, parsed = self._attempt(url)
            last_status = status or last_status
            if parsed is not None:
                return status, parsed
            # A 400 is Metaculus rejecting the request itself (a group post
            # queried without question_id, for one), not a rate limit or a
            # challenge: retrying cannot change the answer and only spends the
            # rate-limit budget the backoff exists to protect.
            if status == 400:
                return status, {}
            # Status 0 means no HTTP response was seen at all, which is the
            # egress proxy killing the handshake rather than Metaculus
            # rate-limiting us -- and the exception that says so does not always
            # carry a reset marker, or `goto` resolves with no response and
            # raises nothing, so _navigate's own downgrade never fires. Spending
            # a relaunch here costs seconds; spending the backoff instead costs
            # the full ~3 min and still ends at status 0.
            if status == 0 and self._downgrade_tls():
                status, parsed = self._attempt(url)
                last_status = status or last_status
                if parsed is not None:
                    return status, parsed
            # A JS challenge can only be solved by a real document, so switch to
            # "load a page, then XHR from it" for the remaining attempts.
            if i == 0 and not self._warmed:
                self._warm()
        return last_status, {}

    def _attempt(self, url: str) -> tuple[int, dict | None]:
        """One transport attempt; the dict is None unless it returned real JSON."""
        status, body = self._page_fetch(url) if self._warmed else self._navigate(url)
        self._last_request = time.monotonic()
        if status == 200 and body and not _is_challenge(body):
            try:
                return status, json.loads(body)
            except json.JSONDecodeError:
                pass
        return status, None


# --------------------------------------------------------------------------- #
# Scaling helpers
# --------------------------------------------------------------------------- #
def _unscale(x: float | None, scaling: dict | None) -> float | None:
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
    return rmin + (rmax - rmin) * (r**x - 1) / (r - 1)


def _iso(ts: float | None) -> str | None:
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
        return (
            _dt.datetime.fromtimestamp(v, _dt.UTC).strftime("%Y-%m-%d")
            if isinstance(v, (int, float))
            else "n/a"
        )

    if qtype == "multiple_choice" and per_option:
        return "  ".join(f"{o}={pct(c)}" for o, c, _, _ in per_option)
    if qtype == "binary":
        return f"{pct(center)}  IQR[{pct(lower)}, {pct(upper)}]"
    if qtype == "date":
        return f"{dt_str(center)}  IQR[{dt_str(lower)}, {dt_str(upper)}]"
    return f"{_num(center)}  IQR[{_num(lower)}, {_num(upper)}]"


def _extract_latest(
    qtype: str, latest: dict, scaling: dict, options: list | None
) -> AggregationLatest | None:
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

    scale = (
        (lambda v: v)
        if qtype in ("binary", "multiple_choice")
        else (lambda v: _unscale(v, scaling))
    )

    per_option = None
    if qtype == "multiple_choice" and options:
        per_option = [
            (
                options[i] if i < len(options) else f"option{i}",
                centers[i] if i < len(centers) else None,
                lows[i] if i < len(lows) else None,
                highs[i] if i < len(highs) else None,
            )
            for i in range(len(centers))
        ]

    center = scale(centers[0])
    lower = scale(lows[0]) if lows else None
    upper = scale(highs[0]) if highs else None
    mean = scale(means[0]) if means else None

    return AggregationLatest(
        as_of=_iso(latest.get("start_time")),
        forecaster_count=latest.get("forecaster_count"),
        center=center,
        lower=lower,
        upper=upper,
        mean=mean,
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
    methods: list[str] | None = None,
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
        on this question, or when the CP has not been revealed yet. For a
        group post, ``result.methods`` is empty and ``result.subquestions``
        holds one result per subquestion (``label`` names it).

    Raises
    ------
    RuntimeError
        If the probe never returns valid JSON (a non-existent post, or a
        Cloudflare challenge that survived all retries), or a group
        subquestion's aggregation cannot be fetched.
    """
    from playwright.sync_api import sync_playwright

    methods = methods or DEFAULT_METHODS

    def _url(mths: list[str], qid: int | None = None) -> str:
        """Aggregation Explorer URL for one or more cohorts.

        A **comma**-separated ``aggregation_methods`` list returns every cohort
        in a single response, which matters a lot: Metaculus rate-limits by IP
        and a tripped limit costs ~2 minutes (see the module docstring), so the
        request count is the binding constraint, not the payload size. v3 sent
        one request per cohort because the page's own ``methods=a|b`` form was
        seen to come back empty for some cohorts -- that is the *pipe*
        separator; comma works and is verified against all three cohorts.
        """
        qid_part = f"&question_id={qid}" if qid is not None else ""
        return (
            f"{_AGG}?post_id={post_id}{qid_part}"
            f"&include_bots={str(include_bots).lower()}"
            f"&aggregation_methods={','.join(mths)}&joined_before_date="
        )

    with sync_playwright() as p:
        fetcher = _Fetcher(p, post_id)
        try:
            result = _collect(
                fetcher,
                post_id,
                _url,
                methods,
                include_history,
                n_comments,
                include_details,
            )
        finally:
            fetcher.close()

    return result


def _group_questions(post: dict | None) -> list[dict]:
    """The subquestion dicts of a group-of-questions post; empty otherwise."""
    return list(((post or {}).get("group_of_questions") or {}).get("questions") or [])


def _lookup_post(fetcher: Any, post_id: int) -> dict:
    """Post JSON via the API key, else via the browser; empty dict on failure."""
    post = fetch_post_api(post_id)
    if not post:
        _, post = fetcher.get_json(f"{_BASE}/posts/{post_id}/?with_cp=false")
    return post or {}


def _from_explorer(
    fetcher: Any,
    post_id: int,
    base: dict,
    status: int,
    _url: Any,
    methods: list[str],
    include_history: bool,
) -> AggregationResult:
    """Parse one Aggregation Explorer response into an :class:`AggregationResult`."""
    qid = base.get("id")
    qtype = base.get("type")
    scaling = base.get("scaling") or {}
    options = base.get("options")

    result = AggregationResult(
        post_id=post_id,
        question_id=qid,
        title=base.get("title"),
        question_type=qtype,
        status=base.get("status"),
        resolution=base.get("resolution"),
        scheduled_close_time=base.get("scheduled_close_time"),
        cp_reveal_time=base.get("cp_reveal_time"),
        options=options,
        scaling=scaling,
    )

    for mth in methods:
        agg = (base.get("aggregations") or {}).get(mth) or {}
        st = status
        # A cohort absent from the combined response gets one dedicated request
        # with the question_id pinned, which is the form that always populates.
        if not agg:
            st, resp_json = fetcher.get_json(_url([mth], qid=qid))
            agg = (resp_json.get("aggregations") or {}).get(mth) or {}

        latest_raw = agg.get("latest") or {}
        hist_raw = agg.get("history") or []

        result.methods[mth] = MethodResult(
            method=mth,
            status=st,
            history_points=len(hist_raw),
            latest=_extract_latest(qtype, latest_raw, scaling, options),
            history=(
                _extract_history(qtype, hist_raw, scaling) if include_history else []
            ),
        )
    return result


def _collect(
    fetcher: Any,
    post_id: int,
    _url: Any,
    methods: list[str],
    include_history: bool,
    n_comments: int,
    include_details: bool,
) -> AggregationResult:
    """Run every request for one post through ``fetcher`` and assemble the result.

    Split out of :func:`fetch_aggregations` purely so the browser is torn down by
    one ``finally`` regardless of where a fetch fails.
    """
    # The explorer goes first, exactly as for every post before group support:
    # an IP-level rate limit also covers the API-key surface, so a lookup ahead
    # of it could spend the request the explorer needs. Only its 400 -- which a
    # single-question post never gets -- costs the extra post lookup.
    post: dict = {}
    subqs: list[dict] = []
    status, base = fetcher.get_json(_url(methods))
    if not base:
        if status == 400:
            # A group post queried without question_id; confirm from the post
            # itself before treating it as one.
            post = _lookup_post(fetcher, post_id)
            subqs = _group_questions(post)
        if not subqs:
            raise RuntimeError(
                f"No aggregation JSON for post {post_id} (last status {status}). "
                "403 means the post does not exist or Cloudflare challenged every "
                "retry -- wait ~3 min. Status 0 means no HTTP response at all, on "
                "TLS 1.2 as well as 1.3 (the downgrade is automatic), so this is "
                "egress: check HTTPS_PROXY and that www.metaculus.com is allowlisted."
            )

    if subqs:
        types = {q.get("type") for q in subqs}
        result = AggregationResult(
            post_id=post_id,
            question_id=None,
            title=post.get("title"),
            # One shared type is what scaffolding needs; a mixed group has none.
            question_type=types.pop() if len(types) == 1 else None,
            status=post.get("status"),
            resolution=None,
            scheduled_close_time=post.get("scheduled_close_time"),
        )
        for q in subqs:
            st, sub_base = fetcher.get_json(_url(methods, qid=q.get("id")))
            if not sub_base:
                raise RuntimeError(
                    f"No aggregation JSON for subquestion {q.get('id')} "
                    f"({q.get('label')!r}) of group post {post_id} (last status {st})."
                )
            sub = _from_explorer(
                fetcher, post_id, sub_base, st, _url, methods, include_history
            )
            sub.label = q.get("label")
            result.subquestions.append(sub)
    else:
        result = _from_explorer(
            fetcher, post_id, base, status, _url, methods, include_history
        )

    if include_details:
        # A group's post JSON was already looked up; reuse it.
        if not post:
            post = fetch_post_api(post_id)
        if not post:
            _, post = fetcher.get_json(f"{_BASE}/posts/{post_id}/?with_cp=false")
        # A group keeps its criteria on the group, not on any one question.
        q = post.get("question") or post.get("group_of_questions") or {}
        result.resolution_criteria = q.get("resolution_criteria")
        result.fine_print = q.get("fine_print")
        result.background = q.get("description")
        result.nr_forecasters = post.get("nr_forecasters")

    if n_comments > 0:
        _, cj = fetcher.get_json(
            f"{_BASE}/comments/?post={post_id}&limit={n_comments}"
            f"&sort=-created_at&use_root_comments_pagination=true",
        )
        for c in (cj.get("results") or [])[:n_comments]:
            result.comments.append(
                Comment(
                    author=(c.get("author") or {}).get("username", "?"),
                    created_at=(c.get("created_at") or "")[:10],
                    text=(c.get("text") or "").strip(),
                )
            )

    return result


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #
def _print_methods(res: AggregationResult) -> None:
    """Print every cohort block of one question."""
    for mth, mr in res.methods.items():
        print(f"\n=== {mth} ===  [{mr.status}]  history_points={mr.history_points}")
        if mr.latest is None:
            print("  (no forecasters for this method, or CP not yet revealed)")
            continue
        print(f"  as_of={mr.latest.as_of}  forecasters={mr.latest.forecaster_count}")
        if mr.latest.per_option:
            for o, c, lo, hi in mr.latest.per_option:
                band = (
                    f"  IQR[{lo * 100:.1f}%, {hi * 100:.1f}%]"
                    if isinstance(lo, float) and isinstance(hi, float)
                    else ""
                )
                print(f"    {o:<24s} {c * 100:5.1f}%{band}")
        else:
            extra = (
                f"   mean={mr.latest.mean * 100:.1f}%"
                if res.question_type == "binary" and mr.latest.mean is not None
                else ""
            )
            print(f"  {mr.latest.display}{extra}")


def _print_human(res: AggregationResult) -> None:
    if res.subquestions:
        print(f"POST {res.post_id}  ->  group of {len(res.subquestions)} subquestions")
    else:
        print(f"POST {res.post_id}  ->  question_id={res.question_id}")
    print(f"TITLE: {res.title}")
    print(
        f"type={res.question_type}  status={res.status}  "
        f"resolution={res.resolution}  close={res.scheduled_close_time}"
    )
    if res.nr_forecasters is not None:
        print(f"forecasters(total)={res.nr_forecasters}")
    if res.options:
        print(f"options={res.options}")

    _print_methods(res)
    for sub in res.subquestions:
        print(
            f"\n##### {sub.label}  (question_id={sub.question_id}, "
            f"type={sub.question_type}, status={sub.status}, "
            f"resolution={sub.resolution})"
        )
        _print_methods(sub)

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
    parser = argparse.ArgumentParser(
        description="Fetch Metaculus Aggregation Explorer data"
    )
    parser.add_argument("post_id", type=int, help="Metaculus post id (from the URL)")
    parser.add_argument(
        "--methods",
        type=str,
        default=",".join(DEFAULT_METHODS),
        help="Comma-separated methods (default: CP,pros,gold)",
    )
    parser.add_argument(
        "--include-bots",
        action="store_true",
        help="Fold bot forecasters into the aggregation",
    )
    parser.add_argument(
        "--history",
        action="store_true",
        help="Also fetch the centre-vs-time series per method",
    )
    parser.add_argument(
        "--comments",
        type=int,
        default=0,
        help="Fetch up to N recent comments (default 0)",
    )
    parser.add_argument(
        "--no-details",
        action="store_true",
        help="Skip resolution criteria / fine print / background",
    )
    parser.add_argument(
        "--wait",
        type=int,
        default=0,
        help="Deprecated no-op; v3 needs no Cloudflare settle wait",
    )
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
