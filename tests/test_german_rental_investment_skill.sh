#!/bin/sh
set -eu
repo_dir=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
skill="$repo_dir/skills/german-rental-investment"
test -f "$skill/SKILL.md"
grep -q '^name: german-rental-investment$' "$skill/SKILL.md"
for file in discovery-and-market legal-and-tax underwriting-and-risk output-contract private-portfolio-schema; do
  test -f "$skill/references/$file.md"
done
test -f "$skill/scripts/underwrite.py"
test -f "$skill/examples/synthetic-deal.json"
python3 "$repo_dir/tests/test_german_rental_investment.py"
printf 'PASS: German rental investment skill and underwriting invariants\n'
