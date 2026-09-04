# Holiday Planning Workflow

## 1. Build one search envelope

Record origin, true destination or experience goal, earliest/latest dates, minimum/maximum nights, party, cabin and baggage, total budget, room needs, priority activities, pace, mobility, meal expectations, cancellation needs, and hard constraints.

Define “three days” explicitly as calendar days, destination nights, or full usable days when the distinction could change the result.

## 2. Obtain intercity candidates from trip

Use `trip` to produce viable exact itineraries. Retain the cheapest, fastest, and price-first compromise plus materially different arrival airports or date pairs.

For every candidate capture its normalized whole-party EUR cost, local arrival/departure date and time, airport/station, required baggage, positioning, elapsed time, ticket protection, risk, and verified booking link.

## 3. Hand exact transport facts to stay

For each retained transport envelope, invoke `stay` with:

- destination and exact nights;
- party and room requirements;
- arrival/departure points and local times;
- luggage and realistic clearance/reporting buffers;
- priority places, fixed activity times, pace, and mobility;
- budget and cancellation requirements.

Do not reuse one accommodation comparison across airports or date pairs when price, access, or availability differs.

## 4. Generate coherent packages

Combine only exact, compatible transport and stay candidates. Check:

- arrival transfer operates and reaches check-in;
- late check-in is confirmed when required;
- checkout, luggage storage, and departure transfer fit;
- priority activities operate on those dates and remain reachable;
- ticket/pass zones, validity, and service span cover planned journeys;
- the itinerary leaves realistic rest, meal, weather, and disruption margin.

Reject combinations that violate a hard constraint. State why a cheap combination was rejected.

## 5. Normalize the complete budget

`holiday total = intercity transport + required baggage + accommodation + mandatory taxes/fees + airport/station transfers + local transport/pass + selected fixed activities + labelled food allowance`

Also calculate:

- whole-party total;
- per-person total;
- cost per usable destination day;
- fixed/verified subtotal;
- estimated components;
- unavailable components.

The food allowance states its basis: people × destination days × daily allowance, adjusted for included meals. Keep shopping, insurance, upgrades, and optional activities outside the main total unless requested.

If a required component is unavailable, do not call the subtotal complete or use it to prove the cheapest package.

## 6. Normalize experience time

`usable destination minutes = time from realistic arrival clearance to departure reporting cutoff - sleep/rest blocks - unavoidable logistics`

`routine local-travel minutes = repeated walk + wait + ride + transfer time required by the feasible outline`

`lost-time ratio = routine local-travel minutes / usable destination minutes`

Report intercity time separately. Identify lost arrival/departure days and the longest routine one-way local journey. Do not monetize time.

## 7. Compare Pareto choices

Identify:

1. cheapest acceptable complete package;
2. recommended price-first best-value package;
3. lowest-travel/most-relaxing package when distinct.

Quantify for the recommendation:

- premium or saving versus the cheapest;
- usable hours gained or lost;
- routine local-travel hours and lost-time-ratio difference;
- risks, flexibility, or inconvenient timing removed;
- activities or meals added or removed.

Trip duration changes the significance of fixed transfers. Judge repeated commuting more severely than one purposeful excursion, and preserve the user's desired pace.

## 8. Confidence and freshness

Give every component a research timestamp and classify it as:

- verified live;
- estimated from a current authoritative tariff;
- unavailable.

Use itinerary-level, exact-rate property, official transit, and official attraction sources. Cached snippets and “from” prices discover candidates only. Refresh components that are older than the most volatile dependency or whose terms conflict.

## 9. Booking order

Recommend an order based on dependency and reversibility:

1. confirm every component is simultaneously available;
2. prefer refundable or held components while dependent prices remain uncertain;
3. secure the scarcest or fastest-moving dependency;
4. recheck linked transport, stay, activities, and transfers immediately before each payment.

Never purchase, reserve, submit traveller data, or accept non-refundable terms without explicit authorization and action-time confirmation.
