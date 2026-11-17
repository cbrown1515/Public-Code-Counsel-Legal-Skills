# Run anywhere

Each skill is an [Agent Skills](https://agentskills.io/specification) folder: `SKILL.md` plus `references/` and `assets/`. To make an upload file, run:

```
python3 tools/package_skill.py nda-review      # writes dist/nda-review.zip
```

## Where to put it

| Tool | How |
|---|---|
| **Claude apps** (web and desktop) | Upload the zip where your plan lets you add custom skills. |
| **Claude Code** | Copy the folder into `.claude/skills/` in your project, or `~/.claude/skills/` for every project. |
| **Codex, Cursor, GitHub Copilot, Gemini CLI and other coding agents** | Copy the folder into `.agents/skills/` in your project. |
| **ChatGPT** | In a Project, paste `SKILL.md` into the project instructions and add the `references/` and `assets/` files as project files. Custom GPTs retire on Dec 11, 2026, so don't start new ones. |
| **Gemini app** | Add it as a skill; Gems are moving into skills. If you use both the Gemini app and Workspace, install it in each, because skills don't sync between them. |
| **AppletHub** | On a new Applet's Instruction tab, choose Import, then Skill folder (.zip). Set the Interface from the skill's Inputs section, test it, and share it. See [the NDA Playbook Builder setup](applets/nda-playbook-builder.md) for a worked example. |
| **Any other model** | Use `SKILL.md` as the system prompt and attach the reference and asset files. |

Platforms change quickly. These notes were checked in November 2026.

## What you can put where

- **Test with fictional or public material first.** Every skill's `evals/` folder has a fictional case to start with.
- **Client documents are client information.** Run a skill on them only in a tool your firm has approved for client material, under terms you have reviewed (data retention, training, where processing happens).
- **Hosted runners send your inputs to model providers.** AppletHub, for example, says it runs on Anthropic, OpenAI and Google business APIs, that nothing is used for training, and that providers typically keep data for about 30 days under their own terms; open models may be processed outside the United States, and it isn't HIPAA compliant. Read the current terms before you decide.
- **Interview skills carry the least risk.** The NDA Playbook Builder asks about your own positions, not your clients' documents.
