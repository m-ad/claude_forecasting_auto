# Research log — Will the US approve a $10B exchange stabilisation facility for Pakistan before 2027?

Working notes. Rough is fine; **completeness beats polish**. The next update reads this to
learn what was already checked and what was already ruled out.

## Question mechanics

- Resolution source: "credible sources" confirming *formal approval* by the US government of an
  exchange stabilisation support facility, or an equivalent currency swap, of ≥ $10B, before
  2027-01-01. Execution or drawing is not needed (fine print).
- Text retrieved via the browser API path on 2026-10-05 (the bot-key API returned null while the
  question was "upcoming"). Opens 2026-10-06 17:00 UTC, CP reveal 2026-10-09 14:36 UTC.
- Edge cases: an Argentina-style "framework agreement" announced by Bessent probably counts.
  Sub-$10B lines, DFC/EXIM credits and guarantees do not. A Fed swap line is implausible for
  Pakistan, but would count as an "equivalent currency swap".

## Reference classes considered

| Class | n | Window | Base rate | Source | Kept? |
|---|---|---|---|---|---|
| Large ESF credits to foreign governments | ~5 (Mex 82, Mex 95, Bra 98, Uru 02, Arg 25) | 1980–2026 | ~1 per 9–10 yrs | CRS IF13200; Wikipedia ESF | yes (shows rarity) |
| Serious public requests to US Treasury for bilateral liquidity → approved within ~6 months | not enumerable | 2015–2026 | guess 10–25% | judgement | yes, as a soft prior |

## Decomposition

P(any offer before Dec 31) 0.22 × P(≥$10B | offer) 0.45 × P(formal approval reported | both) 0.9 ≈ 0.09.

ESF constraint: liquid assets were $23.5B in Treasuries plus $4.3B in FX (Feb 2026), and the
Argentina $20B line is still open (only $2.5B drawn, then repaid). SDRs are ~$176B but less liquid.

## Search log

| Date | Query / source | Finding | Effect on forecast |
|---|---|---|---|
| 2026-10-05 | Reuters via Tribune/ANI/ARY, 21–22 Jul | request: $10B bilateral facility, ≤5y, to Bessent | baseline |
| 2026-10-05 | Al-Monitor/TRT, Bessent readout 22 Jul | praise for reforms; no mention of the facility; "self-reliance" | ↓ |
| 2026-10-05 | Arab News/Profit 24 Jul | Mark Sobel (ex-Treasury): decline; "permanent ward" of the IMF | ↓ |
| 2026-10-05 | Nikkei 2 Aug | leverages Iran mediation; US scrutiny of China debt | neutral |
| 2026-10-05 | Dawn 13 Aug (geopolitics) | "may not be approved"; anti-China rationale | neutral |
| 2026-10-05 | Pak Observer 19 Aug; Tribune 26 Aug | "under consideration", "constructive", expected by Sept | slight ↑ then ↓ (slip) |
| 2026-10-05 | Dawn/Reuters 17 Sep | "response within two months"; also seeking a bigger China swap; EXIM/DFC talks | ↓ (slip; alternatives) |
| 2026-10-05 | Radio Pakistan 22 Sep; Daily Pakistan | Trump "wonderful person"; UNGA reception meeting 23 Sep; no deliverable | neutral |
| 2026-10-05 | CRS IF13200 (Apr 2026) | ESF size; six-month rule; Argentina line active | ↓ (capacity) |
| 2026-10-05 | H.R. 6061; Warren letter Feb 2026 | congressional pushback on ESF use for Argentina | slight ↓ |
| 2026-10-05 | Polymarket/Kalshi/Manifold search | no market | — |

## Dead ends and ruled-out hypotheses

- Reuters direct fetch blocked; used syndications (Dawn, Tribune, Arab News).
- Wikipedia "Pakistan in the 2026 Iran war" has no coverage after April 2026 on this topic.
- No news found dated 2026-09-24 → 2026-10-05 about the facility (searched "stabilisation facility" October 2026).

## Open questions to chase next time

- Metaculus CP after reveal (2026-10-09).
- Any US-side statement (Treasury, NSC, Bessent interview). Watch for Aurangzeb at the IMF/World
  Bank annual meetings in October 2026, where he may meet Treasury again.
- Status of the Argentina ESF line (capacity).
- Whether Pakistan announces DFC refinery financing or EXIM Boeing deals instead (the substitute path).

---

## Update 2026-10-12 (v2)

### Search log

| Date | Query / source | Finding | Effect on forecast |
|---|---|---|---|
| 2026-10-12 | Metaculus bot-key API (parent-fetched) | open since 06 Oct; n=69; criteria/fine print identical to 05 Oct; CP/Pro/gold hidden (bot key) and browser path 403 | — |
| 2026-10-12 | "Pakistan US exchange stabilisation facility October 2026" (web + Pakistani outlets) | nothing newer than 17 Sep "within two months" | ↓ hazard decay |
| 2026-10-12 | Bessent comment on Pakistan swap | none since 22 Jul readout; Treasury "declined to comment" | ↓ slight |
| 2026-10-12 | APP 08 Oct: IMF SLA 4th EFF review | ~.2B; gross reserves ~1.5B end-Sep; rating upgrades, market access | ↓ (less need) |
| 2026-10-12 | EXIM framework (Digital Pakistan 25 Jul; ProPakistani 24 Sep) | UNGA signing target slipped; talks on PIA/refinery/Reko Diq continue | → |
| 2026-10-12 | Argentina ESF line status | no termination reported; Warren letter Feb 2026 only | → |
| 2026-10-12 | White House visit Shehbaz/Munir Oct 2026 | none announced | → |
| 2026-10-12 | IMF/WB Annual Meetings 2026 | Bangkok, 12-18 Oct; possible Treasury meeting | new tripwire |
| 2026-10-12 | Manifold API, Polymarket gamma search, Kalshi open events | no matching market (raw/markets-search-2026-10-12.json) | — |

### Dead ends
- The aaj.tv "staff-level agreement" hit is from Mar 2026 (3rd review), not October. The October SLA comes from APP (08 Oct).
- No October 2026 Pakistani or US article on the ESF request at all.

### Open questions to chase next time
- Metaculus CP / Pro / gold, if the browser path works again.
- Bangkok Annual Meetings readouts (Treasury and Pakistan MoF), 12-18 Oct.
- The ~17 Nov "two months" deadline.


### Addendum 2026-10-12 (sources added to the v2 block)
- Treasury ESF statement, 31 Aug 2026: $24.9B Treasury securities, $4.9B FX, $218.8B total (mostly SDR). BCRA $20B ESA still in force with no drawings; Mexico $9B ESA. Confirms the Argentina tripwire has not fired. → no change.
- SBP reserves $21.45B in the week to 2 Oct (total liquid $26.8B). Dawn 18 Sep and Tribune 20 Aug re-read for timeline and "not a loan" framing. CRS IF13200 re-read for the six-month rule. → no change.
