# Intake and evidence

## Case setup

Ask tax year before applying annual rules. Ask requested stage: document collection, preparation, review, portal entry, submission, assessment review, or planning. Record current date, responsible Finanzamt, mandatory versus voluntary filing, notices/extensions, adviser involvement, and any already-filed version. Do not assume AI assistance qualifies for adviser filing deadlines.

For each adult record residence/available homes and move dates, marital/registered-partnership status and changes, separation/death, country/citizenship where relevant, occupation, religion/church-tax changes, and permission to process that person's records. Identify children/dependants, co-owners, and entities without assuming household members share a return. Unmarried partners ordinarily need separate income-tax assessments; minors may have their own filing obligations.

Collect identity/tax number, address, date of birth, and refund IBAN only when needed for the return; keep summaries masked. Distinguish Steuer-ID, Steuernummer, property references, and economic/business identifiers. Inspect prior returns, assessment notices, loss determinations, depreciation schedules, prepayments, provisional assessments, open objections, and carryforward elections. Prior acceptance is evidence, not proof an old treatment remains correct.

## Adaptive screening

Ask a short yes/no/unknown screen across every row. Expand only applicable or unclear rows. A document can establish applicability; record negative answers rather than interrogating every subcase. Cross-check amounts already supplied before repeating questions.

| Category | Follow-up trigger / minimum evidence |
|---|---|
| Employment, pensions, benefits | Every employer/pension payer; wage/tax certificates, benefit statements, remuneration and reimbursement records |
| Family | Marriage/separation dates; spouse income; each child's residence, education, benefits, childcare and support evidence |
| Residence / abroad | Foreign homes, workdays, income, assets, tax returns/payments, countries and dates |
| Rent/property | Every property and ownership interest; deeds, financing, ledgers, renovation and manager statements |
| Capital / employee equity | Every domestic/foreign bank, broker and share plan; certificates, trades, lots, funds, tax and loss data |
| Self-employment / trade / agriculture | Activities/entities, registrations, books, EÜR/balance sheet, VAT, withdrawals/assets |
| Other receipts / disposals | Crypto, private sales, property sales, annuities, maintenance, royalties, foreign structures, platform income |
| Work expenses | Commute/work calendar, travel, remote work, office, tools, training, moves, dual household |
| Personal relief | Insurance/pension, donations, childcare/school, support, medical/care/disability, household services, energy renovation |
| Prior/future effects | Losses, deferred repair costs, credits, depreciation, foreign tax refunds, deadlines, previous errors |

## Evidence ledger

For each document retain `document_id`, local private path, issuer, issue date, covered period, person/property/account, currency, original/corrected status, and extraction confidence. Every claimed entry records document ID plus page/row/cell/transaction locator, raw amount, reimbursement, deductible share, EUR conversion, calculation and destination ID. Record the evidence for allocation choices too.

Assign stable IDs such as PERSON-A, PROP-01, BROKER-01, DOC-001, ENTRY-001. Identify duplicate uploads and overlapping annual/monthly reports before summing. Reconcile corrected certificates against originals; count only the governing version. Reconcile opening plus movement to closing balances where meaningful. Match payer, economic owner, contractual liability, actual payment date, service period, and tax attribution instead of assuming the person uploading paid everything.

Use local extraction/OCR tools suited to the document, loading a PDF/spreadsheet skill when available. Visually verify low-confidence amounts, signs, dates, and decimal separators against originals; OCR is not conclusive evidence. Preserve original documents. Ask for reissued invoices or supporting bank/contract records for missing evidence. Do not invent receipts or apply undocumented round-number allowances. Statutory lump sums are different from invented expenses: verify eligibility and year.

If a tax-law estimate or substitute evidence may be permissible, research that specific basis, disclose method/uncertainty, and obtain professional review when material; do not silently replace missing claimed costs. A user may decline a supported optional deduction; record the omission and impact. Missing mandatory income cannot be removed to unblock filing.

## Record states and blockers

Screening status: `applicable`, `explicitly_none`, `unresolved`. Entry status: `requested`, `received`, `extracted`, `reconciled`, `law_verified`, `mapped`, `reviewed`. Also record `excluded_with_reason` and `needs_professional_review`. Track assumptions separately from verified facts.

Material unknown income, residence, ownership, classification, evidence conflicts, required election inputs, or unverified law block the affected final calculation/submission. Produce a partial draft plus named blockers and next document/action. Do not keep asking indefinitely for immaterial data or block unrelated preparation.

## Privacy

Create case folders only in an agreed private location, outside skill source, public repositories, synced publication folders, or generated public artifacts. Use restrictive local permissions where supported. Never request an ELSTER certificate password/OTP in chat or print credential files, tokens, full tax IDs, or bank details in logs. Screenshots, tool traces, broker exports, and PDFs can contain sensitive data. Avoid unnecessary copies and redact shared examples. Never commit real tax data, including realistic filenames identifying the taxpayer. Obtain the person's authorization before accessing spouse/child/co-owner records; ELSTER account access alone does not establish authority for every person.
