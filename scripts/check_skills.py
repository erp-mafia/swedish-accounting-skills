#!/usr/bin/env python3
"""Structural checks for the skills in .claude/skills.

Checks (all mechanical, no judgement):
  1. frontmatter parses, name matches the directory, description within limits
  2. references/*.md linked from SKILL.md exist
  3. bold BAS account numbers (**1930**) exist in the BAS 2026 chart
  4. reference files over 100 lines carry a contents index

Run: python3 scripts/check_skills.py
"""
import json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS = os.path.join(ROOT, ".claude", "skills")
BAS = json.load(open(os.path.join(ROOT, "data", "bas-2026-accounts.json"), encoding="utf-8"))
ALLOW = json.load(open(os.path.join(ROOT, "data", "account-exceptions.json"), encoding="utf-8"))
DESC_MAX = 1024          # claude.ai import limit
TOC_MIN_LINES = 100      # Claude may preview a file with head -100

def frontmatter(text):
    m = re.match(r"\A---\n(.*?)\n---", text, re.S)
    if not m:
        return None, "no frontmatter"
    try:
        import yaml
        return yaml.safe_load(m.group(1)), None
    except ImportError:
        d = re.search(r"^description:[ \t]*[>|]?[ \t]*\n((?:[ \t]+.*(?:\n|$))+)|^description:[ \t]*(.+)$",
                      m.group(1), re.M)
        if not d:
            return None, "no description"
        raw = d.group(1) or d.group(2)
        return {"description": " ".join(x.strip() for x in raw.splitlines()).strip()}, None
    except Exception as e:  # yaml present but invalid
        return None, f"frontmatter is not valid YAML: {e}"

def main():
    errors = []
    skills = sorted(d for d in os.listdir(SKILLS) if os.path.isdir(os.path.join(SKILLS, d)))
    for skill in skills:
        sdir = os.path.join(SKILLS, skill)
        spath = os.path.join(sdir, "SKILL.md")
        if not os.path.exists(spath):
            errors.append(f"{skill}: no SKILL.md")
            continue
        text = open(spath, encoding="utf-8").read()
        fm, err = frontmatter(text)
        if err:
            errors.append(f"{skill}: {err}")
        else:
            name = fm.get("name")
            if name and name != skill:
                errors.append(f"{skill}: frontmatter name is '{name}'")
            desc = str(fm.get("description", ""))
            if not desc:
                errors.append(f"{skill}: empty description")
            if len(desc) > DESC_MAX:
                errors.append(f"{skill}: description {len(desc)} chars, limit {DESC_MAX}")
            if re.search(r"[<>]", desc):
                errors.append(f"{skill}: description contains < or >")

        # referenced files exist (skip pointers that name another skill)
        for ref in sorted(set(re.findall(r"`?references/([a-z0-9-]+\.md)`?", text))):
            line = next((l for l in text.splitlines() if ref in l), "")
            if re.search(r"swedish-[a-z-]+`?[,\s]*\(?`?references/" + re.escape(ref), line):
                continue  # cross-skill pointer
            if not os.path.exists(os.path.join(sdir, "references", ref)):
                errors.append(f"{skill}: SKILL.md links missing references/{ref}")

        # BAS accounts and contents index
        for path in [spath] + sorted(
                os.path.join(sdir, "references", f)
                for f in os.listdir(os.path.join(sdir, "references"))
                if f.endswith(".md")) if os.path.isdir(os.path.join(sdir, "references")) else [spath]:
            body = open(path, encoding="utf-8").read()
            rel = os.path.relpath(path, ROOT)
            allowed = set(ALLOW.get("global", [])) | set(ALLOW.get(rel, []))
            for acct in sorted({m.group(1) for m in re.finditer(r"\*\*([1-8]\d{3})\*\*", body)}):
                if acct in BAS or acct in allowed or 2015 <= int(acct) <= 2030:
                    continue
                errors.append(f"{rel}: **{acct}** is not a BAS 2026 account")
            if path != spath and len(body.splitlines()) > TOC_MIN_LINES:
                if "<!-- toc -->" not in body and not re.search(
                        r"^##+ *(Table of Contents|Contents|Innehåll)", body, re.M | re.I):
                    errors.append(f"{rel}: over {TOC_MIN_LINES} lines without a contents index")

    print(f"checked {len(skills)} skills")
    if errors:
        print(f"\n{len(errors)} problem(s):")
        for e in errors:
            print(f"  - {e}")
        return 1
    print("all checks passed")
    return 0

if __name__ == "__main__":
    sys.exit(main())
