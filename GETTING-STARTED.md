# Getting started: a plain-language guide for lawyers

This guide is for litigators who have never installed a plugin or used a "skill", and who may not use Claude or ChatGPT at all. It assumes nothing technical. If you can download a file and paste text into a chat window, you can use these skills.

## What this is, in one paragraph

These are written drafting instructions for an AI assistant. They tell the assistant how a careful litigator drafts a pleading, an affidavit or witness statement, a skeleton or brief, an advice, or a letter to the other side. They cover what each document must contain, whose voice it is in, what to ask you before starting, and what it must never make up. The instructions are plain text files. They work best inside Claude or Codex, but almost any AI assistant can follow them if you give it the files or a link to them.

## Before you start: confidentiality

The skills themselves send nothing anywhere. The AI service you use them with does. Before you put any client material into an AI tool:

1. Check your professional obligations, and your firm's or chambers' policy on AI tools and client information.
2. Use only a service your firm approves for client material (often a business or enterprise account rather than a free personal one).
3. Where your policy requires it, anonymise names and identifying details first. The skills work with placeholders such as `[Plaintiff]` and `[date]`, so you lose nothing by doing this.

## Step 1: choose the skill for your document

You only ever need one skill at a time.

| You want to draft | Use this skill |
|---|---|
| Not sure, or several documents for one step in the case (for example everything needed for an application) | `litigation-writing` (it plans the papers and tells you which skill to use for each) |
| A statement of claim or complaint, a defence or answer, a reply, a counterclaim, or an amendment | `litigation-pleadings` |
| An affirmation, affidavit, declaration or witness statement | `litigation-evidence` |
| Skeleton submissions, a brief or memorandum of law, a reply, a hearing or speaking note, trial opening or closing submissions, appeal or costs submissions, a list of authorities, a chronology | `litigation-submissions` |
| A written advice or opinion | `litigation-advice` |
| A letter to the other side: request for particulars, demand, settlement proposal, formal offer, covering letter | `litigation-correspondence` |

The courts covered today are Hong Kong, the US federal courts, New York, California, Washington and Delaware (Superior Court and Court of Chancery). For another court, the skills still work, but they will tell you which formal requirements you must check yourself.

## Step 2: set it up in the tool you use

Find your tool below and follow only that section.

### If you use Claude on the web (claude.ai) or the Claude desktop app

The simplest way, with nothing to install:

1. Download the file for your skill from the [latest release](https://github.com/3orionkings/litigation-writing/releases/latest). Each skill has its own file, for example `litigation-pleadings.zip`. You do not need to open it.
2. In Claude, open **Settings**, look for **Skills** (it may sit under **Capabilities**), and choose **Upload skill**. Select the file you downloaded.
3. Repeat for any other skills you want. From then on, Claude will use the right skill when you ask for that kind of document, or you can name it ("use the litigation-pleadings skill").

If you do not see Skills in your settings, your plan or your organisation's settings may not include it yet. Use the **Project** method in "Any other AI assistant" below instead: it works in Claude too.

### If you use Claude Code (the terminal version of Claude)

Paste these two lines into the terminal, one at a time, and press Enter after each:

```bash
claude plugin marketplace add 3orionkings/litigation-writing
```

```bash
claude plugin install litigation-writing@litigation-writing
```

Start a new session. All six skills are now available.

### If you use the Codex app or the ChatGPT desktop app

1. The plugin's address has to be added once. If your app's Plugins tab lets you add a marketplace, add `3orionkings/litigation-writing` there. If it does not, ask whoever looks after your computer to run this one command in a terminal: `codex plugin marketplace add 3orionkings/litigation-writing`.
2. Open the **Plugins** tab (in Codex you can also type `/plugins`) and install **Litigation Writing**.
3. Start a new chat. You can type `@` to pick a skill by name, or just describe the document.

If your version does not offer plugins, use one of the methods in the next section.

### If you use any other AI assistant (Gemini, Perplexity, Copilot, ChatGPT on the web, and others)

There are three ways. Pick the one your tool supports. Method A is the quickest to try, and Method C is the best for regular use.

**Method A: give it a link.** This works if your assistant can read web pages. Gemini, Perplexity and ChatGPT with browsing usually can.

1. Copy the message below into a new chat.
2. Replace the words in angle brackets.
3. Send it, then answer the questions it asks.

```text
Please act as my litigation drafting assistant. First read this skill and follow it exactly:
https://raw.githubusercontent.com/3orionkings/litigation-writing/main/plugins/litigation-writing/skills/<skill name>/SKILL.md
The files it refers to are in the same folder, for example .../references/fields.md,
.../references/voice.md, .../references/authorities.md and .../references/jurisdictions/<court code>.md.
Read the ones it tells you to read before you start.
Court: <for example Hong Kong Court of First Instance, or New York Supreme Court>
Document: <for example a defence to the attached statement of claim>
Ask me for anything you need before drafting. Never invent a fact, a case or a citation.
```

The court codes are `hk`, `us-federal`, `ny`, `ca`, `wa`, `de-superior` and `de-chancery`. If the assistant says it cannot open the link, or its answer shows it has not read the files, use Method B.

**Method B: attach the files.** This works with any assistant that accepts attachments.

1. Download `litigation-writing-all-skills.zip` from the [latest release](https://github.com/3orionkings/litigation-writing/releases/latest) and double-click it to unzip. You will get a folder for each skill.
2. Open the folder for your skill. Attach these files to a new chat:
   - `SKILL.md`;
   - from the `references` folder: `fields.md`, `voice.md`, `authorities.md` and `formulae.md`, plus the file for your document type (for example `defence.md` or `skeleton.md`);
   - from `references/jurisdictions`: the file for your court (for example `hk.md` or `ny.md`).
3. In the same message, write: "Follow the attached SKILL.md and the attached reference files exactly. Ask me for anything you need before drafting. Never invent a fact, a case or a citation." Then say what you want drafted and for which court.

If your assistant cannot open `.md` files, rename them to end in `.txt`. They are plain text either way.

**Method C: set it up once in a reusable space.** Most assistants let you save instructions and files in a space you return to. It is called a Project in Claude and ChatGPT, a Gem in Gemini and a Space in Perplexity, and the names change from time to time.

1. Create a new space and give it a name, for example "Pleadings".
2. Add the same files as in Method B to its knowledge or files.
3. In its instructions, write: "Follow the attached SKILL.md and its reference files exactly for every document. Ask for anything you need before drafting. Never invent a fact, a case or a citation."
4. Open a chat inside that space whenever you need that kind of document.

Make one space per skill you use often.

## Step 3: give it what you would give a junior

The skill will ask you, in one list, for what the document needs. Answer what you can and say "go ahead" for the rest. The more of the real material you share, the more accurate the draft:

- the court and the case number, the parties and who you act for;
- for pleadings, the client's instructions, a list of the people and companies involved (a dramatis personae), a chronology, the key documents, and for a defence or reply the pleading you are answering;
- for affidavits and witness statements, the documents to be exhibited, the client's or witness's instructions (a statement, a memo or attendance notes), and the other side's evidence if you are replying;
- for submissions and advice, copies or extracts of the cases and other authorities you rely on, the pleadings, the evidence and any order or transcript that matters.

Share the authorities themselves, not only their names. The skills quote a judgment word for word only when they have its text. They do not quote from memory, and they keep any paraphrase of a legal test to its exact elements.

## Step 4: read what comes back

1. **The draft.** Paragraphs are numbered. The voice fits the document: the party's case in a pleading, the witness's own words in an affidavit, counsel's argument in a skeleton.
2. **Square brackets.** Anything you did not supply appears as a placeholder such as `[date 1]`, `[sum]`, `[Bundle ref]` or `[authority needed: …]`. These are deliberate. The draft never guesses a fact. The same number means the same value, so `[date 1]` can be filled in everywhere with one find-and-replace.
3. **The "FIELDS TO COMPLETE" table** at the end lists every gap and where it sits. Delete the table before filing.
4. **Check every authority yourself.** The skills cite only what you gave them, but you are the one filing the document. Read every citation and every quotation against the source.
5. **Move it into Word.** Copy the text into your firm's template. The paragraph numbers come across as ordinary text; switch them to your template's automatic numbering if you prefer.

## A first message you can copy

```text
Use the litigation-evidence skill. Court: Hong Kong, Court of First Instance.
I need the 1st affirmation of our client, a company director, in support of our
summons for summary judgment. I will attach the statement of claim, the client's
attendance note and the documents to exhibit. Ask me anything you need first.
```

## Common questions

**Do I need to know any code?** No. The guide above needs only downloading, uploading and pasting. The skills include a small checking program for assistants that can run code; if yours cannot, the skills still work and the assistant follows the same rules by reading them.

**It asked me a lot of questions before drafting.** That is intended. It asks once, all together, so that it does not guess. You can answer only some and tell it to go ahead.

**It wrote `[authority needed]` instead of citing a case.** It has no authority from you for that point, and it will not make one up. Give it the case you rely on, preferably with the judgment, and ask it to redraft that paragraph.

**It cited a case I did not give it.** That should not happen. Do not rely on it. Please report it (see below) with an invented example that shows the same thing.

**Is my client's information stored in the repository?** No. Nothing you type goes to the repository. Whether your AI service keeps your chats depends on that service and your account settings, which is why the confidentiality steps above matter.

**Does it work for my court if it is not listed?** Yes, as a drafting guide. It will tell you which formal requirements (format, verification, deadlines) you must check against your court's own rules.

**Is this legal advice?** No. It is a drafting aid. You remain responsible for every document you sign or file.

## Words you may see

- **Skill**: a set of written instructions an AI assistant follows for one kind of task.
- **Plugin**: a bundle of skills that installs in one step in Claude Code, Codex or the ChatGPT desktop app.
- **Repository** (or **repo**): this folder of files on GitHub, which anyone can read and download.
- **Release**: a dated, packaged version of the files, ready to download.
- **Marketplace**: the address a tool uses to find and install a plugin. Here it is `3orionkings/litigation-writing`.
- **Terminal**: a window where you type commands. Only needed for Claude Code; everything else in this guide avoids it.

## Getting help or reporting a problem

Open an issue on the [repository page](https://github.com/3orionkings/litigation-writing/issues). Say which skill and which court, and describe the problem with an invented example. Never post real client material, names or case numbers.
