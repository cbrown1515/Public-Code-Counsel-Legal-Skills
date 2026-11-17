# How every skill here is built

Every skill in this repo follows the same anatomy, so it runs the same way in Claude, ChatGPT, Gemini, coding agents and hosted runners such as AppletHub, and so anyone can check its work.

## The folder

```
skill-name/
├── SKILL.md       the instruction the model follows
├── references/    knowledge to apply: playbooks, standards, checklists, definitions
├── assets/        templates the output follows, and fictional examples
├── evals/         fictional test cases with answer keys
└── README.md      for people: what it does, inputs, outputs, how to run and test it
```

`tools/package_skill.py` zips `SKILL.md`, `references/` and `assets/` for upload. `README.md` and `evals/` stay out of the zip: they are for people and testers, not for the model.

## The frontmatter

```yaml
---
name: skill-name            # lowercase and hyphens, same as the folder
description: >-             # what it does and when to use it, in one paragraph (1,024 characters at most)
license: MIT
metadata:
  author: Code + Counsel
  version: "1.0.0"
  updated: "2026-11-17"
---
```

Keep to the Agent Skills fields (`name`, `description`, `license`, `metadata`, `compatibility`, `allowed-tools`). Some platforms reject anything else.

## The instruction blocks

`SKILL.md` uses the same blocks in the same order. They match how AppletHub structures an Applet's instruction, so a skill imports there cleanly, and they read well in every other tool.

| Block | What it holds | Why |
|---|---|---|
| **Role** | Who the model is for this task, in a sentence or two. | Sets the standard of care. |
| **Task** | What to produce, in one sentence. | Keeps the run on one job. |
| **Inputs** | Numbered inputs, each marked required or optional, with what an empty one means. | Hosted runners turn these into form fields, and the model never guesses a missing input. |
| **Output** | The exact layout, pointing to a template in `assets/`, and "write nothing after it". | Results you can compare, check and paste. |
| **Method** | Numbered steps, each with its decision rule. | The same input gets the same treatment every run. |
| **Evidence rules** | How to quote, cite and mark what isn't there. | Every point rests on text a person can check. |
| **Before you answer: check** | The checks the model runs on its own draft. | Catches the commonest misses before you see them. |
| **Files** | Each file in `references/` and `assets/`, and when to use it. | The model loads what it needs, when it needs it. |

Interview skills, such as the NDA Playbook Builder, add **Interview rules**: one question per message, choices the attorney can answer with a number, and no position the attorney didn't give.

## Evidence first

- Quote the source exactly, and say where the quote is (clause, page, schedule item).
- When something isn't there, say *Not found* and where you looked. Never fill the gap.
- Never cite an authority from memory. Cite only what the document or a reference file shows.
- Never let the model vouch for something it can't see, such as whether a case exists or is good law.
- List what wasn't checked, so the attorney knows where the review stops.

A prompt can ask for all of this but can't guarantee it, so every output is a draft for a person to check.

## The attorney decides

Skills that capture an attorney's positions, such as a playbook, never fill a gap with their own view. A clause type the attorney didn't answer stays open. A common position the model offered and the attorney picked is marked **suggested, accepted**.

## Test before you share

- Each skill ships with fictional test cases in `evals/`: an input with planted problems and an answer key.
- Every file in `evals/` says **Fictional** at the top. No client data, real people or real matters, ever.
- `python3 tools/check_skills.py` checks the format, the file references, the eval files, and that every quote in an answer key appears word for word in its test document.
- Run the evals after every change, bump `metadata.version`, and add a changelog line to the README. Share a version only after it passes.

## Size

Keep `SKILL.md` under 500 lines and put detail in `references/`. Hosted runners limit how much they load: AppletHub allows about 40 pages of Skill files on its free plan and 150 on Plus (a page is about 500 words). `tools/check_skills.py` warns when a skill runs over 40.
