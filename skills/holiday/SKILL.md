---
name: holiday
description: Use when planning or comparing a complete holiday, vacation, city break, weekend trip, itinerary, or travel package where transport, accommodation, local mobility, activities, cost, and usable experience time must work together.
---

# Holiday

## Overview

Find the cheapest coherent holiday, not independently cheap components. Compare complete packages in EUR for the whole party while keeping travel time, usable experience time, relaxation, and booking risk visible.

**REQUIRED SUB-SKILL:** Use trip

**REQUIRED SUB-SKILL:** Use stay

## Standing defaults

- Use EUR unless the user requests another currency.
- Compare whole-party totals; also show per-person and per-usable-day cost.
- Rank complete cost first, then usable destination time, local-travel burden, risk, and relaxation.
- Keep money and time separate; never assign time an invented monetary value.
- Include a clearly labelled food allowance unless the user excludes food.

## Intake

Resolve origin, destination or experience goal, dates/window, duration, party, baggage, budget, accommodation needs, priority experiences, pace, mobility, food scope, and booking constraints.

Ask one compact question only when the answer could change the winner. For flexible plans, compare multiple coherent date, transport, and stay combinations.

## Compose before ranking

Read [references/planning-workflow.md](references/planning-workflow.md).

Use `trip` for exact intercity options. Give each retained arrival/departure point, date, and local time to `stay`. Reject combinations that fail check-in/out, transfer, activity-hours, or local-service constraints.

`holiday total = intercity transport + required baggage + accommodation + mandatory taxes/fees + airport/station transfers + local transport/pass + selected fixed activities + labelled food allowance`

A subtotal with unavailable components is not a complete total and cannot establish the cheapest coherent package.

## Required response

Read [references/output-contract.md](references/output-contract.md).

Lead with one exact package and its complete EUR total. Show the cheapest acceptable, recommended best-value, and lowest-travel/most-relaxing packages when distinct. Quantify price, usable-time, lost-time-ratio, and risk differences. Link every bookable component to a verified path.

## Quick reference

| Situation | Required treatment |
|---|---|
| Cheap flight, poor timing | Recalculate usable destination time |
| Cheap stay, remote location | Add transfers, local fares, and routine travel |
| Different arrival airports | Build separate stay candidates for each |
| Check-in/out mismatch | Resolve it or reject the combination |
| Missing component | Label unavailable; do not call the total complete |
| Flexible dates | Compare coherent packages, not flight fares alone |

## Common mistakes

- Combining the cheapest flight and hotel without testing compatibility.
- Calling flight-plus-hotel a complete holiday price.
- Omitting food, taxes, baggage, transfers, passes, or fixed activities.
- Ignoring closed attractions, missed last transport, or unusable arrival days.
- Producing an ambitious itinerary that conflicts with the requested relaxation.
