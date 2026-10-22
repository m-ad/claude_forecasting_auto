# Will Ukraine strike a Russian oil refinery between October 29 and October 31, 2026?

| | |
|---|---|
| **Source** | metaculus — https://www.metaculus.com/questions/46180/ |
| **Tournament** | minibench — one shot, window 2026-10-22T05:40:32Z -> 2026-10-22T08:40:32Z |
| **Type** | binary |
| **Opened / Closes / Resolves** | 2026-10-22 / 2026-10-22 / 2026-11-02 |
| **Status** | open |
| **Current forecast** | Median 50.0%, IQR [38.0%, 62.0%] (v1, 2026-10-22) |
| **Community** | hidden — bot tournament |
| **Next review** | — |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-10-22

### What resolves YES

YES if, on any day from 29 to 31 October 2026 (inclusive, Moscow time, UTC+3), at least one Ukrainian long-range drone or missile strike *hits* a crude-oil refinery inside Russia's pre-2014 borders. A hit means impact, fire or damage at the refinery site, including debris from an intercepted drone that falls on the site. The source can be Ukraine's General Staff, a Russian regional official, or credible media. Oil depots, export terminals, pumping stations and pipelines do not count, and neither does an attack fully intercepted away from the site. The strike date is the date of the reported impact. Three days, so roughly 72 hours of opportunity.

### Outside view

The reference class is three-day windows during Ukraine's 2025–26 refinery campaign. While the campaign was active (Aug–Oct 2025; Jul–Oct 2026), reported refinery hits came every one to three days, in clusters. One example: 8 Aug 2026 hit Syzran and Ilsky [7], and early October 2026 saw Volgograd on 2 Oct, Omsk and Salavat on 8 Oct, and Ukhta on 9 Oct [1][2][3]. Gaps of about 5–6 days also occurred (2 Oct to 8 Oct). Treating hit-days as clustered at roughly 0.3 a day gives about 60–75% for an arbitrary active three-day window. A rate of 0.3 a day without clustering would give about 65%. During declared or de facto pauses (11–14 Oct 2026) the rate fell to about zero. No per-day public tally exists; Reuters and Kpler count refineries, not strike-days [8]. So the base rate is approximate.

### Inside view

The question's background says the tempo is "near-daily when active". That overstates the last week:

- **Last refinery hit:** Ryazan on 15 Oct, with a fire from debris and the CDU-6 crude unit halted [4][5].
- **Since then (16–22 Oct):** I found no confirmed refinery hit.
  - The 1,000-drone raid of 18 Oct hit the St Petersburg oil *terminal* and the Ruchi *depot* [6]. Some wire copy called these "two refineries ablaze", but neither counts.
  - On the night of 20–21 Oct, 373 drones flew over 15 regions with no refinery reported hit [10].
  - One report said Kyiv had claimed no new refinery attacks since 15 Oct.
  - This may be partly a gap in my searching, but seven quiet days is longer than the usual active-campaign gap.
- **US pressure is at its peak:**
  - Trump called the resumption "a disgrace" [9].
  - The US reportedly reduced satellite access and is holding Patriot deliveries.
  - Witkoff and Kushner keep asking Kyiv to stop, and the midterms fall on 3 Nov, right after the window.
- **Kyiv may be steering away from diesel:** Zelensky offered to stop "targeting Russian diesel" for 30 days in exchange for Patriot interceptors (18–19 Oct) [11][12]. The US envoys showed no openness, so no pause is in force. Still, the offer and the choice of export terminals over refineries on 18 Oct suggest Kyiv may be limiting refinery strikes quietly. **This is speculation.**
- **Against a pause:** Zelensky said "we're done" with the truce on 15 Oct, and Russia keeps hitting Ukrainian energy targets. Ukraine kept up mass drone raids after 15 Oct, and a refusal of the Patriot deal could just as well bring a demonstrative strike.

Decomposition:

| Branch | P(branch) | P(hit in 29–31 Oct given branch) | Contribution |
|---|---|---|---|
| Refinery campaign active at normal tempo by 29 Oct | 0.55 | 0.72 | 0.40 |
| De facto or formal pause on refineries (deal, US leverage, pre-midterm restraint) | 0.45 | 0.15 (pause breaks, or debris at a refinery during a raid on other targets) | 0.07 |
| **Total** | | | **≈ 0.47** |

I add a small amount because an LLM resolver might read loosely worded reports ("oil refinery ablaze" for a terminal) as YES. **Final: 50%.** The interquartile range (IQR, the middle half of my belief) is wide because the campaign's state over the last week is unclear.

### Evidence

- 2 Oct 2026: Volgograd refinery stopped all crude processing after a drone attack (Reuters via Meduza) [3].
- 8 Oct 2026: Omsk refinery struck, claimed by the General Staff (Reuters) [1]. Salavat struck the same day; satellite imagery shows two primary units damaged [2].
- 9 Oct 2026: Lukoil Ukhta refinery hit [2].
- 11 Oct 2026: Trump announced an "energy ceasefire". Moscow never confirmed it, and Ukraine held off for about three days [4][13].
- 15 Oct 2026: Ryazan refinery fire, confirmed by Governor Malkov. The Russian Defence Ministry said it downed 4 Flamingo missiles and 69 drones, and debris started the fire [4][5].
- 15–16 Oct 2026: Trump called the resumed strikes "a disgrace" (CP24/Reuters) [9].
- 18 Oct 2026: 1,015 drones by Russia's count. They hit the St Petersburg oil terminal and the Ruchi depot, not refineries [6].
- 18–19 Oct 2026: Zelensky offered a 30-day halt on refinery strikes in exchange for Patriot interceptors. The envoys showed no openness [11][12].
- 20–21 Oct 2026: the Russian Defence Ministry reported 373 Ukrainian drones overnight. No refinery hit was reported [10].

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus CP | hidden — bot tournament | 2026-10-22 | |
| Polymarket / Kalshi | none found | 2026-10-22 | no market on refinery strikes |
| Manifold | none found | 2026-10-22 | |

### What would change my mind

- **Toward YES:** a confirmed refinery hit between 22 and 28 Oct. That would show the campaign is active, and I would move to about 70–75%.
- **Toward NO:** a US–Ukraine deal (Patriots for a pause on refinery strikes) or a renewed energy truce announced before 29 Oct. That would bring it to about 10–15%.

### Sources

1. Reuters via Korea Times, "Ukraine says it hit Russia's largest oil refinery", https://koreatimes.co.kr/world/20261009/ukraine-says-it-hit-russias-largest-oil-refinery (accessed 2026-10-22)
2. Meduza, Salavat strike, https://meduza.io/en/news/2026/10/08/ukrainian-drones-strike-oil-refinery-in-russia-s-bashkortostan ; Ukrainska Pravda, Ukhta, https://www.pravda.com.ua/eng/news/2026/10/09/8057186/ (accessed 2026-10-22)
3. Meduza, Volgograd refinery shuts down, https://meduza.io/en/news/2026/10/06/another-russian-refinery-goes-offline-volgograd-plant-shuts-down-completely-after-ukrainian-drone-attack-reuters-reports (accessed 2026-10-22)
4. AP, "Ukraine resumes attacks on Russian oil refineries after brief truce", https://mynews13.com/fl/orlando/ap-top-news/2026/10/15/ukraine-resumes-attacks-on-russian-oil-refineries-officials-say-after-brief-truce (accessed 2026-10-22)
5. The Moscow Times, Ryazan fire, https://www.themoscowtimes.com/2026/10/15/ukrainian-drones-spark-fire-at-ryazan-refinery-as-zelensky-vows-to-resume-attacks-a93981 (accessed 2026-10-22)
6. Al Jazeera, "Ukraine launches over 1,000 drones at Russia", https://www.aljazeera.com/news/2026/10/19/ukrainian-drone-attack-on-russias-st-petersburg-kills-1-hits-energy-sites (accessed 2026-10-22)
7. blue News, Syzran and Ilsky hit, 8 Aug 2026, https://www.bluewin.ch/en/news/ukrainian-drone-attacks-hit-two-refineries-li.3556432 (accessed 2026-10-22)
8. Al Arabiya / Kpler, Russian refinery runs at 21-year low, https://english.alarabiya.net/News/world/2026/07/14/russian-oil-refinery-runs-at-21year-lows-after-drone-attacks-kpler-says (accessed 2026-10-22)
9. CP24 / Reuters, Trump calls refinery strikes a "disgrace", https://www.cp24.com/news/world/2026/10/16/ukraines-resumption-of-strikes-on-russian-refineries-is-disgrace-trump-says/ (accessed 2026-10-22)
10. Izvestia, 373 Ukrainian drones downed overnight, https://en.iz.ru/en/2187741/2026-10-21/air-defense-forces-shot-down-373-ukrainian-drones-overnight ; Anadolu, https://www.anews.com.tr/world/2026/10/21/russia-ukraine-report-3-killed-following-exchange-of-overnight-strikes (accessed 2026-10-22)
11. Kyiv Post, "Zelensky Offers to Halt Russian Refinery Strikes in Exchange for Patriot Missiles", https://www.kyivpost.com/post/87487 (accessed 2026-10-22)
12. Kyiv Post, "Zelensky Says US Patriot Missiles Nearly Gone, Offers 30-Day Russian Oil Strike Pause", https://www.kyivpost.com/post/87567 ; Euromaidan Press, https://euromaidanpress.com/2026/10/20/no-warning-capped-starlink-unsigned-patriots-zelenskyy-lists-us-holds-to-senators-as-kyiv-reads-them-as-pressure/ (accessed 2026-10-22)
13. Al Jazeera, Trump announces energy ceasefire, https://www.aljazeera.com/amp/news/2026/10/11/trump-says-ukraine-russia-agree-to-energy-ceasefire-2 (accessed 2026-10-22)

**Question**: [Will Ukraine strike a Russian oil refinery between October 29 and October 31, 2026?](https://www.metaculus.com/questions/46180/)
**Date**: 2026-10-22
**Forecast**: Median 50.0%, IQR [38.0%, 62.0%]
**Thesis**: In an active campaign, a three-day window has a reported refinery hit about 60–75% of the time (Oct 2026: Volgograd, Omsk, Salavat, Ukhta, Ryazan). But no refinery hit has been confirmed since Ryazan on 15 Oct. US pressure peaks before the 3 Nov midterms, and Zelensky has offered a 30-day refinery pause in exchange for Patriots. The forecast turns on whether Kyiv is quietly holding back on refineries; a confirmed hit before 29 Oct would move it sharply up.
