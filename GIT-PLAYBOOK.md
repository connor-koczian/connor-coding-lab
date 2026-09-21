# Git Playbook

Git is the save system for your code.

## Before you start

```bash
git status
```

Read the output before doing anything else.

## See what changed

```bash
git diff
```

Never commit a change you have not looked at.

## Create a feature branch

```bash
git switch main
git pull --ff-only
git switch -c mission/my-feature
```

Use short names such as:

- `mission/neon-city-player`
- `mission/snake-powerup`
- `fix/snake-collision`

## Save a checkpoint

Prefer adding the files you actually changed:

```bash
git add path/to/file.py
git status
git diff --cached
git commit -m "Add player movement"
```

## Look at history

```bash
git log --oneline --decorate -10
```

## Important rule

Do not use these unless you understand exactly why:

```text
git reset --hard
git clean -fd
git push --force
```

Ask Apa or an AI helper to explain first.

## Good commit messages

Good:

- `Add player movement`
- `Fix wall collision`
- `Add mission reward counter`

Weak:

- `stuff`
- `changes`
- `fix`

A commit message should tell future Connor what happened.
