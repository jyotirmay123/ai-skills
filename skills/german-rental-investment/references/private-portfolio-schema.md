# Private profile schema — do not commit personal records

Maintain a local JSON file such as ~/.config/ai-skills/german-rental-investment/portfolio.json. The repository includes **no actual user finances**; use prior authenticated context only with date and ownership verification. Never send private profile values in issue comments, pull requests or public reports.

Required data groups (all money EUR, all dates ISO 8601):
- as_of_date, household ownership/tax-residency, relevant tax year, current annual household tax scenario with and without new purchase, monthly net salary and **recomputed** monthly net salary after a 20% gross-pay cut; monthly essentials and other loans.
- available insured/accessibly liquid reserve after acquisition, source and settlement time, minimum desired reserve floor; clearly separate risk capital/P2P, ETFs, emergency cash, promised deposits and future seller refunds.
- existing properties array, one element per **closed** acquisition: place/id, financed purchase and buyer-paid costs, actual outstanding balances, fixed-rate expiration, annual contracted rent, lawful lease changes, annual recoverable/nonrecoverable expenses, owner-funded maintenance, actual yearly debt service, capital works and guarantees, ownership shares, AfA support and incremental assessed tax.
- pending_deals array with explicit "proposed" status, never included as owned unless acquisition completes.
- candidate financing quotes (independent lender name, offer valid until, APR, fees, loan type, nominal interest, term, initial repayment or fixed annuity, first fixation end), available cash at signing, debt-to-income affordability and contingencies.
- objectives: net-of-tax monthly subsidy ceiling (prefer 0), acceptable capital lockup, target hold period, geographic concentration cap, liquidity horizon, personal approval gate.

No assumed numbers. A user may request a *provisional* partial report with unknowns, but cannot get a verified BUY verdict while mandatory fields remain missing.

The arithmetic CLI in this skill expects a flattened self-contained JSON *scenario*, not this private profile schema. The agent translates verified data to the CLI after checking correctness. The CLI's included synthetic file is for demonstration only.