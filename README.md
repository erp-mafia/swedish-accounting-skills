# swedish-accounting-skills

Claude skills for Swedish accounting compliance. These skills give Claude deep knowledge of Swedish bookkeeping law, tax rules, and reporting requirements, useful for any developer building accounting software targeting Sweden, or anyone doing their own bookkeeping.

## Skills

| Skill | Description |
|-------|-------------|
| `swedish-accounting-compliance` | BFL, BFNAR, BAS kontoplan, K2/K3, verifikationer, bokforingsskyldighet |
| `swedish-asset-accounting` | Anlaggningsredovisning, planenlig/overavskrivning, BAS 10xx-12xx/78xx |
| `swedish-financial-reporting` | Arsredovisning, Bolagsverket filing, INK2/INK2R/INK2S, noter |
| `swedish-invoice-compliance` | ML 17 kap 24ss, kreditfaktura, Peppol BIS 3.0, ROT/RUT, reverse charge |
| `swedish-payroll` | AGI, sociala avgifter, skattetabeller, formansbeskattning, BAS 7xxx |
| `swedish-sie-import-export` | SIE4 parsing, validation, generation, encoding (CP437/UTF-8) |
| `swedish-sru-filing` | SRU file generation for Skatteverket (INFO.SRU + BLANKETTER.SRU) |
| `swedish-tax-planning` | Periodiseringsfond, overavskrivningar, koncernbidrag, 3:12-regler |
| `swedish-vat` | Momsdeklaration rutor, EU VAT, reverse charge, BAS 26xx, ML 2023:200 |
| `swedish-year-end-closing` | Bokslut for AB/EF, bokslutstransaktioner, tax provisions, filing |

## Usage

Clone this repo and the skills will be available in Claude Code when working inside the directory:

```bash
git clone https://github.com/erp-mafia/swedish-accounting-agents.git
cd swedish-accounting-agents
claude
```

Or add the skills to an existing project by copying `.claude/skills/swedish-*` into your project's `.claude/skills/` directory.

**Claude Desktop & claude.ai**
Go to **Settings > Customize** or **Settings > Capabilities > Skills** and add the skill files there. Claude will use them across conversations. Requires code execution to be enabled under Settings > Capabilities.

## Note on skill naming

These are **community-maintained** skills, not official Anthropic skills. Claude Code treats the `anthropic-skills:` prefix as Anthropic-maintained — do not rename these skills with that prefix, as Claude may refuse to modify them or treat them with undue authority.

## Skill description limits

Claude Code enforces a **max 1024 characters** for the `description` field in `SKILL.md` frontmatter. Skills exceeding this limit will fail to import. Keep descriptions concise — detailed trigger keywords and coverage belong in the skill body and reference files, not the description.

## License

AGPL-3.0-or-later
