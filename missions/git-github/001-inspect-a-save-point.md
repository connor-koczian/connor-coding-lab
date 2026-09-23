# 🌿 Mission GIT-01 — Inspect a Save Point

**Track:** Git & GitHub

## Where am I?

A working tree containing one deliberate small change, preferably produced by another mission.

## What am I learning?

Reading Git state before staging or committing.

## What do I do next?

1. Run `git status`.
2. Run `git diff -- <specific-file>`.
3. Explain what was added, removed or changed.
4. Decide whether that file belongs in the intended save point.
5. If a commit is authorised for the learner session, stage the **specific file**.
6. Inspect `git diff --cached` before any commit.
7. Propose a short commit message that explains the purpose.

## How do I run it?

Do not use `git add .` for this mission.

## How do I know it worked?

Connor can explain the difference between working-tree changes and staged changes before creating a save point.

## Connor decides

Connor decides whether the observed change belongs in the save point.

## Tracker evidence

Do **not** promote capability merely because Antigravity completed the work.

Potential evidence from this mission:

- DIRECT DEMONSTRATION: status/diff/specific staging.
- EXPLANATION: working tree versus staged state.
- DECISION: save-point membership and commit message.

## Harder challenge

Use `git log -1 --oneline` and explain how the proposed save point would differ from the current HEAD.
