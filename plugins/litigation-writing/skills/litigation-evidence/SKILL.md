---
name: litigation-evidence
description: "Drafts written evidence in the witness's own first-person voice, with exhibits, jurat and backsheet: affirmations, affidavits and declarations in support of or in opposition to an application, evidence in reply, trial witness statements, enforcement affirmations (examination of a judgment debtor, charging order, garnishee order), evidence for procedural applications such as an extension of time or leave, and non-party evidence. Use for Hong Kong or US courts (federal, New York, California, Washington, Delaware) when asked to draft, settle, tighten or check an affirmation, affidavit, declaration under penalty of perjury, CPLR 2106 affirmation, supporting or opposing evidence, reply affirmation, witness statement, exhibit index or interpreter's jurat. Not for: skeletons, briefs or memoranda of law (litigation-submissions); pleadings or their verification (litigation-pleadings); letters to the other side (litigation-correspondence); counsel's advice (litigation-advice)."
---

# Litigation Evidence

## What this skill is for

This skill drafts written evidence: the affirmation, affidavit, declaration or witness statement that a court reads as the witness's own account, and on which the witness may be cross-examined. It covers evidence in support of and in opposition to applications, evidence in reply, trial witness statements, post-judgment enforcement evidence, evidence for procedural applications, and the evidence of non-parties, in Hong Kong and in the US courts that have profiles.

Evidence does a different job from the submissions it sits beside. It puts the facts on the record, each with its source, so that counsel can argue from them. A draft that argues, cites cases or states tests weakens the witness and hands the other side a line of cross-examination. A draft that says more than the witness knows can be taken apart in the witness box. The skill keeps the evidence on its side of that line.

## Who is speaking

The lawyer drafts; the witness speaks. Every sentence is in the first person, in words this witness would use and could defend under cross-examination. Settle who the witness is before writing anything (`references/deponent-intake.md`), because the same facts sound different in different mouths:

| Deponent | How they sound | What to watch |
|---|---|---|
| Director or officer for a company | Speaks for the company's records and their own dealings; "the [Plaintiff]" for the company, "I" for themselves | Facts from colleagues or files: name the person or the record |
| Party in person | Plain and personal; never the solicitors' "we" or "our client" | Bare "I believe" doing counsel's work |
| Family-law party | Measured feeling where it is their own ("I was worried about [the Child]") | Heat about the other party with no document behind it |
| Solicitor with conduct (usually procedural) | File-based procedural facts, each with its source | Privilege: describe the steps taken, never the advice given |
| Non-party | What they did, saw and hold; nothing on the merits; no prayer | Being drawn into the dispute |

Four rules hold for every deponent:

- **Facts within knowledge are stated flat.** What the witness was told is information and belief, with the source named ("I am informed by [name], {role}, and verily believe that …"; "My belief is based on …"). What the witness does not know is said plainly ("I do not know whether …").
- **Law appears only as advice, and is handed over.** In Hong Kong: "I am advised and verily believe that …", one sentence stating a conclusion, then left to counsel. Never a test, a case, "It is submitted", "a fortiori", "the Court is invited" or any of counsel's signposts. In a US declaration law does not appear at all; it belongs in the memorandum.
- **Argument comes in only through arrangement.** Dates side by side, the other side's own words quoted back, the exhibit placed with the fact it proves, a heading that states the point.
- **A witness statement for trial has its own grammar.** "I make this statement", no "I am advised", "my understanding" for second-hand matter, and any evaluation kept to a short closing section.

## Before drafting

1. **The matter file.** Look for `matter.json` in the user's folder and read it before asking anything (`references/matter-file.md`). Offer to record new facts; never overwrite a value silently.
2. **The jurisdiction.** It is required and has no default. Ask if it is not clear, then read only that profile in `references/jurisdictions/<code>.md`. The instrument changes with it: in Hong Kong, an affirmation or affidavit with a jurat; in the US, a declaration (or a New York affirmation) under penalty of perjury, in the words the statute prescribes. For a court with no profile, say so, draft from the closest profile as a guide and flag every formal requirement for the user to check.
3. **The deponent.** Work through `references/deponent-intake.md`: who they are, their capacity and authority, which facts they know at first hand and which they were told, and by whom, the documents they will exhibit, whether they read English, and anything they are not to depose to. Do not draft the body until these are settled, or the user tells you to proceed with placeholders.
4. **The fields.** Run `python3 scripts/litcheck.py fields --skill litigation-evidence --variant <v> --jurisdiction <code> [--matter matter.json]`. Ask once, in one grouped message, for the missing required fields and the intake answers together. If the user says go ahead, draft with placeholders from `references/fields.md`.
5. **Authorities.** Evidence cites no case and states no test (`references/authorities.md`). If the user supplies authorities, they belong in the submissions, not here. A judgment between the same parties is a fact: describe it by court, date and paragraph, and exhibit it. Name a procedural rule in the purpose paragraph only if the user has given it; otherwise write `[rule]`. Never choose the statute, rule or threshold that applies.
6. **The materials.** In the same message, ask the user to share what they have: the documents to be exhibited; the client's or witness's instructions in any form (a statement, memo, attendance note, emails, a translation); earlier affirmations or witness statements in the matter, so ordinals, defined terms and exhibit numbers continue; the other side's evidence being answered; and the relevant correspondence and orders. The account must come from the witness's own instructions and the documents, not be reconstructed from the conversation. Exhibit only documents the user has, described as they are (date, author, type); a document not yet seen is `[exhibit]`, with its description left to the user. Where the witness quotes a document, quote it exactly.

## Variants

| Variant id | What it is | When to use it | Read |
|---|---|---|---|
| `affirmation` | Affirmation or affidavit (US: declaration, or CPLR 2106 affirmation) in support of or in opposition to an application | Summary judgment, strike-out, security for costs, interim relief, maintenance, unless orders: any application decided on written evidence | `references/affirmation.md` |
| `reply-affirmation` | Evidence in reply, answering the other side's evidence paragraph by paragraph | The other side has filed evidence and the rules or a direction allow a reply | `references/reply-affirmation.md` |
| `witness-statement` | A witness statement for trial or a preliminary issue | Evidence-in-chief exchanged under directions; in the US only where the judge takes direct testimony on paper | `references/witness-statement.md` |
| `enforcement` | Post-judgment evidence: a common preamble plus a module for examination of a judgment debtor, a charging order or a garnishee order | The judgment is unpaid and the creditor seeks a remedy | `references/enforcement.md` |
| `procedural` | Evidence for a procedural application: reasons for delay, prospects, prejudice | Extension of time, leave to file late, leave to amend, relief from a missed deadline, other leave applications | `references/procedural.md` |
| `non-party` | Evidence of a witness who is not a party | A relative, former employee, bank officer or adviser who can prove a specific fact | `references/non-party.md` |

## The moves

1. **Open in the fixed order.** Opening formula, capacity (with authority, for a company), knowledge, reading conventions, then the purpose paragraph listing the orders sought exactly as the summons words them. A non-party states the purpose first.
2. **Thesis first, as fact.** In contested evidence, follow the purpose paragraph with a short overview of what the evidence shows, stated as facts the deponent can prove. Then the chronology. Then the other side's case. The facts sections never argue, and the answering section never starts a new story.
3. **Headings that state a point.** "No Payment Has Been Made" does more work than "Payments". Where the court weighs known factors, the factors can be the headings, with the evidence under each, and the law left unstated.
4. **One paragraph per event.** Dates at the start of the sentence, past tense. For correspondence, a ladder: one paragraph per letter, giving the date, what it asked for, the reply or the silence, and the exhibit.
5. **Let arithmetic carry the inference.** State the deadline, the date of service and the number of days; put the other side's act beside the date it followed. Then concede what the timing does not prove.
6. **Quote the other side back, briefly.** A few words in quotation marks with the paragraph or page, not a long extract.
7. **Belief with its source and its gap.** Every statement of belief says what it rests on and what remains unknown. In enforcement evidence the gap sentence is the reason for the order.
8. **The exhibit follows the fact.** State the fact, then exhibit the document that proves it, in the same paragraph. Use `[exhibit]` placeholders, numbered in order of first mention, unless the user gives the code scheme. Finish with a cover sheet and an index.
9. **Concede plainly, then move on.** A frank admission of a mistake or an adverse point, made once, protects the witness. On an application without notice, the deponent must also disclose the points against it.
10. **Answer the other side in its own order.** Verdict sentence, then the document with its page, then a one-line consequence.
11. **Ask; do not recap.** Hong Kong evidence ends with a prayer asking for the order in terms of the summons, or restating alternatives in full. A US declaration ends with the statutory words; the relief is in the motion. Costs are asked for, never argued.
12. **Keep witnesses consistent.** Where several witnesses speak to the same events, sums, dates and defined terms must match across all of them. Flag any discrepancy to the user rather than resolving it yourself.

## Language

- **Person and names.** "I" throughout; never the deponent in the third person after the capacity line. Parties by role in full ("the Defendant", "the Judgment Debtor"), consistent with the caption. Defined terms in brackets and quotation marks at first use, then exactly the same each time.
- **Belief registers, kept apart.**

| What the deponent is saying | Hong Kong affirmation | Witness statement | US declaration |
|---|---|---|---|
| Their own knowledge | Stated flat | Stated flat | Stated flat |
| What a named person told them | "I am informed by [name] and verily believe that …" | "[name] told me, and I believed, that …" | "[name] told me that …", with when and where |
| What a document shows | "From [document title], I verily believe that …" | "I understand from [document title] that …" | Exhibit the document and describe it |
| An inference from facts already set out | "I verily believe that …" | Only in the closing section | Leave it to the memorandum |
| A proposition of law | "I am advised and verily believe that …", then to counsel | Never | Never |
| What they do not know | "I do not know …" | "I do not know …" | "I do not know …" |

- **Temperature.** Set by the court and the deponent: nil in enforcement and non-party evidence; low in witness statements; measured in commercial applications; some feeling in family proceedings. A strong word is tied to a document and a paragraph, and is better left in the document's mouth ("the letter described the delay as deliberate").
- **Sentences.** About 20 words on average, varied, with some under ten. A short factual sentence closes a run of facts ("No reply was received."). No rhetorical questions.
- **Formulae.** The opening words, the knowledge sentence, "There is now produced and shown to me …", the belief formulae, the prayer, the jurat, the statement of truth and the US declaration words are fixed. Take them word for word from `references/formulae.md`, for the right jurisdiction.

## Workflow

1. Read the matter file, settle the jurisdiction and read the profile.
2. Run the deponent intake and keep the deponent note (`references/deponent-intake.md`) beside the draft.
3. Run the fields helper and ask once for what is missing.
4. Choose the variant and read its reference file.
5. Build a fact list before writing prose: each fact with its date, its source (own knowledge, document, named informant) and its exhibit. A fact with no source becomes information and belief with one, or comes out.
6. Draft in the variant's order, applying the moves. In Hong Kong evidence, law appears only in "advised and verily believe" sentences; in US and witness-statement evidence, not at all.
7. Add the exhibits: the exhibit sentence after each fact, then the cover sheet and the index.
8. Add the formal parts for the jurisdiction: jurat, interpreter's jurat or certificate, "filed on behalf of" line and backsheet in Hong Kong; the profile's declaration words, date, place and signature in the US.
9. Do the register pass (below).
10. Run `python3 scripts/litcheck.py check draft.md --skill litigation-evidence --variant <v> --jurisdiction <code> [--matter matter.json]`. Fix every hard failure; look again at each soft one.
11. Return the draft. Above it, in one or two lines, list anything the deponent must confirm before affirming. After it, the "FIELDS TO COMPLETE" table if any placeholder remains.

## The register pass

Apply "The register pass" in `references/voice.md` to the running prose, with one extra test for evidence: read each paragraph as the deponent and ask whether they would say it in those words. Cut what a lawyer would say and the witness would not: legal labels, polished abstractions, "This matters because", balanced triads, chains of antitheses, anything that sounds argued. Replace any dash. Keep the witness's own settled phrasing when the user supplies it; do not correct it into lawyer's English and do not add errors.

Leave these untouched, word for word:

- the opening formula, the knowledge sentence, the jurat, the interpreter's jurat, the statement of truth and the US statutory declaration words;
- the exhibit formulae and every exhibit code or `[exhibit]` placeholder;
- the belief formulae ("I am advised and verily believe that", "I am informed by … and verily believe that", "My belief is based on");
- the orders sought, copied from the summons with their "and/or" stacks, numbering and tails ("or such further or other order as this Honourable Court thinks fit");
- the enforcement formulae: the (a) to (d) itemisation of the debt, "all debts due or accruing due", "costs of and occasioned by this application", and the Land Registry long-form description;
- run-in lists in the form "(a) …; (b) …; and (c) …", and the paragraph numbering;
- every defined term, sum, date, paragraph reference and placeholder.

## What makes a draft fail

- The deponent argues: "It is submitted", "I submit that", "the Court should", a legal test, a case name or citation, "a fortiori".
- Law stated by the deponent without the "advised and verily believe" wrapper (Hong Kong), or any law at all in a US declaration or a witness statement.
- "I believe" with no source; an asset, account or conversation asserted with no "My belief is based on …" and no "I do not know …".
- The wrong voice: "we" or "our client" from a lay deponent; the deponent in the third person; a non-party commenting on the merits or praying for relief; a witness statement saying "I am advised".
- An exhibit sentence before its fact, an undated document, or an invented exhibit code.
- Orders in the purpose paragraph that differ from the summons, or a prayer that differs from both.
- A missing formal part: no opening formula, no jurat or "Before me", no interpreter's jurat for a deponent who does not read English, no statement of truth, or the wrong US declaration words for the profile.
- A sum, date or defined term that differs between paragraphs, or between this witness and another.
- Privileged advice, without prejudice material, or a matter the deponent was told not to depose to.
- A closing paragraph that summarises the evidence instead of asking for the order.

## Files

- `references/affirmation.md`, `references/reply-affirmation.md`, `references/witness-statement.md`, `references/enforcement.md`, `references/procedural.md`, `references/non-party.md`: one per variant, each with its Hong Kong structure, the US differences, a skeleton and a checklist.
- `references/formulae.md`: the evidence formulae, verbatim, by jurisdiction.
- `references/deponent-intake.md`: the questions to settle before drafting, and the deponent note.
- The shared core, copied into this skill: `references/voice.md`, `references/fields.md`, `references/authorities.md`, `references/jurisdictions.md`, `references/matter-file.md`, `references/jurisdictions/<code>.md` and `assets/*.json`.
- `style.json`: this skill's rules for the checker.
- `scripts/litcheck.py`: the fields helper and the checker.
