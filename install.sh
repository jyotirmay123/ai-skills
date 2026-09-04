#!/bin/sh
set -eu

repo_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
skills_dir="$repo_dir/skills"
platform=${1:---all}

usage() {
  cat <<'EOF'
Usage: sh install.sh [--all | --codex | --claude]

  --all      Install every bundled skill for Codex and Claude Code (default)
  --codex    Install every bundled skill to ~/.agents/skills
  --claude   Install every bundled skill to ~/.claude/skills
  --help     Show this help
EOF
}

install_skills() {
  destination_root=$1
  platform_name=$2
  installed=0

  mkdir -p "$destination_root"

  for source_dir in "$skills_dir"/*; do
    [ -f "$source_dir/SKILL.md" ] || continue

    skill_name=$(basename "$source_dir")
    target_dir="$destination_root/$skill_name"
    staging_dir="$destination_root/.$skill_name.install.$$"

    rm -rf "$staging_dir"
    cp -R "$source_dir" "$staging_dir"

    if [ -e "$target_dir" ]; then
      timestamp=$(date -u +%Y%m%dT%H%M%SZ)
      backup_dir="$destination_root/$skill_name.backup-$timestamp"
      if [ -e "$backup_dir" ]; then
        backup_dir="$backup_dir-$$"
      fi
      mv "$target_dir" "$backup_dir"
      printf 'Backed up %s to %s\n' "$skill_name" "$backup_dir"
    fi

    mv "$staging_dir" "$target_dir"
    printf 'Installed %s for %s at %s\n' "$skill_name" "$platform_name" "$target_dir"
    installed=$((installed + 1))
  done

  [ "$installed" -gt 0 ] || {
    printf 'No skills found in %s\n' "$skills_dir" >&2
    exit 1
  }
}

case "$platform" in
  --all)
    install_skills "$HOME/.agents/skills" 'Codex'
    install_skills "$HOME/.claude/skills" 'Claude Code'
    ;;
  --codex)
    install_skills "$HOME/.agents/skills" 'Codex'
    ;;
  --claude)
    install_skills "$HOME/.claude/skills" 'Claude Code'
    ;;
  --help|-h)
    usage
    ;;
  *)
    printf 'Unknown option: %s\n\n' "$platform" >&2
    usage >&2
    exit 2
    ;;
esac
