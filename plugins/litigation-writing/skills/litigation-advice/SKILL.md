---
name: litigation-advice
description: "Drafts counsel's written advice to instructing solicitors, in counsel's own first-person voice: on the merits of a claim or defence (in or before proceedings), on causes of action and how to plead them, or before action on potential claims or defences, including point-form notes for oral advice in conference. Use for an \"advice\", \"opinion\", \"merits advice\", \"preliminary advice\", \"advice on prospects\", \"advice on pleadings\", \"causes of action\", \"pre-action advice\", \"pre-suit advice\", \"opinion memo\" or \"point form for oral advice\", in Hong Kong or a US court. Sets out the issues as numbered questions, an executive summary answering them, principle, test, application and interim conclusion for each issue, likelihood in words with the hedge, the information still needed and the formal close. Not for: submissions or skeletons to the court (use litigation-submissions), the pleading itself (use litigation-pleadings), letters to the other side (use litigation-correspondence)."
---

# Litigation Advice

## What this skill is for

Counsel's written advice on a contentious matter, sent to instructing solicitors for the client. The solicitors rely on it to report to the client, to decide what to do next, and to brief the next document: the pleading, the evidence, the skeleton. It has three variants: an advice on the merits, an advice on pleading (which causes of action, and the particulars each needs), and a pre-action advice (which may be point-form notes for an advice given orally).

An advice is the one litigation document in which counsel speaks in their own voice and gives their own view. That makes it the place where candour matters most. A client who is told what they want to hear, or given a number that sounds precise, makes worse decisions than one who is told plainly where the case is weak and what is still unknown.

## Who is speaking

- **Counsel, in the first person singular.** "I am asked to advise on", "I am instructed that", "I incline to take the view that". The view is counsel's opinion, so it is never written as fact or as what the court will do. A joint advice signed with the firm uses "we" throughout; the checker expects "I", so warn the user that it will report that.
- **To instructing solicitors.** In Hong Kong the advice goes to the instructing solicitors, who act for the client. In the US it goes to the client's in-house counsel, lead counsel or the supervising attorney. The lay client reads it through them. So the advice never says "you" to the client and never directs the client in the imperative. It says what "should be pleaded", what the client "may wish to consider", or what "I recommend".
- **Candid about the client's own case.** Name the weak points on the client's side, test the client's own best arguments and say when they will not assist, and say when the client's witness will hurt. Never praise the client or the client's case. The other side's documents may be criticised; the other side's people are not.
- **On a stated basis.** Every fact comes from the documents provided or the instructions, and facts that come only from the instructions are marked "I am instructed that". Where a fact is missing, say so and stop: do not speculate, and do not grade a point the information cannot support.
- **Privileged.** Head the advice "PRIVILEGED AND CONFIDENTIAL". In the US add "ATTORNEY-CLIENT COMMUNICATION" and, where litigation is anticipated or pending, "ATTORNEY WORK PRODUCT". Check the profile for local practice.

## Before drafting

1. **The matter file.** Look for `matter.json` in the user's folder, or ask whether there is one. Take every value it holds and ask only for what it lacks (`references/matter-file.md`).
2. **The jurisdiction.** If the user has not said which court or forum, ask. Read only the matching `references/jurisdictions/<code>.md`. The shape of an advice is the same everywhere; what changes is the procedure discussed, the pleading standard (for the pleadings variant), the citation style and the privilege headings.
3. **The fields.** Run `python3 scripts/litcheck.py fields --skill litigation-advice --variant <v> --jurisdiction <code> [--matter matter.json]`. If scripts cannot run, read `assets/fields.json`.
4. **Ask once, grouped.** Ask in one message for the missing required fields: who instructs and for whom; the date of the instructions and the questions asked (verbatim if possible); the documents provided (they become Annex 1); the parties and their roles; the forum and the case number if proceedings exist; the key facts and dates; the authorities to rely on, with pinpoints; for the pleadings variant, the contract terms verbatim and the figures behind any sum. If the user says to go ahead without some of them, draft with placeholders from `references/fields.md`.
5. **Authorities.** Cite only authorities the user supplied or asked you to verify against a primary source (`references/authorities.md`). The principle under each issue comes from those, with a textbook or treatise by edition and paragraph only if the user gives it. Where an issue needs an authority the user has not given, state the proposition neutrally and mark it `[authority needed: <the proposition>]`; never fill it from memory. Keep a supplied citation exactly as given and flag a doubtful one in a line above the draft. Which statute, limitation period or threshold applies is the user's call: write `[statutory provision]` or `[rule]` unless told.
6. **The materials.** In the same message, ask the instructing solicitors (through the user) to share what they have: the instructions and the documents provided (they become Annex 1); copies or extracts of the authorities to be relied on, with the paragraphs; the pleadings and correspondence if proceedings exist. Quote and paraphrase as `references/authorities.md` ("Quotations and paraphrases") requires: a verbatim quotation is never paraphrased, emphasis carries "(emphasis added)", and a paraphrase of a principle or test keeps its elements and threshold words exactly.

## Variants

| Variant id | What it is | When to use it | Read |
|---|---|---|---|
| `merits` | Advice on the merits of a claim or defence | Proceedings are on foot or about to be; the client needs a view on liability, a defence, an application, or the case overall | `references/merits.md` |
| `pleadings` | Advice on causes of action and how to plead them, ending each with the particulars to plead | Before a claim, counterclaim or amendment is drafted; the solicitors need to know what to plead and what relief to claim | `references/pleadings.md` |
| `pre-action` | Pre-action advice on potential claims or defences, including point-form advice for oral delivery | Before proceedings; a demand has been received or is contemplated; notes for a conference | `references/pre-action.md` |

The trade-register formulae for all three are in `references/formulae.md`.

## The moves

1. **Overview first.** Open with who instructs and for whom, what counsel is asked to advise on, and on what documents. List the documents in Annex 1 rather than in the text. For a long advice, add one line on its purpose and a short table of contents.
2. **Reframe where the facts demand it.** If an instructed question cannot be answered until an earlier one is settled (who the parties to the contract are, when it was made, what its terms were), add preliminary issues, say in one sentence why they come first, and answer them first.
3. **Issues as numbered questions.** "Issue 1: Whether …?" Each later heading repeats its issue as a question.
4. **Executive summary in the same order.** Answer each issue in the same numbering, in a sentence each, with the word from the verbal scale that the interim conclusion uses. Then hand off ("Each issue is analysed in turn below.") and give the hedge.
5. **Per issue, four steps.** (a) The principle, from the supplied authorities, quoted in an indented block with the judgment's or text's paragraph numbers kept and "(emphasis added)" wherever emphasis is added. (b) The test, distilled in counsel's own words: "First, … Second, … Finally, …", or a named test defined in brackets ("Step 1"). (c) The pivot: "Applying the principles here, the question to ask is as follows:", then the question, then the application in lettered sub-paragraphs, taking the facts through the test in the same order. (d) The interim conclusion, in one or two sentences, on the scale and hedged.
6. **Scenarios where the facts are open.** If the answer turns on a fact nobody yet knows, enumerate the scenarios (Scenario 1, Scenario 2) and give a view on each, rather than guessing which is true.
7. **The client's own arguments, tested.** Put the client's likely arguments as question headings ("Is it a defence that …?") and answer each candidly, including "This would not assist [Party] because …".
8. **The other side's case, paragraph by paragraph.** Where the opponent has pleaded or written, take its document in order with `[D§n]` labels declared once, and answer each point.
9. **One fixed list of missing information.** Keep the unknowns in one numbered list in their own section, refer back to it wherever a conclusion depends on it ("subject to item (c) of paragraph [number]"), and end the list with the formal request for the information.
10. **For pleading advice, finish each cause of action.** End each with "Particulars to plead" as a lettered list, and close the advice with the relief to be claimed. A minimum sum is stated only from figures the user gave, with the arithmetic shown.
11. **Overall view, hedge, close.** At most one evaluative sentence on the case overall, the hedge, an optional line on the hazards of litigation and on settlement or mediation, then the formal two-sentence close. Nothing restates the analysis.
12. **Two authority lists.** "List of Authorities" (those cited, in order of first citation) and "Other Authorities Considered" (read but not cited), each with full citations as supplied.

## Language

- **Opinion verbs.** "I am of the view that", "I incline to take the view that", "I incline to take the preliminary view that", "I am not of the view that". Use one or two of these consistently; do not rotate them for variety.
- **Likelihood in words, never numbers.** No percentage, fraction, ratio or odds, even if the client asks: a number implies a precision the evidence cannot support, and it gets quoted back. Use the scale below, the same word for the same issue in the summary and the interim conclusion.

  | For the party advised | Words |
  |---|---|
  | Hopeless | "bound to fail", "cannot get off the ground", "would hold no water" |
  | Weak | "unlikely to succeed", "very difficult to prove", "highly unlikely" |
  | Open | "arguable", "at least arguable", "a live issue for argument" |
  | Balanced | "finely balanced" |
  | Better than even | "slightly more likely than not", "more likely than not" |
  | Good | "likely to succeed", "inherently more probable" |

  Do not go beyond "likely": "bound to succeed", "cannot lose" and "a strong case" are praise, not opinion.
- **Always hedged.** Every view on likelihood carries a qualifier: "on the information provided", "subject to further information", "subject to [Party] coming up to proof", "at this stage", "on the balance of probabilities". Where the information cannot support a view, say "I am in no position to assess this on the information provided" and say what would change that.
- **Temperature.** Cool and measured. Words of judgment go to documents and arguments ("unsupported", "inconsistent with the Defence at [D§12]"), never to people. Strong words about the client's prospects are allowed when they are true.
- **Sentences.** About 20 words on average, many shorter. A long paragraph of analysis may end on a short verdict ("That is not enough." "The first limb is not met."). A plain-words gloss after a dense point is fine: "Put simply, …".
- **Form.** Numbered paragraphs throughout; sub-points (a), (b), then (i), (ii); never bullet glyphs. Defined terms in brackets at first use ("the Agreement"), then used the same way every time. Quotations faithful, with "(sic)" for an error in the original and "…" for omissions.

## Workflow

1. Run the fields helper, read the matter file and ask once for the missing required fields.
2. Read the variant's reference file and `references/formulae.md`.
3. Settle the issues as numbered questions, adding preliminary issues if the facts demand them.
4. Draft the analysis first, issue by issue: principle, test, "Applying the principles here, the question to ask is as follows:", application, interim conclusion. Build the missing-information list as you go.
5. Draft the background (only what bears on the issues), the other side's case and the client's own arguments.
6. Draft the executive summary from the interim conclusions, in the same order and with the same scale words. Then the overall view, the hedge and the formal close.
7. Add Annex 1 (documents provided) and the two authority lists. Every authority must be one the user supplied; every gap is `[authority needed: …]`.
8. Do the register pass below.
9. Run `python3 scripts/litcheck.py check draft.md --skill litigation-advice --variant <v> --jurisdiction <code> [--matter matter.json]`. Fix every hard failure and look again at each soft one.
10. Return the draft, followed by the "FIELDS TO COMPLETE" table if any placeholder remains.

## The register pass

Apply "The register pass" in `references/voice.md` to the running prose as the last step before the checker. For an advice that means: cut the tells it lists; vary sentence length; end each paragraph on its point, never on a summary; replace any dash with a comma, brackets, a colon or a new sentence; and take out praise of the client and any "you".

Leave these exactly as they are, because they are the register of an advice and not tells:

- every formula in `references/formulae.md`, including "Applying the principles here, the question to ask is as follows:" and the formal close;
- the hedges and the words of the verbal scale, which are chosen and must match between the summary and the interim conclusions;
- "First, … Second, … Finally, …" runs and named tests ("Step 1"), which carry the structure of the test;
- block quotations, with their paragraph numbers, ellipses, "(emphasis added)" and "(sic)";
- numbered paragraphs, lettered sub-points and the numbered issue questions;
- every citation and pinpoint, defined term, sum, date and placeholder;
- the user's own settled phrasing, if the user supplied a draft to edit.

## What makes a draft fail

- A percentage, ratio or odds for success, or any number near "chance", "prospect", "likelihood" or "success".
- "You should", "you must" or any instruction to the client in the imperative.
- A view on likelihood with no hedge, or a summary that grades an issue differently from its interim conclusion.
- An issue with no interim conclusion, or an executive summary that answers the issues in a different order.
- A principle stated with an authority the user did not supply, or a case cited without a pinpoint.
- Praise of the client's case, or silence about a weak point the documents show.
- A fact asserted that is not in the documents or the instructions, or a guess where the advice should say the information is missing.
- A cause of action recommended in a pleading advice without its particulars, or a sum to claim not built from the user's figures.
- A closing section that restates the analysis, or no formal close.
- Bullet glyphs, unnumbered paragraphs, or dash punctuation.

## Files

- `references/merits.md`, `references/pleadings.md`, `references/pre-action.md`: structure, skeleton and checklist for each variant.
- `references/formulae.md`: the advice formulae, verbatim, by jurisdiction.
- `references/voice.md`, `references/fields.md`, `references/authorities.md`, `references/jurisdictions.md`, `references/jurisdictions/<code>.md`, `references/matter-file.md`: the shared rules every skill in this plugin follows.
- `style.json`: the rules the checker applies to this skill and its variants.
- `scripts/litcheck.py`: the fields helper (`fields`) and the checker (`check`).
- `assets/`: the field list, placeholder vocabulary, perspective and register rules, jurisdiction rules and the matter-file template.
- `agents/openai.yaml`: display metadata for other assistants.
