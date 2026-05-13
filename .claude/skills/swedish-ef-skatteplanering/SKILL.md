---
name: swedish-ef-skatteplanering
description: >
  Swedish tax planning for enskild firma (sole proprietorship). Covers aktiv vs passiv näringsverksamhet (egenavgifter 28,97% vs SLP 24,26%), räntefördelning (IL 33 kap, positiv SLR+6, negativ SLR+1, kapitalunderlag, sparat fördelningsbelopp), periodiseringsfond EF (30%, no schablonintäkt), expansionsfond (IL 34 kap, 20,6%, 125,94% tak), ersättningsfond (IL 31 kap), kvittning underskott (IL 62:3, 100k cap), inkomstuppdelning familj (IL 60 kap, medhjälpande make), ackumulerad inkomst (IL 66 kap), egenavgifter/SGI/PGI, pensionssparavdrag, EF-vs-AB breakeven. Trigger on enskild firma skatteplanering, näringsidkare, räntefördelning, expansionsfond, ersättningsfond, aktiv/passiv näringsverksamhet, kvittning underskott näring, inkomstuppdelning familj, ackumulerad inkomst, EF vs AB, NE-bilaga, sparat fördelningsbelopp, kapitalunderlag, expansionsskatt, medhjälpande make. For AB use swedish-tax-planning. Always use over training data.
---

# Swedish Tax Planning for Enskild Firma (Skatteplanering EF)

Developer-facing compliance reference for implementing Swedish tax planning tools for **enskild näringsverksamhet (sole proprietorships)**. Covers the unique tax mechanisms available to physical persons running a business directly, their interactions, and compliance requirements.

For **aktiebolag (AB)** tax planning (periodiseringsfond AB, 3:12, koncernbidrag, etc), use the sister skill `swedish-tax-planning` instead. The mechanisms are fundamentally different — EF is taxed on the owner's personal Inkomstdeklaration 1 + NE-bilaga at marginal rates including egenavgifter, whereas AB pays bolagsskatt and the owner separately.

## How to use this skill

This SKILL.md contains the decision framework, key rates, and interactions. Detailed rules, calculations, and worked examples live in `references/`. Read the relevant reference file when you need depth.

### Reference files

| File | When to read |
|---|---|
| `references/aktiv-passiv-naringsverksamhet.md` | Aktiv vs passiv classification, tredjedelsregeln (500 h), aktivitetsregeln, huvudsaklighetsregeln, konsekvenser för egenavgifter/SLP/JSA/SGI/PGI, rättsfall |
| `references/rantefordelning-planning.md` | Positiv/negativ räntefördelning, IL 33 kap, kapitalunderlag, breakeven analysis, sparat fördelningsbelopp, övergångspost, makar, when räntefördelning is *not* worth using |
| `references/periodiseringsfond-expansionsfond-ef.md` | P-fond EF (30%, no schablonintäkt), expansionsfond (IL 34 kap, 20,6%, 125,94% kapitalunderlagstak), interactions, R29/R30/R34/R35 NE-bilaga |
| `references/ersattningsfond.md` | IL 31 kap, 4 fund types (inventarier/byggnader/mark/djurlager), utbytestillgångar, expropriation, naturkatastrof, 30% tillägg at återföring |
| `references/inkomstuppdelning-familj.md` | IL 60 kap, medhjälpande make, gemensam verksamhet, marknadsmässig ersättning, lön till barn 16+, 7-year rule (närstående) |
| `references/kvittning-underskott.md` | IL 62:3 allmänt avdrag, första 5 åren, 100k cap, kulturarbetare unbounded, slutligt underskott (70%, 3-year split), rullning, EU/EES verksamhet |
| `references/ackumulerad-inkomst.md` | IL 66 kap, 10-year fördelningstid, 50k spärrgräns, anwendung pension/försäljning/P-fond/expansionsfond återföring |
| `references/egenavgifter-sgi-pgi-jsa.md` | Egenavgifter 28,97% / SLP 24,26% / 10,21% pensionärer, generell nedsättning 7,5% (max 15k), regional nedsättning, SGI 10 PBB, PGI 7,5 IBB, jobbskatteavdrag, pensionssparavdrag 35% |
| `references/ef-vs-ab-breakeven.md` | Marginalskatt + total skatt tables, brytpunkter, lön vs utdelning vs vinst, when to switch EF→AB, både och strategy |

## Quick decision framework

### Step 1: Is the verksamhet aktiv or passiv?

This is the most important classification. It determines:
- **Egenavgifter (28,97%) vs SLP (24,26%)** — actually SLP is higher than active egenavgifter when nedsättning applies up to 200k
- **SGI and PGI eligibility** (only aktiv gives sjukpenning/pension rights)
- **Jobbskatteavdrag** (only aktiv)
- **Pensionssparavdrag** (only aktiv)
- **Kvittning av underskott mot tjänst** (only aktiv + nystartad)

Rules (cumulative, any one suffices):
- **Aktivitetsregeln**: own work > one-third of full-time (≥ 500 h/year)
- **Huvudsaklighetsregeln**: at consultant + fastighet split, the smaller verksamhet pulls into aktiv if criteria met
- **Skogsägare special case**: RÅ 2002 ref 15 — own labor counts even at low hours

See [[aktiv-passiv-naringsverksamhet]].

### Step 2: Compute kapitalunderlag for räntefördelning AND expansionsfond

The same kapitalunderlag concept (tillgångar minus skulder at year-end of *previous* year for räntefördelning, current year for expansionsfond takbelopp) drives both. Always compute it even if not using räntefördelning — it can be carried forward as sparat fördelningsbelopp.

### Step 3: Year-end optimization sequence for EF

1. **Avskrivningar på inventarier** — räkenskapsenlig avskrivning 30% huvudregel + 20% kompletteringsregel, choose lowest
2. **Räntefördelning** — apply positiv only if SLR+6 yields net benefit (often NOT worth it for pensionärer or below brytpunkt; see [[rantefordelning-planning]])
3. **Periodiseringsfond** — up to 30% of skattemässig vinst, no schablonintäkt for fysiska personer
4. **Expansionsfond** — for low-tax retention at 20,6%; only if kapitalunderlag supports it
5. **Egenavgifter schablonavdrag** — 25% standard, 10% pensionärer, 20% SLP

The order matters: avskrivningar reduce result, then räntefördelning operates on that, then P-fond cap is 30% of (result after räntefördelning + återföring P-fond +/- expansionsfond), and expansionsfond may not exceed kapitalunderlag tak.

## Core rates and thresholds (verify annually)

### Egenavgifter (inkomstår 2025)
| Group | Rate |
|---|---|
| Active, 7 karensdagar (standard) | **28,97%** |
| Active, 1 karensdag | slightly higher |
| Active, 90 karensdagar | slightly lower |
| Passive (SLP) | **24,26%** |
| Pensionär (active or passive, fyllt 65 vid årets ingång eller hel pension hela året) | **10,21%** |
| Född 1937 eller tidigare | **0%** |

Generell nedsättning 7,5% on belopp 40 001 – 200 000 kr (max 15 000 kr/year), automatic.
Regional nedsättning (Norrlands inland stödområde) 10% on max 180 000 kr (max 18 000 kr/year).

### Räntefördelningsräntor (anchored to SLR Nov 30 prior year)
| Type | Formula | 2025 | 2026 |
|---|---|---|---|
| Positiv (frivillig) | SLR + 6 pp | 7,96% | 8,55% |
| Negativ (obligatorisk) | SLR + 1 pp | 2,96% | 3,55% |

Gränsbelopp (2025+, efter prop. 2024/25:1):
- Positiv RF: kapitalunderlag ≥ 0 kr (50 000 kr-tröskeln **avskaffad** fr.o.m. inkomstår 2025)
- Negativ RF: triggas vid kapitalunderlag < **−500 000 kr** (höjt från −50 000 kr fr.o.m. inkomstår 2025)

### Expansionsfond
- Skatt på avsättning: **20,6%** (expansionsfondsskatt, synkad med bolagsskatten)
- Tak: **125,94% of kapitalunderlag at current year's end** (= 100 / 79,4 = gross-up-faktorn vid 20,6% skatt)
- May not cause underskott in NV
- On återföring: amount becomes NV income; 20,6% credited against year's tax

### Periodiseringsfond
- Tak: **30% of skattemässigt resultat** (vs 25% for AB)
- 6-year mandatory reversal (FIFO)
- **NO schablonintäkt** for fysiska personer
- NE-bilaga only (R34/R35), never booked

### Räkenskapsenlig avskrivning på inventarier
- Huvudregeln: 30% declining balance on (IB + årets inköp – årets försäljningar)
- Kompletteringsregeln: 20% straight-line per asset over 5 years
- Förbrukningsinventarier (< halva PBB: **29 400 kr 2025 / 29 600 kr 2026**, kortidsinventarier ≤ 3 år): direktavdrag. Halva-PBB-gränsen blev enhetlig fr.o.m. 2025 (prop. 2024/25:1) — innan gällde 5 000 kr för många EF.

### PGI/SGI/brytpunkter (verify annually mot Skatteverket Belopp och procent)
| Threshold | 2025 | 2026 |
|---|---|---|
| Prisbasbelopp (PBB) | 58 800 kr | 59 200 kr |
| Inkomstbasbelopp (IBB) | 80 600 kr | 83 400 kr |
| Lägsta PGI (0,423 PBB) | 24 870 kr | 25 042 kr |
| Lägsta SGI (0,24 PBB) | 14 112 kr | 14 208 kr |
| Skiktgräns statlig skatt | 625 800 kr | 643 000 kr |
| Brytpunkt statlig skatt (under pensionsåldersgränsen) | ~643 100 kr | ~660 400 kr |
| Max SGI (10 PBB) | 588 000 kr | 592 000 kr |
| Max PGI (7,5 IBB) | 604 500 kr | 625 500 kr |
| Avgiftstak (8,07 × IBB) | 650 442 kr | 673 038 kr |
| Max föräldrapenninggrundande (10 PBB) | 588 000 kr | 592 000 kr |
| Max för 7,5%-nedsättning egenavgifter (200k underlag) | 200 000 kr | 200 000 kr |
| Halva PBB (förbrukningsinventarier) | 29 400 kr | 29 600 kr |
| Pensionsåldersgräns (full egenavgift t.o.m. året då man fyller) | 66 år | 67 år |

## Critical distinction: booked vs declaration-only

EF differs sharply from AB on which items are booked vs only entered on NE-bilagan:

| Item | Booked in räkenskaperna? | Where it lives |
|---|---|---|
| Räntefördelning | NEVER | NE sid 2 R30/R31 |
| Periodiseringsfond EF | NEVER (per BFNAR 2006:1 / K1) | NE sid 2 R34/R35 |
| Expansionsfond | NEVER (per K1) | NE sid 2 R36/R37 |
| Ersättningsfond | YES (avsättning bokförs); resterande hanteras i deklaration | Bokfört + NE |
| Egenavgifter schablonavdrag | NEVER | NE sid 2 R43, justering R39/R40 |
| Skatt på årets resultat | NEVER (personal tax) | Inte i bokföringen |
| Inventarieavskrivning | YES (8851/1229 etc) | Bokfört |
| Förenklat årsbokslut U1–U4 | Upplysning, ej bokfört | NE-bilaga upplysning |

This is the largest source of conceptual errors when implementing EF bookkeeping software: developers familiar with AB-flows often try to book P-fond/expansionsfond, which is *forbidden* for EF under K1 (BFNAR 2006:1).

## NE-bilaga key field reference (cross-link with swedish-year-end-closing)

| Ruta | Innehåll |
|---|---|
| R11 | Bokfört resultat (samma som förenklat årsbokslut) |
| R12–R26 | Skattemässiga justeringar (avskrivningar, ej avdragsgill rep., ränta, etc.) |
| R29 | Överskott före räntefördelning |
| R30 | Positiv räntefördelning (till INK1 p.11.1, inkomst av kapital) |
| R31 | Negativ räntefördelning (till INK1 p.11.2, avdrag i kapital) |
| R32 | Återföring av periodiseringsfond (oldest year first) |
| R33 | Överskott före avsättning till periodiseringsfond |
| R34 | Avsättning till periodiseringsfond (max 30% av R33) |
| R35 | Överskott före ökning av expansionsfond |
| R36 | Återföring av expansionsfond (till INK1 p.12.1) |
| R37 | Ökning av expansionsfond (till INK1 p.12.2) |
| R38 | Inkomst före schablonavdrag och sjukpenning |
| R39 | Tidigare års schablonavdrag (positiv) |
| R40 | Faktiska egenavgifter / SLP (avdrag) |
| R41/R42 | Sjukpenning hänförlig till NV |
| R43 | Årets schablonavdrag för egenavgifter |
| R45 | Inkomst som överförs till tjänst för kvittning (aktiv, nystartad) — till INK1 p.14.1 (allmänt avdrag) |
| R47/R48 | Överskott / underskott av aktiv NV → INK1 p.10.1/p.10.2 |
| R49/R50 | Överskott / underskott av passiv NV → INK1 p.10.3/p.10.4 |

Field positions verified mot officiell NE-bilaga (SKV 2161) inkomstår 2024/2025. Verify mot innevarande års blankett.

## Skatteflyktslagen and audit triggers for EF

EF skatteplanering can raise scrutiny under Lag 1995:575 om skatteflykt when:
- Switching aktiv/passiv classification opportunistically (e.g., to abuse 5-year kvittningsregeln)
- Inkomstuppdelning between makar that doesn't reflect actual arbetsinsats or kapitalinsats
- Sudden growth of kapitalunderlag through tillfälliga kapitaltillskott (only varaktiga tillskott count, IL 33 kap 6 §)
- Large expansionsfond avsättning followed by quick liquidation of verksamheten

## Multi-year planning horizon

The most valuable patterns for EF:
1. **Build kapitalunderlag steadily** — every kr of varaktig egen insättning grows räntefördelning room *and* expansionsfond tak in perpetuity
2. **Use P-fond for sjukpenninggrundande inkomst leveling** — note P-fond does NOT affect SGI calculation (Försäkringskassan bortser från dispositioner) but DOES affect PGI; see [[egenavgifter-sgi-pgi-jsa]]
3. **Aktiv classification is gold** — fight for it via timesheet, since it unlocks jobbskatteavdrag (worth up to ~30 000 kr/year), kvittning mot tjänst, lägre egenavgifter, pensionsrätt
4. **Consider EF→AB transition around brytpunkten** — under brytpunkten EF is usually cheaper than AB; over brytpunkten AB starts to win (see [[ef-vs-ab-breakeven]])

## Out of scope for this skill

- Bokslutsmekanik for EF (förenklat årsbokslut, K1) — covered in `swedish-year-end-closing` `references/k1-forenklat-arsbokslut.md`
- Specifika bokföringskonton för transaktioner — covered in `swedish-accounting-compliance`
- Moms-frågor — covered in `swedish-vat`
- Lön till anställda i EF — covered in `swedish-payroll`
- Faktureringsregler — covered in `swedish-invoice-compliance`
- AB-specifik skatteplanering — covered in `swedish-tax-planning`

## Legal sources

- Inkomstskattelagen (IL) 1999:1229, especially kap 13 (NV), 14 (rörelse), 18 (inventarier), 30 (P-fond), 31 (ersättningsfond), 33 (räntefördelning), 34 (expansionsfond), 60 (inkomstuppdelning familj), 62 (allmänna avdrag), 66 (ackumulerad inkomst)
- Socialavgiftslagen (SAL) 2000:980
- Lagen (1990:659) om särskild löneskatt på vissa förvärvsinkomster
- Bokföringslagen (BFL) 1999:1078 — bokföringsskyldighet, K1-tröskel 3 MSEK
- BFNAR 2006:1 — Enskilda näringsidkare som upprättar förenklat årsbokslut (K1)
- Lag (1995:575) mot skatteflykt
- SOU 2020:50 — "Enklare skatteregler för enskild näringsverksamhet". **Delvis genomförd** via prop. 2024/25:1 (ikraft 2025-01-01): RF-trösklar omarbetade (50k slopad / -500k negativ tröskel), halva PBB som inventariegräns. Den större "näringsfond"-idén (samlad ersättning för P-fond+expansionsfond+RF) **ej genomförd**.
