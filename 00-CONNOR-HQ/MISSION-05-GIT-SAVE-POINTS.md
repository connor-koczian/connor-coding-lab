# Mission 5 — Git Save Points

## Goal

Learn how developers safely save progress.

Git is not just for uploading code. It lets you see what changed and return to earlier save points.

## Challenge 1 — Check your position

From the repository root:

```bash
pwd
git status
```

Explain what branch you are on and whether anything has changed.

## Challenge 2 — Make one tiny change

Open `python-basics/src/python_basics/hello.py`.

Make one small change that *you* choose.

Before saving it to Git:

```bash
git diff
```

Read the diff.

## Challenge 3 — Create a branch

```bash
git switch -c mission/git-save-point
```

Check:

```bash
git status
```

## Challenge 4 — Commit

Add only the file you changed:

```bash
git add python-basics/src/python_basics/hello.py
git diff --cached
git commit -m "Improve favourite game question"
```

## Challenge 5 — Inspect history

```bash
git log --oneline --decorate -8
```

Find your new save point.

## Mission complete when

You can explain:

- what a branch is;
- what a diff shows;
- what a commit records;
- why a useful commit message matters.

Reward: Git Developer Level 1
