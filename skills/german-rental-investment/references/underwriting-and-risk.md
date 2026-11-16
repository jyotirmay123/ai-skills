# Portfolio underwriting: mathematics, downside and purchase gates

## Inputs (use latest **verified private data**, never embed personal profile in the public repo)

For the existing portfolio: every signed property loan, balance, contractual rate, payment, fixation end, net monthly rent, lease/guarantee expiry, non-recoverables, owner-funded reserve, management, property tax not recoverable, long-term maintenance, current approved AfA, vacancy, and scheduled works. Specifically reconcile Mannheim; exclude any merely proposed Düsseldorf/Ludwigshafen commitment until signing is confirmed. Confirm liquid **insured and accessible** cash (do not count high-risk P2P at face value), pension/ETF liquidity if relevant, debt not property-backed, net pay, household essential expenses and a gross-pay -20% **recomputed net-pay case**. Record a dated source for each amount. The user's previously discussed €30k liquidity *goal* is not proof that the reserve already exists.

For the candidate: asking price, justified market-value range, full closing/repair/furnishing costs, at-close funding proof, building-versus-land cost allocation, tax rate evidence, rent and enforceable cap, vacancy/arrears, Hausgeld (recovered versus nonrecoverable), rent guarantee expiry, management, repairs/capex, financing (every loan, nominal and effective APR, amortization, term, fixation and fees), and timing of capex.

## Return calculations

- Purchase €/m² = **price / actual Wohnfläche**. Compare purchase + buyer-paid fees + immediate renovations to achievable net yield and matched market transaction prices.
- Gross rent yield = **annual legal cold rent / full acquisition cost**, labeled *gross*, and *not* a decision metric alone.
- Effective gross income = **legally collectible cold rent + verified separately collectible ancillary revenue - vacancy, collection failure and incentives**. Do not double-count passing-through utilities.
- Property NOI = effective gross income - nonrecoverable expenses - management - normalized owner-funded maintenance/capex. Show ordinary cash repair-reserve funding separately from the tax treatment of actual expenditure.
- Annual debt service = interest + principal over all loans (including any property-linked secondary renovation or consumer loan); debt service cover = NOI / service, undefined at zero service.
- **Cash flow before tax** = NOI - debt service, excludes principal from expenses but includes the principal cash payment.
- **Cash flow after tax** = pretax cash flow - *incremental assessed household income tax*, which may be negative for a lawful tax saving. The value must reflect ownership, existing property losses, financing, AfA eligibility and refund usability; when unverified, show "unknown" rather than a fictional number.
- Annual equity build = debt principal paid, **not spendable income**. Purchase-day equity = fair market value - debt - immediate selling friction. Seller gift/subvention may reduce basis or cost, but is not recurring rent.
- Exit equity = independently estimated net sale proceeds - outstanding total debt - exit costs - applicable taxes/penalties. Ten-year cash-on-cash, net wealth and annualized IRR should include all upfront outlay and every yearly net cash flow; separate pretax and after-tax IRR and clearly mark unsupported tax effects.

## Required scenarios (candidate **and combined portfolio**)

| Scenario | Requirement |
|---|---|
| Base today | Verified legal rents, realistic vacancy, all debt/costs, no speculative rate reduction, zero appreciation core |
| Rent shock | -10% collected rent for *all rentals*, with operator-guarantee failure if applicable |
| Salary shock | -20% gross employment earnings; obtain the corresponding recalculated net salary (do not reduce net by 20% blindly) |
| Repair | One-off €10,000 **on top of** ordinary reserve funding/repair assumptions |
| Refixation | +2 percentage points on affected loans when each fixed rate ends; calculate outstanding principal, new payment and date, not +2% today to every fixed loan |
| Vacancy / guarantee | Several empty months, delinquency, rent guarantee ends, management/provider insolvent |
| Exit | Early sale and 10-year sale; -1%, 0%, +2% annual nominal values as transparent illustrations, sales costs and §23 tax timing |
| Energy/WEG | Known upgrades, Sonderumlage, extra Hausgeld and realistic repair contingency |

Report the **worst annual and monthly portfolio cash deficit**, reserve coverage after closing and after €10k repair, debt-service coverage both by unit and portfolio, net pay remaining after essentials and property support, loan-balance schedules, and rate-refix cliff years. Include uncertainty bands rather than hidden point guesses.

## Screen-out and promotion policy

Default *screening* thresholds, amend only with the user's stated risk appetite and verified bank terms:

1. **Hard stop** if legal rent, real listing, purchase costs, lender quote, WEG material liabilities or ownership tax basis is unverified; cannot call a BUY.
2. **Reject** if the purchase requires paying bills or funding closing costs from uncommitted seller kickbacks, future tax refunds, or unsecured speculative investments.
3. **Reject** if normal pre-tax cash flow is negative **and** the mandate requires cash-flow-positive investment. Show exact negotiated price or rent needed for zero cash flow; never assume rent exceeding the cap.
4. Reserve test: after all purchase funding, accessible liquid funds should exceed the *user-confirmed minimum* **plus** the specified one-off repair and at least 12 months of modeled stressed portfolio cash deficits; avoid counting property equity as cash. A default €30k floor may be **proposed**, never assumed to be owned or mandated.
5. For conservative shortlisting target stabilized property DSCR >= 1.10, combined DSCR >= 1.10, and credible survival of guarantee expiry. Below threshold requires NEGOTIATE/WATCH and underwriting evidence, even if the after-tax result seems positive.
6. If salary -20% adjusted net cannot cover essential living costs plus stress rental deficits without dipping below the reserve floor, REJECT.
7. Evaluate debt concentration, one-city/one-agent/one-guarantor reliance, maintenance spikes, insurance and exit liquidity. Cheap-looking returns with single counterparty risk are not safely diversified.
8. A 10-year return requiring future appreciation to overcome ongoing losses is a **speculative growth bet**, not a low-risk cash-flow rental. Compare at 0% appreciation; never describe a positive outcome as "highly probable" without empirical calibration.
9. Always disclose **do nothing** versus buy candidate, existing portfolio-only taxes and money, opportunity cost of keeping liquidity, and post-guarantee year.

Use the included script for indicative amortization, DSCR, pre-tax cash-flow, reserve and exit scenario checks. Its final decision is at most **PRELIMINARY SHORTLIST** and never supersedes primary documentation, personal budget or legal/tax verification.

## Maximum-bid calculation

From a target pre-tax cash-flow floor C per month and achievable yearly NOI N, derive annual affordable debt service D = N - 12*C. Under an indicative loan of principal P, nominal interest i and initial repayment t, annual first-year service approximately P*(i+t). Therefore P_max ≈ D/(i+t), subject to bank terms and full cash/down-payment/closing/reserve constraints. With cash available for acquisition costs, convert P_max into a **purchase price ceiling** only after including all costs. Compute a second ceiling from independent sales comparables and select the **lower** bound. Recalculate for each proposed loan structure and do not apply this approximation to amortizing consumer loans or variable-rate products without correct schedule.