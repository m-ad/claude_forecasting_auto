#!/usr/bin/env python3
"""Build the bot's results page: closed and resolved questions, scores, costs, ranks.

Deterministic, no model. Everything but the leaderboards comes from what the
repository already records:

- ``questions/*/meta.yaml``: status, title, Metaculus URL, and the official spot
  peer score the daily sync stores in ``tournament.official_score``;
- ``ledger/forecasts.jsonl``: the forecast as submitted, and the outcome;
- ``ledger/usage.jsonl``: the API-equivalent cost of every Claude run.

The leaderboards are read live from Metaculus when a token is set, and fail soft:
an API error or a changed response shape leaves a note on the page instead of
failing the build, because a page without ranks is better than no page.

Brier score, by question type (lower is better everywhere):

- **binary**: ``(p - y)^2``, 0 to 1.
- **multiple choice**: multi-class Brier ``sum_k (p_k - y_k)^2``, 0 to 2.
- **numeric / discrete**: the Brier score is defined for categorical outcomes
  only, so these get its standard extension, the ranked probability score: the
  mean Brier score of the threshold questions "value <= x_i" at every point x_i
  of the submitted CDF (Epstein 1969; the discrete form of the CRPS, Gneiting &
  Raftery 2007). 0 to 1, on the same scale as a binary Brier score.

Output: ``<out>/index.html`` and the same data as ``<out>/results.json``.

Examples
--------
    uv run scripts/build_page.py --out _site
    uv run scripts/build_page.py --out _site --no-leaderboards
"""

from __future__ import annotations

import argparse
import datetime as dt
import html
import json
import os
import sys
import time
from collections.abc import Iterable, Sequence
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))
import metaculus_api as mapi
from _common import (
    LEDGER,
    QUESTIONS,
    all_questions,
    fmt_forecast,
    fmt_value,
    ledger_records,
)
from calibration import brier, mc_brier, mc_label
from record_usage import USAGE
from tournament_registry import load_registry

METACULUS = "https://www.metaculus.com"
# Pause between Metaculus calls, as tournament_sync.py does: the API rate-limits per IP.
PAUSE_S = 0.5


@dataclass
class Row:
    """One question as the page shows it."""

    slug: str
    title: str
    url: str | None
    post_id: int | None
    tournament: str | None
    qtype: str
    status: str
    closed: str | None
    resolves: str | None
    forecast: str
    outcome: str | None = None
    brier: float | None = None
    brier_kind: str | None = None
    peer_score: float | None = None
    cost_usd: float = 0.0
    runs: int = 0


# ------------------------------------------------------------------ scoring
def ranked_brier(
    cdf: Sequence[float], xs: Sequence[float], outcome: float | str
) -> float | None:
    """Mean Brier score over the threshold questions "value <= x_i" of a CDF.

    Parameters
    ----------
    cdf : sequence of float
        ``P(X <= x_i)`` at each point, as submitted (``continuous_cdf``).
    xs : sequence of float
        The points in native units: the question's ``scaling.continuous_range``,
        which is evenly spaced on Metaculus' own (linear or log) axis.
    outcome : float or str
        The resolved value, or ``above_upper_bound`` / ``below_lower_bound``.

    Returns
    -------
    float or None
        0 (all mass on the right side of every threshold) to 1; None when the
        inputs do not line up or the outcome is not a value.
    """
    if not cdf or len(cdf) != len(xs):
        return None
    if isinstance(outcome, str):
        side = {"above_upper_bound": 0.0, "below_lower_bound": 1.0}.get(outcome.lower())
        if side is None:
            return None
        hits = [side] * len(xs)
    else:
        hits = [1.0 if outcome <= x else 0.0 for x in xs]
    return sum((f - h) ** 2 for f, h in zip(cdf, hits, strict=True)) / len(cdf)


def score_brier(
    qtype: str,
    outcome: Any,
    payload: dict[str, Any] | None,
    meta: dict[str, Any],
    snapshot: dict[str, Any] | None,
    probabilities: dict[str, float] | None = None,
) -> tuple[float | None, str | None]:
    """The Brier score of the forecast that was scored, and which variant it is.

    The submitted payload is preferred to the ledger's median: it is what Metaculus
    scored (after its clipping), and for numeric questions the only full CDF.

    Returns
    -------
    tuple
        ``(score, kind)`` with kind ``binary``, ``multi-class`` or ``ranked``;
        ``(None, None)`` when the forecast or outcome does not allow one.
    """
    payload = payload or {}
    if outcome is None:
        return None, None
    if qtype == "binary":
        p = payload.get("probability_yes")
        if p is None:
            p = (meta.get("current") or {}).get("median")
        return (
            (brier(float(p), float(outcome)), "binary")
            if p is not None
            else (None, None)
        )
    if qtype == "multiple_choice":
        probs = payload.get("probability_yes_per_category") or probabilities
        label = mc_label(outcome, list(probs)) if probs else None
        if label is None:
            return None, None
        return mc_brier(probs, label), "multi-class"
    cdf = payload.get("continuous_cdf")
    xs = ((snapshot or {}).get("scaling") or {}).get("continuous_range")
    if not cdf or not xs:
        return None, None
    try:
        value = ranked_brier([float(c) for c in cdf], [float(x) for x in xs], outcome)
    except (TypeError, ValueError):  # e.g. ISO-date points on a date question
        return None, None
    return (value, "ranked") if value is not None else (None, None)


# ------------------------------------------------------------------ inputs
def costs_by_slug(path: Path = USAGE) -> dict[str, tuple[float, int]]:
    """``slug -> (API-equivalent cost, runs)`` summed over ``ledger/usage.jsonl``."""
    out: dict[str, tuple[float, int]] = {}
    for rec in ledger_records(path):
        slug = rec.get("slug")
        if not slug:
            continue
        cost = rec.get("cost_usd_equiv")
        cost = (
            float(cost)
            if isinstance(cost, (int, float)) and not isinstance(cost, bool)
            else 0.0
        )
        total, runs = out.get(slug, (0.0, 0))
        out[slug] = (total + cost, runs + 1)
    return out


def latest_snapshot(slug: str) -> dict[str, Any] | None:
    """The ``question`` part of the newest cached ``raw/metaculus-question-*.json``."""
    snaps = sorted((QUESTIONS / slug / "raw").glob("metaculus-question-*.json"))
    if not snaps:
        return None
    try:
        return json.loads(snaps[-1].read_text(encoding="utf-8")).get("question")
    except (json.JSONDecodeError, OSError, AttributeError):
        return None


def _outcome_text(outcome: Any, qtype: str, unit: str | None) -> str:
    if qtype == "binary":
        return "Yes" if float(outcome) == 1.0 else "No"
    if qtype == "multiple_choice":
        # A legacy outcome is the float of a numeric label (calibration.mc_label).
        is_int = isinstance(outcome, float) and outcome.is_integer()
        return str(int(outcome)) if is_int else str(outcome)
    if isinstance(outcome, str):
        return outcome.replace("_", " ")
    text = fmt_value(float(outcome), qtype)
    if unit in ("$", "€", "£"):
        return f"{unit}{text}"
    if unit == "%":
        return f"{text}%"
    return f"{text} {unit}" if unit else text


def _forecast_text(
    meta: dict[str, Any], payload: dict[str, Any], probs: dict[str, float] | None
) -> str:
    qtype = meta.get("type")
    if qtype == "binary" and payload.get("probability_yes") is not None:
        return f"{float(payload['probability_yes']):.1%}"
    if qtype == "multiple_choice":
        probs = payload.get("probability_yes_per_category") or probs
        if probs:
            top = max(probs, key=probs.get)
            return f"{top}: {probs[top] / sum(probs.values()):.1%}"
    return fmt_forecast(meta)


def build_rows(
    usage_path: Path = USAGE, ledger_path: Path = LEDGER
) -> tuple[list[Row], list[Row], int]:
    """Resolved rows (newest first), closed rows (newest first), dropped count."""
    submissions: dict[str, dict] = {}
    resolutions: dict[str, dict] = {}
    forecasts: dict[str, dict] = {}
    for rec in ledger_records(ledger_path):
        event, slug = rec.get("event"), rec.get("slug")
        if event == "submission":
            submissions[slug] = rec
        elif event == "resolution":
            resolutions[slug] = rec
        elif event == "forecast":
            forecasts[slug] = rec  # file order is time order per slug: the last wins
    costs = costs_by_slug(usage_path)

    resolved, closed, dropped = [], [], 0
    for slug, meta in all_questions():
        status = meta.get("status")
        if status == "dropped":
            dropped += 1
        if status not in ("closed", "resolved"):
            continue
        tour = meta.get("tournament") or {}
        qtype = meta.get("type") or "binary"
        payload = (submissions.get(slug) or {}).get("payload") or {}
        probs = ((forecasts.get(slug) or {}).get("distribution") or {}).get(
            "probabilities"
        )
        cost, runs = costs.get(slug, (0.0, 0))
        row = Row(
            slug=slug,
            title=str(meta.get("title") or slug),
            url=meta.get("url"),
            post_id=meta.get("post_id"),
            tournament=tour.get("slug"),
            qtype=qtype,
            status=status,
            closed=str(
                tour.get("closes") or (meta.get("dates") or {}).get("closes") or ""
            )[:10]
            or None,
            resolves=(meta.get("dates") or {}).get("resolves"),
            forecast=_forecast_text(meta, payload, probs),
            cost_usd=round(cost, 4),
            runs=runs,
        )
        if status == "resolved":
            outcome = (resolutions.get(slug) or {}).get("outcome")
            if outcome is None:
                outcome = (meta.get("resolution") or {}).get("outcome")
            if outcome is not None:
                row.outcome = _outcome_text(outcome, qtype, meta.get("unit"))
            row.brier, row.brier_kind = score_brier(
                qtype, outcome, payload, meta, latest_snapshot(slug), probs
            )
            row.peer_score = tour.get("official_score")
            row.resolves = (meta.get("resolution") or {}).get("date") or row.resolves
            resolved.append(row)
        else:
            closed.append(row)
    resolved.sort(key=lambda r: (str(r.resolves or ""), r.slug), reverse=True)
    closed.sort(key=lambda r: (str(r.closed or ""), r.slug), reverse=True)
    return resolved, closed, dropped


# ------------------------------------------------------------- leaderboards
def _projects(post: dict[str, Any]) -> list[dict[str, Any]]:
    """The leaderboard-bearing projects (tournaments, question series) of a post."""
    projects = post.get("projects") or {}
    out: dict[int, dict[str, Any]] = {}
    for proj in [
        *(projects.get("tournament") or []),
        *(projects.get("question_series") or []),
        projects.get("default_project"),
    ]:
        if (
            isinstance(proj, dict)
            and proj.get("type") in ("tournament", "question_series")
            and isinstance(proj.get("id"), int)
        ):
            out.setdefault(proj["id"], proj)
    return list(out.values())


def discover_projects(
    post_ids: Iterable[int], pause: float = PAUSE_S
) -> dict[int, dict[str, Any]]:
    """``project_id -> {"project": ..., "members": set of post ids}`` for these posts.

    One ``get_post`` per project rather than per question: each project found lists
    its closed and resolved posts, and every one of those is then known. This
    assumes the questions of one project share their leaderboard projects, which
    holds for the bot tournaments (one MiniBench round or one FutureEval season
    per question).
    """
    pending = sorted({int(p) for p in post_ids}, reverse=True)
    found: dict[int, dict[str, Any]] = {}
    while pending:
        pid = pending.pop(0)
        post = mapi.get_post(pid, stage="page")
        for proj in _projects(post):
            if proj["id"] in found:
                continue
            time.sleep(pause)
            members = {
                int(p["id"])
                for p in mapi.list_posts(
                    proj["id"], statuses="closed,resolved", stage="page"
                )
                if isinstance(p.get("id"), int)
            }
            found[proj["id"]] = {"project": proj, "members": members | {pid}}
        known = set().union(*(f["members"] for f in found.values())) if found else set()
        pending = [p for p in pending if p not in known]
        time.sleep(pause)
    return found


def standing(
    project: dict[str, Any],
    boards: list[dict[str, Any]],
    user_id: int | None,
    local_scores: list[float],
) -> dict[str, Any]:
    """The bot's place on a project's primary leaderboard.

    Metaculus' ``rank`` counts only entries with ``exclusion_status == 0``; its own
    reference bots carry other statuses and an interpolated rank (checked against
    the live MiniBench 2026-10-19 board on 2026-11-01: rank = 1 + the number of
    status-0 entries with a strictly higher score, for all 384 entries). So the
    field size is the number of status-0 entries.

    When the bot has no entry, the sum of its synced official scores gives an
    estimated place (a ``spot_peer_tournament`` score is that sum), marked as such.
    """
    board = next((b for b in boards if b.get("is_primary_leaderboard")), None) or (
        boards[0] if boards else {}
    )
    entries = [e for e in board.get("entries") or [] if isinstance(e.get("user"), dict)]
    ranked = [e for e in entries if e.get("exclusion_status") == 0]
    slug = project.get("slug") or board.get("project_slug")
    out: dict[str, Any] = {
        "project_id": project.get("id"),
        "name": project.get("name") or board.get("project_name") or slug,
        "url": f"{METACULUS}/tournament/{slug}/" if slug else None,
        "score_type": board.get("score_type"),
        "finalized": bool(board.get("finalized")),
        "max_coverage": board.get("max_coverage"),
        "field": len(ranked),
        "top_score": max((float(e["score"]) for e in ranked), default=None),
        "calculated_on": max(
            (str(e.get("calculated_on") or "") for e in entries), default=""
        )[:10]
        or None,
        "rank": None,
        "score": None,
        "coverage": None,
        "excluded": None,
        "estimated_rank": None,
        "local_score": round(sum(local_scores), 2) if local_scores else None,
        "local_n": len(local_scores),
    }
    mine = next(
        (e for e in entries if user_id is not None and e["user"].get("id") == user_id),
        None,
    )
    if mine:
        out.update(
            rank=mine.get("rank"),
            score=mine.get("score"),
            coverage=mine.get("coverage"),
            excluded=bool(mine.get("excluded"))
            or mine.get("exclusion_status") not in (0, None),
        )
    elif local_scores:
        total = sum(local_scores)
        out["estimated_rank"] = 1 + sum(1 for e in ranked if float(e["score"]) > total)
    return out


def leaderboards(
    resolved: list[Row], closed: list[Row]
) -> tuple[list[dict], str | None, dict]:
    """Standings for every scored project the bot's closed/resolved questions belong to.

    Returns
    -------
    tuple
        ``(standings, note, bot)``: ``note`` says why there are none, if so;
        ``bot`` is ``{"id", "username"}`` or empty.
    """
    if not mapi.token():
        return [], "skipped: no METACULUS_API_KEY in the environment", {}
    unscored = {t.get("slug") for t in load_registry() if t.get("scored") is False}
    rows = [
        r
        for r in resolved + closed
        if r.post_id and r.tournament and r.tournament not in unscored
    ]
    if not rows:
        return [], "no closed or resolved question in a scored tournament yet", {}
    try:
        me = mapi.whoami()
        bot = {"id": me.get("id"), "username": me.get("username")}
        found = discover_projects(r.post_id for r in rows)
        out = []
        for pid, info in sorted(found.items(), reverse=True):
            local = [
                float(r.peer_score)
                for r in resolved
                if r.post_id in info["members"] and r.peer_score is not None
            ]
            time.sleep(PAUSE_S)
            out.append(
                standing(
                    info["project"], mapi.project_leaderboards(pid), bot["id"], local
                )
            )
        return out, None, bot
    except (mapi.MetaculusError, KeyError, TypeError, ValueError) as exc:
        return [], f"unavailable: {mapi.redact(str(exc))}", {}


# ------------------------------------------------------------------ render
CSS = r"""
:root{--bg:#fbfaf7;--fg:#1d1d1b;--muted:#6b6a65;--line:#e4e1d8;--card:#ffffff;
--accent:#2f5d8a;--good:#1f7a4d;--bad:#b23b2e;--head:#f2efe7}
@media (prefers-color-scheme:dark){:root{--bg:#141413;--fg:#ecebe6;--muted:#a3a29b;
--line:#2f2e2b;--card:#1c1c1a;--accent:#8db4dc;--good:#5cc290;--bad:#ec7d6f;--head:#22221f}}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--fg);
font:15px/1.5 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}
main{max-width:1180px;margin:0 auto;padding:24px 16px 64px}
h1{font-size:1.6rem;margin:0 0 4px}h2{font-size:1.15rem;margin:36px 0 10px}
p.sub,.muted{color:var(--muted)}a{color:var(--accent)}
.tiles{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:10px;margin-top:18px}
.tile{background:var(--card);border:1px solid var(--line);border-radius:8px;padding:10px 12px}
.tile b{display:block;font-size:1.3rem;font-variant-numeric:tabular-nums}
.tile span{color:var(--muted);font-size:.85rem}
.wrap{overflow-x:auto;border:1px solid var(--line);border-radius:8px;background:var(--card)}
table{border-collapse:collapse;width:100%;font-size:.9rem}
th,td{padding:7px 10px;border-bottom:1px solid var(--line);text-align:left;vertical-align:top}
th{background:var(--head);font-weight:600;white-space:nowrap}
tr:last-child td{border-bottom:0}
td.n{text-align:right;font-variant-numeric:tabular-nums;white-space:nowrap}
td.q{min-width:260px}.good{color:var(--good)}.bad{color:var(--bad)}
tfoot td{font-weight:600;background:var(--head)}
table.sortable th{cursor:pointer;user-select:none}
table.sortable th::after{content:" \2195";color:var(--muted);font-weight:400}
table.sortable th[aria-sort=ascending]::after{content:" \25B2";color:var(--accent)}
table.sortable th[aria-sort=descending]::after{content:" \25BC";color:var(--accent)}
.notes{font-size:.85rem;color:var(--muted);margin-top:36px}.notes li{margin:4px 0}
"""


# Progressive enhancement: without JS the tables render in their build order. Footer rows
# (totals) sit outside <tbody> and are never sorted. Missing values ("—") always sort last.
SORT_JS = r"""
document.querySelectorAll("table.sortable").forEach(function(t){
var body=t.tBodies[0];
function val(td){return td.textContent.trim().replace(/\u2212/g,"-")}
function num(v){var m=/^([+-]?)\$?([\d,]*\.?\d+)/.exec(v);
return m?parseFloat(m[1]+m[2].replace(/,/g,"")):null}
t.tHead.querySelectorAll("th").forEach(function(th,i){
th.tabIndex=0;
function go(){
var rows=Array.prototype.slice.call(body.rows);
var vals=rows.map(function(r){return val(r.cells[i])});
var isNum=vals.every(function(v){return v==="\u2014"||num(v)!==null});
var dir=th.getAttribute("aria-sort")==="descending"?1:
th.getAttribute("aria-sort")==="ascending"?-1:(isNum?-1:1);
var keyed=rows.map(function(r,k){var v=vals[k];
return {r:r,miss:v==="\u2014"||v==="",k:isNum?num(v):v.toLowerCase()}});
keyed.sort(function(a,b){
if(a.miss||b.miss)return a.miss-b.miss;
return (a.k<b.k?-1:a.k>b.k?1:0)*dir});
t.tHead.querySelectorAll("th").forEach(function(o){o.removeAttribute("aria-sort")});
th.setAttribute("aria-sort",dir<0?"descending":"ascending");
keyed.forEach(function(o){body.appendChild(o.r)})}
th.addEventListener("click",go);
th.addEventListener("keydown",function(e){if(e.key==="Enter"||e.key===" "){e.preventDefault();go()}})})})
"""


def _e(value: Any) -> str:
    return html.escape(str(value), quote=True)


def _num(value: float | None, fmt: str, signed: bool = False) -> str:
    if value is None:
        return '<td class="n muted">—</td>'
    cls = ""
    if signed:
        cls = " good" if value > 0 else " bad" if value < 0 else ""
    return f'<td class="n{cls}">{format(value, fmt)}</td>'


def _title(row: Row) -> str:
    if row.url:
        return f'<a href="{_e(row.url)}" target="_blank" rel="noopener">{_e(row.title)}</a>'
    return _e(row.title)


def _mean(values: list[float]) -> float | None:
    return sum(values) / len(values) if values else None


def render_html(
    resolved: list[Row],
    closed: list[Row],
    dropped: int,
    boards: list[dict],
    board_note: str | None,
    bot: dict,
    now: dt.datetime,
) -> str:
    """The whole page as one self-contained HTML document (one inline sort script, no assets)."""
    listed = resolved + closed
    peers = [r.peer_score for r in resolved if r.peer_score is not None]
    kinds = {
        k: [r.brier for r in resolved if r.brier_kind == k and r.brier is not None]
        for k in ("binary", "multi-class", "ranked")
    }
    total_cost = sum(r.cost_usd for r in listed)
    tiles = [
        (str(len(resolved)), "resolved"),
        (str(len(closed)), "closed, awaiting resolution"),
        (f"{sum(peers):+.1f}" if peers else "—", f"summed peer score ({len(peers)} q)"),
        (f"{_mean(peers):+.1f}" if peers else "—", "mean peer score"),
        (
            f"{_mean(kinds['binary']):.3f}" if kinds["binary"] else "—",
            f"mean Brier, binary ({len(kinds['binary'])} q)",
        ),
        (
            f"{_mean(kinds['ranked']):.3f}" if kinds["ranked"] else "—",
            f"mean ranked Brier, numeric ({len(kinds['ranked'])} q)",
        ),
        (f"${total_cost:,.2f}", "API-equivalent cost, listed questions"),
        (f"${total_cost / len(listed):,.2f}" if listed else "—", "per question"),
    ]

    name = bot.get("username") or "Forecasting bot"
    who = (
        f'<a href="{METACULUS}/accounts/profile/{_e(bot["id"])}/">{_e(name)}</a>'
        if bot.get("id")
        else _e(name)
    )
    out = [
        "<!doctype html>",
        '<html lang="en"><head><meta charset="utf-8">',
        '<meta name="viewport" content="width=device-width,initial-scale=1">',
        f"<title>{_e(name)} results</title>",
        f"<style>{CSS}</style></head><body><main>",
        f"<h1>{who}: closed and resolved questions</h1>",
        (
            f'<p class="sub">An autonomous Metaculus bot (Claude Code in GitHub Actions). '
            f"Generated {now:%Y-%m-%d %H:%M} UTC from the repository's ledger.</p>"
        ),
        '<div class="tiles">',
        *(
            f'<div class="tile"><b>{_e(v)}</b><span>{_e(k)}</span></div>'
            for v, k in tiles
        ),
        "</div>",
        "<h2>Leaderboards</h2>",
    ]

    if boards:
        out += [
            (
                '<div class="wrap"><table class="sortable"><thead><tr><th>Tournament</th><th>Rank</th>'
                "<th>Bot score</th><th>Coverage</th><th>Top score</th><th>Status</th>"
                "</tr></thead><tbody>"
            )
        ]
        for b in boards:
            link = (
                f'<a href="{_e(b["url"])}" target="_blank" rel="noopener">{_e(b["name"])}</a>'
                if b.get("url")
                else _e(b["name"])
            )
            if b["rank"] is not None:
                rank = f"{b['rank']} of {b['field']}" + (
                    " (excluded)" if b["excluded"] else ""
                )
                score, cov = b["score"], f"{b['coverage']}/{b['max_coverage']}"
            elif b["estimated_rank"] is not None:
                rank = (
                    f"not listed; ~{b['estimated_rank']} of {b['field']} by its "
                    f"{b['local_n']} synced scores (estimate)"
                )
                score, cov = b["local_score"], f"{b['local_n']}/{b['max_coverage']}"
            else:
                rank, score, cov = "not listed", None, "—"
            status = "final" if b["finalized"] else "provisional"
            if b.get("calculated_on"):
                status += f", calculated {b['calculated_on']}"
            out.append(
                f"<tr><td>{link}</td><td>{_e(rank)}</td>"
                f"{_num(float(score) if score is not None else None, '+.1f', True)}"
                f'<td class="n">{_e(cov)}</td>'
                f"{_num(b['top_score'], '+.1f')}<td>{_e(status)}</td></tr>"
            )
        out.append("</tbody></table></div>")
    else:
        out.append(
            f'<p class="muted">Leaderboards {_e(board_note or "unavailable")}.</p>'
        )

    out += [
        f"<h2>Resolved ({len(resolved)})</h2>",
        (
            '<div class="wrap"><table class="sortable"><thead><tr><th>Question</th><th>Tournament</th>'
            "<th>Type</th><th>Forecast</th><th>Outcome</th><th>Resolved</th><th>Brier</th>"
            "<th>Peer score</th><th>API cost</th></tr></thead><tbody>"
        ),
    ]
    for r in resolved:
        out.append(
            f'<tr><td class="q">{_title(r)}</td><td>{_e(r.tournament or "—")}</td>'
            f"<td>{_e(r.qtype)}</td><td>{_e(r.forecast)}</td><td>{_e(r.outcome or '—')}</td>"
            f'<td class="n">{_e(r.resolves or "—")}</td>'
            f"{_num(r.brier, '.3f')}{_num(r.peer_score, '+.1f', True)}"
            f"{_num(r.cost_usd if r.runs else None, ',.2f')}</tr>"
        )
    out += [
        (
            '</tbody><tfoot><tr><td colspan="7">Total</td>'
            f"{_num(sum(peers) if peers else None, '+.1f', True)}"
            f"{_num(sum(r.cost_usd for r in resolved), ',.2f')}</tr></tfoot></table></div>"
        ),
        f"<h2>Closed, awaiting resolution ({len(closed)})</h2>",
        (
            '<div class="wrap"><table class="sortable"><thead><tr><th>Question</th><th>Tournament</th>'
            "<th>Type</th><th>Forecast</th><th>Closed</th><th>Resolves</th>"
            "<th>API cost</th></tr></thead><tbody>"
        ),
    ]
    for r in closed:
        out.append(
            f'<tr><td class="q">{_title(r)}</td><td>{_e(r.tournament or "—")}</td>'
            f"<td>{_e(r.qtype)}</td><td>{_e(r.forecast)}</td>"
            f'<td class="n">{_e(r.closed or "—")}</td><td class="n">{_e(r.resolves or "—")}</td>'
            f"{_num(r.cost_usd if r.runs else None, ',.2f')}</tr>"
        )
    out += [
        (
            '</tbody><tfoot><tr><td colspan="6">Total</td>'
            f"{_num(sum(r.cost_usd for r in closed), ',.2f')}</tr></tfoot></table></div>"
        ),
        '<ul class="notes">',
        (
            "<li><b>Forecast</b>: binary, the probability submitted; numeric and discrete, "
            "median [interquartile range]; multiple choice, the leading option.</li>"
        ),
        (
            "<li><b>Brier</b> (lower is better): binary (p − y)², 0–1. Multiple choice: "
            "multi-class Σ(pₖ − yₖ)², 0–2. Numeric and discrete: the ranked probability "
            "score, the mean Brier score of the threshold questions “value ≤ x” at every "
            "point of the submitted CDF, 0–1. Computed here from the submitted forecast.</li>"
        ),
        (
            "<li><b>Peer score</b>: the official Metaculus spot peer score, relative to the "
            "other forecasters on the question (0 = average, higher is better), as synced "
            "daily. A tournament score is the sum.</li>"
        ),
        (
            "<li><b>API cost</b>: the API-equivalent price of the Claude Code runs on the "
            "question, as the CLI reports it (USD). On a subscription token it is not billed; "
            "it measures how much allowance a forecast used.</li>"
        ),
        (
            "<li><b>Rank</b>: Metaculus' rank among the ranked entries of the tournament's "
            "primary leaderboard; provisional until the leaderboard is finalized.</li>"
        ),
    ]
    if dropped:
        out.append(
            f"<li>{dropped} dropped question(s) (missed window, annulled or ambiguous) "
            "are not listed.</li>"
        )
    out += [f"</ul></main><script>{SORT_JS}</script></body></html>", ""]
    return "\n".join(out)


def main() -> None:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("--out", type=Path, default=Path("_site"), help="output directory")
    ap.add_argument(
        "--no-leaderboards", action="store_true", help="do not call Metaculus at all"
    )
    args = ap.parse_args()

    resolved, closed, dropped = build_rows()
    if args.no_leaderboards:
        boards, note, bot = [], "not fetched for this build", {}
    else:
        boards, note, bot = leaderboards(resolved, closed)
    if (
        note
        and note.startswith("unavailable")
        and os.environ.get("GITHUB_ACTIONS") == "true"
    ):
        print(f"::warning::leaderboards {note}")
    now = dt.datetime.now(dt.UTC)
    args.out.mkdir(parents=True, exist_ok=True)
    (args.out / "index.html").write_text(
        render_html(resolved, closed, dropped, boards, note, bot, now),
        encoding="utf-8",
        newline="\n",
    )
    data = {
        "generated": now.isoformat(timespec="seconds"),
        "bot": bot,
        "leaderboards": boards,
        "leaderboard_note": note,
        "resolved": [asdict(r) for r in resolved],
        "closed": [asdict(r) for r in closed],
        "dropped": dropped,
    }
    (args.out / "results.json").write_text(
        json.dumps(data, indent=1, ensure_ascii=False) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(
        f"wrote {args.out / 'index.html'}: {len(resolved)} resolved, {len(closed)} closed, "
        f"{len(boards)} leaderboard(s){f' ({note})' if note else ''}"
    )


if __name__ == "__main__":
    main()
