# Research log — What will be the all-time highest close price of NVDA before January 1, 2027?

Working notes. Rough is fine; **completeness beats polish**. The next update reads this to
learn what was already checked and what was already ruled out.

## Question mechanics

- Resolves to the highest NVDA daily **close** ever recorded through the last session of 2026
  (2026-12-31). Split-adjusted prices; see `forecast.md` digest for the Metaculus wording.
- Current all-time-high close: **$239.24 on 2026-10-06** (Yahoo chart API, cached
  `raw/yahoo-nvda-2026-10-17.json`; StockAnalysis agrees; one aggregator says $239.11 — rounding/feed noise).
  Intraday high $243.37 (2026-10-06) is irrelevant (close, not intraday).
- Last close: **$214.13 on 2026-10-16** (−10.5% from ATH). Needs +11.7% to set a new record.
- Remaining sessions: 52 (2026-10-19 → 2026-12-31, excl. Thanksgiving 11-26 and Christmas 12-25).
- The resolved value is floored at 239.24 → large point mass exactly there (the "no new ATH" branch).
- Edge cases: stock split before year-end (would rescale; Metaculus would presumably use split-adjusted);
  data-vendor rounding (±$0.13 between sources).

## Reference classes considered

| Class | n | Window | Base rate | Source | Kept? |
|---|---|---|---|---|---|
| Driftless/low-drift GBM-t4, vol 35–50%, earnings jump σ=6% | MC 200k paths | 52 sessions | P(new ATH) 0.42–0.57; median 239.2–245; p75 253–274; p90 276–309 | own simulation (`scratchpad nvda_sim.py`, reproduced in forecast.md) | yes (primary) |
| Bootstrap of NVDA's last 500 daily log-returns | MC 200k | 52 sessions | P(new ATH) 0.51 (demeaned) – 0.55 (half drift) | same | yes |
| NVDA Q4 seasonality (late Sep → late Dec) | 27 years | 1999–2025 | up 20/27, median +14% | Motley Fool 2026-10-14 | weak (survivor drift baked in) |

Realized vol: 20d 24.8%, 60d 36.8%, 250d 37.3%, 2y 43.8% (annualised, from Yahoo data).
Options: earnings implied move ≈5.5% (Aug 2026, SpotGamma); realized avg post-earnings move 7.4% (12 q).

## Decomposition

P(new ATH) ≈ P(running max of 52 closes > 1.117 × S0). Under σ≈40% annual, 52-day σ ≈ 18%; reflection
principle for driftless BM: P ≈ 2·(1 − Φ(ln 1.117 / 0.18)) ≈ 2·(1 − Φ(0.61)) ≈ 0.54 (continuous
monitoring overstates; discrete closes + Itô drift → ~0.48–0.50).

## Search log

| Date | Query / source | Finding | Effect on forecast |
|---|---|---|---|
| 2026-10-17 | Yahoo Finance chart API (2y daily) | ATH close 239.24 (10-06); last 214.13 (10-16) | anchor |
| 2026-10-17 | Bloomberg 2026-10-02 "Nvidia hits first record since May" | record run into early Oct, mkt cap ~$6T | context |
| 2026-10-17 | CNBC 2026-10-15 "Nvidia, AMD, Dell sink in global tech rout on AI funding worries" | >$1T lost by top-20 AI/semi names this week; rates, neocloud financing, competition | slight −drift / higher vol |
| 2026-10-17 | Benzinga: rising Treasury yields trigger NVDA/AMD slump | rates channel | — |
| 2026-10-17 | FX Leaders 2026-10-15: ASML capacity warning | supply-side concern | — |
| 2026-10-17 | MarketBeat 10-15/10-16 | consensus target ~$322, $150B buyback authorised | slight + |
| 2026-10-17 | Webull/XTB on Q2 FY27 (2026-08-26) | rev $96.2B, Q3 guide $108B ±2% (zero China DC), FY28 ~70% growth | fundamentals strong |
| 2026-10-17 | Wall Street Horizon / days.to | Q3 FY27 earnings expected Wed 2026-11-18 AMC (inferred) | jump date in sim |
| 2026-10-17 | SpotGamma / Capital.com | implied earnings move 5.5–6.9% | jump σ 6% |
| 2026-10-17 | Motley Fool 2026-10-14 | Q4 seasonality 20/27 up; 52w range 164.27–243.37; ~15x FY28 EPS | mild + |
| 2026-10-17 | Polymarket nvda-above-in-october-2026 | ≥$240 by end-Oct 8.5% (tiny volume) | consistent w/ sim (sim ~10% by Oct 30) |

## Dead ends and ruled-out hypotheses

- No liquid market on "NVDA ATH by year-end" (Kalshi/Polymarket searched).
- Live option chain IV not retrievable without a broker feed.

## Open questions to chase next time

- Confirmed earnings date and the Q4 guide; hyperscaler capex commentary in late-Oct earnings
  (MSFT/GOOGL/META/AMZN ~Oct 27–30).
- FOMC 2026-10-28 and 10y yield path.

## Resolution-text retrieval attempts (2026-10-17, second pass)

- Real criteria still unreadable: bot-key API returns `null` description/criteria/fine print on every endpoint (`/api/posts/<id>/`, `/api/questions/<qid>/`, `/api/posts/?ids=`, `?lang=` variants) while the post is pre-open; browser path fails because the proxy denies `brunhild.challenges.cloudflare.com` (Cloudflare challenge); no Wayback/archive.ph copies; unauthenticated API 403.
- The key-authenticated API **does** return text for open posts (verified on 45515, 45262, 45617, 45670), so the real text becomes readable without Cloudflare once the post opens (open_time below).
- open_time 2026-10-19T17:00Z. Author darkives. Closest open price-extreme template is 45515 (VIX, author Capital): resolves on Yahoo Finance history, CBOE as fallback, no revisions after the window. **Template evidence only** — by analogy NVDA likely resolves on Yahoo Finance daily Close (split-adjusted); Yahoo's max close in the cached data is 239.24 (2026-10-06).
