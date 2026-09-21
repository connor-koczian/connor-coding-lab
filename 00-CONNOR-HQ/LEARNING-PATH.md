# Connor's Learning Path

This is a progression, not a race. Build, run, break, debug and understand each level.

## Level 1 — Terminal explorer

Learn:

- `pwd`, `ls`, `cd`;
- where the repository lives;
- files versus folders;
- how to run a program.

Proof: navigate from the repository root into a project and back again.

## Level 2 — Python pilot

Home base: `python-basics/`.

Learn:

- variables;
- strings and numbers;
- `input()` and `print()`;
- conditions;
- loops;
- functions.

Proof: change a small program, predict what it will do, then run it.

## Level 3 — Git save points

Learn:

- `git status`;
- `git diff`;
- `git add <specific-file>`;
- `git diff --cached`;
- `git commit`;
- `git log`.

Proof: make one intentional change and explain what the commit recorded.

## Level 4 — Game mechanics through Snake

Use the preserved Snake history to understand:

- game loops;
- input;
- position and movement;
- collisions;
- scoring;
- state;
- timing.

Proof: compare two Snake save points and explain one mechanic.

## Level 5 — Branches

Learn:

- why `main` stays stable;
- `git switch -c`;
- one feature per branch;
- review before integration.

Proof: make a small change on a branch without changing `main`.

## Level 6 — Debugging and quality basics

Learn:

- reproduce a bug;
- read a traceback;
- use Ruff;
- understand a small pytest test;
- verify a fix.

Proof: explain what one automated check is protecting.

## Level 7 — Neon City

Start the original top-down open-world project one save point at a time:

1. window and world;
2. player movement;
3. coordinates and map;
4. collision;
5. first mission;
6. credits and pickups;
7. NPCs;
8. vehicles;
9. inventory and upgrades;
10. save/load.

The point is to learn how larger games are split into systems.

## Level 8 — Web development

Use `web-playground/` for new HTML, CSS and JavaScript experiments.

The historical browser Snake remains in `snake-game/web/` so it can be compared with the Pygame version.

## Level 9 — GitHub collaboration

Learn:

- push and pull;
- pull requests;
- review;
- issues;
- resolving feedback.

Proof: complete one bounded feature through a branch and reviewed pull request.

## Level 10 — Design your own project

Connor chooses the project and architecture.

AI may help, but Connor should be able to explain:

- what the program does;
- where the important code lives;
- how to run it;
- how to test it;
- how Git records its history.
