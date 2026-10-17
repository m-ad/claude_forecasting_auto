#!/usr/bin/env python3
"""Token-authenticated client for the official Metaculus API -- the bot's only door.

Every Metaculus call this repository makes goes through this module, over plain
HTTPS with the bot account's token: no browser, no ``/api-proxy/``, no Aggregation
Explorer. Bot tokens cannot see community aggregations on tournament questions
anyway (Metaculus hides the CP from them on all but ~50 questions), so nothing here
asks for one.

The token is read from ``METACULUS_API_KEY`` (``METACULUS_TOKEN``, the name the
official bot template uses, is accepted too). It belongs to a registered **bot
account**; every forecast and comment posted with it is the bot's.

Error discipline -- this is the main source of runtime failure, so it is strict:

- ``429`` waits and retries (Metaculus rate-limits per IP).
- ``5xx`` and connection errors get **one** retry after a short pause.
- Any other ``4xx`` raises at once. A 400 is a malformed request; retrying it burns
  time to fail identically.
- A JSON ``401``/``403`` raises ``MetaculusAuthError``, which callers treat as fatal
  for the whole run. A Cloudflare challenge page is *not* an auth failure and raises
  a plain ``MetaculusError`` that says so.

Examples
--------
    uv run scripts/metaculus_api.py whoami
    uv run scripts/metaculus_api.py open minibench
    uv run scripts/metaculus_api.py post 46044
    uv run scripts/metaculus_api.py tournament minibench
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any
from urllib.parse import urlencode

sys.path.insert(0, str(Path(__file__).resolve().parent))
import _common  # noqa: F401  -- lenient stdio for the CLI

API = "https://www.metaculus.com/api"
# Cloudflare bans the stdlib default "Python-urllib/x.y" outright (error 1010).
USER_AGENT = "claude-forecasting-bot/1.0 (+https://github.com/m-ad/claude_forecasting_auto)"
TOKEN_ENVS = ("METACULUS_API_KEY", "METACULUS_TOKEN")
RETRY_429_S = (30.0, 60.0)
RETRY_5XX_S = (5.0,)
TIMEOUT_S = 60.0
# The question types the bot tournaments use (the resources page: "Only Binary,
# Numeric, Discrete, and Multiple Choice will be used").
FORECAST_TYPES = ("binary", "multiple_choice", "numeric", "discrete")
CLOSED_STATUSES = {"closed", "resolved", "deleted"}

_TOKEN_SHAPE = re.compile(r"(?i)(authorization:?\s*\"?token\s+)[A-Za-z0-9._-]+")


class MetaculusError(Exception):
    """A Metaculus call that failed; ``stage`` says which step, ``hint`` what to do.

    Parameters
    ----------
    stage : str
        The caller's step, e.g. ``"poll"`` or ``"submit"``.
    status : int or None
        HTTP status, or None for a transport failure.
    message : str
        What went wrong, already redacted.
    hint : str, optional
        The likely cause, for the run log.
    """

    def __init__(self, stage: str, status: int | None, message: str, hint: str = ""):
        self.stage, self.status, self.hint = stage, status, hint
        detail = f"[{stage}] HTTP {status}: {message}" if status else f"[{stage}] {message}"
        super().__init__(f"{detail} ({hint})" if hint else detail)


class MetaculusAuthError(MetaculusError):
    """The token was refused. Fatal for a whole run, never a per-question failure."""


def token() -> str | None:
    """The bot token from the environment, or None."""
    for name in TOKEN_ENVS:
        value = os.environ.get(name, "").strip()
        if value:
            return value
    return None


def redact(text: str) -> str:
    """Strip the token and anything token-shaped from text bound for a log or a file.

    API error bodies can echo request headers, and run logs and committed records
    outlive the token's secrecy (the repo may go public), so every message this
    module raises passes through here.
    """
    out = _TOKEN_SHAPE.sub(r"\1[REDACTED]", text)
    for name in (*TOKEN_ENVS, "CLAUDE_CODE_OAUTH_TOKEN"):
        secret = os.environ.get(name, "").strip()
        if len(secret) >= 8:
            out = out.replace(secret, "[REDACTED]")
    return out


def _is_challenge(body: str) -> bool:
    """True for a Cloudflare interstitial rather than an API answer."""
    low = body[:2000].lower()
    return "<html" in low and ("cloudflare" in low or "just a moment" in low)


def request(
    method: str,
    path: str,
    *,
    params: dict[str, Any] | None = None,
    body: Any = None,
    stage: str = "api",
) -> tuple[int, Any]:
    """Call the API and return ``(status, parsed JSON)``.

    Parameters
    ----------
    method : str
        ``"GET"`` or ``"POST"``.
    path : str
        Path below ``/api/``, e.g. ``"posts/46044/"``.
    params : dict, optional
        Query parameters; list values are repeated (``tournaments=a&tournaments=b``).
    body : Any, optional
        JSON body for a POST.
    stage : str
        Label carried by any error raised.

    Raises
    ------
    MetaculusAuthError
        The token is missing or was refused.
    MetaculusError
        Any other failure, after the retries described in the module docstring.
    """
    key = token()
    if not key:
        raise MetaculusAuthError(stage, None, "no token", f"set {TOKEN_ENVS[0]}")
    url = f"{API}/{path.lstrip('/')}"
    if params:
        url += "?" + urlencode(params, doseq=True)
    data = json.dumps(body).encode() if body is not None else None
    waits_429, waits_5xx = list(RETRY_429_S), list(RETRY_5XX_S)
    while True:
        req = urllib.request.Request(
            url,
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
            with urllib.request.urlopen(req, timeout=TIMEOUT_S) as resp:
                raw = resp.read()
                return resp.status, (json.loads(raw) if raw else {})
        except urllib.error.HTTPError as exc:
            text = redact(exc.read()[:800].decode("utf-8", "replace"))
            if exc.code == 429 and waits_429:
                wait = waits_429.pop(0)
                print(f"  (429 rate-limited; waiting {wait:.0f}s)", file=sys.stderr)
                time.sleep(wait)
                continue
            if exc.code >= 500 and waits_5xx:
                time.sleep(waits_5xx.pop(0))
                continue
            if exc.code in (401, 403) and not _is_challenge(text):
                raise MetaculusAuthError(
                    stage, exc.code, text, "token refused: regenerate it or re-check the secret"
                ) from None
            hint = "Cloudflare challenge, not an auth failure" if _is_challenge(text) else ""
            raise MetaculusError(
                stage, exc.code, text if not hint else "challenge page", hint
            ) from None
        except (urllib.error.URLError, OSError) as exc:
            if waits_5xx:
                time.sleep(waits_5xx.pop(0))
                continue
            raise MetaculusError(stage, None, redact(str(exc)), "network") from None


def get_json(path: str, params: dict[str, Any] | None = None, stage: str = "api") -> Any:
    """GET and return only the parsed body."""
    return request("GET", path, params=params, stage=stage)[1]


# ------------------------------------------------------------------ reads
def whoami() -> dict[str, Any]:
    """The account behind the token -- the gate's one cheap token check."""
    return get_json("users/me/", stage="auth")


def get_post(post_id: int, stage: str = "api") -> dict[str, Any]:
    """``/posts/<id>/`` as the bot, including its own ``my_forecasts``.

    The list endpoint omits ``my_forecasts``; this is the call that answers "has
    the bot already forecast this?" authoritatively.
    """
    return get_json(f"posts/{int(post_id)}/", stage=stage)


def get_tournament(slug: str) -> dict[str, Any]:
    """Tournament/series metadata (name, dates, question count) by slug or id."""
    return get_json(f"projects/tournaments/{slug}/", stage="tournament")


def list_posts(
    tournament: str | int,
    statuses: str = "open",
    page_size: int = 50,
    max_pages: int = 20,
    stage: str = "poll",
) -> list[dict[str, Any]]:
    """Every post in a tournament with the given status, following pagination.

    Parameters
    ----------
    tournament : str or int
        Tournament slug or id. ``"minibench"`` always names the current round.
    statuses : str
        Comma-separated post statuses, e.g. ``"open"`` or ``"closed,resolved"``.
    """
    out: list[dict[str, Any]] = []
    for page in range(max_pages):
        doc = get_json(
            "posts/",
            {
                "tournaments": [tournament],
                "statuses": statuses,
                "forecast_type": ",".join(FORECAST_TYPES),
                "order_by": "-open_time",
                "limit": page_size,
                "offset": page * page_size,
                "with_cp": "false",
            },
            stage=stage,
        )
        results = (doc or {}).get("results") or []
        out.extend(results)
        if not doc.get("next") or len(results) < page_size:
            break
    return out


# ------------------------------------------------------------------ writes
def forecast_body(question_id: int, values: dict[str, Any]) -> list[dict[str, Any]]:
    """The JSON body ``POST /questions/forecast/`` takes for one question.

    ``values`` carries exactly one of ``probability_yes`` (binary),
    ``probability_yes_per_category`` (multiple choice) or ``continuous_cdf``
    (numeric/discrete/date); the other two are sent as null, as the API expects.
    """
    return [
        {
            "question": int(question_id),
            "source": "api",
            "probability_yes": values.get("probability_yes"),
            "probability_yes_per_category": values.get("probability_yes_per_category"),
            "continuous_cdf": values.get("continuous_cdf"),
        }
    ]


def submit_forecast(question_id: int, values: dict[str, Any]) -> int:
    """POST one forecast; returns the HTTP status."""
    body = forecast_body(question_id, values)
    return request("POST", "questions/forecast/", body=body, stage="submit")[0]


def post_comment(post_id: int, text: str, private: bool = True) -> int:
    """POST the bot's rationale comment; returns the HTTP status.

    Bots must comment on every question they forecast, and Metaculus asks for
    private comments (``is_private``), which it makes public after the question
    closes. ``included_forecast`` attaches the bot's current forecast, so this goes
    *after* the forecast POST.
    """
    body = {
        "text": text,
        "parent": None,
        "included_forecast": True,
        "is_private": private,
        "on_post": int(post_id),
    }
    return request("POST", "comments/create/", body=body, stage="comment")[0]


# ------------------------------------------------------------------ helpers
def live_values(question: dict[str, Any]) -> list[float] | None:
    """The bot's current forecast on ``question`` as Metaculus stores it, or None.

    A ``latest`` with an ``end_time`` was withdrawn, which is not a live forecast.
    """
    latest = (question.get("my_forecasts") or {}).get("latest")
    if not latest or latest.get("end_time"):
        return None
    return latest.get("forecast_values")


def is_open(post: dict[str, Any], question: dict[str, Any] | None = None) -> bool:
    """True while the post (and its question) still accept forecasts."""
    q = question or post.get("question") or {}
    return post.get("status") == "open" and q.get("status", "open") == "open"


SNAPSHOT_QUESTION_KEYS = (
    "id",
    "title",
    "type",
    "status",
    "description",
    "resolution_criteria",
    "fine_print",
    "unit",
    "options",
    "scaling",
    "open_lower_bound",
    "open_upper_bound",
    "inbound_outcome_count",
    "open_time",
    "scheduled_close_time",
    "scheduled_resolve_time",
    "resolution",
)


def question_snapshot(post: dict[str, Any], question: dict[str, Any]) -> dict[str, Any]:
    """The part of a post the forecaster needs, for ``raw/metaculus-question-<date>.json``.

    Trimmed rather than cached whole: the forecaster reads this instead of calling
    Metaculus itself, and the full post carries per-user state (``my_forecasts``)
    that has no place in a committed file.
    """
    projects = post.get("projects") or {}
    tournaments = [
        p.get("slug") for p in projects.get("tournament") or [] if isinstance(p, dict)
    ] + [p.get("slug") for p in projects.get("question_series") or [] if isinstance(p, dict)]
    return {
        "post_id": post.get("id"),
        "url": f"https://www.metaculus.com/questions/{post.get('id')}/",
        "post_title": post.get("title"),
        "tournaments": [t for t in tournaments if t],
        # Top level as well as under `question`: log_forecast.py checks a
        # multiple-choice forecast's labels against a cached `options` list.
        "options": question.get("options"),
        "question": {k: question.get(k) for k in SNAPSHOT_QUESTION_KEYS},
    }


def main() -> None:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("whoami", help="check the token: who is the bot?")
    p = sub.add_parser("post", help="print a post's forecaster-facing snapshot")
    p.add_argument("post_id", type=int)
    o = sub.add_parser("open", help="list open posts in a tournament")
    o.add_argument("tournament")
    t = sub.add_parser("tournament", help="print tournament metadata")
    t.add_argument("slug")
    args = ap.parse_args()
    try:
        if args.cmd == "whoami":
            me = whoami()
            print(json.dumps({k: me.get(k) for k in ("id", "username", "is_bot")}))
        elif args.cmd == "post":
            post = get_post(args.post_id)
            q = post.get("question") or {}
            print(json.dumps(question_snapshot(post, q), indent=2, ensure_ascii=False))
        elif args.cmd == "open":
            for post in list_posts(args.tournament):
                q = post.get("question") or {}
                print(
                    f"{post['id']}\tq{q.get('id')}\t{q.get('type')}\t"
                    f"closes {post.get('scheduled_close_time')}\t{post.get('title')}"
                )
        elif args.cmd == "tournament":
            doc = get_tournament(args.slug)
            doc.pop("description", None)
            print(json.dumps(doc, indent=2, ensure_ascii=False))
    except MetaculusError as exc:
        sys.exit(f"! {exc}")


if __name__ == "__main__":
    main()
