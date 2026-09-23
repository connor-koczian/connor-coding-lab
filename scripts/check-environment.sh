#!/usr/bin/env bash
set -euo pipefail

repo="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

echo "Compatibility environment check: forwarding to ./scripts/lab doctor"
echo "The V2 doctor is read-only and does not silently sync or repair projects."
exec "$repo/scripts/lab" doctor
