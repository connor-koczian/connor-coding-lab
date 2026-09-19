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

---

### ⏳ 10-Second Level-Up Rule!
- **Every 10 seconds** of survival, you automatically **LEVEL UP**!
- ⏳ **Live Countdown**: Watch the `NEXT LEVEL: Xs` timer tick down in real-time on your HUD!
- 📏 **Automatic Expansion**: On every level up, your snake gets:
  - **THICKER & WIDER**: Snake segments bulge larger and larger on screen!
  - **LONGER**: +4 instant bonus segments added to your tail!
  - **MORE CREDITS**: +25 bonus credits awarded instantly!
  - **MORE SCORE**: +100 level survival points!

---

### 🌟 Level Progression & Themes
As you survive and level up every 10 seconds:
- **Level 1**: 🟢 Baby Viper
- **Level 2**: 🔵 Cobra Striker (Thicker segments!)
- **Level 3**: 🟡 Golden Python (Golden scales & aura!)
- **Level 4**: 🟣 Shadow Hydra (Cosmic purple body!)
- **Level 5**: 🔴 Solar Dragon (Crimson armor & flaming aura!)
- **Level 6**: 🔷 Titan Behemoth (Heavy armor!)
- **Level 7**: 🌸 Cosmic Leviathan (Neon pink scales!)
- **Level 8**: 💎 Quantum Colossus (Diamond emerald!)
- **Level 9**: 🔮 Void Overlord (Dark obsidian & gold!)
- **Level 10+**: 🔥 **APEX OMEGA DRAGON** (Massive giant snake with pulsing cosmic aura!)

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
