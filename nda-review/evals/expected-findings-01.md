# Expected findings: fictional NDA 01 (for evals only)

> **Fictional.** The answer key for `fictional-nda-01.md`, reviewed for Copperfin Robotics, Inc., with "Will the client share its own information?" set to **Yes** and no playbook given, so the review uses the fictional default playbook in `references/nda-playbook.md`.

**Client's side:** both (mutual NDA). **Structure:** mutual. **Overall:** Red.

## Must fix (4)

| Clause | Quote that must appear | Playbook basis |
|---|---|---|
| 3. Exclusions | "is received from a third party who is free to disclose it" (and no independent-development exclusion anywhere) | exclusions: red line, missing independent-development exclusion when our client receives |
| 7. Term | "shall survive for five (5) years after the expiration or termination of this Agreement" | term-and-survival: red line, longer than 3 years |
| 9. Non-Solicitation | "solicit for employment or hire any employee of the other party" | non-solicitation: red line |
| 10. Indemnification | "Each party shall indemnify and hold harmless the other party" | indemnity: red line |

## Should fix (6)

| Clause | Quote that must appear | Playbook basis |
|---|---|---|
| 2. Confidential Information | "whether or not marked as confidential" | definition: outside preferred and fallback |
| 4. Use and Disclosure | "may disclose it only to its employees who need to know it" | permitted-recipients: outside fallbacks (no advisers) |
| 6. Compelled Disclosure | "it shall first obtain a protective order covering such Confidential Information before making any disclosure" | compelled-disclosure: protective order duty, and no notice right |
| 8. Return of Information | "shall promptly return or destroy all Confidential Information and all copies" | return-or-destruction: no legal or backup exception |
| 11. Residual Knowledge | "retained in the unaided memory of its personnel" | residuals: any residuals clause when our client discloses |
| 12. Remedies | "may seek injunctive relief without posting a bond" | remedies: waiver of bond |

## Note (3)

| Clause | Quote or absence | Playbook basis |
|---|---|---|
| 16. Governing Law | "governed by the laws of the State of New York" | governing-law-and-forum: fallback, any US state |
| 15. Assignment | "Neither party may assign this Agreement without the prior written consent of the other party." | assignment: fallback 1 |
| (none) | Not found in the NDA: no publicity or no-obligation clause | publicity-and-no-obligation: if silent, Note |

## Not covered by the playbook (1)

| Clause | Quote that must appear |
|---|---|
| 13. Compliance Audits | "the Disclosing Party may audit the Receiving Party's facilities and systems" |

## Checked and consistent

nda-structure (preamble), purpose-and-use (1), standard-of-care (5), no-license-and-no-warranty (14), general-provisions (17).

## Could not check

- Exhibit A (the controller specifications named in the Purpose) is not attached.

## Must not appear

- A whistleblower-immunity-notice issue: both parties are companies, so that position doesn't apply.
- Any quote that is not word for word in the NDA.
- A rating of the audit clause as Must fix, Should fix or Note.
