# Stay Comparison Output Contract

## Answer order

1. One-sentence recommendation naming the exact property, room/rate, dates, and effective EUR total.
2. Assumptions and research timestamp.
3. Ranked property table.
4. Numeric comparison of cheapest, fastest-location, and recommended stays.
5. Local-ticket or pass calculation.
6. Checkout verification list.

## Required table

Use one row per exact property, room, rate, and cancellation policy.

| Rank | Property and exact rate | Room and terms | Arrival/departure transfer | Priority-place access | Local-ticket strategy | Travel burden | Effective stay cost | Verify/book |
|---:|---|---|---|---|---|---|---:|---|

Each row contains:

- whole-party accommodation price plus mandatory fees;
- exact check-in/out and relevant luggage arrangements;
- transfer modes, costs, and door-to-door minutes;
- representative repeated routes with walk, wait, ride, frequency, and last-return constraints;
- individual-ticket, day pass, multi-day pass, or visitor-card arithmetic;
- routine local-travel minutes, usable destination minutes, and lost-time ratio;
- a reproducible booking URL plus official transit links.

Use `≈` for estimates and `unavailable` for facts that could change the winner but could not be verified. Do not silently treat unavailable costs as zero.

## Decision summary

State numerically:

- cheapest acceptable effective stay cost;
- fastest-location cumulative routine local-travel time;
- recommended cost premium or saving;
- local-travel hours and lost-time-ratio difference versus the cheapest;
- important cancellation, payment, room, or review-confidence differences.

If one property wins every dimension, say so plainly.

## Compact example

“Choose Central Hotel's refundable double room at €286 effective total. It costs €31 more than the remote apartment but avoids €46 of transfers, saves 4.2 local-travel hours, and reduces the lost-time ratio from 14% to 4%.”

The figures illustrate the decision format only; never reuse them as live data.

## Checkout checks

Tell the user to confirm:

1. Dates, nights, guests, room, beds, bathroom, and meal inclusion.
2. Complete EUR total includes every mandatory tax and fee.
3. Payment timing and cancellation deadline match the table.
4. Check-in/out and luggage arrangements fit actual transport times.
5. Linked transit fares, zones, airport coverage, validity, and service hours remain current.
6. The final payment page has not changed the property, rate, terms, or total.
