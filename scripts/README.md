# scripts

## check_skills.py

Structural checks for the skills. Run locally with `python3 scripts/check_skills.py`, and in CI on every pull request that touches `.claude/skills/`.

It checks four things, all mechanical:

1. **Frontmatter** parses, `name` matches the directory, `description` is present, at most 1024 characters, and free of `<` and `>` (both break the claude.ai import).
2. **Reference links** in `SKILL.md` resolve to a file that exists. Pointers to another skill's reference are ignored.
3. **BAS accounts** written in bold (`**1930**`) exist in the BAS 2026 chart (`data/bas-2026-accounts.json`, generated from BAS's own published account list). Deliberate exceptions, such as a passage explaining that an account does *not* exist, go in `data/account-exceptions.json`.
4. **Contents index** on reference files over 100 lines, since Claude may preview a long file with `head -100`.

What it does not check: whether the accounting is correct. Facts still need a source and a reviewer.
