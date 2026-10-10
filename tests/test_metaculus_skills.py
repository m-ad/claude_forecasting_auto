"""Offline regression tests for the two Metaculus access skills.

Every fault that took these scripts down in September 2026 was a *launch or
transport* fault, not a parsing fault: Playwright could not find a browser, the
egress proxy was dropped because the URL carried no credentials, Chromium's
TLS 1.3 handshake was reset, and the Cloudflare challenge page was parsed as if
it were data. None of those need the network to test -- they are decisions the
scripts make before or around a request -- so they are pinned here. Anything
that genuinely needs Metaculus is left to manual verification; a test that hits
a rate-limited third party is a test that fails for the wrong reason.
"""

from __future__ import annotations

import copy
import importlib.util
import itertools
import sys
from pathlib import Path

import pytest
from conftest import REPO

SKILLS = REPO / ".claude" / "skills"


def _load(name: str, path: Path):
    """Import a skill script by absolute path (they are not importable packages)."""
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


@pytest.fixture(scope="module")
def agg():
    return _load(
        "metaculus_aggregations",
        SKILLS / "metaculus-aggregations" / "scripts" / "metaculus_aggregations.py",
    )


@pytest.fixture(scope="module")
def scrape():
    return _load(
        "metaculus_scrape",
        SKILLS / "metaculus-scraper" / "scripts" / "metaculus_scrape.py",
    )


# ------------------------------------------------------------------ proxy wiring
# The bug: a regex requiring user:pass@host:port silently returned {} for the
# credential-less agent proxy, so Chromium launched with no egress at all.
@pytest.mark.parametrize(
    "raw,expected_server,expected_user",
    [
        ("http://127.0.0.1:46351", "http://127.0.0.1:46351", None),
        ("http://proxy.internal:8080", "http://proxy.internal:8080", None),
        ("http://user:pw@proxy:3128", "http://proxy:3128", "user"),
        ("http://u%40corp:p%3Aw@proxy:3128", "http://proxy:3128", "u@corp"),
        ("https://secure-proxy:443", "https://secure-proxy:443", None),
    ],
)
def test_proxy_is_parsed_without_requiring_credentials(
    agg, scrape, monkeypatch, raw, expected_server, expected_user
):
    monkeypatch.setenv("HTTPS_PROXY", raw)
    monkeypatch.setenv("https_proxy", raw)
    for cfg in (agg._proxy_config(), scrape._parse_proxy()):
        assert cfg, f"{raw} must yield a proxy config, not {cfg!r}"
        assert cfg["server"] == expected_server
        if expected_user is None:
            assert "username" not in cfg
        else:
            assert cfg["username"] == expected_user


def test_no_proxy_env_means_direct_connection(agg, scrape, monkeypatch):
    # Outside a sandbox a direct connection is correct; neither script may invent
    # a proxy, and neither may raise.
    monkeypatch.delenv("HTTPS_PROXY", raising=False)
    monkeypatch.delenv("https_proxy", raising=False)
    assert agg._proxy_config() is None
    assert scrape._parse_proxy() == {}


# --------------------------------------------------------------- TLS 1.3 fallback
# The bug: Chromium could reach nothing at all through the egress proxy because
# the proxy resets its TLS 1.3 ClientHello. Recovery depends on classifying the
# error as transport-dead rather than as an HTTP failure.
@pytest.mark.parametrize(
    "msg",
    [
        "Page.goto: net::ERR_CONNECTION_RESET at https://www.metaculus.com/",
        "net::ERR_CONNECTION_CLOSED",
        "net::ERR_SSL_PROTOCOL_ERROR at https://www.metaculus.com/",
        "net::ERR_EMPTY_RESPONSE",
        "net::ERR_TUNNEL_CONNECTION_FAILED",
    ],
)
def test_transport_resets_are_recognised(agg, scrape, msg):
    assert agg._is_transport_reset(Exception(msg))
    assert scrape._is_transport_reset(Exception(msg))


@pytest.mark.parametrize(
    "msg",
    [
        "Timeout 60000ms exceeded",
        "Page.goto: net::ERR_NAME_NOT_RESOLVED",
        "403 Forbidden",
    ],
)
def test_non_transport_errors_do_not_trigger_a_tls_downgrade(agg, scrape, msg):
    # Downgrading TLS for an unrelated error would hide the real cause and waste
    # a launch, so the classifier has to stay narrow.
    assert not agg._is_transport_reset(Exception(msg))
    assert not scrape._is_transport_reset(Exception(msg))


def test_tls12_flag_is_the_exact_chromium_spelling(agg, scrape):
    # A typo here fails open: Chromium ignores unknown flags, so the handshake
    # would simply keep being reset with no error naming the flag.
    assert agg._TLS12_ARG == "--ssl-version-max=tls1.2"
    assert scrape._TLS12_ARG == agg._TLS12_ARG


# ------------------------------------------------------------ challenge handling
# The bug that matters most for forecast quality: a Cloudflare interstitial is a
# 403 HTML page. Treated as data it yields "no community prediction" instead of
# "blocked", which would enter the ledger as a real observation.
def test_cloudflare_interstitial_is_not_mistaken_for_data(agg):
    interstitial = (
        '<!DOCTYPE html><html lang="en-US"><head><title>Just a moment...</title>'
        '<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">'
        '<script src="https://challenges.cloudflare.com/turnstile/v0/api.js">'
    )
    assert agg._is_challenge(interstitial)


def test_real_aggregation_json_is_not_flagged_as_a_challenge(agg):
    body = '{"id": 40839, "title": "Will there be a ceasefire?", "type": "binary"}'
    assert not agg._is_challenge(body)


# --------------------------------------------------------------- request economy
# Metaculus rate-limits by IP and a tripped limit costs ~2 minutes, so the number
# of requests per run is the binding constraint. All cohorts must go out in one
# comma-separated request, not one request each.
def test_all_cohorts_are_requested_in_a_single_call(agg):
    captured: list[str] = []

    class FakeFetcher:
        def get_json(self, url):
            captured.append(url)
            return 200, {
                "id": 40839,
                "type": "binary",
                "scaling": {},
                "aggregations": {
                    m: {
                        "latest": {
                            "centers": [0.09],
                            "interval_lower_bounds": [0.05],
                            "interval_upper_bounds": [0.12],
                            "means": [0.1],
                            "forecaster_count": 7,
                            "start_time": 1_757_000_000,
                        },
                        "history": [],
                    }
                    for m in agg.DEFAULT_METHODS
                },
            }

    def url_for(methods, qid=None):
        return f"agg?methods={','.join(methods)}" + (f"&qid={qid}" if qid else "")

    res = agg._collect(
        FakeFetcher(),
        41138,
        url_for,
        agg.DEFAULT_METHODS,
        include_history=False,
        n_comments=0,
        include_details=False,
    )
    assert len(captured) == 1, f"one request expected, got {len(captured)}: {captured}"
    assert captured[0] == "agg?methods=recency_weighted,metaculus_pros,gold_medalists"
    # And every cohort must actually be parsed out of that single response.
    for m in agg.DEFAULT_METHODS:
        assert res.methods[m].latest is not None
        assert res.methods[m].latest.center == pytest.approx(0.09)


def test_a_cohort_missing_from_the_combined_response_gets_its_own_request(agg):
    # The combined form is an optimisation, not a guarantee: if Metaculus omits a
    # cohort, it must be re-requested with question_id pinned rather than
    # silently reported as "no forecasters".
    captured: list[str] = []

    class PartialFetcher:
        def get_json(self, url):
            captured.append(url)
            latest = {
                "centers": [0.09],
                "interval_lower_bounds": [0.05],
                "interval_upper_bounds": [0.12],
                "means": [0.1],
                "forecaster_count": 7,
                "start_time": 1_757_000_000,
            }
            if "qid" in url:  # the dedicated retry
                return 200, {"aggregations": {"gold_medalists": {"latest": latest}}}
            return 200, {
                "id": 40839,
                "type": "binary",
                "scaling": {},
                "aggregations": {"recency_weighted": {"latest": latest}},
            }

    def url_for(methods, qid=None):
        return f"agg?methods={','.join(methods)}" + (f"&qid={qid}" if qid else "")

    res = agg._collect(
        PartialFetcher(),
        41138,
        url_for,
        ["recency_weighted", "gold_medalists"],
        include_history=False,
        n_comments=0,
        include_details=False,
    )
    assert len(captured) == 2
    assert "qid=40839" in captured[1]
    assert res.methods["gold_medalists"].latest is not None


def test_backoff_outlasts_the_measured_rate_limit_block(agg, scrape):
    # The block was measured at ~2 min (403 at +0/+46/+91 s, 200 at +137 s).
    # A schedule shorter than that guarantees the failure it is meant to absorb.
    assert sum(agg._BACKOFF) >= 140, agg._BACKOFF
    assert sum(scrape._BACKOFF) >= 140, scrape._BACKOFF


# ------------------------------------------------------------------ user agent
def test_user_agent_never_advertises_headless(agg, scrape):
    # Cloudflare challenges the "HeadlessChrome" token outright, including on
    # ordinary HTML pages, so neither script may send it.
    assert "Headless" not in agg._UA
    assert "Headless" not in scrape._UA


# --------------------------------------------------------- scaling / formatting
# Unchanged by this fix, but the numbers they produce go straight into forecasts,
# so they are worth pinning while a regression suite is being written anyway.
def test_linear_unscale_maps_endpoints_and_midpoint(agg):
    scaling = {"range_min": 0.0, "range_max": 10.0, "zero_point": None}
    assert agg._unscale(0.0, scaling) == pytest.approx(0.0)
    assert agg._unscale(0.5, scaling) == pytest.approx(5.0)
    assert agg._unscale(1.0, scaling) == pytest.approx(10.0)


def test_log_unscale_is_monotonic_and_hits_its_endpoints(agg):
    scaling = {"range_min": 1.0, "range_max": 1000.0, "zero_point": 0.0}
    vals = [agg._unscale(x / 10, scaling) for x in range(11)]
    assert vals[0] == pytest.approx(1.0)
    assert vals[-1] == pytest.approx(1000.0)
    assert all(b > a for a, b in itertools.pairwise(vals))
    # Log scaling must bow below the linear midpoint, or it is not log scaling.
    assert vals[5] < 500.0


def test_binary_and_multiple_choice_are_never_unscaled(agg):
    assert agg._unscale(0.42, {}) is None
    assert agg._unscale(0.42, {"range_min": None, "range_max": None}) is None


def test_display_strings_use_each_question_type_s_own_units(agg):
    assert agg._fmt_display("binary", 0.089, 0.05, 0.12, None) == (
        "8.9%  IQR[5.0%, 12.0%]"
    )
    # 1 757 000 000 == 2025-09-04T15:33:20Z
    assert (
        agg._fmt_display("date", 1_757_000_000, 1_757_000_000, 1_757_000_000, None)[:10]
        == "2025-09-04"
    )
    assert agg._fmt_display("numeric", 1234.5, 1000.0, 1500.0, None) == (
        "1,234  IQR[1,000, 1,500]"
    )


def test_latest_block_without_centers_is_reported_as_unrevealed(agg):
    # An unrevealed CP must come back as None, not as 0%.
    assert agg._extract_latest("binary", {}, {}, None) is None
    assert agg._extract_latest("binary", {"centers": []}, {}, None) is None


# The bug this pins: the egress proxy's reset does not always arrive as a
# classifiable exception -- `goto` can resolve with no response object, or raise
# a message carrying none of `_RESET_MARKERS`. `_navigate` then returns status 0
# without downgrading, and the old `get_json` spent its whole ~3 min backoff
# re-issuing a request that could never be answered. Any status-0 attempt must
# now buy a TLS 1.2 relaunch instead of a backoff slot.
class _FakeFetcher:
    """Stands in for a `_Fetcher` whose transport is dead until TLS is downgraded."""

    def __init__(self, agg, payload):
        self._agg = agg
        self._payload = payload
        self.tls12 = False
        self.attempts = 0
        self.downgrades = 0
        self.warms = 0
        self._warmed = False
        self._last_request = 0.0

    def _attempt(self, url):
        self.attempts += 1
        if not self.tls12:  # no HTTP response at all while pinned to TLS 1.3
            return 0, None
        return 200, self._payload

    def _downgrade_tls(self):
        if self.tls12:
            return False
        self.tls12 = True
        self.downgrades += 1
        return True

    def _warm(self):
        self.warms += 1
        self._warmed = True
        return True


def test_status_zero_downgrades_tls_instead_of_spending_the_backoff(agg, monkeypatch):
    monkeypatch.setattr(agg.time, "sleep", lambda _s: None)
    fake = _FakeFetcher(agg, {"id": 1})
    status, body = agg._Fetcher.get_json(fake, "https://www.metaculus.com/api-proxy/x")

    assert (status, body) == (200, {"id": 1})
    assert fake.downgrades == 1
    # Two attempts: one dead on TLS 1.3, one good on TLS 1.2. Anything more means
    # the loop fell through to the backoff, which is the regression.
    assert fake.attempts == 2
    assert fake.warms == 0


def test_status_zero_downgrade_is_tried_only_once(agg, monkeypatch):
    # _downgrade_tls returning False (already downgraded, or METACULUS_FORCE_TLS12
    # was set) must not stop the normal backoff from running its course.
    monkeypatch.setattr(agg.time, "sleep", lambda _s: None)
    fake = _FakeFetcher(agg, {"id": 1})
    fake.tls12 = True  # already pinned; the relaunch cannot help
    fake._attempt = lambda _url: (0, None)

    status, body = agg._Fetcher.get_json(fake, "https://www.metaculus.com/api-proxy/x")
    assert (status, body) == (0, {})
    assert fake.downgrades == 0


def test_a_challenged_request_still_warms_on_a_real_page(agg, monkeypatch):
    # The pre-existing recovery path must survive the status-0 branch: a 403 is a
    # challenge, not a dead transport, so it warms rather than downgrading.
    monkeypatch.setattr(agg.time, "sleep", lambda _s: None)
    fake = _FakeFetcher(agg, {"id": 1})
    fake._attempt = lambda _url: (403, None)

    status, _ = agg._Fetcher.get_json(fake, "https://www.metaculus.com/api-proxy/x")
    assert status == 403
    assert fake.downgrades == 0
    assert fake.warms == 1


# ------------------------------------------------------------ METACULUS_API_KEY
# The key reads post metadata over plain HTTPS with no Cloudflare challenge, but
# a bot-account key sees null aggregations, so it may only ever *replace* the
# browser for details -- and must degrade to the browser when unset or failing.
class _FakeResponse:
    def __init__(self, payload: bytes):
        self._payload = payload

    def read(self) -> bytes:
        return self._payload

    def __enter__(self):
        return self

    def __exit__(self, *exc) -> None:
        return None


@pytest.fixture(params=["agg", "scrape"])
def api_get(request, agg, scrape):
    """Each script's API helper, called the same way: ``fn(post_id)``."""
    if request.param == "agg":
        return agg, agg.fetch_post_api
    return scrape, scrape._api_post


def test_no_api_key_means_no_api_request(api_get, monkeypatch):
    mod, fn = api_get
    monkeypatch.delenv("METACULUS_API_KEY", raising=False)

    def boom(*_a, **_k):
        raise AssertionError("urlopen must not be called without a key")

    monkeypatch.setattr(mod.urllib.request, "urlopen", boom)
    assert fn(41138) is None


def test_api_request_carries_the_token_and_an_unbanned_user_agent(api_get, monkeypatch):
    mod, fn = api_get
    monkeypatch.setenv("METACULUS_API_KEY", "k123")
    seen = {}

    def fake_urlopen(req, timeout=None):
        seen["url"] = req.full_url
        seen["auth"] = req.get_header("Authorization")
        seen["ua"] = req.get_header("User-agent")
        return _FakeResponse(b'{"id": 41138, "title": "T"}')

    monkeypatch.setattr(mod.urllib.request, "urlopen", fake_urlopen)
    assert fn(41138) == {"id": 41138, "title": "T"}
    assert seen["url"] == "https://www.metaculus.com/api/posts/41138/"
    assert seen["auth"] == "Token k123"
    # Cloudflare answers the stdlib default UA with error 1010.
    assert seen["ua"] and "Python-urllib" not in seen["ua"]


@pytest.mark.parametrize(
    "exc", [OSError("reset"), TimeoutError(), ValueError("not json")]
)
def test_api_failure_degrades_to_none(api_get, monkeypatch, exc):
    mod, fn = api_get
    monkeypatch.setenv("METACULUS_API_KEY", "k123")

    def fail(*_a, **_k):
        raise exc

    monkeypatch.setattr(mod.urllib.request, "urlopen", fail)
    assert fn(41138) is None


def _details_fetcher(captured: list[str]):
    class F:
        def get_json(self, url):
            captured.append(url)
            if "/posts/" in url:
                return 200, {
                    "nr_forecasters": 1,
                    "question": {"resolution_criteria": "browser"},
                }
            return 200, {"id": 40839, "type": "binary", "scaling": {}}

    return F()


def _collect_details(agg, fetcher):
    return agg._collect(
        fetcher,
        41138,
        lambda methods, qid=None: "agg",
        ["recency_weighted"],
        include_history=False,
        n_comments=0,
        include_details=True,
    )


def test_details_come_from_the_api_when_it_answers(agg, monkeypatch):
    monkeypatch.setattr(
        agg,
        "fetch_post_api",
        lambda _pid: {
            "nr_forecasters": 980,
            "question": {
                "resolution_criteria": "api",
                "fine_print": "fp",
                "description": "bg",
            },
        },
    )
    captured: list[str] = []
    res = _collect_details(agg, _details_fetcher(captured))
    assert not any("/posts/" in u for u in captured), "browser fetched details anyway"
    assert (res.resolution_criteria, res.fine_print, res.background) == (
        "api",
        "fp",
        "bg",
    )
    assert res.nr_forecasters == 980


def test_details_fall_back_to_the_browser_without_the_api(agg, monkeypatch):
    monkeypatch.setattr(agg, "fetch_post_api", lambda _pid: None)
    captured: list[str] = []
    res = _collect_details(agg, _details_fetcher(captured))
    assert any("/posts/" in u for u in captured)
    assert res.resolution_criteria == "browser"


# The bug: before a question opens (status "upcoming"), the bot-key /api/ endpoint
# answers 200 with title, type, options and dates but description, resolution
# criteria and fine print all null, while the anonymous /api-proxy/ post JSON
# carries the full text (verified 2026-10-09, post 45255). The non-empty API post
# was accepted as-is, so the criteria read as "not published".
_UPCOMING_API_POST = {
    "status": "approved",
    "nr_forecasters": 1,
    "question": {
        "status": "upcoming",
        "type": "multiple_choice",
        "description": None,
        "resolution_criteria": None,
        "fine_print": None,
    },
}


def test_textless_api_post_falls_back_to_the_browser_for_details(agg, monkeypatch):
    monkeypatch.setattr(agg, "fetch_post_api", lambda _pid: _UPCOMING_API_POST)
    captured: list[str] = []
    res = _collect_details(agg, _details_fetcher(captured))
    assert any("/posts/" in u for u in captured), "browser never fetched the text"
    assert res.resolution_criteria == "browser"


def test_textless_group_from_the_api_falls_back_to_the_browser(agg, monkeypatch):
    textless = copy.deepcopy(_GROUP_POST)
    for k in ("resolution_criteria", "fine_print", "description"):
        textless["group_of_questions"][k] = None
    monkeypatch.setattr(agg, "fetch_post_api", lambda _pid: textless)
    f = _GroupFetcher(post_via_browser=True)
    res = agg._collect(
        f,
        45386,
        _url_for,
        agg_methods(),
        include_history=False,
        n_comments=0,
        include_details=True,
    )
    assert sum("/posts/" in u for u in f.captured) == 1
    assert res.resolution_criteria == "group criteria"


def test_textless_api_post_keeps_its_fields_if_the_browser_also_fails(
    agg, monkeypatch
):
    # A failed browser fallback must not throw away what the API did return.
    monkeypatch.setattr(agg, "fetch_post_api", lambda _pid: _UPCOMING_API_POST)

    class F:
        def get_json(self, url):
            if "/posts/" in url:
                return 403, {}
            return 200, {"id": 45444, "type": "multiple_choice", "scaling": {}}

    res = _collect_details(agg, F())
    assert res.resolution_criteria is None
    assert res.nr_forecasters == 1


def test_scraper_prefers_api_text_over_the_page_parse(scrape, monkeypatch):
    page = "Title\n12 forecasters\nResolution Criteria\npage text\nComments\n"
    monkeypatch.setattr(scrape, "_render_page", lambda _pid, _w: ("Page T", page))
    monkeypatch.setattr(
        scrape,
        "_api_post",
        lambda _pid: {
            "title": "API T",
            "nr_forecasters": 980,
            "question": {"resolution_criteria": "api text", "fine_print": "fp"},
        },
    )
    res = scrape.scrape_metaculus_question(41138)
    assert (res.title, res.resolution_criteria, res.fine_print) == (
        "API T",
        "api text",
        "fp",
    )
    assert res.num_forecasters == "980"


def test_scraper_keeps_the_page_parse_without_the_api(scrape, monkeypatch):
    page = "Title\n12 forecasters\nResolution Criteria\npage text\nComments\n"
    monkeypatch.setattr(scrape, "_render_page", lambda _pid, _w: ("Page T", page))
    monkeypatch.setattr(scrape, "_api_post", lambda _pid: None)
    res = scrape.scrape_metaculus_question(41138)
    assert (res.title, res.resolution_criteria) == ("Page T", "page text")
    assert res.num_forecasters == "12"


# ----------------------------------------------------------------- group posts
# The bug: a group-of-questions post (one subquestion per year, say) has no single
# question for the Aggregation Explorer, which answers a post-only query with
# HTTP 400 (verified 2026-09-27, post 45386). The fetcher retried that 400 like a
# rate limit -- ~3 min of backoff spending rate-limit budget -- then reported it
# as "403 / post does not exist". A group must be fetched per subquestion.
def test_a_400_is_returned_at_once_not_retried(agg, monkeypatch):
    monkeypatch.setattr(
        agg.time, "sleep", lambda _s: pytest.fail("a 400 must not wait")
    )
    fake = _FakeFetcher(agg, {"id": 1})
    fake._attempt = lambda _url: (400, None)

    assert agg._Fetcher.get_json(fake, "https://www.metaculus.com/api-proxy/x") == (
        400,
        {},
    )
    assert (fake.warms, fake.downgrades) == (0, 0)


_GROUP_POST = {
    "id": 45386,
    "title": "Group title",
    "status": "open",
    "scheduled_close_time": "2028-07-01T00:00:00Z",
    "nr_forecasters": 5,
    "group_of_questions": {
        "resolution_criteria": "group criteria",
        "fine_print": "group fine print",
        "description": "group background",
        "questions": [
            {"id": 45576, "label": "2028", "type": "numeric"},
            {"id": 45575, "label": "2027", "type": "numeric"},
        ],
    },
}


def _explorer_json(qid: int, center: float) -> dict:
    """Explorer response for one numeric subquestion on a 0-200 range."""
    latest = {
        "centers": [center],
        "interval_lower_bounds": [center / 2],
        "interval_upper_bounds": [min(1.0, center * 1.5)],
        "means": [center],
        "forecaster_count": 5,
        "start_time": 1_758_000_000,
    }
    return {
        "id": qid,
        "type": "numeric",
        "title": f"q{qid}",
        "scaling": {"range_min": 0.0, "range_max": 200.0, "zero_point": None},
        "aggregations": {m: {"latest": latest, "history": []} for m in agg_methods()},
    }


def agg_methods() -> list[str]:
    return ["recency_weighted", "metaculus_pros", "gold_medalists"]


class _GroupFetcher:
    """Answers like Metaculus does for a group post."""

    def __init__(self, post_via_browser: bool):
        self.captured: list[str] = []
        self.post_via_browser = post_via_browser

    def get_json(self, url):
        self.captured.append(url)
        if "/posts/" in url:
            return (200, _GROUP_POST) if self.post_via_browser else (403, {})
        if "qid=45575" in url:
            return 200, _explorer_json(45575, 0.391)  # -> 78.2 on 0-200
        if "qid=45576" in url:
            return 200, _explorer_json(45576, 0.565)  # -> 113.0
        return 400, {}  # post-only query on a group post


def _url_for(methods, qid=None):
    return f"agg?methods={','.join(methods)}" + (f"&qid={qid}" if qid else "")


def _check_group_result(res):
    assert res.question_id is None
    assert res.methods == {}, "a group has no post-level aggregation"
    assert res.question_type == "numeric"
    assert [s.label for s in res.subquestions] == ["2028", "2027"]
    by_label = {s.label: s for s in res.subquestions}
    assert by_label["2027"].question_id == 45575
    for m in agg_methods():
        assert by_label["2027"].methods[m].latest.center == pytest.approx(78.2)
        assert by_label["2028"].methods[m].latest.center == pytest.approx(113.0)


def test_group_post_found_via_the_api_after_the_explorer_s_400(agg, monkeypatch):
    monkeypatch.setattr(agg, "fetch_post_api", lambda _pid: _GROUP_POST)
    f = _GroupFetcher(post_via_browser=False)
    res = agg._collect(
        f,
        45386,
        _url_for,
        agg_methods(),
        include_history=False,
        n_comments=0,
        include_details=True,
    )
    _check_group_result(res)
    # The post-only query once (its 400 is not retried), then exactly one request
    # per subquestion, all cohorts comma-joined, qid pinned. The API answered the
    # post lookup, so the browser never fetched the post.
    assert f.captured == [
        "agg?methods=recency_weighted,metaculus_pros,gold_medalists",
        "agg?methods=recency_weighted,metaculus_pros,gold_medalists&qid=45576",
        "agg?methods=recency_weighted,metaculus_pros,gold_medalists&qid=45575",
    ]
    assert (res.resolution_criteria, res.fine_print, res.background) == (
        "group criteria",
        "group fine print",
        "group background",
    )
    assert res.nr_forecasters == 5


def test_group_post_found_after_a_400_without_the_api(agg, monkeypatch):
    monkeypatch.setattr(agg, "fetch_post_api", lambda _pid: None)
    f = _GroupFetcher(post_via_browser=True)
    res = agg._collect(
        f,
        45386,
        _url_for,
        agg_methods(),
        include_history=False,
        n_comments=0,
        include_details=True,
    )
    _check_group_result(res)
    # The post JSON looked up after the 400 is reused for details, not refetched.
    assert sum("/posts/" in u for u in f.captured) == 1
    assert res.resolution_criteria == "group criteria"


def test_a_400_on_a_post_that_is_not_a_group_still_raises(agg, monkeypatch):
    monkeypatch.setattr(
        agg, "fetch_post_api", lambda _pid: {"id": 1, "question": {"id": 2}}
    )

    class F:
        def get_json(self, url):
            return 400, {}

    with pytest.raises(RuntimeError, match="last status 400"):
        agg._collect(
            F(),
            1,
            _url_for,
            agg_methods(),
            include_history=False,
            n_comments=0,
            include_details=False,
        )


def test_a_failed_subquestion_raises_rather_than_reading_as_no_forecasters(
    agg, monkeypatch
):
    monkeypatch.setattr(agg, "fetch_post_api", lambda _pid: _GROUP_POST)

    class F(_GroupFetcher):
        def get_json(self, url):
            if "qid=45575" in url:
                return 403, {}
            return super().get_json(url)

    with pytest.raises(RuntimeError, match="45575"):
        agg._collect(
            F(post_via_browser=False),
            45386,
            _url_for,
            agg_methods(),
            include_history=False,
            n_comments=0,
            include_details=True,
        )


def test_a_single_question_post_keeps_its_old_shape(agg):
    # Backward compatibility: ordinary posts still fill ``methods`` directly and
    # carry no subquestions, so existing callers see what they always saw.
    class F:
        def get_json(self, url):
            return 200, _explorer_json(40839, 0.5)

    res = agg._collect(
        F(),
        40839,
        _url_for,
        agg_methods(),
        include_history=False,
        n_comments=0,
        include_details=False,
    )
    assert res.question_id == 40839
    assert res.subquestions == [] and res.label is None
    assert res.methods["recency_weighted"].latest.center == pytest.approx(100.0)


def test_a_single_question_post_asks_the_explorer_before_the_api(agg, monkeypatch):
    # An IP-level rate limit covers the API-key surface too, so a post lookup
    # ahead of the explorer could spend the one request the explorer needs. Group
    # support must not reorder a single-question post's requests.
    order: list[str] = []

    def api(_pid):
        order.append("api")
        return {"nr_forecasters": 3, "question": {"resolution_criteria": "rc"}}

    monkeypatch.setattr(agg, "fetch_post_api", api)

    class F:
        def get_json(self, url):
            order.append("browser:" + url.split("?")[0])
            return 200, _explorer_json(40839, 0.5)

    agg._collect(
        F(),
        40839,
        _url_for,
        agg_methods(),
        include_history=False,
        n_comments=0,
        include_details=True,
    )
    assert order == ["browser:agg", "api"]


# The bug: with the Aggregation Explorer challenged on every retry while the
# /api-proxy/posts/ endpoint still answered (seen 2026-10-10, post 45860, from
# one warmed page), _collect raised before it ever looked the post up -- so an
# upcoming question's criteria were lost although they were one request away,
# and the explorer has nothing to add before the CP reveal anyway.
_UPCOMING_BROWSER_POST = {
    "id": 45860,
    "title": "Upcoming title",
    "status": "approved",
    "nr_forecasters": 1,
    "scheduled_close_time": "2026-12-15T13:00:00Z",
    "question": {
        "id": 46035,
        "status": "upcoming",
        "type": "binary",
        "cp_reveal_time": "2026-10-16T17:00:00Z",
        "resolution_criteria": "rc",
        "fine_print": "fp",
        "description": "bg",
    },
}


class _BlockedExplorer:
    """Explorer challenged on every retry; the post endpoint answers as given."""

    def __init__(self, post: dict | None):
        self.captured: list[str] = []
        self.post = post

    def get_json(self, url):
        self.captured.append(url)
        if "/posts/" in url:
            return (200, self.post) if self.post else (403, {})
        if "/comments/" in url:
            return 200, {"results": [{"author": {"username": "u"}, "text": "hi"}]}
        return 403, {}


def _collect_blocked(agg, fetcher, n_comments=0):
    return agg._collect(
        fetcher,
        45860,
        _url_for,
        agg_methods(),
        include_history=False,
        n_comments=n_comments,
        include_details=True,
    )


def test_blocked_explorer_on_an_upcoming_post_still_returns_its_criteria(
    agg, monkeypatch
):
    monkeypatch.setattr(agg, "fetch_post_api", lambda _pid: _UPCOMING_API_POST)
    f = _BlockedExplorer(_UPCOMING_BROWSER_POST)
    res = _collect_blocked(agg, f, n_comments=1)
    assert (res.resolution_criteria, res.fine_print, res.background) == (
        "rc",
        "fp",
        "bg",
    )
    assert res.methods == {}, "no cohort may be invented for a skipped explorer"
    assert res.aggregation_note and "upcoming" in res.aggregation_note
    assert (res.question_id, res.question_type, res.status) == (
        46035,
        "binary",
        "upcoming",
    )
    assert res.cp_reveal_time == "2026-10-16T17:00:00Z"
    assert [c.text for c in res.comments] == ["hi"]


def test_blocked_explorer_on_an_open_post_still_raises(agg, monkeypatch):
    # An open question's missing CP must stay an error, never a silent gap.
    open_post = copy.deepcopy(_UPCOMING_BROWSER_POST)
    open_post["question"]["status"] = "open"
    monkeypatch.setattr(agg, "fetch_post_api", lambda _pid: open_post)
    f = _BlockedExplorer(open_post)
    with pytest.raises(RuntimeError, match="last status 403"):
        _collect_blocked(agg, f)
    # The key answered with text, so no browser request was spent on the post.
    assert not any("/posts/" in u for u in f.captured)


def test_blocked_explorer_on_an_upcoming_post_without_text_still_raises(
    agg, monkeypatch
):
    # Null criteria read as "not published"; a failed fetch must say it failed.
    monkeypatch.setattr(agg, "fetch_post_api", lambda _pid: _UPCOMING_API_POST)
    with pytest.raises(RuntimeError, match="last status 403"):
        _collect_blocked(agg, _BlockedExplorer(None))


def test_an_answering_explorer_leaves_no_aggregation_note(agg):
    class F:
        def get_json(self, url):
            return 200, _explorer_json(40839, 0.5)

    res = agg._collect(
        F(),
        40839,
        _url_for,
        agg_methods(),
        include_history=False,
        n_comments=0,
        include_details=False,
    )
    assert res.aggregation_note is None
