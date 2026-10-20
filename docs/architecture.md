# Architecture

## Why six skills

The voice of a litigation document changes with its kind, and the rules collide. A pleading states facts only, with no law and no argument. A submission argues and cites authority with pinpoints. An affidavit is the witness's own account and never cites a case. One skill holding all three rule sets would load every rule into every draft, and its checker would carry contradictions ("pinpoint every authority" against "never cite a case"). So the drafting is split by family: pleadings, evidence, submissions, advice and correspondence.

Splitting further, one skill per document, would duplicate what documents in a family share. A statement of claim, a defence and a reply use one library of traverses, prayers, statements of truth and backsheets, and amendment applies to all of them. A skeleton, a reply and a hearing note share most of their structure. So each family skill holds its documents as variants.

A main skill, `litigation-writing`, sits in front. Most steps in a case need several documents that must agree. The main skill plans the package, keeps the facts in one matter file, hands each document to its family skill, and drafts the procedural papers (summons or notice of motion, draft order) itself.

## The shared core

Everything the skills have in common lives in `shared/` and is copied into each skill by `tools/sync_shared.py`, so every skill works when installed on its own:

| File | What it holds |
|---|---|
| `references/fields.md` | The field protocol (ask once, then placeholders), the closed placeholder vocabulary, the "FIELDS TO COMPLETE" table |
| `references/voice.md` | Who is speaking in each family; the target voice; the punctuation rule; the tells to keep out; trade register; the register pass |
| `references/authorities.md` | The authority policy; stating and applying a test; pinpoints; bundle references; labels for the other side's papers; lists of authorities |
| `references/matter-file.md` | The `matter.json` that keeps a package consistent |
| `references/jurisdictions.md` and `references/jurisdictions/*.md` | How to choose a profile, and one profile per court system |
| `assets/*.json` | The machine-readable rules: fields by skill and variant, perspective by family, register, jurisdiction formalities and citation patterns, the placeholder list, a blank matter file |
| `scripts/litcheck.py` | The checker and fields helper |

## Jurisdictions

The drafting moves are the same everywhere. A profile changes what the court requires: document names, the pleading standard, the grammar of an answer, verification and the evidence instrument, how amendments are shown, the formal rules and limits for papers, and citation style. The prose profile tells the assistant what to write; `assets/jurisdictions.json` gives the checker the formalities it can test mechanically. The `jurisdiction` field has no default, so a draft is never silently written for the wrong court.

## The checker

`litcheck.py check` runs six kinds of check, from the skill's `style.json` and the shared rule files:

1. **Structure**: numbered paragraphs, required parts of each variant (a prayer, a jurat, a conclusion with orders), length, and no summarising close.
2. **Perspective**: the voice of the family. Pleadings and procedural papers forbid the first person and case citations. Evidence requires the first person and forbids submissions, signposts and case citations. Written submissions forbid the first person. Advice forbids numeric odds and instructions aimed at the client.
3. **Register**: no dash punctuation, no bullet points, none of the listed tells.
4. **Jurisdiction**: the formalities of the profile (a statement of truth and the "Served" slot in a Hong Kong pleading; the statutory declaration words in US evidence; word limits; no Hong Kong forms in a US pleading).
5. **Placeholders**: every gap uses the vocabulary, and a "FIELDS TO COMPLETE" table follows the draft when any remain.
6. **Citations**: every citation found, whether it has a pinpoint, whether it is in the local style, and, with `--matter`, whether it is among the user's authorities (a hard failure if not).

`litcheck.py fields` reads `assets/fields.json` and lists what the variant needs in that jurisdiction, marked R (required), O (optional) or L (filled in later), and which are already in the matter file.

The format of the rule files is in [style-json.md](style-json.md).

## What the checks cannot do

They do not judge the law, the argument or whether a fact is true. A draft can pass every check and still be wrong. The skills say so, and the lawyer remains responsible for every document filed.
