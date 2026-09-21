# Mission 6 — Start Neon City

## The idea

Neon City is the proposed next flagship project: an original top-down open-world game.

It can eventually teach systems such as:

- movement;
- maps;
- collision;
- missions;
- NPCs;
- vehicles;
- credits and pickups;
- inventory;
- upgrades;
- game state;
- save/load.

It must use Connor's own names, map, characters and ideas. Do not copy GTA, Fortnite, their assets or their worlds.

## Important

This mission describes the roadmap. Do not generate the whole game.

The `neon-city/` project should be created as its own reviewed repository save point. Until that project exists, use this page for design decisions only.

## Connor is Game Director

Before coding, decide:

1. What is the player's name?
2. What does the city look like?
3. What is the first mission?
4. What can the player collect?
5. What makes the player win Mission 1?

Write the answers down before expanding the game.

## Development roadmap

### Save Point 1 — The city window

Open a Pygame window and draw a simple city background.

### Save Point 2 — Player movement

Move one character with WASD.

### Save Point 3 — Roads and buildings

Create obstacles the player cannot walk through.

### Save Point 4 — First mission

Connor chooses the actual mission.

### Later systems

Only one at a time:

- mission marker;
- credits;
- inventory;
- NPC;
- vehicle;
- map;
- arena challenge;
- save/load.

## AI pair-programming prompt

    We are working on Connor's original game Neon City.

    Connor is the Game Director.
    Work on only the next save point.

    Before changing code:
    1. explain the goal,
    2. tell me which files will change,
    3. explain the important programming idea.

    After the change:
    1. explain the code,
    2. give me the exact run/test command,
    3. help me inspect git diff,
    4. let me decide what to change or keep before we commit.

    Do not build future save points yet.

## Mission complete when

Save Point 1 runs and Connor can explain how the game window is created.
