# Output format

The format is fixed. Same content in `questions/<slug>/forecast.md` and in the chat reply.

## Header block (top of `forecast.md`, rewritten in place on every update)

```markdown
# <Question title>

| | |
|---|---|
| **Source** | Metaculus #43505 — <url> |
| **Type** | binary |
| **Opened / Closes / Resolves** | 2026-01-14 / 2027-12-31 / 2028-01-15 |
| **Status** | open |
| **Current forecast** | **Median 12.0%, IQR [8.0%, 18.0%]** (v2, 2026-09-30) |
| **Community** | hidden — not visible to the bot token |
| **Next review** | 2026-10-31 |
```

Everything below the header is **append-only**, newest version first, separated by `---`.

## A forecast version

```markdown
## v1 — Initial forecast — 2026-08-27

### What resolves YES
<one paragraph digest of resolution criteria + fine print, in your own words, naming the
resolution source and its release schedule. Flag edge cases.>

### Outside view
<reference class, n, window, raw base rate, source; time-scaling to the question window>

### Inside view
<causal decomposition, the chain or the paths, with numbers>

### Evidence
<what you found, what updated you and by how much (state likelihood ratios), what was absent>

### Other forecasters
| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus | hidden | — | the bot token cannot see the community prediction; no CP is logged |
| Polymarket | 11% | 2026-08-27 | $1.2M volume |
| Manifold | 15% | 2026-08-27 | low volume, discounted |

<explicit note on any material disagreement between sources, and where you sit vs. them and why>

### Scenarios
| # | Scenario | Weight | Implies |
|---|---|---|---|

### Sensitivity
| Assumption | If instead | Forecast becomes |
|---|---|---|

### What would change my mind (tripwires)
- [ ] <dated, observable signal> → <direction, magnitude in the units the forecast moves in>

### Sources
1. <Title> — <URL> (accessed 2026-08-27)

**Question**: [<question title>](<question url>)
**Date**: 2026-08-27
**Forecast**: Median 12.0%, IQR [8.0%, 18.0%]
**Thesis**: <1–3 sentences: the thesis and the main drivers/sources it rests on>
```

## An update version

Same structure, but **prepended above** the previous version, and it opens with the
revision table. Sections that did not change may be replaced by
`unchanged from v1` — never silently omitted.

```markdown
## v2 — Update — 2026-09-30

### Revision
| Driver | Direction | Effect |
|---|---|---|
| Prior (v1, 2026-08-27) | — | Median 12.0%, IQR [8.0%, 18.0%] |
| <one driver per row> | ↑ / ↓ / → | +3pp / −2pp / none |
| **New forecast** | | **Median 13.0%, IQR [9.0%, 19.0%]** |

### Tripwire check
| Tripwire from v1 | Fired? | Note |
|---|---|---|

<...remaining sections as above, or "unchanged from v1"...>

**Question**: [<question title>](<question url>)
**Date**: 2026-09-30
**Forecast**: Median 13.0%, IQR [9.0%, 19.0%]
**Thesis**: ...
```

## Non-binary questions

The summary block keeps native units:

```
**Forecast**: Median 87.8, IQR [80.4, 97.0]                    # numeric
**Forecast**: Median 2028-04-10, IQR [2027-09-09, 2028-12-24]  # date
**Forecast**: A 62.0%, B 25.0%, C 13.0%                        # multiple choice
```

For multiple choice, give the full option vector (summing to 100%) and, if useful, an IQR
on the leading option.

## The question link

The summary block's first line is always `**Question**: [<title>](<url>)`, taken from
`title` and `url` in `meta.yaml`. It applies to **both** `/forecast` (initial versions) and
`/update` (updates and re-analyses), and the chat reply opens with the same line followed by
`Date` / `Forecast` / `Thesis`. Use the canonical question URL (Metaculus `/questions/<id>/`,
or the market page for Kalshi/Polymarket/Manifold); for free-text questions with no URL, `url` in
`meta.yaml` is `null` (allowed only for `source: other` with no `post_id`) and the line is the
plain title, `**Question**: <title>` — never an empty `[title]()` link. The header `Source` row
then reads `other — no URL (free-text question)`. `new_question.py` does both for you. Versions written before this rule are append-only and stay as they are.

## Rounding

One decimal place on percentages. Do not imply precision you do not have — but do not round
to the nearest 5% either; that discards real information.

## Tournament short form (one-shot questions)

`new_question.py --tournament` scaffolds `templates/forecast-tournament.md`. Same header
block (with a **Tournament** row and **Community**: hidden — bot tournament) and the same
closing summary block; the version section carries only:

```markdown
## v1 — Initial forecast — 2026-10-19

### What resolves YES
### Outside view
### Inside view
### Evidence
### Other forecasters        (Metaculus: "hidden — bot tournament"; markets if any)
### What would change my mind
### Sources                  (≥ 5, numbered, `URL (accessed YYYY-MM-DD)`)

**Question**: [<title>](<url>)
**Date**: 2026-10-19
**Forecast**: Median 12.0%, IQR [8.0%, 18.0%]
**Thesis**: <1–3 sentences>
```

There is exactly one version: a tournament question is never revisited.
`log_forecast.py add` rewrites the header's **Current forecast** row from the logged numbers.

### The Metaculus comment

Bots must post a comment with every forecast (private; Metaculus publishes it after close).
`submit_metaculus.py` posts **the newest version block verbatim** — from the `## v1` heading
through the summary block, HTML comments removed — so it represents the actual reasoning and
final decision. Over 9,000 characters the middle is cut and marked `[... truncated ...]`; the
summary block always survives. Nothing is written twice and no model composes the comment.
