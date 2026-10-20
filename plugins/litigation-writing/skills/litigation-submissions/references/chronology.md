# Chronology (agreed or party)

## What it is for

A dated record of events for the court: annexed to a skeleton, an opening or an appeal, or filed as an agreed document. It has no speaker. It does its work by selection and order: the court sees, in one table, what happened and when, and finds each document from its reference. Argument does not belong in it, but a party's chronology may show a pattern through labels and plain facts ("No reply was received.").

Settle the type first, because it sets the temperature:

| Type | Use | Temperature |
|---|---|---|
| **Agreed** | Filed jointly for a hearing or trial | Neutral. Uncontested facts only; disputed matters are left out, not marked disputed |
| **Party, trial or hearing appendix** | Annexed to the party's opening or skeleton | Glosses only, inside the event text ("notwithstanding that the notice was served late") |
| **Procedural** | For an interlocutory hearing about delay or default | Labels and counts ("3rd Time Summons:"); the other side's defaults stated flatly |
| **Family party** | Annexed to a party's submissions in family proceedings | Labels and short refrains allowed ("No reply was received."), with moderation |

None of them has a comment column, adjectives about the other side, or a citation of authority. A rule may be named inline where an event depends on it ("pursuant to [rule]").

## Structure: Hong Kong

**Front matter.**

- Agreed: the action number, the title `AGREED CHRONOLOGY`, the hearing line, and the party legend (`[Plaintiff] = P; [Defendant] = D`). No bundle legend if there are no references; no signature.
- Party appendix: a cover block above the table with the hearing line, the action number, a short title, `APPENDIX [number]: THE [Defendant]'S CHRONOLOGY`, the bundle legend, the party line, then the signature and distribution.
- Procedural and family: the action number, the hearing line, the title, the legend; family chronologies define the parties and `[the Child 1]` in the first rows.

**Columns.** `#` (numbered automatically, never by hand) / `Date` / `Event` / `Ref` for a party appendix; `#` / `Date` / `Event` for an agreed chronology without references.

**Dates.** One format throughout, in the court's usual style ("3 May 2027", or a numeric form the user prefers). A month-only event is written as the month and year; a range uses a hyphen between the dates. A time of day goes inside the event ("at 4:15 pm"), and same-day events get separate rows in time order. Sort every row by date; if the source put a row out of order or wrote a date in another format, normalise it and tell the user, above the draft, which rows moved.

**Events.** One sentence, past tense, subject first: "[Defendant] signed the Agreement." Documents appear as noun phrases ("[Plaintiff]'s solicitors' letter to [Defendant]'s solicitors"). A long letter's operative content goes in (i), (ii), (iii) inside the cell. Orders inside a cell are numbered and end with the costs order. Reuse the pleading's defined terms unchanged; a new term is defined in brackets in the row where it first appears. Hold the past tense to the last row.

**Labels and counts.** For repeated applications by one side, an ordinal label at the head of the cell ("2nd Time Summons:"). For hearings in a series, a label ("1st case management hearing"). For a chronology that supports several grounds, a topical prefix ("Re limitation:"), so that each ground can be traced down the table.

**References.** In a party appendix every row has one, in the user's bundle scheme, several stacked in the cell where needed. Never invent a page; write `[Bundle ref]` until the bundle is paginated.

## Differences in the US profiles

A stand-alone chronology is less common in US courts. The same content usually appears as the statement of facts in a brief (with record citations), as a joint statement of undisputed facts in a pretrial order, or as a demonstrative or exhibit. When one is filed, cite the record in the court's form (`ECF No. [number] at [number]`; `D.I. [number]`; `NYSCEF Doc. No. [number]`; `Dkt. # [number] at p. [number]`), write dates as "May 3, 2027", and keep the agreed and party forms apart as above. A California separate statement is not a chronology: it is a numbered list of material facts with evidence (see `skeleton.md`).

## Skeleton (party appendix, Hong Kong)

```
For trial before [judge] on [date 1] at [time]
[case number]
[Plaintiff] v [Defendant]

APPENDIX 1: THE [Defendant]'S CHRONOLOGY

Legend: [A12/§3] = Bundle A, page 12, paragraph 3
Abbreviations: the [Plaintiff] ("P"); the [Defendant] ("D").

| # | Date | Event | Ref |
|---|---|---|---|
| 1 | [date 2] | P and D signed a written loan agreement ("the Agreement"). | [Bundle ref] |
| 2 | [date 3] | P transferred [sum] to D under the Agreement. | [Bundle ref] |
| 3 | [date 4] | P's solicitors wrote to D demanding repayment by [date 5]. | [Bundle ref] |
| 4 | [date 5] | No payment was made. | [Bundle ref] |
| 5 | [date 6] | P issued the writ. | [Bundle ref] |

[counsel-name]
Counsel for the [Defendant]
[date 7]
```

## Formulae

Section 11 of `formulae.md`.

## Checklist

The checker tests: a date column or dated rows; no comment or argument column (soft); no argument formulae (soft, from the chronology family rules). Paragraph numbering is not required; rows are numbered by the table.

Check by eye:

- Rows are in date order, and every moved row was reported to the user.
- One date format throughout; past tense throughout.
- The temperature matches the type: nothing contested in an agreed chronology.
- Every row in a party appendix has a reference.
- Defined terms match the pleadings.
