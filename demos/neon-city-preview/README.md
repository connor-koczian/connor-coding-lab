# Neon City — AI Technology Preview

This is an **AI-built demonstration for Connor to explore**. It is deliberately
not Connor's real `neon-city/` project and must never be presented as work he
created.

It exists to demonstrate where the skills he is beginning to learn can lead.

## Features

- world larger than the screen with a following camera;
- on-foot movement;
- enter/exit vehicle;
- arcade acceleration, braking, steering and boost;
- building collisions;
- moving traffic;
- simple pedestrians;
- two-stage delivery mission;
- collectible data shards;
- credits, minimap and speedometer;
- particles, screen shake, rain and generated sound;
- no external art assets or game framework.

## Run

From the repository root:

```bash
cd demos/neon-city-preview
uv run --python 3.12 python -m http.server 8000
```

Open `http://127.0.0.1:8000/`.

## Controls

- WASD / arrows — walk or drive
- E — enter/exit the cyan car
- Shift — boost while driving
- P — pause
- R — reset

Connor's eventual real `neon-city/` project starts much smaller. Connor decides
its world, missions, characters, vehicles and direction.
