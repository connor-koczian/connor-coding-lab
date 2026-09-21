#!/usr/bin/env bash
set -euo pipefail

line() {
  printf '%-22s %s\n' "$1" "$2"
}

echo "============================================================"
echo "                 CONNOR'S COMPUTER"
echo "============================================================"
echo

if [[ -r /etc/os-release ]]; then
  # shellcheck disable=SC1091
  source /etc/os-release
  line "Operating system:" "${PRETTY_NAME:-unknown}"
fi

line "Kernel:" "$(uname -r)"
line "Computer:" "$(cat /sys/devices/virtual/dmi/id/product_name 2>/dev/null || echo unknown)"
line "Manufacturer:" "$(cat /sys/devices/virtual/dmi/id/sys_vendor 2>/dev/null || echo unknown)"

echo
echo "-- CPU ------------------------------------------------------"
if command -v lscpu >/dev/null 2>&1; then
  line "CPU:" "$(lscpu | awk -F: '/Model name/ {sub(/^[ \t]+/, "", $2); print $2; exit}')"
  line "CPU cores:" "$(lscpu | awk -F: '/Core\(s\) per socket/ {gsub(/ /, "", $2); cores=$2} /Socket\(s\)/ {gsub(/ /, "", $2); sockets=$2} END {if (cores && sockets) print cores*sockets; else print "unknown"}')"
  line "Logical CPUs:" "$(nproc)"
fi

echo
echo "-- Memory ---------------------------------------------------"
if command -v free >/dev/null 2>&1; then
  line "RAM:" "$(free -h | awk '/^Mem:/ {print $2}')"
fi

echo
echo "-- Storage --------------------------------------------------"
if command -v lsblk >/dev/null 2>&1; then
  lsblk -d -o NAME,MODEL,SIZE,ROTA,TYPE | sed 's/^/  /'
fi

echo
echo "-- Graphics -------------------------------------------------"
if command -v lspci >/dev/null 2>&1; then
  lspci | grep -Ei 'VGA|3D|Display' | sed 's/^/  /' || true
fi

if command -v xrandr >/dev/null 2>&1 && [[ -n "${DISPLAY:-}" ]]; then
  current_mode="$(xrandr --current 2>/dev/null | awk '/\*/ {print $1; exit}')"
  [[ -n "$current_mode" ]] && line "Display mode:" "$current_mode"
fi

echo
echo "-- Developer tools -----------------------------------------"
if command -v git >/dev/null 2>&1; then
  line "Git:" "$(git --version)"
else
  line "Git:" "not installed"
fi

if command -v uv >/dev/null 2>&1; then
  line "uv:" "$(uv --version)"
else
  line "uv:" "not installed"
fi

if command -v code >/dev/null 2>&1; then
  line "VS Code:" "$(code --version | head -n 1)"
else
  line "VS Code:" "not installed"
fi

if command -v uv >/dev/null 2>&1 && uv python find 3.12 >/dev/null 2>&1; then
  line "Python 3.12:" "$(uv run --python 3.12 python --version 2>&1)"
else
  line "Python 3.12:" "not installed through uv"
fi

echo
echo "-- Workspace ------------------------------------------------"
repo="${HOME}/Projects/connor-coding-lab"

if [[ -d "$repo/.git" ]]; then
  line "Repository:" "$repo"
  line "Branch:" "$(git -C "$repo" branch --show-current)"
  line "Latest save point:" "$(git -C "$repo" log -1 --pretty='%h %s')"
else
  line "Repository:" "not found at $repo"
fi

echo
echo "Tip: the computer is not magic. Each line above came from a"
echo "Linux command asking the machine about itself."
