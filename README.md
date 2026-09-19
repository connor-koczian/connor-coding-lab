# 🐍 Connor's Game Studio

Designed by **Lead Architect & Game Director Connor** | Built by **Antigravity**

---

## 🎮 Main Game: 🍎✨ Snake — Fruit Kingdom (Single-Player Edition)

A massive single-player arena with no bots, 5 types of magical fruit, credit economy, and snake evolutions!

- **Command to play**:
  ```bash
  uv run python src/snake_game/__init__.py
  ```

### 🗺️ The Arena
- **Giant Widescreen Arena**: `1400 x 950` pixels with 2,000+ grid tiles!
- **Pure Single Player**: Relax, slither, and hunt down fruit to build the ultimate giant snake!

---

### 🍉 The Fruit Market
| Fruit | Appearance | Spawn Time | Credits | Score | Length Growth |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 🍎 **Red Apple** | Classic Red | Every 1.5s | **+5 CR** | +10 pts | +1 segment |
| ✨ **Golden Apple** | Radiant Gold & Sparkle | Every 5s | **+20 CR** | +50 pts | +2 segments |
| 🍇 **Cosmic Berry** | Deep Purple & Cyan | Every 7s | **+15 CR** | +35 pts | +1 segment |
| 🍉 **Mega Watermelon** | Green Rind & Pink Core | Every 11s | **+40 CR** | +100 pts | +3 segments! |
| 💎 **Diamond Star Fruit** | Glowing Cyan Diamond | Every 18s | **+80 CR** | +250 pts | +4 segments! |

---

### 🌟 Snake Evolution Tiers
Watch your snake grow **visibly wider and thicker** with custom color palettes and glowing armor:

1. 🟢 **Tier 1: Baby Viper** (0 Credits) — Agile green starter snake
2. 🔵 **Tier 2: Cobra Striker** (80 Credits) — Cyan armor + thicker body
3. 🟡 **Tier 3: Golden Python** (200 Credits) — Metallic gold scales + glowing aura
4. 🟣 **Tier 4: Shadow Hydra** (450 Credits) — Cosmic purple scales
5. 🔴 **Tier 5: Mythic Solar Dragon** (800 Credits) — Giant crimson beast with radiant golden aura!

---

### 🕹️ Controls
- **Arrow Keys** or **W, A, S, D** — Steer your snake
- **Spacebar** — Instant replay when game ends
- **Esc** — Quit to desktop

---

### 🏛️ Classic Save Point (First Coding Attempt)
To play your very first classic arcade game:
```bash
uv run python src/snake_game/classic_snake.py
```
