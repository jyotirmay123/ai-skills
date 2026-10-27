# Case records and review outputs

Use Markdown workpapers or an equivalent structured local format in a private case directory. These records persist the annual workflow; do not create real case folders in the public skill repository. Keep concise user replies separate from detailed working schedules. Never populate a real case with fabricated sample values.

## Required records

| Record | Required content |
|---|---|
| Case overview | Tax year(s), as-of date, scope/stage, taxpayers/residence timeline, filing basis, deadlines/source, authorizations and return status |
| Coverage matrix | Each intake category and relevant person/object; applicable/explicitly none/unresolved; answer/evidence; owner; next action |
| Evidence index | Document ID, private path, issuer/period, person/object/account, correction status and page/row locator |
| Entry ledger | Entry ID, owner/year/category, raw amount/currency/date, FX, deductible share/reimbursement, EUR amount, evidence locator, rule ID, calculation ID, destination ID and status |
| Rule register | Year-specific rule/value/method, applicability/effective dates, direct authority URL, supporting section, checked date, status and interpretation |
| Issues/decisions | Missing facts/law, materiality, effect/range, blocker, next question/document, chosen treatment, alternatives and review requirement |
| Reconciliations | Source totals to ledgers to forms; certificate imports, ownership/period allocation, losses, FX and taxes; differences and resolution |
| Elections | Eligible alternatives, same-facts total household liability, refund/due, future effects, evidence, chosen option and consent |
| ELSTER map | Destination ID, tax year, person/object, form/version, exact German section/field label, verified line if available, format/unit, amount, ledger/calculation IDs, source URL, imported/manual/read-back status |
| Lifecycle | Draft/version, approvals, submitted copy, receipt/ticket/date, assessment comparison, payment/refund, objection date/deadline, next-year carryforwards |

Unknown amounts remain explicitly unknown; missing evidence remains visible even if an estimate can be bounded. Keep worksheet precision separately from field-specific rounding. Record intentional exclusions with reason, authority and possible effect.

## Question batch

Ask only the highest-impact unresolved questions, explaining what each answer changes. Start with year, deadline, residence and household/income screen if unknown. For example: “For PROP-02, provide the acquisition settlement and renovation invoices across the three-year acquisition window; these determine whether costs are immediately deductible or depreciated.” Read documents first. Provide upload requests in normal conversation where supported, not through a text-only questionnaire tool.

## Calculation and optimization packet

Show the following in order, to the extent supported:

1. Readiness and immediate deadline action; unresolved material facts and research.
2. Income/expense totals per source and owner, including foreign taxable/exempt/progression streams and restricted losses.
3. Deductions/allowances, taxable income, tariff/capital tax, tax reductions, Soli/church tax, credited withholding/foreign taxes/prepayments, and estimated refund **or** amount due.
4. Eligible scenario comparison: total household liability first, refund/due and carryforward/multi-year effects alongside; distinguish confirmed savings from amounts depending on evidence/interpretation.
5. Year-verified field map and evidence/reconciliation links. Describe eDaten already imported so they are not re-entered.
6. Remaining actions and approval packet only when review-ready.

If no complete tax engine/data exists, provide clearly labelled component calculations and missing inputs rather than a made-up precise refund. If no complete field map exists, label it partial and preserve verified mappings. Each material legal/field claim needs its own directly supporting official citation; a generic source list cannot stand in for this.

## State labels

Use precise labels: `intake in progress`, `partial draft`, `awaiting evidence`, `awaiting legal/professional review`, `ready for taxpayer review`, `approved version`, `transmission uncertain`, `transmitted with receipt`, `assessment received`, `objection pending`, `closed for this year`. Do not describe a saved or validated draft as filed, or a preliminary refund as guaranteed.

## Planning versus completed-year filing

For a completed year, identify allowable claims using actual facts and payments. Present prospective timing, investment, renovation or household changes as next-year planning; never retroactively fabricate payment dates, ownership or workdays. Separate genuine evidence recovery from hindsight changes to historical facts.

## Next-year handoff

Carry forward only verified: assessed losses by category, AfA/basis and remaining lives, spread repair schedules, fund deemed-income/transition balances, foreign-tax corrections, ongoing disputes, recurring document requests, and personal facts requiring reconfirmation. Save updated private case records with the user's chosen retention controls; do not store sensitive case facts in global skill files or broad long-term memory automatically.
