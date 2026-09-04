# Flight Comparison Output Contract

## Answer order

1. One-sentence recommendation with route, dates, airline, and effective EUR round-trip total.
2. Assumptions and fare-check timestamp.
3. Ranked comparison table.
4. Short explanation of why the winner beats the cheapest and fastest alternatives.
5. Positioning and final-ground-leg calculation when applicable.
6. Exact checkout verification list.

## Required table

Use one row per exact itinerary.

| Rank | Dates and route | Outbound | Return | Stops, layovers, airline and risk | Baggage | Effective round-trip price | Verify/book |
|---:|---|---|---|---|---|---:|---|

Every outbound/return cell contains local departure time, arrival time, `+1`/`+2` when applicable, and elapsed duration. Put exact layover airports/durations and every self-transfer in the risk cell.

The price cell contains only EUR as the comparison currency. For positioning routes, show the arithmetic: `flight + return positioning + unavoidable hotel = effective total`. Mark estimated components with `≈`.

The link must reproduce the route and dates on a live booking or comparison site. A generic airline homepage is supporting information, not the row's booking link.

## Decision summary

State these three facts numerically:

- Cheapest viable round trip.
- Fastest viable round trip.
- Recommended round trip, including its premium and round-trip hours saved versus the cheapest.

If one itinerary is simultaneously cheapest and fastest, say so plainly.

## Checkout checks

Tell the user to confirm:

1. Displayed amount is the complete EUR round-trip total for the stated party.
2. Dates, airports, local times, and date offsets match the table.
3. Cabin and baggage apply to every segment.
4. Segments share one booking reference when described as protected.
5. No unreported self-transfer, airport change, or overnight connection exists.
6. The final payment page has not added fees or changed the itinerary.

## Compact example

“Choose BER–DOH–CCU, 24 Sep–22 Oct, at €584 round trip. It costs €37 more than the absolute cheapest route but saves 18 round-trip hours, includes checked baggage, and removes three self-transfers.”

This example demonstrates the decision format; never reuse its fare or dates as live data.
