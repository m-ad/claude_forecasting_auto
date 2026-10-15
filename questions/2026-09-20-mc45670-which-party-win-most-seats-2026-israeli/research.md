# Research log — Which party will win the most seats in the 2026 Israeli election?

Working notes. Rough is fine; **completeness beats polish**. The next update reads this to
learn what was already checked and what was already ruled out.

## Question mechanics

- **Resolution source**: the 2026 Israeli legislative election, 27 October 2026. Official
  seat allocation is published by the Central Elections Committee (CEC,
  https://www.gov.il/en/departments/central-elections-committee/govil-landing-page).
  Final official results are gazetted ~8 days after polling day (2022: vote 1 Nov, official
  results 9 Nov), so a normal count resolves this well inside the 2027-01-01 window.
- **Release schedule / cutoff**: exit polls 22:00 IST on election night; rolling counts over
  the following 3–4 days; soldier/diplomat ("double-envelope") ballots counted last and have
  historically moved 1–2 seats. Election silence bars published polls from the end of Friday
  2026-10-23 — so the last ~72 hours of campaign are **unmeasured**, and that is exactly the
  window in which Israeli late swings have historically happened.
- **Options**: `Likud`, `Yashar`, `Other`. Metaculus post 45670 / question 45859.
  `cp_reveal_time` = 2026-09-24T17:00Z, `nr_forecasters` = 8 — **no community prediction,
  no Pro, no gold aggregation exists yet.** This forecast has no Metaculus anchor at all.

### Edge cases and ambiguities

1. **Exact tie in seats — unaddressed.** The criteria require a party that "receives more
   seats than any other"; the fine print covers only (a) a third party winning a plurality
   → `Other`, and (b) cancellation/postponement past 2027-01-01 → annulled. Question
   commenters `Theomachado` (2026-09-19) and `darkives` (2026-09-20) raised exactly this and
   expect **ambiguous resolution** absent an admin tie-breaker. This is not hypothetical:
   **April 2019 ended Likud 35 – Blue and White 35**, an exact tie, decided on votes
   (Likud 1,140,370 vs 1,125,881). My model puts P(exact tie) at **11.1%**.
   Polymarket's equivalent market *does* define a tie-break (more valid votes, then
   alphabetical). Metaculus does not.
2. **Mergers.** Metaculus does not say what happens if Likud contests jointly with another
   list (Polymarket does: the Likud option would carry the joint list). Moot in practice —
   lists closed 2026-09-08 and both Likud and Yashar filed alone. Likud's list already
   absorbs New Hope (merger formalised August 2025); Likud has a *surplus-vote* agreement
   with RZP–Zehut, which is not a joint list and does not affect this.
3. **`Other`.** Requires a third list to top the poll. Realistically only B'Yachad /
   "Together" (Bennett + Lapid), polling 9–16. ~0.8%.
4. **Annulment.** Postponing an Israeli election requires 80 Knesset votes
   (Basic Law: the Knesset §9A). Lists are filed, CEC disqualification decisions are due
   2026-09-27. P(no result before 2027-01-01) ≈ 1.5%.

## Reference classes considered

| Class | n | Window | Base rate | Source | Kept? |
|---|---|---|---|---|---|
| Israeli elections in which Likud was the largest single list | 12 | 1996–2022 | **6/12 outright, 1 tie** (1996 L, 1999 L, 2003 W, 2006 L, 2009 L, 2013 W, 2015 W, 2019A tie, 2019B L, 2020 W, 2021 W, 2022 W) | Wikipedia election articles | Kept as the crudest anchor: ~50% before any 2026 information |
| New centrist party led by an ex-IDF Chief of General Staff vs. Likud | 5 | 2019A, 2019B, 2020, 2021, 2022 | challenger largest **1/5**, tie 1/5 | ditto | Kept — directly analogous (Gantz then, Eisenkot now), but Gantz-era Likud polled 30–36, not 20 |
| **Drift in the Likud-minus-top-rival seat gap, ~5 weeks out → result** | 5 | 2015–2022 | +4.5, +4.5, −1.5, +1.7, ≈+1.0; **mean +2.0, sd 2.5** | Wikipedia polling pages, see below | **Load-bearing.** Shrunk ~40% toward zero to +1.2 |
| Same, but **final poll → result** (the "polls underestimate Likud" claim) | 5 | 2015–2022 | +9.5, +0.8, −0.4, +0.5, +0.75; **median +0.75** | ditto | Kept as a caution: the claim is almost entirely 2015 |
| Exact tie for largest party | 25 | 1949–2022 | 1/25 unconditional; 1/6 since 2015 | Wikipedia | Kept — conditional on a race this close the smooth-model figure (11%) beats the unconditional 4% |

### The polling-error numbers, in full

| Election | Likud rival | Gap ~5 wk out | Gap in final polls | Gap in result | Δ final→result | Δ 5wk→result |
|---|---|---|---|---|---|---|
| 2015 | Zionist Union | +1.5 | −3.5 (L 21.6, ZU 25.1) | **+6** (30–24) | **+9.5** | +4.5 |
| 2019 Apr | Blue and White | −4.5 | −0.8 (L 28.5, BW 29.3) | **0** (35–35) | +0.8 | +4.5 |
| 2019 Sep | Blue and White | +0.5 | −0.6 (L 31.4, BW 32.0) | **−1** (32–33) | −0.4 | −1.5 |
| 2021 | Yesh Atid | +11.3 | +12.5 (L 31.0, YA 18.5) | **+13** (30–17) | +0.5 | +1.7 |
| 2022 | Yesh Atid | n/a | +6.5 (L 30.5, YA 24.0) | **+8** (32–24) | +0.75 | ≈+1.0 |

**The single most important finding of this research.** "Israeli polls systematically
underestimate Likud" is a widely repeated claim; on the *largest-party gap* it rests almost
entirely on 2015. Strip 2015 and the mean final-poll gap error is **+0.4 seats**, i.e. noise.
What the record *does* support is that in two of the four close races (2015, 2019A) the gap
moved 4–5 seats toward Likud over the final five weeks — and in 2019A **both** big parties
gained ~6 seats simultaneously by consuming their own satellites, so the gap barely moved.
The mechanism is *late consolidation of large lists*, which is symmetric, not Likud-specific.
That is why the drift term here is +1.2 and not +2.0.

## The house-effect problem (the crux)

The 2026 section of the Wikipedia polling table parses to 250 rows
(`raw/wikipedia-polling-wikitext-2026-09-20.txt` + `raw/parse_polls.py` +
`raw/poll_analysis.py`), 70 of which carry usable Likud *and* Yashar figures with fieldwork
2026-08-01 → 2026-09-17. Nine mainstream houses (52 polls) and two Filber-lineage houses
(17 polls):

| Publisher | n | mean Likud | mean Yashar | mean gap | Likud ahead in |
|---|---|---|---|---|---|
| **Channel 14 (Shlomo Filber / NEXT DATA)** | 10 | **31.1** | 22.3 | **+8.8** | 10/10 |
| **i24 News (Direct Polls)** | 7 | **28.0** | 22.7 | **+5.3** | 7/7 |
| Kan 11 (Kantar) | 9 | 21.9 | 23.6 | −1.7 | 1/9 |
| Israel Hayom (Kantar) | 4 | 21.5 | 23.0 | −1.5 | 0/4 |
| HaHadashot 12 (Midgam) | 8 | 21.8 | 24.0 | −2.2 | 0/8 |
| Zman Yisrael (Tatika) | 7 | 21.7 | 23.7 | −2.0 | 0/7 |
| Walla (Lazar) | 3 | 21.3 | 24.7 | −3.3 | 0/3 |
| Channel 13 (Midgam/Madad/Stat-Net) | 7 | 20.4 | 23.1 | −2.7 | 0/7 |
| Channel 16 (Maagar Mochot) | 6 | 20.8 | 22.2 | −1.3 | 0/6 |
| Maariv (Lazar) | 8 | 20.0 | 24.1 | −4.1 | 0/8 |

Across those 52 mainstream polls **Yashar leads in 43, ties in 8 and trails in exactly one**
(Kan 11, 2026-08-09, 24–23). The nine mainstream houses' mean Likud figures span only **1.9
seats** (Kan 21.9 down to Maariv 20.0). The two Filber-lineage houses have Likud ahead in
**17 of 17**, mean Likud 29.8.

Fortnightly mainstream-only means: Aug-a −1.08 (n=13), Aug-b −2.59 (n=17), Sep-a −2.55
(n=20), Sep-b −3.00 (n=3). Filber-lineage over the same buckets: +7.75, +6.60, +7.33, +8.50.
September-only means: mainstream (n=22) Likud 20.36 / Yashar 23.32; Filber-lineage (n=8)
Likud 29.25 / Yashar 21.62.

**Three observations that decide how much weight the outliers get.**

1. **They are not independent.** Shlomo Filber *founded* Direct Polls in 2018, ran it through
   the 2022 cycle, and left in June 2025 to poll for Channel 14 independently. i24's pollster
   is still Direct Polls. Treating them as 2 of 12 houses double-counts one methodology.
2. **The conflict of interest is documented on the source itself.** Wikipedia's own polling
   page carries a standing note: "Shlomo Filber is affiliated with Likud and its leader
   Benjamin Netanyahu. Filber is implicated in Case 4000 on charges of breach of trust; thus
   it may be advisable to approach opinion polls edited by him with caution" (footnoted to
   Haaretz, 2022-06-14). Filber was Netanyahu's chief of staff 2001–03, ran Likud's 2015
   digital voter operation, and was a state witness in Netanyahu's trial.
3. **The number does not move.** Channel 14 has printed Likud 30–32 continuously since
   mid-August while every other house recorded Likud drifting 23 → 20. A headline figure
   that is flat while the field moves 3 seats is not measuring; it is asserting. Note also
   that the divergence is *entirely in Likud's own number* — Channel 14's Yashar (22.3) is
   only ~1.5 below the mainstream. A pollster finding ten extra Likud seats and no
   corresponding deficit anywhere on the centre-left is finding a different electorate.

Counterweight, and the reason the weight is 10% and not 0%: **Direct Polls has a real track
record**. Its final 2022 poll had Likud 31 (actual 32) and Yesh Atid 23 (actual 24) — as good
as anyone's. In 2022 Direct Polls and the mainstream *agreed*. The divergence is new.

Weighting used: 90% mainstream (even blend of the September mean and the 14–17 Sep batch:
Likud 20.0 / Yashar 23.2), 10% Filber-lineage (September mean: Likud 29.3 / Yashar 21.6)
→ **gap₀ = −2.11**. For reference, JPost's own five-poll average of 17 September (which
includes Channel 14 at equal weight) is Yashar 22.2 / Likud 21.2, gap −1.0; mainstream-only
is −3.20.

## Decomposition

Everything reduces to the sign of one integer, `G = Likud seats − Yashar seats`:

```
G = gap₀ (house-weighted polls today)  +  drift (5 weeks → result)  +  house-weighting error
G = −2.11                              +  N(+1.2, 3.2)              +  N(0, 1.3)
⇒ E[G] = −0.91,  sd[G] = 3.45
```

`P(G ≥ 1) = 33.9%`, `P(G ≤ −1) = 54.3%`, `P(G = 0) = 11.1%`. Scaled for `Other` (0.8%) and
conditioned on the question resolving at all: **Likud 38.1 / Yashar 61.0 / Other 0.9**.

**Provenance note.** The first draft used eyeballed poll means (mainstream 20.1 / 23.1,
Filber 29.9 / 21.9) and produced Likud 40.6 / Yashar 58.5, which was logged to the ledger and
then replaced, before any commit, when the exact parsed means (20.0 / 23.2 and 29.3 / 21.6)
moved gap₀ from −1.90 to −2.11. The draft ledger line was removed rather than left standing
as a spurious "v1" I never held; `AGENTS.md` rule 8 protects published history, and there was
none. Nothing else in the analysis changed.

## Search log

| Date | Query / source | Finding | Effect on forecast |
|---|---|---|---|
| 09-20 | Metaculus aggregations script, post 45670 | `cp_reveal_time` 2026-09-24T17:00Z, n=8 forecasters, **all three cohorts empty**. Options Likud/Yashar/Other; tie not addressed in the fine print; two comments (09-19, 09-20) flag the tie and expect ambiguous resolution | No Metaculus anchor. Tie risk becomes the #1 structural issue |
| 09-20 | Wikipedia polling wikitext, 2026 table, 168 rows parsed | Mainstream houses unanimous: Yashar ahead by 1.3–4.1 on average; Filber-lineage houses have Likud ahead by 5.3–8.8 | Defines the whole problem; sets gap₀ |
| 09-20 | Wikipedia polling pages 2015 / 2019A / 2019B / 2021 / 2022 | Gap-error table above. 2015 is the sole large miss; 2019A saw *both* big parties gain ~6 | Drift term +1.2 (not +2.0). Killed my initial instinct to apply a large pro-Likud correction |
| 09-20 | Wikipedia, April 2019 election results | **Likud 35 = Blue and White 35**, an exact seat tie; Likud won on votes by 14,489 | P(tie) 11.1% is not a modelling artefact — it has happened in the most recent comparable race |
| 09-20 | Polymarket Gamma API + CLOB price history (`raw/polymarket-*-2026-09-20.json`) | Yashar **0.61**, Likud **0.39**, Together 0.006, Shas/Democrats/Otzma ≈0.001. Event volume $313,940, liquidity $150,606, spread 2¢. Trend: Yashar 0.475 (08-30) → 0.505 (09-06) → **0.615 (09-13)** → 0.61 (09-20) | Primary external anchor in the absence of a CP. My 61.0/38.1 sits within 1 pp of it |
| 09-20 | Kalshi `KXISRAELKNESSET-26` API | Market exists but the API returns no bid/ask/volume for this session. Via prediction.com's aggregator: Yashar 50%, Likud 33%, minor options 1% each (sums to 0.86 — wide/stale book). Normalised ≈ Yashar 58 / Likud 38 | Second market, agrees with Polymarket. Ticker list still carries dead options (Yesh Atid, National Unity) — treat as thin |
| 09-20 | Manifold API search | **No market on this question.** Only "Will Netanyahu still be PM at end of 2026?" (0.62, $5.6k) | Nothing to discount |
| 09-20 | Wikipedia, Shlomo Filber | Netanyahu's chief of staff 2001–03; ran Likud's 2015 digital voter operation; DG of the Communications Ministry 2015–18; state witness in Case 4000; founded Direct Polls 2018; left June 2025 to poll for Channel 14 | Justifies the 10% weight cap on the two outlier houses *and* their non-independence |
| 09-20 | Wikipedia polling page, standing note | Explicit caution on Filber-edited polls, sourced to Haaretz 2022-06-14 | As above |
| 09-20 | JPost 908921 (09-17), 908437 (09-13), 908282, 908444 | JPost 5-poll average Yashar 22.2 / Likud 21.2; Maariv's pollster Menachem Lazar: "the struggles within the bloc, between Likud and Otzma Yehudit, Religious Zionism and Am Yisrael, are currently not benefiting Likud"; primaries gave Likud no bounce; undecideds will fall as election nears | Confirms Likud's losses are **intra-bloc**, i.e. recoverable — the strongest inside-view argument for the +1.2 drift |
| 09-20 | Times of Israel, 2026-09-18, "Netanyahu's anti-Arab campaign has found Gadi Eisenkot's Achilles' heel" | Netanyahu frames the race as Eisenkot-plus-Ra'am; Eisenkot forced to release 32 minutes of tape and to add anti-Ra'am coalition conditions; Liberman publicly demanded clarity; "the change bloc is losing ground, and shedding seats in several polls" | The 2015/2019A endgame playbook is already running, five weeks early. LR ≈ 1.25 for Likud |
| 09-20 | Times of Israel, 2026-09-14, "As parties lock in, Eisenkot plots path to power through heart of old Likud" | Yashar's 40-name slate is mostly newcomers (ex-officials, reservists, mayors) plus Kahana, Tropper, Farkash-Hacohen, Shaul Meridor; religious Zionists over-represented; explicitly hunting ex-Likud voters, not the left; open to Haredim conditional on conscription | Cuts *against* Likud: Yashar is competing on Likud's own turf, so Netanyahu's gevalt appeal has less room than in 2015 |
| 09-20 | LFI "Israel Elects 2026: Fragmentation on the right risks Bibi's chances" (~09-14) | Zionist opposition 58 vs Netanyahu bloc 50 on Maariv; **~8 seats / ~240,000 pro-Netanyahu votes at risk of falling below the 3.25% threshold** (Amcha Yisrael, RZP, Otzma) | The specific reservoir Netanyahu recaptures in the silent final 72 hours. Supports the drift term |
| 09-20 | ToI / JPost, surplus-vote agreements | Yashar–Democrats and Yisrael Beytenu–B'Yachad signed 2026-09-10; Likud with RZP–Zehut; Otzma with Amcha Yisrael (uncertain). Bader–Ofer mildly favours larger lists | Worth ±1 seat to each of Likud and Yashar; roughly cancels. Folded into the house/drift noise |
| 09-20 | Al Jazeera 2026-09-09 / IDI | 38 lists filed by the 2026-09-08 deadline; Likud list of 35 led by Netanyahu, Cohen, Ohana, Levin; CEC disqualification decisions due **2026-09-27** | Lists are locked — no more merger risk to the Likud/Yashar definitions |
| 09-20 | Wikipedia, 2026 Israeli legislative election | 27 Oct 2026; closed-list PR, single nationwide district, 3.25% threshold; 25th Knesset ran a full term, dissolved 2026-07-17; Likud absorbed New Hope in Aug 2025; Yashar founded 2025-09-16 by Eisenkot after leaving National Unity | Structural background |
| 09-20 | Haaretz election coverage 2026-09-08, 2026-09-17 | Ch12 (09-08): Yashar up, Eisenkot bloc 57–52; Ch13 (09-17): Netanyahu bloc 54–52 | Bloc-level noise; individual-party numbers already captured in the parse |
| 09-20 | ToI / Media Line / Axios, Netanyahu pardon | Herzog has deferred the pardon request, pushing for plea-deal mediation; Trump lobbied publicly; no decision as of 09-20 | Live wildcard with **ambiguous sign** — a pardon before 10-27 mobilises both electorates. Enters as variance, not as drift |
| 09-20 | Israel Elects "The Pollster Scorecard" | Paywalled; Figure 1 (2022 adjusted seat-error ranking) visible but rankings not. Tried without an archive fallback | **Dead end** — the single best source for house-quality weights was not obtainable. Flagged for the next update |

## Dead ends and ruled-out hypotheses

- **Sentinel Team, Mantic, Good Judgment Open, INFER**: no question on the Israeli
  largest-party outcome found. Nothing to compare against.
- **Manifold**: no market. (Per `AGENTS.md` it would have been discounted anyway.)
- **israel2026.co.il poll tracker**: page returned empty to the fetcher. Not used.
- **Israel Policy Forum "120 Project"**: page returned empty to the fetcher. Worth retrying —
  it is the closest thing to an independent expert seat projection.
- **"Israeli polls systematically underestimate Likud" as a licence for a large correction**:
  ruled out. It is a 2015 artefact plus a *bloc-level* phenomenon (small parties crossing or
  missing the threshold), not a largest-party-gap phenomenon. See the table above.
- **Merger/definition risk on the `Likud` and `Yashar` options**: ruled out. Lists closed
  2026-09-08; both run alone.
- **Election postponement**: needs 80 MKs. Priced at 1.5%, not modelled further.

## Open questions to chase next time

1. **Does Metaculus add a tie-breaker?** Highest-value single item. Watch the question's
   comment thread; `darkives` and `Theomachado` have already asked the admins.
2. **The Metaculus CP, Pro and gold cohorts reveal on 2026-09-24.** If Pro + gold agree with
   each other and sit >10 pp from 61.0/38.1, go looking for the missed fact before defending.
3. **Does the mainstream gap keep widening?** Aug-a −1.08 → Sep-b −3.00 is a slow drift
   against Likud that my +1.2 drift term assumes reverses.
4. **Channel 14's Likud number.** If Filber finally moves it off 31, that is the first
   evidence his series is measuring anything; if the mainstream moves toward him, my 10%
   weight is too low.
5. **Amcha Yisrael (Ofer Winter) and Hendel–Zelekha vs. the 3.25% threshold in the final
   polls (23 October).** Both below → the wasted-vote asymmetry, and the size of Netanyahu's
   recapture pool, is settled.
6. **Israel Elects pollster scorecard** — retry via archive.is or a subscription route; it is
   the right empirical basis for the house weights this forecast sets by judgement.

---

## 2026-10-09 — v3 research log (shared pass with #40966)

- **Metaculus**: browser/aggregation path blocked by Cloudflare. Used the parent's API JSON
  (`raw/metaculus-api-2026-10-09.json`): open, 111 forecasters, close 2026-10-27 06:00Z,
  scheduled resolve 2026-10-28. No fresh CP, Pro or gold.
- **Polls**: re-pulled the Wikipedia wikitext (`raw/wikipedia-polling-wikitext-2026-10-09.txt`)
  and parsed it with `parse_polls.py` (path swapped). Latest poll per mainstream house:
  Likud−Yashar −1, 0, −2, −2, 0, −2, −2 → mean −1.29 (was −3.38 as of 24 Sep). Ch14 +8, i24 +6.
  Bloc (mainstream): Netanyahu incl. Amcha 51.9, opposition Zionist 55.1, Arab 13.0. Amcha is
  below threshold in Kantar ×2 and Midgam.
- **Polymarket**: largest party Likud 52.5 / Yashar 48.5 (`raw/polymarket-largest-party-2026-10-09.json`).
  CLOB history shows a single jump on 2 Oct (Likud 0.445 → 0.58), the day of the High Court
  ruling and the 30 Sep–1 Oct poll batch. Likud-seats ladder median ~24.
- **News**: CEC bars Ra'am and the Joint List (23 Sep); High Court reverses (2 Oct); Abu
  Shehadeh withdraws. Five-leader opposition pact (26 Sep). Likud–RZP surplus deal (6 Oct).
  Avi Gil interview (8 Oct). Zamir warns an Iran strike could delay the election (8 Oct);
  Polymarket on-schedule 91.9%.
- **Model**: `raw/gap-model-2026-10-09.py` (closed-form normal). Central: Yashar 47.7.
- **Dead end**: the i24 article on Abbas's statehood speech was empty to the fetcher, and its
  date is unclear (probably early September). Not used.

---

## 2026-10-15 — v4 research log

**Order followed:** prior (v3) read first. Then the v3 tripwires checked one by one (polls for
#1–#3, postponement for #4, cohorts for #5). Then markets and general news.

- **Metaculus**: no aggregation calls this session (the parent got 403, a Cloudflare managed
  challenge). Used the parent's API JSON (`raw/metaculus-api-2026-10-15.json`): open, 119
  forecasters (111 on 10-09), 18 comments, close 2026-10-27 06:00Z, resolve 2026-10-28. I
  re-read the criteria and fine print. The tie rule is: PM of the *first government formed*;
  else the tied party with a minister; else, if both or neither tied party is in government
  or no government forms, most votes. No fresh CP, Pro or gold. The last cohort reading
  (2026-09-26: CP 57.0, Pros and gold 57.9 Yashar) is stale.
- **Polls**: Wikipedia wikitext via `index.php?action=raw`; the MediaWiki API returned 429
  (rate-limited). Saved as `raw/wikipedia-polling-wikitext-2026-10-15.txt` (278 rows, 271 on
  10-09) and parsed with `parse_polls.py`, path swapped, run from a scratch copy. Seven new
  rows: Ch13 14 Oct 18–20, Ch14 12 Oct 29–20, Midgam/Ch12 12 Oct 20–23, Kantar/Kan 11 Oct
  20–22, Maariv 7–8 Oct 20–21, Zman Yisrael 7–8 Oct 20–24, i24 7 Oct 26–20. Two polls are
  not yet in Wikipedia:
  - Walla/Lazar 13 Oct: Yashar 22, Likud 20, Amcha 2.8% (ice.co.il).
  - i24/Direct Polls 13 Oct: Likud 27, Yashar 21, Amcha 3.1% (i24NEWS).

  Latest poll per mainstream publisher: −2, −3, −2, −2, −1, −4, −1, −2 → mean **−2.125**
  (v3: −1.29 over 7). Filber pair +9 / +6. Mainstream Likud mean 19.9 (range 18–21). Blocs:
  Kan 53–50 Netanyahu (11 Oct), Ch13 51–50 Netanyahu (14 Oct), Midgam 54–49 Eisenkot
  (12 Oct), Walla 54–49 Eisenkot (13 Oct). PM suitability: Ch13 Eisenkot 45–38, Kan 43–38.
- **Amcha Yisrael (tripwire 3)**: below threshold in Midgam (1.8%), Walla (2.8%), Kantar/IH
  (2.9%), Ch14 (2.9%) and i24 (3.1%). Four seats in Ch13, Kan, Maariv and Zman Yisrael. Ben
  Gvir ruled out a surplus deal with Winter (ToI live blog, 13 Oct). Surplus-agreement
  deadline is 16 Oct; Shas–UTJ signed 11 Oct.
- **Postponement (tripwire 4)**: no bill. ToI blog (Pomerantz, 14 Oct) is speculation only.
  Polymarket "as scheduled" 0.9215 (0.919 on 10-09).
- **Poll blackout**: Wikipedia's polling page cites the Elections (Propaganda Methods) Law
  §16E(h): no polls may be published from the end of Friday before election day until 22:00
  on election day. So the last polls come Thu 22 Oct (TV) and Fri 23 Oct (papers). Next
  reviews: 10-20 (T−7d), 10-24 (all poll evidence in), 10-26 (T−1d to close).
- **Polymarket** (gamma + CLOB, all 2026-10-15):
  - Largest party: Yashar 0.62 (0.61/0.63, last 0.64), Likud 0.385 (0.37/0.40), Together
    0.0045. Event volume $679,024 (10-09: $619,103); 1-week volume $62,783.
  - CLOB history: Likud ~0.50–0.515 through 12 Oct, then 0.495 → 0.39 on 13 Oct 07:00–19:00
    UTC, 0.415 → 0.295 at 22:00 UTC on 14 Oct (the Urich report), and 0.375 by 04:00 UTC on
    15 Oct (`raw/polymarket-largest-party-clob-history-2026-10-15.json`).
  - Likud-seats ladder: <20 19.2, 20–24 42.5, 25–29 25.5, 30–34 10.5, 35+ 1.5 ($516k).
  - Yashar-seats ladder: thin, $19k.
  - Next PM: Netanyahu 0.275 (0.355 on 10-09), Eisenkot 0.468 (0.436), Bennett 0.155 (0.095);
    $46.5M volume.
  - Other markets: Amcha vote share <3.25% 0.675; Israel–Iran ceasefire holds through 10-21
    0.905 and through 10-31 0.845; Trump endorses Likud 0.335; Likud loses seats 0.936.
  - Snapshots in `raw/polymarket-*-2026-10-15.json`.
- **Kalshi** `KXISRAELKNESSET-26` (first call 429, retry 200): Yashar 0.56/0.59 (last 0.60),
  Likud 0.32/0.37 (last 0.33). Thin. `raw/kalshi-israel-knesset-2026-10-15.json`.
- **Manifold**: "Will the Likud win…" 30.2% (no change since 10-09; $3.8k). PM market:
  Eisenkot 46.9, Netanyahu 32.0, Bennett 14.9. Discounted. `raw/manifold-israel-2026-10-15.json`.
- **News, with disconfirming evidence sought**:
  - Urich–Qatar report (Ch12, 14 Oct) [pro-Yashar, small].
  - Netanyahu–Trump discussion of an Iran strike before the elections (Ch12/Axios, 13 Oct; PMO
    and White House deny) [pro-Likud tail].
  - Netanyahu's hour-long Channel 14 interview (13 Oct).
  - Jewish Insider (11 Oct): best week of the campaign for the Netanyahu *bloc* [pro-Likud on
    blocs, not on Likud's own seats].
  - JTA (13 Oct): blocs ~52–53 each; Rosner warns new parties fade.
  - Rally precedent: Channel 12 had Likud +4 during the June 2025 Iran war (ToI, via search
    summary). A search summary also mentioned a 27 → 31 Zman Yisrael jump after a war
    beginning 28 Feb 2026. Not opened and not used.
- **Model**: `raw/gap-model-2026-10-15.py`, output in `raw/gap-model-output-2026-10-15.txt`.
  Central: Yashar 58.66, Likud 40.74, Other 0.6. E[G] −0.56, sd 2.64, P(tie) 14.7%.
- **Chart**: `charts/gap-shift-2026-10-15.png` (per-house gap, v3 vs v4; P(Yashar) by version
  vs Polymarket).
- **Inconsistency noted**: Polymarket's Likud-seats ladder (median ~23) and Yashar-seats ladder
  (median ~22–23) imply a near coin flip, while its winner market says 62/38. One of them is
  mispriced. This is the main reason I did not add a market row.
- **Dead ends**: MediaWiki API 429 (used `action=raw` instead). ToI live-blog pages are
  ~450k characters and the fetcher truncates them; I read only the 0–200k range of the
  13 Oct page. The Haaretz 15 Oct "Lighthouse" exclusive is paywalled and was not used.

## 2026-10-15 (afternoon) — fresh Metaculus cohorts, no new version

The aggregation script worked again at ~13:15 UTC (blocked at 05:00 UTC). Cached as
`raw/metaculus-2026-10-15.json`. Reading as of 2026-10-15 07:31 UTC, which is after the 14 Oct
Channel 13 poll and the Urich report:

| Cohort | Likud | Yashar | Other | n |
|---|---|---|---|---|
| CP | 44.0 | 55.0 | 1.0 | 117 |
| Pros | 44.1 | 54.8 | 1.0 | 10 |
| Gold | 44.3 | 54.7 | 1.0 | 34 |
| v4 (this repo) | 40.7 | 58.7 | 0.6 | |
| Polymarket (mid, 05:xx UTC) | 38.5 | 61.75 | — | |

Decision: **no new version.** Pros and gold agree with each other, but they are only ~4pp from v4
on Yashar, inside v4's IQR [51.7, 65.7] and below the protocol's 5pp community-move trigger. The
v3 tripwire (both ≥ 8pp from 48.5) is not fired: they are +6.3 / +6.2. v4 sits between them and
Polymarket. Polymarket breaks ties on votes, not on the next-PM rule, so the two are not strictly
comparable. Watch the gap at the 2026-10-20 review: if the final mainstream polls do not widen
further and the cohorts stay at ~55, shade toward them.
