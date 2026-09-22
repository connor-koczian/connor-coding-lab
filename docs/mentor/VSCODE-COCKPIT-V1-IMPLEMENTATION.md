# VS Code Cockpit V1 — Phase 4 Implementation Record

**Phase:** 4 — VS Code / cockpit UX  
**Branch:** `ux/vscode-mission-control-v1`  
**Implementation date:** 2026-09-22  
**Canonical workspace:** `Connor-Coding-Lab.code-workspace`

## Purpose

Phase 4 turns the repository into one coherent learner cockpit rather than a folder Connor must manually reconstruct each time.

The target experience is:

`open workspace -> see Mission Control -> have terminal available -> use Antigravity -> run/test from visible tasks -> inspect Git`

The cockpit must make the normal path obvious without hiding the real tools Connor is learning.

## Workspace design

The current workspace is deliberately transitional because the historical projects have not yet been extracted into sibling repositories.

The Phase 4 workspace exposes three roots:

1. **Mission Control** — the repository control plane;
2. **Python Basics** — current historical learning project;
3. **Snake Game** — current historical game project.

Because Python Basics and Snake Game still physically live inside Mission Control, the Mission Control root hides those two child directories in Explorer/search. This avoids showing the same project twice while preserving separate project roots.

Phase 8 will perform history-preserving extraction. Phase 9 will then repoint the same workspace model to the independent sibling repositories.

No submodules are introduced.

## Terminal behaviour

The cockpit includes one automatic safe task:

`Connor Lab: Mission Control Terminal`

It:

- starts when the trusted Mission Control folder opens;
- launches Connor's normal login shell;
- starts at the Mission Control repository root;
- remains interactive;
- opens in the integrated terminal panel;
- does not install, sync, mutate, stage, commit or run project code.

The workspace sets:

- `task.allowAutomaticTasks = on`;
- `terminal.integrated.defaultLocation = view`;
- the terminal working directory to Mission Control;
- `python.terminal.activateEnvironment = false`.

The automatic-task setting is acceptable here only because the single folder-open task is deliberately non-mutating and repository governance requires review before adding another automatic task.

VS Code will not execute automatic tasks in an untrusted workspace. The repository should be trusted only after the user has verified it is the intended Connor Coding Lab checkout.

### Python environment boundary

Connor's normal terminal should be neutral Mission Control, not silently attached to one project's `.venv`.

Project execution remains explicit:

`uv run ...`

The legacy workspace setting `python.terminal.activateEnvironment = false` is committed to suppress automatic Python activation where that setting controls the Python extension.

Current VS Code Python Environments also exposes a newer user-level setting, `python-envs.terminal.autoActivationType`, which can supersede the legacy setting when configured. That setting is user-scoped rather than repository-scoped.

Therefore:

- Phase 4 does not silently rewrite Connor's global VS Code user settings;
- rehearsal must verify whether the committed workspace settings are sufficient;
- if the Python Environments extension still injects `source .../.venv/bin/activate`, the rehearsal may require one explicit Connor-user setting change to set terminal auto-activation to `off`;
- final Dell provisioning should apply that user preference deliberately if it remains required.

## Markdown / visual navigation

Normal Markdown files open in rendered Markdown Preview by default.

Markdown Git diffs remain normal source diffs so Connor can learn exactly what changed.

The cockpit keeps:

- rendered `START-HERE.md` / learning material for navigation;
- raw source view available through **Reopen Editor With...**;
- source diff view for Git review.

The manual task:

`Connor Lab: Open Start Here`

opens `START-HERE.md` in the current VS Code window. Because Markdown Preview is the default editor association, it should render visually on the tested surface.

## Git learning behaviour

The cockpit deliberately does not optimise Git away.

Workspace defaults:

- smart commit disabled;
- automatic fetch disabled;
- sync confirmation retained.

This supports the intended learning progression:

`status -> diff -> specific-file add -> commit -> log -> branches -> merge -> pull/push -> PR -> review`

Connor still has no private WebshopCompany repository access during preparation, so the cockpit must not continually trigger remote-authentication activity.

## Curated extensions

Recommended extensions are intentionally small:

- `google.google-antigravity`;
- `ms-python.python`;
- `ms-python.vscode-pylance`;
- `ms-python.vscode-python-envs`;
- `ms-python.debugpy`;
- `charliermarsh.ruff`.

Do not turn the learner machine into an extension collection.

Web/database/container tooling should be added only when later curriculum/project work requires it.

## Visible tasks

Phase 4 exposes these VS Code tasks:

- `Connor Lab: Mission Control Terminal` — automatic, safe, interactive shell;
- `Connor Lab: Open Start Here`;
- `Connor Lab: Git Status`;
- `Connor Lab: Run Menu`;
- `Python Basics: Run`;
- `Python Basics: Tests`;
- `Python Basics: Ruff`;
- `Snake: Classic`;
- `Snake: Campaign`.

The run/test tasks use each project's declared `uv` workflow.

They are shortcuts to real commands, not replacements for learning the commands.

## Safety properties

Workspace startup must not:

- run `uv sync`;
- install packages;
- invoke `sudo`;
- alter accounts or system settings;
- change Git state;
- fetch/pull/push;
- stage or commit;
- start web servers or games;
- touch the Dell lifecycle.

Only the neutral interactive terminal is automatic.

All project execution tasks are manual.

## Folder-open fallback

If the repository is opened directly as a normal folder instead of through the canonical `.code-workspace` file, `.vscode/settings.json`, `.vscode/extensions.json` and `.vscode/tasks.json` provide a reduced but compatible cockpit.

The canonical experience remains:

`Connor-Coding-Lab.code-workspace`

## Behavioural acceptance before Phase 4 merge

On the rehearsal ThinkPad:

1. fetch/check out `ux/vscode-mission-control-v1`;
2. open `Connor-Coding-Lab.code-workspace` in VS Code;
3. reload the window;
4. confirm Explorer shows **Mission Control**, **Python Basics** and **Snake Game** as distinct workspace roots without duplicated project folders under Mission Control;
5. confirm the Mission Control terminal opens automatically and is interactive;
6. confirm its working directory is the repository root;
7. confirm the terminal is neutral — no `(python-basics)` / project virtual environment should auto-activate;
8. confirm opening `START-HERE.md` produces rendered Markdown Preview by default;
9. confirm a Markdown Git diff still opens as source text/diff rather than rendered preview;
10. confirm Antigravity still discovers the workspace skills including `/start`;
11. run `Connor Lab: Git Status`;
12. run `Python Basics: Tests` and record the actual result;
13. run one Snake task only if GUI rehearsal is useful at this phase; classify it as interactive GUI validation;
14. confirm no automatic startup task mutated the repository;
15. run `git status` and inspect any diff.

If terminal auto-activation persists because the Python Environments user-level setting overrides the repository setting, record that evidence and apply the smallest explicit Connor-user configuration repair before re-testing.

Phase 4 must not be marked complete solely from static JSON inspection.


## Rehearsal checkpoint — 2026-09-22

User-observed on the rehearsal ThinkPad after opening the Phase 4 workspace:

- automatic task `Connor Lab: Mission Control Terminal` executed;
- terminal remained interactive;
- `pwd` returned `/home/connor/Projects/connor-coding-lab`;
- `SHELL=/usr/bin/zsh`;
- `VIRTUAL_ENV=<none>`;
- current branch was `ux/vscode-mission-control-v1`;
- branch tracked `origin/ux/vscode-mission-control-v1`;
- working tree was clean.

This confirms the core terminal requirement and resolves the earlier concern that VS Code/Python tooling might silently attach the Mission Control terminal to `python-basics/.venv`.

Still required before Phase 4 acceptance:

- verify the three intended Explorer roots and no duplicate nested project display;
- verify `START-HERE.md` opens in rendered Markdown Preview by default;
- verify Antigravity still discovers `/start` in the cockpit workspace;
- run `Connor Lab: Git Status`;
- run `Python Basics: Tests` and record the actual result;
- verify final Git state remains clean.

Markdown source-diff behaviour is statically configured and should be exercised if a convenient bounded diff exists; do not create permanent learner-content changes merely to satisfy this check.
