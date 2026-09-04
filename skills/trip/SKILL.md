---
name: trip
description: Use when planning or comparing flights for fixed dates, flexible dates, arrival deadlines, nearby airports, positioning routes, or trips where live fares and journey time affect the choice.
---

# Trip

## Overview

Find the cheapest practical flight. Compare itinerary-level fares in EUR, with end-to-end time second and connection risk as a tie-breaker.

## Standing defaults

- Use EUR for every monetary figure unless the user explicitly requests another currency.
- Compare complete round-trip totals for the whole party—never one-way prices or “from” fares.
- Rank effective price first, end-to-end time second, then protection, baggage, and arrival convenience.
- Default to economy and one adult only when reasonable from context; state assumptions.
- Treat checked baggage as unknown until the itinerary or fare family confirms it.
- Use local departure/arrival times and show `+1`/`+2` date offsets.

## Intake

Resolve from context: origin, final destination, trip type, dates/window, duration, passengers, cabin, baggage, timing constraints, and deal-breakers.

Ask one compact question when missing information could change the winner. Disclose lower-impact assumptions.

For flexible dates, test multiple eligible date pairs. For fixed dates or an arrival deadline, treat those constraints as hard filters.

## Research and normalization

Read [references/research-workflow.md](references/research-workflow.md) before live flight research.

Start with web search; inspect itinerary-level pages for exact fare, times, baggage, and ticket structure. Verify the deepest safe URL.

Normalize each candidate to:

`effective round-trip price = airfare + required baggage + required positioning + unavoidable hotel/transfer costs`

Compare the direct route, practical nearby arrival airports, and realistic positioning airports. Price positioning from the user's actual origin.

Reject infeasible candidates. Keep the cheapest viable option visible. A premium up to 10% that removes self-transfer risk or saves at least six round-trip hours is usually justified; quantify the trade-off rather than applying this mechanically.

## Required response

Read [references/output-contract.md](references/output-contract.md) before answering.

Lead with the winner. Provide a ranked itinerary table, price/time reasoning, relevant positioning analysis, and checkout checks. Link every comparable row to a live itinerary search or booking path.

Label unverified data as estimated or unavailable. Never present a route-level fare, cached snippet, or conversion as a bookable itinerary.

## Quick reference

| Situation | Required treatment |
|---|---|
| Flexible dates | Compare several valid date pairs and trip lengths |
| Fixed timing | Filter by exact departure/arrival constraint first |
| Nearby airport | Add ground cost and time to the true destination |
| Positioning airport | Add return positioning, buffers, hotel, and ticket risk |
| Self-transfer | Name every self-transfer and baggage recheck |
| Non-EUR source | Convert with a current cited rate and timestamp |
| Missing baggage | Mark unknown; do not infer from airline norms |
| Blocked source | Switch source or disclose the limitation |

## Common mistakes

- Mixing currencies or price bases.
- Omitting positioning cost/time or sharing links that lose dates.
- Omitting times, baggage, self-transfers, or connection protection.
