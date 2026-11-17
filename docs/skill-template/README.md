# Skill template

Copy this folder to start a new skill. Rename the folder and the `name` in `SKILL.md` to the same lowercase, hyphenated name, then fill in every bracket.

Read [How every skill here is built](../skill-anatomy.md) first. Before you open a pull request:

1. Replace the fictional test in `evals/` with one that plants the problems your skill must catch, and write its answer key.
2. Run `python3 tools/check_skills.py your-skill-name`.
3. Run the eval and check the result against the answer key.
4. Write the skill's README: what it does, inputs, outputs, how to run and test it, and a changelog.
