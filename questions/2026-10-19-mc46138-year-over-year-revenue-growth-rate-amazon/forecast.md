# What year-over-year revenue growth rate will Amazon report for its AWS segment in Q3 2026?

| | |
|---|---|
| **Source** | metaculus — https://www.metaculus.com/questions/46138/ |
| **Tournament** | minibench — one shot, window 2026-10-19T11:44:12Z -> 2026-10-19T14:44:12Z |
| **Type** | numeric |
| **Opened / Closes / Resolves** | 2026-10-19 / 2026-10-19 / 2026-10-30 |
| **Status** | closed |
| **Current forecast** | Median 40, IQR [38, 42.3] (v1, 2026-10-19) |
| **Community** | hidden — bot tournament |
| **Next review** | — |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-10-19

### What resolves YES

A number in percent: (Q3 2026 AWS segment net sales − Q3 2025 AWS segment net sales) / Q3 2025 AWS net sales × 100. Both figures come from Amazon's Q3 2026 earnings release, scheduled for 29 Oct 2026 on ir.aboutamazon.com. The base is about $33.0B. If the release gives only the stated percentage, that percentage is used. If the release slips past 30 Oct 2026, the question is annulled. The range is 25–55 and both bounds are open. As a rule of thumb, each $0.33B of AWS revenue moves the result by about 1 percentage point (pp).

### Outside view

The reference class is the recent AWS growth path and AWS's record against consensus. Year-over-year (YoY) growth by quarter:

| Quarter | AWS sales | YoY growth |
|---|---|---|
| Q3 2025 | $33.0B | 20.2% |
| Q4 2025 | ~$35.6B | ~24% |
| Q1 2026 | $37.6B | 28% |
| Q2 2026 | $42.2B | 36.7% |

Growth rose in each of these quarters. AWS beat the sell-side AWS revenue consensus in each of the last three:

| Quarter | Actual vs consensus | Beat in growth terms |
|---|---|---|
| Q4 2025 | — | ~+1.5–2 pp |
| Q1 2026 | $37.6B vs $36.64B | ≈ +3.2 pp |
| Q2 2026 | $42.2B vs $40.6B | ≈ +5.2 pp |

With a hyperscaler's revenue base this large, growth rarely moves by more than ±4 pp in a single quarter. The Q2 jump of +8.7 pp was itself unusual.

### Inside view

- **Consensus.** The question text cites a consensus of about 38%. HSBC models $45.1B, or 36.7%, and the question's worked example uses the same $45.1B figure. One preview treats $44.56B (35%) as the bar AWS has to clear. The buy side reportedly hopes for 43–45% (BNP Paribas).
- **Sequential math.** Adding $3.0B / $4.6B / $6.0B to Q2's $42.2B gives 36.9% / 41.7% / 46.0%. Q3 also has one more day than Q2.
- **Drivers.** AI demand is far above supply: the AWS backlog is $496B, and AI power capacity is set to double by 2027. Capex is being raised to ~$220B, so the binding question is how much capacity came online in Q3.
- **Against a big jump.** Wells Fargo (12 Oct) expects the acceleration to continue in Q4, which reads as an implicit sign that Q3 may be a more modest step. Q2's +8.7 pp jump may also have contained lumpy items.
- **Combined view.** Consensus is ~37–38%, AWS has beaten it by 2–5 pp in recent quarters, and capacity is the constraint. My median is ~40%, with fat tails on both sides.
- **Distribution.** p5 34.8, p10 36.2, p25 38.0, p50 40.0, p75 42.3, p90 44.6, p95 46.2. No model file: the sequential arithmetic above was enough.

### Evidence

- Q2 2026: AWS $42.2B, +36.7%, fastest growth in 18 quarters. Consensus had been $40.6B. Operating margin 39.4%, backlog $496B. Q3 company sales guided to $197–202B [1][2][3].
- Q1 2026: AWS $37.59B, +28%, against a $36.64B consensus [4][5].
- HSBC (12 Oct 2026): Q3 company revenue $203.3B, above the top of guidance. Reported AWS forecast $45.1B (+36.8%) [6][7].
- Wells Fargo and Cantor (12 Oct 2026): expect AWS acceleration; Wells Fargo places it in Q4 [8].
- Drillr preview (29 Sep 2026): no AWS consensus given; sets a bar of $44.56B (35%) [9].

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus | hidden — bot tournament | 2026-10-19 | |
| Sell-side consensus (per question text) | ~38% | 2026-10 | |
| HSBC | $45.1B ≈ 36.8% | 2026-10-12 | single analyst |
| Buy-side (BNP Paribas, per question text) | 43–45% | 2026-10 | whisper |
| Polymarket / Kalshi | none found | 2026-10-19 | |

### What would change my mind

- **Capacity.** Evidence that large blocks of new capacity (Trainium/GPU data centres) came online in July–August would push the result toward 43%+. Evidence of power or chip delays would point to the mid-30s.
- **Q2 one-offs.** Disclosure that the Q2 jump included one-time items, such as large contract true-ups, would lower the base.

### Sources

1. https://www.shelf-awareness.com/theshelf/2026-07-31/amazon_s_second_quarter:_sales_up_20_aws_up_37_.html (accessed 2026-10-19)
2. https://www.shacknews.com/article/150203 (accessed 2026-10-19)
3. https://seekingalpha.com/news/4622393-amazon-outlines-q3-net-sales-of-197b-202b-while-lifting-2026-cash-capex-to-about-220b (accessed 2026-10-19)
4. https://www.shacknews.com/article/148915/amazon-amzn-aws-revenue-q1-2026 (accessed 2026-10-19)
5. https://www.digitalcommerce360.com/2026/04/30/amazon-aws-revenue-growth-milestone-q1-fy26/ (accessed 2026-10-19)
6. https://www.kucoin.com/news/flash/hsbc-aws-revenue-up-37-qoq-q3-earnings-expected-to-exceed-guidance (accessed 2026-10-19)
7. https://www.techflowpost.com/en-US/article/34564 (accessed 2026-10-19; search snippet only)
8. https://stocktwits.com/news-articles/markets/equity/amazon-analysts-slash-price-targets-ahead-of-q3-wells-fargo-sees-aws-acceleration-to-continue-in-q4/cZxIXT6RB87 (accessed 2026-10-19)
9. https://drillr.ai/article/amzn-amazon-q3-2026-earnings-preview-aws-growth-ai-capex (accessed 2026-10-19)
10. https://www.spglobal.com/market-intelligence/en/news-insights/research/2026/08/amazon-postq-aws-reaccelerates-as-ai-investment-pushes-capex-higher (accessed 2026-10-19; 403, snippet only: Q3 AWS estimates revised up 4.7% after Q2)

**Question**: [What year-over-year revenue growth rate will Amazon report for its AWS segment in Q3 2026?](https://www.metaculus.com/questions/46138/)
**Date**: 2026-10-19
**Forecast**: Median 40.0%, IQR [38.0%, 42.3%]
**Thesis**: AWS growth has accelerated from 20% to 24%, 28% and then 36.7% over four quarters, and it beat AWS consensus by roughly 2–5 pp in each of the last three. With consensus near 37–38% ($45.1B per HSBC), I expect about 40%, with wide tails. The result depends most on how much new AI capacity came online in Q3.
