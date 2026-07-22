#!/usr/bin/env bash

set -uo pipefail

mkdir -p reports

echo "Running Python dependency vulnerability scan..."

python -m pip_audit \
  -r requirements.txt \
  -f json \
  -o reports/pip-audit-report.json

exit_code=$?

if [ "$exit_code" -ne 0 ]; then
  echo "pip-audit detected one or more vulnerable dependencies."
else
  echo "pip-audit completed with no known vulnerabilities."
fi

exit "$exit_code"
