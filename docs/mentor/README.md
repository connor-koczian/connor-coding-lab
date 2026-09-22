# Antigravity Mentor System

Antigravity is Connor's primary day-to-day teacher, pair programmer, debugger, tester and reviewer.

## Current status

**Phase 2 candidate is implemented on `agent/antigravity-mentor-v1`.**

The system now has three durable layers:

1. root `GEMINI.md` — project bootstrap and non-negotiable context;
2. `.agents/rules/` — persistent workspace governance;
3. `.agents/skills/` — focused task protocols and learner slash commands.

The canonical progress tracker is deliberately **not** created here. That is Phase 3.

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

See `ANTIGRAVITY-V2-IMPLEMENTATION.md` for the evidence and acceptance checks.

## Governance boundary

Antigravity may routinely update learner and project material when authorised by the active task.

It must not silently weaken or redefine root `GEMINI.md`, `.agents/rules/`, safety or change-control policy, or the V2 implementation authority.

Changes to those files require deliberate Git review.
