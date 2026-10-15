# Which party will win the most seats in the 2026 Israeli election?

| | |
|---|---|
| **Source** | Metaculus #45670 — https://www.metaculus.com/questions/45670/which-party-will-win-the-most-seats-in-the-2026-israeli-election/ |
| **Type** | multiple_choice (Likud / Yashar / Other) |
| **Opened / Closes / Resolves** | ~2026-09-17 / 2026-10-27 / scheduled 2026-10-28 (annulled if no result before 2027-01-01) |
| **Status** | open |
| **Current forecast** | **Yashar 58.7%, Likud 40.7%, Other 0.6%** — IQR on Yashar (leading option) [51.7%, 65.7%] ≡ Likud [33.7%, 47.7%] (v4, 2026-10-15) |
| **Community (as of 2026-10-15 07:31 UTC, fetched 13:15 UTC after v4)** | Yashar / Likud / Other: CP 55.0 / 44.0 / 1.0 (n=117) · Pros 54.8 / 44.1 / 1.0 (n=10) · gold 54.7 / 44.3 / 1.0 (n=34); 119 forecasters. ~4pp below v4, inside its IQR: no new version, see research.md. Polymarket Yashar 61.75% / Likud 38.5% (mid, 2026-10-15) |
| **Next review** | 2026-10-20 (T−7d); then 2026-10-24, after the last pre-blackout polls of 22–23 Oct |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v4 — Update — 2026-10-15

**Mode: Update** (incremental). Six days since v3, 12 days to the 27 Oct vote. I checked the
re-analysis triggers. On a like-for-like tie rule, Polymarket is 3.8pp from me, which is under
the 10pp trigger. Six of the 18 days left at v3 have passed: exactly one third, not more. v2
and v3 moved in opposite directions. The parent session diffed the 2026-10-15 API JSON
against 2026-10-09: criteria, fine print, options and dates are unchanged. Every model input
is still re-derived from today's data (`raw/gap-model-2026-10-15.py`, output in
`raw/gap-model-output-2026-10-15.txt`). Fresh Metaculus aggregations are **unavailable today**:
every aggregation call returned 403 (Cloudflare managed challenge). The bot-key API JSON shows
the question open with **119 forecasters** (111 on 10-09), closing 2026-10-27 06:00 UTC [1].

### Revision table

| Driver | Direction | Effect on P(Yashar) |
|---|---|---|
| **Prior (v3, 2026-10-09)** | — | **48.5%**, IQR [41.0%, 56.0%] (Likud 50.9, IQR [43.4%, 58.4%]; Other 0.6) |
| **v3's +0.8 overlay is retired.** v3 posted 0.8 above its own model (47.7) for two reasons. First, the Avi Gil interview (8 Oct) was not yet in any poll; six mainstream polls fielded after it are now in [2]. Second, Amcha Yisrael's (Ofer Winter's party) sub-threshold readings risked being counted twice; it is below threshold in 3 of 8 latest mainstream polls, against 3 of 7 then. Posted number returns to the model | ↓ | **−0.8** |
| **The mainstream gap widened again, from −1.29 to −2.13 seats.** Latest poll per publisher: Channel 13 18–20 (14 Oct; was 20–20), Midgam/Ch12 20–23 (12 Oct; was 21–23), Kantar/Kan 20–22 (11 Oct; was 21–23), Lazar/Walla 20–22 (13 Oct; new), Lazar/Maariv 20–21 (7–8 Oct; was 19–21), Tatika/Zman Yisrael **20–24** (7–8 Oct; was 21–21), Kantar/Israel Hayom 21–22 (7–8 Oct), Maagar Mochot 19–21 (29 Sep) [2][3][4][5][7][17]. **Both of v3's dead heats (Channel 13, Zman Yisrael) are Yashar leads again.** The Filber houses did not move: Channel 14 29–20 (+9, 12 Oct), i24/Direct Polls 27–21 (+6, 13 Oct) [6][7]. gap₀ moves from −0.46 to **−1.16**. This row uses v3's drift, variance and tie split | ↑ | **+9.7** |
| **Shorter horizon:** 12 days instead of 18, so drift sd falls from 2.5 to 2.3. Remaining drift stays at +0.6 seats to Likud. Half of the early-October move toward Likud (+2.1) has reversed (−0.8), so the mainstream gap is ~1.1 seats above its 20 Sep level (−3.2). That is about v1's whole expected 5-week drift (+1.2). What is left is the error between final polls and the result: +0.4 seats without 2015, shrunk from ~+2 with it | ↑ | **+0.5** |
| **Tie split 0.50 → 0.55.** P(exact tie) is now 14.7%. A tie resolves to the party of the PM of the first government formed, else the tied party with a minister, else the tied party with more votes [1]. On Polymarket's next-PM market ($46.5M volume), Netanyahu fell from 35.5% to 27.5% between 9 and 15 Oct. Eisenkot rose 43.6 → 46.8 and Bennett 9.5 → 15.5 [8]. A Bennett-led government that includes Yashar also resolves Yashar. Conditioning on a tie lifts Netanyahu to ~0.33. The ~0.2 of no-government or unity outcomes fall back to votes (~50/50). That gives 0.57, which I shade to 0.55 | ↑ | **+0.7** |
| **Iran strike before the vote** (speculative mixture term). Channel 12 and Axios (13 Oct) report that Netanyahu and Trump discussed resuming strikes before the Israeli and US elections; the PMO and the White House deny it [9]. Polymarket has the Israel–Iran ceasefire holding through 21 Oct at 90.5% and through 31 Oct at 84.5% [8], so ~12% for a strike before 27 Oct. In that branch I assume a ~+1.7-seat rally for Likud. In June 2025, a Channel 12 poll during the war had Likud up 4 (22 → 26) [19]. I shade that for war fatigue and because a strike would be read as electioneering. E[G] +0.2 | ↓ | **−2.9** |
| **Urich–Qatar report, not yet polled.** Channel 12 (14 Oct): PM aide Jonatan Urich met Qatari minister Ali al-Thawadi twice in Europe in July 2024. Bennett called it "the gravest case of treason in Israeli history" [10]. Polymarket's Likud price fell 0.415 → 0.295 within the hour, then recovered to 0.375 [8]. Qatargate has been public since 2025 and scandal effects on Likud's vote have been small since 2019, so E[G] −0.2. It cancels the Iran row, which is a coincidence of two judgement calls, not a plug | ↑ | **+2.9** |
| **New forecast (v4)** | | **58.7%**, IQR [51.7%, 65.7%] (Likud 40.7, IQR [33.7%, 47.7%]; Other 0.6) |

The rows are rounded and sum to 58.6. The model's unrounded output is 58.66. Other stays at
0.6 (Polymarket Together 0.45%).

**Market move, and why I do not follow it all the way.** Polymarket's largest-party market
moved from Yashar 48.5 / Likud 52.5 to **61.75 / 38.5** (mid; Yashar 0.61/0.63, last 0.64)
[8]. The CLOB history is flat through 12 Oct, then moves in two steps:

- **13 Oct, 07:00–19:00 UTC:** Yashar 0.485 → 0.575. This came after the 12 Oct Midgam 20–23 poll, on the day of the Walla poll and the Iran-strike report.
- **14 Oct, ~22:00 UTC:** the Urich report.

Event volume rose by only about $60k ($619k → $679k). The market moved 13pp; my model moves
10pp on the polls alone. I add no market row, because the move rests on the same polls plus
the Urich story, which has its own row. There is also a reason not to herd: **Polymarket's own
seat markets do not agree with its winner market.** The Likud-seats market ($516k) has its
median near 23 (20–24: 42.5%, 25–29: 25.5%). The thin Yashar-seats market ($19k) has its median
near 22–23. Together they imply a near coin flip, while the winner market says 62/38.

### Tripwire check (v3 list)

| # | Tripwire | Status | Evidence |
|---|---|---|---|
| 1 | By 10-23: mainstream-house average (Channel 14 and i24 excluded) has Likud ahead by ≥ 1 seat → −8pp | **Not fired; moved away** | −1.29 → −2.13. No mainstream house has Likud ahead; Maariv and Israel Hayom are the closest at −1 [2] |
| 2 | By 10-23: mainstream gap back to ≥ 3 seats for Yashar → +10pp | **Not fired; half-way** | −2.13, which is 0.84 of the 1.71 seats needed. The model charges the actual move (+9.7) rather than waiting for the threshold. Not due until 10-23 |
| 3 | By 10-23: Amcha Yisrael below 3.25% in a majority of final-week polls while the gap holds → −3pp | **Not due** (final week = 17–23 Oct); not a majority today | Below threshold in 3 of 8 latest mainstream polls: Midgam 1.8% (12 Oct), Walla 2.8% (13 Oct), Kantar/Israel Hayom 2.9% (7–8 Oct). Four seats in Channel 13, Kan, Maariv and Zman Yisrael. Also below in Channel 14 (2.9%) and i24 (3.1%) [2][4][6]. Ben Gvir ruled out a surplus-vote deal with Winter (13 Oct) [16]. Polymarket puts Amcha below 3.25% at 67.5% [8] |
| 4 | By 10-20: election formally postponed → re-analyse | **Not fired** | No postponement bill has been tabled. Netanyahu says he hopes the vote proceeds but warned of enemy attacks [11]. Polymarket "as scheduled" 92.15% (91.9% on 10-09) [8] |
| 5 | When cohort data returns: Pros and gold both ≥ 8pp from Yashar 48.5 in the same direction | **Cannot check** | 403 on 2026-10-15. The last reading (2026-09-26: Pros and gold 57.9) predates the October swing and is stale |

### What resolves YES

Re-read on 2026-10-15 against the API JSON [1]; unchanged from v3. The question resolves to
the party with **more seats than any other** in the 27 Oct 2026 Knesset election.

- A plurality for a third list resolves `Other`. No results before 2027-01-01 means **annulled**.
- **Exact seat tie:**
  1. the party of the PM of the *first government formed* after the election;
  2. else, if the PM is from another party, the tied party with at least one other minister;
  3. else (both tied parties in government, neither, or **no government formed**), the tied party with more official votes.
- "The party" is the list as filed. Likud runs as Likud (New Hope merged into it in 2025) and Yashar runs alone. Surplus-vote agreements (Yashar–Democrats, Likud–RZP, Shas–UTJ) do not merge lists.
- Options: `Likud`, `Yashar`, `Other`.
- Polymarket and Kalshi break ties on votes, not on the next PM, so their prices are not exactly comparable to this question.
- Coalition talks can run past January, so a tie could leave the question open for a long time.

### Outside view

Unchanged from v1.

### Inside view

```
G = gap₀ (−1.16)  +  remaining drift N(+0.6, 2.3)  +  house error N(0, 1.3)
    [Iran-strike tail +0.2 and Urich report −0.2 on E[G]: they cancel]
E[G] = −0.56 seats,  sd[G] = 2.64 seats
P(Yashar outright) 50.9% · P(tie) 14.7% · P(Likud outright) 34.4%
→ Yashar 58.7, Likud 40.7, Other 0.6
```

What moved in early October was mostly **Yashar**, which dipped to 20–21 seats. Mainstream
Likud has sat at 18–21 for six weeks (mean 19.9 across the latest poll per house). Yashar is
now back at 20–24.

**The bloc picture and the largest-party picture are moving in opposite directions.** Kan has
the Netanyahu bloc ahead 53–50 (11 Oct) and Channel 13 has it ahead 51–50 (14 Oct).
Jewish Insider's ex-outlier average for the first week of October was 52–53 [3][5][12]. Those
bloc gains come from Otzma, Shas and Amcha Yisrael, not from Likud. Votes that stay with
Likud's satellites help Netanyahu form a government without making Likud the largest list.
Late recapture of those votes is the mechanism the drift term prices. The polls do not show it
yet: Likud is flat while its satellites hold.

Head-to-head PM suitability also favours Eisenkot: 45–38 in Channel 13 (14 Oct) and 43–38 in
Kan (11 Oct) [5][3].

### Evidence

New since v3 (detail in the revision table and `research.md`):

- **Seven new mainstream polls.** The mean gap is −2.13 (8 publishers), and none has Likud ahead [2][3][4][5][7][17].
- **Filber houses steady.** Channel 14 +9 (29–20) and i24 +6 (27–21). Both lowered Likud over the fortnight (Channel 14 32 → 29, i24 28 → 27), but their gaps to Yashar moved by at most 2 seats [6][7].
- **Blocs moved toward Netanyahu**, while Likud's own seat count did not [3][12][15].
- **Urich–Qatar report** (Channel 12, 14 Oct) [10]. Not yet polled.
- **Iran-strike report** (Channel 12 and Axios, 13 Oct). The PMO and White House deny it. Trump says no US strikes before the 3 Nov midterms [9][11].
- **Surplus-vote agreements** are due 16 Oct. Shas–UTJ signed on 11 Oct, and Ben Gvir refuses one with Winter [2][16].
- **Poll blackout:** under the election-silence law, no poll may be published from the end of Friday 23 Oct until the polls close at 22:00 on 27 Oct [2]. The last poll evidence is the Thursday 22 Oct TV polls and the Friday 23 Oct newspaper polls, so the review after them is 2026-10-24.

![Gap by pollster, v3 vs v4, and the forecast path against Polymarket](charts/gap-shift-2026-10-15.png)

### Scenarios

| # | Scenario | Weight | Resolves |
|---|---|---|---|
| A | Yashar outright largest | 0.506 | Yashar |
| B | Exact tie; next PM's government or the votes fallback goes to Yashar | 0.080 | Yashar |
| C | Exact tie; Netanyahu forms the government, or the votes fallback goes to Likud | 0.066 | Likud |
| D | Likud outright largest | 0.342 | Likud |
| E | A third list is largest (Together) | 0.006 | Other |

### Sensitivity

| Assumption | If instead | P(Yashar) becomes |
|---|---|---|
| Remaining drift +0.6 | 0.0 (no late consolidation) | 67.0% |
| same | +1.2 (v1's full drift still to come) | 49.9% |
| Filber-house weight 10% | 0% | 71.7% |
| same | 5% | 65.4% |
| same | 15% | 51.6% |
| same | 25% | 37.6% |
| Lazar counted per publisher (Walla + Maariv) | Lazar counted once (Walla only) | 60.7% |
| Tie split 0.55 | 0.45 | 57.2% |
| Drift sd 2.3 | 3.2 (v1) | 56.6% |
| Iran tail and Urich both on | Iran tail on, Urich off | 55.8% |

The house weight is still the most load-bearing judgement. The winner market at 62 is roughly
where a 7–8% Filber weight lands. Polymarket's Likud-seats ladder has its median near 23,
against a mainstream average of 19.9. That implies Likud beating its mainstream polls by ~3
seats, which in this model is close to a coin flip. The two markets disagree with each other,
and I stay at 10%.

### Other forecasters (2026-10-15)

| Source | Yashar | Likud | Other | As of | Note |
|---|---|---|---|---|---|
| **This (v4)** | **58.7** | **40.7** | **0.6** | 2026-10-15 | |
| Metaculus CP | 57.0 | 42.0 | 1.0 | **2026-09-26 (stale)** | 119 forecasters now [1]. **Fresh value unavailable 2026-10-15 (Cloudflare 403)** |
| Metaculus Pros | 57.9 | 40.9 | 1.2 | **2026-09-26 (stale)** | fresh value unavailable 2026-10-15 |
| Metaculus gold | 57.9 | 40.9 | 1.2 | **2026-09-26 (stale)** | fresh value unavailable 2026-10-15 |
| Polymarket, largest party | 61.75 (0.61/0.63, last 0.64) | 38.5 (0.37/0.40) | 0.45 (Together) | 2026-10-15 | event volume $679k (+$60k since 10-09); ties broken on votes [8] |
| Polymarket, Likud seats | — | <20: 19.2 · 20–24: 42.5 · 25–29: 25.5 · 30–34: 10.5 · 35+: 1.5 | — | 2026-10-15 | $516k; median ~23 seats (10-09: 25+ at 43%) [8] |
| Polymarket, Yashar seats | <20: 17.1 · 20–21: 21 · 22–23: 21.5 · 24–25: 16.5 · 26–27: 15.5 · 28–29: 4.4 · 30+: 6.8 | — | — | 2026-10-15 | $19k, thin [8] |
| Polymarket, next PM | Eisenkot 46.8 · Bennett 15.5 | Netanyahu 27.5 | — | 2026-10-15 | $46.5M; Netanyahu 35.5 on 10-09 [8] |
| Kalshi `KXISRAELKNESSET-26` | 0.56/0.59 (last 0.60) | 0.32/0.37 (last 0.33) | — | 2026-10-15 | thin (Yashar ~10k contracts); two-way ≈ 62/38 [13] |
| Manifold, "Will the Likud win the next Israeli election" | — | 30.2 | — | 2026-10-15 | no trades since 10-09; ambiguous wording (could mean forming the government); play money, discounted [14] |
| Manifold, PM after the next election | Eisenkot 46.9 | Netanyahu 32.0 | — | 2026-10-15 | play money; agrees with Polymarket's PM market [14] |

**Cohort disagreement**: cannot be assessed; there is no fresh cohort data. The stale 26 Sep
CP (57.0) happens to sit close to v4. **Me vs markets**: 3.0pp below Polymarket on Yashar
(3.8pp like-for-like on the votes tie-break), and about the same against Kalshi. Three reasons:

- I give the Urich report less weight than traders did.
- I add an Iran-strike tail.
- The market's own Likud-seats ladder argues against its winner price.

### What would change my mind (tripwires)

- [ ] **By 2026-10-23 (last pre-blackout polls): the mainstream average gap is −0.5 or narrower** (latest poll per publisher, Channel 14 and i24 excluded; from −2.13 today) → **down 10pp** on P(Yashar).
- [ ] **By 2026-10-23: the mainstream average gap is −3.5 or wider** → **up 7pp**.
- [ ] **By 2026-10-23: Amcha Yisrael is below 3.25% in a majority of the 17–23 Oct mainstream polls *and* mainstream Likud averages ≥ 21 seats** (19.9 today) → **down 3pp**. This is satellite recapture finally showing up in Likud's own number.
- [ ] **By 2026-10-26: Israel or Iran strikes the other's territory** (Polymarket's ceasefire definition) → **down ~5pp** on P(Yashar), and re-check the annulment risk.
- [ ] **By 2026-10-26: the Knesset passes a postponement** (80 MKs) → **re-analyse**. If there is no result before 2027-01-01, the question is annulled.
- [ ] **Any time before close (2026-10-27 06:00 UTC): cohort data returns with Pros and gold both ≥ 8pp from Yashar 58.7 in the same direction** → re-derive before defending.

### Sources

1. Metaculus question 45670, official API post JSON (bot key; aggregations hidden): criteria, fine print, options, 119 forecasters, close 2026-10-27T06:00Z. Cohort values carried forward from `raw/metaculus-2026-09-26.json`. https://www.metaculus.com/questions/45670/ (accessed 2026-10-15; `raw/metaculus-api-2026-10-15.json`)
2. Opinion polling for the 2026 Israeli legislative election — Wikipedia (raw wikitext, `action=raw`; includes the election-silence note citing the Elections (Propaganda Methods) Law §16E) — https://en.wikipedia.org/wiki/Opinion_polling_for_the_2026_Israeli_legislative_election (accessed 2026-10-15; `raw/wikipedia-polling-wikitext-2026-10-15.txt`, 278 rows; parsed with `raw/parse_polls.py` pointed at the new file)
3. "Poll: Eisenkot Bloc Holds at 54 Seats as Hard-Line Ex-General's Party Falls Short" (Channel 12/Midgam, 12 Oct: Yashar 23, Likud 20, Amcha 1.8%) — Haaretz, 2026-10-13 — https://www.haaretz.com/israel-news/elections/2026-10-13/ty-article/poll-eisenkot-bloc-holds-at-54-seats-hard-line-ex-generals-party-falls-short/000001a1-346a-d36f-a9fd-75ead18b0000 (accessed 2026-10-15). Kan 11 Oct poll via Kan News, https://www.kan.org.il/content/kan-news/politic/1108256/ (cited in [2]; PM suitability 43–38 via search summary of Anadolu/Kan)
4. "סקר מנדטים חדש: איזנקוט מוביל, הנדל וזליכה מפתיעים - וינטר בחוץ" (Walla/Lazar, 13 Oct: Yashar 22, Likud 20, Amcha 2.8%) — ice.co.il — https://www.ice.co.il/research/news/article/1133482 (accessed 2026-10-15)
5. Channel 13 poll, 14 Oct (Yashar 20, Likud 18; Netanyahu bloc 51, Eisenkot bloc 50; suitability Eisenkot 45, Netanyahu 38) — 13tv — https://13tv.co.il/item/news/politics/politics/survey-905396904/?pid=106628 (accessed 2026-10-15)
6. "Two weeks before elections: Ofer Winter does not pass the electoral threshold" (i24NEWS/Direct Polls, 13 Oct: Likud 27, Yashar 21, Amcha 3.1%) — i24NEWS — https://www.i24news.tv/en/news/israel-election-s-2026/artc-two-weeks-before-elections-ofer-winter-does-not-pass-the-electoral-threshold-i24news-poll (accessed 2026-10-15)
7. "Two polls: Hendel and Zelekha cross electoral threshold; Ofer Winter is out" (Channel 14 29–20 and Channel 12 20–23, 12 Oct) — Israel National News — https://www.israelnationalnews.com/news/434503 (accessed 2026-10-15)
8. Polymarket gamma API and CLOB price history: `israeli-legislative-election-winner`, `israel-election-likud-of-seats`, `israel-election-yashar-of-seats`, `who-will-be-the-next-prime-minister-of-israel-after-the-next-election`, `will-israel-election-happen-as-scheduled-…`, `israel-election-amcha-yisrael-vote-share`, `israel-x-iran-ceasefire-continues-through…`, Trump-endorsement and bloc markets — https://polymarket.com/event/israeli-legislative-election-winner (accessed 2026-10-15; `raw/polymarket-largest-party-2026-10-15.json`, `raw/polymarket-largest-party-clob-history-2026-10-15.json`, `raw/polymarket-israel-election-likud-of-seats-2026-10-15.json`, `raw/polymarket-israel-election-yashar-of-seats-2026-10-15.json`, `raw/polymarket-israel-related-markets-2026-10-15.json`)
9. "Netanyahu reportedly pressed Trump to renew Iran fighting before Israeli and US elections" — The Times of Israel, 2026-10-13 — https://www.timesofisrael.com/netanyahu-reportedly-pressed-trump-to-renew-iran-fighting-before-israeli-and-us-elections/ ; Axios, "Inside Trump, Netanyahu's dilemma: Strike Iran before elections or wait" — https://axios.com/2026/10/13/netanyahu-trump-iran-war-elections (accessed 2026-10-15, via search summary)
10. "PM's aide Urich met senior Qatari official in Europe twice in 2024 -- report" — The Times of Israel, 2026-10-14 — https://www.timesofisrael.com/pms-aide-urich-met-senior-qatari-official-in-europe-twice-in-2024-report/ (accessed 2026-10-15)
11. Sherwin Pomerantz, "13 Days to Elections: What is the Risk of Postponement?" — Times of Israel Blogs, 2026-10-14 — https://blogs.timesofisrael.com/13-days-to-elections-what-is-the-risk-of-postponement/ (accessed 2026-10-15). Opinion piece; used only for the absence of a bill and the quoted statements
12. Lahav Harkov, "Netanyahu bloc gains on Gadi Eisenkot's opposition in latest Israeli polls" — Jewish Insider, 2026-10-11 — https://jewishinsider.com/2026/10/netanyahu-rising-in-weekend-polls/ (accessed 2026-10-15)
13. Kalshi API, `KXISRAELKNESSET-26` — https://kalshi.com/markets/kxisraelknesset/israeli-knesset-election/kxisraelknesset-26 (accessed 2026-10-15; `raw/kalshi-israel-knesset-2026-10-15.json`)
14. Manifold Markets API: "Will the Likud win the next Israeli election", "Who will be the Israeli PM after the next election?" — https://manifold.markets/Shump/will-the-likud-win-the-next-israeli , https://manifold.markets/ShakedKoplewitz/who-will-be-the-israeli-pm-after-th (accessed 2026-10-15; `raw/manifold-israel-2026-10-15.json`)
15. "Checkmate? Netanyahu faces a daunting playing field ahead of Oct. 27" — JTA, 2026-10-13 — https://www.jta.org/2026/10/13/israel/checkmate-netanyahu-faces-a-daunting-playing-field-ahead-of-oct-27 (accessed 2026-10-15)
16. The Times of Israel live blog, 2026-10-13 (Ben Gvir rules out a surplus deal with Winter; surplus-agreement deadline 16 Oct; Eisenkot on the polls) — https://www.timesofisrael.com/liveblog-october-13-2026/ (accessed 2026-10-15)
17. "ToI poll: Anti-Netanyahu bloc regains lead but both camps short of majority 19 days ahead of vote" (Zman Yisrael, 7–8 Oct: Yashar 24, Likud 20) — The Times of Israel — https://www.timesofisrael.com/toi-poll-anti-netanyahu-bloc-regains-lead-but-both-camps-fall-short-19-days-ahead-of-vote/ (accessed 2026-10-15, via search summary)
18. Carried forward from v3 [9]–[15] and still relied on for the outside view and house weights: JPost 2026-09-17 (article-908921); ToI 2026-09-18 (anti-Arab campaign); Wikipedia 2015 polling; Wikipedia April 2019 election; Wikipedia Shlomo Filber; CEC candidate lists 2026-09-03; ToI 2026-09-10 surplus-vote deals (all accessed 2026-09-20)
19. "Poll: Netanyahu's Likud enjoys boost amid Iran war, but bloc he leads is no closer to majority" (Channel 12, June 2025: Likud 26, up 4 in three weeks) — The Times of Israel — https://www.timesofisrael.com/poll-netanyahus-likud-enjoys-boost-amid-iran-war-but-not-enough-to-clinch-election-win/ (accessed 2026-10-15, via search summary)

**Question**: [Which party will win the most seats in the 2026 Israeli election?](https://www.metaculus.com/questions/45670/)
**Date**: 2026-10-15
**Forecast**: Yashar 58.7%, Likud 40.7%, Other 0.6% — IQR on Yashar (leading option) [51.7%, 65.7%] ≡ Likud [33.7%, 47.7%]
**Thesis**: Early October's narrowing did not hold. Across eight mainstream pollsters, the latest Likud–Yashar gap widened again from −1.3 to −2.1 seats, and both of v3's dead heats (Channel 13, Zman Yisrael) are Yashar leads again, while Channel 14 and i24 held at +9 and +6 [2][5][6]. With 10% weight on those two houses and +0.6 seats of late drift to Likud, Yashar is largest outright in ~51% of outcomes. It also takes 55% of a 15% exact-tie branch, because the next-PM tie rule tilts its way now that Polymarket's PM market has Netanyahu down to 27.5% [8]. Polymarket's winner market (Yashar 62) and Kalshi sit ~3pp higher. The unpolled Urich–Qatar story and a ~12% Iran-strike tail roughly cancel. Fresh Metaculus cohorts were unavailable (403).

---

## v3 — Update — 2026-10-09

**Mode: Update** (incremental). Thirteen days since v2, 18 days to the 27 Oct vote. A de-novo
rebuild is not needed: the gap model is unchanged in structure, and the 13pp move in
Polymarket has a nameable cause, which is the polls below. The model is re-run with today's
inputs (`raw/gap-model-2026-10-09.py`). Fresh Metaculus aggregations are **not available
today**: the browser path is blocked by Cloudflare for this container. The official API post
JSON (bot key) confirms the question is open, has 111 forecasters, has options
`Likud / Yashar / Other`, and closes 2026-10-27 06:00 UTC [1].

### Revision table

| Driver | Direction | Effect on P(Yashar) |
|---|---|---|
| **Prior (v2, 2026-09-26)** | — | **61.5%**, IQR [55.5%, 67.5%] (Likud 37.6, Other 0.9) |
| **The mainstream gap closed from −3.4 to −1.3 seats.** Latest poll per house: Kantar/Israel Hayom 21–22 (7–8 Oct), Channel 13 **20–20** (7 Oct), Midgam/Ch12 21–23 (5 Oct), Kantar/Kan 21–23 (4 Oct), Zman Yisrael **21–21** (30 Sep–1 Oct), Maariv 19–21 (30 Sep–1 Oct), Maagar Mochot 19–21 (29 Sep) [2][3][4]. The right-leaning houses held steady: Channel 14 +8 (31–23, 7 Oct) and i24/Direct Polls +6 (28–22, 1 Oct). With v1's 10% weight on those two, gap₀ moves from about −2.1 to **−0.46**. At v2's drift and variance, this alone takes Yashar to 41.9 | ↓ | **−19.6** |
| **Shorter horizon.** About +2.1 of the expected +1.2-seat late drift toward Likud has already shown up in the past fortnight, so I keep only half of it (+0.6) for the last 18 days. Drift sd falls from 3.2 to 2.5. Other trimmed 0.9 → 0.6, in line with Polymarket's 0.4% on B'Yachad | ↑ | **+6.5** |
| **Tie split 0.55 → 0.50.** P(exact tie) is now **14.1%**. The tie-breaker is "party of the next PM". The sister question's model (40966 v3) puts P(Eisenkot takes the first mandate) at 0.49, so the tie branch is now set equal to that number | ↓ | **−0.7** |
| **Unmodelled, small.** Avi Gil's Channel 12 interview on 8 Oct alleges that Netanyahu's office tampered with October-7 phone records. Only the Kantar 7–8 Oct poll may partly capture it [5]. Amcha Yisrael is now below threshold in 3 of the 7 latest mainstream polls. Its voters are Likud's main recapture pool, and the Kantar and Midgam polls already show that effect, so the drift term would double-count it. Net: a small lean back toward the polls | ↑ | **+0.8** |
| **New forecast (v3)** | | **48.5%**, IQR [41.0%, 56.0%] (Likud 50.9, IQR [43.4%, 58.4%]; Other 0.6) |

Polymarket moved from Yashar 58.5 / Likud 41.5 to 48.5 / 52.5, mostly in one jump on 2 Oct
(Likud 0.445 → 0.58 intraday). That was the day the High Court reinstated Ra'am and the Joint
List and the 30 Sep–1 Oct poll batch came out [3][6]. Polymarket's move is the same direction
and similar size as mine. I do **not** add a separate market row, because the market is
reacting to the same polls.

### Tripwire check (v2 list)

| # | Tripwire | Status | Evidence |
|---|---|---|---|
| 1 | By 10-13: mainstream average has Likud level with or ahead of Yashar → −12pp | **Not fired, two-thirds of the way** | Average −1.3. Two of seven houses are exactly level (Ch13 20–20, Zman Yisrael 21–21), and none has Likud ahead [2]. The model charges the move at its actual size (−19.6 before the horizon offset) rather than waiting for the threshold |
| 2 | By 10-13: mainstream gap ≥ 4.5 to Yashar → +6pp | Not fired (moved the other way) | −3.4 → −1.3 |
| 3 | By 10-23: Amcha Yisrael below 3.25% in a majority of final-week polls → −4pp | Not due; trending toward firing | Below in Kantar ×2 (2.9% on 7–8 Oct) and Midgam. 4–5 seats in Ch13, Maariv, Zman Yisrael and Maagar Mochot [2]. Polymarket gives Amcha a 53.5% chance of winning a seat [6] |
| 4 | By 10-20: Herzog pardon or AG plea deal | Not fired | No movement reported since Herzog deferred the pardon in favour of plea-deal mediation |
| 5 | By 10-20: Pros and gold both move ≥ 8pp from my Yashar number | **Cannot check** | Cohort data unavailable on 2026-10-09 (Cloudflare block). My own number moved 13pp, so the comparison will need to be redone once data returns |

### What resolves YES

Unchanged from v2. Ties go to the party of the next PM, failing that to the sole tied party in
government, failing that to the most votes. Options are `Likud`, `Yashar`, `Other`. The API
schedule now shows close 2026-10-27 06:00 UTC and scheduled resolve 2026-10-28 [1].

### Outside view

Unchanged from v1.

### Inside view

The structure is unchanged: everything still reduces to the sign of `G = Likud − Yashar`.

```
G = gap₀ (−0.46)  +  remaining drift N(+0.6, 2.5)  +  house error N(0, 1.3)
E[G] = +0.14 seats,  sd[G] = 2.82 seats
P(Yashar outright) 41.6% · P(tie) 14.1% · P(Likud outright) 44.4%
→ Yashar 47.7, Likud 51.7, Other 0.6 (model); posted 48.5 / 50.9 / 0.6
```

On the expected value the race is now a coin flip with a slight lean to Likud. The scale of
uncertainty is still set by the final 72 hours, which no poll covers.

### Evidence

New since v2 (detail in the revision table and `research.md`):

- Mainstream polls: the Likud–Yashar gap closed from −3.4 to −1.3 seats; Channel 13 (7 Oct) and Zman Yisrael (30 Sep–1 Oct) show exact ties, none shows Likud ahead [2][3][4][5].
- Right-leaning houses unchanged: Channel 14 +8 Likud (7 Oct), i24/Direct Polls +6 (1 Oct) [2].
- High Court let Ra'am, the Joint List and Cassif run (2 Oct) [7].
- Amcha Yisrael below the 3.25% threshold in 3 of the 7 latest mainstream polls [2].
- Avi Gil's Channel 12 interview (8 Oct) alleging tampering with October-7 phone records; effect not yet polled [5].
- Polymarket moved from Yashar 58.5 / Likud 41.5 to 48.5 / 52.5, mostly on 2 Oct [6].

### Scenarios

| # | Scenario | Weight | Resolves |
|---|---|---|---|
| A | Yashar outright largest | 0.416 | Yashar |
| B | Exact tie, non-Netanyahu PM | 0.070 | Yashar |
| C | Exact tie, Netanyahu stays PM (or Likud forms) | 0.070 | Likud |
| D | Likud outright largest | 0.438 | Likud |
| E | A third list is largest (B'Yachad) | 0.006 | Other |

### Sensitivity

| Assumption | If instead | P(Yashar) becomes |
|---|---|---|
| Remaining drift +0.6 | 0.0 (no late consolidation) | 56.0% |
| same | +1.2 (full v1 drift still to come) | 39.5% |
| Filber-house weight 10% | 0% (mainstream only) | 59.1% |
| same | 25% | 31.2% |

The house weight is still the most load-bearing judgement. Polymarket's Likud-seats market
(median ~24 seats, P(Likud ≥ 25) = 43%) [6] implies traders put far more weight on Channel 14
and i24 than I do, or expect a large late swing. If either turns out right, I am too high on
Yashar.

### Other forecasters (2026-10-09)

| Source | Yashar | Likud | Other | As of | Note |
|---|---|---|---|---|---|
| **This (v3)** | **48.5** | **50.9** | **0.6** | 2026-10-09 | |
| Metaculus CP | 57.0 | 42.0 | 1.0 | **2026-09-26 (stale)** | n=80 then; 111 forecasters now [1]. **Fresh CP unavailable 2026-10-09 (Cloudflare block)** |
| Metaculus Pros | 57.9 | 40.9 | 1.2 | **2026-09-26 (stale)** | fresh value unavailable 2026-10-09 (Cloudflare block) |
| Metaculus gold | 57.9 | 40.9 | 1.2 | **2026-09-26 (stale)** | fresh value unavailable 2026-10-09 (Cloudflare block) |
| Polymarket, largest party | 48.5 (0.48/0.49) | 52.5 (0.52/0.53) | 0.4 (Together) | 2026-10-09 | $619k event volume (was $401k). Ties broken on votes [6] |
| Polymarket, Likud seats | — | <20: 15.6 · 20–24: 35 · 25–29: 27.5 · 30–34: 13.5 · 35+: 2 | — | 2026-10-09 | $436k [6] |
| Manifold, "Will the Likud win the next Israeli election" | — | 30.2 | — | 2026-10-09 | Play money, ambiguous wording (could mean forming the government). Discounted |

**Cohort disagreement**: cannot be assessed today. **Me vs Polymarket**: 1.6pp less
Likud than the market (50.9 vs 52.5), and level on Yashar (48.5). That is closer than at v2,
and the gap comes from the same polls.

### What would change my mind (tripwires)

- [ ] **By 2026-10-23 (last polls before the blackout): the mainstream-house average has Likud ahead by ≥ 1 seat** → **down 8pp** on P(Yashar).
- [ ] **By 2026-10-23: the mainstream gap returns to ≥ 3 seats in Yashar's favour** → **up 10pp**.
- [ ] **By 2026-10-23: Amcha Yisrael below 3.25% in a majority of final-week polls** while the Likud–Yashar gap holds → **down 3pp** (late recapture beyond what is already in the polls).
- [ ] **By 2026-10-20: the election is formally postponed** (a Knesset vote needs 80 MKs; Polymarket's on-schedule price is 91.9%) → re-analyse (date and annulment risk).
- [ ] **When cohort data returns: Metaculus Pros and gold both sit ≥ 8pp from 48.5 in the same direction** → re-derive before defending.

### Sources

1. Metaculus question 45670, official API post JSON (bot key; aggregations hidden) — https://www.metaculus.com/questions/45670/ (accessed 2026-10-09; `raw/metaculus-api-2026-10-09.json`). Cohort values carried forward from `raw/metaculus-2026-09-26.json`
2. Opinion polling for the 2026 Israeli legislative election — Wikipedia (raw wikitext) — https://en.wikipedia.org/wiki/Opinion_polling_for_the_2026_Israeli_legislative_election (accessed 2026-10-09; `raw/wikipedia-polling-wikitext-2026-10-09.txt`, parsed with `raw/parse_polls.py` pointed at the new file)
3. "Opposition Bloc's Boycott of Arab Parties Hands Netanyahu's Bloc Edge, New Poll Shows" — Haaretz, 2026-10-01 (Ch13: Likud 19, Yashar 21) — https://www.haaretz.com/israel-news/elections/2026-10-01/ty-article/new-poll-boycott-of-arab-parties-hands-netanyahus-bloc-edge-over-opponents/000001a0-f628-da3f-a7fa-f7ed60d40000 (accessed 2026-10-09)
4. Kan poll, 28 Sep: Yashar 23, Likud 21, blocs tied at 52 — The Jerusalem Post — https://www.jpost.com/israel-election-2026/article-909918 (accessed 2026-10-09)
5. "Oct. 8: After Avi Gil interview, Eisenkot calls for criminal probe against Netanyahu" — The Times of Israel live blog (also the Ch13 8 Oct poll: Likud 20, Yashar 20; and the Zamir Iran/postponement report) — https://www.timesofisrael.com/liveblog-october-08-2026/ (accessed 2026-10-09)
6. Polymarket gamma API and CLOB price history: `israeli-legislative-election-winner`, `israel-election-likud-of-seats`, `which-parties-will-win-a-seat-in-the-2026-knesset-elections`, `will-israel-election-happen-as-scheduled-…` — https://polymarket.com/event/israeli-legislative-election-winner (accessed 2026-10-09; `raw/polymarket-largest-party-2026-10-09.json`, `raw/polymarket-israel-election-likud-of-seats-2026-10-09.json`)
7. "High Court lets Arab parties run" (7–2 on Cassif, unanimous on Ra'am and the Joint List; Abu Shehadeh withdraws) — The Times of Israel live blog, 2026-10-02 — https://www.timesofisrael.com/liveblog-october-02-2026/ (accessed 2026-10-09)
8. Manifold Markets API, "Will the Likud win the next Israeli election" — https://manifold.markets (accessed 2026-10-09)
9. "Gadi Eisenkot still leads in polls, but Benjamin Netanyahu shortens distance" — The Jerusalem Post, 2026-09-17 — https://www.jpost.com/israel-election-2026/article-908921 (accessed 2026-09-20) — carried forward from v2 [6], still relied on for the outside view
10. "Netanyahu's anti-Arab campaign has found Gadi Eisenkot's Achilles' heel" — The Times of Israel, 2026-09-18 — https://www.timesofisrael.com/netanyahus-anti-arab-campaign-has-found-gadi-eisenkots-achilles-heel/ (accessed 2026-09-20) — carried forward from v2 [7], still relied on
11. Opinion polling for the 2015 Israeli legislative election — Wikipedia — https://en.wikipedia.org/wiki/Opinion_polling_for_the_2015_Israeli_legislative_election (accessed 2026-09-20) — carried forward from v2 [8], still relied on
12. April 2019 Israeli legislative election — Wikipedia — https://en.wikipedia.org/wiki/April_2019_Israeli_legislative_election (accessed 2026-09-20) — carried forward from v2 [9], still relied on
13. Shlomo Filber — Wikipedia — https://en.wikipedia.org/wiki/Shlomo_Filber (accessed 2026-09-20) — carried forward from v2 [10], still relied on
14. Lists of Candidates — Central Elections Committee, 2026-09-03 — https://www.gov.il/en/pages/candidates-lists-26 (accessed 2026-09-20) — carried forward from v2 [11], still relied on
15. "Main opposition factions ink surplus-vote deals in bid to maximize Knesset representation" — The Times of Israel, 2026-09-10 — https://www.timesofisrael.com/main-opposition-factions-ink-surplus-vote-deals-in-bid-to-maximize-knesset-representation/ (accessed 2026-09-20) — carried forward from v2 [12], still relied on

**Date**: 2026-10-09
**Forecast**: Yashar 48.5%, Likud 50.9%, Other 0.6% — IQR on Likud (leading option) [43.4%, 58.4%] ≡ Yashar [41.0%, 56.0%]
**Thesis**: The mainstream pollsters' Likud–Yashar gap has closed from −3.4 to −1.3 seats in two weeks. Channel 13 and Zman Yisrael now show a dead heat, and Channel 14 and i24 are unchanged at +8 and +6 [2][5]. That makes the race a coin flip with a slight lean to Likud. Polymarket flipped the same way, to 52.5 Likud [6]. Half the expected late drift toward Likud has already happened, and a 14% exact-tie branch resolves by who becomes PM (~50/50), which keeps Yashar near 48.5 rather than lower. Fresh Metaculus cohort data was unavailable today.

---

## v2 — Update — 2026-09-26

**Mode: Update** (incremental). Six days since v1, 16% of the time to the 27 Oct election.
Polymarket and all three Metaculus cohorts are within 4.5pp of me. This is the first revision.
One structural change fired as a v1 tripwire: Metaculus published a tie-breaker. It is handled
here as a re-mapping of v1's tie branch rather than as a new model. The operator also asked for
the full option vector in the ledger's new `distribution` field. This version supplies it.

### Revision table

| Driver | Direction | Effect on P(Yashar) |
|---|---|---|
| **Prior (v1, 2026-09-20)** | — | **61.0%**, IQR [55.0%, 67.0%] (Likud 38.1, Other 0.9), conditional on the question resolving |
| **Tie-breaker published** (admin johnnycaffeine, 2026-09-21): an exact seat tie goes to **the party of the next prime minister**; failing that, to the sole tied party with at least one other minister in the government; failing that, to the party with the most votes [1]. v1's 11.1% tie branch now resolves rather than annuls. In a tie world the Netanyahu bloc still sits well short of 61 in the mainstream polls (45–49 seats) [2]. The next PM would then come from the opposition: Eisenkot, or Bennett with Yashar in government, both of which resolve Yashar. That holds unless Likud builds a coalition anyway. I put **P(Yashar \| tie) ≈ 0.55**, a little below Yashar's share elsewhere, because a tie means Likud has out-performed. Re-normalising v1's branches: Yashar 60.3, Likud 38.9, Other 0.8 | ↓ | **−0.7** |
| **The mainstream-house gap widened slightly, −3.0 → −3.4 seats.** Latest poll per house, 22–24 Sep: Midgam 20–23, Channel 13 18–22, Maariv 18–22, Zman Yisrael 21–23, Maagar Mochot 19–23. Kantar (20–22, 17 Sep) has not polled since [2]. The right-leaning houses eased too: Channel 14 +11 → +10 (32–22), i24 +6 → +5 (27–22). Neither the level-pegging tripwire nor the ≥ 4-seat tripwire fired. The move is smaller than one house's sampling noise, so it gets partial weight | ↑ | **+1.5** |
| **Six fewer days for a structural shift.** v1's drift term is concentrated in the unmeasured final 72 hours and is unchanged. The pre-blackout variance shrinks slightly, which helps the side that is ahead | ↑ | **+0.2** |
| **Cohorts and market sit a little lower.** Metaculus CP Yashar 57.0 / Likud 42.0; Pros and gold both 57.9 / 40.9 [1]. Polymarket Yashar 61 → 59, Likud 39 → 40.5, on ~$87k of fresh volume [3]. Polymarket tie-breaks on votes, not on the next PM. Pros and gold are 3.1pp from me, well inside the 10pp re-analysis band. I weight them, but they carry no reason I have not already priced | ↓ | **−0.5** |
| **New forecast (v2)** | | **61.5%**, IQR [55.5%, 67.5%] (Likud 37.6, Other 0.9) |

The vector is now **unconditional except for the ~1.5% "no result before 2027-01-01" branch**,
since ties no longer annul.

### Tripwire check (v1 list)

| # | Tripwire | Status | Evidence |
|---|---|---|---|
| 1 | Metaculus reveal (09-24): Pro and gold both ≥ 10pp from Likud 38.1 in the same direction → re-analyse | **Not fired** | Pros and gold both at Likud 40.9 (+2.8). CP 42.0 (n=80) [1] |
| 2 | Admins publish a tie-breaker, or rule a tie ambiguous (by 09-30) | **Fired** (2026-09-21) | Next PM's party → sole tied party in government → most votes [1]. Priced in row 2 |
| 3 | Mainstream average has Likud level with or ahead of Yashar (by 10-13) → −12pp | Not fired | Gap −3.4 [2] |
| 4 | Mainstream gap ≥ 4 seats to Yashar (by 10-13) → +8pp | Not fired | Gap −3.4 [2] |
| 5 | Amcha Yisrael below 3.25% in a majority of final-week polls (by 10-23) → −4pp | Not due | — |
| 6 | Herzog pardons Netanyahu or the AG announces a plea deal (by 10-20) → re-analyse | Not fired | On the eve of Yom Kippur Herzog pardoned the soldier **Elor Azaria**, not Netanyahu. Netanyahu's own request is still deferred in favour of plea-deal mediation [4][5] |

### What resolves YES

Unchanged from v1, except the tie rule (above). Options in Metaculus order: `Likud`, `Yashar`,
`Other`.

### Outside view

Unchanged from v1.

### Inside view

Unchanged from v1.

### Scenarios

Unchanged from v1. Scenario C (exact tie, 0.111) now resolves ~55/45 Yashar/Likud instead of
annulling. The rest of the branch weights stand.

### Evidence

Unchanged from v1.

### Other forecasters (2026-09-26)

| Source | Yashar | Likud | Other | As of | Note |
|---|---|---|---|---|---|
| **This (v2)** | **61.5** | **37.6** | **0.9** | 2026-09-26 | |
| Metaculus CP | 57.0 | 42.0 | 1.0 | 2026-09-26 19:39 | n=80 [1] |
| Metaculus Pros | 57.9 | 40.9 | 1.2 | 2026-09-26 | n=9 |
| Metaculus gold | 57.9 | 40.9 | 1.2 | 2026-09-26 | n=27 |
| Polymarket | 59.0 (0.58/0.60) | 40.5 (0.40/0.41) | 0.5 (Together) | 2026-09-26 | $401k volume (was $314k); tie-break on votes [3] |

**Cohort disagreement**: none; Pros and gold are identical. **Disagreement with me: 3–4.5pp**,
Likud-ward. The Metaculus comment thread's most detailed forecast (Theomachado, 21 Sep:
Yashar 55 / Likud 44) splits the polls into two camps. It weights the right-leaning houses more
than my 10% Filber-house weight does. That is exactly v1's second load-bearing sensitivity, and
it is where the gap comes from.

### Sensitivity

Unchanged from v1 for the two load-bearing assumptions: the drift term (+0.0 → Yashar ~74%,
+2.4 → Yashar ~46%) and the Filber-house weight (0% → Yashar ~73%, 25% → Yashar ~40%). v1's
last row (tie → annulled vs. a popular-vote tie-break) is now moot. The published tie-break
(the next PM's party) is priced in the revision table and moves the vector by less than 1pp.

### What would change my mind (tripwires)

- [ ] **By 2026-10-13 — mainstream-house average (Channel 14 and i24 excluded) has Likud level with or ahead of Yashar** → **down 12pp on P(Yashar)**.
- [ ] **By 2026-10-13 — mainstream-house average gap reaches ≥ 4.5 seats to Yashar** (from −3.4 on 2026-09-24) → **up 6pp**.
- [ ] **By 2026-10-23 — Amcha Yisrael (Ofer Winter) below 3.25% in a majority of the final week's polls** → **down 4pp**.
- [ ] **By 2026-10-20 — Herzog grants Netanyahu a pardon, or the Attorney-General announces a plea deal** → re-analyse (direction either).
- [ ] **By 2026-10-20 — Metaculus Pros and gold both move ≥ 8pp from my Yashar number in the same direction** → re-derive before defending.

### Sources

1. Metaculus question 45670, three-cohort aggregations and comments (admin tie-breaker comment by johnnycaffeine, 2026-09-21) — https://www.metaculus.com/questions/45670/ (accessed 2026-09-26; `raw/metaculus-2026-09-26.json`)
2. Opinion polling for the 2026 Israeli legislative election — Wikipedia (raw wikitext) — https://en.wikipedia.org/wiki/Opinion_polling_for_the_2026_Israeli_legislative_election (accessed 2026-09-26; `raw/wikipedia-polling-wikitext-2026-09-26.txt`, parsed with v1's `raw/parse_polls.py` pointed at the new file)
3. Polymarket, "Israeli Legislative Election Winner" (gamma API) — https://polymarket.com/event/israeli-legislative-election-winner (accessed 2026-09-26; `raw/polymarket-largest-party-2026-09-26.json`)
4. Herzog's Yom Kippur pardon of soldier crystallizes choice for Israeli voters — The Forward — https://forward.com/opinion/851495/herzogs-yom-kippur-pardon-of-soldier-crystallizes-eisenkot-netanyahu-choice (accessed 2026-09-26, via search summary)
5. Rebuffing Netanyahu's pardon request, at least for now, Herzog calls for new plea deal talks — The Times of Israel — https://www.timesofisrael.com/herzog-pushes-for-new-plea-deal-talks-says-he-wont-consider-netanyahu-pardon-request-yet/ (accessed 2026-09-26, via search summary)
6. "Gadi Eisenkot still leads in polls, but Benjamin Netanyahu shortens distance" —
   The Jerusalem Post, 2026-09-17 — https://www.jpost.com/israel-election-2026/article-908921
   (accessed 2026-09-20) — carried forward from v1 [3], still relied on
7. "Netanyahu's anti-Arab campaign has found Gadi Eisenkot's Achilles' heel" —
   The Times of Israel, 2026-09-18 —
   https://www.timesofisrael.com/netanyahus-anti-arab-campaign-has-found-gadi-eisenkots-achilles-heel/
   (accessed 2026-09-20) — carried forward from v1 [5], still relied on
8. Opinion polling for the 2015 Israeli legislative election — Wikipedia —
   https://en.wikipedia.org/wiki/Opinion_polling_for_the_2015_Israeli_legislative_election
   (accessed 2026-09-20) — carried forward from v1 [7], still relied on
9. April 2019 Israeli legislative election — Wikipedia —
   https://en.wikipedia.org/wiki/April_2019_Israeli_legislative_election (accessed 2026-09-20) — carried forward from v1 [9], still relied on
10. Shlomo Filber — Wikipedia — https://en.wikipedia.org/wiki/Shlomo_Filber
    (accessed 2026-09-20) — carried forward from v1 [11], still relied on
11. Lists of Candidates — Central Elections Committee, 2026-09-03 —
    https://www.gov.il/en/pages/candidates-lists-26 (accessed 2026-09-20) — carried forward from v1 [15], still relied on
12. "Main opposition factions ink surplus-vote deals in bid to maximize Knesset
    representation" — The Times of Israel, 2026-09-10 —
    https://www.timesofisrael.com/main-opposition-factions-ink-surplus-vote-deals-in-bid-to-maximize-knesset-representation/
    (accessed 2026-09-20) — carried forward from v1 [19], still relied on

**Date**: 2026-09-26
**Forecast**: Yashar 61.5%, Likud 37.6%, Other 0.9% — IQR on Yashar [55.5%, 67.5%]
**Thesis**: The six mainstream pollsters still put Eisenkot's Yashar 3.4 seats ahead of Likud, slightly wider than at v1 [2]. The Channel 14/i24 gap to them narrowed a little. Metaculus's new tie-breaker, the next PM's party, turns v1's 11% annulment branch into a ~55/45 Yashar split, costing 0.7pp [1]. Metaculus Pros and gold (57.9) and Polymarket (59) sit 2.5–4.5pp Likud-ward of me, because they give the right-leaning houses more weight. The final 72 hours before the vote are unpolled, and that remains the main risk.

---

## v1 — Initial forecast — 2026-09-20

### What resolves YES

Resolves as the party holding **more Knesset seats than any other** after the 2026 Israeli
legislative election of **27 October 2026**, as certified by the Central Elections Committee
(CEC). Options are `Likud`, `Yashar` and `Other`; a plurality for any third list resolves
`Other`; if no result exists before **2027-01-01** the question is **annulled**. Seat
allocation is Bader–Ofer (D'Hondt with surplus-vote pooling) over a single nationwide
district with a **3.25% threshold**; official results are gazetted ~8 days after polling
(2022: voted 1 Nov, certified 9 Nov), so a normal count resolves comfortably inside the
window. Published polling is barred from the end of Friday **2026-10-23** — the final ~72
hours are unmeasured.

**The edge case that matters is an exact tie, and the fine print does not cover it.** The
criteria demand a party with "more seats than any other"; the fine print addresses only a
third-party plurality and postponement. Question commenters raised this on 2026-09-19 and
2026-09-20 and expect ambiguous resolution absent an admin ruling. This is not a theoretical
worry: **April 2019 ended Likud 35 – Blue and White 35**, decided on votes (1,140,370 vs
1,125,881) [9]. I put **P(exact seat tie) = 11.1%**. Polymarket's parallel market explicitly
tie-breaks on valid votes, then alphabetically [10]; Metaculus does not. The vector below is
therefore **conditional on the question resolving at all** — I estimate a **12.4%** chance it
is annulled (11.1% tie + 1.5% no-result-by-2027, less overlap).

Secondary edge case, now moot: Metaculus does not say how a *joint list* containing Likud or
Yashar would map to the options. Lists closed 2026-09-08 with 38 filed; both parties run
alone [14][15]. Likud's list already absorbs New Hope (merged August 2025) [16].

### Outside view

| Reference class | n | Window | Raw rate | Kept |
|---|---|---|---|---|
| Israeli elections where **Likud was the largest single list** | 12 | 1996–2022 | **6/12 outright, 1 tie** | crude anchor ≈ 50% |
| **New centrist party led by an ex-IDF Chief of General Staff** beats Likud | 5 | 2019A–2022 | **1/5** largest, 1/5 tie | the Gantz analogue, but Gantz-era Likud polled 30–36, not 20 |
| **Drift in the Likud-minus-top-rival seat gap, 5 weeks out → result** | 5 | 2015–2022 | +4.5, +4.5, −1.5, +1.7, ≈+1.0 → **mean +2.0, sd 2.5** | **load-bearing** |
| Exact tie for largest party | 25 | 1949–2022 | 1/25 unconditional, **1/6 since 2015** | supports the 11% tie figure in a race this close |

The load-bearing class deserves its full table, because the folk version of it is wrong:

| Election | Rival | Gap 5 wk out | Gap, final polls | Gap, result | Δ final→result | Δ 5wk→result |
|---|---|---|---|---|---|---|
| 2015 | Zionist Union | +1.5 | −3.5 | **+6** (30–24) | **+9.5** | +4.5 |
| 2019 Apr | Blue and White | −4.5 | −0.8 | **0** (35–35) | +0.8 | +4.5 |
| 2019 Sep | Blue and White | +0.5 | −0.6 | **−1** (32–33) | −0.4 | −1.5 |
| 2021 | Yesh Atid | +11.3 | +12.5 | **+13** (30–17) | +0.5 | +1.7 |
| 2022 | Yesh Atid | — | +6.5 | **+8** (32–24) | +0.75 | ≈+1.0 |

**"Israeli polls underestimate Likud" is, on this quantity, almost entirely a 2015 artefact.**
Drop 2015 and the mean final-poll gap error is **+0.4 seats** — noise. What the record does
support is different and weaker: in two of four close races the gap moved 4–5 seats toward
Likud over the final five weeks, and in April 2019 *both* leading parties gained ~6 seats by
consuming their own satellites, leaving the gap almost unchanged. The mechanism is **late
consolidation of large lists**, which is symmetric, not a Likud-specific measurement error.
I therefore shrink the sample mean of +2.0 by ~40% to a **drift of +1.2 seats**, and I
explicitly reject the +4 to +8 correction that the popular version of this claim licenses.

### Inside view

Everything reduces to the sign of one integer, `G = Likud seats − Yashar seats`.

```
G  =  gap₀ (house-weighted polls today)  +  drift (5 weeks → result)  +  house-weighting error
   =  −2.11                              +  N(+1.2, 3.2)              +  N(0, 1.3)
⇒  E[G] = −0.91 seats,   sd[G] = 3.45 seats
```

`raw/gap-model-2026-09-20.py`, 2,000,000 draws with integer seat rounding:
`P(G ≥ 1) = 33.9%`, `P(G = 0) = 11.1%`, `P(G ≤ −1) = 54.3%`, `P(Other) = 0.8%`.

**Setting gap₀ is the entire forecasting problem.** The 2026 polling table [2] parses to 250
rows, 70 of them with usable Likud *and* Yashar figures since 2026-08-01, and they split into
two irreconcilable camps (`raw/parse_polls.py`, `raw/poll_analysis.py`):

| Publisher | n | Likud | Yashar | gap | Likud ahead in |
|---|---|---|---|---|---|
| **Channel 14 (Shlomo Filber / NEXT DATA)** | 10 | **31.1** | 22.3 | **+8.8** | 10/10 |
| **i24 News (Direct Polls)** | 7 | **28.0** | 22.7 | **+5.3** | 7/7 |
| Kan 11 (Kantar) | 9 | 21.9 | 23.6 | −1.7 | 1/9 |
| HaHadashot 12 (Midgam) | 8 | 21.8 | 24.0 | −2.2 | 0/8 |
| Zman Yisrael (Tatika) | 7 | 21.7 | 23.7 | −2.0 | 0/7 |
| Israel Hayom (Kantar) | 4 | 21.5 | 23.0 | −1.5 | 0/4 |
| Walla (Lazar) | 3 | 21.3 | 24.7 | −3.3 | 0/3 |
| Channel 16 (Maagar Mochot) | 6 | 20.8 | 22.2 | −1.3 | 0/6 |
| Channel 13 (Midgam/Madad/Stat-Net) | 7 | 20.4 | 23.1 | −2.7 | 0/7 |
| Maariv (Lazar) | 8 | 20.0 | 24.1 | −4.1 | 0/8 |

![Pollster house effects and the modelled seat gap](charts/house-effects-and-gap.png)

The nine mainstream houses' mean Likud figures span just **1.9 seats** (20.0 to 21.9), and
across their 52 polls since 1 August **Yashar leads in 43, ties in 8, and trails in exactly
one** (Kan 11, 2026-08-09, 24–23). The two Filber-lineage houses have Likud ahead in **17 of
17**. Three facts fix their weight at **10%**:

1. **They are one house, not two.** Shlomo Filber *founded* Direct Polls in 2018, ran it
   through the 2022 cycle, and left in June 2025 to poll for Channel 14 independently; i24's
   pollster is still Direct Polls [11]. Counting them as 2 of 12 double-counts a methodology.
2. **The conflict of interest is documented on the data source itself.** Wikipedia's polling
   page carries a standing note that Filber "is affiliated with Likud and its leader Benjamin
   Netanyahu … implicated in Case 4000 on charges of breach of trust; thus it may be
   advisable to approach opinion polls edited by him with caution" [2][12]. Filber was
   Netanyahu's chief of staff 2001–03, ran Likud's 2015 digital voter operation, and was a
   state witness in Netanyahu's trial [11].
3. **The number does not move.** Channel 14 has printed Likud 30–32 continuously since
   mid-August while every other house recorded Likud drifting 23 → 20. And the divergence sits
   *entirely* in Likud's own figure — Channel 14's Yashar (22.3) is only ~1.5 below the
   mainstream. A pollster finding ten extra Likud seats with no matching deficit anywhere on
   the centre-left is surveying a different electorate, not correcting a sampling bias.

Why 10% and not 0%: **Direct Polls has a genuine track record.** Its final 2022 poll had
Likud 31 (actual 32) and Yesh Atid 23 (actual 24) — as good as anyone's [8]. In 2022 Direct
Polls and the mainstream *agreed*; the divergence is new, which is weak evidence that
something changed in the electorate rather than in the pollster, and I price that at 10%.

So gap₀ = 0.90 × (20.0 − 23.2) + 0.10 × (29.3 − 21.6) = **−2.11**, where the mainstream
figures blend the September mean (n=22: Likud 20.36, Yashar 23.32) with the 14–17 September
batch (n=6: 19.67, 23.00), and the Filber figures are their September mean (n=8). For
calibration: mainstream-only is −3.20; JPost's own five-poll average of 17 September, which
takes Channel 14 at equal weight, is −1.0 (Yashar 22.2, Likud 21.2) [3].

**The causal story behind the +1.2 drift.** Likud's decline is *intra-bloc*, and therefore
recoverable. Maariv's pollster Menachem Lazar, 2026-09-13: "the struggles within the bloc,
between Likud and Otzma Yehudit, Religious Zionism and Am Yisrael, are currently not
benefiting Likud" [4]. LFI's tracker counts **~8 seats, ~240,000 pro-Netanyahu votes, at risk
of falling below the 3.25% threshold** across Amcha Yisrael, RZP and Otzma [13]. That is the
reservoir Netanyahu drained in 2015 (Bayit Yehudi 12 → 8, Yachad below threshold, Likud
+8) and in April 2019 (Zehut and the New Right wiped out, Likud +6.5) — and he has already
started, five weeks early, with the anti-Ra'am campaign against Eisenkot [5].

**The causal story against it.** Eisenkot is not running at Likud from the left. Yashar's
40-name slate is ex-officials, reservists and mayors, religious Zionists over-represented,
and it is hunting *ex-Likud* voters explicitly [6]. In 2015 the gevalt appeal worked because
the alternative was Herzog–Livni; a soft-right voter who has moved to Eisenkot is far harder
to scare home. Likud's own opposition-pool (Together 9–16, Democrats 8–10, Yisrael Beiteinu
5–9, Reservists–NEP 0–4) is *larger* than Netanyahu's, so if late consolidation is the
mechanism, Yashar benefits from it too — exactly as Blue and White did in April 2019.

Net: +1.2 seats, sd 3.2 — a genuine but modest tilt, not the 2015 replay.

### Evidence

**What updated me most, and in which direction.**

- **The unanimity of the mainstream houses** — 43 of 52 polls with Yashar ahead, 8 ties, 1
  with Likud ahead; nine houses whose mean Likud figures span 1.9 seats [2]. Against a
  single-house outlier this is close to decisive on gap₀. LR ≈ **2.5** toward Yashar
  relative to an uninformed 50/50.
- **The 2015-is-the-whole-story finding** [7][8] and the April-2019 symmetric-surge finding
  [9]. This was the biggest single correction to my own prior: I came in expecting to apply a
  +3 to +5 pro-Likud correction and the data does not support it. LR ≈ **0.45** on "Likud
  beats its polls by a lot", i.e. toward Yashar.
- **Netanyahu's anti-Ra'am campaign is landing** [5]. Times of Israel, 2026-09-18: Eisenkot
  was forced to release 32 minutes of tape to rebut a Bedouin council head's claim, then to
  add anti-Ra'am coalition conditions; Liberman publicly demanded clarity; "the change bloc is
  losing ground, and shedding seats in several polls". The 2015 endgame playbook is running
  early and Eisenkot is on the defensive. LR ≈ **1.25** toward Likud.
- **Likud's losses are intra-bloc, and ~8 seats of right-wing votes sit below the threshold**
  [4][13]. LR ≈ **1.2** toward Likud.

**What is absent, and what that absence means.**

- **No Metaculus signal whatsoever.** CP, Pro and gold are all empty; `cp_reveal_time` is
  2026-09-24T17:00Z with 8 forecasters [1]. This repo's usual primary anchor does not exist
  today, so the market prices carry the entire external-validation load. It also means my IQR
  should be wider than it would be on a question with a settled CP, and that the 2026-09-24
  reveal is a scheduled, high-information event.
- **No sign the mainstream is converging on Channel 14.** If Filber were measuring a real
  hidden Likud vote, I would expect at least one mainstream house to drift toward him over
  seven weeks. None has; the mainstream gap has instead widened against Likud
  (fortnightly: −1.08 → −2.59 → −2.55 → −3.00). Absence of expected evidence.
- **No pardon decision.** Herzog has deferred Netanyahu's request and is pushing plea-deal
  mediation [17]. A pardon before 27 October is a live wildcard whose *sign is genuinely
  unclear* — it would mobilise both electorates — so it enters as variance, not drift.
- **No Sentinel, Mantic, GJOpen or INFER question** on this outcome. Nothing to triangulate.

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| **Metaculus CP (recency-weighted)** | **not revealed** | 2026-09-20 | reveals 2026-09-24T17:00Z; n=8 forecasters [1] |
| **Metaculus Pro** | **not revealed** | 2026-09-20 | empty aggregation [1] |
| **Metaculus gold medalists** | **not revealed** | 2026-09-20 | empty aggregation [1] |
| **Polymarket** — *Israeli Legislative Election Winner* | **Yashar 61.0%, Likud 39.0%**, Together 0.6%, Shas/Democrats/Otzma ≈0.1% | 2026-09-20 | $313,940 volume, $150,606 liquidity, 2¢ spread. Explicit tie-break on valid votes [10] |
| Polymarket trend (same market) | Yashar 47.5% (08-30) → 50.5% (09-06) → **61.5% (09-13)** → 61.0% | 2026-09-20 | the 10 pp jump lands on the first post-list-filing polls [10] |
| **Kalshi** `KXISRAELKNESSET-26` | Yashar 50%, Likud 33%, minor options 1% each → **normalised ≈ Yashar 58% / Likud 38%** | 2026-09-20 | book sums to 0.86; ticker list still carries dead options (Yesh Atid, National Unity). Thin — treat as corroboration only [18] |
| Manifold | **no market** | 2026-09-20 | searched; only a Netanyahu-tenure market exists |
| Sentinel Team / Mantic / GJOpen / INFER | no matching question | 2026-09-20 | — |
| JPost five-poll average (incl. Channel 14) | Yashar 22.2 / Likud 21.2 seats | 2026-09-17 | equal-house weighting [3] |
| Mainstream-house average (this forecast) | Yashar 23.1 / Likud 20.1 seats | 2026-09-17 | Channel 14 and i24 excluded [2] |

**Cohort disagreement: not assessable.** With all three Metaculus aggregations hidden, the
repo's normal cross-check (Pro and gold against CP, and against me) cannot be run. This is a
material weakness of v1 and the reason `next_review` is set to the day after the reveal.

**Where I sit.** My Likud 38.1% is **0.9 pp below Polymarket** and ~0.1 pp above Kalshi's
normalised price — effectively on top of both. The agreement is not herding: gap₀, the drift
term and the tie mass were all built before prices were pulled, and both my model and the
markets are making the same single live judgement (how much of the mainstream-vs-Filber gap
to split). Two caveats in opposite directions: mild **longshot bias** would inflate the
trailing side, arguing Likud's true price is a shade under 38%; and neither market prices an
*annulment*, because both define a tie-break, so a Metaculus forecaster faces a slightly
different question than a Polymarket trader.

### Scenarios

Branches of `G`, from the simulation. Mutually exclusive, exhaustive; weights are
unconditional (before dropping the annulment mass).

| # | Scenario | Weight | Implies |
|---|---|---|---|
| A | **Mainstream polls are broadly right and hold.** Late consolidation is symmetric or favours Yashar; Netanyahu's anti-Ra'am push does not move the seat gap. `G ≤ −3` | 0.320 | Yashar |
| B | **Narrow Yashar win.** Some late Likud recovery, not enough. `G ∈ {−2, −1}` | 0.223 | Yashar |
| C | **Exact tie.** `G = 0` | 0.111 | **resolution undefined → likely annulled** |
| D | **Narrow Likud win.** The 2019A pattern: both lists consume satellites, Likud's pool is slightly richer. `G ∈ {1, 2}` | 0.178 | Likud |
| E | **2015 replay.** Gevalt campaign in the unmeasured final 72 hours collapses Amcha Yisrael/RZP/Otzma into Likud. `G ≥ 3` | 0.161 | Likud |
| F | **Third list tops the poll** (realistically B'Yachad) | 0.008 | Other |
| — | Election not held / no result before 2027-01-01 | 0.015 | annulled |

### Sensitivity

| Assumption | If instead | Forecast becomes |
|---|---|---|
| **Drift = +1.2 seats** (shrunk from the +2.0 historical mean) | +0.0 — no late swing at all; 2019B/2021 pattern | **Likud 24.7%, Yashar 74.5%** |
| same | +2.4 — the unshrunk 2015/2019A pattern in full | **Likud 53.2%, Yashar 45.9%** |
| **Filber-house weight = 10%** | 0% — treat Channel 14 and i24 as pure advocacy (gap₀ −3.20) | **Likud 25.8%, Yashar 73.3%** |
| same | 25% — equal weight per house, Filber's series taken at face value (gap₀ −0.47) | **Likud 58.8%, Yashar 40.3%** |
| **sd[G] = 3.45 seats** | 4.5 seats | Likud 40.9%, Yashar 58.2% — **small** |
| **Tie → annulled** | Tie → popular-vote tie-break, as Polymarket does | Likud 39.4%, Yashar 59.8% — **negligible** |

Two assumptions do essentially all the work and they pull the answer across a 33 pp range:
the drift term and the house weight. Both are judgement calls on thin evidence, which is why
the IQR on the leading option is 12 pp wide rather than the 4–6 pp a settled question earns.
Note that the two sensitivities are not independent — a forecaster who both believed Filber
and expected a 2015-style endgame would land near Likud 70%, and that is the coherent bull
case I am rejecting.

Calibration hygiene: the answer is not near 0 or 100; it is not a round number; the 61.0/38.1
split moves less than 3 pp when sd[G] is raised to 4.5; I would take either side of a bet at
61/39 on Yashar with mild reluctance, which is the right feeling for a question whose two
load-bearing inputs are both judgement calls; and the scope check passes — pushing the
election out a further month widens sd and pulls both options toward 50.

### What would change my mind (tripwires)

- [ ] **2026-09-24, 17:00 UTC — Metaculus CP, Pro and gold reveal.** If Pro *and* gold both
      land ≥ 10 pp from my Likud 38.1% in the same direction → **re-analyse before defending**
      (direction either, magnitude 0).
- [ ] **By 2026-09-30 — Metaculus admins publish a tie-breaker** (or rule that a tie is
      ambiguous). Either way the 11.1% annulment mass is resolved and the question becomes
      scorable or not (direction either, magnitude 0).
- [ ] **By 2026-10-13 — mainstream-house average (Channel 14 and i24 excluded) has Likud
      level with or ahead of Yashar.** → **down 12 pp on P(Yashar)**.
- [ ] **By 2026-10-13 — mainstream-house average gap reaches ≥ 4 seats to Yashar** (from
      −3.0 on 2026-09-17). → **up 8 pp on P(Yashar)**.
- [ ] **By 2026-10-23 (last legal polls) — Amcha Yisrael (Ofer Winter) below 3.25% in a
      majority of the final week's polls.** Its ~4 seats of votes are the most recoverable
      pool Likud has. → **down 4 pp on P(Yashar)**.
- [ ] **By 2026-10-20 — Herzog grants Netanyahu a pardon, or the Attorney-General announces a
      plea deal.** Sign genuinely unclear; both electorates mobilise → **re-analyse**
      (direction either, magnitude 0).

### Sources

1. Metaculus question 45670 / question id 45859, aggregations + comments via the
   `metaculus-aggregations` skill — snapshot in `raw/metaculus-2026-09-20.json`
   (accessed 2026-09-20)
2. Opinion polling for the 2026 Israeli legislative election — Wikipedia —
   https://en.wikipedia.org/wiki/Opinion_polling_for_the_2026_Israeli_legislative_election
   (wikitext snapshot in `raw/wikipedia-polling-wikitext-2026-09-20.txt`; 168 rows parsed by
   `raw/parse_polls.py` + `raw/poll_analysis.py`) (accessed 2026-09-20)
3. "Gadi Eisenkot still leads in polls, but Benjamin Netanyahu shortens distance" —
   The Jerusalem Post, 2026-09-17 — https://www.jpost.com/israel-election-2026/article-908921
   (accessed 2026-09-20)
4. "Maariv pollster: Election race, Likud struggles, and threshold battles" —
   The Jerusalem Post, 2026-09-13 — https://www.jpost.com/israel-election-2026/article-908437
   (accessed 2026-09-20)
5. "Netanyahu's anti-Arab campaign has found Gadi Eisenkot's Achilles' heel" —
   The Times of Israel, 2026-09-18 —
   https://www.timesofisrael.com/netanyahus-anti-arab-campaign-has-found-gadi-eisenkots-achilles-heel/
   (accessed 2026-09-20)
6. "As parties lock in, Eisenkot plots path to power through heart of old Likud" —
   The Times of Israel, 2026-09-14 —
   https://www.timesofisrael.com/as-parties-lock-in-eisenkot-plots-path-to-power-through-heart-of-old-likud/
   (accessed 2026-09-20)
7. Opinion polling for the 2015 Israeli legislative election — Wikipedia —
   https://en.wikipedia.org/wiki/Opinion_polling_for_the_2015_Israeli_legislative_election
   (accessed 2026-09-20)
8. Opinion polling for the 2022 Israeli legislative election — Wikipedia —
   https://en.wikipedia.org/wiki/Opinion_polling_for_the_2022_Israeli_legislative_election
   (accessed 2026-09-20)
9. April 2019 Israeli legislative election — Wikipedia —
   https://en.wikipedia.org/wiki/April_2019_Israeli_legislative_election (accessed 2026-09-20)
10. Polymarket, *Israeli Legislative Election Winner* — https://polymarket.com/event/israeli-legislative-election-winner
    (Gamma API + CLOB price history; snapshot in
    `raw/polymarket-largest-party-2026-09-20.json`) (accessed 2026-09-20)
11. Shlomo Filber — Wikipedia — https://en.wikipedia.org/wiki/Shlomo_Filber
    (accessed 2026-09-20)
12. Netael Bandel, "Netanyahu Trial: Witness Changes Story on Key Meeting a Second Time" —
    Haaretz, 2022-06-14 —
    https://www.haaretz.com/israel-news/2022-06-14/ty-article/filber-changes-his-story-a-second-time-on-key-case-4000-meeting/00000181-5e9b-dde4-a187-febf1ebd0000
    (cited via [2]; accessed 2026-09-20)
13. "Israel Elects 2026: Fragmentation on the right risks Bibi's chances" — Labour Friends of
    Israel, ~2026-09-14 —
    https://www.lfi.org.uk/israel-elects-2026-fragmentation-on-the-right-risks-bibis-chances/
    (accessed 2026-09-20)
14. "Israeli parties submit slates for October Knesset elections" — Al Jazeera, 2026-09-09 —
    https://www.aljazeera.com/news/2026/9/9/israeli-parties-submit-slates-for-october-knesset-elections
    (accessed 2026-09-20)
15. Lists of Candidates — Central Elections Committee, 2026-09-03 —
    https://www.gov.il/en/pages/candidates-lists-26 (accessed 2026-09-20)
16. 2026 Israeli legislative election — Wikipedia —
    https://en.wikipedia.org/wiki/2026_Israeli_legislative_election (accessed 2026-09-20)
17. "Rebuffing Netanyahu's pardon request, at least for now, Herzog calls for new plea deal
    talks" — The Times of Israel —
    https://www.timesofisrael.com/herzog-pushes-for-new-plea-deal-talks-says-he-wont-consider-netanyahu-pardon-request-yet/
    (accessed 2026-09-20)
18. Kalshi, `KXISRAELKNESSET-26` —
    https://kalshi.com/markets/kxisraelknesset/israeli-knesset-election/kxisraelknesset-26
    (API returned no book this session; prices via prediction.com's cross-exchange aggregator,
    https://prediction.com/odds/who-will-win-the-next-israeli-legislative-election/11068)
    (accessed 2026-09-20)
19. "Main opposition factions ink surplus-vote deals in bid to maximize Knesset
    representation" — The Times of Israel, 2026-09-10 —
    https://www.timesofisrael.com/main-opposition-factions-ink-surplus-vote-deals-in-bid-to-maximize-knesset-representation/
    (accessed 2026-09-20)
20. Opinion polling for the April 2019 / September 2019 / 2021 Israeli legislative elections —
    Wikipedia — https://en.wikipedia.org/wiki/Opinion_polling_for_the_April_2019_Israeli_legislative_election ,
    https://en.wikipedia.org/wiki/Opinion_polling_for_the_September_2019_Israeli_legislative_election ,
    https://en.wikipedia.org/wiki/Opinion_polling_for_the_2021_Israeli_legislative_election
    (accessed 2026-09-20)
21. "Candidate List Selection Ahead of Israel's 2026 Election" — Israel Democracy Institute —
    https://en.idi.org.il/articles/65619 (accessed 2026-09-20)
22. "The Pollster Scorecard" — Israel Elects Deep Dive —
    https://israelects.substack.com/p/the-pollster-scorecard — **paywalled, not used**;
    recorded because it is the right empirical basis for the house weights this forecast sets
    by judgement (accessed 2026-09-20)

**Date**: 2026-09-20
**Forecast**: Likud 38.1%, Yashar 61.0%, Other 0.9% — IQR on Yashar [55.0%, 67.0%]
**Thesis**: Nine mainstream Israeli pollsters span 1.9 seats on Likud and put Eisenkot's
Yashar ahead in 43 of their 52 polls since August (8 ties, 1 Likud lead); the only houses
showing Likud ahead are Channel 14 and i24, which share one pollster, Shlomo Filber, whose
Likud ties Wikipedia's own polling page flags and whose Likud figure has been frozen at 30–32
while the field moved 3 seats [2][11]. Weighting them 10% gives a −2.1 seat gap, to which I
add +1.2 seats of late drift — the historical 5-weeks-out-to-result mean of +2.0 shrunk hard,
because "Israeli polls underestimate Likud" turns out to be a 2015 artefact (drop 2015 and
the mean gap error is +0.4) and because April 2019's surge was symmetric across both leading
lists [7][9]. Net E[gap] = −0.9 ± 3.45 seats, which is Polymarket's price to within a point.
The live tail risk is not Likud but **an exact tie at 11.1%**, which the fine print does not
cover and which happened in April 2019 (35–35); the vector above is conditional on the
question resolving.
