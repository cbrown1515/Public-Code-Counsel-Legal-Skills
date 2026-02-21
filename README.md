# Code & Counsel — Get Started Building Legal AI Skills

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Platform: Multi-LLM](https://img.shields.io/badge/Platform-Claude%20%7C%20ChatGPT%20%7C%20Codex%20%7C%20Gemini-green.svg)](#platform-compatibility)
[![Skills](https://img.shields.io/badge/Skills-Legal-purple.svg)](#available-skills)

**Everything you need to start turning your legal expertise into portable, shareable AI skill files — no code required.**

If you've ever thought *"I wish my AI tool actually followed our firm's workflow instead of guessing"* — this repo is your starting point. It includes working skill files you can use immediately, plus the patterns and structure you need to build your own.

## What's a legal skill file?

A skill file is a plain-text instruction set that teaches an AI assistant to do expert-level work the way *you* do it. Not a one-line prompt. An entire expertise system:

- **Workflow logic** — step-by-step decision paths with IF/THEN branching
- **Reference standards** — statutes, rules, and professional standards cited inline
- **Output templates** — opinion letters, checklists, memos, and structured data
- **Quality checks** — review criteria to catch errors before they reach a client
- **Sample outputs** — real examples showing what the skill produces

One folder turns a general-purpose LLM into a domain-specific legal co-pilot that follows *your* process.

## Start here

**Want to use a skill right now?** Download any skill folder below, drop it into your AI tool, and start working. Each one includes a README with step-by-step setup instructions.

**Want to build your own?** Use any skill in this repo as a template. Copy the folder structure, swap in your practice area's logic and standards, and you're up and running.

## Available Skills

| Skill | Jurisdiction | What it does | Get started |
|-------|-------------|--------------|-------------|
| [TX Title Analysis](./tx-title-analysis-skill/) | Texas | Title commitment review, Schedule B exception analysis, DRAFT title opinions, requirements checklists | [README →](./tx-title-analysis-skill/README.md) |
| *More coming soon* | | | |

## How it works

```
Your expertise          →  SKILL.md file  →  AI follows your workflow
                                          →  Consistent, reviewable output
                                          →  Works on any platform
```

1. **Download** a skill folder (or create your own)
2. **Drop it** into your AI tool
3. **Upload** your documents
4. **Get DRAFT output** that follows the skill's workflow — ready for your review

That's it. No API keys, no fine-tuning, no engineering team.

## Platform compatibility

Every skill works on any platform that accepts system instructions or knowledge files:

| Platform | How to install |
|----------|---------------|
| **Claude Cowork** | Drop the skill folder into your working directory — auto-detected |
| **Claude Code** | Place in `.claude/skills/` directory |
| **ChatGPT** | Upload as Knowledge files in a Custom GPT or Project |
| **OpenAI Codex** | Add to `.codex/skills/` or reference in AGENTS.md |
| **Google Gemini** | Paste into AI Studio system instructions or create a Gem |
| **Any LLM** | Use SKILL.md as a system prompt with reference files as context |

## Who this is for

You don't need to be a developer. If you can write an email, you can build a skill file.

**Attorneys and paralegals** — get AI that follows your workflow, not the other way around. 
**Solo practitioners and small firms** — BigLaw-quality output without the headcount. 
**Legal ops teams** — standardize AI-assisted workflows across your department. 
**Legal knowledge engineers** — open-source building blocks for expertise systems. 
**Law students** — learn practice-area workflows from real-world examples.

## Build your own skill

Every skill in this repo follows the same structure — use any one as a starting point:

```
your-skill-name/
├── SKILL.md                 ← Core instruction set (start here)
├── README.md                ← Installation & usage guide
├── reference-file-1.md      ← Standards, statutes, rules
├── reference-file-2.md      ← Additional reference material
├── output-template.md       ← What the skill produces
├── quality-checklist.md     ← Review criteria
└── samples/
    └── sample-output.md     ← Example of generated output
```

The key insight: **SKILL.md is just a structured document describing how you do your work.** Write down your process, add your references, include an example of good output, and the AI follows along.

## Why skill files beat prompt templates

| | Prompt template | Skill file |
|---|---|---|
| **Scope** | Single instruction | Complete expertise system |
| **References** | None | Statutes, standards, rules inline |
| **Output quality** | Variable | Consistent, template-driven |
| **Portability** | One platform | Any LLM |
| **Version control** | Hard to track | Git-native |
| **Collaboration** | Copy-paste | Fork, edit, PR |
| **Evolution** | Rewrite from scratch | Update incrementally |

## Contributing

Built a skill file for your practice area? We'd love to include it.

1. Fork this repo
2. Add your skill folder following the structure above
3. Include sample outputs so others can see what it produces
4. Open a pull request

All contributions should include appropriate disclaimers and must not contain proprietary or confidential materials.

## Disclaimer

> **All skill files in this repository and all outputs they generate are provided for informational and educational purposes only and do not constitute legal advice.** Every document produced by these skills is DRAFT work product intended for review, revision, and approval by a licensed attorney before any reliance or distribution.
>
**> AI-assisted legal analysis is not a substitute for the independent professional judgment of a qualified attorney. Use of these skill files does not create an attorney-client relationship. See individual skill READMEs for jurisdiction-specific disclaimers.**

## License

MIT — adapt to your jurisdiction, practice area, and professional standards.

## Keywords

Legal AI skills, legal automation, AI for lawyers, AI for paralegals, legal knowledge engineering, legal workflow automation, LLM legal tools, Claude skills, ChatGPT custom GPT, legal prompt engineering, no-code legal AI, legal tech open source, law firm AI, legal operations, document automation legal, contract review AI, title examination AI, legal opinion automation, compliance AI, NDA review AI, legal risk assessment, attorney AI tools, legal co-pilot, AI legal assistant, practice management AI, legal document generation, structured legal analysis, legal decision logic, portable legal AI, multi-platform legal AI, legal skill files, open source legal tools, law firm technology, legal innovation, access to justice technology, legal knowledge management, how to build legal AI, getting started legal AI, legal AI tutorial, build your own legal AI

