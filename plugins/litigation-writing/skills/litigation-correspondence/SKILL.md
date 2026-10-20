---
name: litigation-correspondence
description: "'Drafts solicitors'' letters to the other side in a dispute, in the firm''s voice (\"We\", \"our client\"). Covers a Hong Kong request for further and better particulars under O.18 r.12, a New York demand for a bill of particulars, a meet-and-confer or deficiency letter in other US courts, a letter before action or demand, an open, without prejudice or without prejudice save as to costs proposal, a rule-based offer (Hong Kong sanctioned offer under O.22; US offer of judgment under FRCP 68 or the state equivalent), and a covering letter serving a pleading, amendment or bundle. Use for a \"letter\", \"FNBP\", \"request for particulars\", \"bill of particulars\", \"deficiency letter\", \"meet and confer\", \"demand letter\", \"letter before action\", \"WP letter\", \"Calderbank\", \"sanctioned offer\", \"Rule 68 offer\", \"998 offer\" or \"serve the amended pleading\". Not for: counsel''s advice (use litigation-advice), the pleading or an answer to a request (use litigation-pleadings), submissions (use litigation-submissions).'"
---

# Litigation Correspondence

## What this skill is for

Letters from the firm to the other side's lawyers (or to an unrepresented party) in a dispute: requests, demands, proposals, formal offers and covering letters. Each letter does one procedural job, and many are later read by the judge: a request for particulars is exhibited on the application that follows it, an open letter goes into the bundle on costs or conduct, a without prejudice save as to costs letter is produced once the merits are decided. So every letter is drafted for two readers, the other side now and the court later.

The request-for-particulars variant follows the form of a filed precedent in the study behind this plugin. The study held no other letter, so the demand, proposal, offer and covering variants are built from general practice and the rules. They are deliberately conservative: they state the client's position plainly and briefly, add nothing that could be read as an admission, contain no term the client has not authorised, and mark every rule for the user to check.

## Who is speaking

- **The firm, for its client.** First person plural: "We refer to …", "We are instructed to …", "our client". The firm signs (`[solicitors-firm]`), not an individual, in Hong Kong. A US letter is signed by an attorney for the firm (`[counsel-name]`, then `[solicitors-firm]`) and may use "we" or, sparingly, "I"; the checker reports "I" as a soft finding so it gets a second look.
- **To the other side's lawyers.** Write to the other side's solicitors or attorneys, never directly to a party they represent. If the other side has no lawyer, write to the party, in plain words, and suggest they take legal advice; do not advise them.
- **Firm, courteous, brief.** The letter says what is requested, demanded or offered, by when, and what will follow. It does not argue the case beyond what the letter needs, describe the other side or its lawyers with adjectives, or use "It is submitted".
- **For the judge as well.** Nothing goes into an open letter that the firm would not want the judge to read. Concessions and offers the client does not want the court to see go in a separate letter marked without prejudice.
- **On instructions only.** Every term, sum, deadline and threat of proceedings comes from the client's instructions. A letter never commits the client to a step (an application, a claim, a refusal to extend time) it has not authorised.

## Before drafting

1. **The matter file.** Look for `matter.json` and take what it holds (`references/matter-file.md`): case number, parties, the firm's and the other side's references, the other side's firm and address.
2. **The jurisdiction.** Ask if the user has not said, and read only `references/jurisdictions/<code>.md`. The form of a request for particulars and of an offer depends on it more than on anything else.
3. **The fields.** Run `python3 scripts/litcheck.py fields --skill litigation-correspondence --variant <v> --jurisdiction <code> [--matter matter.json]`, or read `assets/fields.json`.
4. **Ask once, grouped.** Our reference and theirs; the addressee firm, address and the person to whom it is marked; the mode of delivery; the parties and case number for the "Re:" line; the document the letter concerns; the status of the letter (open, without prejudice, without prejudice save as to costs); the deadline; for a demand, proposal or offer, the exact terms and sums the client has authorised. If the user says to go ahead, draft with placeholders from `references/fields.md`. The addressee firm and the signing firm are both `[solicitors-firm]`; number them (`[solicitors-firm 1]` for the addressee, `[solicitors-firm 2]` for the firm signing) while both are unfilled.
5. **Authorities and rules.** Letters rarely cite cases. Name the rule a letter is a step under (O.18 r.12, O.22, CPLR 3042, FRCP 68), and only as the user confirms it applies; otherwise write `[rule]`. If the user wants a case cited, use only one they supplied or verified (`references/authorities.md`) and mark any gap `[authority needed: …]`.
6. **The materials.** In the same message, ask for the document the letter concerns (the pleading to be particularised, the order, the earlier correspondence) and the client's written instructions on any term, sum or deadline. Quote the other side's words from the document itself, never from memory or a summary.

## Variants

| Variant id | What it is | When to use it | Read |
|---|---|---|---|
| `particulars-request` | Hong Kong request for further and better particulars under O.18 r.12; New York demand for a bill of particulars; in other US courts, a meet-and-confer or deficiency letter instead | The other side's pleading does not say enough to answer it, or before applying for an order for particulars | `references/particulars-request.md` |
| `demand` | Letter before action or demand | Before proceedings, to demand payment or performance and say what follows | `references/demand.md` |
| `proposal` | Open, without prejudice, or without prejudice save as to costs proposal | To negotiate, or to put a settlement position on record for costs | `references/proposal.md` |
| `offer` | Rule-based offer: Hong Kong sanctioned offer under O.22; US offer of judgment under FRCP 68 or the state equivalent | When the client wants the costs and interest consequences the rule attaches | `references/offer.md` |
| `covering` | Covering letter serving a pleading, amendment or bundle | Whenever a document is served or sent | `references/covering.md` |

The formulae for all five are in `references/formulae.md`.

## The moves

1. **Settle the status first.** Decide whether the letter is open, without prejudice, without prejudice save as to costs, or a formal offer under a rule, and mark it at the top. The status decides what may go in it and who will read it. A letter that mixes an open complaint with an offer becomes two letters.
2. **The header in a fixed order.** References (`Our ref` / `Your ref`), date, mode of delivery, addressee block, "Attn:" line, salutation, then the "Re:" line with the case number and the parties, the client marked ("our client"), and the subject.
3. **One opening line, one purpose line.** "We refer to …" what the letter answers or concerns. Then why the letter is written, naming the rule if it is a step under one.
4. **One item at a time.** Each request, demand or term in its own numbered paragraph or under its own heading. For particulars, a heading per paragraph of the pleading ("Under paragraph [number]"), the pleading's own words quoted, then "Please provide …" or "Please state …" and a lettered list, so the answer can follow item by item.
5. **Ask for what the rule allows.** Particulars of the case pleaded, not the evidence that will prove it, not documents (that is discovery), not the other side's legal argument.
6. **A clear deadline.** A date (`[date]`, with a time if it matters) or a period with the date it ends, and what will follow if it passes, stated once and only as instructed.
7. **Protect the client's position.** For particulars: the request is without prejudice to the client's own pleading. For proposals: no admission of liability. For every letter that could later matter: a reservation of rights.
8. **Close in the firm's name.** The sign-off that matches the salutation, the firm, and any copy list.
9. **Read it as the judge.** Before finishing an open letter, read it as the judge will on the application or on costs. Take out anything that sounds like a threat the client will not carry out, an exaggeration, or a remark about the other side.

## Language

- **Person.** "We", "our client", "your client" (or "your clients"). Pick one capitalisation for "our client" and keep it throughout, following the firm's house style if the user gives one.
- **Requests.** "Please provide", "Please state", "Please identify", "Please confirm". Every contested fact the other side pleads is "alleged" or "allegedly", so the request admits nothing.
- **Temperature.** Low. Firmness comes from the deadline and the consequence, not from adjectives. No "regrettably", "astonishingly", "wholly without merit", no sarcasm, no rhetorical questions.
- **Sentences.** Short, about 15 to 20 words. One point per paragraph.
- **Formulae.** The status headings, "We refer to", "including but not limited to", "without prejudice to", the reservation of rights and the sign-offs are fixed; see `references/formulae.md`.
- **Salutation and sign-off.** Hong Kong: "Dear Sirs," with "Yours faithfully," to a firm (or the firm's gender-neutral house form); "Dear [name]," with "Yours sincerely," to a named person. US: "Dear Counsel:" or "Dear [name]:" with "Very truly yours," or "Sincerely,".
- **Numbering.** Requests and terms are numbered or lettered. Short narrative letters need not number every paragraph.

## Workflow

1. Run the fields helper, read the matter file and ask once for what is missing, including the client's authorised terms.
2. Settle the status and read the variant's reference file and `references/formulae.md`.
3. For a particulars request, go through the other side's pleading paragraph by paragraph and list what is missing before drafting; for a demand, proposal or offer, list the terms from the instructions.
4. Draft the header, the "Re:" line, the opening and purpose lines, the body, the deadline, the protective lines and the sign-off.
5. Check every rule named against the profile and the user's instructions; mark any not confirmed `[rule]`.
6. Do the register pass below.
7. Run `python3 scripts/litcheck.py check draft.md --skill litigation-correspondence --variant <v> --jurisdiction <code> [--matter matter.json]`. Fix every hard failure and look again at each soft one.
8. Return the letter, followed by the "FIELDS TO COMPLETE" table if any placeholder remains, and a one-line note of any rule the user must confirm.

## The register pass

Apply "The register pass" in `references/voice.md` to the running prose as the last step before the checker. For a letter that means: cut the tells it lists; take out adjectives about the other side, argument the letter does not need, and any "It is submitted"; shorten long sentences; replace any dash with a comma, brackets, a colon or a new sentence.

Leave these exactly as they are:

- the status heading ("WITHOUT PREJUDICE", "WITHOUT PREJUDICE SAVE AS TO COSTS", "CONFIDENTIAL SETTLEMENT COMMUNICATION") and the rule named in it;
- every formula in `references/formulae.md`, including "We refer to", "including but not limited to", the without-prejudice-to-our-pleading line, the reservation of rights and the sign-off;
- the other side's words quoted from its pleading or letter, with any error marked "(sic)";
- the "Under paragraph [number]" headings and the numbered and lettered requests;
- every reference, date, sum, deadline, rule number, defined term and placeholder.

## What makes a draft fail

- No status heading on a proposal or offer, or the wrong one: an offer the client wants to rely on for costs marked plain "WITHOUT PREJUDICE", or a concession in an open letter.
- A particulars request that paraphrases the pleading instead of quoting it, asks for evidence or documents, or is not organised by paragraph so the answer cannot follow it.
- No deadline, or a deadline that is a guess rather than `[date]`.
- A term, sum, interest rate or date the client did not give, or a threat of a step the client has not authorised.
- A threat of a criminal complaint or a report to a regulator to gain an advantage in the civil dispute. Professional conduct rules in many places forbid it.
- Argument, adjectives about the other side, "It is submitted", or a case cited that the user did not supply.
- A sanctioned offer or offer of judgment missing the content the rule requires, made by a party the rule does not allow, or mentioned to the court before the rule permits.
- A covering letter that does not identify exactly what is served, under which rule or order, or records the wrong deadline.
- No sign-off, a sign-off that does not match the salutation, or an individual's signature where the firm signs.
- Dash punctuation.

## Files

- `references/particulars-request.md`, `references/demand.md`, `references/proposal.md`, `references/offer.md`, `references/covering.md`: structure, skeleton and checklist for each variant.
- `references/formulae.md`: the letter formulae, verbatim, by jurisdiction.
- `references/voice.md`, `references/fields.md`, `references/authorities.md`, `references/jurisdictions.md`, `references/jurisdictions/<code>.md`, `references/matter-file.md`: the shared rules every skill in this plugin follows.
- `style.json`: the rules the checker applies to this skill and its variants.
- `scripts/litcheck.py`: the fields helper (`fields`) and the checker (`check`).
- `assets/`: the field list, placeholder vocabulary, perspective and register rules, jurisdiction rules and the matter-file template.
- `agents/openai.yaml`: display metadata for other assistants.
