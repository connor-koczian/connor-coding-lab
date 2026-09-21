#!/usr/bin/env bash
set -euo pipefail

repo="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
failures=0

pass() {
  printf 'PASS  %s\n' "$1"
}

fail() {
  printf 'FAIL  %s\n' "$1"
  failures=$((failures + 1))
}

echo "== Connor Coding Lab environment check =="
echo "Repository: $repo"
echo

if [[ "${EUID}" -eq 0 ]]; then
  fail "running as a normal user (currently root)"
else
  pass "running as normal user $(whoami)"
fi

if command -v git >/dev/null 2>&1; then
  pass "$(git --version)"
else
  fail "Git installed"
fi

if command -v uv >/dev/null 2>&1; then
  pass "$(uv --version)"
else
  fail "uv installed"
fi

if command -v code >/dev/null 2>&1; then
  pass "VS Code $(code --version | head -n 1)"
else
  fail "VS Code installed"
fi

if [[ -d "$repo/.git" ]]; then
  pass "Git repository present"
else
  fail "Git repository present"
fi

if [[ -z "$(git -C "$repo" status --porcelain 2>/dev/null || true)" ]]; then
  pass "working tree clean"
else
  fail "working tree clean"
fi

if [[ -n "${VIRTUAL_ENV:-}" ]]; then
  echo "WARN  active VIRTUAL_ENV=${VIRTUAL_ENV}"
  echo "      Open a clean shell or run 'deactivate' before switching projects."
fi

if command -v uv >/dev/null 2>&1; then
  if uv python find 3.12 >/dev/null 2>&1; then
    pass "Python 3.12 available through uv"
  else
    fail "Python 3.12 available through uv"
  fi
fi

echo
echo "== Python Basics =="

if (
  cd "$repo/python-basics"
  uv sync --locked >/dev/null
  uv run python --version
  uv run ruff check .
  uv run pytest
); then
  pass "Python Basics sync/lint/tests"
else
  fail "Python Basics sync/lint/tests"
fi

echo
echo "== Snake =="

if (
  cd "$repo/snake-game"
  uv sync --locked >/dev/null
  uv run python - <<'PY'
import pygame

print(f"Python/Pygame import OK: pygame {pygame.version.ver}")
PY
); then
  pass "Snake dependencies and Pygame import"
else
  fail "Snake dependencies and Pygame import"
fi

[[ -f "$repo/snake-game/src/snake_game/classic_snake.py" ]] && pass "Classic Snake source present" || fail "Classic Snake source present"
[[ -f "$repo/snake-game/src/snake_game/__init__.py" ]] && pass "campaign Snake source present" || fail "campaign Snake source present"
[[ -f "$repo/snake-game/web/index.html" ]] && pass "browser Snake present" || fail "browser Snake present"

echo
if [[ "$failures" -eq 0 ]]; then
  echo "ENVIRONMENT CHECK: PASS"
  echo "Interactive GUI checks are still required for Pygame, browser, audio and display."
  exit 0
fi

echo "ENVIRONMENT CHECK: FAIL ($failures issue(s))"
exit 1
