# Litigation Writing

Six agent skills for drafting litigation documents the way a careful litigator does. One skill plans the papers for a step in a case and keeps the facts in one matter file; five draft the documents: pleadings, evidence (affidavits, affirmations, declarations, witness statements), submissions (skeletons, briefs, hearing notes, openings, closings, appeals, costs), advice, and letters to the other side. They cover Hong Kong and US courts (federal, New York, California, Washington, and Delaware's Superior Court and Court of Chancery).

Every skill asks for what it needs, marks anything missing with a plain placeholder such as `[date]` or `[Bundle ref]`, never invents a case, citation or paragraph number, and runs a checker on its own draft before handing it back.

The skills install as a plugin in Claude Code, Codex and the ChatGPT desktop app, work as plain skill folders anywhere that reads `SKILL.md`, and can be used from any AI assistant by pointing it at this repository (see [Use with any AI assistant](#use-with-any-ai-assistant)).

> These skills help lawyers draft. They are not legal advice and do not replace a lawyer's judgement. Check every draft, every authority and the current rules of your court before filing anything.

## The skills

| Skill | What it does | Variants |
|---|---|---|
| `litigation-writing` | Start here. Takes in the matter, keeps the matter file, plans the package of documents a step needs, routes each to the right skill, and drafts the summons or notice of motion and the draft order | `package`, `summons`, `draft-order` |
| `litigation-pleadings` | Statement of claim or complaint, defence or answer, reply, counterclaim, and amendments | `claim`, `defence`, `reply`, `counterclaim`, `amendment` |
| `litigation-evidence` | Affirmations, affidavits and declarations in the witness's own voice; witness statements; enforcement evidence | `affirmation`, `reply-affirmation`, `witness-statement`, `enforcement`, `procedural`, `non-party` |
| `litigation-submissions` | Skeleton submissions or briefs, replies, hearing and speaking notes, trial openings and closings, appeals, costs, lists of authorities, chronologies | `skeleton`, `reply`, `hearing-note`, `speaking-note`, `trial-opening`, `trial-closing`, `appeal-leave`, `appeal`, `costs`, `authorities-list`, `chronology` |
| `litigation-advice` | Counsel's advice on the merits, on pleadings and causes of action, or before action | `merits`, `pleadings`, `pre-action` |
| `litigation-correspondence` | Letters to the other side: request for particulars, demand, proposal, rule-based offer, covering letter | `particulars-request`, `demand`, `proposal`, `offer`, `covering` |

### Choosing a skill

Name a skill, or describe the task and let the assistant choose. Each description ends with a "Not for:" line that points to the right sibling. If you are not sure what papers a step needs, start with `litigation-writing`: it plans the package and hands each document over.

## How the skills work

**Who is speaking.** A lawyer drafts every one of these documents, but the voice changes with the document, and each skill holds its voice:

- A **pleading** states the party's case in the third person: material facts, not evidence, law or argument.
- **Evidence** is the witness's own first-person account, in words the witness would use and could defend under cross-examination. Law appears only as "I am advised and verily believe" and is left to counsel.
- **Submissions** are counsel's advocacy, impersonal and addressed to the court, with every fact tied to the record.
- **Advice** is counsel's own opinion in the first person, candid and hedged, with no numeric odds.
- **Letters** speak for the firm ("We refer to …").

The checker tests each boundary: an affidavit that says "It is submitted" fails, and so does a pleading that cites a case.

**Fields, not guesses.** Each document is built from fields: the court, the parties, the hearing, the application, the dates, the sums, the bundle references, the authorities. A skill asks once, grouped, for the fields it needs, and keeps them in a `matter.json` in your case folder so that a summons, its affidavit and the skeleton all use the same facts. Anything you have not supplied becomes a placeholder from a fixed list (`[date]`, `[name]`, `[sum]`, `[Plaintiff]`, `[the Child]`, `[Bundle ref]`, `[exhibit]`, `[counsel-name]`, `[statutory provision]` and so on), numbered when the same kind recurs (`[date 1]`, `[date 2]`). Every draft with a placeholder ends with a "FIELDS TO COMPLETE" table.

**Authorities.** A skill cites only authorities you supplied, or ones you asked it to verify against an official source. It never invents a case name, citation, paragraph number, judge or rule. Where an argument needs authority you have not given, it writes `[authority needed: <the proposition>]`. It does not choose which statute or rule applies; that is yours. Run the checker with your matter file and it fails any citation that is not on your list.

**Jurisdictions.** Each court system has a profile: document names, the pleading standard, how a defence or answer is framed, how evidence is sworn or declared (with the statutory words), how amendments are shown, the formal rules for papers, word limits, and citation style. The drafting moves stay the same everywhere; the profile changes what the court requires. The profiles state the rules as researched in October 2026 from official sources and mark anything not verified. Rules change: check the current rules, local rules and standing orders before filing.

**The voice.** Short, direct sentences; every paragraph numbered; defined terms in brackets at first use; concessions made into an alternative ("taken at its highest (which is denied)"); no recap at the end; the order sought drafted in full. The skills keep out the tells that mark machine-written prose (dashes used as punctuation, stock phrases such as "it is important to note", groups of three, antitheses, set-piece imagery), and keep the profession's set formulae word for word.

**The checker.** `scripts/litcheck.py` ships in every skill. `check` tests structure, voice, register, jurisdiction formalities, placeholders and citations; `fields` lists the fields a document needs. It is one Python file with no dependencies.

## Install

The repository is a marketplace for both Claude Code and Codex.

### Claude Code

Add the marketplace, then install the plugin:

```bash
claude plugin marketplace add 3orionkings/litigation-writing
```

```bash
claude plugin install litigation-writing@litigation-writing
```

Inside a session the same steps are `/plugin marketplace add 3orionkings/litigation-writing` and `/plugin install litigation-writing@litigation-writing`. The skills then appear as `/litigation-writing:litigation-pleadings` and so on, and they also load on their own when a request matches. Run `claude plugin marketplace update litigation-writing` to pick up a new release.

### Codex and the ChatGPT desktop app

```bash
codex plugin marketplace add 3orionkings/litigation-writing
```

```bash
codex plugin add litigation-writing@litigation-writing
```

Or install it from the plugin browser: type `/plugins` in Codex, or open the Plugins tab in the Codex or ChatGPT desktop app. Start a new session afterwards. Type `@` to call a skill by name, or describe the document. Run `codex plugin marketplace upgrade litigation-writing` to pick up a new release.

### As plain skill folders

```bash
git clone https://github.com/3orionkings/litigation-writing.git
```

For Claude Code, copy the skills into your personal skills folder:

```bash
cp -R litigation-writing/plugins/litigation-writing/skills/. ~/.claude/skills/
```

For Codex and other agents that read `~/.agents/skills`:

```bash
mkdir -p ~/.agents/skills && cp -R litigation-writing/plugins/litigation-writing/skills/. ~/.agents/skills/
```

For claude.ai or another tool that takes uploaded skills, build one zip per skill with `python3 tools/package.py` and upload the files from `dist/`.

## Use with any AI assistant

Every skill is a folder of plain Markdown with a `SKILL.md` at the top, so any assistant that can read a web page or a file can use one. [`llms.txt`](llms.txt) is an index written for assistants.

**Pick a skill by the document you need**, then tell the assistant to read its `SKILL.md` and the files it names. Replace `<skill>` with a name from the table above:

```text
Use the <skill> skill from https://github.com/3orionkings/litigation-writing.
Read https://raw.githubusercontent.com/3orionkings/litigation-writing/main/plugins/litigation-writing/skills/<skill>/SKILL.md
and the reference files it names in the same folder, and follow them.
Jurisdiction: <hk | us-federal | ny | ca | wa | de-superior | de-chancery>.
Task: <what you need drafted>, from these facts: <your facts and notes>.
```

**Or let it choose**: point it at the main skill, which plans the papers and names the skill for each document:

```text
Read https://raw.githubusercontent.com/3orionkings/litigation-writing/main/plugins/litigation-writing/skills/litigation-writing/SKILL.md
and follow it to plan and draft the papers for: <the step in the case>.
```

**Or give it the whole repository** (an assistant with repository access, or a coding agent in a clone): ask it to read `AGENTS.md`, which tells an assistant how to choose and load a skill.

An assistant that cannot run Python still follows the rules by reading them; it just skips the automatic check. Do not paste confidential client material into an assistant or service your professional obligations do not allow.

## Using the skills

Give the assistant the material and say what you want: "Draft a defence to this statement of claim; our client's instructions are below", "Prepare the papers to oppose this summary judgment summons in the High Court", "Turn these notes into a declaration for the CFO under California law", "Draft a request for further and better particulars of paragraphs 4 to 9". Paste the pleading, the instructions, the chronology and the authorities you rely on. The skills never invent a fact or an authority.

You get the document back with any "FIELDS TO COMPLETE" table after it. Run the checker yourself on any draft:

```bash
python3 plugins/litigation-writing/skills/litigation-pleadings/scripts/litcheck.py check draft.md --variant defence --jurisdiction hk
```

```bash
python3 plugins/litigation-writing/skills/litigation-submissions/scripts/litcheck.py fields --variant skeleton --jurisdiction ny --matter matter.json
```

`litcheck.py variants` lists a skill's variants; `--json` gives a machine-readable report; `--matter matter.json` checks every citation against your authorities.

## Limits

- The checks are mechanical. They catch missing parts, the wrong voice, banned punctuation, unfilled gaps and unsupported citations. They do not judge whether the law or the argument is right.
- The Hong Kong forms were derived from a close study of filed work. The US forms were built from the rules (quoted, with sources, in the profiles) and the same drafting moves, not from US filings, so check them against your court's practice with particular care.
- The jurisdiction profiles reflect the rules as researched in October 2026. Courts, rules and standing orders change; the profiles list what could not be verified.
- The skills and their examples are written in British English.

## Privacy

Keep `matter.json`, drafts and client documents in your own files. Never put them in a public issue or pull request. When reporting a problem, use an invented example that shows the same thing. The `.gitignore` excludes `matter.json`.

## Development

```text
plugins/litigation-writing/     the plugin: manifests for each harness, and skills/
  skills/<name>/                        SKILL.md, references/, scripts/, assets/, style.json, agents/openai.yaml
shared/                                 the one source for litcheck.py, the shared references, the profiles and the rule files
tools/                                  sync_shared.py, validate.py, package.py
tests/                                  run_tests.py and the test cases
docs/                                   architecture.md, style-json.md
.claude-plugin/marketplace.json         Claude Code marketplace
.agents/plugins/marketplace.json        Codex and ChatGPT marketplace
llms.txt                                index for AI assistants
```

Edit shared files in `shared/`, never the copies inside a skill, then copy them out and run the checks:

```bash
python3 tools/sync_shared.py
```

```bash
python3 -I -B tests/run_tests.py
```

```bash
python3 tools/validate.py
```

[CONTRIBUTING.md](CONTRIBUTING.md) covers changes and releases. [AGENTS.md](AGENTS.md) is the same material for AI assistants and coding agents. [docs/architecture.md](docs/architecture.md) explains how the pieces fit, and [CHANGELOG.md](CHANGELOG.md) lists the releases.

## License

[MIT](LICENSE).
