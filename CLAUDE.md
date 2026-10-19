@AGENTS.md

## Claude Code specifics

- Project skills live in `.claude/skills/`; slash commands in `.claude/commands/`.
  `SKILLS.md` is the index — read it if you are unsure which skill applies.
- Slash commands: `/forecast`, `/update`, `/resolve`, `/status`.
- Long research runs: spawn subagents for independent evidence streams (e.g. one per
  scenario branch or per data source), then integrate yourself. Do **not** delegate
  the final probability judgement — integration is where calibration lives. In tournament
  mode use the `research-scout` subagent (`.claude/agents/`): up to eight per question,
  spawned in one message so they run in parallel.
- Use the TodoWrite/task list for any interactive forecast: the workflow has ≥ 6 steps.

## Running unattended (CI)

The `tournament-sweep` workflow starts `claude -p` once per tournament question with
`.claude/settings.ci.json` (permission mode `dontAsk`: anything not allowlisted is denied).
In that session:

- Follow `.claude/skills/tournament-forecast/SKILL.md`. Its seven budget rules are binding.
- You hold no Metaculus token and no push credential, by design. The workflow submits,
  records usage and commits after you exit. Never try to do any of the three yourself.
- `$FORECAST_DEADLINE` is when the session is killed. Log the forecast before it.

Configuration lives in repository secrets and variables, not code; every one, with its
default and whether it is required, is in `docs/configuration.md`. When something breaks,
`docs/runbook.md`.

## Git

- The bot's commits to `main` are made by `scripts/ci_commit.sh` in the workflows, never by
  the model. An interactive session never runs `git commit` unless asked (an explicit
  instruction to commit and push — e.g. from a harness running you on a feature branch —
  is such a request).
- **Lint and test before every commit.** Any workflow that edits files in the repo
  (`/forecast`, `/update`, `/resolve`, and anything else that touches `questions/`,
  `scripts/`, or the ledger) must run both, in this repo's root, right before staging:

  ```bash
  uv run ruff check .
  uv run pytest -q
  ```

  Fix failures — including pre-existing ones your change now touches — before
  committing. Never commit with either red; this is what CI (`.github/workflows/tests.yml`)
  checks on every push, and a red commit on a feature branch you push directly is not
  caught by anything else.
- **Rebase before every push.** The remote moves under you: other sessions and merged
  PRs land on `main` while a long forecast run is in progress.

  ```bash
  git pull --rebase origin <branch>       # or: git fetch origin && git rebase origin/main
  git push -u origin <branch>
  ```

  Conflicts in `ledger/forecasts.jsonl` are append-only by construction: keep **both**
  sides, in timestamp order. Never resolve a ledger conflict by dropping a line — rule 8
  (never edit or delete a past forecast) applies to conflict resolution too.
- Push failures that look like network errors: retry up to 4 times with exponential
  backoff (2s, 4s, 8s, 16s) before concluding the push is blocked.

### Fallback: push via the GitHub MCP server

If `git push` still fails after those retries — auth failure, 403/407 from the proxy, no
credential helper, remote rejected — do **not** leave the work sitting in the container.
The container is ephemeral; an unpushed forecast is a lost forecast. Fall back to the
GitHub MCP tools (`mcp__github__*`), which authenticate independently of git:

1. `mcp__github__create_branch` — only if the branch does not exist on the remote yet
   (`owner: m-ad`, `repo: claude_forecasting_auto`, `from_branch: main`).
2. `mcp__github__push_files` — all changed files in one commit. Pass each file's full
   post-edit content, not a diff. This is the right tool for a forecast: `meta.yaml`,
   `forecast.md`, `research.md`, `raw/*.json` and the ledger file go in a single call.
   Use `mcp__github__create_or_update_file` only for a genuine one-file change; it needs
   the existing blob SHA (`git rev-parse <branch>:<path>`).
3. Re-sync the local checkout so it does not diverge from what you pushed:
   `git fetch origin <branch> && git reset --hard origin/<branch>`.

Know the limits before relying on it:

- `push_files` **cannot delete or rename files** — it only creates and updates. A change
  that removes a file needs a working `git push`; say so rather than pushing a partial
  state.
- Binary files cannot be sent as text content. The repo generates none by design
  (AGENTS.md §7: no charts), so this only bites if something new starts writing them.
- The commit lands with the GitHub App as committer, not the local git identity.
- `push_files` commits against the remote tip, so a rebase is not a substitute for
  re-reading files another session may have changed — re-fetch before you build the
  payload if the branch moved.

Say which path succeeded — `git push` or the MCP fallback — in the summary you give the
maintainer, along with anything the fallback could not carry.
