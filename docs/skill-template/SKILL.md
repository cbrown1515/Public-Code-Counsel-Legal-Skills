---
name: skill-template
description: >-
  Replace with one paragraph: what the skill does, what it produces, and when to use it
  (the requests and documents that should trigger it). Rename the folder to match the name.
license: MIT
metadata:
  author: Your name or firm
  version: "0.1.0"
  updated: "YYYY-MM-DD"
---

# Skill Name

## Role

You are [who the model is for this task, in a sentence].

## Task

[What to produce, from what, in one sentence.] Write it in the layout of `assets/output-template.md`.

## Inputs

1. **[Input name]** (required): [what it is]. If missing, stop and ask for it.
2. **[Input name]** (optional): [what it is]. If empty, [what to do instead].

## Output

One Markdown document following `assets/output-template.md`. Write nothing after it.

## Method

### Step 1: [Read]

[What to read first and what to find.]

### Step 2: [Decide]

[Each decision, with the rule for it. Point to the reference that holds the rule.]

### Step 3: [Write]

Fill `assets/output-template.md`.

## Evidence rules

- Quote the source exactly, and say where each quote is.
- If something isn't in the source, write *Not found* and where you looked.
- Never cite an authority from memory.

## Before you answer: check

- Every quote appears in the source word for word.
- Every required part of the template is filled.
- [The check that catches this task's commonest miss.]

## Files

- `references/your-reference.md`: [the knowledge it holds, and when to use it].
- `assets/output-template.md`: the layout of the output. Follow it exactly.
