# NDA Review

Review an NDA for your client against your own playbook. Every issue comes with the exact NDA text it rests on, the playbook position it breaks, and a suggested fix. Clauses your playbook doesn't cover are listed for you to decide, never dropped.

> Draft work product for attorney review. Not legal advice. Check every quote against the final document before relying on it.

## What you give it

| Input | Required | Notes |
|---|---|---|
| NDA | Yes | The full text. |
| Client | Yes | The party you advise, named as in the NDA. |
| Will the client share its own information? | No | Yes, No or Not sure. Decides whether to push for a mutual NDA. |
| Playbook | No | Your playbook from the [NDA Playbook Builder](../nda-playbook-builder/). Without one, the review uses a fictional default and says so. |

## What you get

A review following [`assets/review-template.md`](assets/review-template.md):

- **Issues:** Must fix (a red line), Should fix (outside your fallbacks) and Note (within a fallback), each with the clause, the exact NDA text, the playbook position and a suggested fix. Protections the NDA lacks show as *Not found in the NDA*, with where the review looked.
- **Not covered by the playbook:** clauses your playbook has no position on, quoted, for you to decide.
- **Checked and consistent** and **Could not check**, so you can see what the review covered.

## Why quotes matter

The skill asks the model to quote every clause it relies on and to search the NDA for each quote before answering. That makes errors easy to spot, but a prompt can't guarantee it. Check the quotes, or use a tool that verifies every quote against the source in code.

## Use your own playbook

The default in [`references/nda-playbook.md`](references/nda-playbook.md) is fictional. Build your own with the [NDA Playbook Builder](../nda-playbook-builder/) and give it as the Playbook input, or replace that file.

## Files

```
nda-review/
├── SKILL.md                         the instruction
├── references/nda-clause-types.md   clause types and how to spot them
├── references/nda-playbook.md       fictional default playbook
├── assets/review-template.md        the review layout
└── evals/                           a fictional NDA and its answer key (not uploaded with the skill)
```

## Run it

See [Run anywhere](../docs/run-anywhere.md). **Data:** an NDA from a live matter is client information. Run it only in a tool your firm has approved for client material, and keep any hosted runner's data terms in mind.

## Test it

[`evals/evals.json`](evals/evals.json) reviews [a fictional NDA](evals/fictional-nda-01.md) with planted problems and grades the result against [its answer key](evals/expected-findings-01.md).

## Changelog

- 1.0.0 (2026-11-17): first release.
