---
description: Produce a new calibrated forecast for a question (Metaculus URL/ID or free text)
argument-hint: <metaculus-url | post-id | question text>
---

Produce a new forecast for: **$ARGUMENTS**

Load the `forecast-workflow` skill and follow it end to end. Read `docs/methodology.md` and
`docs/output-format.md` first. Create a task list.

Reminders that are easy to skip and expensive to skip:

- Read resolution criteria, fine print and top comments **before** forming a view.
- Establish the outside-view base rate before you look hard at the community prediction.
- Fetch all three Metaculus cohorts (community, Pro, gold medalists) and flag disagreement.
- ≥ 15 distinct sources, varied phrasings, actively hunting disconfirming evidence.
- Tripwires must be dated and observable.
- Write `questions/<slug>/forecast.md`, log to the ledger, refresh `INDEX.md`.

End your chat reply with the fixed summary block (Date / Forecast / Thesis) and the path to
the forecast file.
