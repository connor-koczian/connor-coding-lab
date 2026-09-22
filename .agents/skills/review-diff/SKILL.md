---
name: review-diff
description: Reviews the current Git diff with Connor for correctness, scope, risk and understanding before a save point. Use after implementation or before staging or committing.
---

# Review Diff

1. Inspect `git status` and the relevant diff.
2. Explain which files changed and why.
3. Look for unintended files, unrelated edits, secrets, broken assumptions, missing validation, unnecessary complexity and behavioural regressions.
4. Separate blocking problems from optional improvements.
5. Ask whether Connor can explain the important change at an appropriate level.
6. Stage specific files only after the diff is understood.
7. Review the staged diff again before commit.
