# 🐍 Connor's Game Studio

Designed by **Lead Architect & Game Director Connor** | Built by **Antigravity**

---

## 🎮 Game Modes

### 1. 🤖 Snake: Bot Hunter (NEW EDITION!)
Hunt down AI bots, collect gold credits, and evolve into a giant mythical snake!

- **Command to play**:
  ```bash
  uv run python src/snake_game/__init__.py
  ```
- **How it works**:
  - 🍎 **Food Buffet (+1 Apple every 2s)**: The arena fills with fresh apples! Every red apple eaten makes you longer and grants **+5 Credits**!
  - ✨ **Golden Apples (Every 5s)**: Glowing, shiny golden apples spawn every 5 seconds. Snag one for an instant **+20 Credits**!
  - 🤖 **Enemy Bots**: 3 enemy bots roam the arena (Cyber-Red, Shadow-Purple, Rust-Orange).
  - ⚔️ **Combat**: Trap enemy bots so their heads slam into your body! When a bot dies, it explodes into **Glowing Gold Credits** (🪙).
  - 🪙 **Credits**: Grab the credits (+20 Credits each) to level up!
  - 🌟 **Snake Evolutions**:
    1. **Baby Viper** (Tier 1) — Green starting scout
    2. **Cobra Striker** (Tier 2, 60 Credits) — Cyan armor + instant length growth!
    3. **Titan Python** (Tier 3, 150 Credits) — Gold armor + wider, chunkier body!
    4. **Apex Dragon** (Tier 4, 300 Credits) — Giant crimson dragon with golden aura!

---

### 2. 🏛️ Save Point 1: Connor's First Coding Attempt (Classic Arcade)
The classic game you built from scratch in your first coding session!

- **Command to play**:
  ```bash
  uv run python src/snake_game/classic_snake.py
  ```
- **Features**: Classic apple collecting, solid red danger walls, speed boost every 5 apples, and high score board.

---

## 🕹️ Controls
- **Arrow Keys** or **W, A, S, D** — Steer your snake
- **Spacebar** — Instant replay when game ends
- **Esc** — Quit to desktop
