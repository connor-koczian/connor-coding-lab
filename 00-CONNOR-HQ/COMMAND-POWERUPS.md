# ⚡ Command Power-Ups

You do not need to memorise these. Real developers look commands up.

## Where am I?

    pwd

Shows the folder you are currently inside.

## What is here?

    ls

Shows files and folders.

## Enter a folder

    cd folder-name

Example:

    cd snake-game

## Go back one folder

    cd ..

## Return to Connor Coding Lab

    cd ~/Projects/connor-coding-lab

This command is deliberately explicit so the repository works after a fresh clone without special shell shortcuts.

## Clear the terminal

    clear

## What changed?

    git status

Then inspect the actual changes:

    git diff

## Save one intentional change

Add the specific file you changed:

    git add path/to/file

Check what will be committed:

    git diff --cached

Then create a save point:

    git commit -m "Explain what changed"

Avoid `git add .` while you are learning. It is better to know exactly what you are saving.

## Look at recent save points

    git log --oneline --decorate -10

## Run Python

From inside a Python project such as `python-basics/`:

    uv run python filename.py

## Check Python code

Where Ruff is configured:

    uv run ruff check .

## Run tests

Where tests are configured:

    uv run pytest

Tests check whether code behaves the way you expect.
