# How many drones will Ukraine's Air Force report Russia launched at Ukraine on the night of 12–13 November 2026?

| | |
|---|---|
| **Source** | metaculus — https://www.metaculus.com/questions/46381/ |
| **Tournament** | minibench — one shot, window 2026-11-02T05:21:55Z -> 2026-11-02T08:21:55Z |
| **Type** | numeric |
| **Opened / Closes / Resolves** | 2026-11-02 / 2026-11-02 / 2026-11-13 |
| **Status** | open |
| **Current forecast** | Median 148, IQR [108, 212] (v1, 2026-11-02) |
| **Community** | hidden — bot tournament |
| **Next review** | — |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-11-02

### What resolves YES

The question resolves to one number: the headline count of drones (UAVs) launched that the Ukrainian Air Force gives in its morning report on Telegram (t.me/s/kpszsu) on 13 November 2026. The report covers the night of 12–13 November, normally from 18:00 Kyiv time on 12 November. Subtypes and decoys are not added on top of the headline figure. Shot-down counts are not used, and neither are daytime waves on 13 November. If the Air Force revises the figure, the latest one published before 18:00 Kyiv time on 13 November counts. The range is closed at 0 and open above 1,000. The night is **11 nights after today** (2 November), so no current-week data bears on it directly. The question is a draw from the nightly distribution, with no visible signal for that specific night. The latest values: 134 (30–31 October), 433 (31 October–1 November, a wave) and 193 (1–2 November, preliminary). The last wave before that was 580 on 14–15 October.

### Outside view

The reference class is nightly Air Force headline drone counts in autumn 2026. The nights listed for 19–30 October 2026 are 165, 186, 176, 126, 153 or 140, 280, 88 or 100, 112 and 113. Their median is about 130 and their range is 88–280, and none of them was a wave night. Large strikes (300+ drones and missiles) ran at 2–6 a month in the first half of 2026 (Institute for the Study of War, ISW), about one every 5–10 days, in clusters [5]. Wave nights in 2026 ran from 400 to 700, with a peak of about 948 over 24 hours in March. October 2026 had at least one (580). Monthly averages are higher than a typical night: May 2026 averaged 167 a day [6], and September 2026 about 220–270 a day including daytime launches [2]. That gap reflects the skew from wave nights and daytime waves.

### Inside view

A research scout read the nightly reports from 15 October to 2 November 2026: 149, 180, 210, 176, 153, 140, 280, 88, 112, 113, 134, **433 (31 Oct–1 Nov)** and 193 (1–2 Nov, preliminary) [9, 10]. Leaving out the 433 wave, the median is about 150. On 1 November a separate daytime wave of 326 drones followed the night; it does not count here. The two 400+ waves found, 14–15 Oct (580) and 31 Oct–1 Nov (433), are 17 days apart. If that rhythm held, the next wave would come around mid-November. That is speculation, because ISW shows the spacing varies (about 5–10 days in H1 2026).

I used a mixture model. **86 % is a normal night**, lognormal with a median of 140 and σ 0.40, fitted to the 88–280 range since 15 October. **14 % is a wave night**, lognormal with a median of 430 and σ 0.30, matching the ISW frequency of about 4–5 large strikes a month. Not every large strike is drone-heavy at night, so I set the weight slightly below 5/30. **1 %** is a near-zero night (weather, a lull, a truce). Model output: p5 72, p10 85, p25 111, p50 151, p75 218, p90 374, p95 480. I trimmed it slightly toward the late-October lull (88–134 for four nights running) and widened the low tail, because November 2025 analogues include nights of 71 and 38. Final percentiles: p5 55, p10 75, p25 108, p50 148, p75 212, p90 370, p95 480. The Trump-announced "energy truce" of 11 October has not cut launches: the 580-drone night came three days later, and the 433 wave on 31 October [3, 7]. I give it a small weight in the low tail only.

### Evidence

- 14–15 Oct 2026: 580 strike UAVs (Shahed, Gerbera, Parodiya decoys) plus 2 Kh-59 missiles from 18:00; 536 neutralised [1].
- 16 Oct 2026 (daytime): 315 drones plus 15 Banderol/Dan-T. Daytime waves are reported separately and do not count here [3].
- 19–20 Oct: 165. 22–23 Oct: 176. 25–26 Oct: 140 plus 4 missiles. 28–29 Oct: 112 [3, 4]. 26–27 Oct: 280; 27–28 Oct: 88; 29–30 Oct: 113 (question text).
- Zelensky: about 2,700 attack drones in one week in mid-October 2026, about 385 a day including daytime; more than 2,000 in the week to 20 Sept [7].
- ISW: 300+ strikes numbered 3 in January, 6 in February, 4 in March, 5 in April, 6 in May and 2 in June 2026, clustered [5].
- May 2026: 5,181 Shahed/Geran, an average of 167 a day (Institute for Science and International Security) [6].
- Energy truce: announced by Trump on 11 October 2026; the Kremlin said "contacts ongoing" and gave no confirmation [7].
- 30–31 Oct: 134. 31 Oct–1 Nov: **433** (371 neutralised). Daytime 1 Nov: 326 plus 6 Banderol. 1–2 Nov: 193 (154 downed; preliminary) [9, 10].

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus CP | hidden — bot tournament | 2026-11-02 | |
| Polymarket / Kalshi / Manifold | no drone-count market found | 2026-11-02 | Only ceasefire-in-2026 markets exist; snapshots are stale |

### What would change my mind

- Is 12–13 November a wave night? That one fact moves the answer from about 130 to 400+. Ukrainian officials sometimes warn days ahead of a "massive strike". A warning dated 10–12 November would shift the median well up.
- A confirmed and observed energy truce would compress the distribution toward 50–120.

### Sources

1. Interfax-Ukraine, 580 drones on 14–15 Oct 2026 — https://en.interfax.com.ua/news/general/1220461.html (accessed 2026-11-02)
2. Cached Metaculus question text (recent nightly counts; September monthly figures via search summary) — raw/metaculus-question-2026-11-02.json (accessed 2026-11-02)
3. Ukrainska Pravda, 315 drones + 15 Banderol on 16 Oct 2026 — https://www.pravda.com.ua/eng/news/2026/10/16/8058422/ ; 165 drones 20 Oct — https://www.pravda.com.ua/eng/news/2026/10/20/8058847/ ; 176 drones 23 Oct — https://www.pravda.com.ua/eng/news/2026/10/23/8059345/ (accessed 2026-11-02)
4. NV, 112 drones on 28–29 Oct 2026 — https://english.nv.ua/nation/russian-forces-launch-drone-attack-against-ukraine-50654388.html (accessed 2026-11-02)
5. ISW / Critical Threats, frequency of large strikes in H1 2026 — https://www.criticalthreats.org/analysis/russian-offensive-campaign-assessment-july-2-2026 (accessed 2026-11-02)
6. Institute for Science and International Security, May 2026 Shahed analysis — https://isis-online.org/uploads/isis-reports/documents/May-2026-Updated-Analysis-of-Russian-Shahed-type-UAVs-Deployment-Against-Ukraine_Final.pdf (accessed 2026-11-02, search summary)
7. Ukrainska Pravda, Kremlin on energy truce — https://www.pravda.com.ua/eng/news/2026/10/12/8057592/ ; Trump truce claim — https://www.pravda.com.ua/eng/news/2026/10/11/8057478/ (accessed 2026-11-02)
8. Censor.net, jet-powered drone figures for September 2026 — https://censor.net/en/news/4027102/in-september-russia-deployed-approximately-3-500-jet-powered-uavs-against-ukraine (accessed 2026-11-02)
9. Ukrinform, 433 drones on 31 Oct–1 Nov 2026 — https://www.ukrinform.net/rubric-ato/4180165-air-defense-neutralizes-371-of-433-russian-drones-launched-against-ukraine-overnight.html (accessed 2026-11-02)
10. Ukrinform, 193 drones on 1–2 Nov 2026 — https://www.ukrinform.net/rubric-ato/4180368-air-defenses-down-154-out-of-193-drones-used-by-russia-to-attack-ukraine-since-evening.html (accessed 2026-11-02)

**Question**: [How many drones will Ukraine's Air Force report Russia launched at Ukraine on the night of 12–13 November 2026?](https://www.metaculus.com/questions/46381/)
**Date**: 2026-11-02
**Forecast**: Median 148 drones, IQR [108 drones, 212 drones]
**Thesis**: From 15 October to 2 November 2026, normal nights ran 88–280 drones (median about 150), with waves of 580 (14–15 Oct) and 433 (31 Oct–1 Nov). Large strikes have come every 5–17 days, so 12–13 November is a draw from a right-skewed mixture with about a 14 % chance of a wave night. The forecast is most sensitive to whether that night is one of Russia's massed strikes.
