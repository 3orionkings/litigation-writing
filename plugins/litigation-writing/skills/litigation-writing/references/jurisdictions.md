# Jurisdictions

The drafting moves in these skills are the same everywhere. What changes between courts is vocabulary, the grammar of an answer, how evidence is sworn, how an amendment is shown, the formal rules for papers, and the citation style. Those differences live in a profile, one file per jurisdiction in `jurisdictions/`, plus the machine-readable rules in `assets/jurisdictions.json` that the checker uses.

## Choosing the profile

`jurisdiction` is a required field with no default. If the user has not said, ask which court the document is for. Then read only the matching profile.

| Code | Court system | Profile |
|---|---|---|
| `hk` | Hong Kong: Court of First Instance, District Court, Family Court, Court of Appeal (Rules of the High Court, Rules of the District Court) | `jurisdictions/hk.md` |
| `us-federal` | United States district courts (Federal Rules of Civil Procedure, with local rules of the district) | `jurisdictions/us-federal.md` |
| `ny` | New York Supreme Court, including the Commercial Division (CPLR; 22 NYCRR) | `jurisdictions/ny.md` |
| `ca` | California Superior Court (Code of Civil Procedure; California Rules of Court; local rules such as San Francisco's) | `jurisdictions/ca.md` |
| `wa` | Washington Superior Court (Civil Rules; General Rules; local rules such as King County's) | `jurisdictions/wa.md` |
| `de-superior` | Delaware Superior Court (Superior Court Civil Rules) | `jurisdictions/de-superior.md` |
| `de-chancery` | Delaware Court of Chancery (Court of Chancery Rules) | `jurisdictions/de-chancery.md` |

For a court with no profile (England and Wales, Singapore, another US state), say so, draft with the closest profile as a guide only, and flag every formal requirement as one for the user to check. Never pass a draft off as compliant with rules no profile covers.

## What a profile sets

- **Document names.** For example: Statement of Claim or Complaint; Defence or Answer; Affirmation, Affidavit or Declaration; Skeleton Submissions or Memorandum of Law.
- **The pleading standard.** Material facts (Hong Kong), plausibility (federal), ultimate facts (California), material elements (New York), notice pleading (Washington).
- **The grammar of an answer.** For example, Hong Kong's admit, deny or not admit, with reasons and the defendant's own version, against the US admit, deny or lack knowledge, with affirmative defenses set out separately.
- **Verification and the evidence instrument.** A statement of truth and an affirmation with a jurat, or a signature certification and a declaration under penalty of perjury in the statutory words.
- **Amendment.** Coloured amendments with a legend, or a clean amended pleading plus a comparison (redline).
- **Formal rules for papers.** Backsheets, pleading paper, word or page limits, certificates.
- **The citation style.**
- **Forms that exist only there.** For example a request for further and better particulars, a bill of particulars, or a separate statement of undisputed facts.

## What never changes

The voice and perspective rules (`voice.md`), the field and placeholder rules (`fields.md`) and the authority policy (`authorities.md`) apply in every jurisdiction.

## Currency of the rules

Each profile states the rules as researched in October 2026 from official sources, and marks anything not confirmed as "not verified". Rules change. Tell the user to check the current rules and the local rules and standing orders of their court or judge before filing, and never present a draft as certainly compliant.
