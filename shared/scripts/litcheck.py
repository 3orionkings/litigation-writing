#!/usr/bin/env python3
"""Check a litigation draft, or list the fields a document needs.

Usage:
    python3 litcheck.py check DRAFT --variant NAME --jurisdiction CODE [--matter matter.json] [--json]
    python3 litcheck.py fields --variant NAME --jurisdiction CODE [--matter matter.json] [--json]
    python3 litcheck.py variants

Options:
    --skill NAME    the skill whose rules apply (default: the skill this script sits in)
    --spec FILE     use another style.json (for tests)
    --assets DIR    use another assets folder (for tests)

check runs, in order: structure (this skill's style.json, for the variant), perspective (who is
speaking, from assets/perspective.json), register (dashes and tells, assets/register.json),
jurisdiction rules (assets/jurisdictions.json), placeholders (assets/placeholders.json), and
citations. With --matter, any case citation that is not among the matter file's authorities is
a hard failure. Exit status 0 when there is no hard failure, 1 when there is one, 2 on a usage
error.

fields prints the fields the variant needs in that jurisdiction, grouped and marked R
(required), O (optional) or L (filled in later), from assets/fields.json; with --matter it
marks which are already in the matter file. Ask the user for the missing R fields before
drafting.

The checks are mechanical. They catch missing parts, the wrong voice, banned punctuation,
unfilled gaps and unsupported citations; they do not judge whether the law or the argument is
right. Standard library only. Python 3.8 or later.
"""

import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SKILL_DIR = os.path.dirname(HERE)

END_MARKER = re.compile(r"^\s*#*\s*\**\s*fields to complete\b", re.I | re.M)
TAIL_MARKER = re.compile(
    r"^\s*#*\s*\**\s*(?:statement of truth|verification|certificate|interpreter'?s?|translator'?s?|jurat|"
    r"affirmed\b|sworn\b|declared\b|before me\b|list of authorities|backsheet|signed\b|dated this\b|"
    r"i (?:certify|declare) under penalty)", re.I)
HEADING_MD = re.compile(r"^\s{0,3}#{1,6}\s+")
LETTERED_HEADING = re.compile(r"^\s*(?:[A-Z]{1,2}\d*(?:\.\d+)*\.?|[IVX]{1,5}\.)\s+[A-Z][^.]{0,90}$")
NUMBERED = re.compile(r"^\s*(?:\d+(?:\.\d+)*[A-Z]?[.)]?\s+|\(\s*(?:[a-z]{1,4}|\d{1,3})\s*\)\s+|[a-z][.)]\s+)")
BULLET = re.compile(r"^\s*(?:[-*+•])\s+\S")
QUOTE_LINE = re.compile(r"^(?:\s{4,}|\t|\s*>)")
TABLE_LINE = re.compile(r"^\s*\|")
FENCE = re.compile(r"^\s*```")
SUMMARY_CLOSE = re.compile(r"^\s*(?:\d+(?:\.\d+)*\.?\s+)?(?:in (?:summary|conclusion|short|closing)|to (?:sum up|summari[sz]e|recap|conclude)|overall|all in all)\b", re.I)
FIRST_PERSON = re.compile(
    r"(?<![A-Za-z.\-/])I(?=\s+(?:am|was|have|had|will|would|do|did|submit|say|said|consider|believe|believed|think|"
    r"note|invite|accept|rely|refer|turn|can|could|should|must|may|might|make|made|know|knew|saw|heard|"
    r"received|sent|signed|met|told|asked|agreed|paid|verily|further|also|then|exhibit|produce|affirm|"
    r"declare|certify|understand|recall|remember|was)\b)|\b(?:my|me|myself)\b")
FIRST_PERSON_PLURAL = re.compile(r"\b(?:we|We|our|Our|ours|ourselves)\b|\bus\b")
EM_DASH = re.compile(r"—")
EN_DASH = re.compile(r"(?<![0-9§])\s*–\s*(?![0-9])")
SPACED_HYPHEN = re.compile(r"(?<=[A-Za-z,;)\]])\s-\s(?=[A-Za-z(\[])")
QUOTED_SPAN = re.compile(r"“[^”]{0,600}”|\"[^\"\n]{0,600}\"|‘[^’\n]{0,300}’")


def load_json(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def rx(pattern, case=False):
    flags = re.M if case else (re.M | re.I)
    return re.compile(pattern, flags)


class Draft:
    def __init__(self, text):
        self.raw = text.replace("\r\n", "\n")
        m = END_MARKER.search(self.raw)
        self.text = self.raw[:m.start()] if m else self.raw
        self.has_fields_table = bool(m)
        self.lines = self.text.split("\n")
        tail = None
        for i, line in enumerate(self.lines):
            if i > len(self.lines) * 0.4 and TAIL_MARKER.match(line):
                tail = i
                break
        self.body_end = tail if tail is not None else len(self.lines)
        self.body = "\n".join(self.lines[:self.body_end])
        self.paragraphs = self._paragraphs()

    def _paragraphs(self):
        out, in_fence = [], False
        for i, line in enumerate(self.lines[:self.body_end]):
            if FENCE.match(line):
                in_fence = not in_fence
                continue
            if in_fence or not line.strip():
                continue
            s = line.strip()
            if HEADING_MD.match(line) or TABLE_LINE.match(line) or QUOTE_LINE.match(line):
                continue
            words = re.findall(r"[A-Za-z0-9'§$]+", s)
            if len(words) <= 6:
                continue
            letters = [c for c in s if c.isalpha()]
            if letters and sum(1 for c in letters if c.isupper()) / len(letters) > 0.8:
                continue
            if LETTERED_HEADING.match(s) and not s.endswith((".", ":", ";")) and len(words) <= 14:
                continue
            out.append((i + 1, s))
        return out

    def region(self, where):
        if where == "start":
            return self.text[:max(1, len(self.text) // 4)]
        if where == "end":
            return self.text[int(len(self.text) * 0.67):]
        if where == "body":
            return self.body
        return self.text

    def words(self):
        return len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'’\-]*", self.text))


def strip_quotes(text):
    text = QUOTED_SPAN.sub(" ", text)
    return "\n".join(l for l in text.split("\n") if not QUOTE_LINE.match(l))


def line_of(text, pos):
    return text.count("\n", 0, pos) + 1


def snippet(text, pos, n=60):
    return text[pos:pos + n].split("\n")[0].strip()


class Report:
    def __init__(self):
        self.items = []

    def add(self, check, rule_id, label, passed, severity="hard", evidence=""):
        self.items.append({"check": check, "id": rule_id, "label": label, "passed": bool(passed),
                           "severity": severity, "evidence": evidence})

    def hard_failures(self):
        return [i for i in self.items if not i["passed"] and i["severity"] == "hard"]

    def soft(self):
        return [i for i in self.items if not i["passed"] and i["severity"] == "soft"]


def applies(rule, code, group):
    j = rule.get("jurisdictions")
    return not j or code in j or group in j


def run_rule(draft, rule, kind, report, check, code, group, family=None):
    if not applies(rule, code, group):
        return
    if family and rule.get("families") and family not in rule["families"]:
        return
    text = draft.region(rule.get("where", "anywhere"))
    if rule.get("skip_quotes"):
        text = strip_quotes(text)
    severity = rule.get("severity", "hard")
    hit = None
    for pat in rule.get("any", []):
        m = rx(pat, rule.get("case", False)).search(text)
        if m:
            hit = m
            break
    label = rule.get("label", rule.get("id", "rule"))
    if kind == "require":
        report.add(check, rule.get("id", ""), "has " + label, hit is not None, severity,
                   "" if hit else "not found")
    else:
        ev = ""
        if hit:
            ev = "line %d: %s" % (line_of(text, hit.start()), snippet(text, hit.start()))
        report.add(check, rule.get("id", ""), "no " + re.sub(r"^(?:a|an) ", "", label), hit is None, severity, ev)


def resolve_variant(spec, variant):
    base = dict(spec.get("base", {}))
    variants = spec.get("variants", {})
    if variant not in variants:
        raise KeyError(variant)
    v = variants[variant]
    out = dict(base)
    for k, val in v.items():
        if k in ("require", "forbid", "drop", "description"):
            continue
        out[k] = val
    drop = set(v.get("drop", []))
    out["require"] = [r for r in base.get("require", []) + v.get("require", []) if r.get("id") not in drop]
    out["forbid"] = [r for r in base.get("forbid", []) + v.get("forbid", []) if r.get("id") not in drop]
    out["family"] = v.get("family", spec.get("family"))
    return out


def apply_overrides(vspec, jdata, code, group, skill, variant, family):
    """A jurisdiction may change a variant's structural settings: for example US briefs do not number
    their paragraphs. Keys, least to most specific: family, skill:*, skill:variant; group entries
    apply before the profile's own."""
    out = dict(vspec)
    sources = [jdata.get("groups", {}).get(group, {}).get("overrides", {}),
               jdata.get("profiles", {}).get(code, {}).get("overrides", {})]
    for src in sources:
        for key in (family, "%s:*" % skill, "%s:%s" % (skill, variant)):
            for k, v in src.get(key, {}).items():
                out[k] = v
    return out


def citation_finder(jdata):
    pats = {}
    for style, lst in jdata.get("citation_patterns", {}).items():
        pats[style] = [re.compile(p) for p in lst]
    return pats


def find_citations(text, pats):
    found = []
    for style, lst in pats.items():
        for p in lst:
            for m in p.finditer(text):
                found.append((m.start(), m.end(), style, m.group(0)))
    found.sort()
    out, last_end = [], -1
    for s, e, style, g in found:
        if s >= last_end:
            out.append((s, e, style, g))
            last_end = e
    return out


def norm(s):
    return re.sub(r"[\s.,]+", " ", s).strip().lower()


def check_structure(draft, spec, report):
    if spec.get("numbered_paragraphs"):
        paras = draft.paragraphs
        numbered = [p for p in paras if NUMBERED.match(p[1])]
        ratio = (len(numbered) / len(paras)) if paras else 1.0
        report.add("structure", "numbered", "paragraphs numbered (%d of %d)" % (len(numbered), len(paras)),
                   ratio >= 0.6 or len(paras) < 3, "hard",
                   "" if ratio >= 0.6 else "first unnumbered: line %d" % next((p[0] for p in paras if not NUMBERED.match(p[1])), 0))
    w = spec.get("words")
    if w:
        n = draft.words()
        lo, hi = w.get("min"), w.get("max")
        ok = (lo is None or n >= lo) and (hi is None or n <= hi)
        report.add("structure", "words", "length within %s to %s words (%d)" % (lo, hi, n), ok, "soft")
    last = [p for p in draft.paragraphs[-3:]]
    closer = next((p for p in last if SUMMARY_CLOSE.match(p[1])), None)
    report.add("structure", "summary-close", "no summarising close", closer is None, "hard",
               "line %d" % closer[0] if closer else "")


def check_perspective(draft, family, pdata, spec, report, code, group, cites):
    fam = pdata.get("families", {}).get(family, {})
    body = strip_quotes(draft.body)
    fp_mode = spec.get("first_person") or fam.get("first_person", "allow")
    fp = list(FIRST_PERSON.finditer(body))
    if fp_mode == "forbid":
        ev = "line %d: %s" % (line_of(body, fp[0].start()), snippet(body, fp[0].start())) if fp else ""
        report.add("perspective", "first-person", "no first person singular in a %s document" % family, not fp, "hard", ev)
    elif fp_mode == "soft":
        report.add("perspective", "first-person", "first person singular kept out (%s)" % family, not fp, "soft",
                   "%d uses" % len(fp) if fp else "")
    elif fp_mode == "require":
        report.add("perspective", "first-person", "written in the first person (%d uses)" % len(fp), len(fp) >= 3, "hard")
    fpp_mode = spec.get("first_person_plural") or fam.get("first_person_plural", "allow")
    if fpp_mode in ("forbid", "soft"):
        fpp = list(FIRST_PERSON_PLURAL.finditer(body))
        ev = "line %d: %s" % (line_of(body, fpp[0].start()), snippet(body, fpp[0].start())) if fpp else ""
        report.add("perspective", "first-person-plural", "no first person plural in a %s document" % family, not fpp,
                   "hard" if fpp_mode == "forbid" else "soft", ev)
    if (spec.get("case_citations") or fam.get("case_citations")) == "forbid":
        body_cites = [c for c in cites if c[0] < len(draft.body)]
        report.add("perspective", "no-case-law", "no case citations in a %s document" % family, not body_cites, "hard",
                   body_cites[0][3] if body_cites else "")
    for r in fam.get("forbid", []):
        run_rule(draft, r, "forbid", report, "perspective", code, group)
    for r in fam.get("require", []):
        run_rule(draft, r, "require", report, "perspective", code, group)


def check_register(draft, rdata, report, code, group, family=None):
    text = strip_quotes(draft.text)
    if rdata.get("dashes", True):
        for name, pat in (("em-dash", EM_DASH), ("en-dash", EN_DASH), ("spaced-hyphen", SPACED_HYPHEN)):
            m = pat.search(text)
            report.add("register", name, "no %s used as punctuation" % name.replace("-", " "), m is None, "hard",
                       "line %d" % line_of(text, m.start()) if m else "")
    if rdata.get("bullets"):
        b = next((i + 1 for i, l in enumerate(draft.lines[:draft.body_end]) if BULLET.match(l)), None)
        report.add("register", "bullets", "no bullet points (number every list)", b is None, rdata["bullets"],
                   "line %d" % b if b else "")
    for r in rdata.get("forbid", []):
        run_rule(draft, r, "forbid", report, "register", code, group, family)


def check_jurisdiction(draft, jdata, code, skill, variant, family, report):
    prof = jdata["profiles"][code]
    group = prof.get("group", code)
    blocks = []
    gfam = jdata.get("groups", {}).get(group, {}).get("families", {}).get(family)
    if gfam:
        blocks.append(gfam)
    pfam = prof.get("families", {}).get(family)
    if pfam:
        blocks.append(pfam)
    pvar = prof.get("variants", {}).get("%s:%s" % (skill, variant))
    if pvar:
        blocks.append(pvar)
    for b in blocks:
        for r in b.get("require", []):
            run_rule(draft, r, "require", report, "jurisdiction", code, group)
        for r in b.get("forbid", []):
            run_rule(draft, r, "forbid", report, "jurisdiction", code, group)
    lim = prof.get("word_limits", {}).get("%s:%s" % (skill, variant))
    if lim:
        n = draft.words()
        report.add("jurisdiction", "word-limit", "within %s words, %s (%d)" % (lim["max"], lim["label"], n),
                   n <= lim["max"], "soft")


def placeholder_regex(pdata):
    roles = "|".join(re.escape(r) for r in pdata["party_roles"])
    labels = "|".join(re.escape(l) for l in pdata["labels"])
    free = "|".join(re.escape(l) for l in pdata["free_text"])
    return re.compile(r"\[(?:(?:\d+(?:st|nd|rd|th) )?(?:%s)|%s)(?: \d+)?\]|\[(?:%s):[^\]\n]{1,200}\]" % (roles, labels, free))


def check_placeholders(draft, pdata, report):
    pr = placeholder_regex(pdata)
    found = {}
    for m in pr.finditer(draft.text):
        found.setdefault(m.group(0), []).append(line_of(draft.text, m.start()))
    if found and not draft.has_fields_table:
        report.add("placeholders", "fields-table", "a FIELDS TO COMPLETE table after the draft", False, "hard",
                   "%d placeholder(s) and no table" % len(found))
    elif found:
        report.add("placeholders", "fields-table", "a FIELDS TO COMPLETE table after the draft", True)
    bad = []
    body = draft.body
    for pat in pdata.get("nonstandard", []):
        for m in re.finditer(pat, body):
            bad.append("line %d: %s" % (line_of(body, m.start()), m.group(0)[:30]))
    report.add("placeholders", "vocabulary", "gaps use the placeholder vocabulary", not bad, "soft", "; ".join(bad[:5]))
    return found


def check_citations(draft, jdata, code, matter, report):
    pats = citation_finder(jdata)
    cites = find_citations(draft.text, pats)
    prof = jdata["profiles"][code]
    local = set(prof.get("citation_local", []))
    pins = [re.compile(p, re.I) for p in jdata.get("pinpoint_patterns", [])]
    no_pin, foreign = [], []
    for s, e, style, g in cites:
        after = draft.text[e:e + 70]
        after = after.split("\n")[0]
        if not any(p.search(after) for p in pins):
            no_pin.append(g)
        if local and style not in local:
            foreign.append(g)
    if cites:
        report.add("citations", "pinpoints", "every citation has a pinpoint", not no_pin, "soft", "; ".join(no_pin[:4]))
        report.add("citations", "local-style", "citations in the %s style" % prof.get("name", code), not foreign, "soft",
                   "; ".join(foreign[:4]))
        if matter is not None:
            known = [norm(a.get("citation", "")) for a in matter.get("authorities", []) or [] if isinstance(a, dict)]
            unknown = [g for _, _, _, g in cites if not any(norm(g) in k or k in norm(g) for k in known if k)]
            report.add("citations", "supplied", "every citation is among the matter file's authorities", not unknown,
                       "hard", "; ".join(unknown[:5]))
        else:
            report.add("citations", "confirm", "%d citation(s) found: confirm each was supplied or verified by the user" % len(cites),
                       False, "soft", "; ".join(g for _, _, _, g in cites[:5]))
    return cites


def field_status(field, skill, variant, code, group):
    st = field.get("status", {})
    keys = ["%s:%s@%s" % (skill, variant, code), "%s:%s@%s" % (skill, variant, group), "%s:%s" % (skill, variant),
            "%s@%s" % (skill, code), "%s@%s" % (skill, group), skill, "*@%s" % code, "*@%s" % group, "*"]
    for k in keys:
        if k in st:
            return st[k]
    return "-"


def present(matter, fid):
    if not matter or fid not in matter:
        return False
    v = matter[fid]
    return v not in (None, "", [], {})


def cmd_fields(args, assets, spec, skill):
    fdata = load_json(os.path.join(assets, "fields.json"))
    jdata = load_json(os.path.join(assets, "jurisdictions.json"))
    code = args["--jurisdiction"]
    if code not in jdata["profiles"]:
        print("unknown jurisdiction %r; choose from %s" % (code, ", ".join(jdata["profiles"])))
        return 2
    group = jdata["profiles"][code].get("group", code)
    variant = args["--variant"]
    if variant not in spec.get("variants", {}):
        print("unknown variant %r for %s; choose from %s" % (variant, skill, ", ".join(spec.get("variants", {}))))
        return 2
    matter = load_json(args["--matter"]) if args.get("--matter") else None
    rows = []
    for f in fdata["fields"]:
        s = field_status(f, skill, variant, code, group)
        if s == "-":
            continue
        rows.append({"id": f["id"], "group": f["group"], "status": s, "holds": f["holds"],
                     "placeholder": f.get("placeholder"), "in_matter": present(matter, f["id"]) if matter is not None else None})
    if args.get("--json"):
        print(json.dumps({"skill": skill, "variant": variant, "jurisdiction": code, "fields": rows}, indent=1))
        return 0
    print("Fields for %s / %s / %s" % (skill, variant, code))
    for g in fdata.get("groups", []):
        grp = [r for r in rows if r["group"] == g]
        if not grp:
            continue
        print("\n%s" % g)
        for r in sorted(grp, key=lambda r: "RLO".index(r["status"]) if r["status"] in "RLO" else 9):
            mark = ""
            if r["in_matter"] is True:
                mark = "  [in matter file]"
            elif r["in_matter"] is False and r["status"] == "R":
                mark = "  [MISSING]"
            print("  %s  %-22s %s%s" % (r["status"], r["id"], r["holds"], mark))
    missing = [r["id"] for r in rows if r["status"] == "R" and r["in_matter"] is False]
    if matter is not None:
        print("\n%d required field(s) missing from the matter file%s" % (len(missing), (": " + ", ".join(missing)) if missing else ""))
    print("\nR = required (ask for it), O = optional, L = filled in later (leave a placeholder).")
    return 0


def cmd_check(args, assets, spec, skill):
    path = args.get("draft")
    if not path:
        print(__doc__)
        return 2
    text = sys.stdin.read() if path == "-" else open(path, encoding="utf-8").read()
    jdata = load_json(os.path.join(assets, "jurisdictions.json"))
    code = args["--jurisdiction"]
    if code not in jdata["profiles"]:
        print("unknown jurisdiction %r; choose from %s" % (code, ", ".join(jdata["profiles"])))
        return 2
    group = jdata["profiles"][code].get("group", code)
    variant = args["--variant"]
    try:
        vspec = resolve_variant(spec, variant)
    except KeyError:
        print("unknown variant %r for %s; choose from %s" % (variant, skill, ", ".join(spec.get("variants", {}))))
        return 2
    family = vspec.get("family") or spec.get("family")
    vspec = apply_overrides(vspec, jdata, code, group, skill, variant, family)
    matter = load_json(args["--matter"]) if args.get("--matter") else None
    draft = Draft(text)
    report = Report()
    check_structure(draft, vspec, report)
    for r in vspec.get("require", []):
        run_rule(draft, r, "require", report, "structure", code, group)
    for r in vspec.get("forbid", []):
        run_rule(draft, r, "forbid", report, "structure", code, group)
    cites = check_citations(draft, jdata, code, matter, report)
    check_perspective(draft, family, load_json(os.path.join(assets, "perspective.json")), vspec, report, code, group, cites)
    check_register(draft, load_json(os.path.join(assets, "register.json")), report, code, group, family)
    check_jurisdiction(draft, jdata, code, skill, variant, family, report)
    placeholders = check_placeholders(draft, load_json(os.path.join(assets, "placeholders.json")), report)
    hard = report.hard_failures()
    if args.get("--json"):
        print(json.dumps({"skill": skill, "variant": variant, "jurisdiction": code, "family": family,
                          "passed": not hard, "checks": report.items,
                          "placeholders": placeholders, "citations": [c[3] for c in cites]}, indent=1))
    else:
        print("litcheck: %s / %s / %s (%s)" % (skill, variant, code, family))
        for i in report.items:
            mark = "ok  " if i["passed"] else ("FAIL" if i["severity"] == "hard" else "note")
            ev = (" (%s)" % i["evidence"]) if i["evidence"] and not i["passed"] else ""
            print("  %s %-12s %s%s" % (mark, i["check"], i["label"], ev))
        if placeholders:
            print("\n  placeholders left: " + ", ".join("%s x%d" % (k, len(v)) for k, v in sorted(placeholders.items())))
        print("\n%d hard failure(s), %d note(s)" % (len(hard), len(report.soft())))
    return 1 if hard else 0


def cmd_variants(spec, skill):
    print("%s (%s)" % (skill, spec.get("family")))
    for k, v in spec.get("variants", {}).items():
        print("  %-20s %s" % (k, v.get("description", "")))
    return 0


def parse(argv):
    if len(argv) < 2 or argv[1] in ("-h", "--help"):
        return None
    args = {"cmd": argv[1]}
    i = 2
    while i < len(argv):
        a = argv[i]
        if a in ("--json",):
            args[a] = True
            i += 1
        elif a in ("--variant", "--jurisdiction", "--matter", "--skill", "--spec", "--assets"):
            if i + 1 >= len(argv):
                return None
            args[a] = argv[i + 1]
            i += 2
        elif not a.startswith("--") and "draft" not in args:
            args["draft"] = a
            i += 1
        else:
            return None
    return args


def main(argv):
    args = parse(argv)
    if not args or args["cmd"] not in ("check", "fields", "variants"):
        print(__doc__)
        return 2
    spec_path = args.get("--spec") or os.path.join(SKILL_DIR, "style.json")
    assets = args.get("--assets") or os.path.join(SKILL_DIR, "assets")
    try:
        spec = load_json(spec_path)
    except (OSError, ValueError) as exc:
        print("cannot read %s: %s" % (spec_path, exc))
        return 2
    skill = args.get("--skill") or spec.get("name") or os.path.basename(SKILL_DIR)
    if args["cmd"] == "variants":
        return cmd_variants(spec, skill)
    for need in ("--variant", "--jurisdiction"):
        if need not in args:
            print("%s is required\n" % need)
            print(__doc__)
            return 2
    if args["cmd"] == "fields":
        return cmd_fields(args, assets, spec, skill)
    return cmd_check(args, assets, spec, skill)


if __name__ == "__main__":
    sys.exit(main(sys.argv))
