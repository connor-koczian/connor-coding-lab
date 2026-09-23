#!/usr/bin/env bash
set -euo pipefail

repo="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

echo "Compatibility launcher: forwarding to ./scripts/lab menu"
exec "$repo/scripts/lab" menu
