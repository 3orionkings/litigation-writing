---
name: litigation-submissions
description: "Drafts counsel's submissions to a court, with every fact tied to the record, for Hong Kong or a US court (federal, New York, California, Washington, Delaware): interlocutory skeletons or memoranda of law, replies, hearing notes, private speaking notes, trial openings and closings, leave to appeal (including out of time), appeal submissions, costs submissions, lists of authorities and chronologies. Use it for a skeleton or skeleton argument, written submissions, memorandum of law, brief in support or opposition, points and authorities, reply brief, hearing note for a call-over or case management hearing, speaking note, opening or closing, leave to appeal, appeal skeleton, indemnity costs, list or table of authorities, or an agreed chronology. Not for: pleadings (litigation-pleadings), affirmations or declarations (litigation-evidence), counsel's advice (litigation-advice), letters to the other side (litigation-correspondence), or a summons, notice of motion or draft order alone (litigation-writing)."
---

# Litigation Submissions

## What this skill is for

It drafts the papers counsel puts before a court to argue an application, a trial, an appeal or costs, and the two supporting documents that travel with them: the list of authorities and the chronology. Every one of them has the same three jobs. The judge must see on page one what is asked and why; must be able to find every fact in the bundle from its reference; and must find, at the end, the order to make, already drafted.

The drafting moves below hold in every court. What changes by court (document names, length limits and certificates, the US motion package, citation style) is in the jurisdiction profile.

## Who is speaking

Counsel, as advocate for the party, addressing the court ("the Court", "this Court").

- **Impersonal.** "It is submitted that", "[Plaintiff]'s case is that", or the party's defined abbreviation as the subject. No "I" and no "we" in a written paper, and never the advocate's own belief ("I believe", "we are confident"). The speaking note is the exception: it is a private script, and the first person is allowed there.
- **Facts only from the record.** Every factual sentence ends with its bundle or record reference, or `[Bundle ref]` until the bundle is paginated. The advocate never vouches for a fact and never adds one. If a fact the argument needs is not in evidence, say so to the user: it needs an affirmation or declaration (litigation-evidence), not a sentence in the skeleton.
- **Law only from supplied authorities.** Tests are stated with their source and pinpoint, from the user's authorities; gaps are marked.
- **Heat aimed at the case, not the lawyers.** Criticism is of the other side's case and conduct, tied to a reference. Opposing counsel is not criticised.
- **Temperature follows the paper.** Assertive in a contested skeleton or reply; measured in an appeal; controlled in costs submissions; nil in a hearing note and an agreed chronology.
- **A chronology has no speaker.** It is a record of dated events; see `references/chronology.md` for how much a party's version may show.

## Before drafting

1. **Matter file.** Look for `matter.json` in the working folder and read it first (`references/matter-file.md`). Ask only for what it lacks.
2. **Jurisdiction.** Required, with no default: `hk`, `us-federal`, `ny`, `ca`, `wa`, `de-superior` or `de-chancery`. Read only that profile, `references/jurisdictions/<code>.md`. For a court with no profile, say so, use the closest profile as a guide only, and flag every formal requirement for the user to check.
3. **Fields.** Run `python3 scripts/litcheck.py fields --skill litigation-submissions --variant <v> --jurisdiction <code> [--matter matter.json]` (or read `assets/fields.json`). It lists the fields as R, O or L.
4. **Ask once.** In one grouped message, ask for the missing R fields: the applications and the relief each seeks; the orders sought; the hearing; the evidence filed and the bundle scheme; the prior orders; the paper being answered, with its date (for a reply, an appeal or costs); the grounds or issues; the authorities. If the user says go ahead, draft with placeholders from `references/fields.md`.
5. **Authorities.** Cite only what the user supplied or verified (`references/authorities.md`). Never a case, citation, paragraph, judge or rule from memory. Where the argument needs one, write `[authority needed: <the proposition>]`. Keep a supplied citation exactly as given and flag it in one line above the draft if it looks wrong. Pinpoint every citation, or write `at [§ needed]`. Which statute, rule, threshold or interest provision applies is the user's call: `[statutory provision]`, `[rule]`.
6. **The materials.** In the same message, ask the user to share what they have: copies or extracts of every authority relied on (the judgment with the paragraphs to be cited, the textbook or practice-book passage, the rule or statute as it now reads); the pleadings; the evidence filed and its exhibits; the other side's paper being answered; prior orders and transcripts. A quotation can be exact, and a stated test precise, only when the source is in hand. Quote and paraphrase as `references/authorities.md` ("Quotations and paraphrases") requires: a verbatim quotation is never paraphrased, emphasis carries "(emphasis added)", and a paraphrase of a principle keeps its elements and threshold words exactly.

## Variants

| Variant | What it is | When to use it | Read |
|---|---|---|---|
| `skeleton` | Interlocutory skeleton submissions; US memorandum of law or brief in support or opposition | A contested summons or motion, a supplemental skeleton, an unopposed originating summons that needs reasons | `references/skeleton.md` |
| `reply` | Reply skeleton or reply note; US reply brief | Answering the other side's skeleton or opposition | `references/reply.md` |
| `hearing-note` | Short factual note with the directions sought | Call-over, case management hearing, first appointment, time application | `references/hearing-note.md` |
| `speaking-note` | Private oral script: primary position, fallback, scripted replies, the number to concede | Preparing the advocate for the hearing; never filed | `references/speaking-note.md` |
| `trial-opening` | Opening submissions: the parties' cases side by side, the issues as a decision tree, one section per issue | Before trial; US trial brief | `references/trial-opening.md` |
| `trial-closing` | Closing submissions: evidence by witness and topic, findings sought, weight | After the evidence; US post-trial brief or proposed findings | `references/trial-closing.md` |
| `appeal-leave` | Leave to appeal, including out of time; resisting or setting aside leave | Grounds, delay, prospects, importance | `references/appeal-leave.md` |
| `appeal` | Substantive appeal submissions, grounds in order of strength | The hearing of the appeal, for either side | `references/appeal.md` |
| `costs` | Costs submissions: base order conceded where right, uplifts, indemnity costs, certificate for counsel, assessment | Written costs submissions, a costs-variation summons; US fee or costs motion | `references/costs.md` |
| `authorities-list` | List of authorities; US table of authorities | With any paper that cites authority | `references/authorities-list.md` |
| `chronology` | Chronology, agreed or a party's | Annexed to a paper, or filed as agreed | `references/chronology.md` |

## The moves

1. **Capture page one.** Begin with the hearing sentence: whose application, its date, its defined term, the relief as (1), (2), (3), and its reference. Then at once "In gist, the [Plaintiff]'s stance is that:" with one lettered line per ground. The judge has the application, the relief and the answer before any fact. In a US memorandum the preliminary statement does the same job.
2. **Say it twice.** The overview names every ground in one line; the analysis develops each under the same number, in the same order. A ground only in the analysis may be missed; a ground only in the overview is a promise not kept.
3. **Lock the gateway facts with the other side's own material.** Before arguing, fix the facts the argument stands on: "It is not in dispute that:", the other side's own affirmation, letters and admissions, or their silence ("No reply was received [Bundle ref]."). Their own words outweigh any adjective.
4. **Turn the authorities into a named, numbered test.** Quote the governing passage, keeping its paragraph numbers, then distil it: "Step 1 to Step 4", "the three limbs", "the Threshold Test". Apply it in the same order under the same names and close each limb in one line ("Step 2 is not met."). Enter each later sequential step "If the answer to Step 1 is yes (which is denied), …".
5. **Pair Legal Principles and Analysis under each ground.** The heading states the ground's conclusion as a sentence. The principles are only what that ground needs; the analysis applies them; the ground ends on a disposal sentence ("The Summons fails on this ground alone.").
6. **Answer the other side inside your own structure.** Meet their points where your argument reaches them, by their paragraph labels: "[D§12-14]: …", "At [D§15], the [Defendant] contends that …. That is misconceived because …". Never open with a neutral summary of their case. The one exception is the trial opening, which sets out both cases side by side before the issues.
7. **Concede the undeniable early, then pivot.** Admit in one plain sentence what cannot be fought, and move to what matters: concede the base costs order and fight the uplifts; quote an adverse finding accurately and confine it; accept a procedural lapse, explain it, and show no prejudice.
8. **Argue alternatives as a cascade.** The test does not apply; if it does, it is met; in any event the result is the same. Mark each fallback so it cannot be read as a concession: "taken at its highest (which is denied)".
9. **Draft the order wanted in full.** The conclusion sets out the orders as the court would make them: numbered, deadlines as dates (with "4:00 pm" where the court fixes a time), the consequence of default, sums, interest at `[rate]` from a date, and costs terms. Directions are order paragraphs, not descriptions. When opposing more time, draft the fallback unless order as well.
10. **Make the litigation history the abuse argument.** Where the other side's conduct is the point, count it: each earlier application or default numbered, dated, referenced and closed with its result in a short sentence ("That failed."). A dated list of their changing positions, each in their own words, proves an afterthought better than any label.
11. **Use the tribunal's own words.** The test as the hearing judge has already put it, a prior order's exact terms, the judge below's own findings with "(emphasis added)": each carries more weight than a paraphrase.
12. **Give adverse authority its own heading.** An authority against you, from the other side or from the bench, is met under its own heading: what it decided, why it is distinguishable, not binding or not persuasive, and why it would not assist even if applied.
13. **Build the costs case from page one.** If indemnity costs or a certificate for counsel will be sought, reference the conduct that justifies it as the facts are told, and list it as numbered reasons in the conclusion. In costs submissions, measure success in a way the court can check (issues won, hearing time) and put the figures in an annexed table.
14. **Keep replies and oral notes disciplined.** Open a reply with the common ground the other side's paper concedes; answer by their labels, weakest point first; cross-refer rather than re-argue ("For [D§20-25], the [Plaintiff] relies on [P1§30-34]"). A speaking note scripts "If they say … → reply", states the primary position and the fallback, and gives the number to concede.

## Language

- **Formulae.** Use the forms in `references/formulae.md` word for word: openings, signposts, the "(which is denied)" bracket, order and costs terms, certificates, US headings and record citations.
- **Person and address.** The party by its defined abbreviation in Hong Kong ("P", "D", announced in the party line); by "Plaintiff" or a short name in a US paper. "The Court" in writing; never "Your Lordship" or "Your Honour" in a written paper. Labels for other papers (`[D§n]`, `[P1§n]`, `[Decision/§n]`) are declared once in the legend.
- **Sentences.** About 20 words on average, many under ten. A long paragraph ends on a short verdict sentence: "It is not." "That failed." "No reply was received." In Hong Kong every paragraph is numbered, with sub-points (a), (b), then (i), (ii). A US brief or memorandum uses headings and unnumbered paragraphs, as its court's rules expect (read the profile). Never bullets in a filed paper.
- **Signposts sparingly.** "It is submitted that" where a submission needs marking, not in every sentence. One "In gist" on page one. "Suffice to say", "In the premises", "A fortiori", "In any event" when they do work, and not twice in a paragraph.
- **Verdict words, once a point.** "Misconceived", "no answer", "does not assist", "bound to fail", each tied to a reference. No piles of adjectives, no stacked idioms. A rhetorical question never opens a document or a section.
- **Defined terms inline** in brackets at first use, then used consistently. Dates and citations in the profile's style; one style throughout.
- **Quotations exact.** Indented blocks keep the source's paragraph numbers; "(emphasis added)" only where emphasis was added; "(sic)" for the other side's or a witness's errors.

## Workflow

1. Settle the variant and the jurisdiction. Read the variant's reference file, the profile and `references/formulae.md`.
2. Run the fields helper and ask once for the missing required fields.
3. Collect the record: the applications and relief, prior orders, the evidence with its references, the paper being answered with its labels, the authorities supplied.
4. Plan on one page before writing prose: the stance in one sentence; the grounds in order (strongest first; in a reply, the other side's weakest first); for each ground the test and the facts that meet it; then the orders. Draft the orders first, so the argument is written towards them.
5. Draft the caption, the legend and page one.
6. Draft the body in the reference file's structure: one Legal Principles and Analysis pair per ground, each limb closed in one line, each ground ending on its disposal sentence.
7. Draft the conclusion: one sentence characterising the other side's position, then the orders in full with costs. No recap.
8. Check by eye: every fact has a reference; the overview's grounds match the analysis; every citation is the user's, with a pinpoint; the list of authorities matches the tags; cross-references and sums agree throughout.
9. Make the register pass (below).
10. Run `python3 scripts/litcheck.py check draft.md --skill litigation-submissions --variant <v> --jurisdiction <code> [--matter matter.json]`. Fix every hard failure; look again at each note.
11. Return the draft, followed by the "FIELDS TO COMPLETE" table if any placeholder remains. Above the draft, in one line each, flag: any supplied citation that looks wrong, any date you computed (with the arithmetic), any chronology row you moved, and any formal requirement of a court with no profile.

## The register pass

Apply "The register pass" in `references/voice.md` as the last step before the checker: reread the running prose, cut the tells listed there, vary sentence length, end each paragraph on its point, and replace every dash. In submissions, also cut signposts stacked at paragraph openings; adjectives with no reference behind them; a ground stated a second time in the same words; any closing paragraph that recaps; "not X; it is Y" chains; and abstract bold labels (turn them into ordinals or `[D§n]` labels).

What must survive verbatim:

- every formula in `references/formulae.md`, including "(which is denied)" and "further and/or alternatively";
- the orders in court language ("do pay", "be at liberty", "Liberty to apply", "to be taxed if not agreed"), with their "and/or" stacks and alternatives;
- "First … Second … Third" runs and one-line verdict sentences, which are the voice, not tells;
- numbered paragraphs and (a), (i) sub-lists;
- quotations exactly as in the source, with "(sic)" and emphasis tags;
- citations, pinpoints, bundle and record references, `[D§n]` labels, defined terms, sums, dates, times and placeholders;
- certificate wording and headings that a rule prescribes;
- in a speaking note, the cue lines and arrows (fragments are its form); in a chronology, one plain past-tense sentence per row;
- the user's own settled phrasing when editing their draft.

## What makes a draft fail

- A fact with no reference, or a reference that was invented.
- A citation the user did not supply, a pinpoint from memory, or a threshold or rule chosen for the user.
- Page one that tells the story instead of stating the application, the relief and the answer.
- Grounds in the overview and the analysis that differ in number, order or wording.
- A neutral summary of the other side's case at the start (outside a trial opening), or a separate rebuttal section that re-argues.
- "I" or "we" in a written paper, "Your Lordship" in writing, or counsel's personal view.
- Orders described rather than drafted: no costs terms, an unless order with no date and hour, directions with no dates.
- A conclusion that recaps each ground.
- Heat with no reference behind it; idioms stacked; a rhetorical question opening a section.
- A reply that re-argues the main skeleton, raises a new ground or adds evidence.
- An agreed chronology carrying argument; rows out of date order; the tense drifting into the present.
- A list of authorities with pinpoints, with numbers that do not match the tags, or with entries never cited.
- In a US paper: a Hong Kong bundle tag or "P"/"D" abbreviations; no word certificate where the rule needs one; no tables above the length threshold; a California summary judgment motion without its separate statement; a length over the limit.
- Careless slips a judge will notice: a stale cross-reference, a sum that differs between paragraphs, the wrong party, a heading typo.

## Files

- `references/skeleton.md`, `references/reply.md`, `references/hearing-note.md`, `references/speaking-note.md`, `references/trial-opening.md`, `references/trial-closing.md`, `references/appeal-leave.md`, `references/appeal.md`, `references/costs.md`, `references/authorities-list.md`, `references/chronology.md`: one per variant.
- `references/formulae.md`: the family's formulae, verbatim, by system.
- `references/voice.md`, `references/fields.md`, `references/authorities.md`, `references/matter-file.md`, `references/jurisdictions.md` and `references/jurisdictions/<code>.md`: the shared core.
- `style.json`: this skill's structural rules by variant, read by the checker.
- `assets/`: the shared rule files (`fields.json`, `jurisdictions.json`, `perspective.json`, `register.json`, `placeholders.json`, `matter.template.json`).
- `scripts/litcheck.py`: the checker and fields helper.
