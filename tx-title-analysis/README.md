# Texas Title Analysis

Texas title examination for residential and commercial real estate. Give it a title commitment and the supporting documents, and it drafts a title opinion letter, a requirements checklist and exception cure recommendations, citing the Schedule B item and quoting the document for every finding.

> **Draft work product for attorney review.** Not legal advice. All outputs require review, verification and approval by a licensed Texas attorney before use or reliance. No attorney-client relationship is created by use of this skill.

## What you give it

| Input | Required | Notes |
|---|---|---|
| Title commitment | Yes | Commitment for Title Insurance or preliminary title report, with Schedules A, B-I and B-II. |
| Supporting documents | No | Recorded instruments, survey, tax certificate, HOA documents, searches, affidavits, probate or divorce records. |
| Transaction | No | Purchase, refinance, construction or equity loan, or a mineral interest, and which party you represent. |
| Outputs wanted | No | Opinion, checklist, cure recommendations, or all three (the default). |

## What you get

| Output | Description |
|---|---|
| **Title opinion letter** | Draft with documents examined, chain of title, vesting, requirements, exceptions and Texas-specific findings |
| **Requirements checklist** | Must clear before closing, documents needed, payoffs, affidavits, HOA and tax items, remaining exceptions |
| **Exception cure recommendations** | Cure steps, documents needed, responsible party and timing for each curable exception |

Every finding cites its Schedule and item number or the instrument's recording information, and anything the documents don't show is listed as missing rather than assumed.

## Texas-specific coverage

- **Homestead:** urban and rural classification, spousal joinder, abandonment
- **Community property:** presumptions, separate property tracing, partition
- **Minerals:** severance, leases, executive rights, NPRIs, pooling
- **Water rights:** surface water permits, groundwater rule of capture, GCDs
- **Entities:** LLC, corporation, partnership and trust authority
- **Probate:** muniment of title, independent administration, heirship, transfer on death deeds
- **Surveys:** ALTA/NSPS surveys under the 2026 edition (effective Feb 23, 2026) or the 2021 edition for earlier surveys, T-47 affidavits, survey exception amendments

## Add the Texas Title Examination Standards

The skill's primary authority is the Texas Title Examination Standards, adopted by the State Bar of Texas Real Estate, Probate and Trust Law Section. This open-source copy doesn't include their text. Get them from [REPTL](https://reptl.org/texas-title-examination-standards) or your copy of Vernon's and add them to [`references/tx-exam-standards.md`](references/tx-exam-standards.md), which explains how. Until then the skill cites standards by number from its quick reference, checked against REPTL's February 2024 table of contents, and asks you to confirm each one.

## Files

```
tx-title-analysis/
├── SKILL.md                          the instruction
├── references/                       knowledge the skill applies
│   ├── tx-exam-standards.md          where you add the Texas Title Examination Standards
│   ├── tx-exceptions.md              exception analysis
│   ├── tx-requirements.md            common requirements
│   ├── tx-minerals.md                mineral interests
│   ├── tx-water-rights.md            water rights
│   ├── tx-probate.md                 probate and estate issues
│   ├── tx-entities.md                entity authority
│   ├── tx-foreclosure.md             foreclosure and lien priority
│   ├── tx-survey.md                  survey analysis (ALTA/NSPS 2026 and 2021)
│   ├── tx-forms.md                   Texas title forms and endorsements
│   ├── tx-data-schema.md             data schema documentation
│   └── tx-quality-checklist.md       pre-delivery checklist
├── assets/                           templates and fictional examples
│   ├── tx-opinion-template.md
│   ├── title-analysis-schema.json
│   └── examples/
└── evals/                            a fictional commitment and its answer key (not uploaded with the skill)
```

## Data export

The skill can export its analysis as JSON (primary), flattened CSV or Excel, or XML. See [`assets/title-analysis-schema.json`](assets/title-analysis-schema.json) and [`references/tx-data-schema.md`](references/tx-data-schema.md).

## Run it

See [Run anywhere](../docs/run-anywhere.md). **Data:** a title file holds personal information about owners and borrowers. Run it only in a tool your firm has approved for client material. The reference files are large, so hosted runners with file limits may need only the references your practice uses.

## Test it

[`evals/evals.json`](evals/evals.json) runs the skill on [a fictional commitment](evals/fictional-commitment-01.md) and checks the result against [its answer key](evals/expected-01.md).

## Changelog

- 1.1.0 (2026-11-17): new folder layout (`references/`, `assets/`, `evals/`); inputs, evidence rules and a pre-delivery check in SKILL.md; standard numbers corrected against REPTL's published table of contents; survey reference updated for the 2026 ALTA/NSPS standards; the standards' text left for you to add; tool-neutral output instructions; a fictional eval.
- 1.0.0 (February 2026): first release.
