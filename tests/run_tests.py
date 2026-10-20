#!/usr/bin/env python3
"""Run the litigation-writing test suite.

    python3 -I -B tests/run_tests.py
    python3 -I -B tests/run_tests.py --skills DIR     test another folder of skills (e.g. unzipped packages)

Suites:
  checker   tests/cases.json: each case is a draft in tests/cases/, run through the named skill's own
            copy of scripts/litcheck.py; the case lists check ids that must fail and that must pass,
            and whether the draft passes overall
  fields    tests/fields_cases.json: the fields helper marks fields R, O, L or omits them as expected
  docs      tests/doc_checks.json: wording that must be present in, or absent from, the skill files
  shared    every skill's copy of the shared core is identical to shared/ (tools/sync_shared.py --check)

Exit status 0 when every test passes, 1 otherwise. Standard library only.
"""

import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DEFAULT_SKILLS = os.path.join(ROOT, "plugins", "litigation-writing", "skills")


def skill_dir(root, name):
    nested = os.path.join(root, name, name)
    return nested if os.path.isfile(os.path.join(nested, "SKILL.md")) else os.path.join(root, name)


def py(args):
    p = subprocess.run([sys.executable, "-I", "-B"] + args, capture_output=True, text=True, cwd=HERE)
    return p.returncode, p.stdout, p.stderr


def run_checker(skills):
    results = []
    for c in json.load(open(os.path.join(HERE, "cases.json"), encoding="utf-8")):
        script = os.path.join(skill_dir(skills, c["skill"]), "scripts", "litcheck.py")
        args = [script, "check", os.path.join(HERE, "cases", c["draft"]), "--variant", c["variant"],
                "--jurisdiction", c["jurisdiction"], "--json"]
        if c.get("matter"):
            args += ["--matter", os.path.join(HERE, "cases", c["matter"])]
        code, out, err = py(args)
        try:
            data = json.loads(out)
        except ValueError:
            results.append((c["name"], False, "no JSON from litcheck: %s %s" % (out[:200], err[:200])))
            continue
        problems = []
        by_id = {}
        for item in data["checks"]:
            by_id.setdefault(item["id"], []).append(item)
        for rid in c.get("fail", []):
            items = by_id.get(rid, [])
            if not items or all(i["passed"] for i in items):
                problems.append("expected %s to fail" % rid)
        for rid in c.get("pass", []):
            items = by_id.get(rid, [])
            if not items or any(not i["passed"] for i in items):
                problems.append("expected %s to pass" % rid)
        if "passes" in c and data["passed"] != c["passes"]:
            hard = [i["id"] for i in data["checks"] if not i["passed"] and i["severity"] == "hard"]
            problems.append("expected overall %s, got %s (hard failures: %s)" % (c["passes"], data["passed"], ", ".join(hard)))
        for ph in c.get("placeholders", []):
            if ph not in data.get("placeholders", {}):
                problems.append("expected placeholder %s to be listed" % ph)
        results.append((c["name"], not problems, "; ".join(problems)))
    return results


def run_fields(skills):
    results = []
    path = os.path.join(HERE, "fields_cases.json")
    if not os.path.isfile(path):
        return results
    for c in json.load(open(path, encoding="utf-8")):
        script = os.path.join(skill_dir(skills, c["skill"]), "scripts", "litcheck.py")
        code, out, err = py([script, "fields", "--variant", c["variant"], "--jurisdiction", c["jurisdiction"], "--json"])
        try:
            rows = {r["id"]: r["status"] for r in json.loads(out)["fields"]}
        except (ValueError, KeyError):
            results.append((c["name"], False, "no JSON: %s %s" % (out[:200], err[:200])))
            continue
        problems = []
        for fid, want in c.get("expect", {}).items():
            got = rows.get(fid, "-")
            if got != want:
                problems.append("%s: expected %s, got %s" % (fid, want, got))
        results.append((c["name"], not problems, "; ".join(problems)))
    return results


def run_docs(skills):
    results = []
    path = os.path.join(HERE, "doc_checks.json")
    if not os.path.isfile(path):
        return results
    for c in json.load(open(path, encoding="utf-8")):
        names = c.get("skills") or sorted(os.listdir(skills))
        for n in names:
            d = skill_dir(skills, n)
            if not os.path.isfile(os.path.join(d, "SKILL.md")):
                continue
            files = [os.path.join(d, f) for f in c.get("files", ["SKILL.md"])]
            text = ""
            for f in files:
                if os.path.isfile(f):
                    text += open(f, encoding="utf-8").read() + "\n"
            problems = []
            for s in c.get("must", []):
                if not re.search(s, text, re.I):
                    problems.append("missing %r" % s)
            for s in c.get("never", []):
                m = re.search(s, text, re.I)
                if m:
                    problems.append("contains %r" % m.group(0))
            results.append(("%s [%s]" % (c["name"], n), not problems, "; ".join(problems)))
    return results


def run_shared():
    code, out, err = py([os.path.join(ROOT, "tools", "sync_shared.py"), "--check"])
    return [("shared core copies match", code == 0, (out + err).strip().splitlines()[-1] if code else "")]


def main(argv):
    skills = DEFAULT_SKILLS
    if len(argv) == 3 and argv[1] == "--skills":
        skills = argv[2]
    elif len(argv) != 1:
        print(__doc__)
        return 2
    suites = [("checker", run_checker(skills)), ("fields", run_fields(skills)), ("docs", run_docs(skills))]
    if skills == DEFAULT_SKILLS:
        suites.append(("shared", run_shared()))
    total = failed = 0
    for name, results in suites:
        for label, ok, why in results:
            total += 1
            if not ok:
                failed += 1
                print("FAIL %s: %s: %s" % (name, label, why))
        print("%-8s %d of %d passed" % (name, sum(1 for r in results if r[1]), len(results)))
    print("total: %d of %d passed" % (total - failed, total))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
