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
