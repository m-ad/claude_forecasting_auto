# Research log — Will Benjamin Netanyahu cease to be Prime Minister of Israel during 2026?

Working notes. Rough is fine; **completeness beats polish**. The next update reads this to
learn what was already checked and what was already ruled out.

Session date: 2026-08-31. All numbers fetched live this session unless noted.

## Question mechanics

- **Resolution source**: Metaculus admin judgement against public reporting on who holds the
  office of Prime Minister of Israel. No data series, no release schedule — it is decided by
  a political event, not a statistic.
- **Resolution date**: any point before 2027-01-01. Scheduled close 2026-12-31.
- **The single decisive mechanic**: under Basic Law: The Government, the outgoing government
  **continues to carry out its functions until the new government is constituted**. Netanyahu
  has been a *caretaker/transitional* PM since the Knesset dissolved on 2026-07-17, and a
  caretaker PM **is** the Prime Minister. Neither the dissolution, nor the 2026-10-27 election,
  nor even losing that election resolves this question. Only the swearing-in of a **successor**
  (or death / a ≥14-day suspension) does.
- **Edge cases**:
  - Temporary removal (suspension, acting PM, incapacity) counts **only** if it lasts ≥14
    consecutive days *entirely within 2026* → an event starting after ~2026-12-17 cannot
    resolve YES on that route.
  - A permanent cessation (successor sworn in) has no duration requirement.
  - Losing the election but staying caretaker into 2027 → **NO**.
  - Netanyahu resigning as PM would trigger an acting PM (currently Yariv Levin is the
    designated acting PM) → YES, if it holds ≥14 days inside 2026.
  - Announcing a future resignation is **not** enough for Metaculus (it *is* enough for
    Polymarket — see the market-comparison note; this is the main reason the two differ).

### Statutory clock (this is where the forecast lives)

| Step | Rule | 2026 date |
|---|---|---|
| Election day | fixed by the Party Funding Law | 2026-10-27 |
| Official results confirmed | ≤ 8 days | 2026-11-04 (JPost explainer) |
| President's consultations begin | ≤ 7 days after publication | by 2026-11-11 |
| Mandate assigned | historically 8–14 days after election | ~2026-11-09 to 11-14 |
| First mandate | 28 days **+ optional 14-day extension** | expires **2026-12-21 to 12-26** |
| Second mandate | 28 days, **no extension** | expires ~2027-01-19 → too late |
| Third attempt / Knesset route | 21 + 14 days | 2027 |
| Investiture threshold | **no 61 required** — a simple majority of those voting; a
  government can be installed 59–50 with abstentions (2021 Bennett gov passed 60–59) | — |

**Consequence**: the first-mandate deadline falls *just inside* 2026 (≈ Dec 21–26). So
YES ≈ "a non-Netanyahu figure gets the **first** mandate and succeeds within it".
If the first mandate fails, the second mandate runs into late January 2027 → NO.
This is a much cleaner decomposition than "how fast do Israeli coalitions form".

## Reference classes considered

| Class | n | Window | Base rate | Source | Kept? |
|---|---|---|---|---|---|
| Israeli elections → new government sworn in within 65 days | 15 | 1988–2022 | **11/15 = 73%** | Wikipedia government formation dates, computed this session | **Kept** — the headline outside view |
| …restricted to elections that produced *any* government | 13 | 1988–2022 | 11/13 = 85%; median 50 days | same | Kept |
| …restricted to the fragmented era (2019a, 2019b, 2020, 2021, 2022) | 5 | 2019–2022 | **1/5 = 20%** | same | Kept — sharply disagrees with the long class |
| First mandate-holder succeeds (of elections producing a government) | 13 | 1988–2022 | 11/13 = 85%; IDI: "the first nominee has almost always succeeded" | IDI | Kept |
| Governments replacing an incumbent PM with an opposition leader | 4 | 1992, 1999, 2006, 2021 | 3/4 within 65 days (20, 50, 37 days; 2021 = 82) | same | Kept |
| Annual mortality, male age 77, high-income, treated early-stage prostate cancer + pacemaker | — | — | ~3%/yr → ~1.0–1.3% over Sep 1–Dec 31 | actuarial, judgement | Kept as floor |

Days from election to swearing-in, 1988–2022 (`*` = change of PM):
51 (1988), 20 (1992 Rabin*), 20 (1996 Netanyahu*), 50 (1999 Barak*), 29 (2001 Sharon*),
31 (2003), 37 (2006 Olmert*), 49 (2009 Netanyahu*), 55 (2013), 58 (2015), **FAILED** (2019a),
**FAILED** (2019b), 76 (2020), 82 (2021 Bennett*), 58 (2022 Netanyahu*).
Window this cycle = exactly **65 days** (Oct 27 → Dec 31).

Note the recent pattern: 2013 (55), 2015 (58), 2022 (58) all ran essentially to the full
42-day statutory limit. Modern Israeli coalitions use all the time they are given — which is
fine here, because the limit itself expires ~Dec 21–26.

**Correction to a widely-read Metaculus comment**: user `supernumerate` (2026-07-23, forecast
0.18) asserted "a non-Netanyahu government has never formed faster than 82 days". That is
false and was corrected in-thread by `darkives`: Olmert's 31st government formed in 37 days
(2006), Rabin's in 20 (1992), Barak's in 50 (1999). The CP dipped ~0.30 → ~0.25 shortly after
that comment. Some of the low CP may be anchored on an incorrect base rate.

## Decomposition

P(YES) ≈ P(election held 2026-10-27) × Σ_scenarios w_i · P(successor sworn in ≤ 2026-12-31 | scenario)
        + non-electoral paths (death, ≥14-day incapacity, pre-election resignation)

Post-election configurations (Netanyahu bloc = Likud + RZP + Otzma Yehudit + Shas + UTJ +
Winter's People of Israel, which has pledged to recommend only Netanyahu):

| # | Configuration | Weight | P(YES \| config) | Reasoning |
|---|---|---|---|---|
| A | Netanyahu bloc ≥ 61 | 0.17 | 0.03 | He forms a government himself (49–58 days historically); residual = Likud dumps him |
| B | Anti-Netanyahu Zionist bloc ≥ 61 outright | 0.21 | 0.72 | First mandate to Eisenkot, 4–5 partners, strong urgency; risk = 2021-style internal slog |
| C | Neither ≥ 61, anti-Netanyahu Zionist bloc larger (**modal**) | 0.47 | 0.42 | Needs Arab abstention (minority gov) or a Haredi defection, *and* first-mandate success |
| D | Neither ≥ 61, Netanyahu bloc ≥ anti-Netanyahu bloc | 0.15 | 0.08 | Netanyahu likely gets the first mandate; 2019–21 deadlock replay → NO |

Weighted: 0.17·0.03 + 0.21·0.72 + 0.47·0.42 + 0.15·0.08 = **0.366**
× 0.96 (election on schedule; Polymarket 96.5%) = 0.351
+ non-electoral paths on the NO mass (~2%) ≈ **+0.013**
→ **≈ 0.365**, shaded to **0.350** (see reconciliation below).

Cross-check via the market decomposition: Kalshi and Polymarket both price
P(Netanyahu is the next PM sworn in) at 28–30% → P(someone else, eventually) ≈ 0.70.
My 0.35 implies a timing conditional of ~0.50 (sworn in inside 2026 given it happens at all).
The Metaculus CP of 0.26 implies a timing conditional of ~0.37. That gap **is** the forecast.

## Search log

| Date | Query / source | Finding | Effect on forecast |
|---|---|---|---|
| 08-31 | metaculus_aggregations.py 40966 | CP 26.0% IQR[20,32] n=278; **Pro 34.0%** IQR[22,50] n=23; **Gold 25.0%** IQR[20,30] n=91; 841 total forecasters | Anchor; Pro–gold gap of 9pp is itself signal |
| 08-31 | CP history (399 pts, since 2025-12-19) | Remarkably flat 24–30% all year; brief 0.50 open, 0.30 in June, 0.25 late July | Community view is stable, not drifting |
| 08-31 | Metaculus comments (10) | `supernumerate` 0.18 thesis rests on a false claim (see above), corrected by `darkives` | Reason to discount the low tail of the CP |
| 08-31 | Al Jazeera / ToI: Knesset dissolution | Knesset dissolved **2026-07-17** by 62–0 (Netanyahu voted for it); first Knesset to serve a full term since 1988; election **2026-10-27**, confirmed by the Party Funding Law | Netanyahu is already caretaker PM → dissolution does not resolve YES |
| 08-31 | Wikipedia: Opinion polling for the 2026 election | 9 polls 24–30 Aug. Yashar 21–26, Likud 19–31, Together 7–16, Democrats 8–11, Yisrael Beiteinu 6–10. Coalition bloc: 43, 43, 45, 46, 48, 48, 50, **51**, **59** (median 48; the two highest are Ch.14/Filber and Direct Polls/i24, both right-leaning) | Netanyahu bloc ~11 seats short of 61 on the mainstream median |
| 08-31 | Haaretz election polls, Aug 4 / 11 / 17 / 24 / 26 | Anti-Netanyahu Zionist bloc 55–60, consistently **1–4 short of 61 without Arab parties**; Arab parties 10–15 | Modal outcome is scenario C |
| 08-31 | ToI: "Eisenkot lays groundwork for a minority government" | Eisenkot preparing to be sworn in with **58–59 MKs**; Israeli law needs only a simple majority of those voting; aides say a fragile minority government beats Netanyahu staying; if it collapses **Eisenkot**, not Netanyahu, becomes caretaker | **Raises** P(YES \| C) materially — removes the hard 61 requirement |
| 08-31 | Fruits & Votes (2026-08-26), "Could Eisenkot form a minority government?" | Models 58–52–10; confirms "more votes for than against" suffices; flags the optics problem and Zionist parties' refusal of formal deals with Ra'am / Joint List | Confirms mechanism, flags fragility |
| 08-31 | ToI: "Eisenkot takes heat for implying… Arab parties"; Arab Center DC | Eisenkot: "won't ask anything of them", no deals with Arab-majority parties | **Lowers** P(YES \| C) — abstention has to be unreciprocated |
| 08-31 | JPost: Arab list negotiations | Hadash–Ta'al–Balad Joint List revived **without Ra'am**; a later report says the deal "collapsed over slate order". **Ra'am polls below the 3.25% threshold in 6 of 9 late-August polls** (1.1–2.4%) | **Lowers** P(YES \| C) — the one Arab party willing to sit in a Zionist coalition may not be in the Knesset. Lists close 2026-09-09, so still fluid |
| 08-31 | Haaretz / JC / ToI: Ofer Winter | New far-right "People of Israel" party, 4–8 seats in polls; Winter: "Netanyahu is the leader of the right-wing camp, and he is the only person we will recommend" | Winter counts **inside** the Netanyahu bloc → the bloc is ~48–53, not ~43–48 |
| 08-31 | Israel National News / Media Line: polling accuracy | Across 2015, 2020, 2022 polls under-predicted the right bloc by **~5.7 seats** and over-predicted centre-left/Arab by ~2.5. 2015: Likud polled 22, won 30 | Applied a partial correction (60% no-bias / 40% +4 right). Source is right-leaning; magnitude treated cautiously. 2021 ran the other way (right bloc polled ~59, won 52) |
| 08-31 | ToI: Likud primary 2026-08-17/18 | Eli Cohen took slot 1; Ohana, Levin, Regev top the list; turnout 53.5%; Netanyahu "very satisfied"; Central Committee gave him 8 reserved slots | Netanyahu is firmly Likud leader into the election → pre-election intra-party ouster ≈ 0 |
| 08-31 | ToI / Bloomberg / Axios / Ynet: pardon request | Herzog **rebuffed** the pardon request (April 2026), pushing a plea deal instead; Netanyahu refuses to admit guilt or leave politics; any deal is expected to require departure from public life; Trump lobbied publicly for a pardon | Pardon-driven resignation path ≈ 1–2%, not more |
| 08-31 | ToI / Manila Times: trial | Netanyahu **finished testimony 2026-06-24** after 98 hearings; defence witnesses and closing arguments remain; **verdict expected 2027 at the earliest** | Legal-removal path in 2026 ≈ 0 |
| 08-31 | CNN / Al Jazeera / JPost: health | Age 76 (77 on 2026-10-21). Disclosed **early-stage prostate cancer treated with radiation** (revealed 2026-04-24, declared cancer-free); pacemaker 2023; hernia surgery 2024; prostate removal Dec 2024; hospital visit May 2026 ("dental"). Criticised for opacity | Death/incapacity floor ~1.5–2% for Sep 1 – Dec 17 |
| 08-31 | CNN live / Britannica / Al Jazeera: security | Iran war ended in a ceasefire (early April 2026); Israel–Lebanon ceasefire 2026-04-16; Houthi strikes continue; Kushner shuttling on Gaza; **Netanyahu has rejected key elements of the US-backed Gaza roadmap** | Two-sided wildcard: a rally-round-the-flag event helps him, a Trump rupture hurts him. Kept as a tripwire, no net shift |
| 08-31 | The Week (2026-08-19), "10 reasons Netanyahu could win"; Time (2026-07-14) | Coalition polling 49–54; demographics, Haredi alliance, security persona; **"both are expected to struggle to form a coalition"** | Direct support for the deadlock (NO) branch |
| 08-31 | Polymarket gamma API, `netanyahu-out-before-2027` | **"Out by end of 2026": 48.5%** (bid 0.48 / ask 0.49), $2.23M volume on that leg, $124M event volume. **Criteria are looser**: an *announcement* of resignation or removal suffices | Not directly comparable; explains most of the gap to the CP |
| 08-31 | Polymarket `who-will-be-the-next-prime-minister-of-israel-after-the-next-election` | Eizenkot 49.8%, **Netanyahu 29.5%**, Bennett 7.5%, Lieberman 4.3%, Winter 3.5%. $34.2M volume, $2.34M liquidity. Deadline Dec 2027; caretakers excluded | Real-money P(someone else eventually) ≈ 0.70 |
| 08-31 | Kalshi `KXISRAELPM-26OCT27` | Eizenkot 55% (53/57), **Netanyahu 28%** (26/28), Bennett 5%, Lieberman 5%. Horizon Oct 2027 | Independently corroborates Polymarket |
| 08-31 | Polymarket `israeli-legislative-election-winner` | Largest party: **Yashar 49.5% vs Likud 46.5%** — essentially a coin flip | Cuts against assuming Eisenkot is the automatic mandate-holder |
| 08-31 | Polymarket `israeli-election-results-in-a-hung-parliament` | 26% that a new election is called before any government forms (low volume, $4.6k) | Consistent with a ~25–30% deadlock branch |
| 08-31 | Polymarket `will-israel-election-happen-as-scheduled` | **96.5%** the vote happens on 2026-10-27 | Used directly as the gating factor |
| 08-31 | Manifold API | This exact question (ACX mirror) **41.6%** (vol 21k) and 43.5%; "still PM at end of 2026" 61.6% → 38.4%; "cease before end of 2026" 36.5%; "alive on 2026-12-31" 97.9%; "will run for Knesset" 95.7% | Play-money, discounted, but clusters 36–43% — well above the CP |
| 08-31 | IDI: "Everything You Need to Know About How a Government is Formed" | 28 days + 14-day extension; second nominee 28 days **no extension**; third 14 days; **no absolute majority required in law** for investiture; "the first nominee has almost always succeeded"; total range 20–100 days | The load-bearing source for the statutory-clock argument |
| 08-31 | JPost election explainer (article-902333) | Lists close **2026-09-09**; election **2026-10-27**; official results **2026-11-04**; appeals to **2026-11-18** | Mandate ~Nov 9–14 → first-mandate deadline Dec 21–26 |
| 08-31 | Wikipedia: Cabinet of Israel (formation dates) | 22nd–37th governments, exact swearing-in dates | Base-rate computation above |
| 08-31 | Sentinel Team / Mantic search | **No matching published forecast found** for this question | Dead end — do not re-run next time unless the question becomes topical there |

## Dead ends and ruled-out hypotheses

- **Legal removal in 2026** — ruled out. Testimony ended 2026-06-24; defence witnesses and
  closing arguments remain; a verdict is a 2027+ event, and a *final* conviction (after appeal)
  is what Basic Law: The Government requires for removal. ≈ 0.
- **Attorney-General incapacitation declaration** — attempted in 2023 and blocked; requires
  the government or 61 MKs plus Supreme Court survival. Not live. ≈ 0.
- **Constructive no-confidence before the election** — the Knesset has already dissolved and
  the same 62 MKs who voted for dissolution would have to install someone else. ≈ 0.5%.
- **Pre-election Likud coup** — killed by the 2026-08-17 primary result and the Central
  Committee's 8 reserved slots. ≈ 0.
- **Pardon-for-retirement deal before 2027** — Herzog shelved the pardon request; Netanyahu
  refuses the two conditions (admission of guilt, exit from politics). Kept at 1–2%, not more.
- **Election postponement** — Polymarket 96.5% it happens on schedule; the funding law fixed
  the date; no live proposal to delay. Kept as the 4% gate.
- **Sentinel Team / Mantic** — searched, nothing published on this question.

## Open questions to chase next time

1. **2026-09-09 final party lists.** Does Ra'am run alone (and does it poll above 3.25%)?
   Do Hadash–Ta'al–Balad actually merge? Do RZP and Otzma Yehudit run together, and does
   Winter's party survive? Each threshold miss on the right is worth ~2–4 seats of wasted vote.
2. **Whether Eisenkot moves off "no deals with Arab parties"** — the single biggest lever on
   scenario C. Any signal of quiet Ra'am/Hadash contacts is worth +5pp.
3. **Whether the anti-Netanyahu parties pre-commit to recommending one person.** A public
   pre-election pact naming Eisenkot (or an Eisenkot–Bennett rotation) would be worth +5pp;
   a Bennett or Lieberman refusal is worth −5pp.
4. **Yashar's trajectory in October.** New-party deflation is the main route to scenario A
   (cf. Yamina 2021: polled ~20 at peak, won 7).
5. **Gaza/Iran**: a Trump-brokered deal Netanyahu signs, or a rupture with Trump; a new
   escalation. Two-sided.
6. **Netanyahu's health** — annual medical report timing and any unscheduled hospitalisation.
7. Re-check the Pro cohort: it has been the most volatile (22–50 IQR). If Pro converges
   *down* to gold, that is evidence against this forecast.

---

# v2 working log — 2026-09-18

## Tooling note (applies to the whole repo)

`metaculus-aggregations` returned "status 0 / no HTTP response" on the first attempt this
session — the same failure mode that blocked the Oman and SPR updates on 09-10/09-12 and was
recorded there as a Cloudflare challenge. It is **not** Cloudflare: it is the local egress
proxy resetting Chromium's TLS 1.3 ClientHello, exactly as the script's own module docstring
warns. Re-running with `METACULUS_FORCE_TLS12=1` succeeded in ~40 s on the first try, for all
four questions updated this session. Use that env var by default in this container.

## Searches run

- Metaculus #40966, all three cohorts + 396 history points + 8 comments (`raw/metaculus-2026-09-18.json`)
- Wikipedia opinion-polling page, 16–17 September entries (Channel 14/Filber, Direct Polls/i24, Kantar)
- Middle East Forum poll-of-polls tracker (2026-09-17 state)
- JPost election coverage: articles 908444, 908921, 908282, 907949
- Haaretz 2026-09-17 poll story; Channel 13 poll via secondary reporting
- ToI: surplus-vote deals; Eisenkot minority-government/defections liveblog (Channel 12, 09-15);
  "Netanyahu's anti-Arab campaign has found Eisenkot's Achilles' heel"
- Polymarket gamma API: `netanyahu-out-before-2027`, next-PM event, largest-party event
- Netanyahu health / pardon / trial: Truthout, Media Line, Bloomberg, Ynet — nothing new since v1

## What the v1 open-questions list got right and wrong

Item 7 of the v1 list — "if Pro converges *down* to gold, that is evidence against this
forecast" — is the one that fired, and I honoured it. Items 1–3 all resolved in the *bullish*
direction (Ra'am clears, Eisenkot moves, surplus-vote deals signed) and the forecast still fell
7 pp, because none of the seven v1 tripwires was pointed at the quantity that actually moved:
the bloc-level polling average itself. v1 had a tripwire only for the Netanyahu bloc crossing
**57**, a threshold far above where the action was. v2 replaces it with a two-sided band
(≥57 down / <49 up) and adds a recommendation-count tripwire, which is the real decision node.

## Open questions to chase next time

1. **The recommendation tally** published after Herzog's consultations (~2026-11-09 to 11-11).
   This is now the highest-leverage observable in the question — higher than the seat count.
2. Whether Ra'am and/or the Joint List say anything explicit about recommending Eisenkot during
   the campaign. Both are currently silent, and the model puts 0.60/0.35 on them.
3. Whether the Hendel–Zelekha list (~2.4 seats, below threshold) merges into an existing list
   before the final lists are locked — worth ~1–2 opposition seats in expectation.
4. Yashar's late-campaign trajectory (new-party deflation; cf. Yamina 2021).
5. Whether any named Yashar candidate breaks publicly on the Arab-abstention question.

---

## 2026-10-09 — v3 research log (shared pass with #45670)

- **Metaculus**: Cloudflare block. API JSON shows the question open with 849 forecasters. No cohorts.
- **Markets** (all 2026-10-09, `raw/*-2026-10-09.json`): Polymarket out-by-Dec-31 37.5 (was 46.5);
  next PM: Netanyahu 36.5, Eizenkot 43.7, Bennett 9.5; on-schedule 91.9 (was 96.5); hung
  parliament 37.5 (thin). Kalshi KXISRAELPM: Netanyahu 36, Eizenkot 44, Bennett 8. Manifold ACX
  mirror 28.2 (was 41.6).
- **Bloc polls**: mainstream, latest per house: opposition Zionist 55.1 (was 56.1 mid-Sep),
  Netanyahu incl. Amcha 51.9 (51.5), Arab 13.0 (12.4). Parsed from the sister question's
  wikitext cache.
- **Arab-route evidence**: Eisenkot (JPost, 24 Sep): Ra'am and the JL are not viable partners.
  Liberman's "no 58-seat government" line dates from 17 Aug (already known at v1). Hadash's
  conditions (26 Aug). No Arab-list recommendation statement found either way. The search
  summary claim that "Bennett and Liberman refuse a minority government" could only be traced
  to Liberman in August.
- **Model**: `raw/scenario-model-2026-10-09.py` → 22.5%. The per-driver attribution was done
  by stepping inputs from v2 to v3 one at a time (seeded, 400k draws).
