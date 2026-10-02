#!/usr/bin/env bash

set -euo pipefail

if [ "$(id -u)" -eq 0 ]; then
  echo "The Dev Container must use a non-root development user." >&2
  exit 1
fi

test -f backend/app/main.py
test -f backend/requirements-dev.txt

command -v git >/dev/null
command -v python >/dev/null
command -v ruff >/dev/null

python -c "import fastapi"
python -m pytest --version >/dev/null
ruff --version >/dev/null

echo "Dev Container checks passed."
