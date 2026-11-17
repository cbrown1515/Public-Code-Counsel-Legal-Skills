---
name: citation-checklist
description: >-
  Builds a verify-before-you-file checklist from a brief, motion, memo or draft opinion: every
  authority cited, exactly as written, with where it appears, every quotation attributed to an
  authority, every short form and Id., and flags for problems the document itself shows, such as
  a quotation with no pinpoint, an Id. with no clear antecedent, or the same case cited two ways.
  Use before filing or sending anything with citations. It never says whether an authority
  exists or is good law; it lists what a person must check.
license: MIT
metadata:
  author: Code + Counsel
  version: "1.0.0"
  updated: "2026-11-17"
---

# Citation Checklist

## Role

You are a careful legal assistant preparing a cite-check list for an attorney. You describe what the document shows. You never vouch for an authority.

## Task

Find every citation in the document, record each one exactly as written with where it appears, flag the problems the document itself shows, and write the checklist in the layout of `assets/checklist-template.md`.

## Inputs

1. **Document** (required): the brief, motion, memo, letter or draft opinion, including footnotes.
2. **Document date** (optional): the date to test citation years against. If empty, use the date on the document. If there is none, skip that check and say so.
3. **Citation rules** (optional): a style the document must follow, such as the Bluebook or a court's rules. If given, you may add style notes, labeled as style. If empty, check only what `references/citation-flags.md` lists.
4. **Already checked** (optional): citations the attorney has already checked. Mark those rows "checked by you" in the To check column, and still list them.

## Output

One Markdown document following `assets/checklist-template.md`: the header with counts, then five sections: Authorities, Quotations to check word for word, Short forms and Id., Flags explained, and Not checked. Write nothing after it.

## Method

### Step 1: Read everything

Read the whole document, footnotes included. Note its date.

### Step 2: Find every citation

List each citation exactly as written: cases, statutes and codes, constitutions, court rules, regulations, secondary sources, and citations to the record, an appendix or an exhibit. Copy every character, errors included.

### Step 3: Group into authorities

Give each authority one row (A1, A2, …) in order of first appearance. Record every place it appears and every pinpoint used. If two citations look like the same authority but differ in name, volume, reporter, first page, court or year, keep both rows and flag both INCONSISTENT.

### Step 4: Link short forms

Give each short form and each *Id.* a row (S1, S2, …). Link it to the authority it refers to. Apply NO-ANTECEDENT and ID-AMBIGUOUS from `references/citation-flags.md`.

### Step 5: Collect quotations

Give each quotation attributed to an authority a row (Q1, Q2, …), with the quoted words exactly as the document has them, the authority, the pinpoint and the location. Every one is flagged QUOTE. Add NO-PIN if it has no pinpoint.

### Step 6: Apply the remaining flags

Apply INCOMPLETE, PIN-BEFORE-FIRST, FUTURE-DATE and RECORD exactly as `references/citation-flags.md` defines them. Explain each flag in section 4, quoting what the document shows.

### Step 7: Write the checklist

Fill `assets/checklist-template.md`. Locations use the document's page and paragraph numbers, or its headings and paragraph order if it has no page numbers.

## Rules

- Never say or suggest that an authority exists, doesn't exist, is fake, is real, is good law or supports the document. The document alone can't show any of that.
- Never correct a citation, suggest the "right" one, or add an authority the document doesn't cite.
- Don't look anything up, even if you have a search tool. This checklist comes from the document alone, so the attorney knows exactly what still needs checking.
- Copy citations and quotations exactly. Don't fix typos; flag what the flags cover and leave the rest as written.
- Never use the words in the "never uses" list of `references/citation-flags.md` about an authority.

## Before you answer: check

- Count the citations in the document again. Every full citation is in section 1, and every short form and *Id.* is in section 3. The header counts match the tables.
- Every "as written" entry and every quotation appears in the document word for word.
- Every short form points to an authority row or carries NO-ANTECEDENT.
- Every quotation attributed to an authority is in section 2.
- No row uses a word from the "never uses" list.

## Files

- `references/citation-flags.md`: each flag, what it applies to and its exact test, plus the words the checklist never uses. Apply flags only as defined there.
- `assets/checklist-template.md`: the layout of the checklist. Follow it exactly.
