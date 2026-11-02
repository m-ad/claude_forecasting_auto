# What will Argentina's month-on-month inflation (INDEC national CPI) be for October 2026?

| | |
|---|---|
| **Source** | metaculus — https://www.metaculus.com/questions/46408/ |
| **Tournament** | minibench — one shot, window 2026-11-02T16:23:47Z -> 2026-11-02T19:23:47Z |
| **Type** | discrete |
| **Opened / Closes / Resolves** | 2026-11-02 / 2026-11-02 / 2026-11-12 |
| **Status** | closed |
| **Current forecast** | Median 1.9, IQR [1.8, 2.05] (v1, 2026-11-02) |
| **Community** | hidden — bot tournament |
| **Next review** | — |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-11-02

### What resolves YES

The question resolves to the number INDEC reports as the national "Nivel general" month-on-month change for October 2026, in its IPC press release scheduled for Thursday 12 November 2026, 16:00 ART (one decimal, e.g. 1,9% → 1.9). The core index, regions, y/y and YTD figures do not count; the first published October figure is used. Arithmetic: last published period is September 2026 (released 13 Oct 2026: 1.9% m/m, 33.4% y/y, 23.6% YTD); the target is the very next month, one period ahead, so there is no multi-period projection. The 2026 path is 2.9, 2.9, 3.4, 2.6, 2.1, 1.9, 2.1, 1.7, 1.9. The range is open at both ends (below 0.95 / above 3.05); no fallback formula applies. INDEC prints on a 0.1 grid, so the outcome is one of ~1.5, 1.6, … 2.4 in practice.

### Outside view

Reference class: the next monthly INDEC print given the previous prints during a stabilised disinflation (last 4 months: 1.9, 2.1, 1.7, 1.9, mean 1.9, range 0.4). Month-to-month change in the last 6 months has an absolute size of about 0.2 pp (0.2, 0.2, 0.4, 0.2). A random-walk-with-mean-reversion view centred on 1.9 with sd ≈ 0.2–0.25 is the prior. The REM (analyst panel) has been accurate to ±0.1–0.2 pp in recent months (Sept REM 1.9 → actual 1.9; Aug REM ~1.7–1.8 → 1.7), but missed by 0.2–0.4 in Q1 2026 (oil shock, March 3.4%; one-source evidence only).

### Inside view

Evidence points slightly above the stale REM (1.7%, surveyed 28–30 Sep) and close to the last print. Seven private trackers published 1–2 Nov 2026 give 1.8, 1.8, 1.9, 2.0, 2.0, 2.0, 2.1 (mean 1.94); Orlando Ferreres is reported at ~1.6 (one summary only). Upside drivers: the BCRA says late-September fuel rises (1–5%) "impactarán plenamente" in October; food trackers are hot (Analytica 4-week food avg 2.5%, vegetables +8.8%; LCG 4-week avg 2.7–3.8%, eight straight weekly rises); CABA bus/subway +3.7%, prepagas ~2%, water ~2.2%. Downside: clothing −1.75% in Eco Go's tracker, core easing (1.7% in Sept), weekly food slowing late in the month (LCG +0.2%, Analytica +0.4% in week 4), and FX essentially flat (wholesale ~1,517 → 1,542, +1.7%, far below the band ceiling ~1,951) so no pass-through shock. Weekly food trackers overstated in September (food spiked 3% in a week after August, yet INDEC food printed 2.0%), so I do not extrapolate them fully. Count each event once: the only adjustment from the REM anchor is the late-October private-estimate revision (+0.2 pp). Distribution on the 0.1 grid (my judgement): ≤1.5: 5%, 1.6: 6%, 1.7: 10%, 1.8: 17%, 1.9: 20%, 2.0: 18%, 2.1: 11%, 2.2: 6%, 2.3: 3%, ≥2.4: 4%. Slight right skew because of food/fuel and the Q1 record of larger-than-expected misses; left tail kept because Aug 1.7 showed 0.4 pp drops are common and the Treasury targets lower.

### Evidence

- INDEC Sept 2026: 1.9% m/m, 33.4% y/y, 23.6% YTD; core 1.7%; food 2.0%; housing/utilities 3.1%, education 3.0%, clothing 1.4%, transport 1.5% (iProUP, Canal26, El Economista; accessed 2026-11-02) [1][2].
- Private estimates for October 2026, published 1–2 Nov: FLyP 1.8, Equilibra 1.8, EconViews 1.9, Analytica 2.0, Invecq ~2.0, C&T ~2.0, Eco Go 2.1 (Infobae 2026-11-02; Bloomberg Línea 2026-11-01 had Eco Go 1.8 earlier) [3][4].
- BCRA REM (Sept survey, published 6 Oct, 44 participants): October 1.7%, Nov 1.6%, Dec 1.8%; Top-10 average for October 1.8% [4][5].
- Food/weekly trackers (El Economista 28 Oct; Infobae 2 Nov) [3][6]. FX: official dollar flat ~1,535–1,550 through October; band ceiling ~1,951 [7].
- CABA IPCBA Sept 1.8%; October IPCBA is published ~8–10 Nov, not yet available [8].
- No Polymarket/Kalshi October 2026 market found; Sept markets (9 Oct) favoured 1.9–2.1 at 60.5% and resolved inside that bracket [9].

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus CP | hidden — bot tournament | 2026-11-02 | |
| BCRA REM (Sept survey) | median 1.7%; Top-10 1.8% | 2026-10-06 | stale, pre-October data |
| Private consultoras (7) | 1.8–2.1%, mean 1.94% | 2026-11-02 | Infobae, Bloomberg Línea |
| Polymarket / Kalshi | no October 2026 market found | 2026-11-02 | Sept: 1.9–2.1 at 60.5% |
| Manifold | not found | 2026-11-02 | |

### What would change my mind

(1) The October CABA IPCBA (about 8–10 Nov) or the October REM (about 5 Nov) coming in clearly below 1.7 or above 2.2 would shift the median by roughly half the gap. (2) Evidence that INDEC's October basket carries a clothing/seasonal jump (spring-season rebound) or a large regulated-price rise not captured above would push the median toward 2.1–2.2; an announced large retroactive tariff cut would pull it toward 1.7.

### Sources

1. https://www.iproup.com/finanzas/72300-indec-confirma-inflacion-de-19-en-septiembre-categorias-con-mayor-aumento.amp (accessed 2026-11-02)
2. https://www.canal26.com/economia/2026/10/13/la-inflacion-de-septiembre-fue-de-19-y-acumula-un-alza-de-236-en-lo-que-va-del-2026/ (accessed 2026-11-02)
3. https://www.infobae.com/economia/2026/11/02/que-esperan-las-consultoras-privadas-para-el-dato-de-inflacion-de-octubre/ (accessed 2026-11-02)
4. https://www.bloomberglinea.com/latinoamerica/argentina/ipc-de-octubre-2026-que-inflacion-esperan-las-consultoras/ (accessed 2026-11-02)
5. https://www.bcra.gob.ar/publicaciones/relevamiento-de-expectativas-de-mercado-rem-septiembre-de-2026/ (accessed 2026-11-02)
6. https://eleconomista.com.ar/economia/la-desinflacion-tambien-estanco-precios-cierran-octubre-alzas-18-2-n99289 (accessed 2026-11-02)
7. https://indicadores.ar/cotizacion-dolar/2026-10 (accessed 2026-11-02)
8. https://www.canal26.com/economia/2026/10/08/inflacion-en-ciudad-de-buenos-aires-fue-de-18-en-septiembre-01-mas-que-en-agosto/ (accessed 2026-11-02)
9. https://www.riotimesonline.com/?p=751500 (accessed 2026-11-02)

**Question**: [What will Argentina's month-on-month inflation (INDEC national CPI) be for October 2026?](https://www.metaculus.com/questions/46408/)
**Date**: 2026-11-02
**Forecast**: Median 1.90%, IQR [1.80%, 2.05%]
**Thesis**: Last print 1.9% and seven private trackers at 1.8–2.1% (mean 1.94%) outweigh the stale REM of 1.7%, with fuel and food pushing up and flat FX and falling clothing pulling down. Most sensitive to whether INDEC's food and regulated components follow the hot weekly trackers.
