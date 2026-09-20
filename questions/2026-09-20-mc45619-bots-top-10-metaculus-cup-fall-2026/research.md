# Research log — How many bots will finish in the top 10 of the Metaculus Cup Fall 2026?

Working notes. Rough is fine; **completeness beats polish**. The next update reads this to
learn what was already checked and what was already ruled out.

## Question mechanics

- **Resolution source**: the final Metaculus Cup Fall 2026 tournament leaderboard
  (<https://www.metaculus.com/tournament/metaculus-cup-fall-2026/>), read *after every other
  question in the Cup has resolved*. Count = accounts in the top 10 that are **registered as
  bot accounts** on Metaculus.
- **Fine print**: the top-10 list is built only from (a) prize-eligible users and (b) bots.
  Admins and other excluded human accounts are struck from the list first — so striking a
  staff account *opens a slot that a bot can occupy*.
- **Release schedule / cutoff**: Cup runs 2026-08-28 → 2027-01-01; this question closes
  2026-12-15, i.e. ~2 weeks before the Cup does. Resolution therefore lands in Jan 2027.
- **Question type**: discrete, 0–10 inclusive, both bounds closed (11 outcomes). No
  open tail — a tie pushing 11 accounts into the "top 10" has nowhere to go; a commenter
  (exmateriae, 2026-09-19) raised exactly this, half-jokingly. Treated as negligible.
- **Cup scoring** (drives everything): tournament score is the sum of peer/relative scores
  over all questions, weighted by *coverage* — how early you forecast, how many questions you
  forecast on, and how often you update [S13, S14]. This is the mechanism by which bots beat
  humans on the Cup metric *before* reaching accuracy parity: a bot can hold a live position
  on every question and revise continuously [S9].
- **Bots are not prize-eligible** in the Cup [S12]; they enter as a benchmark. Their
  participation is therefore a *choice*, driven by reputational/commercial payoff — which is
  the largest single source of uncertainty here.

### Edge cases and ambiguities

1. **"Registered as bots"** is an account flag, not a judgement about what the account is.
   MaxA asked the admins (2026-09-19) about `symbiosis` — in Summer 2026 there were **six**
   top performers ineligible for prizes but only **five** carried the robot marker. Unanswered
   as of 2026-09-20. Direction of the effect is ambiguous: an unflagged bot does not count
   (pushes the answer down), but a struck non-bot account opens a slot (pushes it up).
2. **Late entry.** The Cup scores from question *open*, so a bot that starts mid-season is
   structurally out of the top 10 even if perfectly accurate. Participation ≠ contention.
3. **Multiple accounts per operator.** Preseen ran at least two (Preseen-Atlas, Preseen-Chestnut;
   Chestnut placed ~40th in Summer 2026 [S6]). One operator can hold several top-10 slots.

## Reference classes considered

| Class | n | Window | Base rate | Source | Kept? |
|---|---|---|---|---|---|
| Bots in the Cup top 10, per season | 4 | Summer 2025 – Summer 2026 | 1, 1, 2, **5** | [S1] background, [S4], [S5], [S6], [S7] | **yes — primary** |
| Season-to-season persistence of a bot already in the top 10 | 4 bot-seasons | Fall 2025 – Summer 2026 | 4/4 repeated (Laplace 5/6 ≈ 83%) | derived from the series | **yes — secondary** |
| New bots *entering* the top 10 per season | 3 transitions | Fall 2025 – Summer 2026 | 0, 1, 3 | derived | yes, as the additive term |
| Metaculus *baseline* bots (`metac-*`) ranked in the Cup | 3 | Summer 2025 – Spring 2026 | 37th/551, 23rd/539, 33rd/1130 | [S8] | **no** — wrong population; these are Metaculus's own template scaffolds, not the elite third-party bots. Keeping them would have badly understated the bot field. |
| FutureEval head-to-head pros vs bots | 4 quarters | Q3 2024 – Spring 2026 | pros ahead every quarter | [S10], [S11] | partly — informs the *trend*, not the count; the Cup metric is not the FutureEval metric |

**Raw base rate**: the mean of the four observed seasons is 2.25, but the series is strongly
trending (1, 1, 2, 5) and the generating process has visibly changed, so the unweighted mean is
the wrong summary. Last-value-persists (5) and persistence-with-attrition (~4.3) bracket it.

### Reconciling the two bot rank series — a trap worth recording

Two apparently contradictory sets of numbers circulate:

- "Best bot placed 37th / 23rd / 33rd" [S8] — these are **Metaculus's own baseline bots**
  (`metac-gemini-2-5-pro+asknews`, `metac-claude-4-5-sonnet…`), single-scaffold reference
  implementations.
- "ManticAI 8th / 4th / 9th / 2nd" — these are **third-party competitive bots**.

Both are true. Anyone anchoring on the first series would forecast ~0–1 and be badly wrong.

## Decomposition

Under Cup scoring the count is **not** a smooth function of average bot quality. It is
"how many individual bots clear the k-th best human", and there is a visible **tier gap**:
in Summer 2026 the five elite bots took ranks 1, 2, 5, 6, 10 — and the *sixth*-best bot was
ranked ~38th. So the count is essentially a roll-call over a short, named list.

Mechanically, if *k* bots make the top 10 then only 10−*k* humans do, so the *k*-th bot must
beat the (11−*k*)-th best human. **Each extra bot seat is more expensive than the last.**
This is the brake on the upper tail and the reason a naive linear extrapolation of 1→1→2→5
(which gives ~6–7) is wrong.

Incumbent roll-call and P(top 10 again), with the reasoning:

| Bot | Cup rank history | P(top 10, Fall 2026) | Why |
|---|---|---|---|
| laertes | 47 → 12 → **1** | 0.90 | won outright; steep improvement curve; hobby-scale compute (~150 h, ~$2k) so cheap to repeat [S15] |
| manticAI | 8 → 4 → 9 → **2** | 0.93 | only bot in the top 10 of all four Cups; $25M seed raised 2026-09-18 explicitly on this result [S16] |
| futuresearch | 61 → **5** | 0.85 | big jump, but the 61 was a *coverage* failure (51 of 297 Spring FutureEval questions) — coverage is fixable and fatal |
| cassi | 19 → 60 → **6** | 0.85 | most volatile of the five |
| preseen (Atlas) | 3 → **10** | 0.88 | commercial operator (preseen.com); but held the *marginal* seat in Summer |

Participation probabilities are deliberately high (0.85–0.93): the failure mode being priced
is "skips the Cup or loses coverage", not "forecasts badly" — bad forecasting is handled by
the score noise term.

Challenger pool (strong Summer 2026 FutureEval bots that have **not** demonstrated a
continuous-update Cup loop): acm_bot, GreeneiBot2, future-perfect-hindsight, mmBot, ana,
Preseen-Chestnut, plus unknown new entrants such as XtremeSavageForecast (started 2026-09-10
[S17]). The binding constraint on these is the *loop*, not the model. Modelled as 7 candidates,
each ~30% likely to run a Cup-grade loop, drawn from a distribution centred **below** the 10th
human.

### Monte Carlo

`scratchpad/sim.py` (kept in the session scratchpad; parameters reproduced in `forecast.md`).
Scores live on a "per-question peer score relative to the 10th-best human of Summer 2026"
scale. The human ladder shape was calibrated until the model reproduces the *observed* Summer
2026 interleaving exactly (bot, bot, human, human, bot, bot, human, human, human, bot).
200,000 draws; a common season factor couples the bots, an idiosyncratic term covers rebuilds.

Baseline: mean 4.35, median 4, IQR [4, 5].
Mixed over nine parameterisations (weights in `scratchpad/mix.py`): **mean 4.24, median 4,
IQR [3, 5]**, P(≤3) = 25.4%, P(4 or 5) = 62.2%, P(≥6) = 12.4%.

## Search log

| Date | Query / source | Finding | Effect on forecast |
|---|---|---|---|
| 2026-09-20 | `metaculus_aggregations.py 45619` | Question is **upcoming**; CP reveal 2026-09-26. **No community, Pro or gold-medalist aggregation exists yet** (all three cohorts returned empty). n=7 forecasters. | Removes the usual anchor entirely — forecast is unanchored; widens the band |
| 2026-09-20 | same, `--comments 12` | Metaculus's own background states bots took **5 of the top 10** in Summer 2026 | Fixes the key data point authoritatively |
| 2026-09-20 | same | Commenter **Theomachado** posted a full reference-class table (season, entrants, bots in top 10, elite-bot ranks and per-question deltas) and a PMF (mean 4.5) | Major input — but see "anchoring" below |
| 2026-09-20 | Rendered `tournament/metaculus-cup-fall-2026/` with Playwright | Cup runs **2026-08-28 → 2027-01-01**; first questions opened Mon 2026-09-07; **4–5 new questions every Friday**; $5,000 pool; guest forecaster Kiko Llaneras; 13 questions live | Fall will have ~70 questions vs Summer's 58 — more questions, less luck, favours the coverage-heavy side (bots). Small upward |
| 2026-09-20 | Rendered `tournament/metaculus-cup-summer-2026/` | Confirms 58 questions, closed Sep 02, winners announced Sep 05 | Corroborates the Summer data point |
| 2026-09-20 | Economist 2026-09-16 (via secondary reports; archive.is unreachable from this container) | "For the first time an AI won the seasonal Metaculus Cup… Other AIs took the second and fifth places, leaving third and fourth for humans." | Consistent with 5-of-10: 3 bots in the top 5, 2 more in 6–10 |
| 2026-09-20 | Time, 2025-09-18 | Summer 2025: Mantic 8th of ~549; first bot ever in a Cup top 10; scored >80% of top humans vs a predicted 40% | Confirms data point 1 and that the community has **under**-forecast bots before |
| 2026-09-20 | ACX, "The AI Superforecasters Are Here" | Spring 2026: top two were human, Preseen 3rd; Preseen-Chestnut fell to ~40th; bots gain ~0.9 Metaculus Elo/month; parity projected ~6 months from July 2026 | Confirms data point 3; the Fall window straddles the projected crossing → supports a positive drift term |
| 2026-09-20 | EA Forum, "AI Forecasting in 2026: What 11 Analyses Say" | Parity projections: FutureEval → Jun 2027; ForecastBench → Nov 2026 (95% CI Dec 2025 – Jan 2028). Baseline `metac-*` bot ranks 37/23/33 | Wide disagreement on timing; kept drift modest rather than aggressive |
| 2026-09-20 | EA Forum, "Q2 AI Benchmark Results: Pros Maintain Clear Lead" | Q2 2025: all 10 pros beat every bot head-to-head; best bot 11th | Historical baseline for the pro–bot gap; shows how fast it closed |
| 2026-09-20 | explainx.ai, theneuron.ai | Coverage/update-frequency is a structural bot advantage independent of forecasting skill | The key reason the Cup count runs *ahead* of accuracy parity |
| 2026-09-20 | Reuters/TechStartups/CryptoBriefing, 2026-09-18 | Mantic raised **$25M** seed (Radical Ventures, M12, Thinking Machines Lab, Balderton) directly on the Cup win | Strong upward pressure on participation probability |
| 2026-09-20 | preseen.com | Preseen is a commercial product marketing its Metaculus results; first bot to win a *human* tournament on Metaculus (26Q2, 1st of 112) | Raises Preseen's participation probability |
| 2026-09-20 | Metaculus tournament rules, scores FAQ | Bots ineligible for Cup prizes; humans may use AI assistance | Human ceiling also rises with AI assistance — counterweight |
| 2026-09-20 | Hacker News thread on the Economist piece | Confirms 58 questions; critiques are about *interpretation* (coverage advantage, reflexivity), not about the leaderboard facts | No change |
| 2026-09-20 | Searches for "Mantic withdraw / stop competing" and "Metaculus rule change exclude bots" | **Nothing found.** No announced rule change, no announced withdrawal | Absence of expected evidence for the two main tail risks → shrinks the low tail |

## Dead ends and ruled-out hypotheses

- **Metaculus leaderboard tab could not be rendered.** The tournament page's Leaderboard tab
  lazy-loads and the click target would not resolve; repeated attempts tripped a Cloudflare
  interstitial (Metaculus rate-limits by IP). The **Fall 2026 page shows no leaderboard tab at
  all** — in-progress Cups apparently do not publish one. So the single most decision-relevant
  live fact — *which bots are actually forecasting the Fall Cup right now* — could not be
  obtained. This is the first thing to retry at the next update.
- **The Metaculus leaderboard API is authenticated.** Probed from inside a loaded page
  (so a genuine browser fingerprint): `/api/projects/tournaments/<slug>/`,
  `.../leaderboard/`, `/api/leaderboards/project/?projectId=…` and `/api2/…` all return
  **403**. Only the `/api-proxy/aggregation_explorer/` surface the aggregations skill uses is
  open anonymously, and it serves question aggregations, not tournament leaderboards. Do not
  retry these paths at the next update — retry the rendered Leaderboard tab instead.
- **archive.is is unreachable from this container**, so the Economist original could not be
  read directly; its content is taken from four independent secondary reports that agree.
- **Ruled out: "bots will be excluded from the Cup leaderboard."** The question's own fine
  print explicitly includes bots in the top-10 construction, and the question was launched by
  Metaculus staff (skmmcj) for this Cup. P ≈ 1%.
- **Ruled out: the `metac-*` baseline-bot rank series as the reference class** (see above).
- **Not pursued: prediction markets.** No Kalshi, Polymarket or Manifold market on this
  question exists; checked by search, none found. Not surprising for a meta-question about a
  Metaculus tournament.

## Anchoring disclosure (important for scoring this forecast later)

The Theomachado comment was read **before** the decomposition was built, and the incumbent
per-season deltas used in the Monte Carlo are his, not independently recomputed (the
leaderboards they derive from could not be rendered). My result (mean 4.24, median 4) is
therefore **not independent** of his (mean 4.5, mode 4–5). The agreement is substantially
weaker evidence than it looks. What *is* independent: the tier-gap/marginal-seat-cost structure,
the participation-risk weighting, and the model-averaging that widened the IQR from [4,5] to
[3,5]. A future update should recompute the deltas from the raw leaderboards.

## Open questions to chase next time

1. **Which bots are live in the Fall 2026 Cup, and from which date?** Retry the leaderboard
   render; also check `laertes` (profile 277919) and `manticAI` (profile 191026) activity.
2. Did admins answer MaxA on the `symbiosis` / unflagged-bot question?
3. The CP, Pro and gold-medalist aggregations after the 2026-09-26 reveal.
4. Whether any challenger (acm_bot, GreeneiBot2, future-perfect-hindsight, mmBot, ana) is
   running a continuous-update loop on Cup questions.
5. Fall 2026 FutureEval standings — laertes was reported to be leading it [S15]; a
   confirmation would firm up laertes' probability.
