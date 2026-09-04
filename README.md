# AI Skills

Reusable Agent Skills for Codex and Claude Code. Each skill follows the open Agent Skills folder format: a `SKILL.md` entrypoint plus optional references and scripts.

## Included skills

| Skill | Purpose | Invoke in Codex | Invoke in Claude Code |
|---|---|---|---|
| [`trip`](skills/trip/SKILL.md) | Research and compare bookable flights with price-first, total-time-aware ranking | `$trip` | `/trip` |
| [`stay`](skills/stay/SKILL.md) | Compare exact accommodation using complete cost, local mobility, and usable-time impact | `$stay` | `/stay` |
| [`holiday`](skills/holiday/SKILL.md) | Compose transport, stay, activities, food, and local travel into coherent holiday packages | `$holiday` | `/holiday` |

## Quick install

Requires Git and a POSIX shell (macOS, Linux, or WSL).

```bash
git clone https://github.com/jyotirmay123/ai-skills.git
cd ai-skills
sh install.sh --all
```

The default `--all` installation copies every bundled skill to both supported personal skill locations. Existing skills with the same name are preserved in timestamped backup folders.

Install for only one agent:

```bash
sh install.sh --codex
sh install.sh --claude
```

| Target | Personal skill location | After installation |
|---|---|---|
| Codex | `~/.agents/skills/<skill-name>` | Changes are normally detected automatically; restart Codex if the skill does not appear. |
| Claude Code | `~/.claude/skills/<skill-name>` | Run `/skills` to confirm it appears; restart if the top-level skills directory was created after the session started. |

These locations follow the current [Codex skill documentation](https://developers.openai.com/codex/skills) and [Claude Code skill documentation](https://code.claude.com/docs/en/skills).

## Windows without WSL

Run these commands in PowerShell after cloning:

```powershell
New-Item -ItemType Directory -Force "$HOME/.agents/skills" | Out-Null
New-Item -ItemType Directory -Force "$HOME/.claude/skills" | Out-Null
Copy-Item -Recurse -Force "./skills/trip" "$HOME/.agents/skills/trip"
Copy-Item -Recurse -Force "./skills/trip" "$HOME/.claude/skills/trip"
Copy-Item -Recurse -Force "./skills/stay" "$HOME/.agents/skills/stay"
Copy-Item -Recurse -Force "./skills/stay" "$HOME/.claude/skills/stay"
Copy-Item -Recurse -Force "./skills/holiday" "$HOME/.agents/skills/holiday"
Copy-Item -Recurse -Force "./skills/holiday" "$HOME/.claude/skills/holiday"
```

If a destination already exists, rename or remove it first so PowerShell does not nest the new folder inside the old one.

## Use Trip

Examples:

```text
$trip Find the best round trip from Berlin to Kolkata for 21–28 days within October. Use EUR and prioritize price, then total journey time.
```

```text
/trip Compare fixed-date flights from Frankfurt to Delhi, including baggage and self-transfer risks.
```

The skill asks for missing details only when they can materially change the recommendation. It reports complete round-trip totals, exact outbound and return timing, baggage status, connection risks, and verifiable booking links.

## Use Stay

Use `stay` when the destination and travel window are known and you want the best accommodation base—not merely the lowest room price.

```text
$stay Compare hotels in Rovaniemi for two people, 2–4 February. Include airport transfers, transport to Santa Claus Village and aurora pickup points, ticket/pass options, and cumulative travel time.
```

```text
/stay Find a refundable apartment or hotel in Rome for four nights. Compare complete fees and daily travel to the places I listed.
```

The skill evaluates exact room/rate combinations, mandatory fees, booking terms, airport or station transfers, local tickets and passes, attraction access, usable destination time, and the percentage of that time lost to routine travel.

## Use Holiday

Use `holiday` when flights and accommodation must be optimized together with the rest of the trip.

```text
$holiday Plan a relaxing three-day Lapland holiday from Berlin for two. Compare complete EUR totals including flights, stay, baggage, transfers, local transport, activities, and a labelled food allowance.
```

```text
/holiday Compare complete five-night Lisbon packages across flexible dates. Prioritize price, then usable experience time and low daily commuting.
```

`holiday` uses `trip` for intercity transport and `stay` for accommodation and local mobility. It rejects incompatible combinations and reports whole-party, per-person, and per-usable-day cost alongside travel burden and booking risk.

## Update

```bash
git pull --ff-only
sh install.sh --all
```

Reinstalling preserves the previous copy in a sibling folder named `<skill-name>.backup-<UTC timestamp>`.

## Uninstall

Delete only the installed skill directory for the target agent:

```bash
rm -r "$HOME/.agents/skills/trip"
rm -r "$HOME/.claude/skills/trip"
rm -r "$HOME/.agents/skills/stay"
rm -r "$HOME/.claude/skills/stay"
rm -r "$HOME/.agents/skills/holiday"
rm -r "$HOME/.claude/skills/holiday"
```

## Validate changes

```bash
sh tests/test_skill.sh
sh tests/test_install.sh
```

## License

MIT — see [LICENSE](LICENSE).
