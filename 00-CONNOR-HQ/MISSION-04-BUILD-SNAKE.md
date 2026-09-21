# 🐍 Mission 4 — Explore Your Snake History

Snake is already an important part of your coding history.

This mission is not about replacing it with a cleaner AI rewrite. It is about learning how a game grows through save points.

## Goal

Run two versions of Snake and identify some of the programming ideas inside them.

## Challenge 1 — Run the current game

    cd ~/Projects/connor-coding-lab/snake-game
    uv sync
    uv run python src/snake_game/__init__.py

Play it, then close it normally.

## Challenge 2 — Run the Classic save point

    uv run python src/snake_game/classic_snake.py

Compare it with the current game.

What changed?

## Challenge 3 — Find three game ideas in the code

Open:

`snake-game/src/snake_game/classic_snake.py`

Try to find code for three of these:

- player input;
- position;
- movement;
- food;
- collision;
- score;
- the game loop.

Ask for an explanation if you need one, but point to the code yourself.

## Challenge 4 — Look at history

Return to the repository root:

    cd ~/Projects/connor-coding-lab

Then run:

    git log --oneline --all --decorate -20

Find some of the Snake save points.

## ✅ Mission complete when

You can explain one way the Classic version and the later version are different, and one programming idea both games use.

## 🏆 Reward

🏅 Game Developer
