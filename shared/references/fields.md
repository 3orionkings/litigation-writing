# Fields and placeholders

Every litigation document is built from case-specific information: who the parties are, which court, which application, what happened and when, how much, and where the evidence sits in the bundle. In these skills each piece of that information is a **field**. A field is either supplied by the user or left as a visible placeholder. It is never guessed, and never filled from memory or from an example.

## Why this matters

A wrong name, date, sum or paragraph number in a filed document is worse than a gap. A gap is obvious and gets filled before filing. A plausible invention survives proofreading and reaches the court. So the rule is simple: if the user has not given it, the draft shows that it is missing.

## The order of work

1. **Find out what the document needs.** Run the fields helper for the skill, variant and jurisdiction (see "The fields helper" below). It lists the required fields (R), the optional ones (O), and those normally filled in later (L), and marks which are already in the matter file.
2. **Ask once, grouped.** Ask the user for the missing required fields in one message, grouped as the helper groups them (matter and court, parties, hearing, procedure, evidence, authorities, facts). Ask nothing the matter file or the conversation already answers.
3. **Draft with what you have.** If the user says to go ahead without some fields, draft anyway. Each missing value becomes a placeholder from the vocabulary below.
4. **Close with the list.** Whenever the draft contains a placeholder, end it with a "Fields to complete" table (format below).

Later fields (L) are placeholders by default even when you could guess them, because they are fixed only at filing or at the hearing: hearing time, bundle pages, filing and service dates, the jurat, the signature date.

## The placeholder vocabulary

Plain square brackets, with a label for the kind of information. Use only these labels, so the user and the checker can find every gap.

| Kind | Labels |
|---|---|
| Party roles | `[Plaintiff]` `[Defendant]` `[Claimant]` `[Respondent]` `[Petitioner]` `[Appellant]` `[Applicant]` `[Intervener]` `[Third Party]` `[Judgment Creditor]` `[Judgment Debtor]` `[Garnishee]` `[Party]`, with an ordinal where needed: `[1st Defendant]`, `[2nd Plaintiff]` |
| People | `[name]` `[the Child]` `[deponent]` `[witness]` `[expert]` `[judge]` |
| Signatories | `[counsel-name]` `[solicitors-firm]` `[bar number]` |
| Dates and numbers | `[date]` `[time]` `[age]` `[sum]` `[rate]` `[period]` `[number]` `[percentage]` |
| Places and identifiers | `[address]` `[language]` `[company number]` `[account number]` `[property description]` |
| Matter | `[case number]` `[court]` `[statutory provision]` `[rule]` `[document title]` |
| Evidence | `[Bundle ref]` `[exhibit]` |
| Authorities | `[authority needed: <the proposition it must support>]` `[quotation needed: <authority and paragraph>]` |

**Suggest the right party label.** Pick the label that fits the court and the document: `[Plaintiff]` and `[Defendant]` in a Hong Kong action, `[Petitioner]` and `[Respondent]` in matrimonial proceedings, `[Appellant]` and `[Respondent]` on appeal, `[Claimant]` where the court uses it, `[Judgment Creditor]` and `[Judgment Debtor]` after judgment. If you are unsure, use `[Party]` and say which label you expect.

**Children.** Refer to a child as `[the Child]` (or `[the Child 1]`, `[the Child 2]`). The user decides how the child is named or described.

**Number repeats.** When the same kind of placeholder stands for different values in one document, number them, and keep the same number for the same value throughout: `[date 1]` is the summons date wherever it appears and `[date 2]` is the hearing date. The user can then complete each one with a single find-and-replace. A placeholder that occurs once needs no number.

**Never mix a placeholder with a guess.** Write `[sum]`, not `HK$[sum]` with a guessed currency, unless the user gave the currency. Write `[date]`, not `[date] 2025`.

**Not placeholders.** Real references stay as they are: bundle tags such as `[A12/§3]`, authority tags such as `[P#2]` or `[Authority#4]`, and labels for the other side's paragraphs such as `[D§12]` (see `authorities.md`). The checker tells these apart from placeholders because none of them uses a label from the table.

**Never invent.** Do not fill a field from an example in these skills, from another matter, or from general knowledge. That covers names, numbers, dates, sums, judges, case numbers, citations, pinpoints, exhibit codes and bundle pages. Which statute, rule or interest provision applies is a matter of law for the user; write `[statutory provision]` or `[rule]` unless they have told you.

## Materials, not only fields

Fields are the facts a document needs; materials are where those facts and the law come from. Each skill asks, once and with the fields, for the materials the user has: client instructions, a dramatis personae, a chronology, the documents and exhibits, the pleadings and orders, the other side's papers, and copies of the authorities. A draft built from the materials is more accurate than one built from a summary of them. The user may not have all of them; ask, use what is shared, and do not hold the draft back for what is not.

## The "Fields to complete" table

Put it after the document, under its own heading, so it can be deleted in one go before filing:

```
FIELDS TO COMPLETE

| Placeholder | Where | What belongs here |
|---|---|---|
| [date 1] | paras 1, 4, 12 | Date of the summons |
| [Bundle ref] | paras 6 to 19 | Bundle page and paragraph for each fact |
| [authority needed: strike-out threshold] | para 8 | An authority for the "plain and obvious" test |
```

List every placeholder that remains, with the paragraphs it appears in. If nothing is missing, leave the table out.

## The fields helper

The checker script doubles as a fields helper:

```
python3 scripts/litcheck.py fields --skill <skill-name> --variant <variant> --jurisdiction <code> [--matter matter.json]
```

It reads `assets/fields.json` and prints the fields that document needs, grouped, each marked R, O or L, and, if a matter file is given, whether a value is already there. Run it before drafting. If you cannot run scripts, read `assets/fields.json` yourself: each field lists the skills and variants for which it is required.

## Fields by group

The full list, with the status of each field for each skill and variant, is in `assets/fields.json`. In outline:

- **Matter and court.** Jurisdiction, court and level, case number, the decision under appeal, related proceedings.
- **Parties.** Each party's name, role, abbreviation, pronoun and type (individual or company), which party the document is for, and the particulars a claim pleading needs (incorporation, registered office, residence, capacity).
- **Tribunal and hearing.** The judge or master, the hearing date and time, the type of hearing, the time reserved, the direction under which the paper is filed.
- **The document.** Its type and variant, title, ordinal, purpose line, signatories (`[counsel-name]`, `[solicitors-firm]`), signing date.
- **Procedure.** The applications before the court, the orders sought, prior orders, the procedural history, the pleadings in play, the paper being answered, grounds of appeal, issues for trial, costs position.
- **Evidence and bundles.** The bundle scheme and its legend, the affirmations or declarations filed, the exhibits, witnesses, experts and transcripts.
- **Authorities.** Each authority the user supplies, with citation, pinpoint, bundle tag and whether it is verified; the tag scheme; the statutes and rules relied on.
- **Facts and money.** Defined terms, key dates, sums and interest, agreements and their clauses, property and assets.
- **Verification and formalities.** Who verifies a pleading and in what capacity, the deponent's details, an interpreter where the deponent does not read English, the jurat, the backsheet dates, the amendment history.

Identity-card numbers and medical details are deliberately not fields. Do not prompt for them. If the user supplies them, use only what the document needs.
