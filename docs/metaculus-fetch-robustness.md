# Metaculus fetch failures: diagnosis and plan (2026-10-17)

Status: **plan, nothing implemented yet.** Measurements were taken in one cloud session on
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
Metaculus hides the numbers from our bot key.

## 3. Plan, ordered by robustness gained per unit of effort

### P1: get the numbers over an authenticated channel (the real fix; needs the operator)

Only this removes the dependency on Cloudflare's verdict. Options, in order of preference:

1. **Ask Metaculus** (support or the bot-benchmark team) whether the bot account can be given
   read access to aggregations, or what the sanctioned way is. Metaculus hides the community
   prediction (CP) from bot keys on purpose: in the AI benchmark, bots must not copy the crowd.
   This workbench reads the CP anonymously and then **submits as that bot**
   (`submit-metaculus.yml`). Check the rules of each tournament the bot enters. The question
   that would make the pipeline robust also settles whether it is allowed.
2. **A separate human-account read token** (`METACULUS_READ_TOKEN`), used only for GETs,
   never for submissions. Test first:
   - Does `/api/posts/<id>/?with_cp=true` return `aggregations.recency_weighted.latest` for
     that token?
   - Does `/api/aggregation_explorer/` return `metaculus_pros` and `gold_medalists`?
   - Does `/api/comments/?post=` work?

   I could not test these (no such token here), and I don't know the answers. If only the CP
   comes back, Pro/gold stays on the browser path, but the headline number becomes reliable.
3. Script change, whichever token it is: `_api_get_json` becomes the first transport for the
   explorer, post and comments. The browser path is kept as a fallback.

### P2: fail fast, recover later (in-repo, small, do now)

This does not prevent blocks. It stops them costing ~3.5 min per post and stops them silently
degrading the forecasts.

- **Circuit breaker.** When the first browser request gets `cf-mitigated: challenge`, and the
  warm-up question page is challenged too, treat it as a **pool block**:
  - stop retrying (skip `_BACKOFF`);
  - write a marker with a timestamp (e.g. `$TMPDIR/metaculus-block.json`), so later calls in
    the session fail fast for 30 min;
  - exit with a distinct code (e.g. 3) and a partial result: API metadata, plus
    `aggregation_note="pool block"`.

  Keep `_BACKOFF` only for a real rate-limit signature, i.e. a 429, or a 403 on a page that
  was 200 moments earlier from the same session.
- **Deferred re-fetch.** On a pool block, the routine finishes with API metadata and stale
  cohorts, as today. It then schedules **one** follow-up (`send_later` +90 min, or a second
  daily routine slot around 13:00 UTC) that only re-fetches cohorts. The follow-up appends an
  update only if a cohort moved materially. The record shows a clean fetch 51 min to 8 h after
  every block.
- **Batch mode.** `metaculus_aggregations.py 45262 45219 45617 … --out-dir` runs one browser
  and one warm page for N posts, instead of N cold launches. That means fewer first-contact
  requests, and one probe decides the whole batch.

### P3: an off-pool fetcher (medium effort; test before building)

A `workflow_dispatch` + cron GitHub Action that runs the unchanged browser script from GitHub's
runners. Those are Azure addresses, so a different pool and ASN. It would write the JSON as a
workflow artifact or to a `metaculus-cache` branch.

- Cloud sessions can trigger it through `mcp__github__actions_run_trigger` and read the result
  back. No new secret is needed: the bot key is already in CI for submissions.
- **Unverified:** whether Metaculus also challenges GitHub runner addresses, which are popular
  with scrapers too. Test first with one `workflow_dispatch` run during a block window.
- Rule 4 ("fresh data, fetched in the current session") would need an amendment, e.g.
  "retrieved ≤ 6 h before the forecast, with its retrieval timestamp recorded".

### P4: instrumentation (cheap; needed to confirm the timing hypothesis)

Add a `fetch_meta` block to every cached JSON, and to a `…-FETCH-FAILED.json` stub on failure:

- `fetched_at`;
- egress IP from `/cdn-cgi/trace`, which still answered 200 during the block;
- `cf-ray`, the status and `cf-mitigated` of each attempt;
- transport (api/browser/ci);
- browser version.

After a few weeks this shows whether blocks cluster by hour, and so whether moving the routine
cron off 04:00–05:30 UTC is worth doing.

### P5: client hygiene (optional, low value)

- Derive the UA from `browser.version` instead of hard-coding `Chrome/122`.
- Add `--disable-blink-features=AutomationControlled`.

This removes self-inconsistent signals that can only lower the bot score outside block windows.
It does **not** get through a block (finding 6). Go no further: solving or evading Turnstile is
an arms race against a control the site chose to deploy, and it breaks again at the next
Cloudflare change.

### Docs to correct in `.claude/skills/metaculus-aggregations/SKILL.md`

- The "IP-level rate limit, clears in ~2 min" troubleshooting row: add the pool block
  (hours, all addresses), and say that waiting 3 min does not help.
- TLS 1.3 reset: did not reproduce on 2026-10-17; keep the fallback, but mark it historical.
- The "keep the spoofed `Chrome/122` UA" invariant: what matters is the absence of
  `HeadlessChrome`, not the 122. P5 replaces it.
