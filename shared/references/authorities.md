# Authorities, citations and references

## The authority policy

This is the one rule with no exceptions. A fabricated authority in a court document can end a career and mislead a court.

1. **Cite only what the user supplied or verified.** An authority may appear in a draft only if it is in the matter file's `authorities` list, or the user gave it in the conversation, or the user asked you to verify it and you checked it against an official or primary source and recorded where (in the matter file, `verified_source`). Your own memory of a case is not verification.
2. **Never invent.** Not a case name, a citation, a neutral citation, a report volume or page, a paragraph number, a judge, a statute section or a rule number. Not even one that "sounds right".
3. **Mark the gap.** Where the argument needs an authority the user has not given, write `[authority needed: <the proposition>]` and list it in "Fields to complete". The proposition tells the user exactly what to find, for example `[authority needed: a statement verified by a statement of truth and later withdrawn needs an explanation]`.
4. **Keep the user's citation as given.** If a supplied citation looks wrong (a year that does not fit, a garbled name), keep it exactly as given and flag it in one line above the draft. Do not silently correct it.
5. **Do not choose the law.** Which statute, rule, threshold or interest provision applies is the user's call. If they have not said, write `[statutory provision]` or `[rule]`.
6. **Pinpoint every citation.** A case is cited with the paragraph or page relied on. If the user gave the case but not the pinpoint, write the citation followed by `at [§ needed]` and list it.
7. **The policy covers everything you write, not only the draft.** Notes to counsel, flags above the draft, the "FIELDS TO COMPLETE" table and your reply to the user follow the same rule. Never name a rule number, practice direction, paragraph or case from memory there either. Describe what to check instead: "Check the court's practice on the notice required for a strike-out application", not a paragraph number you have not been given.

The checker flags every citation in the draft. Run it with `--matter matter.json` and it fails any citation that is not in the matter file's authorities.

## Ask for the sources

A citation tells you where an authority is; only its text tells you what it says. Whenever a document will quote an authority or state a principle or test from it, ask the user to share the authority itself: the judgment (or the paragraphs relied on), the textbook or practice-book passage, and the rule or statute as it now reads. Ask once, with the other materials. If the text is not shared, you may still cite the authority with its pinpoint, but never quote it from memory: where a quotation would go, write `[quotation needed: <authority and paragraph>]` and list it in "FIELDS TO COMPLETE".

## Quotations and paraphrases

- **A quotation is reproduced exactly.** Where the user quotes a passage in quotation marks, or names a paragraph to be quoted, reproduce it word for word from the source: the same words, spelling, punctuation, capitals and paragraph numbers. Never paraphrase it, tidy it, modernise it or merge it with your own words. Mark an omission with an ellipsis, an insertion with square brackets, and an error in the original with "(sic)". If the source is not available to check, keep the user's text exactly and flag "quotation not checked against the source" above the draft.
- **Emphasis is marked.** If the user wants part of a quotation emphasised, apply the emphasis (in the user's house style: bold, underline or italics) to those words only, and put "(emphasis added)" immediately after the closing quotation mark or the end of the block. Emphasis already in the source is "(emphasis in original)". Never add emphasis without the tag, and never use the tag where nothing was emphasised.
- **A paraphrase stays exact in substance.** Where the user's draft or notes paraphrase a principle, the elements of a cause of action or a legal test, keep it substantively accurate and precise: the same elements, the same threshold words ("plain and obvious", "real prospect of success", "triable issue"), the same qualifications and exceptions, and the same order where the order matters. Do not broaden, narrow, soften or merge limbs, and do not add an element. Attribute the paraphrase to its authority with a pinpoint. If you have the source, check the paraphrase against it and flag any difference above the draft rather than silently changing it; if you do not, keep the user's paraphrase and do not "improve" its substance.

## Stating and applying a test

In submissions and advice, the law is stated so the court can see where it comes from:

- **Quote, then distil.** Quote the governing passage in an indented block, keeping the judgment's own paragraph numbers and following "Quotations and paraphrases" above. Then distil it into numbered propositions ("First, … Second, …") or a named test of your own ("Step 1 to Step 4", "the three limbs").
- **One proposition, one source.** Each proposition carries its authority and pinpoint.
- **Apply in the same order.** Take the facts through the test using the same ordinals or sub-headings, and close each limb in one line ("The first limb is not met.").
- **Adverse authority gets its own heading.** If the court or the other side relies on an authority against you, deal with it under its own heading: what it decided, why it does not apply or is not binding. Do not leave it unanswered.

Pleadings and evidence never state a test or cite a case. A pleading cites statutes only where a claim depends on them (by section and chapter or code). Evidence carries law only through "I am advised and verily believe that …".

## Pinpoints and citation form

Citation style comes from the jurisdiction profile (`jurisdictions/<code>.md`): Hong Kong neutral and report citations with "§" pinpoints; the Bluebook for federal and Delaware courts; the New York Official Reports style; the California Style Manual; the Washington Style Sheet. Use one style throughout a document. Give the full citation at first mention, then a short name, the same short name every time.

## Bundle references

Every fact in a submission, and every document referred to in evidence, points to where it is:

- **Legend first.** State the reference scheme near the top: `[A12/§3] = Bundle A, page 12, paragraph 3`. The bundle scheme is a field; use the user's.
- **At the end of the sentence.** Put the reference at the end of the sentence it supports, in square brackets, not in a footnote: "The Defendant did not reply [B45]."
- **`[Bundle ref]` until paginated.** If the bundle is not yet paginated, write `[Bundle ref]` after each fact that needs one. Never invent a page.
- **Authority tags.** Where authorities are bundled, tag each at first citation with the user's scheme, for example `[P#3]` or `[Authority#3]`, numbered in order of first citation. In a sequence of papers, continue the numbering from the last list.

## The other side's papers and your own earlier papers

Refer to a paragraph of another paper with a label built from the party label and "§": `[D§12]` is paragraph 12 of the Defendant's paper, `[P§4-6]` paragraphs 4 to 6 of the Plaintiff's. Declare each label once in the legend: "[D§n] = paragraph n of the Defendant's Skeleton Submissions dated [date]". For more than one paper from the same party, add a short tag: `[D1§n]`, `[D2§n]`, declared the same way. Use the same labels in headings when a reply answers the other side paragraph by paragraph.

## Lists of authorities

A list of authorities repeats the document's caption, lists each authority once in order of first citation with its full citation and no pinpoint, puts statutes and rules in their own group, and is signed and dated like the document it accompanies. Number it consistently with the tags used in the text.
