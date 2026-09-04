#!/bin/sh
set -eu

repo_dir=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
skill_dir="$repo_dir/skills/stay"

fail() {
  printf 'FAIL: %s\n' "$1" >&2
  exit 1
}

[ -f "$skill_dir/SKILL.md" ] || fail 'skills/stay/SKILL.md is missing'
[ -f "$skill_dir/references/research-workflow.md" ] || fail 'stay research workflow is missing'
[ -f "$skill_dir/references/output-contract.md" ] || fail 'stay output contract is missing'

grep -q '^name: stay$' "$skill_dir/SKILL.md" || fail 'skill name is invalid'
grep -q '^description: Use when' "$skill_dir/SKILL.md" || fail 'trigger description is invalid'
grep -q 'references/research-workflow.md' "$skill_dir/SKILL.md" || fail 'research reference is not discoverable'
grep -q 'references/output-contract.md' "$skill_dir/SKILL.md" || fail 'output reference is not discoverable'

for phrase in EUR 'whole party' 'mandatory fees' 'local transport' 'day pass' zones 'lost-time ratio' 'usable destination time' 'booking URL'; do
  grep -qi "$phrase" "$skill_dir/SKILL.md" "$skill_dir"/references/*.md ||
    fail "required rule is missing: $phrase"
done

if grep -RniE 'TODO|TBD|PLACEHOLDER' "$skill_dir"; then
  fail 'unfinished placeholder found'
fi

printf 'PASS: Stay skill structure and invariants\n'
