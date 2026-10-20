# The checker's rule files

`scripts/litcheck.py` (one copy in every skill, edited only in `shared/scripts/`) reads four kinds of rule file. All rules use the same shape, so a skill author only needs to learn it once.

## A rule

```json
{"id": "prayer", "label": "a prayer for relief", "any": ["^AND THE .{1,60} CLAIMS", "PRAYER FOR RELIEF", "^WHEREFORE"],
 "severity": "hard", "where": "end", "jurisdictions": ["hk"]}
```

- `id`: short, unique within the file.
- `label`: what the report says is missing or present, in plain words.
- `any`: Python regular expressions. A `require` rule passes when at least one matches. A `forbid` rule fails when any matches. Matching is case-insensitive and multiline (`^` and `$` match at line breaks) unless the rule sets `"case": true`.
- `severity`: `hard` (the draft fails; exit status 1) or `soft` (reported for a second look). Default `hard`.
- `where`: `anywhere` (default), `start` (first quarter of the document), `end` (last third, before "FIELDS TO COMPLETE"), or `body` (everything except the caption block, the signature block and the "FIELDS TO COMPLETE" table).
- `jurisdictions`: optional list of profile codes, or the group names `hk` and `us`. The rule applies only to those. Omit it to apply everywhere.
- `skip_quotes`: optional `true`. Ignore matches inside quotation marks and indented quotation blocks (useful for first-person checks in submissions that quote evidence).

## `style.json`, one per skill

```json
{
  "name": "litigation-pleadings",
  "family": "pleadings",
  "base": {
    "numbered_paragraphs": true,
    "words": {"min": 150, "max": 40000},
    "require": [],
    "forbid": []
  },
  "variants": {
    "claim": {
      "description": "statement of claim or complaint",
      "require": [ {"id": "prayer", "label": "a prayer for relief", "any": ["..."], "where": "end"} ],
      "forbid": []
    },
    "defence": {"description": "defence or answer", "words": {"min": 100, "max": 40000}}
  }
}
```

- `family` is one of `pleadings`, `evidence`, `submissions`, `advice`, `correspondence`, `procedural`, `chronology`. It selects the perspective rules in `assets/perspective.json`. A variant may set its own `family` (a chronology inside the submissions skill uses `chronology`; a speaking note may set `"first_person": "allow"`).
- `numbered_paragraphs`: when true, at least 60 per cent of the body paragraphs must begin with a paragraph number (`1.`, `12.`, `3.4`) or a sub-paragraph marker (`(a)`, `(iii)`).
- `words`: minimum and maximum words in the body. Jurisdiction word limits in `assets/jurisdictions.json` apply on top.
- `require` and `forbid`: lists of rules. A variant's lists are added to the base lists. To switch a base rule off for one variant, list its `id` in the variant's `"drop": ["id"]`.
- Any other base key a variant sets replaces the base value; `null` switches the check off.

## Shared rule files (in `shared/assets/`, copied to every skill)

- `perspective.json`: for each family, `first_person` (`forbid`, `allow`, or `require`), `first_person_plural` (`forbid`, `allow`, `soft`), and `require` and `forbid` rule lists (for example, evidence forbids "It is submitted" and case citations).
- `register.json`: the dash rule and the tells every family keeps out.
- `jurisdictions.json`: for each profile, its `group` (`hk` or `us`), rule lists for each family and for each `skill:variant`, word limits, citation patterns, and `overrides`: structural settings that replace a variant's own, keyed by family, `skill:*` or `skill:variant`, at group or profile level (US briefs, for example, set `numbered_paragraphs` to false).
- `fields.json` and `placeholders.json`: the field list with each field's status by skill and variant, and the closed placeholder vocabulary.

## Checks that are built in

Beyond the rule files, the checker always runs these:

- **Placeholders.** Lists every placeholder from `placeholders.json` left in the draft, with paragraph numbers. Flags bracketed gaps outside the vocabulary (`[ ]`, `[XX]`, `[TBC]`, `[insert …]`, runs of underscores in the body) as soft findings. If any placeholder remains and there is no "FIELDS TO COMPLETE" table, that is a hard failure.
- **Citations.** Lists every case citation the patterns recognise. With `--matter`, any citation not found among the matter file's authorities is a hard failure. A citation with no pinpoint in the same sentence is a soft finding. A citation in another jurisdiction's style is a soft finding.
- **Dashes and tells.** From `register.json`.
- **Summary close.** A closing paragraph that opens "In conclusion", "In summary", "To summarise" or similar is a hard failure.
