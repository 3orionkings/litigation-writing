# Contributing

Thanks for helping. Useful changes fall into four kinds: a document that comes out with the wrong structure, a jurisdiction rule that is wrong or out of date, a checker that flags what it should not (or misses what it should), and a skill instruction a model misreads. Each is easiest to act on with an example.

## Reporting a problem

Open an issue with:

- the skill, the variant and the jurisdiction;
- an **invented** input and the output you got, or the line the checker flagged or missed;
- what you expected, and why. For a rule, cite the rule and give the official source.

Never include anything from a real matter: no names, case numbers, facts, drafts or matter files. A short invented example that shows the same problem is enough.

## Changing a skill, a profile or the checker

1. Read [AGENTS.md](AGENTS.md). Its invariants apply to people too.
2. Write the test first. Checker cases live in `tests/cases.json` (a draft, the skill, variant and jurisdiction, and the checks that must pass or fail). Wording that a skill must keep or must never contain goes in `tests/doc_checks.json`.
3. Make the change. Shared files are edited in `shared/` only, then copied out with `python3 tools/sync_shared.py`.
4. Run the checks:

```bash
python3 -I -B tests/run_tests.py
```

```bash
python3 tools/validate.py
```

If you have the Claude Code CLI, also run `claude plugin validate . --strict` and `claude plugin validate plugins/litigation-writing --strict`.

5. Add a line under `[Unreleased]` in `CHANGELOG.md`.

## How the skills are written

The skills hold to their own rules: plain, direct prose, no dash punctuation, none of the tells listed in `shared/references/voice.md`, no closing summaries. Four rules matter more than the rest:

- A skill never tells the model to invent a fact or an authority; where a document needs something the user has not supplied, it asks or leaves a placeholder from the fixed list.
- A skill never chooses the law; it drafts.
- A skill encodes moves and the profession's set formulae, never passages from anyone's filed documents.
- No name, case number or fact from a real matter appears anywhere.

Jurisdiction profiles state each rule with its number and, for US courts, an official source. Mark anything you could not confirm as not verified.

## Releasing

Versions follow semantic versioning. A patch fixes wording, a rule's detail or a checker without changing what passes. A minor version adds a rule, a check, a variant, a jurisdiction or a skill. A major version removes or renames a skill, a variant or a script option. To release: bump the version in the places listed in AGENTS.md, write the `CHANGELOG.md` entry, run the checks, tag `vX.Y.Z`, and attach the output of `python3 tools/package.py` to a GitHub release.
