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

workspace_root="${HOME}/Projects/Connor"
repo="${workspace_root}/connor-coding-lab"
projects_root="${workspace_root}/projects"

mkdir -p "${projects_root}"

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
  echo "Installing the curated VS Code extensions..."
  code --install-extension google.google-antigravity >/dev/null || {
    echo "WARNING: Antigravity extension installation failed."
    echo "Install/authorise it manually using the current supported provider flow."
  }
  code --install-extension ms-python.python >/dev/null
  code --install-extension ms-python.vscode-pylance >/dev/null
  code --install-extension ms-python.vscode-python-envs >/dev/null
  code --install-extension ms-python.debugpy >/dev/null
  code --install-extension charliermarsh.ruff >/dev/null

  if command -v jq >/dev/null 2>&1; then
    settings_dir="${HOME}/.config/Code/User"
    settings_file="${settings_dir}/settings.json"
    mkdir -p "${settings_dir}"

    if [[ ! -f "${settings_file}" ]]; then
      printf '{}\n' >"${settings_file}"
    fi

    tmp_settings="$(mktemp)"
    jq '
      .["python-envs.terminal.autoActivationType"] = "off"
      | .["python-envs.alwaysUseUv"] = true
      | .["telemetry.telemetryLevel"] = "off"
    ' "${settings_file}" >"${tmp_settings}"
    mv "${tmp_settings}" "${settings_file}"
  else
    echo "WARNING: jq is unavailable; VS Code user settings were not updated."
  fi

  echo "VS Code extensions:"
  code --list-extensions | grep -E '^(google\.google-antigravity|ms-python\.python|ms-python\.vscode-pylance|ms-python\.vscode-python-envs|ms-python\.debugpy|charliermarsh\.ruff)$' || true
else
  echo "WARNING: VS Code is not installed or 'code' is not on PATH."
fi

echo
if [[ -d "${repo}/.git" ]]; then
  echo "Mission Control found: ${repo}"
  git -C "${repo}" status --short --branch
else
  echo "Mission Control not found at:"
  echo "  ${repo}"
  echo
  echo "Clone the final repositories into the approved multi-repository topology before acceptance."
fi

for project in python-basics snake-game; do
  project_repo="${projects_root}/${project}"
  if [[ -d "${project_repo}/.git" ]]; then
    echo "Project found: ${project_repo}"
    git -C "${project_repo}" status --short --branch
  else
    echo "Project not found yet: ${project_repo}"
  fi
done

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
echo "Next: open the canonical workspace:"
echo "  ${repo}/Connor-Coding-Lab.code-workspace"
echo "Then complete the Antigravity sign-in/authorisation step using an eligible account under the provider's current rules."
