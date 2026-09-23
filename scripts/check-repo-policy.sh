#!/usr/bin/env bash
set -euo pipefail

repo="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo"

failures=0

pass() {
  printf 'PASS  %s\n' "$1"
}

fail() {
  printf 'FAIL  %s\n' "$1" >&2
  failures=$((failures + 1))
}

echo "== Connor Coding Lab repository policy =="
echo "Checks tracked-file safety and control-plane integrity."
echo "Secret values are never printed."
echo

dangerous_path() {
  local path="$1"
  local base="${path##*/}"

  case "$base" in
    .env.example|.env.sample|.env.template)
      return 1
      ;;
    .env|.env.*|*.pem|*.key|*.p12|*.pfx|id_rsa|id_ed25519|credentials.json|credentials.yaml|credentials.yml)
      return 0
      ;;
  esac

  case "$path" in
    */.ssh/*|.ssh/*)
      return 0
      ;;
  esac

  return 1
}

tracked_secret_path=0
while IFS= read -r path; do
  if dangerous_path "$path"; then
    printf 'FAIL  tracked sensitive-path candidate: %s\n' "$path" >&2
    tracked_secret_path=1
  fi
done < <(git ls-files)

if [[ "$tracked_secret_path" -eq 0 ]]; then
  pass "no tracked secret/private-key file paths"
else
  failures=$((failures + 1))
fi

private_key_files="$(git grep -I -l -E 'BEGIN ([A-Z0-9]+ )?PRIVATE KEY' -- . 2>/dev/null || true)"
if [[ -z "$private_key_files" ]]; then
  pass "no tracked private-key header detected"
else
  echo "FAIL  private-key header detected in tracked file(s):" >&2
  printf '%s\n' "$private_key_files" | sed 's/^/      /' >&2
  failures=$((failures + 1))
fi

for path in   GEMINI.md   AI-CODING-RULES.md   .agents/rules/core-mentor.md   .agents/rules/learning-model.md   .agents/rules/safety.md   .agents/rules/git-and-change-control.md   .agents/rules/project-engineering.md   .agents/rules/system-maintenance.md
do
  if [[ -f "$path" && ! -L "$path" ]]; then
    pass "control file present as regular file: $path"
  else
    fail "control file missing or symlinked: $path"
  fi
done

for path in scripts/lab scripts/run-lab.sh scripts/check-environment.sh scripts/check-repo-policy.sh; do
  mode="$(git ls-files -s -- "$path" | awk '{print $1}')"
  if [[ "$mode" == "100755" ]]; then
    pass "executable mode tracked: $path"
  else
    fail "expected tracked executable mode 100755: $path (found ${mode:-none})"
  fi
done

if [[ "$failures" -eq 0 ]]; then
  echo
  echo "REPOSITORY POLICY: PASS"
  exit 0
fi

echo
printf 'REPOSITORY POLICY: FAIL (%d issue(s))\n' "$failures" >&2
exit 1
