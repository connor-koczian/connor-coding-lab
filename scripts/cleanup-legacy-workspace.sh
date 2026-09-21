#!/usr/bin/env bash
set -euo pipefail

projects="${HOME}/Projects"
repo="$projects/connor-coding-lab"
mode="archive"
confirmed="no"

usage() {
  cat <<'EOF'
Usage:
  ./scripts/cleanup-legacy-workspace.sh
  ./scripts/cleanup-legacy-workspace.sh --purge --yes

Default behaviour archives the old pre-monorepo folders under ~/Archive.

--purge --yes permanently deletes only the explicitly recognised legacy
entries after verifying that ~/Projects/connor-coding-lab exists.
EOF
}

while [[ "$#" -gt 0 ]]; do
  case "$1" in
    --purge)
      mode="purge"
      ;;
    --yes)
      confirmed="yes"
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "Unknown argument: $1"
      usage
      exit 2
      ;;
  esac
  shift
done

if [[ ! -d "$repo/.git" ]]; then
  echo "STOP: $repo is not a Git repository."
  echo "The consolidated monorepo must exist before legacy cleanup."
  exit 1
fi

required=("00-CONNOR-HQ" "python-basics" "snake-game")

for entry in "${required[@]}"; do
  if [[ ! -e "$repo/$entry" ]]; then
    echo "STOP: monorepo is missing $entry"
    exit 1
  fi
done

legacy=(
  "00-CONNOR-HQ"
  "experiments"
  "GEMINI.md"
  "python-basics"
  "snake-game"
  "web-playground"
)

present=()
for entry in "${legacy[@]}"; do
  if [[ -e "$projects/$entry" ]]; then
    present+=("$entry")
  fi
done

if [[ "${#present[@]}" -eq 0 ]]; then
  echo "No recognised pre-monorepo entries remain under $projects."
  exit 0
fi

echo "Consolidated repository:"
echo "  $repo"
echo
echo "Recognised legacy entries:"
printf '  %s\n' "${present[@]}"
echo

if [[ "$mode" == "purge" ]]; then
  if [[ "$confirmed" != "yes" ]]; then
    echo "STOP: permanent deletion requires both --purge and --yes."
    exit 1
  fi

  for entry in "${present[@]}"; do
    rm -rf -- "$projects/$entry"
  done

  echo "Legacy entries permanently removed."
  exit 0
fi

stamp="$(date +%Y%m%d-%H%M%S)"
archive="${HOME}/Archive/connor-pre-monorepo-$stamp"
mkdir -p "$archive"

for entry in "${present[@]}"; do
  mv -- "$projects/$entry" "$archive/"
done

echo "Legacy entries archived to:"
echo "  $archive"
echo
echo "After you have verified the monorepo contains everything you need,"
echo "the archive can be deleted deliberately."
