# Antigravity Mentor System

Antigravity is Connor's primary day-to-day teacher, pair programmer, debugger, tester and reviewer.

## Current status

**Phase 2 is accepted and merged into `main`. Phase 3 tracker integration is implemented on `learning/master-tracker-v1` pending behavioural acceptance.**

The system now has three durable layers:

1. root `GEMINI.md` — project bootstrap and non-negotiable context;
2. `.agents/rules/` — persistent workspace governance;
3. `.agents/skills/` — focused task protocols and learner slash commands.

The canonical learner-state file now exists at `progress/CONNOR-MASTER-TRACKER.md`.

Phase 3 also activates `.agents/skills/update-master-tracker/SKILL.md` and integrates tracker authority into session start/finish behaviour.

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

See `ANTIGRAVITY-V2-IMPLEMENTATION.md` for Phase 2 evidence and `MASTER-TRACKER-V1-IMPLEMENTATION.md` for the Phase 3 evidence/update protocol and acceptance checks.

## Governance boundary

Antigravity may routinely update learner and project material when authorised by the active task.

It must not silently weaken or redefine root `GEMINI.md`, `.agents/rules/`, safety or change-control policy, or the V2 implementation authority.

Changes to those files require deliberate Git review.
