# Flight Research Workflow

## 1. Build the search envelope

Record:

- Actual starting city and true final destination.
- Earliest/latest outbound and return dates.
- Minimum/maximum trip length.
- Hard departure, arrival, work, festival, visa, or accessibility constraints.
- Passenger ages, cabin, checked/cabin baggage, and acceptable self-transfer risk.

For a flexible trip, generate date pairs inside the window that satisfy duration. Cover the boundary dates and cheaper midweek candidates exposed by a live date grid. Do not assume one sample pair represents the window.

## 2. Build candidate route families

Evaluate only plausible families:

1. Home airport to the most practical international gateway.
2. Home airport to a closer regional airport.
3. A nearby major departure hub reached by train/flight when it could materially reduce fare.
4. Open-jaw or multi-city routing when it avoids backtracking.

Exclude a route family once a trustworthy check shows it is dominated on both effective price and time.

## 3. Gather itinerary-level facts

Use live public search and booking pages. Search snippets can discover routes and price bands, but the comparison table requires an itinerary-level result.

For every retained itinerary capture:

- Search timestamp.
- Exact travel dates.
- Total fare and whether it is per traveler or party.
- Currency and point of sale.
- Outbound and return local departure/arrival times and date offsets.
- Duration of each direction.
- Airlines and operating carriers.
- Stops, airports, and layover durations.
- Self-transfer, airport change, terminal change, or overnight connection.
- Cabin and confirmed cabin/checked baggage.
- Whether segments are on one protected booking.
- Exact reproducible search or booking URL.

Use a second source when the first source is ambiguous about price basis, itinerary, or baggage. Prefer booking directly with the airline when the same itinerary costs no more than a small disclosed premium.

## 4. Normalize money

For a round trip, the table's main price is always the complete round-trip total in EUR.

- Multiply per-person fares by the number of travelers.
- Add mandatory baggage for both directions.
- Add round-trip positioning tickets and realistic local transfers.
- Add an unavoidable positioning hotel when same-day travel is unsafe.
- Convert non-EUR components with a current cited exchange rate; state that conversion is approximate.
- Do not add optional meals, seats, insurance, or lounge access unless requested.

Keep airfare and additions visible when an effective total contains estimates.

## 5. Normalize time and risk

Compute end-to-end time from the user's real origin:

- Flight itinerary duration in both directions.
- Positioning travel in both directions.
- Safe check-in and connection buffers.
- Required overnight stays.
- Ground travel from arrival airport to the true destination when comparing gateways.

Flag:

- Separate tickets and missed-connection exposure.
- Baggage collection and recheck.
- Airport or terminal changes.
- Transit visa uncertainty.
- Very short, overnight, or extremely long layovers.
- Arrivals that make onward ground travel impractical.

Do not price risk as imaginary money. Describe it and use it to break close price/time comparisons.

## 6. Rank without hiding trade-offs

First remove hard-constraint violations. Identify the cheapest viable itinerary, fastest viable itinerary, and Pareto-efficient compromise.

Recommend the price-first compromise. Quantify:

- Premium over the absolute cheapest.
- Round-trip hours saved.
- Risks removed.
- Baggage or surface-cost difference.

A very cheap self-transfer stays visible but should not win merely because it is first when sorted by fare.

## 7. Verify links and stop honestly

Open and verify the deepest safe URL that preserves route and dates. Avoid session-bound checkout URLs when a stable exact search URL is available. Never purchase without explicit user authorization and action-time confirmation.

When a site blocks detailed results, make one proportionate retry, switch to a credible alternative, and state any remaining gap. Prices are snapshots, so state the checked date/time and instruct the user to confirm fare, baggage, ticket protection, and total immediately before payment.
