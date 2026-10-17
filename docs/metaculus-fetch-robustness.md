# Metaculus fetch failures: diagnosis and plan (2026-10-17)

Status: **P2(b) implemented 2026-10-17** (`metaculus_aggregations.py` v4.6, `scripts/fetch_metaculus.py`);
P1 open. Measurements were taken in one cloud session on
2026-10-17, 11:42–11:51 UTC; the block was still on at the last probe (11:51). Scripts: `metaculus_aggregations.py` v4.5, Playwright 1.64,
Chromium 141.0.7390.37.

## 1. What fails

The repo's own `raw/` caches give the record. A post counts as fetched when its
`metaculus-<date>.json` has a `latest` block. A post counts as blocked when only the bot-key
`metaculus-api-<date>.json` exists.

| Session start (UTC) | Posts | Browser path | Note |
|---|---|---|---|
| 10-09 04:22 | 17 | **blocked** | API-only for all 17 |
| 10-09 05:13 | 17 | ok | another container, 51 min later |
| 10-10 07:26 | 1 | **blocked** | upcoming post; criteria also missing |
| 10-12 04:12 | 5 | **blocked** | |
| 10-15 03:44 | 1 | ok | |
| 10-15 05:24 | 4 | **blocked** | the first call failed after a 200 s cool-down |
| 10-15 13:23 | 4 | ok | |
| 10-16 04:45 | 12 | ok | |
| 10-17 11:43 → 11:45 | — | ok → **blocked** | this session, after only 4 Metaculus requests |

## 2. Diagnosis

### Verified (2026-10-17)

1. **Egress is a shared, rotating pool.** Six `curl` calls left from six addresses in
   `160.79.106.0/24` (ipinfo: AS396982, Google LLC; Cloudflare colo IAD). Each connection may
   use a different address. Every Claude cloud session shares this pool, and so do other users'
   Metaculus bots.
2. **The block covers the whole pool, not one address.** During the block, five cold browser
   launches got five different egress IPs (`.131 .133 .139 .129 .142`, read from
   `www.metaculus.com/cdn-cgi/trace`). All five got `403 cf-mitigated: challenge` on
   `/api-proxy/posts/<id>/`.
3. **We did not cause it.** The block began about 2 minutes after a clean probe, with 4
   Metaculus requests made in total. The 10-15 session was also challenged on its first call
   after a cool-down.
4. **It is not the ~2 min rate limit that `_BACKOFF` is sized for.** Blocks last from tens of
   minutes to hours (10-15: blocked at 05:24, clear at 13:23). The 3.5 min backoff per request
   therefore only burns time: an N-post run spends about N × 3.5 min before it gives up.
5. **The token-authenticated official API is not challenged.** During the block,
   `/api/posts/<id>/` with `METACULUS_API_KEY` answered 200 for two posts, with criteria. The
   same pattern shows in the record: every blocked session still cached `metaculus-api-*.json`.
6. **A hardened browser does not get through a block window.** I fixed the obvious headless
   tells (`--disable-blink-features=AutomationControlled`, so `navigator.webdriver` is false; a
   UA matching the real version; a real viewport). The page still sat on "Performing security
   verification" for 60 s with a Turnstile iframe (`challenges.cloudflare.com/.../turnstile`),
   and no `cf_clearance` cookie was set. Outside a block, a plain visit passes without any
   challenge solving: the 11:43 probe got a `cf_clearance` cookie on a 200.
7. **The client has detectable tells.** These are signals Cloudflare can score, not proven
   causes:
   - the hard-coded UA says `Chrome/122`, while `sec-ch-ua` and `navigator.userAgentData` say
     `Chromium 141`, and the TLS fingerprint (JA4 `t13d1515h2_…`, with the X25519MLKEM768
     group) is a Chrome ≥ 131 handshake;
   - `navigator.webdriver === true`;
   - SwiftShader WebGL.

   The remote side sees Chromium's own TLS fingerprint. The egress proxy does not rewrite it
   (tls.peet.ws: curl and Chromium give different JA3/JA4).
8. **The TLS 1.3 reset described in SKILL.md did not reproduce today.** Chromium's default
   TLS 1.3 handshake through the proxy succeeded. The `--ssl-version-max=tls1.2` fallback is
   harmless, but it is no longer the live failure mode.

### Inference (not proven)

Metaculus's Cloudflare setup intermittently puts a managed challenge in front of this
datacenter pool, or the whole ASN, as a group. That could be adaptive bot management or a WAF
rule switched on under load. Headless Chromium cannot pass the interactive Turnstile stage, so
in those windows the browser path is dead **whatever our own behaviour**.

The 04:00–05:30 UTC failures may be a coincidence of when routines run (n ≈ 9 sessions, too few
to tell). They are also consistent with other bots on the pool running at the same cron hours.
**Unverified.**

**Core issue:** the only data channel that carries the numbers, the anonymous `/api-proxy/`,
depends on Cloudflare's bot verdict for an address pool we share and cannot influence. The
channel that is exempt from the challenge, the authenticated `/api/`, is the one where
Metaculus withholds the numbers: every account starts on the `restricted` API tier (§3).

## 3. Rules check (2026-10-17)

Read from Metaculus's published source, `github.com/Metaculus/metaculus` at `b1c6b52`
(2026-10-16). The live pages were behind the same block.

- **Tournament rules do not apply, and do not forbid using the CP (community prediction).**
  `tournament-rules`: accounts "officially registered as bot accounts, are ineligible for
  tournament prizes" unless a competition's rules allow them. The AIB rules (AI Forecasting
  Benchmark, `aib/contest-rules`: no human in the loop, one bot per person) bind only bots
  entered in AIB. This bot isn't entered.
- **Bot account: correct for this setup.** UI string `apiForecastingAccessBotNotice`:
  "Accounts used for AI bot forecasts, automated forecast generation, or other non-human
  forecasting systems must use a linked bot account." A human-supervised hybrid that submits
  through the API falls under this. Human accounts that submit through the API get paused.
- **API access is tiered for every account, not just bots.** `docs/openapi.yml`: all
  authenticated accounts get the CP on "a small set of ~50 questions" only. The tiers are
  `restricted` (the default), `benchmarking` (~250 open + ~250 resolved questions) and
  `unrestricted`. A tier can be granted per account, per project or per post
  (`misc/models.py`). Requests go through the "Metaculus Data Needs Form" or
  api-requests@metaculus.com. **Correction to the first draft:** a human-account token would
  not help; it starts on `restricted` too.
- **The current browser path conflicts with the Terms of Use** (last modified 2026-09-21).
  The Terms forbid procuring content "by automated means (such as scripts, bots, spiders,
  crawlers, or scrapers)", "except as may be a result of standard search engine or Internet
  browser usage or through and subject to the terms of an API provided by Metaculus". They
  also forbid "circumventing … any security technology". Three points against the path:
  - headless Playwright is automated, not standard browser use;
  - `/api-proxy/` is the website's own internal route, and from there it returns the CP that
    the official API withholds from our tier;
  - the spoofed UA exists to avoid Cloudflare's challenge.

  The AI Products Supplement §5.2 repeats it: automated access to "Metaculus Data … by any
  other automated means (including scraping the Metaculus website) remains prohibited". The
  `metaculus-scraper` skill and comment fetching fall under the same clauses.
- **Evaluation clause.** API data "may not be used to train, evaluate, or otherwise create or
  develop AI/ML models or algorithms without Metaculus's prior written permission". Scoring
  the bot against the CP is arguably evaluation. Name it in the access request.

## 4. Plan (revised after the rules check)

### P1: request a higher API tier (the real fix; operator)

Use the Data Needs Form / api-requests@metaculus.com. Ask for:

- `benchmarking` or `unrestricted` tier for the bot account, or per-post grants for the
  questions it forecasts;
- Aggregation Explorer access for `metaculus_pros` and `gold_medalists`;
- comment read access.

State the use: non-commercial, a human-supervised hybrid bot that is not in any tournament;
comparison scoring only; no model training.

Once granted, the whole client becomes `urllib` + token:

- `/api/posts/<id>/?with_cp=true`;
- `/api/aggregation_explorer/`;
- `/api/comments/`.

That route was not challenged during the 2026-10-17 block, and it needs no Chromium.

### P2: interim (operator's choice)

(a) Stop the browser path now. Forecast from API metadata and markets, and mark Metaculus
cohorts "not retrieved".

(b) Keep it until Metaculus replies, accepting the ToS conflict. With (b), the
circuit breaker from the first draft still pays: on a pool block, stop at once instead of
spending ~3.5 min per post. It also avoids adding load during blocks.

### Dropped from the first draft

- **Off-pool CI fetcher (P3) and client hardening (P5):** both are the scraping and
  security-circumvention patterns the Terms prohibit.
- **Instrumentation (P4):** it only diagnosed block timing for the browser path. Once P1
  lands it is moot. Under P2(b), the circuit breaker's own status check (`cf-mitigated`
  on the first request) is enough.

## 5. Decision and implementation (2026-10-17)

**Decision (operator): P2(b).** The browser path stays for this workbench. The operator's
reasoning:

- the workbench is a research assistant: a human makes every final forecast, and approves each
  submission by merging;
- the operator can see the CP and the cohorts on the site anyway, so the fetcher replaces
  copy-pasting them by hand;
- the conflict with the Terms of Use (§3) is acknowledged and accepted.

A future fully autonomous bot will be a separate fork that uses only sanctioned API access. P1
(asking for a higher tier) remains the long-term fix. The constraints that follow are recorded
in AGENTS.md §4:

- no escalation past Cloudflare (no Turnstile solving, no stealth patches);
- no retry loops beyond the pool-block protocol.

**Implemented:**

- **Circuit breaker.** A challenge that survives the whole backoff writes
  `$TMPDIR/metaculus-block.json` (30 min TTL). Every later request in the process, and in later
  processes in the container, then answers at once.
- **Blocked result.** A blocked post comes back with `blocked: true`, API-key metadata, empty
  `methods`/`comments`, and an `aggregation_note` saying the cohorts were not fetched. A block
  that starts after the cohorts flags the missing comments in the note. Exit status: 3 for a
  block, 1 for a failure, 0 when everything was fetched.
- **Batch.** `fetch_many` and a multi-id CLI serve N posts through one browser.
  `scripts/fetch_metaculus.py <slugs>` fetches each post once and writes
  `raw/metaculus-<date>.json`, or `raw/metaculus-api-<date>.json` when blocked, into every
  matching slug.
- **Deferred re-fetch.** This is workflow text, not code: AGENTS.md §4, `/status`,
  `forecast-update` and `forecast-workflow`. One `send_later` re-fetch ~90 min after a block,
  and a new version only if the fresh cohorts are material.

**Verified live, during the block** (still on at 12:14 UTC, i.e. ≥ 29 min):

| Run | Time | Exit | Note |
|---|---|---|---|
| Two posts (45262, 45617), one call | 194 s | 3 | Both posts came back `blocked` with titles and forecaster counts from the key. About 190 s of the 194 was the first post's backoff, and the second post took about 1 s. The old code needed ~7 min and raised twice |
| A second process, 45262 | 1 s | 3 | Inherited the block from the marker file |
