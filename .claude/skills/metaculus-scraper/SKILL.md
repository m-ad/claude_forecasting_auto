---
name: metaculus-scraper
description: >
  Scrape Metaculus questions to extract community predictions, resolution criteria, and comments
  using Playwright. Use this skill whenever the user asks about a Metaculus question, wants to
  look up a Metaculus prediction, needs the community forecast for a specific question ID, wants
  to compare Metaculus predictions, or references a metaculus.com URL. Also trigger when the user
  mentions "community prediction", "Metaculus question", "forecasting question", or provides a
  Metaculus post ID. This skill is required because the Metaculus API requires authentication and
  direct curl/fetch returns 403; Playwright with proxy is the only working access method in the
  Claude.ai sandbox.
---

# Metaculus Scraper

Extracts the headline community prediction and the resolution criteria from Metaculus question
pages using Playwright browser automation, routed through the container egress proxy.

> **This is the fallback, not the primary tool.** Prefer the **`metaculus-aggregations`** skill:
> it returns exact numbers for all three cohorts (community, Metaculus Pro, gold medalists),
> per-option multiple-choice breakdowns, and comment text as structured JSON. This script sees
> only what the page renders — one number, and no comments at all (see Limitations).

## Prerequisites

- `metaculus.com` and `www.metaculus.com` must be in the project's egress domain allowlist
  (Settings → Capabilities → "Package managers + specific domains")
- Playwright + Chromium (pre-installed in the sandbox at `/opt/pw-browsers`). The script sets
  `PLAYWRIGHT_BROWSERS_PATH` and pins the binary to `/opt/pw-browsers/chromium` itself — don't
  remove either, and don't run `playwright install`. Playwright demands the exact Chromium build
  *its own version* expects (1.62 wants build 1234) while the image ships an older one (1194)
  behind that stable symlink, so an unpinned launch fails outright.

## Quick Usage

Run the script at `scripts/metaculus_scrape.py` (relative to this skill's directory):

```bash
# Human-readable output
python <skill_dir>/scripts/metaculus_scrape.py <POST_ID>

# JSON output with more comments
python <skill_dir>/scripts/metaculus_scrape.py <POST_ID> --comments 10 --json

# Faster if you know the page loads quickly
python <skill_dir>/scripts/metaculus_scrape.py <POST_ID> --wait 8
```

### Finding the POST_ID

The post ID is the number in a Metaculus URL: `https://www.metaculus.com/questions/578/` → `578`.

### Output Fields

| Field | Description |
|---|---|
| `title` | Question title (from page `<title>`) |
| `question_type` | `binary`, `date`, `numeric`, or `unknown` |
| `community_prediction` | e.g. `"2%"` for binary, `"17 Mar 2028"` for date |
| `num_forecasters` | e.g. `"1.7k"` |
| `num_comments` | e.g. `"378"` |
| `resolution_criteria` | Full resolution text |
| `fine_print` | Fine print section (if present) |
| `comments` | List of `{author, text, author_prediction, date}` |

## Programmatic Usage (from Python)

```python
from metaculus_scrape import scrape_metaculus_question

result = scrape_metaculus_question(post_id=578, max_comments=5)
print(result.community_prediction)  # "2%"
print(result.question_type)  # "binary"
for c in result.comments:
    print(f"@{c['author']}: {c['text'][:100]}")
```

## How It Works

1. Parses the egress proxy from `https_proxy` / `HTTPS_PROXY` — **credentials are optional**; a
   bare `http://127.0.0.1:<port>` is normal and must not be rejected
2. Launches headless Chromium routed through that proxy, with the binary pinned
3. Navigates to `https://www.metaculus.com/questions/{post_id}/`
4. Waits for JS rendering (default 10s — Metaculus is a React SPA)
5. Clicks the **"Question Info"** tab, which is where the resolution criteria now live
6. Extracts `innerText` from the fully rendered page
7. Parses prediction and metadata using text patterns

### Two failure modes it handles automatically

- **TLS 1.3 reset.** Through a MITM egress proxy, Chromium's TLS 1.3 ClientHello is reset and the
  browser can reach *nothing at all* (`net::ERR_CONNECTION_RESET`, for any host). The script
  retries the launch with `--ssl-version-max=tls1.2`, which fixes it. Force it up front with
  `METACULUS_FORCE_TLS12=1`. This is a property of the local proxy, not of Metaculus.
- **Cloudflare rate-limit block.** Metaculus rate-limits by IP and answers over-quota clients with
  a "Just a moment..." challenge — on ordinary HTML pages too, not just the API. Measured to clear
  after ~2 min, so the script backs off across ~3 min before giving up. A challenge is raised as an
  error, never parsed: a blocked fetch must not masquerade as "no community prediction".

## Supported Question Types

| Type | Detection Pattern | Prediction Format |
|---|---|---|
| Binary | `<N>%\nCHANCE` in body text | `"42%"` |
| Date | `Current estimate\n<date>` | `"17 Mar 2028"` |
| Numeric | `Current estimate\n<number>` | `"1,234"` |

## Limitations

- **Comments are not available from this path.** Metaculus moved them behind a lazy-loaded tab
  that does not survive a scripted click, so `comments` comes back empty and the CLI says so
  explicitly. Use `metaculus-aggregations --comments N` for comment text. Don't report an empty
  list here as "no discussion".
- **Only the headline number.** No pro/gold-medalist split, no per-option multiple-choice data,
  no IQR. Those need `metaculus-aggregations`.
- **~25s latency** per scrape (Playwright launch + JS render wait + the Question Info click);
  longer if it has to ride out a rate-limit block.
- No authentication — only publicly visible data is extracted.
- If Metaculus changes their page structure again, the text-pattern parsing will break. It already
  did once: the resolution criteria moved behind a tab, which silently emptied that field while
  the community prediction kept working.

## Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| `Cloudflare was still challenging ... after 170s` | IP-level rate-limit block | Wait 2–3 min. A shared sandbox egress IP trips this easily — batch questions, don't loop |
| `Could not load ...: net::ERR_CONNECTION_RESET` | TLS 1.3 reset by the egress proxy, on both attempts | Try `METACULUS_FORCE_TLS12=1`; check that any page loads at all |
| `Executable doesn't exist at .../chromium_headless_shell-<n>` | Playwright upgraded past the Chromium build the image ships | The script pins `/opt/pw-browsers/chromium`; override with `PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH` if needed |
| `Looks like Playwright was just installed... run playwright install` | `PLAYWRIGHT_BROWSERS_PATH` unset | The script sets it when `/opt/pw-browsers` exists; don't remove that |
| Empty `resolution_criteria` | The "Question Info" tab was renamed or didn't mount | Dump `inner_text("body")` and update the tab label / section markers |
| Empty `comments` | Expected — see Limitations | Use `metaculus-aggregations --comments N` |
| `question_type: unknown` | New page layout or unsupported type | Check body text manually, update detection patterns |
