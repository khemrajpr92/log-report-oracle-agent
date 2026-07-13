#!/bin/bash
set -euo pipefail

# Create logs directory for Harbor
mkdir -p /logs/verifier

# Run tests with pytest-json-ctrf
pytest /tests/test_outputs.py -rA --json-report --json-report-file=/logs/verifier/ctrf.json

# Determine reward based on test result
if [ $? -eq 0 ]; then
  echo "1" > /logs/verifier/reward.txt
else
  echo "0" > /logs/verifier/reward.txt
fi
