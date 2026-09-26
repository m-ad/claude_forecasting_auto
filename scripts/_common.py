"""Shared helpers for the forecasting workbench scripts.

Kept dependency-light on purpose: only PyYAML, so the tooling still runs when a
Playwright/browser install is broken.
"""

from __future__ import annotations

import codecs
import datetime as _dt
import math
import re
import sys
from itertools import pairwise
from pathlib import Path
from typing import Any

import yaml

# ------------------------------------------------------------------- stdio
# The scripts print arrows, middots and em dashes. Windows gives a redirected or
# piped stdout the locale codepage (cp1252), which has none of them, so an
# unguarded print() dies with UnicodeEncodeError mid-report — and takes the exit
# code with it. Degrade the characters instead of the run: transliterate the ones
# we actually emit to ASCII, and fall back to "?" for anything else.
_ASCII_FALLBACKS = {
    "→": "->",  # rightwards arrow
    "←": "<-",
    "—": "-",  # em dash
    "–": "-",  # en dash
    "·": "*",  # middot
    "•": "*",
    "≈": "~",  # almost equal
    "≤": "<=",
    "≥": ">=",
    "Δ": "delta",
    "×": "x",
    "‘": "'",
    "’": "'",
    "“": '"',
    "”": '"',
    "…": "...",
}
_ERROR_HANDLER = "forecasting_ascii_fallback"


def _ascii_fallback(exc: UnicodeError) -> tuple[str, int]:
    """Codec error handler: replace unencodable characters with ASCII stand-ins."""
    if not isinstance(exc, UnicodeEncodeError):
        raise exc
    bad = exc.object[exc.start : exc.end]
    return "".join(_ASCII_FALLBACKS.get(ch, "?") for ch in bad), exc.end


def make_stdio_lenient() -> None:
    """Stop a narrow console encoding from crashing a script's own output.

    Idempotent, and a no-op on streams that cannot be reconfigured (a pytest
    capture buffer, say). Characters the stream *can* encode are untouched, so
    a UTF-8 terminal still gets the real arrows.
    """
    try:
        codecs.lookup_error(_ERROR_HANDLER)
    except LookupError:
        codecs.register_error(_ERROR_HANDLER, _ascii_fallback)
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(errors=_ERROR_HANDLER)  # type: ignore[union-attr]
        except (AttributeError, ValueError, OSError):
            pass


make_stdio_lenient()


REPO = Path(__file__).resolve().parent.parent
QUESTIONS = REPO / "questions"
LEDGER = REPO / "ledger" / "forecasts.jsonl"
TEMPLATES = REPO / "templates"

SRC_ABBREV = {
    "metaculus": "mc",
    "kalshi": "ks",
    "polymarket": "pm",
    "manifold": "mf",
    "other": "x",
}


def today() -> str:
    """Return today's date as an ISO ``YYYY-MM-DD`` string."""
    return _dt.date.today().isoformat()


def slugify(text: str, max_words: int = 7) -> str:
    """Turn a question title into a short, filesystem-safe slug fragment.

    Parameters
    ----------
    text : str
        Free-form title.
    max_words : int, optional
        Cap on the number of words kept, by default 7.

    Returns
    -------
    str
        Lowercase hyphenated fragment, stopwords dropped.
    """
    stop = {
        "will",
        "the",
        "a",
        "an",
        "of",
        "in",
        "on",
        "at",
        "to",
        "be",
        "by",
        "for",
        "and",
        "or",
        "is",
        "are",
        "there",
        "any",
        "what",
        "when",
    }
    words = re.findall(r"[a-z0-9]+", text.lower())
    kept = [w for w in words if w not in stop] or words
    return "-".join(kept[:max_words])[:60].strip("-")


def load_meta(slug: str) -> dict[str, Any]:
    """Read ``questions/<slug>/meta.yaml``."""
    with (QUESTIONS / slug / "meta.yaml").open(encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def save_meta(slug: str, meta: dict[str, Any]) -> None:
    """Write ``questions/<slug>/meta.yaml``, preserving key order."""
    with (QUESTIONS / slug / "meta.yaml").open("w", encoding="utf-8") as fh:
        yaml.safe_dump(meta, fh, sort_keys=False, allow_unicode=True, width=100)


def all_questions() -> list[tuple[str, dict[str, Any]]]:
    """Return ``(slug, meta)`` for every scaffolded question, oldest first."""
    out: list[tuple[str, dict[str, Any]]] = []
    if not QUESTIONS.exists():
        return out
    for d in sorted(QUESTIONS.iterdir()):
        if (d / "meta.yaml").is_file():
            try:
                out.append((d.name, load_meta(d.name)))
            except yaml.YAMLError as exc:  # a hand-edited file should not kill triage
                print(f"! {d.name}: unreadable meta.yaml ({exc})")
    return out


def find_slug(needle: str) -> str | None:
    """Resolve a slug, URL, post id, or title fragment to exactly one slug.

    Returns ``None`` when nothing matches or the match is ambiguous (the
    candidates are printed in that case).
    """
    needle = needle.strip().rstrip("/")
    cands = all_questions()
    exact = [s for s, _ in cands if s == needle]
    if exact:
        return exact[0]
    m = re.search(r"/questions/(\d+)", needle) or re.fullmatch(r"(\d+)", needle)
    if m:
        pid = int(m.group(1))
        hits = [s for s, meta in cands if meta.get("post_id") == pid]
        if len(hits) == 1:
            return hits[0]
    low = needle.lower()
    hits = [
        s
        for s, meta in cands
        if low in s.lower() or low in str(meta.get("title", "")).lower()
    ]
    if len(hits) == 1:
        return hits[0]
    if hits:
        print("Ambiguous, candidates:")
        for h in hits:
            print("  ", h)
    return None


def days_until(date_str: str | None) -> int | None:
    """Whole days from today to ``date_str`` (negative once past)."""
    if not date_str:
        return None
    try:
        d = _dt.date.fromisoformat(str(date_str)[:10])
    except ValueError:
        return None
    return (d - _dt.date.today()).days


def fmt_number(value: float) -> str:
    """Render a native-unit number without %g's switch to scientific notation.

    A question denominated in barrels or dollars runs to 1e8, where ``%g`` emits
    ``2.823e+08`` and the index stops being readable. Group-separate anything
    that large and leave smaller values on ``%g``, which keeps the existing
    percentage- and index-scale questions unchanged.
    """
    if abs(value) >= 1e6:
        return f"{value:,.0f}"
    return f"{value:g}"


def fmt_forecast(meta: dict[str, Any]) -> str:
    """Render a question's current forecast as a one-line human string."""
    cur = meta.get("current") or {}
    med, iqr = cur.get("median"), cur.get("iqr") or [None, None]
    if med is None:
        return "—"
    if meta.get("type") == "binary":
        lo, hi = iqr
        band = f" [{lo:.1%}, {hi:.1%}]" if lo is not None and hi is not None else ""
        return f"{med:.1%}{band}"
    lo, hi = iqr
    band = (
        f" [{fmt_number(lo)}, {fmt_number(hi)}]"
        if lo is not None and hi is not None
        else ""
    )
    return f"{fmt_number(med)}{band}"


# ------------------------------------------------------------ distributions
# The ledger's median/IQR is the whole forecast only for a binary question. The
# optional ``distribution`` field on a forecast record carries the rest, in one
# shape per question type (a record's distribution has exactly one of these keys).
DISTRIBUTION_SHAPES: dict[str, set[str]] = {
    "multiple_choice": {"probabilities"},
    "numeric": {"percentiles"},
    "date": {"percentiles"},
    "discrete": {"pmf", "percentiles"},
}
SUM_TOLERANCE = 0.01  # one-decimal percentages over ~10 options can drift this far
LEAD_TOLERANCE = 5e-4  # the leading option vs. the median it was logged as


def _is_num(x: Any) -> bool:
    return isinstance(x, (int, float)) and not isinstance(x, bool) and math.isfinite(x)


def _same(a: float, b: float) -> bool:
    return math.isclose(a, b, rel_tol=1e-9, abs_tol=1e-12)


def distribution_problems(
    qtype: str,
    dist: Any,
    median: float,
    iqr: list[float] | tuple[float, float],
    options: list[str] | None = None,
) -> list[str]:
    """Reasons ``dist`` is not a valid full forecast for this record; empty if valid.

    Parameters
    ----------
    qtype : str
        The question type, as in ``meta.yaml``.
    dist : Any
        The candidate ``distribution`` value, e.g. ``{"probabilities": {...}}``.
    median, iqr : float, list of float
        The record's median and IQR, which the distribution must agree with: for
        multiple choice the median is the leading option's probability; for
        percentiles p50/p25/p75 must equal median/IQR exactly.
    options : list of str, optional
        The question's exact option labels, when known; multiple-choice keys must
        then match them as a set.

    Returns
    -------
    list of str
        Human-readable problems; the caller decides whether to exit or raise.
    """
    allowed = DISTRIBUTION_SHAPES.get(qtype)
    if allowed is None:
        return [f"{qtype} questions take no distribution (the median is the forecast)"]
    if not isinstance(dist, dict) or len(dist) != 1 or next(iter(dist)) not in allowed:
        return [f"{qtype} distribution must be exactly one of {sorted(allowed)}"]
    ((kind, body),) = dist.items()
    if not isinstance(body, dict) or len(body) < 2:
        return [f"{kind} must map at least two keys to numbers"]
    if not all(isinstance(k, str) and _is_num(v) for k, v in body.items()):
        return [f"{kind} keys must be strings and values finite numbers"]

    if kind == "probabilities":
        return _probability_problems(body, median, options)
    if kind == "pmf":
        return _pmf_problems(body, median)
    return _percentile_problems(body, median, iqr)


def _probability_problems(
    probs: dict[str, float], median: float, options: list[str] | None
) -> list[str]:
    out = []
    if any(not 0 <= p <= 1 for p in probs.values()):
        out.append("probabilities must be fractions in [0, 1], not percent")
    total = sum(probs.values())
    if abs(total - 1) > SUM_TOLERANCE:
        out.append(f"probabilities sum to {total:.4f}, not 1")
    lead = max(probs.values())
    if abs(lead - median) > LEAD_TOLERANCE:
        out.append(
            f"leading option is {lead}, but the median (leading option) is {median}"
        )
    if options is not None and set(probs) != set(options):
        out.append(
            f"labels must match the question's options exactly; missing "
            f"{sorted(set(options) - set(probs))}, unknown {sorted(set(probs) - set(options))}"
        )
    return out


def _pmf_problems(pmf: dict[str, float], median: float) -> list[str]:
    try:
        table = sorted((float(k), p) for k, p in pmf.items())
    except ValueError:
        return ["pmf keys must be outcome values (numbers as strings)"]
    out = []
    if any(not 0 <= p <= 1 for _, p in table):
        out.append("pmf values must be fractions in [0, 1], not percent")
    total = sum(p for _, p in table)
    if abs(total - 1) > SUM_TOLERANCE:
        out.append(f"pmf sums to {total:.4f}, not 1")
    below = sum(p for x, p in table if x < median) / total
    at_or_below = sum(p for x, p in table if x <= median) / total
    # Definition of a median, with the same slack as the sum.
    if below > 0.5 + SUM_TOLERANCE or at_or_below < 0.5 - SUM_TOLERANCE:
        out.append(
            f"median {median} is not a median of the pmf "
            f"(P(X<m) = {below:.3f}, P(X<=m) = {at_or_below:.3f})"
        )
    return out


def _percentile_problems(
    pct: dict[str, float], median: float, iqr: list[float] | tuple[float, float]
) -> list[str]:
    try:
        knots = sorted((float(k), v) for k, v in pct.items())
    except ValueError:
        return ["percentile keys must be numbers as strings, e.g. '5', '50'"]
    out = []
    if any(not 0 < k < 100 for k, _ in knots):
        out.append("percentile keys must lie strictly between 0 and 100")
    if any(b[1] < a[1] for a, b in pairwise(knots)):
        out.append("percentile values must not decrease")
    by_key = dict(knots)
    lo, hi = iqr
    for key, want, name in (
        (50.0, median, "median"),
        (25.0, lo, "IQR lower"),
        (75.0, hi, "IQR upper"),
    ):
        if key == 50.0 and key not in by_key:
            out.append("percentiles must include '50'")
        elif key in by_key and not _same(by_key[key], want):
            out.append(f"p{key:g} = {by_key[key]} differs from the {name} {want}")
    return out
