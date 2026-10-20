# How will Amazon's stock close on October 30, 2026, the first full trading day after its Q3 report?

| | |
|---|---|
| **Source** | metaculus — https://www.metaculus.com/questions/46143/ |
| **Tournament** | minibench — one shot, window 2026-10-19T13:10:03Z -> 2026-10-19T16:10:03Z |
| **Type** | multiple_choice |
| **Opened / Closes / Resolves** | 2026-10-19 / 2026-10-19 / 2026-10-30 |
| **Status** | closed |
| **Current forecast** | Median 25.0%, IQR [20.0%, 30.0%] (v1, 2026-10-19) |
| **Community** | hidden — bot tournament |
| **Next review** | — |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-10-19

### What resolves YES

The question resolves to whichever of five buckets holds AMZN's official Nasdaq regular-session "Close" for Friday 2026-10-30, as shown on Yahoo Finance's AMZN history page (Nasdaq, Google Finance or WSJ if Yahoo has no value). The buckets are <$235, $235–<250, $250–<265, $265–<280 and ≥$280. Each includes its lower bound, so a close of exactly $250.00 resolves "$250.00 to less than $265.00". If Amazon moves its report, October 30 still decides. If there is no regular session that day, the question is annulled. Amazon reports Q3 after the close on Thursday Oct 29, so the Oct 30 close includes the full earnings reaction.

### Outside view

Reference class: AMZN's closing move on the day after earnings, plus normal drift over the 9 sessions before it.
- **Earnings reaction:** options imply about ±7.6% [3], close to the 10-year average of ±7.7%. The last five reactions were +15.3%, +0.8%, −5.6%, +9.6% and −8.3% [3]. The mean absolute move was about 7.9%, with no reliable sign.
- **Pre-earnings drift:** AMZN has recently moved about 1.5–2% a day [1], which gives roughly ±5% (1σ) over 9 sessions.
- **Combined:** about ±11–12% at 1σ around a spot of about $253. That is wide compared with the $15 buckets (about 6% each), so no bucket should get much more than a quarter of the mass.

### Inside view

The anchor is $253, a blend of the Oct 16 close of $250.00 and the Oct 19 pre-market quote of $255.14 (+2.1%) [1].

`model.py` runs a Monte Carlo with 9 sessions of t(5) noise at 1.8% a day, plus a t(4) earnings jump with mean |move| of 7.6%. Its output:

| Bucket | Model |
|---|---|
| <235 | 0.233 |
| 235–250 | 0.219 |
| 250–265 | 0.227 |
| 265–280 | 0.158 |
| ≥280 | 0.163 |

The model's median is $253, its IQR is $236–271, and its 5–95% range is $210–305.

I shifted a little mass toward the central bucket because the model's tails are on the generous side (t(4) jump plus fat-tailed drift). I kept a slight upward skew: the last three Q3/Q2 prints had large positive reactions on AWS acceleration, and the stock sits about 12% below its August high of $284 [2]. Against that, the capex worries (~$220B guidance) that took the stock from $262 to $250 over the last week [2] could cap any rally. The skew is treated as near-zero; no directional edge is claimed.

### Evidence

- AMZN closed at $250.00 on 2026-10-16 (−1.87%), after $262.43 on Oct 9. The Oct 19 pre-market quote was $255.14 at 9:23 ET [1] (accessed 2026-10-19).
- The Oct 13 close was $258.58 on light volume [4].
- Options imply ±7.6% for the Oct 29 report, as of Oct 16. The realized peak move exceeded the implied move in 12 of 17 reports [3].
- Amazon guided Q3 net sales to $197–202bn [5].
- The question text gives a 52-week range of about $196–287 and an all-time closing high of $284.02 on Aug 3, 2026 [2].

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus CP | hidden — bot tournament | 2026-10-19 | — |
| Options market | ±7.6% implied earnings move | 2026-10-16 | EarningsWatcher [3] |
| Kalshi/Polymarket | Daily AMZN close-above markets exist [4]; none found for Oct 30 | 2026-10-19 | not used |

### What would change my mind

- A large pre-earnings move before Oct 29 (e.g. AMZN at $240 or $265 going into the print) would shift the whole distribution by a bucket.
- A broad market selloff or rally over the next 9 sessions.
- The sign of the AWS growth surprise, which decides the direction of the about 8% earnings jump.

### Sources

1. StockAnalysis, AMZN price history — https://stockanalysis.com/stocks/amzn/history/ (accessed 2026-10-19)
2. Metaculus question 46143, background text — https://www.metaculus.com/questions/46143/ (accessed 2026-10-19, cached raw/)
3. EarningsWatcher, AMZN earnings October 2026 — https://earnings-watcher.com/wiki/amzn-earnings-october-2026 (accessed 2026-10-19)
4. Gotrade, Amazon stock news Oct 14 2026 — https://www.heygotrade.com/en/news/amazon-amzn-stock-news-october-14-2026/ (accessed 2026-10-19); PredScope AMZN Oct 16 market — https://predscope.com/event/amzn-close-above-on-october-16-2026 (accessed 2026-10-19)
5. Regards of Wall Street, AMZN earnings-move database — https://www.regardsofwallstreet.com/data/earnings-moves/ticker/amzn (accessed 2026-10-19)
6. Saxo, Amazon into earnings (Q2 2026 options structure) — https://www.home.saxo/en-gb/content/articles/options/amazon-into-earnings-choosing-a-structure-when-the-move-is-already-priced-28072026 (accessed 2026-10-19)

**Question**: [How will Amazon's stock close on October 30, 2026, the first full trading day after its Q3 report?](https://www.metaculus.com/questions/46143/)
**Date**: 2026-10-19
**Forecast**: Median 25.0% ($250.00 to less than $265.00), IQR [20.0%, 30.0%]
**Thesis**: AMZN sits at about $253 (Oct 16 close $250.00, Oct 19 pre-market $255) with 9 sessions plus an earnings print priced at ±7.6% by options. That is roughly ±11% of combined 1σ uncertainty, so mass spreads across all five buckets, peaking slightly in the bucket containing spot. The forecast is most sensitive to the direction of the AWS/capex surprise on Oct 29.
