# Snake: OVERDRIVE — AI Showcase

This is an **AI-built demonstration for Connor to study and critique**. It is
not Connor's historical Snake and must not be presented as his work.

The point is to show what happens when the core Snake idea is pushed into a
different genre:

- scrolling arena larger than the viewport;
- smooth steering rather than grid movement;
- long articulated snake body;
- auto-targeting plasma weapon;
- hostile drones and elite ranged enemies;
- multi-attack boss encounters;
- health, shields and dash energy;
- collectible growth cores;
- random power-ups;
- combo multiplier;
- particles, glow, camera shake and hit flashes;
- runtime diagnostics visible on-screen.

## Run

From the repository root:

```bash
cd demos/snake-overdrive
uv run --python 3.12 python -m http.server 8002
```

Open `http://127.0.0.1:8002/`.

## Controls

- A/D or left/right — steer
- W/S or up/down — accelerate/brake
- Space — dash
- P — pause
- R — restart

Connor's original Snake history remains untouched in `snake-game/`.
