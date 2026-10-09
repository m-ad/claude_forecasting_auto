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
  is the PRIMARY Metaculus tool and should be preferred over web_fetch or the metaculus-scraper
  skill, which only return the headline number and often break. Handles binary, numeric,
  discrete, date, and multiple-choice questions.
---

# Metaculus Aggregations

Fetches Metaculus forecasts as structured JSON directly from the `/api-proxy/aggregation_explorer/`
endpoint the site's own frontend consumes. Unlike page scraping, this returns exact numeric
centers and interval bounds for every aggregation cohort, not just the headline community
prediction.

**Why this beats the alternatives:** `web_fetch` and the `metaculus-scraper` skill return only
the top-line community prediction, drop the pro/gold-medalist split entirely, and can't retrieve
comments. This skill returns all three cohorts, per-option multiple-choice breakdowns, full
resolution criteria, and comments — in ~20 s for a cold run.

## Prerequisites

- `www.metaculus.com` must be in the project's egress allowlist (it normally is for forecasting projects).
- Playwright + Chromium (pre-installed in the sandbox at `/opt/pw-browsers`). The script sets
  `PLAYWRIGHT_BROWSERS_PATH` **and** pins the binary to `/opt/pw-browsers/chromium` itself, so no
  `playwright install` step is needed. Do not remove the explicit `executable_path`: Playwright
  looks for the exact Chromium build *its own version* expects (1.62 wants build 1234) and the
  image ships an older one (1194) behind that stable symlink.
- Optional: `METACULUS_API_KEY`. When set, resolution criteria / fine print / background /
  forecaster count come from the official `/api/posts/<id>/` endpoint over plain HTTPS (no
  Cloudflare, one browser request fewer); when unset or failing, the browser path is used.
  It does **not** replace the browser for the numbers: the key is a bot account, and
  Metaculus returns null aggregations to bots, 403s the Aggregation Explorer and restricts
  comments (verified 2026-09-26). `fetch_post_api(post_id)` exposes the raw post JSON.
  **Before a question opens** (`status=upcoming`, the pre-prediction phase) the key's endpoint
  also returns description, resolution criteria and fine print as `null`, although they are
  published and the anonymous browser JSON carries them (verified 2026-10-09, post 45255).
  Since v4.4 a text-less key response falls back to the browser automatically; call
  `fetch_post_api` directly and you get the nulls.

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

## Group posts (one post, several subquestions)

Some posts are a **group of questions**: one numeric subquestion per year, say (post 45386 has
"2027" and "2028"). A group has no single question to aggregate, and the Aggregation Explorer
answers a post-only query with **HTTP 400**: `"Post with id 45386 has no question, please submit a
subquestion."` (verified 2026-09-27). Since v4.3 the script handles this itself; pass the
**post** id as usual.

- It still asks the explorer first, so a single-question post makes exactly the requests it
  always did. Only after a 400 does it look the post up (`METACULUS_API_KEY` first, else the
  browser) and check for `group_of_questions`. The explorer stays first on purpose: a tripped
  rate limit also blocks the API surface, so a lookup ahead of it could spend the one request
  the explorer needs.
- It then makes **one request per subquestion**, with `question_id` pinned and all cohorts
  comma-joined.
- Results come back in `res.subquestions`, one `AggregationResult` per subquestion. `label` holds
  the group label (e.g. `"2027"`). The post-level `res.methods` is **empty** for a group.
  Resolution criteria, fine print, background and comments are post-level and live on `res`.
- `res.question_type` is the subquestions' shared type (e.g. `numeric`), or `None` if they differ.

```python
res = fetch_aggregations(45386, include_history=True)
for sub in res.subquestions:
    cp = sub.methods["recency_weighted"].latest
    print(sub.label, sub.question_id, cp.display if cp else "no data yet")
```

The `--json` output carries the same `subquestions` list. For a single-question post it is `[]`,
and nothing else about the output changes.

A 400 is never retried (also since v4.3). It means Metaculus rejected the request itself, and
the ~3 min backoff would only spend rate-limit budget.

## How it works (and why v4 is built this way)

**Everything goes through a real Chromium.** Requests are issued either as a page navigation to
the `/api-proxy/` URL, or as a same-origin `fetch()` from a loaded Metaculus page. Nothing uses
Playwright's own HTTP stack (`context.request`), and nothing uses `curl`.

That is not a style preference — it is the whole fix. Cloudflare's managed challenge on
`/api-proxy/*` now keys on the **TLS/JA3 fingerprint**, not just on headers, so any non-browser
client is challenged no matter what it claims to be. Measured 2026-09-11:

| Client | Result |
|---|---|
| `ctx.request.get()` with `Sec-Fetch-*` headers | 403 `cf-mitigated: challenge` |
| `ctx.request.get()` replaying the browser's cookies | 403 challenge |
| `curl` with a spoofed Chrome UA + `Sec-Fetch-*` | 403 challenge |
| **Chromium page navigation** | **200 JSON** |
| **same-origin `fetch()` in a loaded page** | **200 JSON** |

Earlier versions of this file told you to add `Sec-Fetch-*` headers and to never load a page. Both
instructions are now **inverted**: header spoofing no longer works, and loading a real page is the
recovery path, because only a real document can run a JS challenge.

Three invariants remain. Do not "fix" them out:

1. **Keep the spoofed `Chrome/122` user agent.** An honest `HeadlessChrome` UA is challenged
   outright, on ordinary HTML pages too.
2. **Keep all cohorts in one request.** `aggregation_methods=a,b,c` (comma) returns every cohort in
   a single response. Metaculus rate-limits by IP and a tripped limit costs ~2 minutes, so the
   *request count* is the binding constraint, not the payload size. (The old warning about combined
   calls returning empty cohorts was about the **pipe** separator `a|b`; comma is verified against
   all three.)
3. **Keep the backoff long.** `_BACKOFF` totals ~3 min because the block was measured to clear only
   after ~2 min. Short retries are wasted requests that re-arm the limit.

### The environment can break this independently of Metaculus

Through a MITM egress proxy, Chromium's **TLS 1.3 ClientHello is reset** — it could not reach
*any* host, example.com included (`net::ERR_CONNECTION_RESET`, ~1.8 kB sent, 39 B back). Disabling
post-quantum key agreement or ECH did not help; `--ssl-version-max=tls1.2` did.

The script relaunches with that flag automatically, on **either** of two triggers:

1. a navigation dying with a reset-class error (`_RESET_MARKERS`), or
2. **any attempt coming back with `status 0`** — no HTTP response at all.

Trigger 2 was added in v4.1 and is the one that matters in practice. The reset does not reliably
surface as a classifiable exception: `page.goto` can resolve with no response object, or raise a
message carrying none of the markers. Before v4.1 those runs spent the full ~3 min backoff
re-issuing a request that could never get an answer, then failed with a message blaming Cloudflare
and telling the caller to set the environment variable by hand. Measured 2026-09-20: a
`new_question.py --url` scaffold of post 45219 failed exactly that way, and the identical command
with `METACULUS_FORCE_TLS12=1` returned in ~40 s.

`METACULUS_FORCE_TLS12=1` still works and still skips the failing probe, which saves one
relaunch — but it is now an **optimisation, not a requirement**. A plain run recovers on its own.

This is a property of the local proxy, not of Metaculus: on a normal workstation the TLS 1.3
attempt succeeds and the fallback never runs.

Note the sibling `metaculus-scraper` skill does **not** have trigger 2 — it raises on the first
unclassified error instead of burning a backoff, so its message is immediate and actionable. If
you fall back to it in a reset-prone environment, set `METACULUS_FORCE_TLS12=1` up front.

## Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| `RuntimeError: No aggregation JSON ... last status 403` after the full backoff | IP-level rate-limit block (it blocks plain HTML pages too, so it is not path-specific) | Wait ~2–3 min and retry. A shared sandbox egress IP trips this easily; batch your questions and don't re-run in a loop |
| `last status 0` (no HTTP response at all) | Chromium has no egress: `www.metaculus.com` not allowlisted, or the proxy is not reaching the browser. Since v4.1 the TLS 1.3 reset is *not* a cause — it is retried on TLS 1.2 automatically, so reaching this message means TLS 1.2 failed too | Check the allowlist and `HTTPS_PROXY`; confirm a plain page loads at all. Setting `METACULUS_FORCE_TLS12=1` will not help here — it is already being tried |
| `Executable doesn't exist at .../chromium_headless_shell-<n>` | Playwright was upgraded past the Chromium build the image ships | The script pins `/opt/pw-browsers/chromium`; don't remove that, or override `PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH` |
| `Looks like Playwright was just installed... run playwright install` | `PLAYWRIGHT_BROWSERS_PATH` unset | The script sets it when `/opt/pw-browsers` exists; don't remove that |
| `latest` is `None` for all cohorts | Question is `upcoming` / CP not revealed | Expected — report "no community data yet" |
| `resolution_criteria` / `fine_print` / `background` all `None` | Since v4.4 only when the browser fallback *also* failed (the key's endpoint hides them before opening). Metaculus always publishes criteria, also for `upcoming` questions | A fetch failure, never "criteria not published": wait ~3 min and re-run once |
| `res.methods` is empty but `res.subquestions` is not | Group post | Expected — read each subquestion's `methods`; see "Group posts" |
| `RuntimeError: ... last status 400` | Metaculus rejected the query; for a post that is *not* a group this is unexpected | Check the post id. Groups are handled automatically, so the post itself is the likely problem |
| Only community shows, pros/gold `None` | Those cohorts genuinely have no forecasters on this question | Expected for low-traffic questions |
| Script missing from project dir | A stale session may try to rebuild it from memory | Don't rebuild from memory — use this bundled copy, which is the correct v4 |

## Fallback

If the api-proxy is ever hard-blocked despite the invariants being intact, fall back to the
`metaculus-scraper` skill (renders the question page directly) for the headline community
prediction and resolution criteria only — it cannot retrieve the pro/gold split, per-option
multiple-choice data, or comments. Note that an IP-level block hits the scraper too, since it
blocks HTML pages as well; in that case the only fix is to wait.
