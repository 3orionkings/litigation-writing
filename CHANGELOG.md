# Changelog

All notable changes to this project are recorded here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and versions follow [semantic versioning](https://semver.org/).

## [Unreleased]

## [1.0.0] - 2026-10-19

The first release.

### Added

- Six skills: `litigation-writing` (matter intake, packages, summons or notice of motion, draft or proposed order), `litigation-pleadings`, `litigation-evidence`, `litigation-submissions`, `litigation-advice` and `litigation-correspondence`.
- A shared core copied into every skill: the field and placeholder protocol, the voice and perspective rules for each kind of document, the authority policy, the matter file, and jurisdiction profiles for Hong Kong, US federal courts, New York, California, Washington, and Delaware's Superior Court and Court of Chancery.
- Each skill asks, with the fields, for the materials it drafts from: copies of the authorities (submissions, advice), the exhibits, memos and client instructions (evidence), the client's instructions, a dramatis personae, a chronology and the source documents (pleadings). Quotations of authority are reproduced exactly, emphasis is marked "(emphasis added)", and a paraphrase of a principle or test keeps its elements and threshold words.
- `scripts/litcheck.py` in every skill: checks structure, voice, register, jurisdiction formalities, placeholders and citations, and lists the fields a document needs.
- A plugin for Claude Code and for Codex and the ChatGPT desktop app, with a marketplace for each; `llms.txt` and `AGENTS.md` so any AI assistant can choose and load a skill.
- `tools/validate.py`, `tools/sync_shared.py`, `tools/package.py`, the test suite, and continuous integration on GitHub Actions.
