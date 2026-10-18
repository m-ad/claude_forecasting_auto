# Update protocol

> **One-shot tournament questions are out of scope.** A question with
> `tournament.mode: one_shot` takes exactly one forecast and is never updated (Metaculus bot
> tournament rule; see `docs/tournament-protocol.md`). Its resolution is recorded by the daily
> `tournament-sync` workflow, not by `/resolve`.

A forecast that is never revisited is a guess with a timestamp. This repo treats updating
as a first-class workflow with its own trigger, its own checklist, and its own record.

## When to update

`uv run scripts/status.py` ranks open questions by urgency. Update when **any** holds:

| Trigger | Rule of thumb |
|---|---|
| `next_review` date reached | set explicitly at forecast time; default below |
| A tripwire fired | check the news feed for the signals listed in `meta.yaml` |
| Community moved | Metaculus CP moved > 5 pp (percentage points), or > 1/3 of the gap between you and CP closed/opened |
| Resolution approaching | at T−30d, T−7d, T−1d for questions still live |
| Manual request (development, debugging) | `/update <slug>` |

Default `next_review` cadence, set by time-to-resolution at the moment of forecasting:

| Time to resolution | Review every |
|---|---|
| < 2 weeks | 2 days |
| 2–8 weeks | 1 week |
| 2–6 months | 2 weeks |
| 6–24 months | 1 month |
| > 24 months | 3 months |

Shorten it when the question is news-driven; lengthen it when resolution depends on a single
scheduled release (then just review shortly before the release).

## The update checklist

1. **Read the previous version first** — the prior median/IQR, the thesis, and above all the
   tripwire list. That list is your search plan.
2. **Search specifically for the tripwires**, by name and date, before general news search.
   Record each as fired / not fired / partially fired.
3. **Re-fetch the live numbers**: the Metaculus question text (criteria get edited), market
   prices, the underlying data series. Snapshot into `raw/` with today's date in the filename.
4. **Distinguish new evidence from no evidence.** "Nothing happened" is informative: for a
   question requiring an event, elapsed quiet time *lowers* the probability mechanically.
   An update that changes nothing is a valid update — write it down as such with the reason.
5. **Update as a Bayesian**: prior = your last forecast, not the community's. State the
   likelihood ratio for each driver.
6. **Consider a de-novo re-analysis instead of an incremental update** when:
   - the market/CP contradicts you by > 10 pp and you cannot name why;
   - > 3 months or > 1/3 of the remaining time has passed since the last version;
   - the question's structure changed (criteria clarified, resolution source changed);
   - your last two updates moved in the same direction (a sign of anchoring on your own prior
     and drifting rather than re-deriving).
   Say explicitly in the version header which mode you used: `Update` or `Re-analysis`.
7. **Prepend** the new version to `forecast.md`, rewrite the header block, update
   `meta.yaml` (`current`, `next_review`, `tripwires`), and log to the ledger.

## Anti-patterns

- Nudging the number toward the CP without new evidence. That is herding, not updating.
- Excessive volatility: moving 20 pp on a single news article. Ask for the likelihood ratio.
- Excessive stickiness: refusing to move because you wrote a persuasive thesis last month.
  Sunk-cost applies to arguments too.
- Rewriting history. Old versions stay exactly as they were, errors included.

## Resolution

When a question resolves:

**Metaculus questions resolve only on Metaculus's own posted resolution.** Look it up; do not
infer it from the event. If it is not posted yet, do not run `log_forecast.py resolve`.

```bash
uv run scripts/log_forecast.py resolve <slug> --outcome yes        # binary
uv run scripts/log_forecast.py resolve <slug> --outcome 87.4       # numeric
uv run scripts/log_forecast.py resolve <slug> --outcome 2031-03-31 # date, stored as Unix seconds
uv run scripts/log_forecast.py resolve <slug> --outcome "Labour Party"  # multiple choice
```

A multiple-choice outcome is the **exact option label**, stored verbatim (an option named `"0"`
stays the string `"0"`). `log_forecast.py` refuses a label that is not among the question's
options.

A binary outcome must be yes or no; `log_forecast.py` refuses anything else. An annulled
question is dropped, not resolved — see [below](#annulled-or-ambiguous-questions).

Then append a short **post-mortem** section to `forecast.md`:

- What actually happened, and via which resolution source.
- Which version was closest, and what the Brier score was for each version.
- **Which tripwire should have existed and did not.** This is the highest-value line in
  the whole repo — it is the only part that improves future forecasts.
- Whether the community beat you, and on what.

`uv run scripts/calibration.py` then recomputes the calibration record across all resolved
questions: Brier score, log score, calibration-by-bucket, and skill relative to the Metaculus
community prediction at the same timestamps. Multiple-choice versions are scored with the
multi-class Brier score and the log score from their recorded option vector; versions logged
without one (before the ledger had a `distribution` field) are listed as not scored.

## Annulled or ambiguous questions

An annulled question (Metaculus "annulled" or "ambiguous") has no outcome to score, so it is
**not** a resolution: do not run `log_forecast.py resolve`. Instead:

1. In `meta.yaml` set `status: dropped` and `next_review: null`, and leave the `resolution`
   block null.
2. Append an `## Annulled — <date>` note to `forecast.md`, citing Metaculus's annulment, and
   set the header's Status row to `dropped`.
3. Leave the ledger alone. The forecast versions stay as they are and go unscored:
   `calibration.py` scores only slugs with a resolution record, and `status.py` stops
   listing the question.

## Automating the cadence

Run the triage on a schedule and let it tell you what is stale:

```bash
# weekly, non-interactive
claude -p "/status --act" --permission-mode acceptEdits
```

`--act` tells the agent to actually run the due updates rather than only listing them.
Start with the listing mode until you trust it.
