#!/usr/bin/env bash

set -uo pipefail

mkdir -p reports

echo "Running Bandit static security scan..."

bandit \
  -r app \
  -c pyproject.toml \
  -f json \
  -o reports/bandit-report.json

exit_code=$?

if [ "$exit_code" -ne 0 ]; then
  echo "Bandit detected one or more security findings."
else
  echo "Bandit scan completed with no findings."
fi

exit "$exit_code"
