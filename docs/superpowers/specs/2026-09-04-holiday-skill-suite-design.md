# Trip, Stay, and Holiday Skill Suite Design

Date: 2026-09-04
Status: Approved for implementation

## Purpose

Extend the repository from flight-only optimization to composable holiday planning. Preserve `trip` as the intercity transport specialist, add `stay` for accommodation and local-mobility optimization, and add `holiday` as the orchestrator that compares complete, coherent packages.

The suite optimizes for low total cost, limited travel friction, relaxation, and usable experience time. All monetary comparisons default to EUR and whole-party totals.

## Architecture

### trip

`trip` remains independently invokable and flight-focused. It owns:

- exact intercity itineraries;
- round-trip airfare and required positioning costs;
- baggage, self-transfer, connection, and ticket-protection risks;
- door-to-door intercity time;
- live, reproducible booking or search links.

Its existing output contract remains compatible. Local sightseeing transport and accommodation selection do not move into `trip`.

### stay

`stay` is independently invokable when a user wants accommodation in a destination. It owns:

- exact, available properties for the requested dates and party;
- complete stay price after mandatory property taxes and fees;
- room, bed, occupancy, bathroom, meal, payment, and cancellation terms;
- review quality plus recurring material complaints;
- arrival/departure transfers from the selected airport or station;
- routing from each property to priority attractions or activity clusters;
- public-transport frequency, service span, last return, zones, and pass validity;
- individual fares versus day passes, visitor cards, taxis, parking, and walking;
- local-mobility cost and cumulative travel time;
- check-in/check-out and luggage-storage consequences;
- a lost-time ratio: routine local travel time divided by usable destination time.

The skill ranks complete stay choices rather than nightly headline prices. It shows the cheapest acceptable stay, the fastest-location stay, and a price-first best-value recommendation.

### holiday

`holiday` requires both `trip` and `stay`. It composes their normalized candidates into coherent packages; it does not independently redo or duplicate their specialist research.

For each plausible date-and-destination envelope, it:

1. obtains viable intercity options from `trip`;
2. gives the exact arrival airport/station, dates, local times, and party details to `stay`;
3. reconciles check-in, check-out, airport transfers, activity operating times, and local mobility;
4. rejects combinations that violate hard constraints or leave insufficient usable experience time;
5. compares complete packages using cost, usable time, local-travel burden, relaxation, risk, and booking conditions.

## Normalized Package Model

The primary price is:

`holiday total = intercity transport + required baggage + accommodation + mandatory taxes/fees + airport/station transfers + local transport/pass + selected fixed activities + labelled food allowance`

Optional shopping, insurance, upgrades, and discretionary purchases remain outside the main total unless requested.

Every package also reports:

- whole-party and per-person total;
- cost per night and per usable destination day;
- usable destination hours;
- intercity travel hours;
- routine local-travel hours;
- lost-time ratio;
- longest routine one-way local journey;
- material booking and cancellation risks;
- verified versus estimated components.

Time is never converted into invented monetary cost. Cost and time remain separate dimensions, with the trade-off quantified.

## Duration-Aware Treatment

Short trips place greater weight on location efficiency because fixed transfers consume a larger share of the holiday. The lost-time ratio is calculated against the actual usable time between arrival and departure, after realistic airport/station buffers.

A property is not rejected by a universal distance limit. Instead, the skill evaluates:

- the user's stated tolerance;
- trip length and usable hours;
- frequency and reliability of required transport;
- whether travel is concentrated into one worthwhile excursion or repeated every day;
- seasonal walking and waiting conditions;
- whether the cheaper location materially reduces relaxation or access.

## Research and Evidence

Live planning uses:

1. itinerary-level airline, rail, or comparison pages;
2. exact property booking pages or official property pages;
3. official transit operators for fares, zones, passes, schedules, and airport inclusion;
4. official attraction pages for opening times, closures, and ticket conditions;
5. routing/map sources for realistic door-to-door journeys;
6. authoritative tax or tourism sources for mandatory destination charges.

Cached snippets and route-level or property-level “from” prices may discover candidates but cannot substantiate a comparable row. Every retained option receives a research timestamp and reproducible link. Unknowns are labelled rather than inferred.

## Output Contracts

### stay

The response leads with one exact property recommendation, followed by assumptions and timestamp, then a ranked table. Each row includes complete stay price, room/terms, transfer details, attraction access, local-ticket strategy, cumulative local-travel time, lost-time ratio, risks, and a verified booking link.

### holiday

The response leads with one coherent package and complete EUR total. It then presents:

1. cheapest acceptable package;
2. recommended best-value package;
3. lowest-travel or most-relaxing package when distinct.

The comparison explains the recommended premium, money saved or spent, usable hours gained, local-travel hours avoided, and risks removed. It finishes with a day-level feasibility outline, booking order, and checkout verification list.

## Safety and Booking Boundary

Research and comparison are read-only. Neither skill purchases, reserves, submits traveller data, or accepts non-refundable terms without explicit user authorization and action-time confirmation.

## Repository Changes

Add:

- `skills/stay/SKILL.md`
- `skills/stay/references/research-workflow.md`
- `skills/stay/references/output-contract.md`
- `skills/holiday/SKILL.md`
- `skills/holiday/references/planning-workflow.md`
- `skills/holiday/references/output-contract.md`

Update:

- structural and invariant tests for all skills;
- installer tests for Codex and Claude Code;
- README skill catalogue, examples, installation, Windows, and uninstall sections.

The installer already discovers all directories containing `SKILL.md`, so no installer logic change is expected.

## Verification Strategy

Skill development follows red-green-refactor independently for `stay` and then `holiday`.

Baseline scenarios cover:

- a cheap hotel whose daily transfers erase the saving;
- a transit pass that excludes the airport or required zones;
- a short trip whose flight fare is cheap but usable destination time is poor;
- independently cheapest flight and hotel choices that form an inferior combined package;
- missing taxes, baggage, food allowance, or activity costs;
- non-bookable cached prices and unverifiable links.

Automated repository tests verify valid frontmatter, discoverable references, required normalization rules, absence of unfinished placeholders, installation of all three skills for both agents, and backup behavior. Final verification runs all repository tests and skill validators before deployment.
