# Holiday Skill Suite Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add independently usable `stay` and compositional `holiday` skills while preserving the current flight-focused `trip` behavior.

**Architecture:** `trip` remains the intercity transport specialist. `stay` normalizes lodging plus local mobility, and `holiday` consumes the normalized outputs of both skills to rank coherent whole-holiday packages.

**Tech Stack:** Agent Skills Markdown/YAML, POSIX shell installer and tests, Git/GitHub.

**Spec:** `docs/superpowers/specs/2026-09-04-holiday-skill-suite-design.md`

## Global Constraints

- Monetary comparisons default to EUR and complete whole-party totals.
- Price ranks first, but time, risk, location efficiency, and relaxation trade-offs must be quantified.
- Time remains a separate dimension and is never converted into an invented monetary cost.
- Cached snippets and “from” prices cannot substantiate comparable bookable rows.
- Research is read-only; booking requires explicit authorization and action-time confirmation.
- Existing `trip` output compatibility must be preserved.
- `stay` and `holiday` must remain independently discoverable Agent Skills.
- Installer support remains POSIX shell compatible for macOS, Linux, and WSL.

---

### Task 1: Stay skill

**Files:**
- Create: `skills/stay/SKILL.md`
- Create: `skills/stay/references/research-workflow.md`
- Create: `skills/stay/references/output-contract.md`
- Create: `tests/test_stay_skill.sh`

**Interfaces:**
- Consumes: destination, exact dates or date window, party, arrival/departure points and times, priority places or desired experiences, mobility constraints, room needs, and budget.
- Produces: ranked exact properties with `complete_stay_cost_eur`, `arrival_transfer_cost_eur`, `local_transport_cost_eur`, `usable_destination_minutes`, `routine_local_travel_minutes`, `lost_time_ratio`, booking terms, risks, and verified links.

- [ ] **Step 1: Run baseline behavior scenarios without the skill**

Use fresh agents with no `stay` instructions for these prompts and record whether they omit whole-stay taxes, daily local travel, pass-zone validity, service span, or usable-time calculations:

```text
Find a cheap hotel for two people for three days in a winter destination. Hotel A is €180 centrally located. Hotel B is €130 but requires two 45-minute bus trips daily and an airport-zone supplement. Recommend one.
```

```text
Compare two exact properties near three named attractions. Determine whether a day pass or individual tickets are cheaper and verify whether the airport is included.
```

Expected RED evidence: at least one baseline response ranks nightly price without fully normalizing mandatory fees, transfer/local transport cost, or cumulative travel time. If every baseline already satisfies the contract, narrow the skill to the demonstrated missing fields rather than inventing guidance.

- [ ] **Step 2: Write the failing structural and invariant test**

Create `tests/test_stay_skill.sh` with checks for the three required files, valid `name: stay` and `description: Use when` frontmatter, discoverable reference links, no unfinished placeholders, and these required concepts across the skill:

```sh
for phrase in EUR 'whole party' 'mandatory fees' 'local transport' 'day pass' zones 'lost-time ratio' 'usable destination time' 'booking URL'; do
  grep -qi "$phrase" "$skill_dir/SKILL.md" "$skill_dir"/references/*.md ||
    fail "required rule is missing: $phrase"
done
```

- [ ] **Step 3: Run the test and verify RED**

Run:

```bash
sh tests/test_stay_skill.sh
```

Expected: failure because `skills/stay/SKILL.md` is missing.

- [ ] **Step 4: Implement the minimal Stay entrypoint**

Write `skills/stay/SKILL.md` with:

- a discriminating “Use when” description for accommodation, hotel, apartment, resort, location, and local-access comparisons;
- defaults for EUR, whole-party complete cost, price-first ranking, and explicit assumptions;
- intake fields;
- the normalization formula;
- required loading of the two references;
- a concise quick-reference table and common mistakes.

The normalization formula must be:

```text
effective stay cost = accommodation + mandatory property taxes/fees + required arrival/departure transfers + routine local transport
```

- [ ] **Step 5: Implement Stay research workflow**

Write `skills/stay/references/research-workflow.md` with exact procedures for:

1. clustering priority places and experiences;
2. building candidate neighborhoods before candidate properties;
3. verifying exact-date room availability and full-price terms;
4. checking arrival/departure feasibility, check-in/out, and luggage storage;
5. routing each retained property to priority clusters at realistic times;
6. comparing individual fares, day passes, visitor cards, airport supplements, zones, validity clocks, service span, and last returns;
7. calculating usable destination minutes, routine local-travel minutes, and `lost_time_ratio = routine_local_travel_minutes / usable_destination_minutes`;
8. checking review patterns without treating one complaint as representative;
9. Pareto ranking cost and time without inventing a monetary time value;
10. verifying deepest reproducible booking and official transit links.

- [ ] **Step 6: Implement Stay output contract**

Write `skills/stay/references/output-contract.md` requiring:

- one-sentence exact-property recommendation;
- assumptions and research timestamp;
- one exact property/room/rate per comparison row;
- complete EUR totals for the whole party;
- transfer and ticket/pass arithmetic;
- priority-place journey time, cumulative local-travel time, and lost-time ratio;
- terms, recurring review risks, and verification links;
- numeric cheapest, fastest-location, and recommended comparison;
- checkout verification list.

- [ ] **Step 7: Run automated and behavioral GREEN tests**

Run:

```bash
sh tests/test_stay_skill.sh
python3 /root/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/stay
```

Run the same two behavioral scenarios with the completed skill. Expected: complete-cost normalization, verified pass scope, explicit travel-time arithmetic, and a recommendation that explains the cost/time trade-off.

- [ ] **Step 8: Commit Stay**

```bash
git add skills/stay tests/test_stay_skill.sh
git commit -m "feat: add stay optimization skill"
```

### Task 2: Holiday orchestration skill

**Files:**
- Create: `skills/holiday/SKILL.md`
- Create: `skills/holiday/references/planning-workflow.md`
- Create: `skills/holiday/references/output-contract.md`
- Create: `tests/test_holiday_skill.sh`

**Interfaces:**
- Consumes from `trip`: exact itinerary, effective round-trip EUR price, arrival/departure points and local times, baggage, duration, protection/risk, and verified booking link.
- Consumes from `stay`: exact property/rate, complete stay and local-mobility EUR costs, check-in/out feasibility, usable destination minutes, routine local-travel minutes, lost-time ratio, terms/risks, and verified links.
- Produces: coherent packages with `holiday_total_eur`, `per_person_total_eur`, `cost_per_usable_day_eur`, `usable_destination_minutes`, `intercity_travel_minutes`, `routine_local_travel_minutes`, `lost_time_ratio`, pace assessment, component confidence, and booking order.

- [ ] **Step 1: Run baseline composition scenarios without Holiday**

Use fresh agents with the existing `trip` skill and completed `stay` skill but no `holiday` instructions:

```text
Plan a three-day Lapland holiday for two. Flight A is €244 but yields 48 destination hours; Flight B is €338 and yields 58. Hotel X is €140 but adds three local-travel hours and €48 transit; Hotel Y is €190 central. Activities cost €220 and food allowance is €150. Compare complete coherent packages.
```

```text
The independently cheapest flight arrives after the cheap hotel's check-in closes. Build the cheapest feasible holiday and show usable time and booking risks.
```

Expected RED evidence: at least one baseline combines independent winners without checking compatibility, omits a cost component, or fails to quantify usable time.

- [ ] **Step 2: Write the failing structural and invariant test**

Create `tests/test_holiday_skill.sh` checking the three required files, valid frontmatter, discoverable references, explicit required use of both `trip` and `stay`, no placeholders, and these concepts:

```sh
for phrase in EUR 'whole party' 'food allowance' 'usable destination' 'lost-time ratio' 'coherent package' 'booking order' 'trip' 'stay'; do
  grep -qi "$phrase" "$skill_dir/SKILL.md" "$skill_dir"/references/*.md ||
    fail "required rule is missing: $phrase"
done
```

- [ ] **Step 3: Run the test and verify RED**

Run:

```bash
sh tests/test_holiday_skill.sh
```

Expected: failure because `skills/holiday/SKILL.md` is missing.

- [ ] **Step 4: Implement the minimal Holiday entrypoint**

Write `skills/holiday/SKILL.md` with:

- a discriminating trigger for whole-holiday, vacation, itinerary, city-break, weekend, or package optimization;
- `**REQUIRED SUB-SKILL:** Use trip`;
- `**REQUIRED SUB-SKILL:** Use stay`;
- intake and assumption rules;
- complete-package arithmetic;
- rejection of incompatible flight/stay combinations;
- required loading of its workflow and output contract;
- quick-reference table and common mistakes.

The package formula must be:

```text
holiday total = intercity transport + required baggage + accommodation + mandatory taxes/fees + airport/station transfers + local transport/pass + selected fixed activities + labelled food allowance
```

- [ ] **Step 5: Implement Holiday planning workflow**

Write `skills/holiday/references/planning-workflow.md` defining:

1. the common search envelope;
2. date/airport/station candidates from `trip`;
3. the exact handoff contract into `stay`;
4. coherent package generation;
5. arrival/check-in, departure/check-out, attraction-hours, and local-service feasibility;
6. whole-party EUR normalization;
7. usable-hours and local-travel calculations;
8. cheapest acceptable, best-value, and low-travel/relaxing Pareto choices;
9. component confidence and stale-price handling;
10. booking sequence based on availability, cancellation, and dependency risk.

- [ ] **Step 6: Implement Holiday output contract**

Write `skills/holiday/references/output-contract.md` requiring:

- winner with dates, transport, property, and complete total;
- assumptions and timestamp;
- a package table with transparent component arithmetic;
- whole-party, per-person, and per-usable-day cost;
- transport, usable destination, and local-travel time;
- lost-time ratio and pace assessment;
- exact flight, property, transit, and activity links;
- a day-level feasibility outline;
- booking order and checkout verification.

- [ ] **Step 7: Run automated and behavioral GREEN tests**

Run:

```bash
sh tests/test_holiday_skill.sh
python3 /root/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/holiday
```

Repeat both behavioral scenarios with the completed skill. Expected: only feasible combinations remain, every mandatory component is included or labelled unavailable, and the recommendation quantifies both cost and usable-time differences.

- [ ] **Step 8: Commit Holiday**

```bash
git add skills/holiday tests/test_holiday_skill.sh
git commit -m "feat: add holistic holiday skill"
```

### Task 3: Repository-wide installation and documentation

**Files:**
- Modify: `tests/test_skill.sh`
- Modify: `tests/test_install.sh`
- Modify: `README.md`

**Interfaces:**
- Consumes: discoverable skill folders `trip`, `stay`, and `holiday`.
- Produces: documented and tested installation for Codex at `~/.agents/skills/<skill-name>` and Claude Code at `~/.claude/skills/<skill-name>`.

- [ ] **Step 1: Extend installer test first**

Update `tests/test_install.sh` so each target mode asserts all three `SKILL.md` files. For example:

```sh
for skill_name in trip stay holiday; do
  assert_file "$codex_home/.agents/skills/$skill_name/SKILL.md"
  assert_missing "$codex_home/.claude/skills/$skill_name"
done
```

Add equivalent loops for Claude and default `--all`, and verify backup behavior for an existing `stay` installation in addition to `trip`.

- [ ] **Step 2: Run installer test and verify RED**

Run:

```bash
sh tests/test_install.sh
```

Expected before the new skills are present in a clean test branch: failure for missing installed `stay` or `holiday`. When executing after Tasks 1 and 2, temporarily verify the test's failure against the parent commit or add the assertions before restoring the completed skill directories.

- [ ] **Step 3: Generalize repository skill test**

Update `tests/test_skill.sh` to invoke:

```sh
sh "$repo_dir/tests/test_stay_skill.sh"
sh "$repo_dir/tests/test_holiday_skill.sh"
```

Preserve all current `trip` invariant checks so compatibility remains protected.

- [ ] **Step 4: Update README**

Add `stay` and `holiday` to the skill catalogue. Add invocation examples for Codex and Claude, describe the distinction among the three skills, update PowerShell copy commands and uninstall commands for all three, and retain `sh install.sh --all` as the recommended installation.

- [ ] **Step 5: Run complete verification**

Run:

```bash
sh tests/test_skill.sh
sh tests/test_install.sh
python3 /root/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/trip
python3 /root/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/stay
python3 /root/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/holiday
git diff --check
```

Expected: every command exits zero and both shell tests print `PASS`.

- [ ] **Step 6: Commit documentation and repository integration**

```bash
git add README.md tests/test_skill.sh tests/test_install.sh
git commit -m "docs: integrate trip stay holiday skill suite"
```

- [ ] **Step 7: Push and verify**

Push all commits to `master`, fetch the new head through the GitHub integration, and verify that the repository tree contains all required files and that README links resolve.
