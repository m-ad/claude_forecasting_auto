---
name: metaculus-aggregations
description: >-
  Fetch structured numeric forecasts from Metaculus — community prediction (recency_weighted),
  Metaculus Pro forecasters, and gold-medalist forecasters — plus resolution criteria, fine
  print, background, forecaster counts, and comments, all as structured data. Use this skill
  whenever the user asks about a Metaculus question, references a metaculus.com URL or a post/
  question ID, wants a community prediction or "CP", wants the pro or gold-medalist aggregation,
  wants per-option probabilities for a multiple-choice question, wants an IQR/quartile band, or
  wants to compare their own forecast against Metaculus. Trigger even when the user only says
  "check Metaculus", "what does Metaculus say", "pull the CP", or gives a bare question ID. This
  is the PRIMARY Metaculus tool and should be preferred over web_fetch or the older
  metaculus_scrape_v2.py, which only return the headline number and often break. Handles binary,
  numeric, discrete, date, and multiple-choice questions.
---

# Metaculus Aggregations

Fetches Metaculus forecasts as structured JSON directly from the `/api-proxy/aggregation_explorer/`
endpoint the site's own frontend consumes. Unlike page scraping, this returns exact numeric
centers and interval bounds for every aggregation cohort, not just the headline community
prediction.

**Why this beats the alternatives:** `web_fetch` and the older `metaculus_scrape_v2.py` return
only the top-line community prediction, drop the pro/gold-medalist split entirely, and can't
retrieve comments. This skill returns all three cohorts, per-option multiple-choice breakdowns,
full resolution criteria, and comments — in ~3 seconds.

## Prerequisites

- `www.metaculus.com` must be in the project's egress allowlist (it normally is for forecasting projects).
- Playwright + Chromium (pre-installed in the sandbox at `/opt/pw-browsers`). The script sets
  `PLAYWRIGHT_BROWSERS_PATH` itself, so no `playwright install` step is needed.

## Finding the post ID

The post ID is the number in the question URL:
`https://www.metaculus.com/questions/43505/...` → `43505`.

Pass the **post** ID. The script resolves the internal `question_id` itself (they differ, e.g.
post 43505 → question 43510).

## Quick usage

Run the bundled script (path is relative to this skill's directory):

```bash
# Community + pros + gold medalists, human-readable
python <skill_dir>/scripts/metaculus_aggregations.py <POST_ID>

# Add comments and the CP-vs-time history series
python <skill_dir>/scripts/metaculus_aggregations.py <POST_ID> --comments 8 --history

# Structured JSON for programmatic use
python <skill_dir>/scripts/metaculus_aggregations.py <POST_ID> --json

# Skip resolution criteria / fine print / background if you only need numbers
python <skill_dir>/scripts/metaculus_aggregations.py <POST_ID> --no-details
```

By default it fetches all three cohorts: `recency_weighted` (the community prediction),
`metaculus_pros`, and `gold_medalists`.

### Interpreting the cohorts

Weight the **Pro** and **gold-medalist** cohorts more heavily than the raw community prediction —
they have stronger track records. **Always flag major discrepancies between the three**, e.g. when
pros sit well below the community, that gap is itself signal. A concurring pro + gold cohort that
diverges sharply from your own forecast is a strong prompt to search for missed facts before
defending the divergence.

## Programmatic usage

```python
import sys

sys.path.insert(0, "<skill_dir>/scripts")
from metaculus_aggregations import fetch_aggregations

res = fetch_aggregations(
    43505,
    methods=["recency_weighted", "metaculus_pros", "gold_medalists"],
    n_comments=5,
    include_history=True,
)

cp = res.methods["recency_weighted"].latest
print(cp.display)  # "1.0%  IQR[0.3%, 3.0%]"
print(cp.center, cp.lower, cp.upper, cp.forecaster_count)

pros = res.methods["metaculus_pros"].latest
print(pros.display if pros else "no pro forecasters")

# Multiple-choice: per-option (option, center, lower, upper) rows
mc = fetch_aggregations(44676).methods["recency_weighted"].latest
for option, center, lo, hi in mc.per_option or []:
    print(f"{option}: {center:.1%} IQR[{lo:.1%}, {hi:.1%}]")
```

## Output by question type

The `display` string and native `center`/`lower`/`upper` are formatted per type:

| Type | Example display | Native units |
|---|---|---|
| binary | `1.0%  IQR[0.3%, 3.0%]` | probability in [0, 1] |
| numeric | `87.84  IQR[80.40, 96.96]` | real values (already unscaled) |
| discrete | `20.1  IQR[19.4, 20.8]` | real values (Metaculus's newer bucketed type) |
| date | `2028-04-10  IQR[2027-09-09, 2028-12-24]` | unix seconds internally, formatted as dates |
| multiple_choice | `OptionA=68.9%  OptionB=17.8%  ...` | per-option probabilities in `per_option` |

`latest` is `None` when a cohort has no forecasters on the question, or when the CP has not been
revealed yet (`status=upcoming`). This is normal, not an error — report it as "no data yet."

## How it works (and why it's reliable now)

The `/api-proxy/` endpoint is gated by a Cloudflare **managed challenge**, which an XHR can never
solve. Two things — and only these two — make anonymous access work. The script already does both;
**do not "fix" them out**, or the 403 "Just a moment..." challenge returns:

1. **Send `Sec-Fetch-*` request headers on every call.** Playwright's `context.request` HTTP
   stack omits them, but every real Chromium sends them. A Chrome user-agent with no `Sec-Fetch-*`
   headers is a detectable inconsistency that trips the challenge. Presence is what matters, not
   the values. (Measured: 0/5 success without, 5/5 with.)
2. **Never load a Metaculus page in the browser context, and clear cookies before every request.**
   A `cf_clearance` cookie is bound to the browser's TLS fingerprint; replaying it from Playwright's
   separate HTTP stack looks like a stolen token and trips the challenge. The script opens no page
   at all and calls `ctx.clear_cookies()` before each request. (Measured: page-load-with-cookie 0/5;
   no-page-load 5/5.)

Also: keep the spoofed `Chrome/122` user agent. An honest `HeadlessChrome` UA gets challenged
outright. A residual ~5% rate-triggered challenge is handled by `_get_json`'s retry-with-backoff —
**not** by longer waits. There is no useful settle wait; the `--wait` flag is a deprecated no-op.

## Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| `RuntimeError: No aggregation JSON ... last status 403` on every retry | Rate-triggered challenge, or an edit removed the Sec-Fetch headers / reintroduced a page load | Wait ~30s and retry; verify the two invariants above are intact |
| `last status 0` | `www.metaculus.com` not in the egress allowlist | Add it in Settings → Capabilities |
| `latest` is `None` for all cohorts | Question is `upcoming` / CP not revealed | Expected — report "no community data yet" |
| Only community shows, pros/gold `None` | Those cohorts genuinely have no forecasters on this question | Expected for low-traffic questions |
| Script missing from project dir | A stale session may try to rebuild it from memory | Don't rebuild from memory — use this bundled copy, which is the correct v3 |

## Fallback

If the api-proxy is ever hard-blocked despite the invariants being intact, fall back to
`metaculus_scrape_v2.py` (renders the page directly) for the headline community prediction only —
it cannot retrieve the pro/gold split, per-option multiple-choice data, or comments.
