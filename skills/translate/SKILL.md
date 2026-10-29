---
name: translate
description: Detect the source language of provided text or documents, then translate faithfully and completely into English, favoring word-for-word accuracy, especially for German contracts, letters, and financial documents.
---

# Translate to English

## Trigger
When the user asks to translate or provides text/document for translation in this workflow.

## Procedure
1. Identify the source language from the content, not the filename. If multiple languages are present, identify each relevant language.
2. Read every page and section. If extraction is incomplete, inspect page images; never fabricate unreadable text.
3. Translate into English as literally as natural English allows. Preserve original sequence, headers, clauses, tables, footers, signatures and annotations.
4. Keep personal names, company names, document numbers, identifiers, IBAN/BIC, policy numbers, amounts, units and dates exact. Convert date formatting only when unambiguous.
5. Do not replace translation with a summary. For technical/legal terms retain the original in parentheses on first occurrence when useful.
6. Clearly distinguish the source translation from any explanatory notes or interpretations.
7. Highlight significant deadlines, monetary obligations, discrepancies or apparent errors in a separate short section. Do not infer unstated contractual terms.
8. If requested, include source and English side by side sentence-by-sentence or word-by-word vocabulary glosses.

## Default output
- Detected source language
- Complete English translation in source order
- Important details and potential discrepancies (separate from translation)
