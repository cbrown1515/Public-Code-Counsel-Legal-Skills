# Citation Checklist

Before you file, get a list of every authority your document cites, exactly as written, with where it appears, every quotation you attribute to an authority, every short form and *Id.*, and flags for problems the document itself shows.

It never tells you a case exists or is good law. Models can't know that from a document, and saying so is how fabricated citations get filed. It gives you the list to check.

> Draft work product for attorney review. Not legal advice. Check every row in Westlaw, Lexis, CourtListener or the official source before filing.

## What you give it

| Input | Required | Notes |
|---|---|---|
| Document | Yes | Brief, motion, memo, letter or draft opinion, with footnotes. |
| Document date | No | For the future-year check. Otherwise the date on the document is used. |
| Citation rules | No | A style the document must follow. Style notes are labeled as style. |
| Already checked | No | Citations you've already checked. They stay on the list, marked "checked by you". |

## What you get

A checklist following [`assets/checklist-template.md`](assets/checklist-template.md):

1. **Authorities:** one row per authority, with every place it appears and every pinpoint used.
2. **Quotations to check word for word:** every quotation attributed to an authority.
3. **Short forms and *Id.*:** each linked to the authority it refers to.
4. **Flags explained.**
5. **Not checked:** what the checklist couldn't cover.

## Flags

Defined in [`references/citation-flags.md`](references/citation-flags.md): QUOTE, NO-PIN, NO-ANTECEDENT, ID-AMBIGUOUS, INCONSISTENT, INCOMPLETE, PIN-BEFORE-FIRST, FUTURE-DATE and RECORD. Each one is something visible in the document, not a judgment about the authority.

## Files

```
citation-checklist/
├── SKILL.md                         the instruction
├── references/citation-flags.md     flag definitions and the words it never uses
├── assets/checklist-template.md     the checklist layout
└── evals/                           a fictional brief and its answer key (not uploaded with the skill)
```

## Run it

See [Run anywhere](../docs/run-anywhere.md). **Data:** a draft brief is usually confidential work product. Run it only in a tool your firm has approved for client material.

## Test it

[`evals/evals.json`](evals/evals.json) runs the skill on [a fictional brief](evals/fictional-brief-01.md) whose case citations are invented, with planted problems, and grades the result against [its answer key](evals/expected-01.md).

## Changelog

- 1.0.0 (2026-11-17): first release.
