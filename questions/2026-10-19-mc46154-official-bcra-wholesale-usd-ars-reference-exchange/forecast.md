# What will the official BCRA wholesale USD/ARS reference exchange rate (dólar mayorista, Comunicación A 3500) be on October 29, 2026?

| | |
|---|---|
| **Source** | metaculus — https://www.metaculus.com/questions/46154/ |
| **Tournament** | minibench — one shot, window 2026-10-19T19:32:21Z -> 2026-10-19T22:32:21Z |
| **Type** | numeric |
| **Opened / Closes / Resolves** | 2026-10-19 / 2026-10-19 / 2026-10-30 |
| **Status** | open |
| **Current forecast** | Median 1521, IQR [1512, 1531] (v1, 2026-10-19) |
| **Community** | hidden — bot tournament |
| **Next review** | — |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-10-19

### What resolves YES

The question resolves to the BCRA "Tipo de Cambio Mayorista ($ por USD) Comunicación A 3500 – Referencia" published for **Thursday 29 October 2026**, in pesos per US dollar, rounded to two decimals, as shown on the BCRA Principales Variables dashboard (fallbacks: the com3500.xls series or credible press). Oct 29 is an ordinary business day in Argentina; the only October holiday was Oct 12. If no value is published that day, the latest prior business-day value counts. The A 3500 rate is a weighted average of the day's spot trades, so it can differ by a few pesos from the closing prices that Rava and the press quote (e.g. Oct 13: A 3500 ≈ 1,515.85 vs Rava close 1,512.50). The question's range is 1,400–1,750 with both bounds open.

### Outside view

Reference class: 8–9 business-day changes of the mayorista under the current band regime, which has the BCRA buying reserves inside a wide band. Over 28 Sep–16 Oct 2026 every daily close fell between 1,512.50 and 1,524.50. September's range was 1,506.50–1,525.50 (about 1.3%), with daily moves of 0 to ±0.5% and a +0.3% change for the month [1][2]. A random walk with about 0.3% daily volatility gives a standard deviation of roughly 0.85% (≈13 ARS) over 8 days. Earlier in the regime the moves were much larger (a six-month low near 1,355 in mid-April; an October 2025 election-driven swing), so the tails should be fatter than normal.

### Inside view

- **Starting level**: Rava close 1,518.00 on Fri 16 Oct, the first weekly gain in October [1][3]. The question text gives the A 3500 reference as 1,513.93 on Oct 15. I put the current A 3500 at roughly 1,516–1,519.
- **Drift**: small and upward. The REM (BCRA's survey of market expectations) September survey has an October **average** median of 1,545 and November 1,580 [5]. Spot has run about 25 pesos below the REM path for weeks, and the REM revised October down by 20, so it overstates near-term drift. Press projections put end-October near 1,525 [4]. Year-end consensus of about 1,600–1,650 implies roughly 1.5% a month, or about +5 to +8 pesos over 8 business days.
- **Support and pressure**: the BCRA is on a 13-session buying streak with reserves above US$50bn [4]. That buying puts a soft floor under the rate and reduces downside. The band ceiling (≈1,936, rising to ≈1,951 at end-October) is about 27% away and does not matter on this horizon. No news in the last 7 days points to an October run [3][6].
- **Number**: median 1,521, IQR 1,512–1,531. The tails are skewed up (p95 1,560) because peso stress moves faster than appreciation. The p5 of 1,490 allows for a carry-driven appreciation like April's.

### Evidence

- Rava daily closes: 16 Oct 1,518.00; 15 Oct 1,513.00; 14 Oct 1,513.00; 13 Oct 1,512.50; 9 Oct 1,517.00; 1 Oct 1,524.50; 30 Sep 1,517.00 (accessed 2026-10-19) [1][2].
- 16 Oct: BCRA purchases extended a 13-session streak, gross reserves above US$50bn, ceiling 1,936.17. Other quotes: BNA retail 1,535, blue 1,545, MEP 1,543, CCL 1,620 [3][4].
- REM September 2026 (published 6 Oct): October 1,545, November 1,580, December 1,614; Top-10 October 1,543 [5].
- Year-end 2026 forecasts range 1,600–1,670 (BofA 1,600, BBVA 1,630, Morgan Stanley 1,671). The risks they name are medium-term: the 2027 election and real appreciation [6].
- Futures implied about 1,528 for end-September in early September; the actual end-September rate was 1,517, so forward pricing overshot spot [2].

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus | hidden — bot tournament | 2026-10-19 | — |
| BCRA REM (Sep survey) median, October average | 1,545 | 2026-10-06 | has run ~25 above spot; revised down 20 |
| Press projection, end-October | ~1,525 | 2026-10-16 | secondary [4] |
| A3 futures, end-October | not found | 2026-10-19 | December contract ~1,600 cited |
| Polymarket / Kalshi / Manifold | no October market | 2026-10-19 | only illiquid Dec-2026 brackets |

### What would change my mind

- A break out of the 1,505–1,530 corridor in the next few sessions, for example the BCRA stopping its purchases or a global risk-off shock. Either would move the median toward the new level.
- Policy news on the band or the purchase programme. The government is reported to be debating FX policy; a widening or a faster band crawl would shift the upper tail.

### Sources

1. Rava Bursátil, Dólar Mayorista historical closes, https://www.rava.com/cotizaciones/historico/dolar-mayorista (accessed 2026-10-19)
2. Rava Bursátil, September 2026 monthly page, https://www.rava.com/cotizaciones/historico/dolar-mayorista/2026/09/ (accessed 2026-10-19)
3. Economis, 16 Oct 2026 market close, https://economis.com.ar/?p=498446 (accessed 2026-10-19)
4. Noticias NQN, "El dólar oficial repuntó y el Banco Central aceleró las compras…", 16 Oct 2026, https://www.noticiasnqn.com.ar/noticias/2026/10/16/356909-el-dolar-oficial-repunto-y-el-banco-central-acelero-las-compras-de-divisas-que-paso-con-las-reservas (accessed 2026-10-19)
5. El Cronista, REM: a cuánto estará el dólar a fin de año, https://www.cronista.com/finanzas-mercados/rem-a-cuanto-estara-el-dolar-a-fin-de-ano-segun-el-pronostico-de-mas-de-40-consultoras-y-bancos/ (accessed 2026-10-19)
6. DolarHoy, "La City apuesta a un cierre de año en torno a los $1.600…", 16 Oct 2026, https://dolarhoy.com/dolar/dolar-la-city-apuesta-a-un-cierre-de-ano-en-torno-a-los-1-600-pero-mira-con-cautela-2027-2026101613240 (accessed 2026-10-19)
7. iProUP, band ceiling for October/November, https://www.iproup.com/economia-digital/72312-a-cuanto-puede-llegar-el-dolar-en-noviembre-sin-que-intervenga-el-bcra (search snippet, accessed 2026-10-19)

**Question**: [What will the official BCRA wholesale USD/ARS reference exchange rate (dólar mayorista, Comunicación A 3500) be on October 29, 2026?](https://www.metaculus.com/questions/46154/)
**Date**: 2026-10-19
**Forecast**: Median 1521 ARS/USD, IQR [1512 ARS/USD, 1531 ARS/USD]
**Thesis**: The mayorista has stayed within 1,506–1,525 since September while the BCRA keeps buying, and it closed at 1,518 on 16 Oct (Rava, press). The forecast assumes a small upward drift (REM and year-end consensus near 1,600) and wider tails to the upside. It is most sensitive to whether the 1,505–1,530 corridor holds through 29 Oct.
