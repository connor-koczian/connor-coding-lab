# 📈 Progress

This directory contains Connor's canonical learner-state record.

## Canonical tracker

The single current learner-state file is:

[`CONNOR-MASTER-TRACKER.md`](CONNOR-MASTER-TRACKER.md)

Connor is **not** expected to maintain it manually. Antigravity updates it after meaningful learner sessions using evidence from Connor's own explanations, decisions, execution, debugging and verification.

## What the tracker is not

It is not:

- a score for how much AI-generated code exists;
- a list of every project feature;
- a claim that Connor completed a mission because the mission file exists;
- a second curriculum;
- a reward system that automatically promotes skills.

## Evidence standard

AI output and repository artefacts may provide context, but they are not sufficient learner evidence by themselves.

The tracker distinguishes:

- NOT STARTED;
- INTRODUCED;
- GUIDED;
- CAN EXPLAIN;
- CAN USE;
- CAN DIRECT AI;
- CAN VERIFY AI;
- INDEPENDENT.

`CAN DIRECT AI` and `CAN VERIFY AI` are deliberately separate.

The detailed update protocol is implemented by:

- `.agents/skills/update-master-tracker/SKILL.md`;
- `docs/mentor/MASTER-TRACKER-V1-IMPLEMENTATION.md`.

## Normal session flow

At session start, Antigravity reads the tracker before making claims about Connor's current level.

At session end, Antigravity:

1. reviews what Connor personally demonstrated;
2. separates learner evidence from AI execution;
3. updates only materially affected tracker sections;
4. preserves uncertainty;
5. inspects the tracker diff;
6. records one concise session-log entry when warranted.

A meaningful session may legitimately leave the tracker unchanged if it produced no new learner evidence.
