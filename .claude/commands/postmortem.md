---
description: Post-mortem of resolved tournament questions — worst forecasts plus matched controls, analysed in parallel
argument-hint: [--since YYYY-MM-DD] [--worst N] [--controls N]
---

Run a post-mortem following `docs/postmortem.md` step by step. Arguments: **$ARGUMENTS**
(defaults: everything resolved, 6 worst, 6 controls). Read `docs/postmortem.md` and the newest
`docs/postmortem-*.md` first; carry its open items forward.

1. `uv run scripts/postmortem.py report` (add `--since` if given) — read the aggregate before any
   single question.
2. `uv run scripts/postmortem.py sample --worst N --controls N --seed <today as YYYYMMDD>`. Give
   questions on the same underlying event one analyst and pull in the next worst.
3. Spawn one `general-purpose` subagent per question in **one message**, each with the analyst
   brief from `docs/postmortem.md` plus its per-question paragraph. Save the reports as they arrive.
4. Integrate yourself: verify the heaviest findings against repo files, settle disagreements with
   data, contrast failures with controls.
5. Replay any distribution-rule proposal (`uv run scripts/postmortem.py replay --detail`) before
   recommending it.
6. Write `docs/postmortem-<YYYY-MM>.md` with a ranked suggestion list (status column) and present
   the per-question answers (good / bad / better calibrated) and the ranked list to the maintainer.
   Implement only what the maintainer picks, red/green, lint and test before committing.
