---
name: german-rental-investment
description: Use when searching for, screening, negotiating, or underwriting German buy-to-let apartments; assessing legally achievable rent, Mietpreisbremse, WG or furnished letting, appreciation, financing, AfA and taxes, guarantees, existing portfolio exposure, liquidity, stress tests, and property purchase go/no-go decisions.
---

# German Rental Investment — risk-first acquisition scout

Find independently verifiable German residential apartments that can produce credible, *lawfully collectible* rental income, resilient cash flow, and defensible 10-year total returns **without overleveraging the existing portfolio**. Optimize the user's **incremental household wealth and risk**, not advertised depreciation, seller rebates, promises of rent, or headline yield. A good answer may be **BUY NOTHING**.

This is a research-and-underwriting agent skill, not an always-running property alert, insurer, tax assessment, lender offer, or guarantee of profitability. Research live listings whenever tools permit; never pretend cached advertisements are available. Do not make an offer or sign anything without explicit user approval.

## Files and operating order

Read these before issuing a purchase recommendation:

1. [Discovery and location evaluation](references/discovery-and-market.md)
2. [Rental law, tax, and guarantees](references/legal-and-tax.md)
3. [Portfolio underwriting and stress tests](references/underwriting-and-risk.md)
4. [Evidence and output contract](references/output-contract.md)

For reproducible first-pass calculations, use [the standard-library underwriting CLI](scripts/underwrite.py) and the synthetic [example input](examples/synthetic-deal.json). This CLI performs arithmetic only. It **cannot** authenticate source documents, settle German tax law, estimate probability of appreciation, or approve a deal.

## Privacy and personal context

- Consult *this user's current conversation, private records explicitly supplied, or a private local profile* for loans, salary, cash, expenses, and existing investments. Confirm dates and distinguish signed obligations from contemplated offers.
- Existing Mannheim investment must be included in the portfolio baseline when applicable. Do **not** assume a Düsseldorf, Ludwigshafen, or other proposed acquisition was completed.
- Do **not** publish personal income, property address, bank balances, debt terms, tax documents, credentials, or private portfolio files into this public GitHub repository. Use a local file outside the repo (for example ~/.config/ai-skills/german-rental-investment/portfolio.json), excluded from commits and reports shared externally. The [private profile schema](references/private-portfolio-schema.md) describes the fields; it contains no personal values.
- Carry forward remembered details as *candidates for verification*, not facts valid forever. Unknown means **unknown**, never zero. If current portfolio inputs are missing, do location and listing research, but issue **INSUFFICIENT DATA**, not a firm BUY.

## Acquisition workflow

1. **Establish the investment mandate.** Confirm desired regions or Germany-wide search, monthly affordable out-of-pocket limit, purchase and closing cash, reserve floor, lenders' real quotes, ownership, tax year, hold period, portfolio exposure, and required management model. Default to a 10-year horizon, EUR nominal amounts, and **no assumed price growth** as the core base case.
2. **Discover and de-duplicate.** Search multiple live listing sources, direct agents and public data. Preserve timestamped original listing URLs, location, asking price, Wohnfläche, construction and modernization dates, EPC, lease status, Hausgeld breakdown, tenant terms, and source quality. Do not infer missing features. Explore smaller-ticket and reasonably priced units, but rank *value* rather than cheapest asking price.
3. **Research location and executable resale value.** Compare achieved local transaction prices when obtainable, matched sale listings separately, rent level, real tenant demand, population and household trends, employers, jobs, transport, vacancy, pipeline, demographic and climate risks. Distinguish completed infrastructure from proposals. Price/m² alone is never sufficient.
4. **Underwrite legal rent.** Identify the current Bundesland/municipal Mietpreisbremse ordinance, exact Mietspiegel category or admissible comparison method, existing tenancy and rent, exclusions/evidence under §§ 549 and 556d–556g BGB, furnished and WG nuances, subsidy restrictions, and future increase constraints. Calculate sustainable **Kaltmiete** independently of seller-projected WG rates. If legal rent is unresolved, STOP at research status.
5. **Audit the real acquisition.** Require full purchase price plus Grunderwerbsteuer, notary, Grundbuch, commission, repairs, furnishing, loan setup and retained liquidity. Check independent valuation, WEG resolutions, reserve fund, arrears, liabilities, planned Sonderumlagen, energy transition, and contract contingencies. Confirm each lender's actual availability, LTV, APR, repayment structure and refinancing exposure. Seller-funded expenses or commission rebates are not automatically free equity.
6. **Model income and taxes separately.** Compute collected rent after vacancy and legal cap, non-recoverable costs, management, realistic maintenance/capex, annual debt service and principal; report operating cash flow **before** taxes. Model incremental household tax liability with the existing rental property, verified building share and lawful AfA only. Do not treat AfA as cash, principal as an expense, or a rebate as recurring income.
7. **Stress the combined portfolio.** Run no appreciation; -10% rental collection **across the portfolio**; -20% employment gross pay with **recalculated net pay**; an additional €10,000 one-off repair; +2 percentage points on post-fixation rates; rent-guarantee expiry; vacant/tenant-default months; energy and WEG repair; early sale. Preserve liquidity and job-loss / no-tax-refund views.
8. **Rank or decline.** Apply hard exclusion gates before any score. Compare at least 3 qualifying listings when possible; if none passes, say why and set evidence-based maximum bid prices. Present **BUY / NEGOTIATE / WATCH / REJECT / INSUFFICIENT DATA** with explicit unresolved blockers and conditions for upgrading a preliminary shortlist to BUY.

## Mandatory decision rules

- **No BUY** based on a fictional or unverified listing, unsourced legal rent, unproven AfA, seller promise of guarantees, future 10–15% rent bumps, falling interest rates, or appreciation needed to survive.
- **No BUY** if the combined portfolio would violate confirmed available liquidity or living-expense resilience; unsecured P2P/investment balances do not automatically count as insured cash reserves.
- **No BUY** just because rental losses lower tax. Compare the *incremental* total household after-tax result against owning only the preexisting property and against not purchasing.
- **No BUY** if essential purchase contract, tenant lease, WEG budgets/minutes, reserve balance, energy certificate, building allocation, legal rent assessment, and finance offers are missing. Flag conditional candidates as WATCH or NEGOTIATE.
- **No manufactured percentages.** A 10-year scenario is not a probability distribution. Only quote "probability of profitability" if calibrated to attributable empirical data, explicit uncertainty, assumptions and documented method; otherwise show downside/base/upside without odds.
- A risk score may organize fully evidenced cases, but cannot override a failed hard gate; suppress it if key information is unknown.

Follow the full required response format in [the output contract](references/output-contract.md).