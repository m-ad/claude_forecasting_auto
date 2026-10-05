# Research log — What will be the total OpenRouter token usage December 21-27, 2026?

Working notes. Rough is fine; **completeness beats polish**. The next update reads this to
learn what was already checked and what was already ruled out.

## Question mechanics

- Resolution source: the openrouter.ai/rankings "Top Models: Weekly usage" chart, Dec 21 bar,
  value as displayed (rounded). Mon–Sun bins.
- **Data endpoint (no key needed):** `GET https://openrouter.ai/api/frontend/v1/rankings/model-rankings-chart`.
  It returns `{"data": {"data": [{"x": "YYYY-MM-DD", "ys": {model: tokens, ..., "Others": tokens}}], "cachedAt": ...}}`:
  weekly rows with the top 9 models plus `Others`. The last row is the current partial week.
  **The bar total = sum of ys**. Verified: week 2026-09-07 = 126.76T, which matches the question's
  "127T" example.
- Official Data API (`/api/v1/datasets/rankings-daily`) needs an OpenRouter key; none is in the env.
  Kalshi resolves on that API (top 50 + other), so it may differ slightly from the chart.
- Edge cases: display rounding; snapshot restatements; bin changes (fallback: last full week in 2026).

## Reference classes considered

| Class | n | Window | Base rate | Source | Kept? |
|---|---|---|---|---|---|
| 12-week growth multiple of the weekly total | 40 (overlapping) | Oct 2025–Sep 2026 | p10 1.55, p25 2.04, p50 2.43, p75 2.75, p90 3.13, min 1.11 | chart JSON | yes, shaded down for decay |
| Holiday weeks (Dec 22 / Dec 29 2025) | 2 | 2025 | −3.0% / −1.7% w/w | chart JSON | yes |
| Stealth-model exits | 2–3 | 2025–26 | −14% (2025-12-01), −22% (2026-04-06) w/w | chart JSON | yes |

## Decomposition

- Stealth-adjusted base ≈ 150T (last week 165.9T, of which space-bunny-alpha was 38.7T; assume
  about half of it is transient).
- × decayed 12-week multiple ≈ 2.3 × holiday 0.95 ≈ **330T**.
- Percentiles: p5 160, p10 190, p25 250, p50 330, p75 430, p90 530, p95 600 (T).

## Search log

| Date | Query / source | Finding | Effect on forecast |
|---|---|---|---|
| 2026-10-05 | openrouter.ai/rankings HTML | app ranks (Hermes Agent 15.4T/wk); week view of the top 20 models | drivers |
| 2026-10-05 | model-rankings-chart JSON | full weekly series Oct 2025–Sep 2026; last full week 165.9T | anchor |
| 2026-10-05 | OpenRouter Data API docs | rankings-daily needs a key; CC BY 4.0; restatement note | — |
| 2026-10-05 | space-bunny-alpha page | free stealth model released 2026-09-23 | transient-volume risk |
| 2026-10-05 | Business Wire / Investing (May 2026 Series B) | 25T/week, 5× in six months | consistent with series |
| 2026-10-05 | Polymarket week-of-Oct-5 market | implied median ≈ 169T (flat) | ↓ near-term |
| 2026-10-05 | Kalshi KXTOKENUSE / KXTOKENUSEM | thin; Oct >600T bid 0.76 | weak |
| 2026-10-05 | Octagon AI | Kalshi September market context (>525T resolved YES) | — |

## Dead ends and ruled-out hypotheses

- The "top ten models alone totaled 127T" background phrasing: ruled out as the resolution
  definition. The chart total includes Others.

## Open questions to chase next time

- Week of Oct 5 total (available Oct 12) vs the Polymarket ~169T.
- Status of space-bunny-alpha (paid/unmasked?) and new stealth models.
- Metaculus CP after reveal (Oct 10).
