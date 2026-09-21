#!/usr/bin/env bash
set -euo pipefail

if [[ "${EUID}" -eq 0 ]]; then
  echo "Do not run this script with sudo."
  echo "Log in as Connor and run it as the normal user."
  exit 1
fi

echo "== Connor Coding Lab: user setup =="
echo "User: $(whoami)"
echo "Home: ${HOME}"

mkdir -p "${HOME}/Projects"

if [[ -n "${VIRTUAL_ENV:-}" ]]; then
  echo
  echo "A virtual environment is already active:"
  echo "  ${VIRTUAL_ENV}"
  echo "This script will ignore it. Open a clean terminal before normal project work."
  unset VIRTUAL_ENV
fi

if ! command -v uv >/dev/null 2>&1; then
  echo
  echo "Installing uv into this user's home directory..."
  curl -LsSf https://astral.sh/uv/install.sh | sh
fi

export PATH="${HOME}/.local/bin:${PATH}"

echo
echo "Installing the Python 3.12 toolchain managed by uv..."
uv python install 3.12

git config --global init.defaultBranch main
git config --global pull.ff only

if command -v code >/dev/null 2>&1; then
  echo
  echo "Installing the beginner VS Code extensions..."
  code --install-extension ms-python.python >/dev/null
  code --install-extension charliermarsh.ruff >/dev/null

  echo "VS Code extensions:"
  code --list-extensions | grep -E '^(ms-python\.python|charliermarsh\.ruff)$' || true
else
  echo "WARNING: VS Code is not installed or 'code' is not on PATH."
fi

repo="${HOME}/Projects/connor-coding-lab"

echo
if [[ -d "$repo/.git" ]]; then
  echo "Repository found: $repo"
  git -C "$repo" status --short --branch
else
  echo "Repository not found at:"
  echo "  $repo"
  echo
  echo "Transfer or clone the complete repository there before acceptance testing."
  echo "Do not recreate it by copying only project folders."
fi

echo
echo "== Versions =="
git --version
uv --version
uv run --python 3.12 python --version
if command -v code >/dev/null 2>&1; then
  code --version | head -n 1
fi

echo
echo "User setup complete."
