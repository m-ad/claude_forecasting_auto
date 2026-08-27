@AGENTS.md

## Claude Code specifics

- Project skills live in `.claude/skills/`; slash commands in `.claude/commands/`.
  `SKILLS.md` is the index — read it if you are unsure which skill applies.
- Slash commands: `/forecast`, `/update`, `/resolve`, `/status`, `/review`.
- Long research runs: spawn subagents for independent evidence streams (e.g. one per
  scenario branch or per data source), then integrate yourself. Do **not** delegate
  the final probability judgement — integration is where calibration lives.
- Use the TodoWrite/task list for any forecast: the workflow has ≥ 6 steps.
- Never `git commit` unless asked. Committing forecasts is the operator's call.
