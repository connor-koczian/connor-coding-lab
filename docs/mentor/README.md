# Antigravity Mentor System

Antigravity is Connor's primary day-to-day teacher, pair programmer, debugger, tester and reviewer.

## Current status

**Phases 2–5 are accepted and merged into `main`. Phase 6 lab control tooling is implemented on `tooling/lab-control-v2` pending behavioural acceptance.**

The system now has three durable layers:

1. root `GEMINI.md` — project bootstrap and non-negotiable context;
2. `.agents/rules/` — persistent workspace governance;
3. `.agents/skills/` — focused task protocols and learner slash commands.

The canonical learner-state file now exists at `progress/CONNOR-MASTER-TRACKER.md`.

Phase 3 also activates `.agents/skills/update-master-tracker/SKILL.md` and integrates tracker authority into session start/finish behaviour.

Phase 4 adds the accepted VS Code cockpit. Phase 5 adds the accepted AI-native curriculum and V2 mission catalogue.

## Learner commands

- `/start`
- `/mission`
- `/build`
- `/debug`
- `/review`
- `/finish`
- `/new-project`
- `/maintenance`

These are Agent Skills, not legacy workflow files.

## Why there is no .agents/workflows directory

Official Google Antigravity documentation was re-checked on 2026-09-22.

Google states that legacy Workflows are deprecated and will be retired on 2026-11-01. Current Agent Skills are workspace-scoped under `.agents/skills/<name>/SKILL.md` and remain directly slash-invokable.

Creating new workflow files now would introduce immediate migration debt.

See `ANTIGRAVITY-V2-IMPLEMENTATION.md` for Phase 2 evidence, `MASTER-TRACKER-V1-IMPLEMENTATION.md` for Phase 3, and `VSCODE-COCKPIT-V1-IMPLEMENTATION.md` for the Phase 4 cockpit design and acceptance checks.

## Governance boundary

Antigravity may routinely update learner and project material when authorised by the active task.

It must not silently weaken or redefine root `GEMINI.md`, `.agents/rules/`, safety or change-control policy, or the V2 implementation authority.

Changes to those files require deliberate Git review.


## Phase 5 curriculum implementation

See [AI-NATIVE-CURRICULUM-V1-IMPLEMENTATION.md](AI-NATIVE-CURRICULUM-V1-IMPLEMENTATION.md) for the AI-native curriculum architecture, starter mission set and behavioural acceptance requirements.


## Phase 6 lab control implementation

See [LAB-CONTROL-V2-IMPLEMENTATION.md](LAB-CONTROL-V2-IMPLEMENTATION.md) for the learner-facing `./scripts/lab` command, transparency rules and behavioural acceptance requirements.


## Phase 7 safety, governance and CI

See [SAFETY-GOVERNANCE-CI-V1-IMPLEMENTATION.md](SAFETY-GOVERNANCE-CI-V1-IMPLEMENTATION.md) for the repository policy checks, CI design and post-merge `main` protection gate.
