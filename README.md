# Code + Counsel: Get Started Building Legal AI Skills

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Platform: Multi-LLM](https://img.shields.io/badge/Platform-Claude%20%7C%20ChatGPT%20%7C%20Codex%20%7C%20Gemini-green.svg)](#platform-compatibility)
[![Skills](https://img.shields.io/badge/Skills-Legal-purple.svg)](#available-skills)

**Everything you need to start turning your legal expertise into portable, shareable AI skill files. No code required.**

If you've ever thought *"I wish my AI tool actually followed our firm's workflow instead of guessing"*, this repo is your starting point. It includes working skill files you can use right away, plus the patterns and structure you need to build your own.

## What's a legal skill file?

A skill file is a plain-text instruction set that teaches an AI assistant to do expert-level work the way *you* do it. Not a one-line prompt. An entire expertise system:

- **Inputs:** what the skill needs from you, and what it does when something is missing
- **Workflow logic:** step-by-step decision paths, each with its rule
- **Reference standards:** your playbook, checklists and standards, cited by name
- **Output templates:** opinion letters, checklists, issue tables and memos
- **Evidence rules:** every point quotes its source, and anything missing is marked as missing
- **Quality checks:** what the AI checks before you see the result
- **Tests:** fictional cases with answer keys, so you can see it works before you rely on it

One folder turns a general-purpose LLM into a domain-specific legal co-pilot that follows *your* process.

## Start here

**Want to use a skill right now?** Download any skill folder below, add it to your AI tool, and start working. Each one includes a README with its inputs, outputs and setup.

**Want to build your own?** Copy the [skill template](docs/skill-template/), read [how every skill here is built](docs/skill-anatomy.md), and swap in your practice area's logic and standards.

## Available Skills

| Skill | Jurisdiction | What it does |
|-------|-------------|--------------|
| [NDA Playbook Builder](./nda-playbook-builder/) | Any | Interviews you, one question at a time, and writes your NDA playbook: preferred positions, fallbacks, red lines and reasons |
| [NDA Review](./nda-review/) | Any | Reviews an NDA against your playbook; every issue quotes the clause it rests on, and clauses your playbook doesn't cover are listed for you |
| [Citation Checklist](./citation-checklist/) | US | Before you file: every authority, quotation and short form in your brief, with flags for problems the document shows. It never says a case exists; it gives you the list to check |
| [TX Title Analysis](./tx-title-analysis/) | Texas | Title commitment review, Schedule B exception analysis, DRAFT title opinions and requirements checklists |

The NDA Playbook Builder and NDA Review work as a pair: build your playbook, then review against it.

## How it works

```
Your expertise          →  SKILL.md file  →  AI follows your workflow
                                          →  Output that quotes its sources
                                          →  Works on any platform
```

1. **Download** a skill folder (or create your own)
2. **Add it** to your AI tool
3. **Give it** the inputs listed in its README
4. **Get DRAFT output** that follows the skill's workflow and shows its sources, ready for your review

That's it. No API keys, no fine-tuning, no engineering team.

## Platform compatibility

Every skill is an [Agent Skills](https://agentskills.io/specification) folder and works on any platform that accepts skills, system instructions or knowledge files:

| Platform | How to install |
|----------|---------------|
| **Claude apps** (web and desktop) | Upload the zipped skill folder as a custom skill |
| **Claude Code** | Place in `.claude/skills/` |
| **Codex, Cursor, GitHub Copilot, Gemini CLI** | Place in `.agents/skills/` |
| **ChatGPT** | In a Project: `SKILL.md` as the instructions, the other files as project files |
| **Google Gemini** | Add as a skill in the Gemini app (Gems are moving into skills) |
| **AppletHub** | Import the zipped skill folder and run it in a browser, or share it as an Applet |
| **Any LLM** | Use `SKILL.md` as a system prompt with the reference files as context |

`python3 tools/package_skill.py <skill>` makes the zip. Details, and what you can safely put into each tool, are in [Run anywhere](docs/run-anywhere.md).

## Test before you trust

Every skill ships with fictional test cases in its `evals/` folder: a document with planted problems and an answer key. Run the skill on the test case and compare. Before you share a change:

```
pip install skills-ref pyyaml      # optional: adds the Agent Skills spec validator
python3 tools/check_skills.py      # format, file references, fictional test data, answer-key quotes
```

## Who this is for

You don't need to be a developer. If you can write an email, you can build a skill file.

**Attorneys and paralegals:** get AI that follows your workflow, not the other way around. **Solo practitioners and small firms:** BigLaw-quality output without the headcount. **Legal ops teams:** standardize AI-assisted workflows across your department. **Legal knowledge engineers:** open-source building blocks for expertise systems. **Law students:** learn practice-area workflows from real-world examples.

## Build your own skill

Every skill in this repo follows the same structure. Start from the [template](docs/skill-template/):

```
your-skill-name/
├── SKILL.md       ← the instruction: role, task, inputs, output, method, evidence rules, checks, files
├── references/    ← your playbook, standards, checklists
├── assets/        ← output templates and fictional examples
├── evals/         ← fictional test cases with answer keys
└── README.md      ← what it does and how to run it
```

The key insight: **SKILL.md is just a structured document describing how you do your work.** Write down your process, add your references, include a template for good output and a test case, and the AI follows along.

## Why skill files beat prompt templates

| | Prompt template | Skill file |
|---|---|---|
| **Scope** | Single instruction | Complete expertise system |
| **References** | None | Your playbook, standards and checklists |
| **Output quality** | Variable | Consistent, template-driven, sources quoted |
| **Portability** | One platform | Any LLM |
| **Testing** | Try it and hope | Fictional test cases with answer keys |
| **Version control** | Hard to track | Git-native |
| **Collaboration** | Copy-paste | Fork, edit, PR |
| **Evolution** | Rewrite from scratch | Update incrementally |

## Contributing

Built a skill file for your practice area? We'd love to include it. See [CONTRIBUTING.md](CONTRIBUTING.md): follow the template, use fictional test data only, include an eval with an answer key, and run the checks before you open a pull request.

## Disclaimer

> **All skill files in this repository and all outputs they generate are provided for informational and educational purposes only and do not constitute legal advice.** Every document produced by these skills is DRAFT work product intended for review, revision, and approval by a licensed attorney before any reliance or distribution.
>
> **AI-assisted legal analysis is not a substitute for the independent professional judgment of a qualified attorney. Use of these skill files does not create an attorney-client relationship. See individual skill READMEs for jurisdiction-specific disclaimers.**

## License

MIT. Adapt to your jurisdiction, practice area, and professional standards.

## Keywords

Legal AI skills, legal automation, AI for lawyers, AI for paralegals, legal knowledge engineering, legal workflow automation, LLM legal tools, Claude skills, Agent Skills, ChatGPT, legal prompt engineering, no-code legal AI, legal tech open source, law firm AI, legal operations, document automation legal, contract review AI, NDA review AI, NDA playbook, negotiation playbook, citation checking, cite check, verify citations before filing, title examination AI, legal opinion automation, legal risk assessment, attorney AI tools, legal co-pilot, AI legal assistant, legal document generation, structured legal analysis, legal decision logic, portable legal AI, multi-platform legal AI, legal skill files, AppletHub, open source legal tools, law firm technology, legal innovation, access to justice technology, legal knowledge management, how to build legal AI, getting started legal AI, legal AI tutorial, build your own legal AI
