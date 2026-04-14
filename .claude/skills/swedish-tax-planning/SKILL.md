---
name: swedish-tax-planning
description: >
  Swedish corporate tax planning for AB: periodiseringsfond (IL 30 kap, 25% avsättning, 6-year reversal, schablonintäkt), överavskrivningar (30-regeln/20-regeln, BAS 2150/8850), koncernbidrag (IL 35 kap, >90% ownership), 3:12-reglerna (gränsbelopp, K10, löneunderlag, 2026 reform), ränteavdragsbegränsningar (EBITDA 30%, förenklingsregeln 5 MSEK), kapitalförsäkring (avkastningsskatt, breakeven), and lön-vs-utdelning optimization. Trigger on periodiseringsfond, överavskrivning, koncernbidrag, 3:12, fåmansbolag, gränsbelopp, K10, löneunderlag, ränteavdrag, EBITDA-regeln, kapitalförsäkring, skatteplanering, or tax optimization for Swedish AB. Always use over training data.
---

# Swedish Tax Planning (Skatteplanering AB)

Developer-facing compliance reference for implementing Swedish corporate tax planning tools. Covers the major tax deferral and optimization instruments available to aktiebolag, their interactions, and compliance requirements.

## How to use this skill

This SKILL.md contains the decision framework and key interactions. Detailed rules, calculations, and examples live in `references/`. Read the relevant reference file when you need depth.

### Reference files

| File | When to read |
|---|---|
| `references/periodiseringsfond.md` | Questions about periodiseringsfond avsättning/återföring, IL 30 kap, schablonintäkt, 6-year rule, BAS 2110/8811 |
| `references/overavskrivningar.md` | Questions about 30-regeln/20-regeln, räkenskapsenlig avskrivning, direktavdrag, BAS 2150/8850 |
| `references/koncernbidrag.md` | Questions about koncernbidrag, IL 35 kap, >90% ownership, directions, underskottsspärr, BAS 8820/8830 |
| `references/312-regler.md` | Questions about 3:12, fåmansbolag, kvalificerade andelar, gränsbelopp, K10, löneunderlag, 2026 reform |
| `references/ranteavdragsbegransningar.md` | Questions about ränteavdragsbegränsningar, EBITDA-regeln, förenklingsregeln 5 MSEK, N9, carry-forward |
| `references/kapitalforsakring.md` | Questions about kapitalförsäkring in AB, avkastningsskatt, BAS 1385, when KF beats direktägande |
| `references/strategy-and-interactions.md` | Questions about optimal year-end sequence, lön vs utdelning, interaction matrix, Skatteverket audit triggers |

Read multiple reference files when a question spans domains (common in tax planning).

## Year-end decision sequence (optimal order)

1. **Överavskrivningar** — limited by asset base, calculate first
2. **Periodiseringsfond** — 25% of remaining taxable income
3. **Koncernbidrag** — equalize profits/losses across group
4. **Löneuttag** — verify lönekrav for 3:12 (through inkomstår 2025)
5. **Utdelning** — plan within gränsbelopp
6. **Ränteavdragsbegränsningar** — verify compliance (interactions with steps 2-3)

## Core instruments summary

### Periodiseringsfond (IL 30 kap)
- Max: 25% of skattemässigt överskott
- Up to 6 parallel funds, each reversed within 6 tax years (FIFO)
- Must be booked as obeskattad reserv (formellt samband)
- Schablonintäkt: SLR (min 0.5%) x total funds, reported on INK2S 4.6a
- BAS: 2110-2139 / 8811 (avsättning) / 8819 (återföring)

### Överavskrivningar (IL 18 kap)
- 30-regeln: pool written down to 70% of avskrivningsunderlag (declining balance)
- 20-regeln: 20% straight-line per asset (full in 5 years)
- Choose whichever yields lowest tax book value each year
- Direktavdrag: assets < half PBB (29,400 kr for 2025)
- BAS: 2150 / 8850

### Koncernbidrag (IL 35 kap)
- Transfers taxable income between group companies (>90% ownership)
- Avdragsgillt for giver, skattepliktigt for receiver
- Requires ownership for entire tax year + bolagsstämmobeslut
- BAS: 8820 (mottaget) / 8830 (lämnat)

### 3:12-reglerna (IL 56-57 kap)
- Utdelning within gränsbelopp: 20% effective tax
- Förenklingsregeln: 2.75 x IBB (209,550 kr for inkomstår 2025)
- Huvudregeln: omkostnadsbelopp x (SLR+9%) + lönebaserat utrymme
- K10 must be filed every year to preserve sparat utdelningsutrymme
- **2026 reform**: grundbelopp 4 IBB, lönekrav abolished, 4%-spärr abolished, karenstid 4 years

### Ränteavdragsbegränsningar (IL 24 kap)
- EBITDA-regeln: negativt räntenetto max 30% of skattemässigt EBITDA
- Förenklingsregeln: max 5 MSEK per intressegemenskap (not per bolag)
- Carry-forward 6 years under EBITDA-regeln only
- Key: periodiseringsfond avsättning increases EBITDA (good), koncernbidrag decreases it (bad)

### Kapitalförsäkring
- Sole schablonbeskattad sparform for AB (ISK only for fysiska personer)
- Effective annual tax ~1.065% of kapitalunderlag (at SLR 2.55%)
- Breakeven return vs direktägande: ~5.2%
- Never for näringsbetingade andelar (already skattefria)
- BAS: 1385

## Interaction matrix (critical for year-end optimization)

| Tool A | Affects | How |
|--------|---------|-----|
| Periodiseringsfond avsättning | EBITDA | Increases avdragsunderlag (good) |
| Periodiseringsfond återföring | EBITDA | Decreases avdragsunderlag (bad) |
| Koncernbidrag lämnat | EBITDA | Decreases avdragsunderlag (bad for giver) |
| Överavskrivningar | Periodiseringsfond | Reduces taxable income, lowering max avsättning |
| Löneuttag | 3:12 gränsbelopp | Meets lönekrav AND feeds löneunderlag |

## Lön vs utdelning: effective tax burdens

| Method | Combined burden |
|--------|----------------|
| Utdelning within gränsbelopp | ~36.5% |
| Lön below brytpunkt | ~47-52% |
| Lön above brytpunkt | ~58-63% |
| Utdelning above gränsbelopp | ~52-58% |

Optimal for most fåmansbolagsägare: lön up to pension ceiling (8.07 x IBB), then utdelning within gränsbelopp.

## Obeskattade reserver split

Both periodiseringsfonder and överavskrivningar: ~79.4% equity + ~20.6% latent tax.

## Skatteflyktslagen (1995:575)

Four cumulative conditions: väsentlig skatteförmån, taxpayer participation, tax was predominant reason, contravenes law's purpose. All four must be met.
