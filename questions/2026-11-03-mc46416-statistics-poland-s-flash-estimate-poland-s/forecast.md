# What will Statistics Poland's flash estimate of Poland's Q3 2026 GDP growth be?

| | |
|---|---|
| **Source** | metaculus — https://www.metaculus.com/questions/46416/ |
| **Tournament** | minibench — one shot, window 2026-11-03T03:23:37Z -> 2026-11-03T06:23:37Z |
| **Type** | discrete |
| **Opened / Closes / Resolves** | 2026-11-03 / 2026-11-03 / 2026-11-13 |
| **Status** | closed |
| **Current forecast** | Median 3.8, IQR [3.55, 4] (v1, 2026-11-03) |
| **Community** | hidden — bot tournament |
| **Next review** | — |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-11-03

### What resolves YES

The question resolves to the headline year-on-year real growth of Polish GDP in Q3 2026, seasonally unadjusted, constant prices, exactly as stated in GUS's flash estimate ("Szybki szacunek PKB za 3 kwartał 2026"), due 2026-11-13 (Trading Economics lists 13 Nov; Q2's flash was 13 Aug). Only the flash counts; the later preliminary estimate and revisions do not. If the release gives several y/y rates, the unadjusted one is used. The value is reported to one decimal (the scale runs 2.4–4.8 in 0.1 steps, open on both sides).

Arithmetic. Latest published quarters (GUS revision of 2026-10-16, via xyz.pl): Q1 2026 = 3.7 % (was 3.5), Q2 2026 = 4.1 % (flash 3.8 on 13 Aug, regular 3.9 on 31 Aug, now 4.1). Target quarter is the next one, Q3 2026; one quarter ahead. Base: Q3 2025 was 3.7 flash → 3.8 regular, seasonally adjusted q/q about 0.8–0.9 (pre-revision; 2025 quarters were revised up ~0.2 pp on 16 Oct). Mechanical carry-over: y/y(Q3) ≈ 4.1 + q/q(Q3'26) − q/q(Q3'25 ≈ 0.9–1.0). A Q3 q/q of 0.5 gives about 3.7; 0.8 gives about 4.0; 0.2 gives about 3.4. No fallbacks in the criteria apply.

### Outside view

Reference class: the next quarter's y/y in a slowly moving series. Poland's y/y has moved by ≤0.4 pp between consecutive quarters in 2025-26 (3.4→3.8→4.0→3.5/3.7→3.9/4.1 across revisions), so the last value (4.1) with mean reversion toward the annual-forecast average (~3.7) gives a prior of ~3.8–3.9, sd ~0.4. Flash-versus-consensus errors in recent quarters were small (Q1 2026: 3.4 vs 3.6; Q2 2026: 3.8 vs 3.8; Q3 2025: 3.7 vs 3.7), i.e. sd ≈ 0.15–0.2 around consensus. Here no hard consensus is visible, so uncertainty is larger.

### Inside view

Evidence points to a slowdown from the revised 4.1 %: September construction −9 % y/y (consensus was far higher), retail sales +3.3 % y/y (Sep) and −3.8 % m/m, while industry beat (+4.6 % y/y vs 3.1 % consensus). Bank views are dispersed: PKO BP (20 Oct, after the revision) "most likely around 3 %"; ING BSK (22 Sep, before the revision and the weak construction) ~3.5 %; Trading Economics ~3.5 %; question text cites mBank 3.6–3.8 and Pekao 3.8–3.9 (not independently verified); mBank's 2026 annual forecast of 3.9 % with Q4 at 3.7 % implies a Q3 near 4 %. PKO's ~3 % is hard to square with its own annual 3.8 % and the mechanics above (it would need a q/q of about −0.1 %), so I give it partial weight. Q3 2026 also has one more working day than Q3 2025 (15 Aug is a Saturday in 2026 and a Friday holiday in 2025; my own calendar count, an in-lieu day off may offset part), a small plus for the unadjusted figure; and every recent revision of GUS quarters has gone up. Weighted centre 3.8 %, below the ~4.0 % carry-over because construction/investment softness and the retail slowdown point to a lower q/q than Q2's ~1.0. Left tail is fatter than right: weak data are known, upside rests on lumpy investment and inventories/net exports I have no data for. Adjustments (two events): post-revision bank nowcasts below the carry-over, −0.3 pp from 4.0; extra working day, +0.1 pp.

Distribution (percentiles, %): p5 3.1, p10 3.3, p25 3.55, p50 3.8, p75 4.0, p90 4.2, p95 4.35.

### Evidence

- GUS revision 2026-10-16: Q1 3.7, Q2 4.1; driven by public consumption and gross fixed capital formation [1].
- Q2 2026: flash 3.8 (13 Aug), 3.9 (31 Aug), q/q 0.9→1.0; investment +8.4 %, private consumption +2.8 % [2].
- September data (20–22 Oct): industry +4.6 % y/y, construction −9.0 % y/y (SA −7.2), retail +3.3 % y/y [3][4].
- PKO BP 2026-10-20: Q3 growth "najpewniej" slowed to about 3 % [5]. ING BSK 2026-09-22: ~3.5 % [6]. mBank 2026-10-30: weaker construction may lower Q3, partly recouped in Q4; 2026 forecast 3.9 % [7].
- Six-institution average 2026 forecast 3.68 % (30 Oct) [7]; Trading Economics Q3 forecast 3.5 % [8].

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus CP | hidden — bot tournament | 2026-11-03 | |
| Polymarket / Kalshi | none found | 2026-11-03 | no market on Polish GDP |
| PKO BP | ~3.0 % | 2026-10-20 | "najpewniej"; low weight (inconsistent with its annual 3.8 %) |
| ING BSK | ~3.5 % | 2026-09-22 | pre-revision |
| Trading Economics | 3.5 % | 2026-11-03 | model/forecast |
| mBank / Pekao | 3.6–3.8 / 3.8–3.9 % | late Oct (per question text) | unverified by me |

### What would change my mind

A published Pekao/PKO/mBank note with a firm Q3 nowcast (a cluster at 3.8–4.0 would move the median to ~3.9; one at ≤3.3 to ~3.5), and any sign that the Q2 revision to 4.1 comes with a very high Q3 2025 base (q/q ≥1.1), which would push the carry-over lower.

### Sources

1. https://xyz.pl/?p=262951 (accessed 2026-11-03)
2. https://bank.pl/gus-zrewidowal-w-gore-odczyt-wzrostu-pkb-polski-w-ii-kwartale-2026-roku/ (accessed 2026-11-03)
3. https://xyz.pl/?p=264288 (accessed 2026-11-03)
4. https://tradingeconomics.com/poland/retail-sales-annual/news/594141 (accessed 2026-11-03)
5. https://www.wnp.pl/rynki/pko-bp-w-iii-kw-2026-r-wzrost-pkb-spowolnil-do-ok-3-proc,1110849.html (accessed 2026-11-03)
6. https://www.wnp.pl/rynki/ing-bsk-wzrost-pkb-w-iii-kw-2026-r-moze-wyniesc-ok-3-5-proc,1101485.html (accessed 2026-11-03)
7. https://www.analizy.pl/tylko-u-nas/40940/prognozy-pkb-i-inflacji-pazdziernik-2026-ulga-w-tym-roku-wyzsze-ceny-w-przyszlym (accessed 2026-11-03)
8. http://tradingeconomics.com/poland/gdp-growth-annual (accessed 2026-11-03)

**Question**: [What will Statistics Poland's flash estimate of Poland's Q3 2026 GDP growth be?](https://www.metaculus.com/questions/46416/)
**Date**: 2026-11-03
**Forecast**: Median 3.8%, IQR [3.55%, 4.0%]
**Thesis**: The revised Q2 level (4.1 % y/y) and an extra working day carry over to about 4.0 %, but weak September construction and retail data and bank nowcasts of 3–3.5 % pull the centre to 3.8 %. Most sensitive to the actual Q3 q/q, which the banks disagree on.
