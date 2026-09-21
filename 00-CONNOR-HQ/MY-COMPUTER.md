# My Computer

Your coding computer is a **Dell Latitude E5550**.

It is not a new gaming laptop. That is useful: it is a real machine you can
understand, experiment on and use to learn how software turns ordinary hardware
into something interesting.

## CPU — the instruction runner

Your CPU is an **Intel Core i5-5300U**.

It has:

- 2 physical cores;
- 4 logical processors.

A CPU executes instructions. A core is like a worker that can run instructions.
Having more than one lets the computer work on several things at once.

When your game updates movement, checks collisions, runs Python and asks Linux
for files, the CPU is doing the work.

## RAM — fast working space

Your computer has **16 GB of RAM**.

RAM holds things that programs are using right now. It is much faster to work
with than long-term storage, but its contents disappear when the computer is
powered off.

16 GB is plenty for what we are learning:

- Python;
- VS Code;
- Git;
- browser games;
- Pygame;
- tests;
- small game-development projects.

## SSD — long-term storage

Your computer has a **2 TB Crucial MX500 SSD**.

This is where Linux, your code, games and other files stay when the computer is
turned off.

An SSD uses flash memory rather than a spinning magnetic disk. That makes it
much faster than an old mechanical hard drive.

Your Git repository lives on this SSD, but GitHub is a separate copy/history on
another computer somewhere else.

## GPU — drawing pixels

Your graphics processor is **Intel HD Graphics 5500**.

It is built into the CPU rather than being a powerful separate gaming graphics
card.

That means it is not designed for modern AAA games at high settings. But it is
well suited to learning:

- 2D graphics;
- Canvas browser games;
- Pygame;
- animation;
- particles;
- maps;
- simple lighting effects.

A useful developer learns to build for the hardware they actually have.

## Display

The built-in screen runs at **1920 × 1080** pixels.

That means the screen contains:

- 1,920 pixels across;
- 1,080 pixels down;
- more than two million pixels in total.

When you position something at `x = 500, y = 300` in a game, you are learning
how software maps numbers to places on a display like this.

## Network hardware

Your Dell has:

- Intel AC 7265 Wi-Fi;
- Intel I218-LM Ethernet;
- Intel Bluetooth.

Wi-Fi communicates by radio.

Ethernet sends network data through a cable.

Both ultimately move packets of data between computers.

## Operating system

The target operating system is **Ubuntu Linux**.

Linux sits between your programs and the hardware.

Your Python program does not directly know how to draw a pixel, read the SSD or
talk to Wi-Fi hardware. It asks the operating system, and Linux talks to the
hardware through drivers.

## Your user account

Your normal account is:

```text
connor
```

Your normal coding work should not need `sudo`.

That is a real software-engineering rule called **least privilege**: use only
the permissions a task actually needs.

System administration belongs to the separate administrator account.

## Your coding workspace

Your main workspace is:

```text
/home/connor/Projects/connor-coding-lab
```

Inside it, Git tracks your learning history.

A useful starting command is:

```bash
cd ~/Projects/connor-coding-lab
git status
```

## Python and uv

Python is the programming language used by your first projects.

`uv` manages Python versions, project environments and dependencies.

Instead of changing the whole computer every time a project needs a package,
each project gets its own isolated environment.

That is why commands such as this matter:

```bash
uv sync
uv run python --version
```

## Git

Git records meaningful save points in your code.

Three of the most important commands are:

```bash
git status
git diff
git log --oneline
```

Git is not just a backup system. It lets you understand **what changed, why it
changed and when it changed**.

## See the live machine

This document describes the expected machine. You can ask Linux what is
actually running right now:

```bash
cd ~/Projects/connor-coding-lab
./scripts/show-my-computer.sh
```

Compare the live output with this file.

That is one of the central habits of engineering:

> Do not guess when the computer can tell you the answer.
