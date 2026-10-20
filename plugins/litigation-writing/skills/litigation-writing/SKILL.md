---
name: litigation-writing
description: "Start here for any litigation drafting task. Takes in the matter (court, jurisdiction, parties, the application or stage), keeps a matter file so every document uses the same facts, chooses the right drafting skill for each document, plans document packages (an application with its summons or notice of motion, supporting evidence, skeleton or brief and draft order), and drafts the short procedural papers that hold a package together: summons, notice of motion and draft or proposed order. Use it when a lawyer asks to prepare papers for a hearing, an application, a motion, a claim, a defence, enforcement or an appeal, or asks \"what do I need to file\", or names a court in Hong Kong or the United States (federal, New York, California, Washington, Delaware) without naming a document. Not for: drafting a pleading, affidavit, skeleton, advice or letter itself (use litigation-pleadings, litigation-evidence, litigation-submissions, litigation-advice or litigation-correspondence)."
---

# Litigation writing

## What this skill is for

A litigator rarely needs one document. An application needs the application itself, the evidence that supports it, the argument, a list of authorities and the order sought, and they must agree on every name, date and defined term. This skill is the front door: it settles the matter, keeps those facts in one place, decides which documents are needed and in what order, sends each to the skill that drafts it, and drafts the procedural papers itself.

The drafting skills in this plugin:

| Document | Skill |
|---|---|
| Statement of claim or complaint, defence or answer, reply, counterclaim, amendment | `litigation-pleadings` |
| Affirmation, affidavit, declaration, witness statement, enforcement evidence | `litigation-evidence` |
| Skeleton submissions or brief, reply, hearing note, speaking note, trial opening and closing, appeal, costs, list of authorities, chronology | `litigation-submissions` |
| Advice or opinion on merits, on pleadings, before action | `litigation-advice` |
| Letters to the other side: request for particulars, demand, proposal, offer, covering letter | `litigation-correspondence` |
| Summons or notice of motion, draft or proposed order, the package plan | this skill |

## Who is speaking

This skill plans and does not argue. The procedural papers it drafts speak in the court's formal voice (a summons calls the parties to attend; an order records what the court orders) or the applicant's formal voice (a notice of motion). They state the relief sought and the procedural details, and nothing else: no argument, no evidence, no first person. Read `references/voice.md` for the voice of each family before handing over.

## Before drafting

1. **The matter file.** Ask whether there is a `matter.json` for this case, or look for one in the working folder. If there is none and more than one document is coming, offer to create one from `assets/matter.template.json` and fill it as the user answers. Read `references/matter-file.md`.
2. **The jurisdiction.** Ask which court the papers are for. It is a required field with no default. Read `references/jurisdictions.md` and then only the matching profile in `references/jurisdictions/`.
3. **The task.** Find out the stage and the goal: issuing a claim, defending one, making or opposing an application (and which), a trial, enforcement, an appeal, or advice before action. Then ask, once for the whole package, for the materials its documents will draw on: the client's instructions, a dramatis personae and a chronology, the key documents and exhibits, the pleadings and orders, the other side's papers, and copies of the authorities. Each drafting skill says what it needs and how it uses them. Then plan the package (below) before drafting anything.
4. **The fields.** For each document this skill drafts, run `python3 scripts/litcheck.py fields --variant <variant> --jurisdiction <code> [--matter matter.json]`, and ask once, grouped, for the missing required fields. Read `references/fields.md`.
5. **Authorities.** This skill's papers cite rules, not cases. Name the rule the application is made under only if the user has given it; otherwise write `[rule]`. Read `references/authorities.md` before any document that will cite authority.

## Variants

| Variant | What it is | When to use it | Read |
|---|---|---|---|
| `package` | A plan: the documents an application, claim, defence, trial, enforcement step or appeal needs, in drafting order, with the skill for each and the fields they share | Whenever the user wants papers for a step in the case rather than one named document | `references/package.md` |
| `summons` | Hong Kong summons (inter partes or ex parte) or originating summons; US notice of motion or motion | The application document itself | `references/summons.md` |
| `draft-order` | Hong Kong draft order; US proposed order | When the court will expect the order sought in draft, and with any unless order or directions sought | `references/draft-order.md` |

## The moves

- **Plan before drafting.** Write the package plan first: each document, its skill, the order to draft in, and the fields they share. Draft the evidence before the argument that relies on it, and the order sought before the submissions that ask for it, so the submissions can quote it.
- **One set of facts.** Every document in a package draws its parties, dates, defined terms, bundle scheme and authorities from the matter file. When a later document changes a fact, update the file and say which earlier documents must change.
- **The relief is the spine.** Settle the exact orders sought first, in court language, and use the same wording in the summons or notice of motion, the evidence's purpose paragraph, the submissions' conclusion and the draft order.
- **Formal papers stay formal.** A summons or notice of motion states who applies, for what, under which rule, when and where it is heard, and who takes it out. It never argues.
- **Hand over cleanly.** When handing a document to another skill, pass the variant, the jurisdiction and the matter file, and say which fields are still missing.

## Language

The procedural papers use the court's set forms, word for word, from `references/formulae.md`: "LET ALL PARTIES CONCERNED ATTEND …", "UPON HEARING …", "IT IS ORDERED that …", "PLEASE TAKE NOTICE that …". Orders are numbered paragraphs, each one an order the court can make. Deadlines are dates (`[date 1]`), with a time where the order needs one. Costs terms are stated in full ("costs of and occasioned by this application to be paid by [Defendant] to [Plaintiff], to be taxed if not agreed").

## Workflow

1. Settle the matter file, the jurisdiction and the task (Before drafting).
2. Write the package plan (`references/package.md`) and show it to the user. Confirm the orders sought in court language.
3. For each document: if it belongs to another skill, hand over to that skill with the variant, the jurisdiction and the matter file. In a plugin the skills sit side by side. Reading this repository directly, the skill is at `plugins/litigation-writing/skills/<skill>/SKILL.md`. If that skill is not available, say so.
4. For a summons, notice of motion or draft order: run the fields helper, ask for the missing required fields, and draft from the reference file and `references/formulae.md`.
5. Save the draft and run `python3 scripts/litcheck.py check draft.md --variant <variant> --jurisdiction <code> [--matter matter.json]`. Fix every hard failure; look at every note.
6. Return the document followed, if any placeholder remains, by the "FIELDS TO COMPLETE" table. Then list, in one line each, the other documents in the package and their status.

## The register pass

Procedural papers are almost entirely set forms, so the register pass is light: keep every formula verbatim, keep the numbered order paragraphs, and check that nothing argumentative or evidential has crept in. In the package plan (a working note for the lawyer, not a court document), write plainly and briefly, and apply `references/voice.md` to any sentence that is not a formula.

## What makes a draft fail

- Drafting the skeleton before the evidence, so the argument relies on facts no one has sworn to.
- Relief worded differently in the summons, the evidence and the draft order.
- A summons that argues, or a notice of motion that recites the evidence.
- Guessing the rule an application is made under, or the hearing details, instead of using `[rule]`, `[date]`, `[time]` and `[judge]`.
- Forgetting the US meet-and-confer step where the court requires one, or the Hong Kong ex parte or inter partes choice.
- Not telling the user which earlier documents change when a fact changes.

## Files

- `references/package.md`: the packages by stage and jurisdiction, with drafting order and shared fields.
- `references/summons.md`, `references/draft-order.md`: structure and skeletons for each jurisdiction.
- `references/formulae.md`: the set forms, verbatim.
- `references/fields.md`, `references/voice.md`, `references/authorities.md`, `references/matter-file.md`, `references/jurisdictions.md` and `references/jurisdictions/`: the shared core, identical in every skill of this plugin.
- `assets/`: `fields.json`, `jurisdictions.json`, `perspective.json`, `register.json`, `placeholders.json` and `matter.template.json`, read by the checker.
- `scripts/litcheck.py`: the checker and fields helper (Python 3.8 or later, standard library only). Where code cannot run, apply the rules by reading the files and skip the check.
