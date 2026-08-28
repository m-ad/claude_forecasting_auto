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

Extracts community predictions and comments from Metaculus question pages using Playwright
browser automation, routed through the container egress proxy.

## Prerequisites

- `metaculus.com` and `www.metaculus.com` must be in the project's egress domain allowlist
  (Settings → Capabilities → "Package managers + specific domains")
- Playwright + Chromium must be installed (pre-installed in most sessions; if not: `pip install playwright && python -m playwright install chromium`)

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

1. Parses the egress proxy credentials from `https_proxy` / `HTTPS_PROXY` env vars
2. Launches headless Chromium routed through the proxy
3. Navigates to `https://www.metaculus.com/questions/{post_id}/`
4. Waits for JS rendering (default 10s — Metaculus is a React SPA)
5. Extracts `innerText` from the fully rendered page
6. Parses prediction, metadata, and comments using text patterns

## Supported Question Types

| Type | Detection Pattern | Prediction Format |
|---|---|---|
| Binary | `<N>%\nCHANCE` in body text | `"42%"` |
| Date | `Current estimate\n<date>` | `"17 Mar 2028"` |
| Numeric | `Current estimate\n<number>` | `"1,234"` |

## Limitations

- **~10-15s latency** per scrape (Playwright launch + JS render wait)
- Only extracts comments visible on initial page load (typically ~20-30 most recent).
  "Load more comments" is not clicked.
- No authentication — only publicly visible data is extracted
- If Metaculus changes their page structure, the text-pattern parsing may break.
  The detection heuristics are intentionally simple for easy maintenance.

## Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| Cloudflare challenge page | `challenges.cloudflare.com` blocked | Add it to egress allowlist, or increase `--wait` |
| Empty body / short text | Page didn't fully render | Increase `--wait` to 15-20 |
| `Could not parse proxy URL` | Not in Claude.ai sandbox | Set `https_proxy` env var manually |
| `question_type: unknown` | New page layout or unsupported type | Check body text manually, update detection patterns |
