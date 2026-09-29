# Research log — What will be the highest intraday value of the VIX between October 1 and December 24, 2026?

Working notes. Rough is fine; **completeness beats polish**. The next update reads this to
learn what was already checked and what was already ruled out.

## Question mechanics

- Resolution source: **not yet published.** On 2026-09-28 (~05:00 UTC) the Metaculus API
  returned `resolution_criteria`, `fine_print` and `description` all `null` — both via the
  aggregations script and via a direct `/api/posts/45515/` call with the bot key. The question
  was set to *upcoming* by a moderator (darkives, 2026-09-27 comment); it opens
  2026-09-28 17:00 UTC, CP reveal 2026-09-30 17:00 UTC, closes 2026-12-10, scheduled resolve
  2026-12-25. Numeric, range 6–40, **open upper and lower bounds**. Tournament: Metaculus Cup
  Fall 2026.
- Working assumption: resolves to the maximum daily **HIGH** of the Cboe Volatility Index (VIX)
  over trading sessions 2026-10-01 … 2026-12-24 inclusive, as published by Cboe (or a mirror
  such as Yahoo Finance `^VIX`). **Re-read the criteria once they are published.**
- Edge cases and ambiguities:
  - **Extended-hours values.** Cboe's `VIX_History.csv` contains rows for US equity holidays
    since 2022 (2022-07-04, 2022-09-05, 2022-11-24, … 2026-09-07), i.e. Cboe now disseminates
    VIX during Global Trading Hours (GTH) and its daily HIGH can include overnight prints.
    Yahoo/other vendors may show regular-hours highs only. Effect: usually a few tenths, rarely
    several points (e.g. a 03:00 ET spike on a geopolitical headline). Slight upward skew
    if Cboe is the source.
  - Opening-print artefacts: VIX's first print at 09:30 ET is computed from wide SPX quotes and
    can spike (2024-08-05 intraday high 65.73 vs close 38.57). Intraday HIGH is systematically
    above closes; our reference class uses HIGH, not CLOSE, so this is priced in.
  - Dec 24 is a half-day session; Thanksgiving (Nov 26) closed, Nov 27 half-day.
  - Window ≈ 59 regular trading sessions; three sessions (Sep 28–30) before it opens.

## Reference classes considered

All computed from Cboe `VIX_History.csv` (downloaded 2026-09-28, last row 2026-09-25). Script:
`analysis/base_rates.py`.

| Class | n | Window | Base rate / distribution | Source | Kept? |
|---|---|---|---|---|---|
| Oct 1–Dec 24 max HIGH / last-Sept close, all years | 36 yrs (1990–2025) | Q4 | ratio p10/25/50/75/90 = 1.12/1.17/1.36/1.66/1.99 → ×14.87 = 16.7/17.4/20.3/24.7/29.7 | Cboe | yes (low weight: ratio compresses for high-start years) |
| Q4 max HIGH, calm-start years (late-Sept VIX 11.5–18.5) | 18 yrs (1992–2025) | Q4 | median 21.8; p25 ≈ 17.2; p75 ≈ 28.3; min 12.9 (2006), max 36.1 (2018) | Cboe | yes |
| same, 2012–2025 only | 9 yrs | Q4 | 19.9, 21.3, 31.1, 23.0, 36.1, 21.5, 23.1, 28.3, 29.0 → median 23.1 | Cboe | yes (modern microstructure) |
| Rolling: 59-session forward max HIGH, start close 13.5–16.5, 2004+ | 1,400 overlapping windows | any season | p5/10/25/50/75/90/95 = 16.3/17.2/20.0/23.2/29.0/37.5/53.3; P>25 = 40%, P>30 = 23%, P>40 = 8% | Cboe | yes |
| Rolling, same but 1992+ | 1,866 | any season | median 22.7, IQR [19.3, 28.3], P>30 = 18% | Cboe | yes |
| Rolling, start 13.5–16.5 **and** VIX3M 16.9–18.9 (steep contango like now) | 442 windows, ~20 episodes | any season, 2006+ | p10/25/50/75/90 = 18.9/21.7/24.8/29.6/36.2; P>30 = 24% | Cboe VIX + VIX3M | yes, but ~20 independent episodes |
| Rolling, start 13.5–16.5 and VIX/VIX3M < 0.87 | 500 windows, ~16 episodes | 2006+ | median 26.7, IQR [21.3, 29.6] | Cboe | yes (low weight, few episodes) |

Overlapping rolling windows massively overstate the effective sample: 1,400 windows ≈ 25–30
independent 3-month periods. Treat the rolling distributions as the shape, not as precise.

Path-max vs terminal ratio (2004+, start 13.5–16.5): P(max HIGH over 59 sessions > K) is
5–9× P(close 36 sessions ahead > K) for K = 20–35. Used to translate option-implied
terminal probabilities into path-max probabilities.

## Decomposition

- Max over window = max(level drift, spike). Starting VIX 14.87 (2026-09-25), VIX9D 12.76,
  VIX3M 17.93, VVIX 87.8.
- Market-implied path: VIX futures (via put–call parity on Cboe option mids, 2026-09-25 close):
  Oct-21 17.5, Nov-18 18.4, Dec-16 18.8. Nov future ≈ +3.5 over spot — above the usual
  ~+1.5–2.5 contango at a 2-month tenor for spot 15 → an event premium over the Nov 3 midterms,
  consistent with Kelly-Pástor-Veronesi (2016) evidence that options spanning elections are dearer.
- Risk-neutral terminal tails (call-spread digitals, noisy): Nov-18 P(>20) 19%, P(>25) 8%,
  P(>30) 5%; Dec-16 P(>20) 21%, P(>25) 10.5%, P(>30) 6%. Historical physical P(close>25 at
  ~+36 sessions | start ~15) = 5.2%, P(>30) = 2.8%. Risk-neutral carries a premium (VIX calls are
  structurally rich), so after a ~1.3–1.6× haircut the options market is pricing tails at or
  somewhat above the historical conditional base rate — i.e. roughly the rolling-window
  distribution, slightly fatter on the right.
- Shock catalysts inside the window: Oct earnings season (mid-Oct → NVDA ~late Nov); FOMC
  Oct 27–28 and Dec 8–9 (hiking cycle — first hike in 3+ years on 2026-09-16, dots show one
  more in 2026); Nov 3 midterms; Trump says US strikes on Iran likely resume **after** the
  midterms (WSJ via UPI/The Hill, 2026-09-25/26); CR expires Dec 11 (shutdown risk in the last
  two weeks of the window); 10-year Treasury at 5.23% (highest since 2007) — a bond-led
  equity drawdown is the main non-geopolitical channel.
- Dampeners: equities 0.7% below ATH with 27 record closes YTD; market has been repeatedly
  desensitised to Iran headlines (Sept 7–8 US–Iran strikes and Brent ~$109 moved VIX only to
  ~18.9); post-election vol crush and December seasonality usually calm; low VVIX.

## Search log

| Date | Query / source | Finding | Effect on forecast |
|---|---|---|---|
| 2026-09-28 | Metaculus aggregations script + API (`/api/posts/45515/`) | Criteria null, CP hidden until 09-30; 8 forecasters; range 6–40 open-ended | Must assume Cboe daily HIGH |
| 2026-09-28 | metaculus-scraper (Playwright) | ERR_CERT_AUTHORITY_INVALID — dead end; WebFetch 403 | — |
| 2026-09-28 | Cboe VIX/VIX3M/VIX9D/VVIX history CSVs | VIX 14.87, VIX3M 17.93, VIX9D 12.76, VVIX 87.8 (09-25) | Anchors base rates |
| 2026-09-28 | Cboe delayed VIX option chain (`_VIX.json`, ts 2026-09-26 03:44) | Forwards 17.5/18.4/18.8 for Oct/Nov/Dec | Slight ↑ vs plain base rate |
| 2026-09-28 | thetrading.tools term structure | 09-22: VIX 14.21, VIX3M 17.61, day 116 of contango regime | confirms steep contango |
| 2026-09-28 | Biggo (Aug 25) | VIX futures Sep 17.4 / Oct 19.0 / Nov 19.7 with spot 15.8; SpotGamma: "insurance is very cheap" | election premium existed in Aug too |
| 2026-09-28 | IndexBox (Sept 9) | Tallbacken's Purves: futures "not pricing in any additional risk tied to the midterms"; S&P fell ≥5% in Sep–Oct in 15 of 24 midterm years since 1930 | mixed; mild ↑ |
| 2026-09-28 | CNBC/Bloomberg Sept 15/17/26 (search snippets; pages 403) | 10Y 5.23% on Sep 25, highest since 2007 | ↑ tail risk |
| 2026-09-28 | CNBC/Schwab/TheStreet Fed | Sept 16 hike to 3.75–4.00% (12-0), Chair Warsh; dots imply one more 2026 hike | ↑ |
| 2026-09-28 | CNBC 2026-09-24 markets, Pluang | S&P 7,743 (0.7% below ATH), +13% YTD | ↓ (calm regime) |
| 2026-09-28 | UPI / The Hill / Iran International | Trump rejected Iran 7-day proposal; expects bombing to resume after midterms; talks via mediators continue | ↑ (post-Nov-3 geopolitical catalyst inside window) |
| 2026-09-28 | CNBC oil 2026-09-28, Al Jazeera 2026-09-07 | Brent ~$106, WTI ~$94; oil +8% in Sept | ↑ inflation/rates channel |
| 2026-09-28 | CNBC 2026-04-01, Resonanz Capital | March 2026 Iran-war vol: VIX intraday 35.3 on 2026-03-09 | shows reachable spike size this year |
| 2026-09-28 | Breaking Defense / NBC | CR signed Sep 2, funds government to Dec 11 | shutdown risk moved to Dec 11–24 |
| 2026-09-28 | Fortune 2026-09-23; UBS via Biggo | Midterm-year Oct historically strong for stocks; vol normalises after elections | ↓ after Nov 3 |
| 2026-09-28 | Bloomberg 2025-10-10; StockCharts 2025 review | Oct 2025 spike (tariff threat + regional-bank credit scare) to 28.99 from ~16 | shows base of idiosyncratic Q4 spikes |
| 2026-09-28 | Kalshi API series list (14,399 series) | No VIX series | no market anchor |
| 2026-09-28 | Polymarket gamma search, Manifold search | No matching VIX Q4 market (only long-dated Manifold VIX questions) | none |
| 2026-09-28 | Sentinel Global Risks Weekly #29–#31 | Ongoing US–Iran war; munitions stockpiles depleted | context |
| 2026-09-28 | Kelly, Pástor & Veronesi (2016, J. Finance 71(5)) | Options spanning national elections are more expensive | explains Nov-future premium; premium ≠ realised spike |

## Dead ends and ruled-out hypotheses

- FRED CSV download (DGS10, SP500, Brent, HY OAS) failed: HTTP/2 stream error, then HTTP/1.1
  timeout. 10Y level taken from news snippets instead.
- Metaculus scraper: TLS error through proxy. Metaculus page via WebFetch: 403.
- Kalshi/Polymarket VIX markets: none exist for this window.
- "Midterm year = bigger Q4 VIX peak": calm-start midterm Q4s were 1994 19.6, 2006 12.9,
  2014 31.1, 2018 36.1 — n=4, no usable signal beyond the known pre-election premium.

## Open questions to chase next time

- Published resolution criteria and fine print (source, GTH inclusion, rounding).
- Metaculus CP/Pro/gold after reveal 2026-09-30 17:00 UTC.
- 10Y yield path after Sept PCE / Oct 2 payrolls; VIX futures Nov–Dec premium.
- Whether US strikes on Iran resume earlier than "after midterms".
