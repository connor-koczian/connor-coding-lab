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

The canonical VS Code workspace is:

```text
/home/connor/Projects/Connor/connor-coding-lab/Connor-Coding-Lab.code-workspace
```

## 3. Accounts and identities

### Linux

- daily account: `connor`;
- Connor is not in the sudo group for ordinary development;
- Geza retains a separate administrator account;
- ordinary coding must not require administrator privileges.

### GitHub

Connor uses his own personal GitHub account after Phase 12 ownership handover.

Do not leave Geza's GitHub credentials, tokens, SSH keys or browser sessions in Connor's profile.

Git identity must be configured to Connor's own chosen GitHub identity during Phase 12. Do not invent an email address in provisioning scripts.

### VS Code sign-in

VS Code itself does not require an account.

After Phase 12, sign VS Code into Connor's own GitHub account so GitHub authentication, Copilot and optional Settings Sync belong to Connor rather than Geza.

Settings Sync is optional. If enabled, enable it only after the local baseline is correct and review the initial merge/replace choice deliberately.

## 4. AI mentor platform

### Current approved surface: GitHub Copilot in VS Code

Google's current published Antigravity eligibility excludes under-18 users. Connor must therefore not be signed into Antigravity or use another person's Google account as a workaround.

The current supported mentor surface is GitHub Copilot in VS Code.

Current VS Code releases ship Copilot Chat as a built-in AI surface. The repository's portable AI control layer is:

- root `AGENTS.md`;
- `.agents/rules/`;
- `.agents/skills/`;
- `progress/CONNOR-MASTER-TRACKER.md`.

Current VS Code Copilot supports Agent Skills from `.agents/skills/`, including slash-command invocation. This preserves the intended `/start`, `/mission`, `/build`, `/debug`, `/review`, `/finish`, `/new-project` and `/maintenance` model.

### Copilot plan

Preferred:

1. Connor owns a normal GitHub personal account.
2. Apply for GitHub Education if his current school evidence meets GitHub's requirements.
3. If verified, activate Copilot Student.
4. If verification is pending or unavailable, Copilot Free is an acceptable baseline subject to its usage limits.
5. Do not purchase a paid Copilot plan merely to complete the Dell build.

### AI privacy and telemetry baseline

For Connor's VS Code user profile:

- set `telemetry.telemetryLevel` to `off`;
- review Copilot account privacy/policy controls under Connor's own GitHub account;
- do not connect unnecessary MCP servers or external services;
- never provide secrets or private family information to an AI tool;
- keep provider/model choice subordinate to repository evidence and safety rules.

## 5. VS Code baseline

Use current stable Microsoft Visual Studio Code from Microsoft's supported Ubuntu repository.

Repository/workspace settings remain authoritative for the cockpit:

- three workspace roots;
- rendered Markdown-first navigation;
- neutral Mission Control terminal;
- no Git smart commit;
- no automatic Git fetch;
- sync confirmation;
- manual project execution through explicit tasks/commands.

### Python extensions

Curated extension set:

- Microsoft Python;
- Pylance;
- Python Environments;
- Python Debugger;
- Ruff.

Do not install a large extension collection by default.

### Python terminal policy

Set the Connor-user setting:

```json
"python-envs.terminal.autoActivationType": "off"
```

This is user-scoped in current VS Code and prevents the Python Environments extension from silently activating one project's environment in the neutral Mission Control terminal.

Also set:

```json
"python-envs.alwaysUseUv": true
```

Project execution remains explicit with `uv run ...`.

## 6. Python/tooling baseline

- project baseline: Python 3.12;
- Python installed/managed through `uv`;
- no copied `.venv` directories;
- no raw `pip` as the normal workflow;
- project dependencies recreated from committed project metadata/lock files;
- Ruff/pytest used where declared by the project.

## 7. Git baseline

Global safe defaults for Connor:

```text
init.defaultBranch = main
pull.ff = only
```

Do not globally configure destructive shortcuts or force-push aliases.

After Phase 12, normal Git network operations must authenticate as Connor. Until ownership handover, temporary WebshopCompany access remains an admin/preparation concern and must not become Connor's long-term credential model.

## 8. What provisioning may automate

The final provisioning/user-setup path may automate:

- supported system prerequisites;
- current stable VS Code installation;
- `uv` installation for Connor;
- uv-managed Python 3.12;
- curated Python/Ruff VS Code extensions;
- safe Connor-user VS Code settings;
- target directory creation;
- static/read-only environment checks.

It must not automate:

- disk wiping or Ubuntu installation;
- GitHub account creation;
- GitHub Education verification;
- Copilot Student activation;
- browser sign-ins;
- repository ownership transfer;
- secret/token creation or copying;
- administrator elevation for Connor;
- acceptance claims that require GUI/hardware observation.

## 9. Dell acceptance after separate release

After the physical build is authorised and completed, acceptance must prove:

1. Connor logs in as a normal user.
2. The three-repository topology exists.
3. All remotes point to Connor-owned repositories after Phase 12.
4. VS Code opens the canonical multi-root workspace.
5. the neutral terminal opens with no active project venv;
6. the curated extensions are present;
7. Connor is signed into his own GitHub account;
8. Copilot is available under Connor's own eligible plan;
9. `/start` discovers the repository skills and tracker;
10. `/finish` applies evidence rules correctly;
11. `./scripts/lab doctor` passes;
12. Python/Ruff/pytest pass;
13. Classic Snake and Campaign Snake work interactively;
14. browser Snake and showcases work;
15. no ordinary workflow requires `sudo`;
16. no Geza credentials remain in Connor's user profile;
17. reboot -> login -> open workspace -> `/start` works without parent intervention.

## 10. Future Antigravity reconsideration

If Google later changes Antigravity eligibility so Connor can legitimately use it, reassess it against the current repository and provider terms at that future date.

Do not assume future eligibility from this document.
