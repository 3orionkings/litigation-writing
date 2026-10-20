# Amendment: amended and re-amended pleadings, and the application for leave

## What it is for

Amendment is an operation on a pleading already served: any claim, defence, reply, counterclaim or defence to counterclaim. The amended pleading must show the court and the other side exactly what has changed, when and on what authority, and it must still be internally consistent once changed. Most amendment errors are not in the new text but in what the drafter forgot to chase: a prayer item left at the old figure, a statement of truth that still names the old title, a backsheet that was never retitled.

Draft the new text with the variant reference for that pleading (`claim.md`, `defence.md` and so on), then apply this file.

## Hong Kong

### Does the amendment need leave?

- **Without leave (O.20 r.3).** Once only, before pleadings close, and only for the six pleadings: statement of claim, defence, counterclaim, defence to counterclaim, reply. A writ may be amended without leave once before pleadings close (O.20 r.1), but after service only for formal corrections, never to add, omit or substitute a party, change a capacity or add a cause of action. The other side may apply to disallow an amendment made without leave (O.20 r.4), so make only amendments that would be allowed on an application for leave.
- **With leave (O.20 rr.5, 8).** Everything else: a re-amendment, an amendment after pleadings close, amended particulars, a pleading after a reply. The draft amendment must be exactly formulated, annexed to the summons and shown in colour. Leave turns on whether the amendment raises the real question in controversy, is properly particularised, is not bound to fail, and does not add a cause of action that arose after the writ. A new cause of action after the limitation period is allowed only where it arises out of the same or substantially the same facts already pleaded (O.20 r.5(2), (5)). Changing a party's name or capacity after limitation has its own limits (O.20 r.5(3), (4)).
- **By written agreement (O.20 r.12).** At any stage, but never to add, omit or substitute a party (that needs leave under O.15).
- **Responsive amendments.** Where the other side amends, a consequential amendment of the answering pleading made without leave is confined to dealing with the amended allegations, and should be made within 14 days; otherwise issue is taken to be joined on the new allegations (O.20 r.3(2), (3)).

### When a supporting affirmation is needed

Ask the user, and pass the affirmation to `litigation-evidence`, where the amendment:
- pleads fraud, misrepresentation or another serious allegation for the first time (the affirmation explains why it was not pleaded before and shows it has substance).
- comes late, near or at trial (the affirmation accounts for the delay).
- departs from facts the party has already verified by a statement of truth (the change must be explained, O.20 r.13).
- withdraws an admission (good faith and a credible explanation).
- adds a cause of action after limitation, or changes a party's name or capacity.

### Mode of amendment (O.20 r.10)

1. **Legend.** At the head of the first page, above the title: that the pleading is amended, the date, and either the rule (without leave) or the judge or master and the date of the order (with leave). One legend per round, stacked, earlier ones kept. Forms: `formulae.md` section 13. With leave, the draft annexed to the summons carries the legend with the order date blank.
2. **Colour by round.** First amendment red, then green, violet and yellow for later rounds. This is the conventional sequence under Practice Direction 19.1 Part II; tell the user to check the current direction. Each round's insertions are underlined in its colour and its deletions struck through in its colour. Nothing is erased: struck text stays legible.
3. **Title by round.** "AMENDED", "RE-AMENDED", "RE-RE-AMENDED" before the title, on the face, in the statement of truth and on the backsheet, all three together.
4. **Numbering.** Never renumber existing paragraphs. A new paragraph after paragraph 11 is 11A (then 11B), with sub-paragraphs 11A.1 or (a), (b); a new item in a list continues its lettering; a deleted paragraph keeps its number with its text struck through. Cross-references to existing paragraphs therefore stay true; check every one that points at an inserted or deleted paragraph.
5. **Inside a sentence.** Insert and strike the exact words. When an item is added to a list, move "; and" to the new penultimate item and turn the old final full stop into a semicolon. Change tense where the facts have moved on, and widen a lead-in ("By reason of the matters aforesaid") where new matters feed it.
6. **The dated line and signatures.** Keep the original dated line and add a new one for the amendment, with counsel and solicitors as now instructed; strike the old one if that is the firm's practice, but never delete it.
7. **Statement of truth (O.20 r.13).** A fresh statement of truth naming the amended pleading by its new title ("this Amended Statement of Claim"), signed by a verifier who can stand behind the amended allegations. Strike the old one; do not leave it as the only verification.
8. **Backsheet.** Retitled to match the face. Keep Dated, Filed and Served, and add "Re-filed the [date]" for the amended version.
9. **Only what is authorised.** With leave, the amended pleading contains the amendments the order allows and nothing else. Make and serve it within the time the order sets, or within 14 days, or the leave lapses (O.20 r.9). An amended indorsed claim is re-served before any default judgment is sought. Amendments are never made by letter.
10. **Fresh document.** Where the changes are so many that the marked-up pleading would be hard to read, prepare a fresh document with the "Replaced by Amendment" legend instead of colour (O.20 r.10(1)); a writ is re-issued and the original marked "Superseded by amendment". Offer this when the insertions would exceed roughly a third of the pleading.
11. **Costs.** The costs of and occasioned by the amendment normally fall on the amending party. The summons asks for that order unless the user decides to seek something else; "costs reserved" or "costs in the cause" is the user's choice, not the default.

### Showing colour in a text draft

A text draft cannot carry colour. Mark the round's insertions as `++inserted words++` and its deletions as `~~deleted words~~`, and tell the user that in the filed copy these become underlined and struck through in the round's colour. Give a clean copy as a reading aid only: the clean copy is not the amended pleading.

### The consistency chase

After the amendments are made, go through the whole pleading, not only the amended paragraphs:
- every sum, rate and period that changed, wherever else it appears, above all in the prayer and its interest items.
- every defined term the amendment introduces, renames or retires.
- every cross-reference, in the body and in the prayer's paragraph ranges.
- the party references and pronouns in any section adapted from another.
- the legend, the title, the statement of truth and the backsheet together.
- consistency with the party's other pleadings, which may themselves need amendment.

### The summons for leave

Formal parts in `formulae.md` section 13. In order:
1. The caption, and "SUMMONS".
2. In the margin, the rules relied on, as the user gives them.
3. "LET ALL PARTIES concerned attend ..." with the tribunal, the place, the date and the time as placeholders (hearing details are fixed later).
4. The orders sought, numbered: leave to amend in the form of the annexed draft, naming each document and its colour (and the writ, if its indorsement changes, in its own round's colour); filing and service within a stated number of days; leave for the other side to file and serve a consequential amended pleading within a stated time, and for the applicant to answer it; costs of and occasioned by the amendment.
5. "Dated", "Registrar", the taking-out line with the firm's name and address, the estimated length of the hearing, and "To:" the other side's solicitors.
6. The annexed draft amended pleading (and draft amended writ), in colour, each with its legend and the order date blank.
7. The backsheet for the summons, with Dated and Filed.

The supporting affirmation belongs to `litigation-evidence`, a skeleton for a contested application to `litigation-submissions`, and the covering letter serving an amendment to `litigation-correspondence`.

## United States: what changes

- **A complete fresh pleading.** The amended pleading is a new, complete document that does not incorporate the earlier one by reference. No colours and no legend. It is titled by number: "First Amended Complaint", "Second Amended Answer" (California requires the serial number, CRC 3.1324(a)(1)).
- **As of course or with leave.**
  - Federal: once as a matter of course within 21 days after serving, or within 21 days after a responsive pleading or a Rule 12(b), (e) or (f) motion, whichever is earlier (FRCP 15(a)(1)); otherwise with written consent or leave, freely given when justice requires (15(a)(2)).
  - New York: once without leave within the CPLR 3025(a) windows; otherwise by leave or stipulation (3025(b)). The Commercial Division's pre-motion letter requirement applies to a motion for leave.
  - California: once without leave before the answer, demurrer or motion to strike is filed, or after a demurrer up to the date for opposing it (CCP 472); otherwise by leave (CCP 473(a)(1)).
  - Washington: once as of course before a responsive pleading is served; otherwise by leave or written consent (CR 15(a)).
  - Delaware Superior Court and Court of Chancery: once before a responsive pleading is served; otherwise by leave or written consent. In the Court of Chancery, a plaintiff facing a Rule 12(b)(6) or 23.1 motion must amend or seek leave before its response is due, or a dismissal is with prejudice as to that plaintiff (Rule 15(a)(5)).
- **What shows the changes.**
  - Federal: by district. S.D.N.Y. and E.D.N.Y.: a clean copy and a redline with the motion (Local Civil Rule 15.1). N.D. Cal.: the entire proposed pleading and a redlined or highlighted comparison, and a redline even when amending as of right (Civil L.R. 15-1). W.D. Wash.: the proposed pleading marking deletions by brackets or strike-through and additions by underlining or highlighting, also when amending by consent (LCR 15). D. Del.: the signed proposed pleading and a form showing the differences, filed separately on consent (LR 15.1).
  - New York: the proposed pleading "clearly showing the changes or additions" (CPLR 3025(b)), in practice a blackline.
  - California: the proposed pleading; a statement of each deletion and addition by page, paragraph and line; and a separate declaration stating the effect of the amendment, why it is necessary and proper, when the facts were discovered and why the request was not made earlier (CRC 3.1324(a), (b)). No alterations on the face of a pleading (3.1324(d)).
  - Washington: the proposed pleading marked "proposed" and unsigned (CR 15(a)); no colour or highlighting in any filed paper (GR 14(a)), so a comparison uses underlining and strike-through only. After leave, file and serve the signed version.
  - Delaware Superior Court: the amended pleading must indicate plainly how it differs (Rule 15(aa)). Court of Chancery: file the amended pleading even after leave, with a document indicating plainly how it differs (Rule 15(a)(3)), and verify it (Rule 3(c)).
  - Always end the amended pleading, or the motion, with the one-paragraph statement of changes (`formulae.md` section 18) pointing to the comparison. Most courts require one; where none is required it costs nothing and saves the other side a comparison of its own.
- **Verification.** Where the original was verified (New York, California) or the court requires it (Chancery), verify the amended pleading.
- **Supplemental pleadings.** Events after the pleading was filed go in a supplemental pleading by motion (FRCP 15(d); CPLR 3025(b)), not an amendment.
- **The motion papers.** This variant drafts the proposed amended pleading, the comparison statement or schedule, and the formal parts of the notice of motion. The memorandum of law belongs to `litigation-submissions`, the supporting declaration to `litigation-evidence`, the proposed order to `litigation-writing`.

## Skeleton: Hong Kong amended statement of claim (without leave)

Insertions in `++ ++`, deletions in `~~ ~~`; text in braces is a drafting note. Put the markers after a paragraph number ("5A. ++text++") so the numbering stays readable, and leave a heading that does not change ("STATEMENT OF TRUTH") unmarked.

```
Amended and underlined in red the [date 1], pursuant to RHC, Order 20, Rule 3

                                                            [case number]
{court heading lines}
ACTION NO. [case number]

BETWEEN

[name 1]                                                          Plaintiff

and

[name 2]                                                          Defendant

{rule}
++AMENDED++ STATEMENT OF CLAIM
{rule}
(Writ of Summons issued on the [date 2])

5. The Agreement contained, among others, the following express terms:-
   (a) {term} (see Clause [number]);
   (b) {term} (see Clause [number])~~.~~++; and++
   (c) ++{new term} (see Clause [number]).++

5A. ++It was an implied term of the Agreement that {term}. The term is to
    be implied because:-++
    (a) ++{fact};++
    (b) ++{fact}.++

11. By reason of the ~~Defendant's breach~~ ++matters aforesaid++, the
    Plaintiff has suffered loss and damage.

AND THE PLAINTIFF CLAIMS AGAINST THE DEFENDANT FOR:-

(1) The sum of ~~[sum 1]~~ ++[sum 2]++.
(3) Interest on ~~[sum 1]~~ ++[sum 2]++ at the rate of [rate] per annum ...
    {every prayer item that carries a changed figure}

~~Dated the [date 3].~~ {or keep it, by the firm's practice}
++Dated the [date 4].++

STATEMENT OF TRUTH

~~The Plaintiff believes that the facts stated in this Statement of Claim are
true. ...~~

++The Plaintiff believes that the facts stated in this Amended Statement of
Claim are true. I am duly authorised by the Plaintiff to sign this statement
of truth.++
++Signed:++
++Name: [name 3]++
++Position: {office held}++
++Date: [date 5]++

{backsheet}
AMENDED STATEMENT OF CLAIM
Dated the [date 3]
Filed the [date 6]
Re-filed the [date 7]
Served the [date 8]
```

With leave, the legend reads "Amended pursuant to the Order of [judge] dated the [date]", left blank in the draft annexed to the summons. A re-amendment adds its own legend above the first, uses green, and retitles "RE-AMENDED".

## Skeleton: Hong Kong summons for leave to amend

```
                                                            [case number]
{court heading lines}
ACTION NO. [case number]

BETWEEN

[name 1]                                                          Plaintiff

and

[name 2]                                                          Defendant

                                SUMMONS

{margin: the rules relied on}

LET ALL PARTIES concerned attend before [judge] in Chambers at [court] on
[date 1] at [time] on the hearing of an application by the Plaintiff for an
Order that:-

1. The Plaintiff do have leave to amend the Statement of Claim in the form of
   the draft Amended Statement of Claim annexed hereto, the amendments being
   shown in red;

2. The Plaintiff do file and serve the Amended Statement of Claim within
   [number] days of the date of the Order;

3. The Defendant do have leave to file and serve an Amended Defence, if so
   advised, within [number] days after service of the Amended Statement of
   Claim;

4. The Plaintiff do have leave to file and serve an Amended Reply, if so
   advised, within [number] days after service of the Amended Defence; and

5. The costs of and occasioned by the amendment be borne by the Plaintiff.

Dated the [date 2].
                                                    Registrar

This Summons was taken out by [solicitors-firm], Solicitors for the
Plaintiff, of [address].

Estimated length of hearing: [number] minutes.

To: [solicitors-firm], Solicitors for the Defendant, [address].

{annex: the draft Amended Statement of Claim in red, legend "Amended pursuant
to the Order of [judge] dated the [date 3]" with the date left blank}
```

## Skeleton: US proposed amended complaint and comparison (federal)

```
{caption as on the complaint}

             [PROPOSED] FIRST AMENDED COMPLAINT
                     JURY TRIAL DEMANDED

{the complete amended complaint, from the complaint skeleton in claim.md,
with nothing incorporated by reference from the original}

                     STATEMENT OF CHANGES

Exhibit B is a comparison of the proposed First Amended Complaint against the
Complaint filed on [date 1], showing additions underlined and deletions
struck through.

{notice of motion, where leave is needed}

PLEASE TAKE NOTICE that, upon the accompanying memorandum of law, the
declaration of [name] dated [date 2] and the exhibits to it, and all prior
pleadings and proceedings in this action, Plaintiff [name 1] will move this
Court, before [judge], at [court], on [date 3] at [time], for an order under
[rule] granting Plaintiff leave to file the proposed First Amended Complaint
annexed as Exhibit A, and for such other and further relief as the Court
deems just and proper.
```

California: add the CRC 3.1324(a) schedule of deletions and additions by page, paragraph and line (`formulae.md` section 18) and the 3.1324(b) declaration. Washington: "proposed" and unsigned, no colour. Court of Chancery: the comparison document and a fresh verification.

## Formulae

`formulae.md` sections 12 and 13 (Hong Kong) and 18 (US), with the variant formulae for the pleading amended.

## Checklist

Run the checker on the complete amended pleading, or on the summons together with its annexed draft: a summons on its own has no legend, title or statement of truth to find.

The checker tests:
- Hong Kong: an amendment legend ("Amended ... pursuant to ...", or "Replaced by Amendment"); a title marked AMENDED or RE-AMENDED; a statement of truth naming the amended pleading; a "Served" line on the backsheet.
- US: a statement that a comparison or redline shows the changes; a numbered or "proposed" amended title (soft); no Hong Kong colour legend (soft).
- numbered paragraphs, and the shared and base rules for every pleading.

Check by eye:
- whether leave is needed, and on what basis; whether an affirmation must support the application.
- the colour and title match the round; earlier legends kept.
- no existing paragraph renumbered; inserted paragraphs lettered; struck text legible.
- every changed figure chased into the prayer and every other place it appears; cross-references live.
- the statement of truth, title and backsheet updated together.
- with leave, only the authorised amendments; the summons names each document and its colour; costs as the user decides.
- US: a complete document with no incorporation of the original; the comparison, schedule, declaration or "proposed" marking the profile requires; verification where needed.
