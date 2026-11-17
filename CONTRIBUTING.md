# Contributing

Thanks for sharing your expertise. A skill here should work the first time someone tries it, and show its sources when it does.

## The rules

1. **Follow the anatomy.** Start from [docs/skill-template](docs/skill-template/) and read [How every skill here is built](docs/skill-anatomy.md).
2. **Fictional data only.** No client documents, client or matter names, real people, or confidential or proprietary material, anywhere: skills, references, examples or tests. Mark every file in `evals/` **Fictional** at the top.
3. **Only text you have the rights to.** Summarize standards and rules in your own words and cite them; don't paste a publisher's text or a commercial form. Tell users where to get the original.
4. **Evidence first.** Outputs quote their sources, mark what's missing as missing, and never cite an authority from memory.
5. **Include a test.** At least one fictional case in `evals/` with an answer key, listed in `evals/evals.json`.
6. **Disclaimers.** Every output is labeled as a draft for attorney review, and every README says so.

## Before you open a pull request

```
pip install skills-ref pyyaml      # optional: the Agent Skills spec validator
python3 tools/check_skills.py      # must pass
```

Then run your skill on its eval and check the result against the answer key. Bump `metadata.version` in `SKILL.md` and add a line to the changelog in the skill's README.

## Pull requests

- One skill, or one change to a skill, per pull request.
- Say what the skill does, which jurisdiction it covers, and how you tested it.
