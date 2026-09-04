#!/bin/sh
set -eu

repo_dir=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
test_root=$(mktemp -d)
trap 'rm -rf "$test_root"' EXIT HUP INT TERM

fail() {
  printf 'FAIL: %s\n' "$1" >&2
  exit 1
}

assert_file() {
  [ -f "$1" ] || fail "expected file: $1"
}

assert_missing() {
  [ ! -e "$1" ] || fail "expected missing path: $1"
}

run_install() {
  test_home=$1
  shift
  HOME="$test_home" sh "$repo_dir/install.sh" "$@"
}

codex_home="$test_root/codex"
mkdir -p "$codex_home"
run_install "$codex_home" --codex
for skill_name in trip stay holiday; do
  assert_file "$codex_home/.agents/skills/$skill_name/SKILL.md"
  assert_missing "$codex_home/.claude/skills/$skill_name"
done

claude_home="$test_root/claude"
mkdir -p "$claude_home"
run_install "$claude_home" --claude
for skill_name in trip stay holiday; do
  assert_file "$claude_home/.claude/skills/$skill_name/SKILL.md"
  assert_missing "$claude_home/.agents/skills/$skill_name"
done

all_home="$test_root/all"
mkdir -p "$all_home"
run_install "$all_home"
for skill_name in trip stay holiday; do
  assert_file "$all_home/.agents/skills/$skill_name/SKILL.md"
  assert_file "$all_home/.claude/skills/$skill_name/SKILL.md"
done

printf 'old installation\n' > "$all_home/.agents/skills/trip/marker.txt"
printf 'old installation\n' > "$all_home/.agents/skills/stay/marker.txt"
run_install "$all_home" --codex
for skill_name in trip stay; do
  backup_marker=$(find "$all_home/.agents/skills" -path "*/$skill_name.backup-*/marker.txt" -type f | head -n 1)
  [ -n "$backup_marker" ] || fail "existing $skill_name installation was not backed up"
  assert_file "$all_home/.agents/skills/$skill_name/SKILL.md"
done

if run_install "$test_root/invalid" --unknown >"$test_root/invalid.out" 2>&1; then
  fail 'unknown option unexpectedly succeeded'
fi
grep -q 'Unknown option' "$test_root/invalid.out" || fail 'unknown option message missing'

printf 'PASS: installer behavior\n'
