# Packages: the documents a step in the case needs

Use this to plan before drafting. Each package lists the documents in the order to draft them, the skill for each, and the fields they must share. Adjust to the court's rules and any directions already given; the profiles in `jurisdictions/` say what each court expects.

## The plan to show the user

```
PACKAGE PLAN: [document title]
Jurisdiction: [court] ([code])
Orders sought (the spine): 1. [ ] 2. [ ] 3. Costs [ ]

Draft in this order
1. [document] .......... [skill] / [variant] .......... status: to draft
2. [document] .......... [skill] / [variant] .......... status: to draft
...
Shared fields still missing: [field], [field]
Deadlines: [date 1] filing of [document]; [date 2] hearing
```

The plan is a working note for the lawyer. Keep it short, and update it as documents are drafted.

## Hong Kong

**Making an interlocutory application (inter partes).**
1. The orders sought, settled in court language (this skill).
2. Supporting affirmation (`litigation-evidence` / `affirmation`): the purpose paragraph repeats the orders sought.
3. Summons (this skill / `summons`).
4. Draft order, where directions, an unless order or detailed terms are sought (this skill / `draft-order`).
5. Skeleton submissions and list of authorities, once the evidence is in (`litigation-submissions` / `skeleton`, `authorities-list`).
6. Hearing note for a short or procedural hearing instead of a skeleton (`litigation-submissions` / `hearing-note`).

**Opposing an application.** Affirmation in opposition (`litigation-evidence` / `affirmation`), then skeleton (`litigation-submissions` / `skeleton`), list of authorities, and a draft of any alternative order (for example an unless order as the fallback).

**Ex parte application** (for example some enforcement steps). Affirmation, ex parte summons or application, draft order. No service before the hearing unless the court directs.

**Issuing a claim.** Letter before action if appropriate (`litigation-correspondence` / `demand`); statement of claim (`litigation-pleadings` / `claim`), indorsed on or served with the writ. The writ itself is a court form: fill it from the court's current form rather than drafting it.

**Defending.** Request for further and better particulars if the claim is unclear (`litigation-correspondence` / `particulars-request`); defence, or defence and counterclaim (`litigation-pleadings` / `defence`, `counterclaim`).

**Amending a pleading.** Amended pleading (`litigation-pleadings` / `amendment`); if leave is needed, the summons for leave with the draft annexed, an affirmation explaining the amendment and any delay or change of case, and a draft order with consequential directions and costs.

**Trial.** Witness statements (`litigation-evidence` / `witness-statement`); chronology (`litigation-submissions` / `chronology`); opening submissions and list of authorities (`trial-opening`, `authorities-list`); closing submissions (`trial-closing`).

**Enforcement.** Enforcement affirmation (`litigation-evidence` / `enforcement`); the application (summons or ex parte application under `[rule]`); draft order.

**Appeal.** Affirmation explaining any delay (`litigation-evidence` / `procedural`); leave submissions (`litigation-submissions` / `appeal-leave`); later the appeal submissions (`appeal`) and a list of authorities. The notice of appeal follows the court's prescribed form.

**Costs.** Costs submissions (`litigation-submissions` / `costs`); a sanctioned offer or other rule-based offer, made earlier, is a letter (`litigation-correspondence` / `offer`).

## United States

**Making a motion.**
1. Check the court's pre-motion steps: meet and confer where a rule or the judge requires it (California CCP 430.41 and 435.5 before a demurrer or motion to strike; many federal judges' individual practices; New York Commercial Division Rule 24 pre-motion letter). A meet-and-confer letter is `litigation-correspondence`.
2. Declaration or affirmation with exhibits (`litigation-evidence` / `affirmation`).
3. Notice of motion, or the motion, stating the relief and grounds (this skill / `summons`).
4. Memorandum of law or brief (`litigation-submissions` / `skeleton`), within the word or page limit, with the word-count certificate the court requires.
5. Proposed order where the court wants one (this skill / `draft-order`); in the New York Commercial Division, none on a dispositive motion.
6. For summary judgment in California, the separate statement; in the New York Commercial Division, a statement of material facts if directed (`litigation-submissions`, read the profile).

**Opposing a motion.** Declaration, opposition memorandum, any evidentiary objections, and a proposed order if the court wants one.

**Pleadings.** Complaint (`litigation-pleadings` / `claim`); answer with affirmative defenses and any counterclaim (`defence`, `counterclaim`); amended pleading with a comparison and, where leave is needed, a motion for leave (`amendment`).

## Shared fields

Every package shares at least: `jurisdiction`, `court`, `case_number`, `parties`, `client_party`, `orders_sought`, `key_event_dates`, `defined_terms`, `bundle_scheme`, `authorities`. Record them in the matter file once.
