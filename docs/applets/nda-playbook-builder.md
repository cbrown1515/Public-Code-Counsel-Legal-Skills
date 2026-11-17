# Running the NDA Playbook Builder on AppletHub

How Code + Counsel sets up the [NDA Playbook Builder](../../nda-playbook-builder/) as a public Applet on [AppletHub](https://applethub.ai/help), so attorneys can run it in a browser with nothing to install. Use the same steps to host any skill in this repo.

## Why this skill runs well as an Applet

- It asks about the attorney's own positions, so no client documents go into it.
- It runs as a conversation, which AppletHub supports as a chat before the output.
- Its output, the playbook, is what the [NDA Review](../../nda-review/) skill reads, so it leads straight to the next step.

## 1. Package and import

```
python3 tools/package_skill.py nda-playbook-builder    # writes dist/nda-playbook-builder.zip
```

In AppletHub, create a new Applet, open the **Instruction** tab and choose **Import**, then **Skill folder (.zip)**. AppletHub brings in `SKILL.md`, the clause list under References and the template and example under Assets. Check the list of files it shows.

## 2. Interface

| Field | Setting |
|---|---|
| Input 1 | **Which side do you usually represent?** Choice: Disclosing party, Receiving party, Either. Optional. |
| Input 2 | **Your NDA template or notes.** Long text, file upload allowed (Word, PDF, text). Optional. Help text: "Your own form or notes, not a client's NDA." |
| Input 3 | **Your practice.** Short text. Optional. Help text: "One line on your usual clients and deals. No client names." |
| Chat before the output | On. This is the interview. Allow about 80 messages: the core playbook takes up to 40 questions. |
| Output | **Your NDA playbook.** Text output. Explanation: "Your positions for each clause type, ready to use with the NDA Review skill or any AI review tool." |
| Follow-up chat | On, about 10 messages, for changing a position after the playbook is written. |

## 3. Tools

Model: Claude Sonnet 5.5 (AppletHub's default). Web search: off; the interview needs none. Once it passes its test, try a lower-cost model and keep it only if the test still passes.

## 4. Test

1. On the **Test** tab, run the interview and play the fictional attorney in [`evals/persona-fictional-attorney.md`](../../nda-playbook-builder/evals/persona-fictional-attorney.md).
2. Check the playbook against the expectations in [`evals/evals.json`](../../nda-playbook-builder/evals/evals.json): one question per message, a read-back before writing, the persona's positions recorded as stated, the skipped clause under **No position yet**, and the "depends" answer under **Open questions**.
3. Save as a new version with a note. AppletHub shares only a version that has passed a test.

## 5. Share

| Setting | Choice |
|---|---|
| Who can use it | Anyone with the link (Public) |
| Price | Free |
| Who can see the Instruction | Everyone (Open source). AppletHub lists open-source Applets under CC BY 4.0; this repo is MIT. Both are permissive, and the copyright holder can offer both. |
| Examples | The fictional persona's test run only. No real positions or client material. |

## 6. Listing

- **Name:** NDA Playbook Builder
- **Description:** Answer a few questions about how you negotiate NDAs and get your own NDA playbook: preferred positions, fallbacks, red lines and the reasons behind them. Takes 10 to 15 minutes. No client documents needed. Have a lawyer review the result before relying on it.
- **Rights line:** © 2026 Code + Counsel · [open-source skill](https://github.com/cbrown1515/Public-Code-Counsel-Legal-Skills/tree/main/nda-playbook-builder)

## 7. Embed

In **Share & sell**, choose **Copy embed code** and paste it into a web page. Visitors see a card for the Applet; **Run on AppletHub** opens it.
