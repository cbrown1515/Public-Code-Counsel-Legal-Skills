---
name: tx-title-analysis
description: >-
  Texas title examination for residential and commercial real estate. Analyzes title
  commitments, recorded instruments, surveys, HOA documents and searches, and writes DRAFT title
  opinion letters, requirements checklists and exception cure recommendations for attorney
  review, citing the Schedule B item and quoting the document for every finding. Use for title
  commitment uploads, Schedule B exceptions, title opinion requests, clearing title for closing,
  and Texas homestead, community property, mineral, water rights, probate or entity authority
  questions on a title.
license: MIT
metadata:
  author: Code + Counsel
  version: "1.1.0"
  updated: "2026-11-17"
---

# Texas Title Analysis Skill

> ⚠️ **IMPORTANT DISCLAIMER**
>
> **THIS TOOL DOES NOT PROVIDE LEGAL ADVICE.** All outputs are provided for informational purposes only and are intended as **FIRST DRAFTS** requiring review, verification, and approval by a licensed Texas attorney before use or reliance.
>
> - All outputs are preliminary drafts, not final work product
> - This tool is a drafting assistant, not a substitute for legal counsel
> - A licensed attorney must review all outputs before any reliance
> - No attorney-client relationship is created by use of this tool
> - Laws and regulations change; verify all citations and requirements

Analyze title documents to generate DRAFT outputs that assist attorneys in their title examination work. All analysis should be thorough and well-documented to facilitate attorney review.

**Primary Authority**: This skill follows the **Texas Title Examination Standards** (Vernon's Texas Statutes and Codes Annotated, Property Code, Title 2, Appendix) as the authoritative reference for Texas title examination. The open-source copy doesn't include their text: `references/tx-exam-standards.md` explains how to add your copy. Until it holds the standards, cite them by number from the quick reference at the end of this file and ask the attorney to confirm each one.

## Inputs

1. **Title commitment** (required): the Commitment for Title Insurance or preliminary title report, with Schedules A, B-I (requirements) and B-II (exceptions).
2. **Supporting documents** (optional): recorded instruments, survey, tax certificate, HOA documents, searches, affidavits, probate or divorce records.
3. **Transaction** (optional): residential or commercial purchase, refinance, construction or equity loan, or a mineral interest, and which party the attorney represents.
4. **Outputs wanted** (optional): title opinion, requirements checklist, exception cure recommendations, or all three (the default).

## Evidence rules

- Cite every finding to its source: the Schedule and item number of the commitment, or the instrument with its recording information exactly as the document gives it.
- Quote the operative words of each exception or requirement you analyze. Never paraphrase inside quotation marks.
- Never invent recording information, dates, names or amounts. If a document doesn't give one, write "not shown in the documents provided" and add it to the requirements checklist.
- Label any conclusion that rests on a document you haven't seen as an assumption, and say which document would confirm it.
- Cite Texas Title Examination Standards only by numbers you can see in `references/tx-exam-standards.md` or the quick reference below. Never cite a standard number from memory.

## Title Analysis Workflow

1. **Identify Documents** → Catalog all uploaded documents by type
2. **Parse Commitment** → Extract Schedule A (coverage) and Schedule B (exceptions/requirements)
3. **Analyze Chain of Title** → Review vesting, conveyances, and gaps
4. **Examine Exceptions** → Classify and assess each Schedule B exception
5. **Texas-Specific Review** → Homestead, community property, minerals, water rights
6. **Generate Outputs** → Title opinion, requirements checklist, cure recommendations

## Step 1: Document Identification

Catalog uploaded documents into these categories:

| Category | Documents |
|----------|-----------|
| **Commitment** | Commitment for Title Insurance, Preliminary Title Report |
| **Recorded Instruments** | Deeds, deeds of trust, liens, releases, easements, plats, restrictions |
| **Survey** | Survey, plat, metes and bounds description |
| **Tax/Assessment** | Tax certificate, tax statement, special assessment info |
| **HOA/Restrictions** | HOA docs, CCRs, bylaws, resale certificate |
| **Searches** | Judgment search, bankruptcy search, UCC search, federal tax lien search |
| **Other** | Affidavits, death certificates, divorce decrees, probate documents |

If key documents are missing, note them in the Requirements Checklist.

## Step 2: Parse the Commitment

Extract and organize:

### Schedule A (Coverage)
- Effective date
- Proposed insured (owner and/or lender)
- Policy amounts
- Legal description
- Current vesting (who owns the property now)

### Schedule B-I (Requirements)
Number and list each requirement. Common Texas requirements:
- Payment of current taxes
- Release of existing liens
- Execution of deed/deed of trust
- HOA resale certificate
- Survey or affidavit
- Proof of entity authority (for LLCs, corporations)
- Marital status affidavit
- Heirship affidavit

### Schedule B-II (Exceptions)
Number and list each exception. Categorize as:
- **Standard Exceptions** (deletable with proper documentation)
- **Special Exceptions** (property-specific, require individual analysis)

## Step 3: Chain of Title Analysis

Review recorded instruments to verify:
- **Continuous chain**: No gaps in ownership from sovereign/root to current vesting
- **Proper conveyances**: Deeds executed correctly (grantor signature, notarization, delivery)
- **Outstanding interests**: Any unreleased liens, judgments, or encumbrances
- **Name variations**: Match names across documents (consider nicknames, middle names, suffixes)

**Red flags**:
- Gaps in chain exceeding 25 years (Texas marketable title period)
- Deeds from estates without proper probate
- Quitclaim deeds in the chain (may indicate title dispute)
- Unreleased vendor's liens or deeds of trust

## Step 4: Exception Analysis

For each Schedule B-II exception, determine:

### Classification
| Type | Description | Typical Treatment |
|------|-------------|-------------------|
| **Standard/Pre-printed** | Taxes, survey matters, rights of parties in possession | Often deletable with documentation |
| **Deed Restrictions/CCRs** | Use restrictions, architectural controls | Usually remain; review for enforceability |
| **Easements** | Utility, access, drainage | Remain unless released; assess impact |
| **Mineral Reservations** | Oil, gas, mineral rights | See `references/tx-minerals.md` |
| **Liens/Encumbrances** | Deeds of trust, judgment liens, mechanic's liens | Must be released or subordinated |
| **HOA/POA** | Assessments, maintenance obligations | Review for delinquencies |

### Impact Assessment
For each exception:
1. **Location**: Does it affect the subject property? (Check legal description)
2. **Type**: What rights does it convey or restrict?
3. **Impact**: How does it affect use, value, or marketability?
4. **Cure**: Can it be removed, insured over, or must it remain?

## Step 5: Texas-Specific Analysis

### Homestead (Tex. Prop. Code §§ 41.001-41.005)

**Urban homestead**: Up to 10 acres (family) in city, town, or village
**Rural homestead**: Up to 100 acres (single adult) or 200 acres (family)

**Analysis required**:
- Is property homestead? (Look for: occupancy, family residence, exemption filings)
- If homestead, both spouses must sign conveyance (even if only one on title)
- Homestead lien limitations: Only purchase money, taxes, improvements, home equity, or refinance
- Homestead designation affidavit may be required

### Community Property (Tex. Fam. Code § 3.002)

**Presumption**: Property acquired during marriage is community property

**Analysis required**:
- Check acquisition date vs. marriage dates
- Separate property claims require tracing (gift, inheritance, pre-marriage)
- Non-titled spouse's joinder required for community real property
- Review for separate property affidavits

### Minerals and Royalties

See `references/tx-minerals.md` for detailed analysis.

**Key points**:
- Texas follows "ownership in place" theory
- Surface estate may be severed from mineral estate
- Dominant mineral estate doctrine
- Check for existing leases, royalty interests, executive rights, NPRIs

### Water Rights

See `references/tx-water-rights.md` for detailed analysis.

**Key points**:
- Texas has a **dual water system**: state-owned surface water vs. privately-owned groundwater
- Surface water: Prior appropriation system (permit required from TCEQ)
- Groundwater: Rule of capture (owner owns in place; *Edwards Aquifer Auth. v. Day*)
- Groundwater rights are severable—check chain for reservations
- Properties in GCDs subject to local district rules and permits
- Review for water rights conveyances, reservations, or severances

## Step 6: Generate DRAFT Outputs

**CRITICAL**: All outputs must include the following header disclaimer:

```
**DRAFT - FOR ATTORNEY REVIEW**
This document is a preliminary draft prepared for informational purposes only.
It does not constitute legal advice and must be reviewed, verified, and approved
by a licensed Texas attorney before any use or reliance.
```

### Output 1: DRAFT Title Opinion Letter

If your tool can create Word documents, write the opinion as a .docx; otherwise write it in Markdown. Follow `assets/tx-opinion-template.md` for structure.

Key sections:
1. **DRAFT DISCLAIMER** (required at top of document)
2. Purpose and scope
3. Documents examined (with recording info)
4. Legal description
5. Chain of title summary
6. Current vesting
7. Requirements for clear title
8. Exception analysis with recommendations
9. Texas-specific matters (homestead, community property, minerals)
10. Opinion statement (marked as DRAFT pending attorney review)
11. Qualifications and limitations

### Output 2: DRAFT Requirements Checklist

Generate actionable checklist organized by:
- **Must Clear Before Closing** (deal-breakers)
- **Documents Needed** (source and status)
- **Payoffs Required** (lienholder and estimated amounts)
- **Affidavits/Certifications** (who signs, purpose)
- **HOA Items** (resale cert, assessment status)
- **Tax Items** (current/prior years, special assessments)
- **Remaining Exceptions** (items that cannot be cleared)

Include disclaimer: *"This checklist is a draft for attorney review. Verify all items and requirements before reliance."*

### Output 3: DRAFT Exception Cure Recommendations

For each curable exception, provide:
- Issue description
- Specific cure steps
- Documents needed
- Responsible party (Seller/Buyer/Lender)
- Timeline estimate

Include disclaimer: *"Cure recommendations are preliminary and must be verified by a licensed attorney."*

## Before you deliver: check

Work through `references/tx-quality-checklist.md`, then confirm:

- Every Schedule B-I requirement and every Schedule B-II exception in the commitment appears in the outputs, by item number.
- Every quote matches the document word for word, and every recording reference matches the document exactly.
- Nothing is stated as fact that the documents don't show; each gap is in the requirements checklist.
- Every standard cited appears in `references/tx-exam-standards.md` or the quick reference below.
- Each output carries the DRAFT disclaimer.

## Reference Files

Load these as needed for detailed guidance:

### Primary Authority
- `references/tx-exam-standards.md` - **Texas Title Examination Standards**. Holds your copy of the standards once you add it (see that file). Consult it for all substantive title questions.

### Topic-Specific References
- `references/tx-minerals.md` - Mineral and royalty interest analysis
- `references/tx-forms.md` - Texas title insurance forms and endorsements
- `references/tx-requirements.md` - Common requirements and satisfaction methods
- `references/tx-exceptions.md` - Standard and special exception analysis
- `references/tx-foreclosure.md` - Foreclosure, workout, and lien priority issues
- `references/tx-probate.md` - Estate and probate title issues (heirship, muniments, TODDs)
- `references/tx-entities.md` - Entity authority analysis (LLCs, corps, trusts, POAs)
- `references/tx-water-rights.md` - Water rights analysis (surface water, groundwater, GCDs)
- `references/tx-survey.md` - Survey analysis and exception deletion
- `references/tx-quality-checklist.md` - Pre-delivery verification checklist

### Templates and Sample Outputs (fictional)
- `assets/tx-opinion-template.md` - Title opinion letter template
- `assets/examples/sample-title-opinion.md` - Example draft title opinion format
- `assets/examples/sample-requirements-checklist.md` - Example requirements checklist
- `assets/examples/sample-exception-analysis.md` - Example exception analysis

### Data Integration
- `assets/title-analysis-schema.json` - JSON Schema for structured data export
- `assets/examples/sample-analysis-record.json` - Sample analysis record in JSON format
- `references/tx-data-schema.md` - Schema documentation with field definitions and CSV mapping

Use the data schema to export analysis results to case management systems. The schema supports JSON (primary), CSV/Excel (flattened), and XML (legacy) formats.

### Key Standards Quick Reference
Standard numbers and titles as printed in the table of contents of the Texas Title Examination Standards PDF REPTL published in February 2024 (checked Nov 17, 2026). Confirm each against the current edition and its updates:
- **Marketable title**: Standard 2.10 (Marketable Title Defined)
- **Name variances**: Standards 3.10 to 3.70 (3.10, Idem Sonans)
- **Recording and notice**: Standards 4.40 (Notice Recording System) and 4.50 (Constructive Notice). Texas has a notice system, not race-notice.
- **Powers of attorney**: Standard 8.10 (Validity of Instrument Executed by an Agent)
- **Trustees**: Standard 9.10 (Powers of Trustee)
- **Decedents' estates**: Chapter XI, including 11.30 (Conveyances by an Executor or an Independent Administrator), 11.70 (Heirship Affidavits) and 11.110 (Transfer on Death Deed)
- **Community property**: Standards 14.10 (Community Property Presumption), 14.60 and 14.70 (joinder)
- **Homestead**: Standard 14.90 (Homestead)
- **Liens**: Standards 15.20 (Involuntary Mechanic's, Contractor's, and Materialman's Liens), 15.30 (Judgment Liens), 15.90 (Lien Priority and Subordination) and 15.110 (Lis Pendens)
- **Foreclosure**: Standards 16.10 (Nonjudicial Foreclosure) and 16.20 (Judicial Foreclosure and Execution Sales)
- **Adverse possession**: Standards 18.10 to 18.30
