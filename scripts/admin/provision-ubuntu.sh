#!/usr/bin/env bash
set -euo pipefail

if [[ "${EUID}" -ne 0 ]]; then
  echo "Run this system-provisioning script as an administrator:"
  echo "  sudo ./scripts/admin/provision-ubuntu.sh"
  exit 1
fi

if [[ ! -r /etc/os-release ]]; then
  echo "Cannot identify the operating system."
  exit 1
fi

# shellcheck disable=SC1091
source /etc/os-release

if [[ "${ID:-}" != "ubuntu" ]]; then
  echo "This script is designed for Ubuntu. Detected: ${PRETTY_NAME:-unknown}"
  exit 1
fi

echo "== Connor Coding Lab: Ubuntu system provisioning =="
echo "Operating system: ${PRETTY_NAME}"

apt update
apt install -y ca-certificates curl git gpg jq tree wget

if ! command -v code >/dev/null 2>&1; then
  echo "Installing Microsoft's official VS Code apt repository..."

  install -d -m 0755 /usr/share/keyrings

  tmp_key="$(mktemp)"
  wget -qO "$tmp_key" https://packages.microsoft.com/keys/microsoft.asc
  gpg --dearmor --yes -o /usr/share/keyrings/microsoft.gpg "$tmp_key"
  rm -f "$tmp_key"
  chmod 0644 /usr/share/keyrings/microsoft.gpg

  arch="$(dpkg --print-architecture)"

  cat >/etc/apt/sources.list.d/vscode.sources <<EOF
Types: deb
URIs: https://packages.microsoft.com/repos/code
Suites: stable
Components: main
Architectures: $arch
Signed-By: /usr/share/keyrings/microsoft.gpg
EOF

  apt update
  apt install -y code
fi

if id connor >/dev/null 2>&1; then
  install -d -m 0755 -o connor -g connor /home/connor/Projects
else
  echo
  echo "NOTE: user 'connor' does not exist yet."
  echo "Create the normal user deliberately, for example:"
  echo "  sudo adduser connor"
  echo "Do not add Connor to sudo for ordinary development."
fi

echo
echo "== Installed system tools =="
git --version
curl --version | head -n 1
code --version | head -n 1

echo
echo "System provisioning complete."
echo "Next: log in as Connor and run ./scripts/setup-connor-user.sh"
