#!/usr/bin/env python3
"""Copy the shared core into every skill, then fail if any copy differs from its source.

    python3 tools/sync_shared.py            copy shared/ into the skills, then verify
    python3 tools/sync_shared.py --check    verify only; change nothing

shared/scripts/litcheck.py              -> <skill>/scripts/litcheck.py
shared/references/*.md                  -> <skill>/references/*.md
shared/references/jurisdictions/*.md    -> <skill>/references/jurisdictions/*.md
shared/assets/*.json                    -> <skill>/assets/*.json

for all six skills. Edit the file in shared/, never a copy: each skill carries its own copy
because a skill is installed and loaded on its own and must work without the others. A copy
whose source has been deleted from shared/ is reported as stale. Exit status 0 when every copy
matches, 1 otherwise, 2 on a usage error. Standard library only.
"""

import filecmp
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SHARED = os.path.join(ROOT, "shared")
SKILLS_DIR = os.path.join(ROOT, "plugins", "litigation-writing", "skills")
SKILLS = ["litigation-writing", "litigation-pleadings", "litigation-evidence", "litigation-submissions",
          "litigation-advice", "litigation-correspondence"]
# (folder in shared/, folder in the skill, file suffix)
SETS = [("scripts", "scripts", ".py"), ("references", "references", ".md"),
        ("references/jurisdictions", "references/jurisdictions", ".md"), ("assets", "assets", ".json")]


def shared_files():
    out = []
    for src_dir, dst_dir, suffix in SETS:
        d = os.path.join(SHARED, src_dir)
        if not os.path.isdir(d):
            continue
        for f in sorted(os.listdir(d)):
            if f.endswith(suffix) and os.path.isfile(os.path.join(d, f)):
                out.append((os.path.join(d, f), os.path.join(dst_dir, f)))
    return out


def main(argv):
    if len(argv) > 2 or (len(argv) == 2 and argv[1] != "--check"):
        print(__doc__)
        return 2
    check_only = len(argv) == 2
    files = shared_files()
    if not files:
        print("no shared files found under %s" % SHARED)
        return 1
    copied, bad = 0, []
    for skill in SKILLS:
        sdir = os.path.join(SKILLS_DIR, skill)
        if not os.path.isfile(os.path.join(sdir, "SKILL.md")):
            bad.append("%s has no SKILL.md" % skill)
            continue
        for src, rel in files:
            dst = os.path.join(sdir, rel)
            if not check_only and not (os.path.isfile(dst) and filecmp.cmp(src, dst, shallow=False)):
                os.makedirs(os.path.dirname(dst), exist_ok=True)
                shutil.copyfile(src, dst)
                copied += 1
            if not (os.path.isfile(dst) and filecmp.cmp(src, dst, shallow=False)):
                bad.append("differs from shared/: %s/%s" % (skill, rel))
        shared_names = {rel for _, rel in files}
        for src_dir, dst_dir, suffix in SETS:
            d = os.path.join(sdir, dst_dir)
            if not os.path.isdir(d) or dst_dir == "references":
                continue
            for f in os.listdir(d):
                rel = os.path.join(dst_dir, f)
                if f.endswith(suffix) and rel not in shared_names:
                    bad.append("stale copy, no longer in shared/: %s/%s" % (skill, rel))
    for b in bad:
        print(b)
    total = len(files) * len(SKILLS)
    print("%s%d of %d copies match shared/" % ("" if check_only else "copied %d; " % copied,
                                                total - len([b for b in bad if b.startswith("differs")]), total))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
