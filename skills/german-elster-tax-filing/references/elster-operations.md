# ELSTER, browser workflows, and optional tools

## Choose a supported route

Discover tools actually connected in the host. For interactive work, load the available browser-control skill first and follow its documented interface; prefer a signed-in user session. If browser control is unavailable, produce exact year-verified field instructions and let the user enter them. Do not block document preparation on portal access.

Official programmatic integration is ERiC, a library supplied through ELSTER's developer registration process, with software integration and manufacturer requirements. It is not a ready-made public REST endpoint or an official generic MCP. Use an already configured, authorized ERiC-compatible application only after verifying its year/schema/form capabilities, validation and test/live distinction. Do not invent income-tax XML, infer an import format from UStVA, or claim a generated archive was transmitted. [ELSTER developer guidance](https://www.elster.de/elsterweb/infoseite/entwickler).

## Community MCP findings: a candidate, not a dependency

Inspected on 2026-10-27: [lukasschwarz/elster-mcp-server](https://github.com/lukasschwarz/elster-mcp-server), commit `baa029dcb414bab5e2240cbfa062978bde49ae9e`. This is community Puppeteer automation, not tax-authority-endorsed software. Findings below apply to that revision, not a future release; no authenticated live filing was tested.

| Capability | Evidence and constraint |
|---|---|
| `elster_est_start` | ESt 1 A preparation, generic field hints, stops for review; does not submit personal income tax |
| `elster_eur_start` | EÜR preparation only; does not complete all business returns |
| `elster_ustva_start` / `elster_ustva_confirm` | VAT advance return flow with a separate transmission action; not ESt submission |
| `elster_sync_history` / `elster_sync_inbox` | Advertised history/inbox retrieval; downloads and local traces contain private data |

Review [tool definitions](https://github.com/lukasschwarz/elster-mcp-server/blob/baa029dcb414bab5e2240cbfa062978bde49ae9e/src/index.ts) before use. The [ESt implementation](https://github.com/lukasschwarz/elster-mcp-server/blob/baa029dcb414bab5e2240cbfa062978bde49ae9e/src/elster/est.ts) matches the first input whose ID/name includes a hint, attempts generic personal labels across pages, logs values, takes screenshots, and can continue when year selection or a validation click was not confirmed. Therefore a session status does not prove correct year, spouse/property attribution, complete annexes, successful validation, saved draft or submission. Generic hint matching is insufficient for unattended complex household returns.

Do not auto-install/run a community MCP with a real certificate merely because it exists. If requested, review current pinned source/dependencies, certificate and password handling, browser sandbox, logs/screenshots/downloads, data destinations, portal access conditions and exact tool support before configuring it. Review current ELSTER terms directly; a community README's warning is not proof of a legal prohibition or permission. Keep credentials in a protected user-managed local secret flow; do not paste them into prompts, shell history, repository files or displayed config. Prefer verified browser entry when a tool cannot unambiguously map and read back each field. This skill does not require that MCP.

If credentials have already been exposed publicly, stop their use, avoid displaying them, and guide the user through official revocation/replacement and protected storage. Removing a public copy does not establish that its contents were never copied. Handle any revocation/account mutation through the user's authenticated flow and scoped authorization.

## Prepare and enter a return

1. Confirm account/taxpayer authorization, selected tax year, assessment/liability type, and whether to resume an existing draft or create one. Inspect existing state to avoid duplicates. User performs login, certificate selection/password and MFA. Check expiry or missing spouse data permissions without collecting passwords in chat.
2. Import prior-year data and Bescheinigungsabruf only when available and authorized. Verify current-year changes and corrected certificates. Import is a starting point, not completeness proof; foreign brokers, deductions, rents and some income may be absent. Request spouse/other-person retrieval permission through the supported process if needed. [ELSTER certificate help](https://www.elster.de/eportal/helpGlobal?themaGlobal=help_vast).
3. Use a field map with tax year, person/property/account, exact form, German section/field label, verified line if applicable, units/format, amount and evidence/calculation IDs. Verify the actual UI because paper lines and portal fields may differ. If no trustworthy source/UI is available mark the field unverified and stop that entry; do not guess a line or input ID.
4. Reconcile imported versus manual fields. Select/add required annexes and correct repeatable person/object instances. Check signs, German decimal format, whole euros/cents, percentages, dates, gross/net and pre/post-exemption basis. Respect each field's instructions for rounding or totals. Enter known supported values and immediately read them back within the right context.
5. Save and confirm the draft identifier/state. Run `Prüfen` and inspect actual errors and warnings. Fix true data/mapping issues; do not change correct facts merely to remove a warning. Keep a record explaining remaining warnings. Validation checks plausibility, not legal correctness or completeness.
6. Open the preliminary calculation and full return preview. Reconcile source totals, each spouse's figures, property/participation shares, progression, capital taxation, credits, losses, Soli/church tax and expected refund/due against workpapers. Explain material differences and limits. Mark professionally unresolved entries as blockers.

## Final transmission gate

Present a compact approval packet: year, taxpayer(s), draft/version, required returns/annexes, material elections, income/deduction/tax totals, estimated refund/due, warnings and remaining issues. Block transmission for material unknowns, unexplained mismatches, unverified fields or required professional review. Ask approval for the exact reviewed return; record approval time/version. A subsequent material change invalidates it. Separate returns (for example a co-owner determination or VAT return) need their own scoped approval.

After approval use a verified transmission route if available, or hand final click to user. Do not call a VAT confirmation tool for income tax. Stop at user-required signature/authentication steps. Confirm success through ELSTER's explicit receipt and transmission ticket/history, not a click, screenshot name or tool `DONE` status. Save the submitted copy, receipt, timestamp, calculation, evidence index and elections privately. A receipt confirms transmission, not substantive tax acceptance.

If connection fails after sending, treat result as uncertain: inspect receipts/history and the current draft before any retry. Never blindly resubmit. If no supported route exists, clearly label `reviewed draft — not transmitted` and provide remaining user actions.

## Assessment, objections, and annual rollover

Establish the year and status of each return/notice separately: an objection concerns an issued assessment, not an unsubmitted draft. Distinguish portal preliminary tax calculation, Bescheiddaten and the legally relevant Steuerbescheid. Read the complete assessment including explanations, provisional/reservation clauses, interest/prepayments and legal-remedy instructions. Compare accepted income, expenses, allocation, tax credits and losses line by line with the filed return. A foreign refund or corrected certificate may require follow-up.

Record issue date, dispatch/delivery/access facts and legal notification rules for that year and channel. Calculate the applicable objection deadline from the actual notification; verify weekends/holidays and exceptions. Do not equate inbox availability or assessment date with notification, or treat a month as 30 days. [§355 AO](https://www.gesetze-im-internet.de/ao_1977/__355.html), [§122 AO](https://www.gesetze-im-internet.de/ao_1977/__122.html), [§122a AO](https://www.gesetze-im-internet.de/ao_1977/__122a.html).

Electronic notification is a year-sensitive trap: for notices issued after 31 December 2025, inspect the changed §122a rule anchoring the ordinary deemed-notification period to provision for retrieval and the transitional provisions, including different commencement dates within the amended section. Do not carry an earlier email-dispatch trigger forward automatically. Reverify the notice's channel, actual applicable text and exceptions. [Art.97 §28 EGAO](https://www.gesetze-im-internet.de/aoeg_1977/art_97__28.html).

Draft a fact-specific correction request or Einspruch with references and requested outcome when authorized. Underlying Feststellungsbescheide may need a separate challenge; contesting the personal return alone may not fix them. An objection does not automatically suspend payment. Obtain explicit approval before sending a new objection, extension request, amendment or payment-related instruction; preparing those drafts does not require waiting. Track actual acceptance, amount paid/refunded, remaining deadlines and next year's verified carryforwards. Reconfirm personal facts and refresh law next year.

If an objection deadline is imminent and grounds need further work, prepare a short protective draft identifying taxpayer, Finanzamt, exact notice/type/year/date, the clear intention to object, challenged scope and that reasons will follow. Verify a valid filing channel and deadline; resolve necessary scope facts before sending, obtain scoped approval, and retain delivery confirmation. Do not let a lengthy merits analysis silently consume the deadline or claim an unsent draft preserved it.
