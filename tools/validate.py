#!/usr/bin/env python3
"""Check that the plugin manifests, marketplaces, skills and docs agree, and that the skills
keep their own rules.

    python3 tools/validate.py

Checks:
  - every manifest and marketplace file is valid JSON, and the identity fields (name, version,
    description, license, homepage, repository, author) match across plugin.json,
    .codex-plugin/plugin.json, .claude-plugin/plugin.json and the Claude marketplace entry
  - the newest release in CHANGELOG.md is the manifest version
  - each marketplace entry resolves to the plugin folder; .codex-plugin/ holds only plugin.json
  - every skill: SKILL.md name matches its folder, description of 1,024 characters at most with
    a "Not for:" line, agents/openai.yaml with a display name and a short description of 64
    characters at most, a style.json whose rules compile and whose variants match the variant
    table in SKILL.md, and every reference file SKILL.md names exists
  - README.md, AGENTS.md and llms.txt name every skill
  - the skills follow their own punctuation rule: no em dash, and no en dash outside a range
  - the plugin is self-contained: no file tells the model to use a skill outside this plugin, and
    no file links to another repository
  - no file holds a real case or action number, and, if the environment variable
    LITIGATION_DENYLIST names a file (kept outside the repository, one name per line), no file
    contains any name on that list

Prints a warning, without failing, when the skill descriptions together exceed Codex's default
skill-list budget of 8,000 characters. Exit status 0 when every check passes, 1 otherwise.
Standard library only.
"""

import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PLUGIN_NAME = "litigation-writing"
PLUGIN = os.path.join(ROOT, "plugins", PLUGIN_NAME)
SKILLS = os.path.join(PLUGIN, "skills")
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
IDENTITY = ("name", "version", "description", "license", "homepage", "repository", "author")
CODEX_BUDGET = 8000
SKIP_DIRS = {".git", "dist", "__pycache__", "tests"}
BINARY = (".zip", ".skill", ".png", ".jpg", ".jpeg", ".gif", ".pdf", ".pyc")
CASE_NUMBER = re.compile(r"\b(?:HCA|HCMP|HCPI|HCCL|HCCW|HCB|HCAL|HCAJ|HCMC|CACV|CAMP|FACV|FAMV|FCMC|DCCJ|DCMP|DCPI|LDBM)\s?\d{1,5}\s?(?:/|of)\s?\d{4}\b")
OWN_SKILLS = {"litigation-writing", "litigation-pleadings", "litigation-evidence", "litigation-submissions",
              "litigation-advice", "litigation-correspondence"}
SKILL_CALL = re.compile(r"\b(?:load|use|run|call|invoke|stack(?:s)? on)\s+the\s+`?([A-Za-z0-9-]+)`?\s+skill", re.I)
REPO_LINK = re.compile(r"(?:github\.com|raw\.githubusercontent\.com)/([\w.-]+/[\w.-]+)")

errors, warnings = [], []


def rel(path):
    return os.path.relpath(path, ROOT)


def load(path):
    try:
        with open(path, encoding="utf-8") as fh:
            return json.load(fh)
    except FileNotFoundError:
        errors.append("missing %s" % rel(path))
    except ValueError as exc:
        errors.append("%s is not valid JSON: %s" % (rel(path), exc))
    return None


def frontmatter(text):
    m = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None
    fields, key = {}, None
    for line in m.group(1).splitlines():
        km = re.match(r"^([A-Za-z_][\w-]*):\s?(.*)$", line)
        if km:
            key = km.group(1)
            fields[key] = km.group(2).strip()
        elif key and line.startswith((" ", "\t")):
            fields[key] = (fields[key] + " " + line.strip()).strip()
    for k, v in fields.items():
        if len(v) >= 2 and v[0] == v[-1] == '"':
            try:
                fields[k] = json.loads(v)
            except ValueError:
                fields[k] = v[1:-1]
        elif len(v) >= 2 and v[0] == v[-1] == "'":
            fields[k] = v[1:-1].replace("''", "'")
    return fields


def yaml_value(text, key):
    m = re.search(r"^\s+%s:\s*\"((?:[^\"\\]|\\.)*)\"\s*$" % re.escape(key), text, re.M)
    return m.group(1) if m else None


def check_manifests():
    portable = load(os.path.join(PLUGIN, "plugin.json"))
    codex = load(os.path.join(PLUGIN, ".codex-plugin", "plugin.json"))
    claude = load(os.path.join(PLUGIN, ".claude-plugin", "plugin.json"))
    claude_mp = load(os.path.join(ROOT, ".claude-plugin", "marketplace.json"))
    codex_mp = load(os.path.join(ROOT, ".agents", "plugins", "marketplace.json"))
    if None in (portable, codex, claude, claude_mp, codex_mp):
        return None
    if not str(portable.get("$schema", "")).startswith("https://agent-plugins.org/schemas/"):
        errors.append("plugin.json needs the Agent Plugins $schema")
    if "extensions" in portable:
        errors.append("plugin.json must not carry an extensions block, or Codex ignores .codex-plugin/plugin.json")
    for label, m in (("plugin.json", portable), (".codex-plugin/plugin.json", codex), (".claude-plugin/plugin.json", claude)):
        for k in IDENTITY:
            if k not in m:
                errors.append("%s is missing %s" % (label, k))
            elif m[k] != portable.get(k):
                errors.append("%s: %s differs from plugin.json" % (label, k))
    if codex.get("skills") != "./skills/":
        errors.append('.codex-plugin/plugin.json needs "skills": "./skills/"')
    for k in ("displayName", "shortDescription", "developerName", "category"):
        if not codex.get("interface", {}).get(k):
            errors.append(".codex-plugin/plugin.json interface is missing %s" % k)
    extra = sorted(set(os.listdir(os.path.join(PLUGIN, ".codex-plugin"))) - {"plugin.json"})
    if extra:
        errors.append(".codex-plugin/ must hold only plugin.json, found %s" % ", ".join(extra))
    entries = [p for p in claude_mp.get("plugins", []) if p.get("name") == portable.get("name")]
    if len(entries) != 1:
        errors.append(".claude-plugin/marketplace.json needs exactly one entry named %s" % portable.get("name"))
    else:
        e = entries[0]
        for k in ("version", "description", "license"):
            if e.get(k) != portable.get(k):
                errors.append(".claude-plugin/marketplace.json entry: %s differs from plugin.json" % k)
        if os.path.normpath(os.path.join(ROOT, e.get("source", ""))) != PLUGIN:
            errors.append(".claude-plugin/marketplace.json source should be ./plugins/%s" % PLUGIN_NAME)
    if claude_mp.get("metadata", {}).get("version") != portable.get("version"):
        errors.append(".claude-plugin/marketplace.json metadata.version differs from plugin.json")
    entries = [p for p in codex_mp.get("plugins", []) if p.get("name") == portable.get("name")]
    if len(entries) != 1:
        errors.append(".agents/plugins/marketplace.json needs exactly one entry named %s" % portable.get("name"))
    else:
        e = entries[0]
        src = e.get("source", {})
        path = src.get("path", "") if isinstance(src, dict) else src
        if not path.startswith("./") or os.path.normpath(os.path.join(ROOT, path)) != PLUGIN:
            errors.append(".agents/plugins/marketplace.json source.path should be ./plugins/%s" % PLUGIN_NAME)
        for k in ("installation", "authentication"):
            if not e.get("policy", {}).get(k):
                errors.append(".agents/plugins/marketplace.json policy is missing %s" % k)
        if not e.get("category"):
            errors.append(".agents/plugins/marketplace.json entry is missing category")
    return portable.get("version")


def check_changelog(version):
    try:
        text = open(os.path.join(ROOT, "CHANGELOG.md"), encoding="utf-8").read()
    except FileNotFoundError:
        errors.append("missing CHANGELOG.md")
        return
    m = re.search(r"^## \[(\d+\.\d+\.\d+)\]", text, re.M)
    if not m:
        errors.append("CHANGELOG.md has no '## [x.y.z]' release heading")
    elif version and m.group(1) != version:
        errors.append("newest CHANGELOG.md release is %s, manifests say %s" % (m.group(1), version))


def variant_table(text):
    m = re.search(r"^## Variants\s*\n(.*?)(?=^## )", text, re.S | re.M)
    if not m:
        return None
    return set(re.findall(r"^\|\s*`([a-z0-9-]+)`\s*\|", m.group(1), re.M))


def check_style(n, d, skill_text):
    spec = load(os.path.join(d, "style.json"))
    if spec is None:
        return
    if spec.get("name") != n:
        errors.append("skills/%s/style.json name is %r" % (n, spec.get("name")))
    families = {"pleadings", "evidence", "submissions", "advice", "correspondence", "procedural", "chronology"}
    if spec.get("family") not in families:
        errors.append("skills/%s/style.json family %r is not one of %s" % (n, spec.get("family"), ", ".join(sorted(families))))
    rules = list(spec.get("base", {}).get("require", [])) + list(spec.get("base", {}).get("forbid", []))
    for vname, v in spec.get("variants", {}).items():
        if v.get("family") and v["family"] not in families:
            errors.append("skills/%s/style.json variant %s family %r unknown" % (n, vname, v["family"]))
        rules += list(v.get("require", [])) + list(v.get("forbid", []))
    for r in rules:
        for p in r.get("any", []):
            try:
                re.compile(p)
            except re.error as exc:
                errors.append("skills/%s/style.json rule %s: bad regex %r (%s)" % (n, r.get("id"), p, exc))
    table = variant_table(skill_text)
    if table is None:
        errors.append("skills/%s/SKILL.md has no '## Variants' table" % n)
    else:
        spec_v = set(spec.get("variants", {}))
        for v in sorted(table - spec_v):
            errors.append("skills/%s: variant %s is in SKILL.md but not style.json" % (n, v))
        for v in sorted(spec_v - table):
            errors.append("skills/%s: variant %s is in style.json but not SKILL.md" % (n, v))


def check_skills():
    names, total = [], 0
    for n in sorted(os.listdir(SKILLS)):
        d = os.path.join(SKILLS, n)
        if not os.path.isdir(d):
            continue
        names.append(n)
        path = os.path.join(d, "SKILL.md")
        if not os.path.isfile(path):
            errors.append("skills/%s has no SKILL.md" % n)
            continue
        text = open(path, encoding="utf-8").read()
        fm = frontmatter(text)
        if fm is None:
            errors.append("skills/%s/SKILL.md has no frontmatter" % n)
            continue
        name, desc = fm.get("name", ""), fm.get("description", "")
        if name != n:
            errors.append("skills/%s/SKILL.md name is %r, expected %r" % (n, name, n))
        if not NAME_RE.match(name) or len(name) > 64:
            errors.append("skills/%s: name must be lowercase words joined by hyphens, 64 characters at most" % n)
        if not desc:
            errors.append("skills/%s/SKILL.md has no description" % n)
        else:
            if len(desc) > 1024:
                errors.append("skills/%s description is %d characters; the limit is 1,024" % (n, len(desc)))
            if "Not for:" not in desc:
                errors.append("skills/%s description has no 'Not for:' line" % n)
        total += len(desc)
        if len(text.splitlines()) > 500:
            errors.append("skills/%s/SKILL.md is over 500 lines" % n)
        for ref in sorted(set(re.findall(r"`(references/[\w./-]+\.md)`", text))):
            if not os.path.isfile(os.path.join(d, ref)):
                errors.append("skills/%s/SKILL.md names %s, which does not exist" % (n, ref))
        ypath = os.path.join(d, "agents", "openai.yaml")
        if not os.path.isfile(ypath):
            errors.append("skills/%s has no agents/openai.yaml" % n)
        else:
            y = open(ypath, encoding="utf-8").read()
            short = yaml_value(y, "short_description")
            if not yaml_value(y, "display_name"):
                errors.append("skills/%s/agents/openai.yaml has no display_name" % n)
            if not short:
                errors.append("skills/%s/agents/openai.yaml has no short_description" % n)
            elif len(short) > 64:
                errors.append("skills/%s short_description is %d characters; keep it to 64" % (n, len(short)))
        check_style(n, d, text)
    if total > CODEX_BUDGET:
        warnings.append("skill descriptions total %d characters, over Codex's default %d-character skill list; "
                        "Codex shortens them unless skills.max_context_tokens is raised (see README)" % (total, CODEX_BUDGET))
    return names


def text_files(base, skip=SKIP_DIRS):
    for b, dirs, files in os.walk(base):
        dirs[:] = sorted(x for x in dirs if x not in skip)
        for f in sorted(files):
            if f.endswith(BINARY):
                continue
            p = os.path.join(b, f)
            try:
                yield p, open(p, encoding="utf-8").read()
            except (UnicodeDecodeError, OSError):
                continue


def repo_slug():
    try:
        url = json.load(open(os.path.join(PLUGIN, "plugin.json"), encoding="utf-8")).get("repository", "")
    except (OSError, ValueError):
        return ""
    m = REPO_LINK.search(url)
    return m.group(1).lower() if m else ""


def check_own_rules():
    for p, t in text_files(PLUGIN):
        if not p.endswith(".md"):
            continue
        for i, line in enumerate(t.splitlines(), 1):
            if "\u2014" in line:
                errors.append("%s:%d uses an em dash" % (rel(p), i))
            if re.search(r"(?<![0-9])\u2013|\u2013(?![0-9])", line):
                errors.append("%s:%d uses an en dash outside a range" % (rel(p), i))
    own_repo = repo_slug()
    for p, t in text_files(ROOT):
        for m in SKILL_CALL.finditer(t):
            if m.group(1).lower() not in OWN_SKILLS:
                errors.append("%s:%d tells the model to use a skill outside this plugin (%s); the plugin must be self-contained"
                              % (rel(p), t.count("\n", 0, m.start()) + 1, m.group(1)))
        for m in REPO_LINK.finditer(t):
            slug = re.sub(r"\.git$", "", m.group(1).lower().rstrip("."))
            if own_repo and slug != own_repo and not slug.startswith(own_repo + "/"):
                errors.append("%s:%d links to another repository (%s)" % (rel(p), t.count("\n", 0, m.start()) + 1, slug))


def check_no_names():
    deny = []
    path = os.environ.get("LITIGATION_DENYLIST")
    if path:
        try:
            deny = [l.strip() for l in open(path, encoding="utf-8") if l.strip() and not l.startswith("#")]
        except OSError as exc:
            errors.append("cannot read LITIGATION_DENYLIST %s: %s" % (path, exc))
    pats = [re.compile(r"(?<![A-Za-z])%s(?![A-Za-z])" % re.escape(d), re.I) for d in deny]
    for p, t in text_files(ROOT, skip=SKIP_DIRS - {"tests"}):
        for m in CASE_NUMBER.finditer(t):
            errors.append("%s:%d holds what looks like a real case number" % (rel(p), t.count("\n", 0, m.start()) + 1))
        for pat in pats:
            m = pat.search(t)
            if m:
                errors.append("%s:%d contains a name on the private deny-list" % (rel(p), t.count("\n", 0, m.start()) + 1))


def check_docs(names):
    for doc in ("README.md", "AGENTS.md", "llms.txt"):
        try:
            text = open(os.path.join(ROOT, doc), encoding="utf-8").read()
        except FileNotFoundError:
            errors.append("missing %s" % doc)
            continue
        for n in names:
            if n not in text:
                errors.append("%s does not name the %s skill" % (doc, n))


def main(argv):
    if len(argv) != 1:
        print(__doc__)
        return 2
    version = check_manifests()
    check_changelog(version)
    names = check_skills()
    check_docs(names)
    check_own_rules()
    check_no_names()
    for w in warnings:
        print("warning: " + w)
    for e in errors:
        print("error: " + e)
    print("validate: %d skills, version %s, %d error%s" % (len(names), version, len(errors), "" if len(errors) == 1 else "s"))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
