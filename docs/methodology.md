# Methodology — how to build a forecast here

A checklist, not a ritual. Skip a step only when you can say why it does not apply.

## 0. Parse the question before anything else

- Read resolution criteria, fine print, background, and any linked methodology/data source.
- Identify the **resolution source** (which series, which publisher, which revision) and its
  **release schedule**. Many questions are decided by a data cutoff, not by the world.
- Identify the **resolution date** and whether early resolution is possible.
- Write down at least one way the question could resolve counter-intuitively
  (definitional edge cases, revisions, ties, "if no such event, resolves NO").

If the question is ambiguous *as written*, that ambiguity is part of the forecast:
put weight on the resolver's likely reading, and say so.

## 1. Outside view — reference class and base rate

- Name the reference class explicitly. How many comparable cases? Over what window?
- Compute the raw base rate. Write it in `research.md` with the source.
- Where no clean class exists, build 2–3 partial ones and note their disagreement.
- Adjust for the **time remaining**: a base rate per year must be scaled to the window.
  For a hazard-rate style event, `P ≈ 1 − exp(−λ·t)` beats a naive annual figure.
- Status-quo prior: for "will X change by date D" questions, the status quo usually wins.
  Short horizons should pull hard toward "no change".

## 2. Inside view — the causal story

- What specific mechanism produces YES? What has to happen, in what order, by when?
- Decompose: `P(YES) = P(step1) × P(step2 | step1) × …` — a Fermi-style chain often
  exposes over-confidence in a narrative.
- For multi-path events use the complement: `P(YES) = 1 − Π(1 − p_i)` over independent paths.
- Who are the actors, what are their incentives, and what have they done in similar spots?

## 3. Evidence and updating

- Start from the outside-view prior, then update with a stated likelihood ratio:
  `odds_post = odds_prior × LR`. Write the LR down even if approximate — it disciplines
  the size of updates.
- Separate **new information** from **new salience**. A story you just read is not evidence
  that the world changed.
- Ask what evidence you would expect to see if YES were true, and check whether it is absent.
  Absence of expected evidence is evidence of absence; absence of unexpected evidence is not.

## 4. Other forecasters

Pull any market prices (the Metaculus community prediction is hidden from the bot token on
almost every question, and on tournament questions until after close). Treat markets as an
informed prior held by people with skin in the game, not as noise to be corrected.

- Adjust market prices for known biases: longshot bias (low-probability contracts trade
  rich), time-value/interest drag on long-dated Polymarket contracts, low-volume noise on
  Manifold.
- A gap of > 10 percentage points against a liquid market requires an explicit, written
  justification. Most of the time you are wrong.

## 5. Scenarios and the distribution

- Sketch 3–5 mutually exclusive scenarios with weights summing to 1 and the resolution
  each implies. This is what generates the IQR (interquartile range), not vibes.
- Binary questions: the IQR expresses *uncertainty about your own probability* — how much
  a reasonable next week of evidence could move you. A well-researched, stable question
  deserves a narrow band; a question hinging on one unpredictable decision deserves a wide one.
- Numeric/date questions: give median plus 25th/75th percentiles in native units. Check the
  band against history — if the last ten years never fell inside your IQR, widen it.

## 6. Sensitivity analysis

For the 2–3 assumptions doing the most work, state how the forecast moves if they are wrong:

| Assumption | If instead | Forecast becomes |
|---|---|---|

## 7. Calibration hygiene

- Avoid 0% and 100%. Floor/ceiling at roughly 1%/99% unless resolution is mechanically settled.
- Beware round numbers as anchors; 37% is a legitimate answer.
- Check the **conjunction**: if your story requires four things, your probability should be
  lower than the least likely of them.
- Check the **scope**: does the probability change appropriately if the window doubles?
- Ask "would I take the other side of this bet at my own price?" If not, the number is wrong.

## 8. Tripwires

End with 3–6 concrete, dated, observable signals that would move the forecast, each with a
direction and rough magnitude. These become the search targets for the next update, and go
into `meta.yaml` under `tripwires:`.

Bad: "further escalation". Good: "IAEA Board of Governors resolution referring the file to
the Security Council before 2026-11-30 → +15pp".

State the magnitude in the units the forecast itself moves in, and record it in `meta.yaml`
as an unsigned `magnitude` plus an explicit `magnitude_unit` — `direction` carries the sign:

| Question type | `magnitude_unit` | Example |
|---|---|---|
| binary, multiple choice | `pp` (percentage points, 0-100) | `magnitude: 15`, `magnitude_unit: pp` |
| date | `days`, `weeks` or `months` | `magnitude: 6`, `magnitude_unit: weeks` |
| numeric, discrete | the question's own `unit:` | `magnitude: 6000`, `magnitude_unit: cases` |

Never convert a numeric magnitude into a percentage of your median to make it fit a
probability scale — the tripwire stops being readable against the forecast it moves.
A tripwire whose direction you cannot call in advance takes `direction: either` and
`magnitude: 0`; it is a trigger to re-analyse, not a signed update.

## Cognitive-bias watchlist

Availability (recent vivid news over-weighted) · narrative fallacy (a coherent story feels
more probable) · anchoring (on the first number seen, including the CP) · confirmation
(searching only for supporting evidence) · scope insensitivity · overconfidence in
resolution-criteria reading · herding on the community prediction without independent work.

**Do your own decomposition before you look at the community prediction** where practical,
then reconcile. Anchoring on the CP first destroys most of the value you could add.

## Tournament mode (one-shot bot-tournament questions)

MiniBench and the FutureEval seasons give each question a 3-hour window, allow one forecast,
hide the community prediction, and score with the spot peer score (a log score at close,
relative to the other bots). The bot gets ~25 minutes per question. The checklist shrinks to
what drives calibration; what serves a *revisitable* forecast goes:

| Kept | Why it stays |
|---|---|
| The "What resolves YES" digest, first | Misreading resolution is the commonest loss — more so on LLM-written MiniBench questions |
| Outside view with a named base rate | Without the crowd anchor, the base rate is the main defence against overconfidence |
| One deliberate disconfirming search | Cheap, and the classic failure mode of a fast forecast |
| Median, IQR, and the full distribution | The log score punishes a too-narrow numeric distribution or an extreme binary miss hardest |
| Market prices where a market exists | Public forecasts on other platforms are allowed and are the best crowd signal left |

| Dropped | Why it is safe to drop |
|---|---|
| ≥ 15 sources (now ≥ 5 cited, from ≥ 15 searches) | The marginal *cited* source rarely moves a 3-hour question; time-outs score nothing. The search floor is enforced, because sessions left to judge "enough" stopped at a median of 4 (2026-10-19) |
| Scenario and sensitivity tables | Their job is to make the next update cheap; there is no next update |
| Tripwires and `next_review` | Nothing ever comes back to the question |
| `research.md` | A log with no second reader; sources go into `forecast.md` |
| The Metaculus CP / Pro / gold comparison | Not visible to the bot |

Binary probabilities stay within [2 %, 98 %] unless the outcome is already essentially
determined by data in hand: a peer log score rewards being right with confidence only
modestly and punishes being wrong with confidence severely.
