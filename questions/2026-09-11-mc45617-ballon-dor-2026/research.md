# Research log — Who will win the 2026 Ballon d'Or?

Working notes. Rough is fine; **completeness beats polish**.

## Question mechanics

- **Resolution source**: France Football, at the ceremony on **2026-10-26** in London (70th
  edition). Not verifiable on Metaculus this session (Cloudflare block — see Dead ends), so
  the option set Metaculus offers is **unknown**; this forecast gives a full vector over the
  realistic field plus "anyone else", which can be collapsed onto whatever options exist.
- **Eligibility window: 2025-08-03 → 2026-07-19.** The window closes *on the day of the World
  Cup final*. This is the single most load-bearing mechanical fact in the question. The
  2026-27 club season explicitly does **not** count, so Kane's September ankle injury and
  Yamal's September goals are outside the window (though ballots are cast in the weeks before
  26 Oct, so recency effects on voters are an unquantifiable channel).
- **Electorate**: 100 journalists, **one per country from the top 100 of the FIFA Men's World
  Ranking** (snapshot published 2026-09-08). Each ranks **10** players from the 30-man
  shortlist; points 15 / 12 / 10 / … / 1. Ties broken on count of first-place votes.
  A one-journalist-per-nation panel is structurally more World-Cup-literate and less
  Bundesliga-literate than a club-football panel would be.
- **Shortlist**: 30 names published **2026-09-08**. PSG have 8 nominees, Bayern 4, Arsenal 3,
  Real Madrid 3, Barcelona 3.
- **Edge case**: a player can be listed under the club he played for *in the window* — Rodri
  appears as Manchester City despite an August 2026 move to Barcelona. Does not affect
  resolution.

## Reference classes considered

| Class | n | Window | Base rate | Source | Kept? |
|---|---|---|---|---|---|
| Polymarket favourite at T−45 days before the ceremony | 2 | 2024, 2025 | 1 of 2 won (Vinícius 0.625 → lost; Dembélé 0.790 → won) | Polymarket CLOB price history, computed this session | yes — but see note |
| World-Cup-year Ballon d'Or goes to a player of the WC-winning nation | 4 | 2010, 2014, 2018, 2022 | 0 of 4 (2010 Messi over Spain; 2014 Ronaldo over Germany; 2018 Modrić, a *runner-up*; 2022 ceremony predated the WC) | Wikipedia / SI | yes |
| WC Golden Ball winner takes the Ballon d'Or the same cycle | 4 | as above | 1 of 4 (Modrić 2018 — who also won the CL) | same | yes |
| Winner won the CL or reached its semi-final | 12 | 2012–2025 | 12 of 12 | Oddschecker | yes — screens *out* Mbappé |
| Winner without a major trophy (non-Messi) | 19 | 2006–2025 | ~1 of 19 | OddsShopper, citing the same underlying stat as Sky | kept, but weak — the "major trophy" definition is unverified and Kane won the Bundesliga |

**Note on the T−45 class.** The obvious reading — "a 62.5% favourite lost in 2024, so 62% is
too high now" — is a base-rate error and was rejected. One loss in two draws is exactly what
calibrated prices at 0.625 and 0.790 produce (expected hits 1.42, observed 1). The backtest
is evidence of *nothing* about miscalibration at n=2; it was computed, inspected, and given
no weight in the final number. Recorded here so the next update does not re-make the mistake.

## Decomposition

Under a 100-juror, 10-deep ranked ballot, the winner needs breadth, not just a peak. The
structural question for 2026 is whether the World-Cup bloc consolidates or fragments.

- **Kane's path**: near-universal presence on ballots. 73 goals + 8 assists in 65 games —
  the second-best scoring season by anyone since 2000 (behind only Messi's 82 in 2011-12) —
  European Golden Shoe, Bundesliga + DFB-Pokal + Supercup, Bayern to the CL semi-final,
  6 goals and England's best World Cup since 1966 (3rd). He passes the CL-semi-final screen.
  He wins if the Spanish vote splits.
- **Spain's fragmentation is real and is the mechanism.** Spain won the World Cup *defensively*
  — one goal conceded in the tournament, Golden Glove to Unai Simón — so there is no single
  dominant attacking narrative. The credit is spread across Rodri (Golden Ball), Yamal,
  Ferran Torres (final winner), Cubarsí (Best Young Player), Fabián Ruiz (the only man to win
  both the CL and the WC in the window) and Cucurella.
- **Yamal's path**: World Cup + La Liga + LaLiga Player of the Season, age 19, the
  new-era-coronation narrative France Football likes. Blocked by a hamstring tear announced
  2026-04-23 that cost him the entire club run-in, and a thin World Cup (1 goal, 1 assist in 8).
- **Rodri's path**: the Modrić-2018 template — World Cup Golden Ball in the cycle the WC closes
  the window. Weaker than Modrić's, though: Modrić paired it with a Champions League, while
  Rodri was sidelined five separate times and City won only the two domestic cups.
- **Mbappé's path**: Pichichi (25), CL top scorer (15 in 11), WC Golden Boot (10) and Bronze
  Ball — the best raw numbers after Kane — but Real Madrid won **nothing** and went out in the
  CL quarter-final, which would make him the first winner in 13 years to fail the
  CL-semi-final screen.

## Search log

| Date | Query / source | Finding | Effect on forecast |
|---|---|---|---|
| 2026-09-11 | Polymarket gamma-api `ballon-dor-winner-2026` | Kane 62.0%, Yamal 16.4%, Mbappé 10.1%, Rodri 5.5%, Messi 2.9%, Kvaratskhelia 2.1%; **$34.6m volume**, book sums to 100.5% | primary anchor |
| 2026-09-11 | Polymarket CLOB price history, same market | Kane 0.223 (17 Mar) → 0.268 (14 Jun) → 0.291 (14 Jul, mid-WC) → **0.593 (13 Aug)** → 0.670 (5 Sep) → 0.620 (11 Sep) | the re-rating happened *after* the final, on the shortlist/awards news; he has since given back 5pp |
| 2026-09-11 | Polymarket CLOB history, 2024 and 2025 markets | T−45: Vinícius 0.625 (lost), Rodri 0.300 (won); Dembélé 0.790 (won), Yamal 0.096 | the T−45 class above; no weight, see note |
| 2026-09-11 | Kalshi, via Covers/Yahoo, 2026-09-09 | Kane 63¢, Yamal 16¢, Mbappé ~14¢, Rodri 5¢; **~$8m volume** | independent venue, agrees |
| 2026-09-11 | Oddschecker UK board 2026-09-08; Betting Lounge best-price | Kane 4/7 (63.6%) / 8/13 (61.9%); Yamal 9/2; Mbappé 8/1; Rodri 8/1–9/1 | third independent venue, agrees |
| 2026-09-11 | Wikipedia 2026 Ballon d'Or; Pulse regulations digest | window 2025-08-03 → 2026-07-19; 100 voters one per top-100 FIFA nation; 15→1 over 10 places | the mechanics section |
| 2026-09-11 | Bundesliga.com Kane season numbers | 73 G + 8 A in 65; European Golden Shoe; 3rd straight Torjägerkanone | Kane's case |
| 2026-09-11 | Al Jazeera / ESPN WC awards | Golden Ball **Rodri**; Golden Boot **Mbappé** (10); Golden Glove Unai Simón (1 goal conceded); Best Young Player Cubarsí | Spain's credit is spread |
| 2026-09-11 | CBS 2026-04-23 | Yamal hamstring tear, out for the rest of the club season | caps Yamal |
| 2026-09-11 | OddsShopper 8-model ensemble, pub. 2026-07-29, upd. 2026-08-30 | Yamal 24.5%, Rodri 24.3%, **Kane 18.0%** | the one quantified dissent; see Dead ends for why it gets little weight |
| 2026-09-11 | Kalshi `/trade-api/v2` events + series probes | only `KXSUPERBALLONDOR-30` (a different question) is reachable by API | Kalshi figures above are second-hand via Covers/Yahoo, not API-verified |
| 2026-09-11 | metaculus.com, all access paths | blocked (see Dead ends) | **no CP/Pro/gold this version** |

## Dead ends and ruled-out hypotheses

- **metaculus.com was unreachable for the first half of this session** — Cloudflare 403 on
  `/api-proxy/aggregation_explorer/`, `/questions/<id>/`, `/embed/` and `/sitemap.xml`; page
  navigation died with `ERR_CONNECTION_RESET`; no Wayback snapshot; metaforecast.org is
  defunct. **Resolved mid-session**: the `metaculus-aggregations` skill was fixed upstream
  (commit ba7514b, "browser-native transport") and merged to `main` as PR #21. After rebasing
  onto it every question fetched cleanly. Two operational notes for next time: `--history`
  hangs on these questions (omit it), and a single fetch takes 100–200s, so run it in the
  background rather than under a 120s foreground timeout.
- **An earlier draft of this forecast was written blind**, before the criteria were available,
  and put Messi at 2.5% as a standalone line. He is **not a listed option**. The draft was
  corrected in place rather than appended as a v2, because it was never committed and a
  spurious version would pollute the calibration record; the ledger line was replaced to match.
- **OddsShopper's 18% for Kane** is the only quantified contrarian signal. Down-weighted, not
  ignored: it is a betting-affiliate content page whose "8-model ensemble" is not described,
  documented, or backtested anywhere, and it was last updated 2026-08-30 — before the
  shortlist. A 44-point disagreement with three independent liquid venues is far more likely
  to be a weak model than a real edge.
- **Oddschecker's US moneyline board** (Kane +162 = 38%) was rejected as stale: its overround
  is ~144% and it is the lone outlier against four other boards.
- **GiveMeSport's power ranking** was rejected outright: it ranks five players who are not on
  the 30-man shortlist (Salah, Palmer, Nico Williams, Wirtz, Raphinha).
- **"Kane 7/4" search snippet** irreconcilable with 4/7 and 8/13 on the same date; treated as
  a garbled transcription, not a real price.
- **European Golden Shoe 2025-26**: Bundesliga.com says Kane, one Gulf News headline says
  Mbappé. Kane's 36 league goals × 2.0 = 72 points beats Mbappé's 25 × 2.0 = 50, so Kane is
  almost certainly right; the conflict does not change any probability here.

## Open questions to chase next time

- The CP, once revealed. The question is still `upcoming` at n=10 with no Pro or gold cohort,
  so this version has no community anchor at all — the largest remaining hole.
- Whether any juror straw poll or result leak appears (2024's leak moved the market days out).
- Whether Kane's ankle keeps him out of Bayern matches into October — out-of-window for
  eligibility but in-window for voter salience.
- Whether the Spanish vote consolidates behind Rodri or Yamal in the October previews.

## v3 session — 2026-09-30 (leak check after voting closed)

Trigger: operator reports that voting has closed and a Facebook leak names Yamal. The wording
matches the Metaculus comment by @Theomachado, 2026-09-29.

| Date | Search / fetch | Finding |
|---|---|---|
| 2026-09-30 | Polymarket gamma event + CLOB hourly history (Kane, Yamal) | Kane 0.447 / Yamal 0.447, Messi 0.0405, Mbappé 0.0365, Rodri 0.0175. Volume $41.16M (up $2.26M since 26 Sep). Moves: 26 Sep 16–19 UTC Yamal 22 → 27 (England–Spain); 27–28 Sep drift to 34; **28 Sep 13–17 UTC 33.8 → 45.1 (unexplained)**; flat ~43–47 on the 29th |
| 2026-09-30 | Metaculus 45617 (skill, no --history) | CP Kane 53.0 / Yamal 33.0 (n=109); Pros 49.0 / 37.0 (n=10); gold 55.7 / 30.4 (n=29). Comments: Theomachado (the leak, "doubt it actually leaked a month early", still Kane 60 / Yamal 25); MaxA ("on nothing but speculation") |
| 2026-09-30 | "Ballon d'Or 2026 leak Yamal winner", "voting closed leaked results Facebook" | Dailysports (403), ZonalSports "exclusive" (no source), Foot Africa: voting closed at midnight on 27 Sep, and FF says nothing that circulates is official |
| 2026-09-30 | "Balón de Oro 2026 filtración Lamine Yamal ganador" | tunota: the list spread via Instagram DeportesRPC and Facebook — **Yamal 805, Kane 738, Mbappé 703**, unconfirmed. Search summary credits @MadeInArsenal6 on X with the "leak", with a claimed record of Messi, Rodri and Dembélé |
| 2026-09-30 | "MadeInArsenal6 Ballon d'Or leak 805 points" | **World Soccer Talk, 2025-09-22: the 2025 fake list also had "Yamal 805", with Dembélé 800 and Vitinha 643. Vincent García denied it: "I am the only one who knows the result."** Dembélé won 1,380–1,059, and Vitinha was 3rd on 703. The 2026 list reuses 805, and 703 is Vitinha's real 2025 total |
| 2026-09-30 | "MadeInArsenal6" | X status IDs found. Snowflake decode: Yamal "CONFIRM" at **2026-09-26 05:44 UTC**, before voting closed (TouchlineX "voting has closed" at 2026-09-27 22:04 UTC). The 2025 Dembélé "confirm" was on 2025-09-07, when Dembélé was already the heavy favourite |
| 2026-09-30 | England–Spain Nations League | 26 Sep (Sat), England 2–3 Spain at Wembley. Yamal scored in the 2nd minute; Kane's penalty hit the bar at 2–1 (Al Jazeera, ESPN). Out of the eligibility window |
| 2026-09-30 | "Polymarket Kalshi Ballon d'Or Yamal odds surge" | Prediction News: Kalshi Yamal 31 (27 Sep) → 51 ATH (28 Sep), attributed to thin liquidity. AllFootball: Polymarket Yamal 44.2 / Kane 42.6; names no cause. predictionnews pages returned 403 |
| 2026-09-30 | "Ballon d'Or 2026 jury vote … reveals ballot" | No juror has disclosed a vote. RMC and Goal pieces on lobbying only |
| 2026-09-30 | deportestvc.com, dated 2026-09-27 | Names @MadeInArsenal6 and quotes its "I can CONFIRM Yamal" post. The article predates voting close, which corroborates the snowflake timing. No point totals |
| 2026-09-30 | Spanish/French "fuite" search | Nothing from L'Équipe, RMC, Marca, AS or Mundo Deportivo reports a result |

### Dead ends

- The news trigger for the 28 Sep 13–17 UTC jump was **not found**. The best guesses are the
  X "confirmation" going viral after voting closed, or momentum from Kalshi FC's post. Either
  way it is unverified. This is the single most important open item.
- dailysports.net and predictionnews.com returned 403. They are known only through search
  summaries.
- There is no Metaculus `--history` this time (per v1's note that it hangs).

### Open questions for next time

- Did any credible outlet explain the 28 Sep move? Search for "whale", "Polymarket Ballon d'Or
  insider", and Kalshi FC.
- Final-week logistics: do Bayern or Barcelona schedule around 26 Oct, and do Kane or Yamal
  confirm attendance?
- Any jurors publishing their ballots early (Theomachado noted some do after the ceremony).

## v5 session — 2026-10-09 (cohort move; re-analysis)

Trigger: fresh Metaculus aggregations (`raw/metaculus-2026-10-09.json`, fetched by the operator
session, not re-fetched). Since 30 Sep: CP Kane 53.0 → 46.5 / Yamal 33.0 → 44.3 (n=123);
Pros 49.0 → 44.1 / 37.0 → 45.0 (n=10); gold 55.7 → 45.6 / 30.4 → 45.6 (n=31).

| Date | Search / fetch | Finding |
|---|---|---|
| 2026-10-09 | Metaculus comments (8, newest 8 Oct) | No leak cited. @sai_39 (2 Oct) quotes Polymarket at 58 and books at 7/10, and gives a World Cup-cycle table that includes **2023 Messi**. @DeRuina (30 Sep, 1 Oct) argues that on the journalist-only electorate every World Cup-year winner played in the final, and that Spain's vote has two homes (Rodri, Yamal). @Russell-viper (8 Oct) "had to agree with overall market's consensus", i.e. explicit market-following |
| 2026-10-09 | Re-read of v1's outside view | **Error found**: the "0 of 4 (2010, 2014, 2018, 2022)" class assigned Qatar 2022 to the 2022 award (Benzema, 2021–22 season). Qatar fell in the 2023 window, and Messi won. Corrected: 1 of 4; Golden Ball → Ballon d'Or 2 of 4; journalist-only "winner played in the final" 6 of 6 |
| 2026-10-09 | "2023 Ballon d'Or … eligibility … points" | Wikipedia/90min: window 1 Aug 2022 – 31 Jul 2023; Messi 462, Haaland 357; 65 vs 20 first-place votes |
| 2026-10-09 | "2010 FIFA Ballon d'Or journalists … Sneijder" | Maxifoot / 90min: journalists alone would have elected Sneijder (293) over Xavi (229) and Iniesta (226); Messi 175. The Spanish split is the precedent for v1's fragmentation thesis |
| 2026-10-09 | "Ballon d'Or 2026 … leak October" | French Football Weekly (9 Oct): *The Touchline* names the top two, Yamal and Kane, with no order; Canal+'s Garétier calls it "plausible". FullTime X "Yamal 1st, Mbappé 2nd" image reported as fabricated. No credible result report |
| 2026-10-09 | Polymarket gamma + Kalshi API, 05:09 UTC | Polymarket Kane 52.25 / Yamal 40.1 / Messi 3.15 / Mbappé 2.25 / Rodri 1.05; $46.29M volume (flat since v4). Kalshi Kane 52 / Yamal 42 / Mbappé 5 / Messi 4 |
| 2026-10-09 | Polymarket Yamal 6-hourly history | 54.75 (2 Oct 00:00) → 44.5 (5–7 Oct) → 44.05 (8 Oct) → 40.1 now. The Metaculus cohort move most likely began in the 1–5 Oct market spike, but the cohorts did not follow the market back down |
| 2026-10-09 | "Harry Kane injury Bayern October 2026" | Nothing current, and irrelevant anyway now that ballots are closed |

### Lesson

The cohort disagreement was signal. The error had been in the file since v1, and three updates
inherited it because each one wrote "Outside view: unchanged". Re-check the outside view when
cohorts with good track records diverge, rather than only scanning for news.

## v6 session — 2026-10-15 (Polymarket tripwire fired; re-analysis)

Trigger: scheduled review, which was due 2026-10-16. Metaculus aggregations were unavailable:
the parent session's single fetch returned 403 (Cloudflare). Only the bot-key API was readable
(`raw/metaculus-api-2026-10-15.json`): n 126 → 134, forecasts 1,823 → 2,005, comments 13 → 17,
criteria unchanged. No Metaculus endpoint was called from this session.

| Date | Search / fetch | Finding |
|---|---|---|
| 2026-10-15 | Polymarket gamma event (05:24 UTC) | Kane **63.05**, Yamal **29.7**, Mbappé 3.85, Messi 2.65, Rodri 0.65, Kvara 0.45, Dembélé 0.25; volume $50.25M (+$3.96M since v5; Kane + Yamal markets +$0.81M), liquidity $9.94M, book sum 101.7%. One-week change Kane +13.6, Yamal −14.35 |
| 2026-10-15 | Polymarket CLOB hourly history since 8 Oct | Kane drifted 0.49 → 0.56 on 8–9 Oct, then **jumped 0.56 → 0.63 between 17:00 and 18:00 UTC on 9 Oct**. Yamal 0.37 → 0.30. Since then Kane 0.59–0.67, Yamal 0.27–0.34 |
| 2026-10-15 | Polymarket data-api trades (taker), 9 Oct 16:00–20:00 UTC | ~$27k Kane and ~$29k Yamal taker flow. First aggressive prints at 17:42:41 UTC: one wallet bought Kane Yes and Yamal No (~$17k in total over the window), and five other wallets joined within four minutes. Yamal went 0.362 → 0.187 by 18:03. Cached to `raw/polymarket-trades-kane-yamal-2026-10-15.json` |
| 2026-10-15 | Polymarket comments | No trader cites a cause: "why is yamal dumping like a mf" (9 Oct 21:04 UTC); "I refuse to believe there are no leaks" (10 Oct); an unsourced "insiders revealed Kane, Mbappé, Yamal", whose author then says "follow the money", i.e. the price itself |
| 2026-10-15 | Kalshi markets + hourly candlesticks | Kane 64 (bid/ask 64/65), Yamal 31, Mbappé 6, Messi 4. Hourly candle ending 18:00 UTC on 9 Oct: Kane 0.56 → 0.64, Yamal 0.40 → 0.23 (~52k / 26k contracts), so the move was simultaneous with Polymarket |
| 2026-10-15 | "Ballon d'Or 2026 Kane Yamal odds October 9", "bookmakers … Kane gamble" | William Hill (12 Oct, updated 14 Oct): Kane 1/2 from 5/4, Yamal 7/4; Phelps credits Kane's six Nations League goals. OLBG (14 Oct): bet365 Kane 1/2, Yamal 2/1, Mbappé and Messi 22/1, Rodri and Olise 40/1. World Soccer Talk (10 Oct): attributes the shift to Kane's brace against Czechia (6 Oct) and Yamal's blank against Croatia, both out of window |
| 2026-10-15 | "Ballon d'Or 2026 leak winner Kane", "Balón de Oro 2026 filtración", "fuite L'Équipe", "Kane Ballon d'Or Gewinner Bericht" | No credible-outlet result report. New fake list via Vermouth Deportivo / Yahoo Noticias (9 Oct 16:42 UTC): Yamal 670, Messi 546, Mbappé 401, Kane 342. Defensa Central: 4,051 of 6,700 points unallocated, so impossible. It names Yamal first, so it cannot explain the move against him |
| 2026-10-15 | "Messi present Ballon d'Or Yamal" | "Juan Jesus" (via sportstiger) claimed Messi would present the trophy, read as pointing to Yamal. Romano: Messi "has not received an invitation" (Goal 13 Oct; Lente Desportiva 14 Oct). Lente's "Yamal 10/11 favourite" odds line is stale or recycled |
| 2026-10-15 | Infobae 29 Sep (citing L'Équipe) | **Only Vincent García and, in the final hours, the producer Marc Las know the result.** Winners are no longer called in advance; photo shoots happen on the night. Las: "Este año, quien diga saberlo miente" |
| 2026-10-15 | "jury Ballon d'Or 2026 … mon vote / reveals vote" (EN/FR) | No juror disclosures |
| 2026-10-15 | "Rodri Balón de Oro votos periodistas España" | Nothing on a Spanish-bloc split |
| 2026-10-15 | L'Équipe readers' poll (COPE, Record, Vardeportivo, 12–13 Oct) | Mbappé 34.2%, Kvaratskhelia 24.3%, Kane 8.6%. Readers, not jurors; ignored |
| 2026-10-15 | Ceremony logistics | Still Monday 26 Oct, London Palladium, 20:00 London / 21:00 CET (callmepower.be; Goal; William Hill). Nothing on Kane or Yamal travel. Barcelona beat Galatasaray 4–1 in the CL on 13 Oct, which is irrelevant |
| 2026-10-15 | Manifold API search | No 2026 Ballon d'Or market; only a 2027 market with 11 bettors |
| 2026-10-15 | Outside-view re-verification | 1998 Zidane, 2002 Ronaldo, 2006 Cannavaro confirmed (France Football list via Ahram; Daily Star 2006). v5's 6-of-6 "winner played in the WC final" screen now rests on verified rows |

### Dead ends

- **The 9 Oct 17:42 UTC trigger was not found.** I searched in EN, FR, ES and DE and checked
  X-status timing for TouchlineX: the Ballon d'Or posts that search surfaced decode to
  2026-10-06 13:30 and 2026-10-08 11:02 UTC, both before the move. Polymarket's own commenters are equally
  puzzled. The candidates are: (a) private information (weight 6%); (b) one large trader moving
  a thin book, with cross-venue arbitrage carrying it to Kalshi; (c) a salience move on
  October international form, which is the bookmakers' story. None is verified.
- oddspedia, bookies.com and X status pages returned 403/402; they are known only through
  search summaries.

### Lesson

The pre-registered "move ~40% of the way after checking the cause" rule worked as an anchor.
The cause check, though, is where the work is. A move that no one, including the traders
making it, can explain, and that two venues repeat within the hour, is more likely one book
being pushed than a leak, especially when the organiser has restricted who can know.
Moved ~1/3 of the way, not 40%.

### Open questions for next time (T−7d 2026-10-19, T−1d 2026-10-25)

- Does the Kane ~63 level hold, or round-trip as the 1 Oct Yamal spike did?
- Ceremony-week logistics: Bayern's and Barcelona's fixtures on 24–25 Oct, and any camp that
  skips London.
- Fresh Metaculus cohorts: did Pros and gold follow the 9 Oct market move?
