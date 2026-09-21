# Git Playbook

Git is the save system for your code, but a good save point is intentional.

## Before you start

    cd ~/Projects/connor-coding-lab
    git status

Read the output before doing anything else.

## See what changed

    git diff

Never commit a change you have not looked at.

## Create a feature branch

When you are ready to practise branches:

    git switch main
    git pull --ff-only
    git switch -c mission/my-feature

Examples:

- `mission/neon-city-player`
- `mission/snake-powerup`
- `fix/snake-collision`

## Stage the files you mean to save

    git add path/to/file.py
    git status
    git diff --cached

Prefer specific files while learning. Do not default to `git add .`.

## Create a save point

    git commit -m "Add player movement"

## Look at history

    git log --oneline --decorate -10

## Commands to treat carefully

Do not use these unless you understand why and Geza has authorised the destructive ones:

    git reset --hard
    git clean -fd
    git push --force

## Useful commit messages

Good:

- `Add player movement`
- `Fix wall collision`
- `Add mission reward counter`

Weak:

- `stuff`
- `changes`
- `fix`

A commit message should tell future Connor what happened.
