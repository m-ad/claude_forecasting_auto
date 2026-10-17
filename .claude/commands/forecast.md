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
- The Metaculus community prediction is hidden from the bot token; use prediction markets as the crowd check.
- A bot-tournament question is not for `/forecast`: it is forecast once, unattended, by the sweep.
- ≥ 15 distinct sources, varied phrasings, actively hunting disconfirming evidence.
- Tripwires must be dated and observable.
- Write `questions/<slug>/forecast.md`, log to the ledger, refresh `INDEX.md`.

End your chat reply with the fixed summary block (Question link / Date / Forecast / Thesis; the clickable
`**Question**: [title](url)` line comes first) and the path to
the forecast file.
