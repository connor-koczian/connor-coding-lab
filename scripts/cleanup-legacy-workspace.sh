#!/usr/bin/env bash
set -euo pipefail

cat <<'EOF'
RETIRED: cleanup-legacy-workspace.sh must not be used after Phase 8.

Python Basics and Snake Game are now intentional independent Git repositories.
A generic archive/purge script could destroy real project repositories, so the
old cleanup behaviour has been permanently disabled.

Current expected topology:

  ~/Projects/Connor/
    connor-coding-lab/
    projects/
      python-basics/
      snake-game/

Do not delete or archive project repositories as "legacy" workspace folders.
Use current Mission Control and repository-transition documentation instead.
EOF

exit 1
