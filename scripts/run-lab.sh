#!/usr/bin/env bash
set -euo pipefail

repo="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

open_url() {
  local url="$1"
  if command -v xdg-open >/dev/null 2>&1 && [[ -n "${DISPLAY:-}${WAYLAND_DISPLAY:-}" ]]; then
    (sleep 1; xdg-open "$url" >/dev/null 2>&1 || true) &
  fi
}

clear 2>/dev/null || true
echo "============================================================"
echo "                 CONNOR CODING LAB"
echo "============================================================"
echo
echo "Choose what you want to run:"
echo
echo "  1) Python Basics"
echo "  2) Classic Snake"
echo "  3) Campaign Snake"
echo "  4) Original Browser Snake"
echo "  5) Neon City — AI Technology Preview"
echo "  6) Snake: OVERDRIVE — AI Showcase"
echo "  7) Show My Computer"
echo "  8) Check My Environment"
echo "  q) Quit"
echo

read -r -p "Mission > " choice

case "$choice" in
  1)
    cd "$repo/python-basics"
    uv sync --locked
    uv run python src/python_basics/hello.py
    ;;
  2)
    cd "$repo/snake-game"
    uv sync --locked
    uv run python src/snake_game/classic_snake.py
    ;;
  3)
    cd "$repo/snake-game"
    uv sync --locked
    uv run python src/snake_game/__init__.py
    ;;
  4)
    cd "$repo/snake-game"
    echo "Opening Original Browser Snake at http://127.0.0.1:8000/"
    echo "Press Ctrl+C in this terminal when you are finished."
    open_url "http://127.0.0.1:8000/"
    uv run python -m http.server 8000 --directory web
    ;;
  5)
    cd "$repo/demos/neon-city-preview"
    echo "Opening Neon City preview at http://127.0.0.1:8001/"
    echo "Press Ctrl+C in this terminal when you are finished."
    open_url "http://127.0.0.1:8001/"
    uv run --python 3.12 python -m http.server 8001
    ;;
  6)
    cd "$repo/demos/snake-overdrive"
    echo "Opening Snake: OVERDRIVE at http://127.0.0.1:8002/"
    echo "Press Ctrl+C in this terminal when you are finished."
    open_url "http://127.0.0.1:8002/"
    uv run --python 3.12 python -m http.server 8002
    ;;
  7)
    "$repo/scripts/show-my-computer.sh"
    ;;
  8)
    "$repo/scripts/check-environment.sh"
    ;;
  q|Q)
    echo "See you next mission."
    ;;
  *)
    echo "That is not a menu option yet."
    exit 2
    ;;
esac
