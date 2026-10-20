# How many of the 18 crew still missing from the HS Dignity and Wine Trader Black Sea attacks will have their bodies recovered by October 29, 2026?

| | |
|---|---|
| **Source** | metaculus — https://www.metaculus.com/questions/46146/ |
| **Tournament** | minibench — one shot, window 2026-10-19T15:27:13Z -> 2026-10-19T18:27:13Z |
| **Type** | discrete |
| **Opened / Closes / Resolves** | 2026-10-19 / 2026-10-19 / 2026-10-30 |
| **Status** | closed |
| **Current forecast** | Median 0.4, IQR [0, 3] (v1, 2026-10-19) |
| **Community** | hidden — bot tournament |
| **Next review** | — |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-10-19

### What resolves YES

The question resolves to a count, an integer from 0 to 18 (both bounds closed). It counts the 18 crew missing as of 16 Oct 2026: 11 from HS Dignity, which sank about 15–17 nautical miles off Krapets/Shabla, Bulgaria, on 13 Oct, and 7 from Wine Trader, which caught fire about 13 nautical miles southeast of Sulina, Romania, on 15 Oct. A crew member counts only if their body has been *physically recovered*, from the sea or the wreck, and authorities attribute it to one of these two vessels. The figure is taken from credible reporting as of 23:59 UTC on 29 Oct 2026. Crew presumed dead without a body do not count, and neither do crew found alive. Bodies from other vessels in the same campaign are excluded. If reporting is ambiguous, the lowest firmly established number is used. That rule, and the fact that an LLM does the resolving, pull the answer toward 0 whenever reporting is thin.

### Outside view

The reference class is crew missing at sea after a ship sinks or catches fire, where the search has been suspended. Examples are the Sanchi (2018, 32 crew, 3 bodies recovered, almost all from the burning ship), the Gulf of Aden and Red Sea Houthi strikes (True Confidence: bodies of the 3 dead found on board; Eternity C: most missing never found), and the earlier Bulgarian sinking in this same October 2026 campaign. In that sinking, Bulgaria called off the search for 10 crew after finding no trace [6]. I have no formal n. Roughly, in more than half of such cases no body is recovered within about two weeks of a sinking in open water. A burned vessel that **stays afloat** is the main exception: remains are often recovered once the fire is out and the ship is boarded, though this can take days to weeks.

### Inside view

- **HS Dignity (11):** the ship sank in open water. Bulgaria formally ended the search at 15:00 on 14 Oct because of the weather [1], and Bulgarian reporting on 15–16 Oct says the remaining sailors are still unaccounted for [2]. Crew trapped in the hull will not be recovered without salvage diving, which is unlikely within two weeks. Crew who went into the water could resurface and wash ashore after one to three weeks in water at about 15 °C. I put P(≥1 recovered) at about 20%, mostly 1–2 bodies.
- **Wine Trader (7):** this is the main upside. The first drone strike reportedly hit the crew accommodation at about 04:00 [3], so the missing crew were plausibly trapped on board. The ship was anchored, carried no cargo and was still afloat on 15 Oct. Specialist personnel and IGSU rescuers were put aboard by vessel and Black Hawk helicopter, but the hazardous conditions and high waves prevented any search [3][4] (IGSU is Romania's General Inspectorate for Emergency Situations). Once the fire is out and the ship can be boarded or towed, remains could be recovered in a batch. But four days later I found no report of any recovery. Identification and attribution of badly burned remains can also lag, and the resolution's "lowest firmly established" rule penalises vague reports. I put P(≥1 recovered by 29 Oct) at about 35%, and given a recovery, typically 2–7 bodies.
- Combined, P(0) ≈ 0.80 × 0.65 ≈ 0.52. The rest of the mass is spread across 1–7 with a thin tail above 7. A Wine Trader batch recovery could coincide with a few HS Dignity bodies washing ashore.

| Outcome | Probability (approx.) |
|---|---|
| 0 | 52% |
| 1–2 | 18% |
| 3–5 | 16% |
| 6–7 | 7% |
| 8–18 | 7% |

Percentiles (native units, continuous representation over the discrete bins): p5 −0.3, p10 −0.2, p25 0.0, p50 0.4, p75 3.0, p90 6.0, p95 8.0.

### Evidence

- 13 Oct 2026: HS Dignity was sunk by a drone off Krapets. Of 16 crew, 5 were rescued and 11 are missing [5][7].
- 14 Oct 2026: BTA (Bulgaria's state news agency) reported the search was officially abandoned at 15:00 because of the weather [1]. Maritime.bg reported on a later date that the remaining sailors are still unaccounted for [2]. I found no report of a body recovered.
- 15 Oct 2026: Wine Trader caught fire 13 nautical miles southeast of Sulina. Of 12 crew, 5 were evacuated and 7 are missing, according to ANR, Romania's Naval Authority [4][8]. The San Marino registry said the conditions on board prevented any search, and damage to the firefighting system stopped firefighting [3].
- 15–18 Oct 2026: Romanian reports say the search was resumed but hampered by high waves, and that recovering people from on board was not yet possible safely [8][9]. My searches as of 19 Oct found no report of a recovered body from either ship. One Romanian site reported only 3 still missing; this is unconfirmed and conflicts with ANR.

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus | hidden — bot tournament | 2026-10-19 | |
| Polymarket / Kalshi / Manifold | none found | 2026-10-19 | no matching market |

### What would change my mind

- Whether Wine Trader is still afloat and when it is boarded or towed. A report that its fire is out and it is being towed to Constanța or Sulina would push the median up to about 3–5. A report that it sank would push P(0) toward 70%.
- Any body washing ashore on the Bulgarian or Romanian coast in the next ten days and being attributed to HS Dignity.

### Sources

1. BTA, "Bulgaria Abandons Search for Crew of HS Dignity", https://www.bta.bg/en/news/world/1224856-bulgaria-abandons-search-for-crew-of-hs-dignity (accessed 2026-10-19)
2. Maritime.bg, "В неизвестност остават останалите моряци от „HS Dignity“" ("The remaining HS Dignity sailors remain unaccounted for"), https://www.maritime.bg/155980/ (accessed 2026-10-19)
3. Riviera MM, "Chemical tanker reported on fire in Black Sea", https://www.rivieramm.com/news-content-hub/chemical-tanker-reported-on-fire-in-black-sea-eight-seafarers-missing-90273 (accessed 2026-10-19)
4. Agerpres, "Five crew members from Wine Trader rescued, seven others remain missing", https://agerpres.ro/english/2026/10/15/five-crew-members-from-wine-trader-rescued-seven-others-remain-missing--1603294 (accessed 2026-10-19)
5. CNN, "11 sailors missing after drone strike sinks merchant vessel near Bulgarian waters", https://www.cnn.com/2026/10/13/world/several-sailors-missing-after-drone-strike-sinks-merchant-vessel-near-bulgarian-waters (accessed 2026-10-19)
6. Euronews, "Bulgaria calls off search for 10 missing sailors after drone attack sinks cargo ship", https://www.euronews.com/2026/10/06/drones-hit-two-ships-off-coast-of-bulgaria-as-government-calls-emergency-meeting (accessed 2026-10-19)
7. Cyprus Mail, "From the Gulf to Europe, maritime trade faces a widening security crisis", https://cyprus-mail.com/2026/10/19/from-the-gulf-to-europe-maritime-trade-faces-a-widening-security-crisis (accessed 2026-10-19)
8. Antena3, "Alertă la Marea Neagră… 5 marinari au fost salvați. Alți 7, dați dispăruți" ("Black Sea alert… 5 sailors rescued, 7 others missing"), https://www.antena3.ro/actualitate/alerta-la-marea-neagra-inca-o-nava-a-cerut-ajutor-in-apropiere-de-sulina-dupa-ce-a-izbucnit-un-incendiu-8-persoane-date-disparute-807286.html (accessed 2026-10-19)
9. Jurnalul, "Mobilizare masivă lângă Sulina…" ("Massive mobilisation near Sulina…"), https://jurnalul.ro/stiri/observator/mobilizare-masiva-langa-sulina-elicoptere-black-hawk-si-nave-multirol-cauta-cei-sapte-marinari-disparuti-in-marea-neagra-1046982.html (accessed 2026-10-19)

**Question**: [How many of the 18 crew still missing from the HS Dignity and Wine Trader Black Sea attacks will have their bodies recovered by October 29, 2026?](https://www.metaculus.com/questions/46146/)
**Date**: 2026-10-19
**Forecast**: Median 0.4 crew, IQR [0.0 crew, 3.0 crew]
**Thesis**: Most crew missing after open-sea sinkings are never recovered within two weeks; HS Dignity sank and Bulgaria abandoned the search on 14 Oct, so ~52% on 0. The upside is Wine Trader, still afloat with crew likely trapped in its burned accommodation, so a batch recovery once it can be boarded is plausible; the forecast is most sensitive to whether that boarding happens before 29 Oct.
