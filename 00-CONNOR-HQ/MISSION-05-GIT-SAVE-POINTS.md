# Mission 5 — Git Save Points

## Goal

Learn how developers safely save progress.

Git is not just for uploading code. It records meaningful checkpoints and lets you inspect exactly what changed.

## Challenge 1 — Check your position

From the repository root:

    cd ~/Projects/connor-coding-lab
    git status

Explain what branch you are on and whether anything has changed.

## Challenge 2 — Create a mission branch

Before editing:

    git switch -c mission/git-save-point
    git status

A branch gives your experiment its own lane while `main` stays stable.

## Challenge 3 — Make one tiny change

Open:

`python-basics/src/python_basics/hello.py`

Make one small change that you choose.

Now inspect it:

    git diff

Read the diff before staging anything.

## Challenge 4 — Stage only your file

    git add python-basics/src/python_basics/hello.py
    git diff --cached

The staged diff is what your next commit will record.

## Challenge 5 — Commit

Choose a short message that describes your actual change:

    git commit -m "Improve favourite game question"

Then inspect history:

    git log --oneline --decorate -8

## Mission complete when

You can explain:

- what a branch is;
- what a diff shows;
- what staging means;
- what a commit records;
- why a useful commit message matters.

Reward: Git Developer Level 1
