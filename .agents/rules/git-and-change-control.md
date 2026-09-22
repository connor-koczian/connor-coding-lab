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

Imported `python-basics` and `snake-game` history must be preserved until the dedicated migration phase.
