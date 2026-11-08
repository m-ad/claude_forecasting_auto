#!/usr/bin/env python3
"""The results page's **Bot usage** section: sessions, rounds and the Claude allowance.

Built by ``scripts/build_page.py`` from ``ledger/usage.jsonl`` and ``meta.yaml``, no
network (issue #20, section 4). Charts are inline SVG, so the page stays one
self-contained file with no script or style from elsewhere; a small inline script adds
the hover tooltips, and every value is also in a table.

1. **Sessions, by index**: API-equivalent cost, turns and web searches of every
   session on a MiniBench question, one panel each (three scales, so three charts, never
   a second axis), coloured by the main model; refused sessions as grey stubs; a line
   where each round starts.
2. **Question cadence per round**: each question's window as a bar, submitted or
   missed, with the periods of refused sessions shaded; the last ``PAGE_USAGE_ROUNDS``
   rounds.
3. **Allowance over time**: the CLI's 5-hour and 7-day utilization readings, with the
   window resets marked.
4. **Per-round table**: questions, share submitted, cost, estimated allowance, median
   searches, models, efforts, refused sessions.

A **round** starts after a gap of ``ROUND_GAP`` (72 hours) or more between question
openings in ``ROUND_TOURNAMENT``. A session is **refused** per ``allowance.refusal``:
``conclusion: usage_limit``, or for a record before issue #20 a one-turn, zero-cost
line with an empty ``by_model`` (inferred). The **estimated allowance** of a session is
its cost times the allowance points per dollar (``allowance.calibrate``: measured from
the CLI's readings once there are enough, else ``100 / ALLOWANCE_<5H|7D>_USD_EQUIV``),
computed here at build time, so a recalibration never rewrites the ledger.
"""

from __future__ import annotations

import datetime as dt
import html
import math
import os
import statistics
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))
import allowance as al

ROUND_TOURNAMENT = "minibench"
ROUND_GAP = dt.timedelta(hours=72)
DEFAULT_ROUNDS_SHOWN = 3
# Two refused sessions further apart than this, or with a served one between them, are
# two refusal periods; a period ends at the next served session or this long after its
# last refusal (about the next sweep), whichever is first.
REFUSAL_JOIN = dt.timedelta(minutes=75)
REFUSAL_TAIL = dt.timedelta(minutes=30)

# Chart colours by entity (the CSS defines each class in light and dark mode). The
# first three categorical slots validate all-pairs in both modes; a fourth family folds
# into "other". Windows take a validated pair of their own, so no colour means a model
# in one chart and a window in another.
FAMILY_CLASS = {"opus": "c-opus", "sonnet": "c-sonnet", "fable": "c-fable"}
FAMILY_LABEL = {"opus": "Opus", "sonnet": "Sonnet", "fable": "Fable", "other": "other"}
WINDOW_CLASS = {"five_hour": "c-5h", "seven_day": "c-7d"}
WINDOW_LABEL = {"five_hour": "5-hour window", "seven_day": "7-day window"}

CSS = r"""
.viz{background:var(--card);border:1px solid var(--line);border-radius:8px;padding:10px 12px;
margin:10px 0;overflow-x:auto}
.viz svg{display:block;width:100%;min-width:720px;height:auto}
.viz text{fill:var(--muted);font-size:11px;font-family:inherit}
.viz text.t{fill:var(--fg);font-weight:600}
.viz .grid{stroke:var(--grid);stroke-width:1}.viz .axis{stroke:var(--axis);stroke-width:1}
.viz .hit{fill:transparent}.viz .hit:hover+.mark,.viz rect.mark:hover{opacity:.75}
.legend{display:flex;flex-wrap:wrap;gap:4px 16px;font-size:.85rem;color:var(--muted);margin:2px 0 6px}
.legend i{display:inline-block;width:10px;height:10px;border-radius:2px;margin-right:6px;
vertical-align:-1px}.legend i.dot{border-radius:50%}
.c-opus{fill:#2a78d6;background:#2a78d6}.c-sonnet{fill:#eb6834;background:#eb6834}
.c-fable{fill:#1baf7a;background:#1baf7a}.c-other{fill:#52514e;background:#52514e}
.c-refused{fill:#898781;background:#898781}.c-band{fill:#898781;fill-opacity:.16;
background:rgba(137,135,129,.28)}
.c-ok{fill:#0ca30c;background:#0ca30c}.c-miss{fill:#d03b3b;background:#d03b3b}
.c-5h{fill:#6250d6;background:#6250d6;stroke:#6250d6}.c-7d{fill:#1baf7a;background:#1baf7a;stroke:#1baf7a}
.ring{stroke:var(--card);stroke-width:2}
:root{--grid:#e1e0d9;--axis:#c3c2b7}
@media (prefers-color-scheme:dark){:root{--grid:#2c2c2a;--axis:#383835}
.c-opus{fill:#3987e5;background:#3987e5}.c-sonnet{fill:#d95926;background:#d95926}
.c-fable{fill:#199e70;background:#199e70}.c-other{fill:#c3c2b7;background:#c3c2b7}
.c-5h{fill:#9085e9;background:#9085e9;stroke:#9085e9}.c-7d{fill:#199e70;background:#199e70;stroke:#199e70}}
.tip{position:fixed;z-index:9;pointer-events:none;max-width:340px;white-space:pre-line;
background:var(--card);color:var(--fg);border:1px solid var(--line);border-radius:6px;
padding:6px 9px;font-size:.8rem;line-height:1.4;box-shadow:0 2px 8px rgba(0,0,0,.15)}
.tip b{font-variant-numeric:tabular-nums}
"""

# One delegated listener for every mark: the tooltip text is set with textContent, since
# titles come from Metaculus. Its first line, the values, is set bold.
# The leading semicolon: this script follows build_page's sort script, which ends in a
# call; without it `(function(){...})` would be parsed as a call on that call's result.
TIP_JS = r"""
;(function(){var tip=document.createElement("div");tip.className="tip";tip.hidden=true;
document.body.appendChild(tip);
function show(el,x,y){var lines=el.getAttribute("data-tip").split("\n");tip.textContent="";
var b=document.createElement("b");b.textContent=lines[0];tip.appendChild(b);
if(lines.length>1){tip.appendChild(document.createTextNode("\n"+lines.slice(1).join("\n")))}
tip.hidden=false;var w=tip.offsetWidth,h=tip.offsetHeight;
tip.style.left=Math.min(x+14,window.innerWidth-w-8)+"px";
tip.style.top=(y+h+20>window.innerHeight?y-h-10:y+14)+"px"}
document.addEventListener("pointermove",function(e){
var el=e.target.closest&&e.target.closest("[data-tip]");
if(el){show(el,e.clientX,e.clientY)}else{tip.hidden=true}});
document.addEventListener("focusin",function(e){var el=e.target.closest&&e.target.closest("[data-tip]");
if(el){var r=el.getBoundingClientRect();show(el,r.right,r.top)}});
document.addEventListener("focusout",function(){tip.hidden=true})})();
"""


def _e(value: Any) -> str:
    return html.escape(str(value), quote=True)


def _f(x: float) -> str:
    return f"{x:.1f}".rstrip("0").rstrip(".")


# ------------------------------------------------------------------- data
@dataclass
class UsageSession:
    """One usage record as the page charts it."""

    ts: dt.datetime  # when the session ended (the record's ts)
    start: dt.datetime
    slug: str | None
    family: str
    cost: float
    turns: int
    searches: int
    refused: bool
    inferred: bool
    effort: str | None
    mode: str | None
    conclusion: str | None


@dataclass
class Question:
    slug: str
    title: str
    opened: dt.datetime
    closes: dt.datetime
    submitted: bool


@dataclass
class Round:
    number: int
    questions: list[Question]
    sessions: list[UsageSession] = field(default_factory=list)

    @property
    def start(self) -> dt.datetime:
        return min(q.opened for q in self.questions)

    @property
    def end(self) -> dt.datetime:
        return max(q.closes for q in self.questions)


def _number(value: Any) -> float:
    ok = isinstance(value, (int, float)) and not isinstance(value, bool)
    return float(value) if ok and not math.isnan(value) else 0.0


def parse_usage(records: list[dict[str, Any]]) -> list[UsageSession]:
    """Usage records as sessions, oldest first; a line without a time is skipped."""
    out = []
    for rec in records:
        ts = al._when(rec.get("ts"))
        if ts is None:
            continue
        refused, _until, inferred = al.refusal(rec)
        config = rec.get("config") if isinstance(rec.get("config"), dict) else {}
        out.append(
            UsageSession(
                ts=ts,
                start=ts - dt.timedelta(seconds=_number(rec.get("duration_s"))),
                slug=rec.get("slug"),
                family=al.model_family(rec.get("model_resolved") or rec.get("model")),
                cost=max(_number(rec.get("cost_usd_equiv")), 0.0),
                turns=int(_number(rec.get("num_turns"))),
                searches=int(_number(rec.get("web_searches"))),
                refused=refused,
                inferred=inferred,
                effort=config.get("effort"),
                mode=config.get("mode"),
                conclusion="usage_limit (inferred)" if inferred else rec.get("conclusion"),
            )
        )
    out.sort(key=lambda s: s.ts)
    return out


def tournament_questions(
    metas: list[tuple[str, dict[str, Any]]], tournament: str = ROUND_TOURNAMENT
) -> list[Question]:
    """The tournament's questions with a known window, in opening order."""
    out = []
    for slug, meta in metas:
        tour = meta.get("tournament")
        if not isinstance(tour, dict) or tour.get("slug") != tournament:
            continue
        opened, closes = al._when(tour.get("opened")), al._when(tour.get("closes"))
        if opened is None or closes is None:
            continue
        out.append(
            Question(slug, str(meta.get("title") or slug), opened, closes,
                     bool(tour.get("submitted")))
        )
    out.sort(key=lambda q: (q.opened, q.slug))
    return out


def rounds(
    questions: list[Question], sessions: list[UsageSession], gap: dt.timedelta = ROUND_GAP
) -> list[Round]:
    """Questions split where openings are ``gap`` or more apart, each with its sessions."""
    out: list[Round] = []
    for q in questions:
        if not out or q.opened - out[-1].questions[-1].opened >= gap:
            out.append(Round(len(out) + 1, []))
        out[-1].questions.append(q)
    where = {q.slug: r for r in out for q in r.questions}
    for s in sessions:
        if s.slug in where:
            where[s.slug].sessions.append(s)
    return out


def refusal_periods(sessions: list[UsageSession]) -> list[tuple[dt.datetime, dt.datetime]]:
    """Spans during which sessions were refused (all tournaments: the allowance is shared)."""
    periods: list[list[dt.datetime]] = []
    last_refused: dt.datetime | None = None
    open_period = False
    for s in sessions:
        if s.refused:
            if open_period and last_refused and s.start - last_refused <= REFUSAL_JOIN:
                periods[-1][1] = s.ts + REFUSAL_TAIL
            else:
                periods.append([s.start, s.ts + REFUSAL_TAIL])
            last_refused, open_period = s.ts, True
        elif open_period:
            periods[-1][1] = min(periods[-1][1], s.start)
            open_period = False
    return [(a, b) for a, b in periods]


@dataclass
class Rates:
    """Allowance points per dollar for each window and model family, and their source."""

    by: dict[tuple[str, str], tuple[float, str]]

    def points(self, s: UsageSession, window: str) -> float:
        return s.cost * self.by[(window, s.family)][0]


def rates(records: list[dict[str, Any]], cfg: al.Config) -> Rates:
    sessions = al.parse_sessions(records)
    by = {}
    for window in al.WINDOW_LENGTH:
        cal = al.calibrate(sessions, window)
        for family in (*FAMILY_LABEL, "mixed"):
            by[(window, family)] = cal.rate(family, cfg)
    return Rates(by)


def slug_usage(
    sessions: list[UsageSession], rate: Rates
) -> dict[str, dict[str, Any]]:
    """Per question: its models, efforts and modes, and its estimated 5-hour allowance."""
    out: dict[str, dict[str, Any]] = {}
    for s in sessions:
        if not s.slug:
            continue
        u = out.setdefault(s.slug, {"models": [], "efforts": [], "modes": [], "allowance": 0.0})
        if not s.refused and FAMILY_LABEL[s.family] not in u["models"]:
            u["models"].append(FAMILY_LABEL[s.family])
        for key, value in (("efforts", s.effort), ("modes", s.mode)):
            if value and value not in u[key]:
                u[key].append(value)
        u["allowance"] += rate.points(s, "five_hour")
    return out


# ------------------------------------------------------------------- svg helpers
W = 1100
LEFT, RIGHT = 58, 14


def _nice_max(value: float) -> float:
    if value <= 0:
        return 1.0
    mag = 10 ** math.floor(math.log10(value))
    for step in (1, 2, 2.5, 5, 10):
        if value <= step * mag:
            return step * mag
    return 10 * mag


def _ticks(top: float, n: int = 4) -> list[float]:
    return [top * i / n for i in range(n + 1)]


def _tick_label(value: float, unit: str) -> str:
    text = f"{value:,.0f}" if value >= 10 or value == 0 else f"{value:.2f}".rstrip("0").rstrip(".")
    return f"${text}" if unit == "$" else text


def _time_ticks(lo: dt.datetime, hi: dt.datetime) -> list[dt.datetime]:
    span = (hi - lo).total_seconds() / 3600
    step = next(h for h in (1, 3, 6, 12, 24, 48, 96, 168) if span / h <= 10)
    t = lo.replace(minute=0, second=0, microsecond=0)
    t -= dt.timedelta(hours=t.hour % step if step < 24 else t.hour)
    out = []
    while t <= hi:
        if t >= lo:
            out.append(t)
        t += dt.timedelta(hours=step)
    return out


def _time_label(t: dt.datetime) -> str:
    return t.strftime("%d %b") if t.hour == 0 else t.strftime("%d %b %H:%M")


def _legend(items: list[tuple[str, str, bool]]) -> str:
    """``(css class, label, dot?)`` swatches, in a row above the chart."""
    return '<div class="legend">' + "".join(
        f'<span><i class="{cls}{" dot" if dot else ""}"></i>{_e(label)}</span>'
        for cls, label, dot in items
    ) + "</div>"


# ------------------------------------------------------------------- charts
def sessions_chart(sessions: list[UsageSession], round_of: dict[str, int]) -> str:
    """Small multiples by session index: cost, turns, web searches (chart 1)."""
    if not sessions:
        return '<p class="muted">No sessions on MiniBench questions recorded yet.</p>'
    n = len(sessions)
    slot = (W - LEFT - RIGHT) / n
    bar = max(1.0, min(24.0, slot - 2 if slot > 4 else slot * 0.7))
    panels = [("API-equivalent cost", "$", [s.cost for s in sessions]),
              ("Turns", "", [float(s.turns) for s in sessions]),
              ("Web searches", "", [float(s.searches) for s in sessions])]
    ph, gap, top = 84, 30, 34  # the top band holds the round labels
    height = top + len(panels) * (ph + gap) + 4
    out = [(f'<svg viewBox="0 0 {W} {height}" role="img" aria-label="Cost, turns and web '
           f'searches of each of {n} sessions, coloured by model">')]
    for p, (title, unit, values) in enumerate(panels):
        y0 = top + p * (ph + gap) + 16  # top of the plot area
        base = y0 + ph
        ymax = _nice_max(max(values))
        out.append(f'<text class="t" x="{LEFT}" y="{y0 - 6}">{_e(title)}</text>')
        for t in _ticks(ymax, 2):
            y = base - t / ymax * ph
            out.append(f'<line class="{"axis" if t == 0 else "grid"}" x1="{LEFT}" x2="{W - RIGHT}" '
                       f'y1="{_f(y)}" y2="{_f(y)}"/>')
            out.append(f'<text x="{LEFT - 6}" y="{_f(y + 4)}" text-anchor="end">'
                       f'{_tick_label(t, unit)}</text>')
        for i, (s, v) in enumerate(zip(sessions, values, strict=True)):
            x = LEFT + i * slot + (slot - bar) / 2
            if s.refused:
                out.append(f'<rect class="c-refused" x="{_f(x)}" y="{_f(base - 3)}" '
                           f'width="{_f(bar)}" height="3"/>')
                continue
            h = max(v / ymax * ph, 1.0 if v > 0 else 0.0)
            r = 2 if bar >= 8 else 0
            out.append(f'<rect class="{FAMILY_CLASS.get(s.family, "c-other")}" x="{_f(x)}" '
                       f'y="{_f(base - h)}" width="{_f(bar)}" height="{_f(h)}" rx="{r}"/>')
    # round starts, then the index axis
    plot_bottom = top + len(panels) * (ph + gap) - gap + 16
    seen: set[int] = set()
    for i, s in enumerate(sessions):
        k = round_of.get(s.slug or "")
        if k is None or k in seen:
            continue
        seen.add(k)
        x = LEFT + i * slot
        out.append(f'<line class="axis" x1="{_f(x)}" x2="{_f(x)}" y1="4" '
                   f'y2="{plot_bottom}"/>')
        out.append(f'<text x="{_f(x + 4)}" y="13">Round {k}</text>')
    step = next(k for k in (1, 5, 10, 25, 50, 100, 250, 500) if n / k <= 12)
    for i in range(0, n, step):
        x = LEFT + (i + 0.5) * slot
        out.append(f'<text x="{_f(x)}" y="{plot_bottom + 14}" text-anchor="middle">{i + 1}</text>')
    # one hit column per session, all panels, carrying the tooltip
    for i, s in enumerate(sessions):
        tip = (f"${s.cost:.2f} · {s.turns} turns · {s.searches} searches\n"
               f"{FAMILY_LABEL[s.family]} · {s.conclusion or '—'}"
               f"{' · ' + s.mode if s.mode else ''}\n"
               f"{s.ts:%Y-%m-%d %H:%M} UTC · session {i + 1}\n{s.slug or ''}")
        out.append(f'<rect class="hit" x="{_f(LEFT + i * slot)}" y="{top}" width="{_f(slot)}" '
                   f'height="{plot_bottom - top}" data-tip="{_e(tip)}"/>')
    out.append("</svg>")
    families = [f for f in FAMILY_LABEL if any(s.family == f and not s.refused for s in sessions)]
    legend = [(FAMILY_CLASS.get(f, "c-other"), FAMILY_LABEL[f], False) for f in families]
    if any(s.refused for s in sessions):
        legend.append(("c-refused", "refused (usage limit)", False))
    return _legend(legend) + "\n".join(out)


def cadence_chart(rnd: Round, periods: list[tuple[dt.datetime, dt.datetime]]) -> str:
    """Each question's window as a bar, submitted or missed, refusals shaded (chart 2)."""
    lo = rnd.start - dt.timedelta(hours=1)
    hi = rnd.end + dt.timedelta(hours=1)
    span = (hi - lo).total_seconds()
    lanes: list[dt.datetime] = []  # when each lane is free again
    lane_of = []
    for q in rnd.questions:
        lane = next((i for i, free in enumerate(lanes) if free <= q.opened), None)
        if lane is None:
            lanes.append(q.closes)
            lane = len(lanes) - 1
        lanes[lane] = q.closes
        lane_of.append(lane)
    lane_h, top = 14, 8
    plot_h = len(lanes) * lane_h + 4
    height = top + plot_h + 24

    def x(t: dt.datetime) -> float:
        return LEFT + (t - lo).total_seconds() / span * (W - LEFT - RIGHT)

    out = [(f'<svg viewBox="0 0 {W} {height}" role="img" aria-label="Round {rnd.number}: '
           f'{len(rnd.questions)} question windows, submitted or missed">')]
    for a, b in periods:
        if b < lo or a > hi:
            continue
        a, b = max(a, lo), min(b, hi)
        tip = f"sessions refused\n{a:%d %b %H:%M} – {b:%H:%M} UTC"
        out.append(f'<rect class="c-band" x="{_f(x(a))}" y="{top}" width="{_f(max(x(b) - x(a), 2))}" '
                   f'height="{plot_h}" data-tip="{_e(tip)}"/>')
    for t in _time_ticks(lo, hi):
        out.append(f'<line class="grid" x1="{_f(x(t))}" x2="{_f(x(t))}" y1="{top}" '
                   f'y2="{top + plot_h}"/>')
        out.append(f'<text x="{_f(x(t))}" y="{top + plot_h + 16}" text-anchor="middle">'
                   f'{_time_label(t)}</text>')
    out.append(f'<line class="axis" x1="{LEFT}" x2="{W - RIGHT}" y1="{top + plot_h}" '
               f'y2="{top + plot_h}"/>')
    for q, lane in zip(rnd.questions, lane_of, strict=True):
        y = top + 2 + lane * lane_h
        cls, state = ("c-ok", "submitted") if q.submitted else ("c-miss", "missed")
        tip = f"{state}\n{q.opened:%d %b %H:%M} – {q.closes:%H:%M} UTC\n{q.title}"
        out.append(f'<rect class="{cls}" x="{_f(x(q.opened))}" y="{y}" '
                   f'width="{_f(max(x(q.closes) - x(q.opened) - 2, 2))}" height="{lane_h - 4}" '
                   f'rx="2" data-tip="{_e(tip)}"/>')
    out.append("</svg>")
    return "\n".join(out)


def allowance_chart(records: list[dict[str, Any]]) -> str:
    """The CLI's utilization readings over time, resets marked (chart 3)."""
    sessions = al.parse_sessions(records)
    points = [(s.ts, w, u) for s in sessions for w, (u, _r) in s.windows.items()
              if w in WINDOW_CLASS and u is not None]
    resets = sorted({(w, r) for s in sessions for w, (_u, r) in s.windows.items()
                     if w in WINDOW_CLASS and r is not None})
    if not points:
        return ('<p class="muted">No allowance reading recorded yet. The CLI reports '
                "utilization only at its warning thresholds (5-hour window: 90 %; 7-day: "
                "25, 50, 75 %); every session records the reset times it saw.</p>")
    lo = min(t for t, _w, _u in points) - dt.timedelta(hours=6)
    hi = max(t for t, _w, _u in points) + dt.timedelta(hours=6)
    span = (hi - lo).total_seconds()
    top, ph = 10, 150
    height = top + ph + 40

    def x(t: dt.datetime) -> float:
        return LEFT + (t - lo).total_seconds() / span * (W - LEFT - RIGHT)

    def y(u: float) -> float:
        return top + ph - min(u, 100) / 100 * ph

    out = [(f'<svg viewBox="0 0 {W} {height}" role="img" aria-label="{len(points)} allowance '
           'readings over time">')]
    for u in (0, 25, 50, 75, 100):
        out.append(f'<line class="{"axis" if u == 0 else "grid"}" x1="{LEFT}" x2="{W - RIGHT}" '
                   f'y1="{_f(y(u))}" y2="{_f(y(u))}"/>')
        out.append(f'<text x="{LEFT - 6}" y="{_f(y(u) + 4)}" text-anchor="end">{u} %</text>')
    for t in _time_ticks(lo, hi):
        out.append(f'<text x="{_f(x(t))}" y="{top + ph + 16}" text-anchor="middle">'
                   f'{_time_label(t)}</text>')
    for w, r in resets:
        if lo <= r <= hi:
            tip = f"{WINDOW_LABEL[w]} reset\n{r:%Y-%m-%d %H:%M} UTC"
            out.append(f'<rect class="{WINDOW_CLASS[w]}" x="{_f(x(r) - 1)}" y="{top + ph - 5}" '
                       f'width="2" height="10" data-tip="{_e(tip)}"/>')
    for t, w, u in points:
        tip = f"{u:.0f} %\n{WINDOW_LABEL[w]} · {t:%Y-%m-%d %H:%M} UTC"
        out.append(f'<circle class="{WINDOW_CLASS[w]} ring" cx="{_f(x(t))}" cy="{_f(y(u))}" '
                   f'r="4.5" data-tip="{_e(tip)}"/>')
    out.append("</svg>")
    present = [w for w in WINDOW_CLASS if any(pw == w for _t, pw, _u in points)]
    legend = [(WINDOW_CLASS[w], WINDOW_LABEL[w], True) for w in present]
    return _legend(legend) + "\n".join(out) + (
        '<p class="muted">Ticks on the axis: window resets, in the window\'s colour.</p>'
    )


def round_rows(rnds: list[Round], rate: Rates) -> list[dict[str, Any]]:
    """Chart 4's table, one dict per round (also written to ``results.json``)."""
    out = []
    for r in rnds:
        served = [s for s in r.sessions if not s.refused]
        out.append({
            "round": r.number,
            "start": r.start.isoformat(),
            "end": r.end.isoformat(),
            "questions": len(r.questions),
            "submitted": sum(q.submitted for q in r.questions),
            "cost_usd": round(sum(s.cost for s in r.sessions), 2),
            "allowance_7d_pct": round(sum(rate.points(s, "seven_day") for s in r.sessions), 1),
            "median_searches": statistics.median([s.searches for s in served]) if served else None,
            "models": sorted({FAMILY_LABEL[s.family] for s in served}),
            "efforts": sorted({s.effort for s in r.sessions if s.effort}),
            "modes": sorted({s.mode for s in r.sessions if s.mode}),
            "sessions": len(r.sessions),
            "refused": sum(s.refused for s in r.sessions),
        })
    return out


def _round_table(rows: list[dict[str, Any]]) -> str:
    head = ("<th>Round</th><th>Dates (UTC)</th><th>Questions</th><th>Submitted</th>"
            "<th>API cost</th><th>Est. allowance</th><th>Median searches</th>"
            "<th>Models</th><th>Efforts</th><th>Modes</th><th>Sessions</th><th>Refused</th>")
    body = []
    for r in rows:
        pct = r["submitted"] / r["questions"] if r["questions"] else 0
        start, end = al._when(r["start"]), al._when(r["end"])
        dates = f"{start:%d %b} – {end:%d %b %Y}" if start and end else "—"
        med = "—" if r["median_searches"] is None else _f(float(r["median_searches"]))
        body.append(
            f'<tr><td class="n">{r["round"]}</td><td>{_e(dates)}</td>'
            f'<td class="n">{r["questions"]}</td>'
            f'<td class="n">{r["submitted"]} ({pct:.0%})</td>'
            f'<td class="n">${r["cost_usd"]:,.2f}</td>'
            f'<td class="n">{r["allowance_7d_pct"]:.0f} % of 7 d</td>'
            f'<td class="n">{med}</td><td>{_e(", ".join(r["models"]) or "—")}</td>'
            f'<td>{_e(", ".join(r["efforts"]) or "—")}</td>'
            f'<td>{_e(", ".join(r["modes"]) or "—")}</td>'
            f'<td class="n">{r["sessions"]}</td><td class="n">{r["refused"]}</td></tr>'
        )
    return ('<div class="wrap"><table class="sortable"><thead><tr>' + head
            + "</tr></thead><tbody>" + "".join(body) + "</tbody></table></div>")


def rounds_shown() -> int:
    """``PAGE_USAGE_ROUNDS``: how many of the latest rounds chart 2 draws (default 3)."""
    try:
        value = int(os.environ.get("PAGE_USAGE_ROUNDS", "").strip())
    except ValueError:
        return DEFAULT_ROUNDS_SHOWN
    return value if value > 0 else DEFAULT_ROUNDS_SHOWN


@dataclass
class UsageSection:
    html: str
    rounds: list[dict[str, Any]]
    per_slug: dict[str, dict[str, Any]]
    rate_note: str


def build(
    records: list[dict[str, Any]],
    metas: list[tuple[str, dict[str, Any]]],
    cfg: al.Config | None = None,
    shown: int | None = None,
) -> UsageSection:
    """The whole section, its per-round rows and the per-question usage columns."""
    cfg = cfg or al.Config.from_env()
    shown = shown or rounds_shown()
    sessions = parse_usage(records)
    rate = rates(records, cfg)
    rnds = rounds(tournament_questions(metas), sessions)
    round_of = {q.slug: r.number for r in rnds for q in r.questions}
    mine = [s for s in sessions if s.slug in round_of]
    periods = refusal_periods(sessions)
    rows = round_rows(rnds, rate)
    (five, five_src), (seven, seven_src) = (
        rate.by[("five_hour", "mixed")], rate.by[("seven_day", "mixed")]
    )
    note = (f"allowance points per API-equivalent dollar: 5-hour window {five:.2f}, "
            f"{five_src}; 7-day window {seven:.2f}, {seven_src}")
    out = [
        "<h2>Bot usage</h2>",
        ('<p class="muted">Every Claude Code session on a MiniBench question, the windows '
         "of each round's questions, and the subscription allowance, from "
         "<code>ledger/usage.jsonl</code>. Hover a mark for its values; the tables below "
         "hold them all.</p>"),
        "<h3>Sessions, by index</h3>",
        f'<div class="viz">{sessions_chart(mine, round_of)}</div>',
        f"<h3>Question windows, last {min(shown, len(rnds)) or shown} round(s)</h3>",
    ]
    if rnds:
        out.append(_legend([("c-ok", "submitted", False), ("c-miss", "missed", False),
                            ("c-band", "sessions refused", False)]))
    else:
        out.append('<p class="muted">No MiniBench round recorded yet.</p>')
    for r in rnds[-shown:]:
        sub = sum(q.submitted for q in r.questions)
        out.append(
            f'<div class="viz"><p class="muted" style="margin:0 0 4px">'
            f"Round {r.number}: {r.start:%d %b %H:%M} – {r.end:%d %b %H:%M} UTC, "
            f"{len(r.questions)} questions, {sub} submitted</p>"
            f"{cadence_chart(r, periods)}</div>"
        )
    out += [
        "<h3>Allowance readings</h3>",
        f'<div class="viz">{allowance_chart(records)}</div>',
        "<h3>Per round</h3>",
        _round_table(rows) if rows else '<p class="muted">No round yet.</p>',
    ]
    per_slug = slug_usage(sessions, rate)
    return UsageSection("\n".join(out), rows, per_slug, note)
