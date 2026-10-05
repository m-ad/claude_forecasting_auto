# What will be the total OpenRouter token usage December 21-27, 2026?

| | |
|---|---|
| **Source** | Metaculus #45689 — https://www.metaculus.com/questions/45689/what-will-be-the-total-openrouter-token-usage-december-21-27-2026 |
| **Type** | numeric (tokens; range 100T–700T, open both bounds) |
| **Opened / Closes / Resolves** | 2026-10-06 (scheduled) / 2026-12-01 / 2026-12-29 |
| **Status** | open |
| **Current forecast** | **Median 330T, IQR [250T, 430T]** (v1, 2026-10-05) |
| **Community (as of 2026-10-05)** | hidden: question opens 2026-10-06 17:00 UTC, CP reveal 2026-10-10 17:00 UTC (n=5 pre-open) |
| **Next review** | 2026-10-13 |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-10-05

### What resolves YES

Resolves to the value shown for the **Dec 21 bar** (Monday–Sunday, Dec 21–27, 2026) in the
"Top Models: Weekly usage of models across OpenRouter" chart on openrouter.ai/rankings,
**including its displayed rounding** (e.g. "127T"). If OpenRouter changes the bin start day,
the last full week falling within 2026 is used [1]. **Checked: what the bar means.** The chart's
JSON (`/api/frontend/v1/rankings/model-rankings-chart`) gives, per week, the top 9 models plus an
`Others` bucket. For the week of 2026-09-07 those sum to **126.76T**, which matches the question's
own example of "127 trillion" [2]. So the resolution value is **total platform tokens** (prompt +
completion, excluding requests marked private), not just the top 10. The background's phrase
"top ten models alone totaled 127T" is loose wording. Edge cases: display rounding (the nearest
1T, or coarser if the value exceeds 1 quadrillion); OpenRouter restating figures as snapshots
refresh [3]; a change of bins or chart definition (re-analyse if it happens).

### Outside view

**Reference class: the platform's own 12-week growth multiples over the past year** (n=40
overlapping windows, Oct 2025–Sep 2026) [2]: 10th percentile 1.55×, 25th 2.04×, **median 2.43×**,
75th 2.75×, 90th 3.13×, minimum 1.11×. Applied to the last complete week (Sep 28–Oct 4:
**165.9T**), that gives a median of **≈ 403T**, IQR ≈ 338–456T.

Caveats on that class:
1. It comes from a single hypergrowth regime: about 33× in 12 months (5.0T → 165.9T). Growth
   rates of hypergrowth series decay as the base grows, so the class probably over-states the
   forward multiple.
2. Overlapping windows understate the true dispersion.
3. External sanity check: May 2026 Series B, "25T tokens/week, 5× in six months" [4][5]. That
   matches the series, so the series is the right object.

Holiday effect: in the same chart, the weeks of 2025-12-22 and 2025-12-29 were −3.0% and −1.7%
week-on-week [2]. That is small, because agent workloads do not take holidays.

### Inside view

Main drivers [2][6]:
- **Agentic, always-on workloads.** One personal-agent app (Hermes Agent) used 15.4T tokens last
  week, and Kilo Code and Claude Code are also large. These grow with users, not with developer
  working hours.
- **Cheap open-weight "flash" models.** DeepSeek V4.1 Flash is 15% of tokens; GLM-5.3 Flash and
  MiMo v2.6 Flash are 6% each.
- **A free stealth model, `stealth/space-bunny-alpha`**: released 2026-09-23 [7], it had **38.7T =
  23%** of last week's volume. Stealth models are temporary. When they convert to paid or vanish,
  volume can drop sharply: −22% in the week of 2026-04-06, −14% in the week of 2025-12-01 [2]. So
  last week's 165.9T base is partly transient.
- **Near-term market read:** Polymarket's "week of Oct 5" market centres around **165–175T**, i.e.
  roughly flat on last week [8]. Kalshi's October (4-week) market bids 0.76 that the total exceeds
  600T, i.e. at least ~150T/week on average [9]. Both are thin (a few thousand dollars), but they
  point to a pause, not to continued +13%/week.

Projection: a stealth-adjusted base of ≈ 150T, times a decayed 12-week multiple of ≈ 2.3× (the
historical median 2.43× shaded for decay), times a holiday factor of ≈ 0.95, gives **≈ 330T**.

### Evidence

- Weekly totals from the chart JSON (retrieved 2026-10-05) [2]:
  - 2026-08-03 69.1T, 08-10 75.3T, 08-17 93.4T, 08-24 113.0T, 08-31 115.5T, 09-07 126.8T,
    09-14 128.9T, 09-21 145.9T, 09-28 165.9T.
  - Mean weekly log-growth: 6.9% over the past year (SD 9.9%); 9.7% over the last 13 weeks.
- Plateaus do occur. Jun 15 to Jun 29 was flat at 46.7T, Jul 13 to Jul 27 fell from 62.8T to
  56.8T, and Mar 30 to Apr 13 fell from 27.0T to 20.5T. Each time, growth resumed within 2–5 weeks.
- What would argue for slowing: price changes on free tiers, the end of stealth models,
  large customers moving to direct provider APIs, OpenRouter rate limits or capacity.
  I found none announced (searched 2026-10-05).
- What would argue for speeding up: new frontier releases routed through OpenRouter (GPT-6 Luna,
  Claude Opus 5.5 and Gemini 3.8 Flash are all in the top 20 within two weeks of release [2]) and
  agent frameworks scaling.

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus CP (recency-weighted) | hidden | 2026-10-05 | CP reveal 2026-10-10 17:00 UTC; 5 pre-open forecasters |
| Metaculus Pro | hidden | 2026-10-05 | |
| Metaculus gold medalists | hidden | 2026-10-05 | |
| Polymarket, week of Oct 5 | <155T 9.5% · 155–165 25.5% · 165–175 31.5% · 175–185 21% · 185+ 15.5% | 2026-10-05 | ~$2k volume; implied median ≈ 169T |
| Polymarket, Sep 28–Oct 25 | 725T+ 46% (thin) | 2026-10-05 | $70 volume, ignore |
| Kalshi KXTOKENUSEM Oct (Sep 28–Oct 25) | >600T bid 0.76 / ask 0.98; >575T last 0.98 | 2026-10-05 | resolves on the Data API, not the chart |
| Question design | range 100T–700T, centre 400T | 2026-09-28 | the author's prior is somewhat above mine |

### Scenarios

| # | Scenario | Weight | Implies (Dec 21–27) |
|---|---|---|---|
| 1 | Hypergrowth continues (≥ 7%/week on average) | 0.30 | 400–600T |
| 2 | Moderate growth (3–7%/week) | 0.40 | 250–400T |
| 3 | Plateau (0–3%/week) | 0.20 | 170–250T |
| 4 | Contraction (stealth exit, free-tier cuts, a big customer leaves) | 0.10 | < 170T |

Percentiles: p5 160T, p10 190T, **p25 250T, p50 330T, p75 430T**, p90 530T, p95 600T.
P(> 700T, the open upper bin) ≈ 2%. P(< 100T) < 1%.

![Weekly tokens and forecast](charts/weekly-tokens-and-forecast.png)

### Sensitivity

| Assumption | If instead | Forecast becomes |
|---|---|---|
| Hypergrowth multiple decays (2.3× vs historical 2.43×) | No decay; full reference-class median on the unadjusted base | median ≈ 400T |
| Stealth volume is ~half transient | Space Bunny stays free through December | median ≈ 360T |
| Holiday dip ≈ −5% | Dip ≈ −15% (developer-heavy usage mix) | median ≈ 300T |

### What would change my mind (tripwires)

- [ ] Chart total for the week of Oct 5–11 (readable 2026-10-12) below 155T → down 30T; above 185T → up 30T (signed separately in meta.yaml)
- [ ] `stealth/space-bunny-alpha` leaves free/stealth status before 2026-11-15 and the weekly total falls > 15% week-on-week → down 40T
- [ ] Any weekly chart total ≥ 250T before 2026-11-30 → up 60T
- [ ] OpenRouter changes the chart's binning, the `Others` bucket, or its rounding before 2026-12-21 → re-analyse (either)

### Sources

1. Metaculus question #45689, text via /api-proxy/posts — https://www.metaculus.com/questions/45689/ (accessed 2026-10-05; cached `raw/question-text-2026-10-05.json`)
2. OpenRouter, model rankings chart JSON — https://openrouter.ai/api/frontend/v1/rankings/model-rankings-chart (accessed 2026-10-05; cached `raw/openrouter-model-rankings-chart-2026-10-05.json`). Source: OpenRouter (openrouter.ai/rankings), CC BY 4.0
3. OpenRouter Data API docs (rankings-daily: top 50 plus "other", restatement note) — https://openrouter.ai/docs/cookbook/administration/data-api (accessed 2026-10-05)
4. Business Wire, "OpenRouter Raises $113 Million CapitalG-led Series B as Weekly Volume Explodes to 25T Tokens", 2026-05-26 — https://www.businesswire.com/news/home/20260526953416/en/OpenRouter-Raises-$113-Million-CapitalG-led-Series-B-as-Weekly-Volume-Explodes-to-25T-Tokens (accessed 2026-10-05)
5. Investing.com, "OpenRouter raises $113M as token volume surges to 25T weekly" — https://www.investing.com/news/stock-market-news/openrouter-raises-113m-as-token-volume-surges-to-25t-weekly-93CH-4710030 (accessed 2026-10-05)
6. OpenRouter rankings page (apps and week view embedded in HTML) — https://openrouter.ai/rankings (accessed 2026-10-05)
7. OpenRouter, Space Bunny Alpha model page (released 2026-09-23, free) — https://openrouter.ai/stealth/space-bunny-alpha (accessed 2026-10-05)
8. Polymarket Gamma API, events `openrouter-token-usage-week-of-october-5` and `openrouter-ai-token-usage-sep-28-to-oct-25-2026` (accessed 2026-10-05; cached in `raw/`)
9. Kalshi Trade API, series KXTOKENUSEM and KXTOKENUSE (accessed 2026-10-05; cached in `raw/`)
10. Octagon AI, "OpenRouter AI token usage in September" (Kalshi KXTOKENUSEM context) — https://www.octagonai.co/markets/science-and-technology/tokens/openrouter-ai-token-usage-in-september (accessed 2026-10-05)
11. CryptoBriefing, "OpenRouter reports 9,000x increase in token usage since January 2024" — https://cryptobriefing.com/openrouter-9000x-token-usage-growth/ (accessed 2026-10-05)
12. 36Kr, "AI transit station OpenRouter… 100 trillion tokens monthly" — https://eu.36kr.com/en/p/3827152626225799 (accessed 2026-10-05)

**Date**: 2026-10-05
**Forecast**: Median 330T, IQR [250T, 430T]
**Thesis**: The resolving chart totals top-9 models plus Others (Sep 7 week = 126.76T ≈ the question's 127T), and the last full week was 165.9T. The platform's own 12-week growth multiples over the past year (median 2.43×) imply ≈ 400T. I shade that down for decaying hypergrowth, for a transient free stealth model that is 23% of current volume, for a ~5% holiday dip, and for near-term markets pricing a flat next week (~169T), which gives ≈ 330T with wide tails.
