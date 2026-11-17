# NDA Playbook Builder

Turn how you negotiate NDAs into a written playbook in 10 to 15 minutes. The skill interviews you one question at a time, then writes your preferred positions, fallbacks, red lines and reasons for each clause type.

The playbook it writes is the input the [NDA Review](../nda-review/) skill reads, so your review follows your rules instead of a generic checklist.

> Draft work product for attorney review. Not legal advice. You decide every position.

## What you give it

| Input | Required | Notes |
|---|---|---|
| Which side you usually represent | No | Disclosing party, receiving party, or either. Asked first if you leave it empty. |
| Your NDA template or notes | No | Your own form or notes. The builder drafts positions from them, quotes its sources, and asks only about the gaps. |
| Your practice | No | One line on your usual clients and deals. No client names. |

Then answer its questions in the conversation. Answer "skip" to leave a clause type open; it goes under **No position yet**.

## What you get

A Markdown playbook following [`assets/playbook-template.md`](assets/playbook-template.md):

- one block per clause type: applies when, preferred, fallbacks in order, red line, what to do if the NDA is silent, why, your wording, and the source of the position;
- **No position yet:** clause types you skipped, which the review escalates to you;
- **Open questions:** positions that depend on facts, with what they depend on.

See a finished example for a fictional practice in [`assets/example-playbook.md`](assets/example-playbook.md).

## How it stays yours

- It never fills a gap with its own position. A clause type you don't answer stays open.
- When it offers common positions as choices and you pick one, the playbook marks it **suggested, accepted**.
- Positions drawn from your template quote the clause they came from.

## Files

```
nda-playbook-builder/
├── SKILL.md                         the instruction
├── references/nda-clause-types.md   clause types, questions and common positions
├── assets/playbook-template.md      the playbook layout
├── assets/example-playbook.md       a fictional finished playbook
└── evals/                           a fictional attorney persona and the checks (not uploaded with the skill)
```

## Run it

See [Run anywhere](../docs/run-anywhere.md) for Claude, ChatGPT, Gemini, Codex and AppletHub. On AppletHub this skill runs as a chat Applet; the setup is in [docs/applets/nda-playbook-builder.md](../docs/applets/nda-playbook-builder.md).

**Data:** you share your own positions, not client documents, so the interview carries little confidential material. Still don't paste client names or a client's confidential NDA.

## Test it

[`evals/evals.json`](evals/evals.json) runs the interview against a fictional attorney persona. Have a second model or a colleague play the persona and check the playbook against the answer key.

## Changelog

- 1.0.0 (2026-11-17): first release.
