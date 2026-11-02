# What will Rosstat's preliminary estimate of Russia's Q3 2026 GDP growth (year-on-year) be?

| | |
|---|---|
| **Source** | metaculus — https://www.metaculus.com/questions/46380/ |
| **Tournament** | minibench — one shot, window 2026-11-02T05:00:55Z -> 2026-11-02T08:00:55Z |
| **Type** | discrete |
| **Opened / Closes / Resolves** | 2026-11-02 / 2026-11-02 / 2026-11-13 |
| **Status** | closed |
| **Current forecast** | Median 0.6, IQR [0.5, 0.8] (v1, 2026-11-02) |
| **Community** | hidden — bot tournament |
| **Next review** | — |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-11-02

### What resolves YES

This is a discrete numeric question. It resolves to Rosstat's preliminary index of the physical volume of GDP for Q3 2026 (July–September 2026) relative to Q3 2025, minus 100, to one decimal place: an index of 100.6 resolves as 0.6. The source is the release "Справка о предварительной оценке динамики ВВП в III квартале 2026 года", scheduled for 13 Nov 2026. Later revisions (the "первая оценка" in December) do not count. The target period is one quarter ahead of the last Rosstat print (Q2 2026, +1.3%, published 12 Aug 2026). The comparison base is Q3 2025, first printed at +0.6% and since revised to +0.8% [1][4]. The question's bins run from -1.5 to 2.5 in 0.1 steps, with both ends open. The Ministry of Economic Development (MinEk) published its Q3 estimate on 29 Oct 2026: +0.6% y/y [2]. The question therefore comes down to the gap between Rosstat's preliminary print and MinEk's monthly-indicator estimate: 0.6 + gap.

### Outside view

Reference class: Rosstat's preliminary quarterly print minus MinEk's pre-release estimate for the same quarter, Q1 2024–Q2 2026 (n = 7 usable pairs) [3][4][5]:

| Quarter | Rosstat prelim | MinEk est. | Gap |
|---|---|---|---|
| Q1 2024 | 5.4 | 5.4 | 0.0 |
| Q2 2024 | 4.0 | 4.0 | 0.0 |
| Q1 2025 | 1.4 | 1.7 | −0.3 |
| Q2 2025 | 1.1 | ~1.1 | ~0.0 |
| Q3 2025 | 0.6 | 0.6 | 0.0 |
| Q1 2026 | −0.2 | −0.3 | +0.1 |
| Q2 2026 | 1.3 | 0.9 | +0.4 |

The modal gap is 0, the mean is about +0.03 pp and the standard deviation about 0.2 pp. Applied to MinEk's 0.6, the outside view is centred on 0.6, with roughly two-thirds of the mass in 0.4–0.8.

### Inside view

- MinEk's monthly profile is July +0.6, August +0.8 and September +0.5, giving Q3 +0.6 and January–September +0.6 [2][6]. That is consistent with an H1 of +0.6 and a soft quarter.
- The Bank of Russia (CBR) forecast Q3 at +0.5% in August [7]. Its mid-October commentary said Q3 growth persists but is slower than Q2 [6]. The question text quotes Deputy Governor Zabotkin (9 Oct) saying Q3 is faster than H1 (0.6%), which points slightly above 0.6. I could not independently verify that quote.
- Upside: the two most recent quarters both beat MinEk (+0.1 and +0.4), and the Q2 beat was large. Downside: industrial production was weak (January–August 0.0%) and retail growth slowed to +3.3% in August [8][9]. The only clear miss below MinEk was Q1 2025 (−0.3).
- The net is a median kept at 0.6 with a slightly fatter upper tail (adjustment logged). Percentiles: p5 0.15, p10 0.3, p25 0.5, p50 0.6, p75 0.8, p90 1.0, p95 1.2.

### Evidence

- 2026-10-29: MinEk "О текущей ситуации": Q3 2026 +0.6% y/y, September +0.5%, January–September +0.6% [2].
- 2026-08-12: Rosstat's Q2 2026 preliminary of +1.3% beat MinEk's 0.9% and the CBR's 0.8% [3][5].
- 2026-05-15: Rosstat's Q1 2026 preliminary of −0.2% compared with MinEk's −0.3% [3].
- 2025-11-14: Rosstat's Q3 2025 preliminary of +0.6% matched MinEk's 0.6% (CBR: 0.4%) [4].
- 2025-05: Rosstat's Q1 2025 preliminary of +1.4% compared with MinEk's 1.7% [10].
- 2026-08-05: CBR estimated Q2 at +0.8% and expected Q3 at +0.5% [7].
- Industrial production for January–August 2026 was 0.0% y/y [8]. Retail sales grew +3.3% y/y in August 2026 [9].

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus CP | hidden — bot tournament | 2026-11-02 | |
| MinEk Q3 estimate | +0.6% | 2026-10-29 | monthly-indicator based |
| CBR Q3 forecast | +0.5% | 2026-08-05 | from the July forecast round |
| HSE consensus (question text) | +0.6% | Aug 2026 | not independently verified |
| Polymarket / Kalshi | none found | 2026-11-02 | no Russia quarterly GDP market |

### What would change my mind

- Evidence that MinEk's monthly series was itself revised up after Rosstat's Q2 release, so that 0.6 already embeds the Q2-type gap. That would tighten the distribution around 0.6.
- Rosstat sector data for September (construction, wholesale trade, agricultural harvest) well above or below the monthly figures. The size of the 2026 harvest is a known swing factor for Q3.

### Sources

1. Metaculus question text, cached at raw/metaculus-question-2026-11-02.json (accessed 2026-11-02)
2. https://sberbusiness.live/news/rost-vvp-rossii-v-sentyabre-zamedlilsya-do-05 (accessed 2026-11-02)
3. https://ru.themoscowtimes.com/2026/05/15/rosstat-otsenil-snizhenie-vvp-rf-v-1-kv-v-02-luchshe-mineka-i-tsbr-a195454 (accessed 2026-11-02)
4. https://ru.themoscowtimes.com/2025/11/14/rosstat-vvp-rf-v-3-kv-po-predvaritelnoy-otsenke-vyros-na-06-gg-a180156 (accessed 2026-11-02)
5. https://meduza.io/news/2026/08/12/ekonomika-rossii-vo-vtorom-kvartale-vyrosla-na-1-3-posle-provala-v-pervom (accessed 2026-11-02)
6. https://interfax.com/newsroom/top-stories/119348/ (accessed 2026-11-02)
7. https://investfuture.ru/articles/ts-b-otsenil-rost-vvp-vo-ii-kvartale-v-0-8-i-ozhidaet-0-5-v-iii-1184148570 (accessed 2026-11-02)
8. https://www.finmarket.ru/main/article/6712908 (accessed 2026-11-02)
9. https://ru.themoscowtimes.com/2026/09/30/rost-roznichnykh-prodazh-v-rf-v-avguste-zamedlilsya-do-33-a207462 (accessed 2026-11-02)
10. https://smart-lab.ru/blog/1155517.php (accessed 2026-11-02)
11. https://www.finmarket.ru/news/6597631 (accessed 2026-11-02)

**Question**: [What will Rosstat's preliminary estimate of Russia's Q3 2026 GDP growth (year-on-year) be?](https://www.metaculus.com/questions/46380/)
**Date**: 2026-11-02
**Forecast**: Median 0.6%, IQR [0.5%, 0.8%]
**Thesis**: MinEk's monthly-indicator estimate for Q3 2026 is +0.6% y/y (29 Oct). Rosstat's preliminary print has matched MinEk within ±0.1 pp in 5 of 7 recent quarters (misses: −0.3 in Q1 2025, +0.4 in Q2 2026), so the median stays at 0.6 with a slightly heavier upper tail. The forecast is most sensitive to whether the Q2-2026-style upside gap recurs.
