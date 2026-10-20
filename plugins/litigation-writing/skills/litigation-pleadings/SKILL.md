---
name: litigation-pleadings
description: "Drafts pleadings as the party's own case, in the third person and in facts only, for Hong Kong and US courts (federal, New York, California, Washington, Delaware): statements of claim and complaints, defences and answers, replies and defences to counterclaim, counterclaims and cross-complaints, and amended pleadings with the application for leave to amend. Use when a lawyer asks to draft, answer, traverse, amend or check a pleading, or writes statement of claim, SOC, indorsed writ, points of claim, complaint, defence, answer, affirmative defenses, reply, defence to counterclaim, counterclaim, cross-complaint, re-amended, leave to amend, redline, prayer for relief or particulars of fraud. Not for: affirmations, affidavits or declarations (litigation-evidence); skeletons or briefs (litigation-submissions); letters or requests for particulars (litigation-correspondence); advice on the merits (litigation-advice); other summonses, motions and orders (litigation-writing)."
---

# Litigation Pleadings

## What this skill is for

A pleading fixes what the trial is about. The judge reads it to decide what may be argued and what evidence is relevant; the opponent reads it looking for a fact that is missing, an allegation left unanswered, or a plea that can be struck out. A party is bound by the case it has pleaded: a point left out is usually lost, however good the evidence for it.

This skill drafts the five documents that do that work, and the amended version of any of them: the claim, the defence, the reply (with any defence to counterclaim), the counterclaim, and the amendment with its application for leave. It drafts for Hong Kong first and states where each US profile differs.

## Who is speaking

The party, through its lawyers, stating its case as allegations of fact.

- **Person.** Third person throughout: "The Plaintiff avers", "The 1st Defendant denies", "Plaintiff alleges", "Defendant admits". Never "I" or "we", except inside a statement of truth, a verification or an interpreter's certificate.
- **Who stands behind it.** In Hong Kong the party (or a director, officer or solicitor for it) signs a statement of truth, which means the verifier must believe each allegation to be true. That rules out speculation, two contradictory primary cases, and alternatives on matters the party knows. In the US the attorney's signature certifies the pleading (FRCP 11 and the state equivalents named in the profile); a fact the party does not know first-hand is pleaded "upon information and belief". Some US pleadings must also be verified by the party: claim pleadings in the Court of Chancery, and every later pleading in New York or California once the complaint is verified.
- **What it contains.** Material facts in summary form, the particulars the rules require, and the relief claimed.
- **What it never contains.** Evidence, argument, case citations, law recited as fact, rhetorical questions, characterisation of the opponent's conduct, or threats about what the party will apply for. A statute appears only where the claim or defence depends on it, by section, as the user gives it.
- **Before writing, settle:** who verifies and in what capacity; what that person knows first-hand and what they were told; whether they read English (a Hong Kong pleading then needs an interpreter's or translator's certificate); and, for any response, exactly which pleading and which version is being answered.

## Before drafting

1. **Matter file.** Look for `matter.json` in the user's case folder and read it first (`references/matter-file.md`). Take every value it holds; offer to record new facts in it.
2. **Jurisdiction.** Required, with no default. Ask if it is not clear, then read `references/jurisdictions/<code>.md` for document names, the pleading standard, the grammar of an answer, verification, amendment mode and formal rules. For a court with no profile, say so, use the nearest profile as a guide only, and flag every formal requirement for the user to check.
3. **Fields.** Run `python3 scripts/litcheck.py fields --skill litigation-pleadings --variant <v> --jurisdiction <code> [--matter matter.json]`. If scripts cannot run, read `assets/fields.json`.
4. **Ask once.** Put every missing required field in one grouped message. For pleadings the questions that matter most are: the opponent's pleading in full with its paragraph numbers (for any response); the agreement or other document sued on, with its date and the clauses relied on; the sums, rates and periods claimed; the verifier and their capacity; and, before any allegation of fraud or dishonesty, confirmation that the user has instructions and credible material for it. If the user says to go ahead, draft with placeholders from `references/fields.md` and list them at the end.
5. **Authorities.** A pleading cites no case law at all, so it never needs an authority from the user; legal argument belongs in the submissions. Where a claim depends on a statute (an interest power, a statutory cause of action, a limitation period), use the provision the user names, or write `[statutory provision]`. Never choose the provision yourself, and never cite a case, even one you are sure of. The full policy is in `references/authorities.md`.
6. **The materials.** In the same message, ask the user to share what they have: the client's instructions (a statement, memo or attendance notes); a dramatis personae, or the people and entities involved and their roles; a chronology; the documents the facts come from (the agreement and its schedules, correspondence, invoices, bank records, registry searches); the writ and any earlier pleadings; and, for a defence or reply, the pleading being answered, in full. Plead only facts that come from these or from the user's instructions in the conversation. Where a fact the cause of action needs is missing, use a placeholder and ask rather than infer it. Where a pleading sets out a contract term or a document's words, take them from the document itself.

## Variants

| Variant | What it is | When to use it | Read |
|---|---|---|---|
| `claim` | Hong Kong statement of claim, served separately or indorsed on the writ; points of claim in family proceedings; US complaint | Starting a claim, or pleading one after the writ | `references/claim.md` and `references/causes-of-action.md` |
| `defence` | Hong Kong defence and points of defence; US answer with affirmative defenses | Answering a claim with no cross-claim | `references/defence.md` |
| `reply` | Hong Kong reply, and reply and defence to counterclaim; US reply or answer to a counterclaim, and a court-ordered reply | Answering new matter in a defence, or defending a counterclaim | `references/reply.md` |
| `counterclaim` | Hong Kong defence and counterclaim, and a counterclaim against an added party; US answer with counterclaims; California cross-complaint | A defendant with its own claim against the claimant or another party | `references/counterclaim.md` |
| `amendment` | An amended or re-amended version of any pleading above, with the Hong Kong summons for leave and its annexed draft, or the US motion for leave with the proposed pleading and its comparison | Changing a pleading already served | `references/amendment.md` |

Formulae for every variant are in `references/formulae.md`. A family case (petitioner, respondent, intervener) is a switch on `claim` and `defence`, not a variant: only the caption, the role names and the certificate change.

## The moves

1. **Plead the facts that complete each cause of action, and stop.** Every fact the claim or defence needs, in summary form, one allegation to a paragraph, in date order, with the same name for the same person or thing throughout. No evidence, no argument and no law dressed as fact. Federal complaints need enough facts to make liability plausible; the other US standards are in the profiles.
2. **Run the claim engine in order.** Parties; background, short and dated; the agreement identified by date, parties and form, with its material terms clause by clause, each ending "(see Clause [number])"; implied terms with the facts they arise from; performance or readiness; breach, with particulars; demand and any answer; loss, with particulars; interest pleaded specifically; the prayer. In the US: caption, jurisdiction and venue (federal), parties, facts, counts, prayer or WHEREFORE clause, jury demand where wanted, signature with `[bar number]`.
3. **Build other causes of action from the modules.** `references/causes-of-action.md` gives the paragraph sequence and the particulars each cause requires. Plead the primary case first and each alternative expressly as an alternative, in its own paragraphs, with only the facts that support it. Do not stack every equitable route on every asset by reflex.
4. **Name headings after facts.** In a claim: "The Agreement", "The Payments for the Property", "The Representations", never the doctrine relied on. A defence or reply follows the order of the pleading it answers, and heads each affirmative matter by name ("Limitation", "Set-off") so the reader can find it.
5. **Make interest and sums consistent.** The body states the basis (the contractual clause and rate, or `[statutory provision]`), the sum, and the period from and to; the prayer repeats them exactly. A sum written in two places is the same sum.
6. **Write the prayer as the order sought.** "AND THE PLAINTIFF CLAIMS" (or the US WHEREFORE clause), then each relief numbered separately: the sum or damages, declarations, specific and proprietary relief, interest, costs, and the tail. Every relief must follow from pleaded facts. "Further or other relief" carries nothing, so nothing important may depend on it.
7. **Answer every allegation (Hong Kong).** Each allegation is admitted, denied or not admitted. Split compound allegations and answer each part, turning "and" into "or" and "all" into "any". Every denial carries its reason, and where the party's version differs, that version is pleaded as a positive case in the pleading itself (O.18 r.13). Admit what cannot sensibly be disputed; where a fact is true but answerable, admit it and plead the answer. Strict proof is never the only answer.
8. **Plead affirmative matter on its own.** Limitation, set-off, estoppel, release, illegality, fraud, change of position, bona fide purchase and every other matter O.18 r.8 lists go in separate paragraphs under their own heading, each with its facts, never nested inside the traverse of a claim paragraph. In the US they go under the affirmative defenses heading, one defense to a numbered paragraph, with the facts behind it.
9. **Use the traverse formulae in their place.** A defence never joins issue. A reply may join issue, but no joinder is possible on a counterclaim: the defence to counterclaim traverses every allegation specifically. The general traverse closes a Hong Kong defence as a backstop, never as the answer to an essential allegation, and is left out where nothing is denied. US answers use the profile's grammar (admit, deny, lack knowledge), never "save and except" or "traversed seriatim".
10. **Plead fraud and states of mind exactly.** Fraud is pleaded distinctly, with who, what, when, where and how, actual knowledge (or recklessness) and the primary facts from which it is inferred. Never "knew or ought to have known": that pleads constructive knowledge and will not support a finding of dishonesty. Bad faith alleges the other party's knowledge.
11. **Finish the formal parts.** Hong Kong: a statement of claim served apart from the writ states the writ's issue date (O.18 r.15(3)); the dated line, counsel and solicitors; the statement of truth naming this pleading by its exact title; a certificate where the verifier does not read English; a backsheet with Dated, Filed and Served slots. US: the attorney signature block, any verification the profile requires, and the profile's paper format.
12. **Sweep for consistency, above all after amendment or cloning.** Every sum, rate, period, date, defined term, party reference and cross-reference must agree across the body, the prayer, the statement of truth and the backsheet. When one pleading is cloned for a parallel action, render each from its own facts rather than editing a copy, then check every recurring figure and party reference.

## Language

- **Formulae stay word for word.** Traverse language, the prayer openings and tails, statements of truth, legends, the US answer and count formulae: `references/formulae.md`. Do not paraphrase them into plain English.
- **Hong Kong register.** "avers", "is and was at all material times", "In the premises,", "Further or alternatively,", "By reason of the matters aforesaid,", "save that", "whether as alleged or at all", "or any part thereof", "(which is denied)". "And/or" stacks and near-synonym pairs ("right, title and interest") are trade register. Lists open with ":-". Dates, sums and numbers in figures, never in words.
- **US register.** "alleges", "upon information and belief", "repeats and realleges", "admits", "denies", "lacks knowledge or information sufficient to form a belief", "WHEREFORE". US spelling inside US pleadings ("defense", "favor").
- **Temperature.** Low. Strong words belong only in admissions, denials and the facts. No intensifiers on a denial ("strongly denied"), no "is not denied" (it is neither an admission nor a denial), no characterisation of the other side. The one short sentence a pleading may use for effect is factual: "No reply was received."
- **Sentences.** As long as an allegation needs and no longer. Split a paragraph that carries two allegations. Particulars go in lettered sub-paragraphs, not in a running sentence.
- **Defined terms** are made at first use, in brackets and quotation marks ("Agreement"), and used the same way to the end. Party abbreviations are announced up front or adopted from the pleading answered.

## Workflow

1. Settle the variant and the jurisdiction; read the variant reference and the profile.
2. Run the fields helper and ask once for what is missing.
3. For a claim, choose the cause-of-action modules, confirm the primary case and the alternatives, and list the relief each supports. For fraud, confirm the instructions and the material first.
4. For a response, build the response map before drafting: every paragraph and compound allegation of the pleading answered, with admit, deny or not admit, the reason, the positive case it hooks to, and a separate list of the affirmative matters to plead.
5. Draft the caption and title, the body, the prayer, the signature block, the statement of truth or verification, and the backsheet, from the skeleton in the variant reference. In the draft file, write each paragraph and sub-paragraph as one unbroken line, number every paragraph of the body, and put each backsheet slot (Dated, Filed, Served) on its own line; the checker reads line by line. Number placeholders that stand for different values (`[name 1]` for the plaintiff throughout, `[name 2]` for the defendant, `[date 1]`, `[date 2]`), as `references/fields.md` requires.
6. Run the consistency sweep (move 12).
7. Run the register pass below.
8. Run `python3 scripts/litcheck.py check draft.md --skill litigation-pleadings --variant <v> --jurisdiction <code> [--matter matter.json]`. Fix every hard failure and look again at every soft one.
9. Return the draft, followed by the "FIELDS TO COMPLETE" table (`references/fields.md`) if any placeholder remains.

## The register pass

Apply "The register pass" in `references/voice.md` to the running prose, the narrative and particulars paragraphs where the drafter's own sentences live. In a pleading that means:

- **Cut:** balanced groups of three in running prose where the facts give two or four; antithesis chains; signposting sentences ("It is necessary to set out the background"); rhetorical questions; adjectives about the other side; any closing paragraph that restates the case; every dash, replaced by a comma, brackets, a colon or a new sentence.
- **Vary** sentence length in the narrative, ending a paragraph on the fact that matters.
- **Leave untouched:** every formula in `references/formulae.md`; the traverse and prayer language; "and/or" stacks and near-synonym pairs of pleading register; the ":-" list introducers; the capitals of headings and prayer openings; numbered paragraphs and lettered sub-paragraphs (never turned into prose, never merged); clause pinpoints and paragraph cross-references; defined terms, sums, rates, periods and dates; statements of truth, verifications, certificates and legends; every placeholder.

Then run the checker, which tests the dash rule and the tells mechanically.

## What makes a draft fail

- An essential fact missing: no date or form for the agreement, a term without its clause, an implied term with no facts behind it, a loss with no particulars, interest with no basis, rate or period.
- Interest, a sum or a period that differs between the body and the prayer; a prayer item left at its old figure after an amendment.
- A relief claimed with no pleaded facts behind it, or a declaration argued for but not prayed.
- Fraud pleaded as "knew or ought to have known", or with no primary facts showing knowledge; bad faith with no allegation of what the other side knew.
- An allegation in the answered pleading left unanswered, a bare denial with no reason, a denial with no positive case where the party has one, or strict proof as the only answer.
- An affirmative defence buried inside the traverse of a claim paragraph; limitation pleaded without its accrual and expiry dates.
- Joinder of issue in a defence or on a counterclaim; a general traverse doing the work of a specific denial.
- A reply that raises a new cause of action or contradicts the statement of claim.
- Law recited as fact, a case cited, argument, or a threat to apply to strike out or to complain to a professional body.
- In Hong Kong: no "Served" slot on the backsheet; no writ-issue date on a separately served statement of claim; a statement of truth or backsheet that still carries the old title after amendment; a legend missing or naming the wrong rule or order.
- In the US: "save and except" or "traversed seriatim" in an answer; a general denial in the Court of Chancery; affirmative defenses with no facts; an amended pleading filed without the comparison the profile requires.
- A wrong party in a cloned pleading ("held on trust for the Defendant" in the plaintiff's claim), a stale cross-reference, a transposed figure, a title typo.

## Files

- `references/claim.md`, `references/defence.md`, `references/reply.md`, `references/counterclaim.md`, `references/amendment.md`: structure, Hong Kong first and then the US differences, skeleton, formulae used, checklist.
- `references/causes-of-action.md`: the module library for the claim engine.
- `references/formulae.md`: the trade-register formulae, by jurisdiction.
- `references/voice.md`, `references/fields.md`, `references/authorities.md`, `references/jurisdictions.md`, `references/matter-file.md`, `references/jurisdictions/<code>.md`: the shared contract.
- `style.json`: the rules the checker applies to this skill.
- `scripts/litcheck.py`: the fields helper and the checker. `assets/fields.json`, `assets/placeholders.json`: the field list and placeholder vocabulary.
- `agents/openai.yaml`: display metadata.
