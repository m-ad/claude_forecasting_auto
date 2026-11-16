# How many cumulative confirmed measles cases will Mexico's daily measles bulletin report on November 26, 2026?

| | |
|---|---|
| **Source** | metaculus — https://www.metaculus.com/questions/46577/ |
| **Tournament** | minibench — one shot, window 2026-11-16T07:22:17Z -> 2026-11-16T10:22:17Z |
| **Type** | numeric |
| **Opened / Closes / Resolves** | 2026-11-16 / 2026-11-16 / 2026-11-27 |
| **Status** | open |
| **Current forecast** | Median 20860, IQR [20795, 20950] (v1, 2026-11-16) |
| **Community** | hidden — bot tournament |
| **Next review** | — |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-11-16

### What resolves YES

The question resolves to the combined 2025–2026 "Total casos confirmados acumulados" in the Secretaría de Salud (Ministry of Health) daily measles bulletin. It uses the latest edition dated on or before 26 Nov 2026 by its own "Información preliminar con fecha …" line. The 26 Nov edition falls on a Thursday, so it should exist. The latest edition I could read is dated **12 Nov 2026**, with **20,701** confirmed. That is +149 on the 20,552 of 11 Nov: 2 new lab-confirmed cases plus 147 backlog cases "dictaminados" (classified by expert review), 144 of them in Jalisco [1]. Mon 16 Nov is a federal holiday (the Revolution Day long weekend) [6], so 9 editions remain: 13 Nov and 17–20, 23–26 Nov. The resolution value is 20,701 plus whatever those 9 editions add. Both bounds are open; the 20,550 lower bound is already passed.

### Outside view

The cumulative total moved as follows: 20,229 (6 Oct) [4], 20,332 (19 Oct), 20,350 (23 Oct) [4], 20,375 (26 Oct), 20,410 (5 Nov), 20,552 (11 Nov) and 20,701 (12 Nov) [1]. From 6 Oct to 5 Nov it rose about 180 over about 22 editions, roughly 8/edition. The PAHO (Pan American Health Organization) figure for Mexico's 2026 cases rose 13,595 → 13,761 between EW39 and EW43 (epidemiological weeks), about 40/week [2]. At an October-like pace of 8–12 per edition, 9 editions add about 70–110, giving roughly 20,770–20,810.

### Inside view

The backlog push has clearly sped up: +142 between 5 and 11 Nov and +149 on 12 Nov alone. Cases under study fell from 910 to 695 in one day [1], around the 10–13 Nov PAHO re-verification meeting [3]. Of the 231 cases classified that day, about 65% were confirmed. Some 695 cases plus about 30 new notifications a week remain to classify. If most are classified by 26 Nov at 45–65% confirmation, that alone could add about 300–450. That is the upper tail. Batches are lumpy, though, and the push could ease once the PAHO meeting is over. Organic new lab confirmations are now only about 2–5 a day.

My central case is the October run-rate (+~100) plus some further batches (+~60), giving a **median of about 20,860**. A long right tail runs to about 21,170 at p95. The left tail is bounded: no backlog batches at all and only organic additions gives about 20,725 at p5. Revisions downward are rare.

| Percentile | 5 | 10 | 25 | 50 | 75 | 90 | 95 |
|---|---|---|---|---|---|---|---|
| Cases | 20,725 | 20,745 | 20,795 | 20,860 | 20,950 | 21,070 | 21,170 |

### Evidence

- 12 Nov 2026 bulletin: 20,701 confirmed; 46,598 EFE (febrile rash illness) cases notified; 25,202 discarded; 695 under study; 50 deaths; 32 EFE in EW45; 147 dictaminated cases (Jalisco 144, Baja California 3) [1].
- The bulletin index lists editions only on weekdays; the latest was 12 Nov at access [1].
- PAHO sitrep #15 (6 Nov): Mexico 13,761 cases in 2026 through EW43; 29 new cases in EW41–42 [2].
- The PAHO commission met 10–13 Nov; I found no published outcome [3].
- Excélsior: 20,229 (6 Oct cut), 20,350 (23 Oct cut) [4].

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus | hidden — bot tournament | 2026-11-16 | |
| Polymarket / Kalshi / Manifold | none found | 2026-11-16 | only US measles markets [5] |

### What would change my mind

How fast the 695 cases under study get adjudicated. If more Jalisco-style batches of 100+ appear in the 13–20 Nov editions, the outcome moves to my p90 or above (21,050+). If the 13 Nov edition and the following ones show only single-digit changes, the result lands near 20,760–20,800.

### Sources

1. Secretaría de Salud, Informe diario del brote de sarampión en México 2026 (index + 12 Nov PDF), https://www.gob.mx/salud/documentos/informe-diario-del-brote-de-sarampion-en-mexico-2026 and https://www.gob.mx/cms/uploads/attachment/file/1116356/Informe_diario_12_11_2026.pdf (accessed 2026-11-16)
2. PAHO, Informe de situación #15 sarampión, 6 Nov 2026, https://www.paho.org/es/documentos/informe-situacion-15-sarampion-region-americas-6-noviembre-2026 (accessed 2026-11-16)
3. PAHO, Comisión Regional de Monitoreo y Reverificación, https://www.paho.org/es/noticias/14-10-2026-comision-regional-monitoreo-reverificacion-eliminacion-sarampion-rubeola (accessed 2026-11-16)
4. Excélsior, "México supera 20 mil contagios de sarampión", https://www.excelsior.com.mx/nacional/mexico-supera-20-mil-contagios-sarampion-jalisco-encabeza-caso and https://www.excelsior.com.mx/nacional/sarampion-deja-50-muertes-y-mas-20-mil-casos-mexico (accessed 2026-11-16)
5. Manifold / Polymarket measles markets (US only), https://manifold.markets/event/total-cases-of-measles-reported-in (accessed 2026-11-16)
6. N+, Día festivo Revolución Mexicana 2026, https://www.nmas.com.mx/sociedad/dia-festivo-noviembre-2026-cambia-fecha-cuando-se-descansa-revolucion-mexicana/ (accessed 2026-11-16)

**Question**: [How many cumulative confirmed measles cases will Mexico's daily measles bulletin report on November 26, 2026?](https://www.metaculus.com/questions/46577/)
**Date**: 2026-11-16
**Forecast**: Median 20,860 cases, IQR [20,795, 20,950]
**Thesis**: The 12 Nov bulletin stands at 20,701 with 9 editions left before 26 Nov. The October run-rate (~8–12 per edition) gives ~20,800, and the backlog push (147 cases classified on 12 Nov, 695 still under study) adds a right-skewed batch allowance. The forecast is most sensitive to whether Jalisco-style batch confirmations continue after the PAHO meeting.
