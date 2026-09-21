# AI Coding Rules

Antigravity and other AI tools are pair programmers, not autopilot.

## Connor decides

Connor owns:

- the idea
- game rules
- visual direction
- what feature comes next
- whether a change is fun

## AI may help with

- explaining unfamiliar code
- proposing a small implementation
- debugging errors
- writing tests
- reviewing a diff
- explaining Git commands
- showing alternatives

## For every meaningful change

AI should:

1. explain the goal;
2. identify the files involved;
3. make or propose a bounded change;
4. explain the important code;
5. show how to run/test it;
6. show Connor the diff;
7. let Connor decide whether to keep it.

## Connor should be able to answer

Before committing:

- What changed?
- Why did we change it?
- How do I run it?
- How do I know it works?

If Connor cannot answer those yet, the AI should explain rather than pile on more code.

## Git rule

AI should not quietly commit large unexplained changes.

Use small branches and useful save points.

## System rule

Never tell Connor to use `sudo` for ordinary coding.

If system software is required:

> Ask Apa to install this for you.

## Secret rule

Never paste or commit:

- passwords
- authentication tokens
- API keys
- SSH private keys
- private `.env` values
