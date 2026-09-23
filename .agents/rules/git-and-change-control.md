# Git and Change-Control Rule

Treat `main` as stable.

For substantive repository work:

1. inspect current branch and status;
2. update from current `main` safely;
3. create a bounded branch;
4. make one coherent change;
5. inspect `git diff`;
6. validate;
7. stage specific files;
8. inspect `git diff --cached`;
9. commit an understandable save point;
10. use a PR and review before integration.

Teach Git progressively:

`status -> diff -> specific-file add -> commit -> log -> branches -> merge -> pull/push -> PR -> review`

Prefer `git add path/to/file` over `git add .` while Connor is learning.

Do not force-push, rewrite learning history, use `git reset --hard`, or use destructive clean commands without Geza's explicit authority.

Do not commit a large change Connor cannot explain at the appropriate level.

Python Basics and Snake Game now live in independent repositories. Preserve their original Connor history and do not rewrite it. Treat each repository's `main` as stable and use its own status/diff/branch/PR workflow.


## CI and protected main

CI is independent evidence for a save point, not proof that every behaviour works.

For substantive work:

- inspect the CI result before merge;
- inspect failed steps rather than retrying blindly;
- do not bypass a required check merely to make a PR green;
- keep interactive GUI/runtime claims separate from headless CI evidence.

The intended `main` protection target is documented at `docs/governance/MAIN-BRANCH-PROTECTION.md`.

Do not weaken branch protection or required checks merely to avoid fixing a real defect.
