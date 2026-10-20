# AGENTS.md

Two kinds of reader land here: an AI assistant asked to **use** these skills to draft a litigation document, and a coding agent asked to **change** this repository. The first part is for the first; the rest is for the second. [CONTRIBUTING.md](CONTRIBUTING.md) says the same for people.

## Using the skills (for any AI assistant)

You have been pointed at a repository of six litigation writing skills. Each skill is a folder under `plugins/litigation-writing/skills/` with a `SKILL.md` that tells you what to do, `references/` that hold the detail, `assets/` that hold the rule files, and `scripts/litcheck.py`, a checker you can run if you can execute Python.

1. **Choose the skill** by the document the user needs:

   | The user needs | Skill |
   |---|---|
   | Papers for a step in a case, or does not know which documents; a summons, notice of motion or draft order | `litigation-writing` |
   | A statement of claim or complaint, defence or answer, reply, counterclaim, or an amendment | `litigation-pleadings` |
   | An affirmation, affidavit, declaration, witness statement, or enforcement evidence | `litigation-evidence` |
   | Skeleton submissions or a brief, a reply, hearing or speaking note, trial opening or closing, appeal or costs submissions, a list of authorities, a chronology | `litigation-submissions` |
   | Counsel's advice or opinion | `litigation-advice` |
   | A letter to the other side: request for particulars, demand, proposal, offer, covering letter | `litigation-correspondence` |

2. **Read that skill's `SKILL.md`** in full and follow it. Then read the reference files it names for the variant and the jurisdiction, and no others: each skill is self-contained, and the shared files (`references/fields.md`, `voice.md`, `authorities.md`, `matter-file.md`, `jurisdictions.md`, `references/jurisdictions/<code>.md`) are identical in every skill.
3. **Ask for the jurisdiction** if the user has not given it: `hk`, `us-federal`, `ny`, `ca`, `wa`, `de-superior` or `de-chancery`. There is no default.
4. **Ask once for the missing fields** the document needs (run `python3 scripts/litcheck.py fields …` if you can, or read `assets/fields.json`).
5. **Never invent** a name, date, sum, case number, authority, citation, pinpoint or bundle page. Use the placeholders in `references/fields.md` and end the draft with the "FIELDS TO COMPLETE" table.
6. **Check the draft** with `python3 scripts/litcheck.py check …` if you can run code; otherwise go through the skill's "What makes a draft fail" list yourself.

Raw file addresses follow this pattern, for assistants that read the web:
`https://raw.githubusercontent.com/3orionkings/litigation-writing/main/plugins/litigation-writing/skills/<skill>/SKILL.md`. [`llms.txt`](llms.txt) lists them all.

## What this repository is

One plugin, `litigation-writing`, holding six skills: `litigation-writing` (the main skill: matter intake, packages, procedural papers), and five drafting skills, `litigation-pleadings`, `litigation-evidence`, `litigation-submissions`, `litigation-advice` and `litigation-correspondence`. The product is the text of each `SKILL.md` and its references. The rule files and `litcheck.py` are the checker each skill runs on its own drafts. The plugin installs in Claude Code, Codex and the ChatGPT desktop app, and each skill folder also works on its own.

## Layout

```text
plugins/litigation-writing/
  plugin.json                  portable Agent Plugins manifest (identity only, no extensions block)
  .codex-plugin/plugin.json    Codex overlay: identity, "skills": "./skills/" and the interface block
  .claude-plugin/plugin.json   Claude Code manifest
  skills/<name>/
    SKILL.md                   the skill
    style.json                 the skill's structural rules, by variant (read by litcheck.py)
    agents/openai.yaml         Codex and ChatGPT display metadata
    references/                the skill's own variant files and formulae.md, plus copies of the shared references
    assets/                    copies of the shared rule files
    scripts/litcheck.py        copy of the shared checker
shared/
  scripts/litcheck.py          the only place to edit the checker
  references/                  fields.md, voice.md, authorities.md, matter-file.md, jurisdictions.md
  references/jurisdictions/    hk.md, us-federal.md, ny.md, ca.md, wa.md, de-superior.md, de-chancery.md
  assets/                      fields.json, jurisdictions.json, perspective.json, register.json, placeholders.json, matter.template.json
tools/sync_shared.py           copies shared/ into the skills; --check verifies
tools/validate.py              manifests, versions, skills, docs and the skills' own rules agree
tools/package.py               builds dist/*.skill and dist/litigation-writing.zip
tests/                         run_tests.py and the cases
docs/                          architecture.md, style-json.md
```

## Invariants

The tests and `tools/validate.py` enforce these. Do not work around a failing check; fix the cause.

1. **One source for shared files.** Edit `shared/` only, then run `python3 tools/sync_shared.py`. Each skill carries its own copy because a skill is installed and loaded on its own.
2. **One version.** The version appears in the three plugin manifests, both places in `.claude-plugin/marketplace.json`, and the newest `## [x.y.z]` heading of `CHANGELOG.md`. Change them together.
3. **One identity.** `name`, `description`, `license`, `homepage`, `repository` and `author` match across the three plugin manifests.
4. **Codex overlay rules.** `.codex-plugin/` holds `plugin.json` and nothing else. The root `plugin.json` has no `extensions` block.
5. **Skill identity.** Folder name equals frontmatter `name`; description at most 1,024 characters, first sentence saying what the skill drafts, ending with a "Not for:" line; `agents/openai.yaml` with a `display_name` and a `short_description` of 64 characters at most; every variant in the SKILL.md table exists in `style.json` and the reverse.
6. **Docs name every skill.** README.md, AGENTS.md and llms.txt.
7. **Self-contained.** No file in the plugin mentions or depends on any other plugin or skill collection.
8. **No names, no real matters.** No file names a person, counsel, firm, party or judge from any real matter, holds a real case or action number, or uses facts from a real matter. Examples are invented and use placeholders. `tools/validate.py` fails on anything that looks like a real case number, and on any name in a private deny-list passed through `LITIGATION_DENYLIST` (kept outside the repository).

## Rules for the skill text

- **Neutral and general.** A skill carries no author profile and no firm's or court's house style beyond what the rules require. Voice comes from `shared/references/voice.md` and the user's own drafts.
- **No invented facts or authorities.** Every name, number, date, quotation and authority in an output comes from the user; otherwise a placeholder. The skills carry no lists of cases to cite; the jurisdiction profiles may name the decisions that set a standard, as background only.
- **Moves, not passages.** The skills encode structure, moves and the profession's set formulae. Do not paste in text from anyone's filed documents.
- **Harness-neutral wording.** "The assistant", or address the model directly. Do not name a vendor.
- **The skills follow their own rules.** No dash punctuation, none of the tells in `voice.md`.

## Before you finish a change

```bash
python3 tools/sync_shared.py
python3 -I -B tests/run_tests.py
python3 tools/validate.py
claude plugin validate . --strict
claude plugin validate plugins/litigation-writing --strict
```

The last two need the Claude Code CLI; CI runs the rest.

## Do not

- Commit `dist/`, `__pycache__/`, test output, a `matter.json` or anything from a real case.
- Add third-party dependencies to the scripts. They are standard library only and run on Python 3.8.
