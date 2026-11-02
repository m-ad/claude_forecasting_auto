# How many commercial ship crossings of the Strait of Hormuz will be recorded on 12 November 2026?

| | |
|---|---|
| **Source** | metaculus — https://www.metaculus.com/questions/46386/ |
| **Tournament** | minibench — one shot, window 2026-11-02T06:51:57Z -> 2026-11-02T09:51:57Z |
| **Type** | discrete |
| **Opened / Closes / Resolves** | 2026-11-02 / 2026-11-02 / 2026-11-13 |
| **Status** | open |
| **Current forecast** | Median 8, IQR [5, 12] (v1, 2026-11-02) |
| **Community** | hidden — bot tournament |
| **Next review** | — |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-11-02

### What resolves YES

The question resolves to one number: the total commercial crossings, inbound plus outbound, that hormuz.now's archive page https://hormuz.now/traffic/2026-11-12 states for the UTC day 12 November 2026. Small craft are excluded; they are vessels under 80 m, tugs, dhows and fishing boats, which the page lists separately. The IMF PortWatch figure shown on the same page is ignored. If the archive page is unavailable, the 2026-11-12 row of hormuz.now/data is used. The range runs from 0 to 150, with a closed lower bound and an open upper bound.

The arithmetic: the last complete day published is 1 Nov (9 crossings), and the target day is 12 Nov. That is 11 days ahead, a single UTC day, read once.

The hormuz.now series under the current method began on 19 Oct. The complete days from 20 Oct to 1 Nov read 7, 11, 6, 9, 6, 4, 8, 5, 6, 11, 13, 12 and 9. That is a mean of 8.2 and a range of 4–13, and the 7-day average on 1 Nov was 9.1. The pre-crisis baseline is 84.8 a day.

### Outside view

The reference class is the series itself: 13 complete days under the current method, with a mean of 8.2, a standard deviation of about 2.8 and a slight upward drift over the last 4 days (11, 13, 12, 9).

Over an 11-day horizon in a war, the big risk is a regime change rather than noise. Since February this strait has gone through at least three regime shifts:

- an April reopening, reversed within a day;
- the June memorandum of understanding (MoU), after which crossings jumped within one day;
- the July collapse.

That is roughly one shift every 2–3 months, or about 10–15 % per 11-day window, split between up and down.

### Inside view

I used a three-scenario mixture, computed in `model.py` with negative-binomial and lognormal draws:

| Scenario | Weight | Distribution | Why |
|---|---|---|---|
| Status quo, restricted with permit traffic | 70 % | mean 9, sd 4 | late-October level with mild drift |
| Escalation after the 3 Nov US midterms | 16 % | mean 4, sd 2.5 | Trump told aides and Time that bombing could resume after the midterms [8]; tanker attacks peaked in early October [9]; PortWatch-like lows of 2–4 |
| Deal implemented or partial reopening by 12 Nov | 14 % | lognormal, median 24 | the Qatar seven-day plan is under discussion [5][6]; Iran wants to implement it in "even less than a week" [5]. After the June MoU, crossings went from under 10 to 25 a day on day 1 and 31–42 later (Kpler) [7] |

The reopening weight is held down by several facts:

- An Iranian official called the Qatar draft "unacceptable ideas, not a proposal" [6].
- I found no announcement of a deal or of a shipping-line resumption as of 2 Nov.
- Under the reported US sequencing, navigation would only resume on day 6 [6].
- Insurers lag behind any deal.

The mixture gives P(≥20) ≈ 10 % and P(≤3) ≈ 12 %. Its percentiles are p5 2, p10 3, p25 5, p50 8, p75 12–13, p90 19 and p95 29.

### Evidence

- **hormuz.now daily series, 19 Oct to 2 Nov** [1][2]. The daily totals are listed in the digest above. Of the 31 Oct crossings, 8 were outbound and 4 tankers. The 1 Nov crossings were all cargo ships, with no tankers. On 2 Nov the status was "Restricted", with 8 crossings in the last 24 h and about 681 ships stationary in the region [1][3].
- **PortWatch counts, 13–25 Oct** [1]. These ran 2–7 a day, with a mean of about 3.9. The PortWatch series runs at roughly half of hormuz.now's count, so the two are not interchangeable.
- **The June MoU precedent** [4][7]. The MoU was signed 17–18 Jun. Kpler and AXSMarine counted 25 crossings on 18 Jun, Kpler 42 on 20 Jun and 39 on 22 Jun. hormuz.now's FAQ puts June's average at 12.9 a day.
- **Diplomacy** [5][6].
  - Qatar's draft of 25 Oct sets out seven days of daily confidence-building steps.
  - On 28 Oct Araghchi said Iran was discussing implementation with mediators.
  - An Iranian official rejected the draft as "unacceptable ideas".
  - I found no Iran–US meeting in Turkey.
- **Escalation risk** [8][9]. Trump ruled out strikes before 3 Nov but floated their resumption afterwards. Reuters (7 Oct) reported the most tanker attacks of any week of the war in the week of 28 Sep–5 Oct.

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus CP | hidden — bot tournament | 2026-11-02 | — |
| Polymarket "Hormuz traffic returns to normal by Dec 31" | 12 % Yes | 2026-11-02 | $16.1M volume; resolves on a PortWatch 7-day average ≥ 60. Markets see a full normalisation in 2 months as unlikely [10] |
| Kalshi / Manifold | none current | 2026-11-02 | only stale or expired contracts |

### What would change my mind

- **A signed Iran–US deal, or an Iranian announcement of reopening, before about 9 Nov.** That would move the median to 20–30.
- **Renewed US strikes on Iran, or attacks on ships, after 3 Nov.** That would move the median to about 3–4.

The forecast is most sensitive to whether the Qatar seven-day process starts the week of 2 Nov.

### Sources

1. hormuz.now, home page and data — https://hormuz.now and https://hormuz.now/data (accessed 2026-11-02)
2. hormuz.now daily series JSON — https://hormuz.now/api/daily.json (accessed 2026-11-02)
3. hormuz.now archive pages for 31 Oct and 1 Nov — https://hormuz.now/traffic/2026-10-31, https://hormuz.now/traffic/2026-11-01 (accessed 2026-11-02)
4. Gulf News, "Ships surge out of Hormuz as Iran peace deal takes hold", 18 Jun 2026 — https://gulfnews.com/business/energy/ships-surge-out-of-hormuz-as-iran-peace-deal-takes-hold-asian-tankers-european-ships-lead-the-rush-1.500578568 (accessed 2026-11-02)
5. Arab News, "Iran says discussing plan with mediators to end war, reopen Hormuz", 28 Oct 2026 — https://www.arabnews.com/middle-east/iran-says-discussing-plan-with-mediators-to-end-war-reopen-hormuz-3008650 (accessed 2026-11-02)
6. Ynet, Qatar draft and Iranian reaction, 28 Oct 2026 — https://www.ynetnews.com/article/bkbihrjazl ; Al-Monitor/Reuters, 30 Sep 2026 — https://www.al-monitor.com/originals/2026/09/iran-receives-us-feedback-seven-day-trust-building-plan (accessed 2026-11-02)
7. Breitbart, Kpler counts after the June MoU, 23 Jun 2026 — https://www.breitbart.com/middle-east/2026/06/23/ship-trackers-see-more-vessels-passing-through-strait-hormuz/amp/ (accessed 2026-11-02)
8. Boston Globe, "Trump says US will not resume military strikes on Iran before Nov 3 midterm elections", 8 Oct 2026 — https://www.bostonglobe.com/2026/10/08/nation/trump-says-us-will-not-resume-military-strikes-iran-before-nov-3-midterm-elections/ ; Business Standard, 1 Oct 2026 — https://www.business-standard.com/world-news/iran-bombing-could-ramp-up-after-midterm-elections-donald-trump-126100101535_1.html (accessed 2026-11-02)
9. The Star/Reuters, tanker attacks peak, 7 Oct 2026 — https://www.thestar.com.my/news/world/2026/10/07/attacks-on-tankers-in-hormuz-hit-highest-of-any-week-since-start-of-iran-war-sources-say (accessed 2026-11-02, snippet)
10. Polymarket, "Strait of Hormuz traffic returns to normal by December 31?" — https://polymarket.com/event/strait-of-hormuz-traffic-returns-to-normal-by-december-31 (accessed 2026-11-02)

**Question**: [How many commercial ship crossings of the Strait of Hormuz will be recorded on 12 November 2026?](https://www.metaculus.com/questions/46386/)
**Date**: 2026-11-02
**Forecast**: Median 8 crossings, IQR [5 crossings, 12 crossings]
**Thesis**: hormuz.now's own series is the outside view: 4–13 commercial crossings a day since 20 Oct, with a 7-day average of 9.1 on 1 Nov. The median stays near it because Iran has not accepted the Qatar seven-day plan. The tails are fat in both directions. A deal implemented in early November could, as after the June MoU, take crossings to 20–40 (≈10–14 %). Renewed US strikes after the 3 Nov midterms could cut them to 2–4. The forecast is most sensitive to whether the Qatar process starts the week of 2 Nov.
