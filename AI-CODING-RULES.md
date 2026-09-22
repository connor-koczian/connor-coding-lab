# AI Coding Rules

This file is the concise human-readable summary of Connor Coding Lab's AI rules.

The operational Antigravity governance lives under:

- `.agents/rules/`
- `.agents/skills/`
- root `GEMINI.md`

## Connor decides

Connor owns the product and learning decisions: what to build, why it matters, game rules, visual direction, feature order and whether the result is good.

## Antigravity may help substantially

Antigravity may explain, plan, implement, debug, test and review substantial work once the important concepts are understood.

The goal is not manual typing. The goal is that Connor can increasingly:

- explain the intent;
- direct the work;
- run it;
- verify it;
- debug failures;
- review changes;
- understand the Git save point.

## Meaningful change protocol

Before changing code:

1. state the goal;
2. identify the files;
3. explain the important concept;
4. state how success will be checked;
5. keep the scope bounded.

After changing code:

1. report exactly what changed;
2. run or state the applicable checks;
3. distinguish verified from unverified behaviour;
4. inspect the diff;
5. let Connor make meaningful decisions;
6. commit only when the save point is understandable.

## Evidence

A program starting is not proof that it behaves correctly.

Never promote AI output into Connor's demonstrated competence without evidence from Connor.

## Git

Treat `main` as stable.

Prefer:

`git status -> git diff -> specific-file git add -> git diff --cached -> git commit -> git log`

No force-push or destructive history rewriting without Geza's explicit authority.

## Python

Use each project's declared toolchain. Current Python baseline is 3.12 and the normal workflow is `uv`, not raw `pip`.

## Safety

Ordinary coding must not require `sudo`.

Never expose or commit passwords, tokens, API keys, SSH private keys, secret `.env` values or private family information.

System-level changes require the approved maintenance path.
