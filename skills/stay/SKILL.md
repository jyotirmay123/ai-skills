---
name: stay
description: Use when finding or comparing hotels, apartments, resorts, hostels, or neighborhoods where exact accommodation cost, location, local transport, attraction access, and usable holiday time affect the choice.
---

# Stay

## Overview

Find the cheapest practical place to stay, not the cheapest room headline. Compare exact bookable rates in EUR for the whole party, then use local-travel burden, booking terms, and stay quality to break close price choices.

## Standing defaults

- Use EUR unless the user requests another currency.
- Compare complete stay totals for the whole party.
- Rank effective cost first, cumulative local-travel time second, then cancellation terms, room suitability, and review confidence.
- Keep money and time separate; never invent a monetary value for time.
- Treat taxes, fees, transport fares, pass coverage, and luggage storage as unknown until verified.

## Intake

Resolve destination, dates or window, party, budget, room/bed needs, arrival and departure points and times, priority places or experiences, mobility constraints, and cancellation needs.

Ask one compact question only when the missing answer could change the winner. For flexible searches, compare multiple eligible dates and neighborhoods.

## Research and normalization

Read [references/research-workflow.md](references/research-workflow.md) before live accommodation research.

Build useful neighborhoods from the user's priority places before selecting properties. Retain only exact-date room and rate combinations.

`effective stay cost = accommodation + mandatory property taxes/fees + required arrival/departure transfers + routine local transport`

Calculate the lost-time ratio against actual usable destination time:

`lost-time ratio = routine local-travel minutes / usable destination minutes`

Use official transport sources for individual tickets, day pass or visitor-card prices, zones, airport supplements, validity, frequency, and last returns. Unknown components remain visible and may prevent a price claim from being comparable.

## Required response

Read [references/output-contract.md](references/output-contract.md) before answering.

Lead with one exact property, room/rate, and complete EUR total. Show the cheapest acceptable stay, fastest-location stay, and recommended stay when distinct. Link each row to a reproducible booking URL and the relevant official transport evidence.

## Quick reference

| Situation | Required treatment |
|---|---|
| Short trip | Calculate usable time and lost-time ratio |
| Cheap remote property | Add transfers and repeated local transport |
| Transit pass | Verify zones, airport inclusion, validity, and service span |
| Headline room price | Add mandatory fees and taxes |
| Check-in mismatch | Verify late arrival, luggage storage, or reject |
| Review score | Check volume, recency, and recurring material complaints |

## Common mistakes

- Ranking nightly price instead of the whole-party effective cost.
- Measuring distance without realistic routes, waiting, and service hours.
- Assuming a day pass covers the airport or every required zone.
- Combining a property page with a different room, rate, or cancellation policy.
- Treating one review or an unverified booking snippet as decisive.
