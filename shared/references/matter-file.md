# The matter file

A single application often needs several documents: a summons, a supporting affirmation, a skeleton, a draft order. They must agree on every name, date, defined term and reference. The matter file holds those facts once, so every document is drafted from the same values.

## Where it lives

`matter.json`, in the user's own folder for the case, next to the drafts. It holds client information, so it stays on the user's machine. Never put it in a public repository, and never paste its contents into a public place. A blank template is at `assets/matter.template.json`.

## How the skills use it

1. **Look for it first.** At the start of a task, ask whether there is a matter file, or look for `matter.json` in the working folder.
2. **Read before asking.** Take every value the file holds. Ask only for what the document needs and the file lacks.
3. **Offer to record new facts.** When the user gives you a new fact (a hearing date, a new affirmation, an authority), offer to add it to the file. Write to the file only with the user's agreement.
4. **Never overwrite silently.** If the user gives a value that differs from the file, ask which is right before using it.
5. **Without a file.** If there is none and the user does not want one, work from the conversation. Offer to create one when a second document for the same matter comes up.

## Shape

The keys are the field ids in `assets/fields.json`. Lists hold one object per item. A value the user has not given is left out; do not store guesses or placeholders in the file.

```json
{
  "jurisdiction": "hk",
  "court": "Court of First Instance",
  "case_number": "HCA [number]/[year]",
  "parties": [
    {"role": "Plaintiff", "name": "[name]", "abbreviation": "P", "pronoun": "it", "entity": "company"},
    {"role": "Defendant", "name": "[name]", "abbreviation": "D", "pronoun": "he", "entity": "individual"}
  ],
  "client_party": "Plaintiff",
  "authorities": [
    {"name": "[case name]", "citation": "[citation]", "pinpoint": "[§]", "tag": "P#1", "verified": true, "verified_source": "supplied by the user"}
  ]
}
```

The values in brackets above only show the shape. A real matter file holds the user's actual values.
