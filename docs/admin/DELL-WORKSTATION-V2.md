# Dell Workstation V2 — Final Software and Account Design

**Phase:** 11 — Dell handover authority V2  
**Status:** design authority only; no Dell lifecycle execution  
**Target user:** `connor` as a normal non-admin account

## 1. Scope and authority

This document defines the final Connor-facing software, account and development-environment baseline to apply after the Dell is separately released by `gk-home-lab`.

It does not authorise wiping, repartitioning, BIOS changes, Ubuntu installation or any other physical-machine lifecycle action.

## 2. Final workspace topology

```text
/home/connor/Projects/Connor/
|-- connor-coding-lab/
`-- projects/
    |-- python-basics/
    `-- snake-game/
```

Each directory is an independent Git repository. There are no Git submodules.

Canonical workspace:

```text
/home/connor/Projects/Connor/connor-coding-lab/Connor-Coding-Lab.code-workspace
```

## 3. Linux account model

- daily account: `connor`;
- Connor remains a normal non-admin user;
- Geza retains a separate administrator account;
- ordinary coding must not require `sudo`;
- Antigravity must not receive unrestricted administrator/root authority.

## 4. GitHub identity

Phase 12 is complete. Connor's personal GitHub account owns the three canonical public repositories: `connor-koczian/connor-coding-lab`, `connor-koczian/python-basics` and `connor-koczian/snake-game`.

Do not leave Geza's GitHub credentials, tokens, SSH keys or browser sessions in Connor's Linux profile.

Configure the Dell Git username/email from Connor's established GitHub identity. Do not invent an email address in provisioning scripts and do not replace Connor's identity with Geza's.

## 5. VS Code account and sync

VS Code itself does not require an account.

Connor may sign VS Code into his own GitHub account for GitHub integration and optional Settings Sync.

Settings Sync is optional. If enabled:

- first establish the correct local baseline;
- review the initial merge/replace choice;
- sync Connor's settings only;
- do not import Geza's unrelated extensions or account state.

## 6. Primary AI mentor: Antigravity

Antigravity remains the intended day-to-day mentor, coding agent, debugger, tester and reviewer for Connor Coding Lab.

The repository-native control layer remains:

- root `GEMINI.md`;
- `.agents/rules/`;
- `.agents/skills/`;
- `progress/CONNOR-MASTER-TRACKER.md`.

The learner commands remain:

- `/start`
- `/mission`
- `/build`
- `/debug`
- `/review`
- `/finish`
- `/new-project`
- `/maintenance`

Do not replace this architecture with Copilot merely because Copilot is available in VS Code.

Antigravity sign-in and account authorisation are explicit deployment steps. They must use an account that is eligible under the provider's current rules at deployment time. Do not encode credentials or account workarounds in the repository.

## 7. Copilot policy

GitHub Copilot is not required for the baseline Connor environment.

Default Phase 11 decision:

- do not rely on Copilot for the learning system;
- do not purchase Copilot simply to complete the Dell build;
- if VS Code exposes Copilot UI by default and Connor is not using it, disable/hide it to reduce confusion;
- Copilot can be reconsidered later as a secondary comparison tool.

## 8. VS Code baseline

Use current stable Microsoft Visual Studio Code from Microsoft's supported Ubuntu repository.

Curated extension baseline:

- `google.google-antigravity`;
- `ms-python.python`;
- `ms-python.vscode-pylance`;
- `ms-python.vscode-python-envs`;
- `ms-python.debugpy`;
- `charliermarsh.ruff`.

Do not install a large extension collection by default.

Repository/workspace settings provide:

- the three-root cockpit;
- rendered Markdown-first navigation;
- neutral Mission Control terminal;
- no Git smart commit;
- no automatic Git fetch;
- sync confirmation;
- explicit project execution.

Connor-user VS Code settings should include:

```json
{
  "python-envs.terminal.autoActivationType": "off",
  "python-envs.alwaysUseUv": true,
  "telemetry.telemetryLevel": "off"
}
```

The neutral Mission Control terminal must not silently activate a project virtual environment.

## 9. Python and uv baseline

- project baseline: Python 3.12;
- `uv` manages Python and project environments;
- do not copy `.venv` directories between machines;
- do not use raw `pip` as the normal workflow;
- recreate project dependencies from committed metadata/lock files;
- use Ruff/pytest where the project declares them.

## 10. Git baseline

Safe global defaults:

```text
init.defaultBranch = main
pull.ff = only
```

No force-push aliases or destructive shortcuts.

Normal network Git operations authenticate as Connor against Connor-owned repositories.

## 11. What provisioning may automate

The final provisioning/user-setup path may automate:

- supported machine-level prerequisites;
- stable VS Code installation;
- `uv` installation for Connor;
- uv-managed Python 3.12;
- the curated VS Code extension set;
- safe Connor-user VS Code settings;
- target directory creation;
- static/read-only environment checks.

It must not automate:

- disk wiping or Ubuntu installation;
- private account creation;
- browser/account sign-ins;
- GitHub ownership transfer;
- credential/token creation or copying;
- administrator elevation for Connor;
- hardware acceptance claims.

## 12. Final Dell acceptance

After the physical Dell is separately released and built, prove:

1. Connor logs in as a normal user.
2. The three independent repositories exist under `~/Projects/Connor/`.
3. Remotes point to the canonical Connor-owned repositories.
4. VS Code opens the canonical multi-root workspace.
5. the neutral terminal opens with no active project venv;
6. the curated extension set is present;
7. Antigravity is available through an authorised account;
8. `/start` discovers the rules, skills and tracker;
9. `/finish` enforces evidence-based learner progress;
10. `./scripts/lab doctor` passes;
11. Python/Ruff/pytest pass;
12. Classic Snake and Campaign Snake work interactively;
13. browser Snake and showcases work;
14. ordinary work needs no `sudo`;
15. no Geza credentials remain in Connor's profile;
16. reboot -> login -> open workspace -> `/start` works without parent intervention.

## 13. Provider changes

Antigravity, VS Code and account rules can change.

At actual Dell deployment time, verify current provider documentation before sign-in or extension configuration. Do not assume this Phase 11 document overrides provider eligibility, account or licensing rules.
