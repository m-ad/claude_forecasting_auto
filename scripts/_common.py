"""Shared helpers for the forecasting workbench scripts.

Kept dependency-light on purpose: only PyYAML, so the tooling still runs when a
Playwright/browser install is broken.
"""

from __future__ import annotations

import datetime as _dt
import re
from pathlib import Path
from typing import Any, Optional

import yaml

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
    stop = {"will", "the", "a", "an", "of", "in", "on", "at", "to", "be", "by",
            "for", "and", "or", "is", "are", "there", "any", "what", "when"}
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


def find_slug(needle: str) -> Optional[str]:
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
    hits = [s for s, meta in cands
            if low in s.lower() or low in str(meta.get("title", "")).lower()]
    if len(hits) == 1:
        return hits[0]
    if hits:
        print("Ambiguous, candidates:")
        for h in hits:
            print("  ", h)
    return None


def days_until(date_str: Optional[str]) -> Optional[int]:
    """Whole days from today to ``date_str`` (negative once past)."""
    if not date_str:
        return None
    try:
        d = _dt.date.fromisoformat(str(date_str)[:10])
    except ValueError:
        return None
    return (d - _dt.date.today()).days


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
    band = f" [{lo:g}, {hi:g}]" if lo is not None and hi is not None else ""
    return f"{med:g}{band}"
