#!/bin/sh
set -eu

repo_dir=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
skill_dir="$repo_dir/skills/holiday"

fail() {
  printf 'FAIL: %s\n' "$1" >&2
  exit 1
}

[ -f "$skill_dir/SKILL.md" ] || fail 'skills/holiday/SKILL.md is missing'
[ -f "$skill_dir/references/planning-workflow.md" ] || fail 'holiday planning workflow is missing'
[ -f "$skill_dir/references/output-contract.md" ] || fail 'holiday output contract is missing'

grep -q '^name: holiday$' "$skill_dir/SKILL.md" || fail 'skill name is invalid'
grep -q '^description: Use when' "$skill_dir/SKILL.md" || fail 'trigger description is invalid'
grep -q 'references/planning-workflow.md' "$skill_dir/SKILL.md" || fail 'planning reference is not discoverable'
grep -q 'references/output-contract.md' "$skill_dir/SKILL.md" || fail 'output reference is not discoverable'
grep -q '\*\*REQUIRED SUB-SKILL:\*\* Use trip' "$skill_dir/SKILL.md" || fail 'trip dependency is not required'
grep -q '\*\*REQUIRED SUB-SKILL:\*\* Use stay' "$skill_dir/SKILL.md" || fail 'stay dependency is not required'

for phrase in EUR 'whole party' 'food allowance' 'usable destination' 'lost-time ratio' 'coherent package' 'booking order' 'trip' 'stay'; do
  grep -qi "$phrase" "$skill_dir/SKILL.md" "$skill_dir"/references/*.md ||
    fail "required rule is missing: $phrase"
done

if grep -RniE 'TODO|TBD|PLACEHOLDER' "$skill_dir"; then
  fail 'unfinished placeholder found'
fi

printf 'PASS: Holiday skill structure and invariants\n'
