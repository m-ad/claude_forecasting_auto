# How many AIS-visible commercial ships will the hormuz.now tracker count crossing the Strait of Hormuz on October 29, 2026?

| | |
|---|---|
| **Source** | metaculus — https://www.metaculus.com/questions/46161/ |
| **Tournament** | minibench — one shot, window 2026-10-20T02:07:37Z -> 2026-10-20T05:07:37Z |
| **Type** | discrete |
| **Opened / Closes / Resolves** | 2026-10-20 / 2026-10-20 / 2026-10-30 |
| **Status** | closed |
| **Current forecast** | Median 1.8, IQR [0.21, 5.5] (v1, 2026-10-20) |
| **Community** | hidden — bot tournament |
| **Next review** | — |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-10-20

### What resolves YES

The question resolves to the finalized integer shown on https://hormuz.now/traffic/2026-10-29 ("[N] AIS-visible commercial ships crossed the Strait of Hormuz"), for the full UTC day of 29 Oct 2026. Under hormuz.now's methodology that means distinct cargo or tanker ships ≥ 80 m (or ≥ 5,000 dwt) broadcasting AIS that cross the Musandam–Kuhestak gate line. Ships running dark are excluded. The page wording "no AIS-visible commercial ships crossed" means 0. Range 0–24, closed at 0, open above 24. The archive page beats the CSV if they differ, and the question is annulled if the site stops publishing.

### Outside view

The question text says the tracker counted about 9–10 a day in the week to 14 Oct (6–12 a day; 1 on 1 Oct). Other AIS-only series run lower: IMF PortWatch had 1 on 27 Sep, 4 on 4 Oct and 2 on 11 Oct, with a 7-day average of 4.1. Kpler had 7 and 10 on 6–7 Oct. A naive persistence prior would centre on about 5–9 with a wide spread. But the site itself has changed since the question was written (see below), so the most relevant reference class is the tracker's *current* output, and it has only one complete day.

### Inside view

- **The tracker was rebuilt on 19 Oct 2026.** Its archive, CSV and JSON now start on 19 Oct, and the changelog says "first data, earliest crossing in the log." Its first complete day, **19 Oct, is 0**, and 20 Oct is 0 so far (as of 02:12Z). The status feed shows 0 crossings over 24 hours, 7 days and 30 days, and "~0% of normal," while it still sees 1,555 vessels in its box. Whatever the cause (a collector reading public AIS map tiles that misses the gate, or real AIS-visible traffic collapsing), the resolving instrument currently reads 0. The question text's 9–10 a day comes from a series the site no longer publishes.
- **Escalation:** UKMTO has recorded about 20 attacks since 1 Oct. Two ships (GFS Pride, Cape Dao) sank around 14 Oct, and reports say Iran attacked ≥ 15 container ships in 10 days. This pushes traffic dark or away, so real AIS-visible traffic is plausibly near PortWatch's 1–4 a day, not 9.
- **Upside:** the site may fix or recalibrate the pipeline before 29 Oct. Iran's "seven-day reopening plan" is still on the table, and a deal could produce a surge (small tail beyond 24). Daily counts are lumpy: the trackers showed 20+ on some days in early October.
- **My distribution:** P(0) ≈ 35%, P(1) 12%, P(2) 10%, P(3) 8%, P(4–5) 10%, P(6–8) 10%, P(9–12) 8%, P(≥13) 7%. Median ≈ 2, IQR 0–5.

### Evidence

- hormuz.now daily page for 19 Oct: "no AIS-visible commercial ships crossed the Strait of Hormuz, on our count." Inbound, outbound, tankers and cargo all 0 [1] (accessed 2026-10-20).
- hormuz.now daily.json: 19 Oct total 0; 20 Oct 0, partial. The data page lists daily rows only since 19 Oct, with 0 commercial crossings in 30 days [2][3].
- hormuz.now methodology: gate method; collector reads public AIS map tiles every ~20 s; changelog entries dated 29 Sep and 19 Oct [4].
- status.json: PortWatch 11 Oct = 2, 7-day average 4.1, October average 3.5 [5].
- straits.live, 19 Oct: no Iran–US agreement, the 7-day plan still on the table, Iran attacked ≥ 15 container ships in 10 days [6].
- Mid-October sinkings and UKMTO's 20 attacks since 1 Oct [7].
- Kpler, 6–7 Oct: 7 then 10 commodity vessels, against more than 20 on the preceding Sunday and Monday [8].

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus CP | hidden — bot tournament | 2026-10-20 | |
| Polymarket / Kalshi | no live market on daily counts found | 2026-10-20 | Kalshi weekly series exists; no current price seen |
| Manifold | PortWatch 40+ by 20 Sep resolved NO | 2026-09-24 | low volume |

### What would change my mind

- hormuz.now posting non-zero daily counts for 20–28 Oct, which would show the new pipeline does catch crossings. That would shift mass to about 3–10.
- An Iran–US deal on the 7-day reopening plan before 29 Oct would raise the upper tail sharply.

### Sources

1. https://hormuz.now/traffic/2026-10-19 (accessed 2026-10-20)
2. https://hormuz.now/api/daily.json (accessed 2026-10-20)
3. https://hormuz.now/data (accessed 2026-10-20)
4. https://hormuz.now/methodology (accessed 2026-10-20)
5. https://hormuz.now/status.json (accessed 2026-10-20)
6. https://straits.live/briefs/2026-10-19 (accessed 2026-10-20)
7. https://www.hawaiitribune-herald.com/2026/10/15/nation-world-news/two-ships-sink-near-hormuz-after-being-hit-by-projectiles-amid-surge-in-attacks/ (accessed 2026-10-20)
8. https://www.theleader.com.au/story/9365051/hormuz-shipping-transits-at-lowest-in-over-two-months/ (accessed 2026-10-20)
9. https://straits.live/briefs/2026-10-08 (accessed 2026-10-20)

**Question**: [How many AIS-visible commercial ships will the hormuz.now tracker count crossing the Strait of Hormuz on October 29, 2026?](https://www.metaculus.com/questions/46161/)
**Date**: 2026-10-20
**Forecast**: Median 1.8 ships, IQR [0.21 ships, 5.5 ships] (continuous scale; integer bins: 0 ≈ 35%, median bin 2, p75 bin 5–6)
**Thesis**: The question cites about 9–10 a day, but hormuz.now rebuilt its data on 19 Oct and its first full day shows 0. AIS-only series such as PortWatch (2–4 a day) and the mid-October escalation (about 20 attacks, two sinkings) support a low count. About 35% is on 0, and the forecast is most sensitive to whether the new pipeline records any crossings at all.
