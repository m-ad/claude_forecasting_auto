# What will the ONS's first estimate of UK GDP growth be for Q3 2026 (quarter-on-quarter)?

| | |
|---|---|
| **Source** | metaculus — https://www.metaculus.com/questions/46374/ |
| **Tournament** | minibench — one shot, window 2026-11-02T02:41:20Z -> 2026-11-02T05:41:20Z |
| **Type** | discrete |
| **Opened / Closes / Resolves** | 2026-11-02 / 2026-11-02 / 2026-11-12 |
| **Status** | closed |
| **Current forecast** | Median 0.67, IQR [0.58, 0.76] (v1, 2026-11-02) |
| **Community** | hidden — bot tournament |
| **Next review** | — |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-11-02

### What resolves YES

The question resolves to the quarter-on-quarter growth in real GDP for July–September 2026, as stated in the main points of the ONS bulletin "GDP first quarterly estimate, UK: July to September 2026" (07:00 GMT, 12 November 2026). ONS rounds this to one decimal, so the outcome is one of the discrete values …, 0.5, 0.6, 0.7, 0.8, …. Values below 0.0 and above 1.2 fall in the open tails. Later revisions don't count.

**Arithmetic.** The last published month is August 2026 (released 15 Oct). The target quarter is Jul–Sep, and only September is still unpublished. I took the monthly path from the QNA of 30 Sep: Apr −0.1%, May 0.0%, Jun +0.3%, then the 15 Oct release (Jun revised to +0.4%, Jul +0.4%, Aug +0.1%). Indexing March = 100 gives Apr 99.9, May 99.9, Jun 100.3, Jul 100.7 and Aug 100.8, so the Q2 average is 100.03. As a cross-check, the three months to August against the three months to May gives +0.67%, which ONS reports rounded as 0.7% ✓.

The September outcome then maps to Q3 growth like this:

| Sep m/m | Q3 q/q | Rounds to |
|---|---|---|
| −0.4% | 0.60% | 0.6 |
| −0.2% | 0.67% | 0.7 |
| flat | 0.73% | 0.7 |
| +0.2% | 0.80% | 0.8 |

The 0.6/0.7 boundary falls at about Sep −0.25%, and 0.7/0.8 at about Sep +0.05%. Monthly rounding (±0.05 on each month) and revisions to Jul/Aug add about ±0.1 pp on top.

### Outside view

The reference class is the UK first quarterly estimate when two of the quarter's three months are already published. The carry-over from months 1–2 usually lands within ±0.1–0.2 pp of the outturn. The main sources of miss are the month-3 print (UK monthly GDP m/m has a standard deviation of about 0.3 pp, so it moves the quarter by about ±0.1 pp) and revisions to months 1–2, typically ±0.1 each. Recent precedent leans downward: in Q3 2024 and Q3 2025 a weak September pulled the first estimate below expectations [5]. With September flat, the prior centre is 0.73%.

### Inside view

The September evidence leans soft:
- Retail volumes fell 0.4% m/m [2].
- ONS says real-time indicators "pointed to weaker activity in September" [1].
- August's +0.8% production jump (manufacturing +1.2%) is a candidate for partial reversal.
- The PMIs are still expansionary: composite 52.0, services 52.1, manufacturing 51.9, and construction improving to 46.1 [3][4]. That argues against a slump.

I assume September m/m of about −0.2%, which moves the centre to about 0.67%. Deutsche Bank's ~0.5% call (8 Oct, secondhand [6]) came before August beat its flat expectation by 0.1. That beat adds about 0.07 pp, putting the call at roughly 0.55–0.6, below my centre. I give it some weight.

Revisions recently ran upward (June, Q2, the three-month rates), and that partly offsets. The result is a centre of 0.67 with a standard deviation of about 0.14 pp and slightly fat tails. Bin probabilities:

| Outcome | Probability |
|---|---|
| ≤0.4 | ~7% |
| 0.5 | ~13% |
| 0.6 | ~25% |
| 0.7 | ~27% |
| 0.8 | ~18% |
| 0.9 | ~7% |
| ≥1.0 | ~3% |

### Evidence

- ONS, GDP monthly estimate for August 2026 (15 Oct 2026) [1]:
  - Aug +0.1% m/m (Reuters poll had −0.1%); Jul +0.4% unrevised; Jun revised up to +0.4%.
  - The three months to August were up 0.7% on the three months to May; the three months to Jun and Jul were both revised to 0.5%.
  - In August, services were flat, production +0.8% and construction −0.2%.
  - Real-time indicators were weaker in September.
- ONS QNA, Q2 2026 (30 Sep 2026): Q2 revised to +0.5% from +0.4%; monthly path Apr −0.1, May 0.0, Jun +0.3 [7].
- ONS retail sales, September 2026 (23 Oct): volumes −0.4% m/m, August revised to +0.7%, Q3 +0.7% q/q [2].
- S&P Global September PMIs: composite 52.0 (Aug 52.5), services 52.1, manufacturing 51.9 [3]; construction 46.1 (Aug 44.3) [4].
- SMMT September car output 70,831, up 38.6% y/y. The jump is mostly a base effect from the 2025 JLR cyberattack [8].

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus CP | hidden — bot tournament | 2026-11-02 | |
| Deutsche Bank | Q3 ~0.5% q/q | 2026-10-08 | Secondhand; came before the August beat [6] |
| Polymarket Q3 2026 band markets | "negative" 19–25¢, "≥1.0%" ~7¢ | undated | Thin (<$1k), stale mirrors; inconsistent with the carry-over; heavily discounted |
| Kalshi | none found | 2026-11-02 | |
| Reuters/Bloomberg Q3 consensus | not yet published | 2026-11-02 | |

### What would change my mind

- **The monthly path for April/May 2026.** If the Q2 base is lower than I reconstructed, the carry-over rises by about 0.05–0.1 pp.
- **Revisions to July (+0.4%) and August.** A 0.1 pp downward revision to July shifts the quarter by about 0.07 pp.
- **September's print.** A drop worse than −0.4% (for example, a sharp production reversal) would make 0.5–0.6 the modal outcome.

### Sources

1. ONS, GDP monthly estimate, UK: August 2026 — https://www.ons.gov.uk/economy/grossdomesticproductgdp/bulletins/gdpmonthlyestimateuk/august2026 (accessed 2026-11-02)
2. ONS, Retail sales, Great Britain: September 2026 — https://www.ons.gov.uk/businessindustryandtrade/retailindustry/bulletins/retailsales/september2026 (accessed 2026-11-02)
3. Trading Economics, UK composite PMI — https://tradingeconomics.com/united-kingdom/composite-pmi/news/589506 (accessed 2026-11-02; snippet)
4. Trading Economics, UK construction PMI — https://tradingeconomics.com/united-kingdom/construction-pmi/news/589833 (accessed 2026-11-02; snippet)
5. Investment Week, "UK economy grows only 0.1% in third quarter after September slowdown" — https://www.investmentweek.co.uk/news/4380188/uk-economy-grows-quarter-september-slowdown (accessed 2026-11-02; snippet)
6. TMGM, Deutsche Bank note "UK GDP momentum seen slowing" — https://www.tmgm.com/es/analysis/market-news/article/united-kingdom-gdp-momentum-seen-slowing-deutsche-bank-202610081200 (accessed 2026-11-02; search summary only)
7. ONS QNA April–June 2026, reproduced at https://static.poder360.com.br/uploads/2026/09/PIB-ReinoUnido-abril-junho-2026.pdf (accessed 2026-11-02; snippet)
8. Trading Economics, UK car production — https://tradingeconomics.com/united-kingdom/car-production/news/596001 (accessed 2026-11-02; snippet)
9. Polymarket mirror — https://orrery.me/markets/will-uk-gdp-growth-in-q3-2026-be-negative-20260813112748101 (accessed 2026-11-02; snippet)

**Question**: [What will the ONS's first estimate of UK GDP growth be for Q3 2026 (quarter-on-quarter)?](https://www.metaculus.com/questions/46374/)
**Date**: 2026-11-02
**Forecast**: Median 0.67%, IQR [0.58%, 0.76%]
**Thesis**: July (+0.4%) and August (+0.1%) are already published, and the monthly path gives a Q3 carry-over of about 0.73% q/q if September is flat [1][7]. Soft September indicators (retail −0.4%, weaker ONS real-time data) pull the centre to about 0.67%, so 0.6 and 0.7 are near coin-flips [1][2]. The forecast is most sensitive to September's print and to revisions to July/August.
