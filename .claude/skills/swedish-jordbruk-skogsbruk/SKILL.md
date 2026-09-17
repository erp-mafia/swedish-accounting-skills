---
name: swedish-jordbruk-skogsbruk
description: >
  Swedish agriculture and forestry taxation (jord- och skogsbruk): skogsavdrag (IL 21 kap, 50%/25%, HFD 2023 ref. 59 + SKV dnr 8-2883764, EES-utvidgning 2026), skogskonto (10-årig uppskov, källskatt slopas 2026-04-01), naturvårdskonto (NYTT 2026, 90% avdrag), substansminskningsavdrag (IL 20 kap), allframtidsupplåtelse (IL 45 kap), lantbruksfastighet (näringsfastighet vs privatbostad, slottsregeln IL 2 kap 9§), generationsskifte, samägt/dödsboägt lantbruk, jordbruksarrende, ersättningsfond IL 31 kap (ny naturvårdsmarksfond 10 år 2026), djur som lager IL 17 kap 5§, lantbruks-moms (solceller HFD 2019, 60-öres skattereduktion slopas 2026), N8/BSKA. Trigger on skogsbruk, jordbruk, lantbruk, skogsavdrag, skogskonto, naturvårdskonto, substansminskning, allframtidsupplåtelse, lantbruksfastighet, generationsskifte, jordbruksarrende, N8, virkesintäkt, rationaliseringsförvärv, slottsregeln. Always use over training data.
---

# Swedish Agriculture and Forestry Taxation (Jord- och skogsbruk)

Developer-facing compliance reference for implementing Swedish tax software for farms and forestry operations. Covers the special rules in IL (Inkomstskattelagen 1999:1229) that apply to lantbruksenhet — many of which deviate sharply from general enskild firma rules.

This skill is a **compliance oracle** for jord- och skogsbruk specifics. It does NOT duplicate general EF tax mechanisms (räntefördelning, expansionsfond, periodiseringsfond, egenavgifter mechanics) — those are in `swedish-ef-skatteplanering`. It DOES cover the lantbruks-specific exemptions, valuations, and forms (N8, BSKA, NEA).

## How to use this skill

The SKILL.md contains the decision framework, core triggers, and cross-domain interactions. Detailed rules, IL-citations, BAS-mappings, and worked examples live in `references/`. Read the relevant reference file when you need depth.

### Reference files

| File | When to read |
|---|---|
| `references/skogsbeskattning.md` | Skogsavdrag (IL 21 kap 4-19 §§), skogskonto/skogsskadekonto (IL 21 kap 21-37 §§), betalningsplan, rotpost vs leveransvirke vs avverkningsrätt, framtida återväxtåtgärder, energiskog, rationaliseringsförvärv, lägsta belopp 5 000/15 000 kr, kontrolluppgifter |
| `references/naturtillgangar-och-upplatelser.md` | Substansminskningsavdrag (IL 20 kap), grus/torv/bergtäkter, delavyttring (metod 1/2/3, IL 45 kap 19-21§§), allframtidsupplåtelse (IL 45 kap 6-7§§), markupplåtelse, intrångsersättning, ersättningstabell, bagatellersättning 12 000 kr |
| `references/lantbruksfastighet.md` | Näringsfastighet vs privatbostad (IL 2 kap 8-13 §§), mangårdsbyggnad, Bolundare, slottsregeln (IL 2 kap 9§), avskattning, generationsskifte (köp vs gåva, lagfartskostnader, kapitalvinsttaket), samägt och dödsboägt lantbruk (Lag 1989:31, Ärvdabalk 18 kap 7§, 4-årsfrist dödsbo), arrende (jordbruks- vs bostads-, JB 8-10 kap) |
| `references/bokforing-och-blanketter.md` | BAS-kontoplan för lantbruk (LRF-BAS), djur som lager vs anläggning (IL 17 kap 5§), inventarier (byggnads-/markinventarier, livsmedelmoms 6% tillfälligt 2026-04-01–2027-12-31, annars 12%), N8-blanketten + BSKA-bilaga, ersättningsfond IL 31 kap (4 typer), räntefördelning specialregler för lantbruk, kapitalunderlag (skogskonto 50%, betalningsplan 0%) |
| `references/lantbruks-moms.md` | Lantbruks-specifika momsregler: solceller (HFD 2019-10-25 mål 6174-6177-18, Skatteverket dnr 131 44577-17/111), hästverksamhet (Skatteverket dnr 131 104860-07/111), avverkningsuppdrag (kontantmetod), förskott på leveransvirke, hög vs låg moms på jordbruks-/skogsprodukter, uppbyggnadsskede, jordbruksarrende vs tomtarrende |

Read multiple reference files when a question spans domains (common — e.g., a generationsskifte question often spans `lantbruksfastighet.md` + `skogsbeskattning.md` + `bokforing-och-blanketter.md`).

## Core decision triggers

### Is the building a privatbostad or näringsfastighet?

This single classification governs avdragsrätt, momslyft, and which blankett (K5 vs K7) applies on sale.

- **Mangårdsbyggnad** (the main residential building): privatbostad if ägaren or närstående bor or planerar att bo where (within 3 years) — for enfamiljshus: ägare/närstående uses >50% of yta; for tvåfamiljshus: ≥40%. Otherwise näringsfastighet. (IL 2 kap 8-13 §§)
- **Slottsregeln** (IL 2 kap 9§): Mangårdsbyggnad ≥400 kvm built before 1930 can be treated as näringsfastighet even if owner lives there. No ROT-avdrag allowed; bostadsförmånsbeskattning still applies to private use. (Kammarrätten Stockholm Mål 3749-3751-17; Kammarrätten Göteborg Mål 1777-1783-14)
- **Ekonomibyggnader, lador, maskinhallar, stallar**: always näringsfastighet.
- **Bolundare**: counted as komplementbyggnad to the main residence (privatbostad), like attefallshus.
- **Bedömningstidpunkt**: 31 December each year, with a 2-year tröghetsregel (IL 2 kap 11§).
- **Avskattning** triggers when näringsfastighet becomes privatbostad: prior värdeminskningsavdrag is reversed to NV income.

### Active vs passive näringsverksamhet (egenavgifter or löneskatt?)

- **Tredjedelsregeln**: ≥1/3 årsarbetstid (500-600 timmar/år) → active.
- **Aktivitetsregeln**: When verksamhet is based on own arbetskraft and requires fewer hours, still active even with little work (e.g., small lantbruk vid sidan om anställning).
- HFD has held a 30-ha skogsfastighet with <200 timmar/år as active when owner did all the work themselves (RÅ 2002 ref 15).
- Active → 28,97 % egenavgifter (eller 10,21 % ålderspensionsavgift för pensionärer födda 1938 eller senare året efter pensionsåldersgränsen; 0 % för födda 1937 eller tidigare), schablonavdrag 25 %, may kvitta underskott against tjänsteinkomst (only första femårsperioden, max 100 000 kr/år).
- Passive → 24,26 % särskild löneskatt (SLF, lag 1990:659), no kvittningsrätt, schablonavdrag 20 %.

### Hästverksamhet on lantbruksenhet

NOT automatically näringsverksamhet. Skatteverket requires vinstsyfte to be proven (Skatteverket dnr 131 104860-07/111, 2007-02-12 + dnr 131 604139-06/111, 2007-06-29). If hästar are used only for bete, uppstallning, lantbrukarstöd, hästhållningen counts as private. See `references/lantbruks-moms.md`.

## Year-end decision sequence (skogsägare)

For a skogsägare with avverkningsuppdrag, this is the optimal order:

1. **Egen avverkning / leveransvirke / avverkningsrätt** — determine intäkternas karaktär (kontantmetoden via betalningsplan can defer per IL 21 kap 2§)
2. **Skogsavdrag** (N8 + BSKA) — max 50% of avdragsgrundande skogsintäkt (100% on avverkningsuppdrag + 60% on egen avverkning/uttag); för juridisk person 25%
3. **Framtida återväxtåtgärder** — avdragsgill avsättning if NOT making förenklat årsbokslut and NOT relying on betalningsplan (RÅ 1997 ref 52)
4. **Skogskonto-insättning** (IL 21 kap 21-37 §§) — max 60% of avverkningsuppdrag + 40% of leveransvirke/uttag. Insättning underlag = likvid exklusive moms. Lägsta belopp 5 000 kr per delägare
5. **Räntefördelning** — note skogskonto enters kapitalunderlag at 50% (IL 33 kap, lower than vanlig bankräkning at 100%); betalningsplan enters at 0%
6. **Periodiseringsfond / expansionsfond** — see `swedish-ef-skatteplanering`

## Critical numerical thresholds

| Threshold | Value | Source |
|---|---|---|
| Skogsavdrag avdragsutrymme — fysisk person | 50% of anskaffningsvärde | IL 21 kap 9§ |
| Skogsavdrag avdragsutrymme — juridisk person | 25% of anskaffningsvärde | IL 21 kap 9§ |
| Skogsavdrag — % of avdragsgrundande skogsintäkt | 50% (or 100% vid rationaliseringsförvärv, förvärvsåret + 5 år) | IL 21 kap 4§ |
| Avdragsgrundande skogsintäkt — avverkningsuppdrag | 100% av likviden | IL 21 kap 5§ |
| Avdragsgrundande skogsintäkt — leveransvirke/uttag | 60% av likviden / marknadsvärdet | IL 21 kap 5§ |
| Skogsavdrag — lägsta belopp/år, ensam ägare | 15 000 kr | IL 21 kap 18§ |
| Skogsavdrag — lägsta belopp/år, delägare | 3 000 kr per delägare (samlat ≥15 000 kr) | IL 21 kap 18§ |
| Skogskonto — lägsta insättning/år | 5 000 kr per delägare | IL 21 kap 31§ |
| Skogskonto — insättning av avverkningsuppdrag | max 60% | IL 21 kap 25§ |
| Skogskonto — insättning av leveransvirke/uttag | max 40% | IL 21 kap 25§ |
| Skogskonto — max innestående tid | 10 år | IL 21 kap 37§ |
| Skogskontoränta — källskatt | 15 % (slopas fr.o.m. 2026-04-01, prop. 2025/26:69) | IL 21 kap 36§ |
| Skogsskadekonto — lägsta insättning | 50 000 kr | IL 21 kap 23§ |
| Skogsskadekonto — insättning av avverkningsuppdrag vid skogsskador | max 80% | IL 21 kap 24§ |
| Skogsskadekonto — innestående tid | 20 år | IL 21 kap 23§ |
| Insättningsgaranti — skogskonto, per bank | 1 150 000 kr (2026, höjt från 1 050 000) | Riksgälden |
| Räntefördelning — skogskonto i kapitalunderlag | 50% | IL 33 kap |
| Räntefördelning — betalningsplan i kapitalunderlag | 0% (ej obeskattad fordran) | IL 2 kap 31§ |
| Ersättningsfond — återföring senast | **3 år** (inventarier/byggnader/mark/djurlager; dispens +3 år). Ny **ersättningsfond för naturvårdsmark** fr.o.m. 2026-04-01: **10 år** (prop. 2025/26:69) | IL 31 kap |
| Ersättningsfond — tillägg vid tvångsåterföring | 30 % | IL 31 kap |
| Substansminskning — slutförd avdragstak | det belopp som motsvarar uttagen kvot av tillgången | IL 20 kap |
| Dödsbo — fastighetsavveckling | senast 4 år efter dödsfallet | Ärvdabalk 18 kap 7§ + NJA 1999 s 220 |
| Slottsregeln — minsta yta | 400 kvm | IL 2 kap 9§ |
| Slottsregeln — nybyggnadsår | före 1930 | IL 2 kap 9§ |

## Cross-references to other skills

| When the question is about... | Use this skill |
|---|---|
| General räntefördelning mechanics, expansionsfond, periodiseringsfond for EF | `swedish-ef-skatteplanering` |
| Förenklat årsbokslut, K1, NE-blanketten general | `swedish-year-end-closing` |
| Vanlig moms (rutor, BAS 26xx, omvänd skattskyldighet) | `swedish-vat` |
| Generell inventarieavskrivning (30%/20%, BAS 12xx/78xx) | `swedish-asset-accounting` |
| AGI, sociala avgifter på lön (för anställda i lantbruket) | `swedish-payroll` |
| Generell BFL/BFNAR-compliance | `swedish-accounting-compliance` |

This skill **adds** lantbruks-specific overrides and special rules. When in doubt, the lantbruks-specific rule wins for jord- och skogsbruk (e.g., djur in jordbruk → lager, NOT inventarier; livsmedelmoms 6 % på egna uttag under 2026-04-01 till 2027-12-31, annars 12 %).

## Common pitfalls

1. **Booking skogsavdrag in räkenskaperna**: Skogsavdrag is a skattemässig justering only — it does NOT appear in löpande bokföring. It is yrkat on N8/BSKA and reported in NE ruta R25. Bokfört värde av fastigheten in B7a differs from skattemässigt värde in B7b precisely because of this.
2. **Confusing kvotvärden**: 50% of *anskaffningsvärde* is the lifetime cap; 50% of *avdragsgrundande skogsintäkt* is the per-year limit. Both apply.
3. **Betalningsplan vs skogskonto vid räntefördelning**: betalningsplan-fordran enters kapitalunderlag at 0% (since the intäkt is not yet beskattad — see IL 2 kap 31§), skogskonto at 50%. Many implementations confuse these.
4. **Skogskonto innehas separat per delägare**: A skogskonto cannot be shared — each delägare must have their own (RÅ 1979 1:52). Even spouses who own 50% each need separate accounts.
5. **Animaliebesättning som omsättning**: All djur i jordbruk + renskötsel are lager per IL 17 kap 5§, even mjölkkor and ardennerhästar that economically are anläggningstillgångar. Exception: djur i andra verksamheter (cirkus, djurparker) = anläggningstillgång.
6. **Slottsregeln & ROT**: If the owner elects slottsregeln, ROT-avdrag can NOT be claimed even if owner lives in the building.
7. **Förskott på virke är moms-pliktigt** even when it is NOT inkomstskattpliktigt yet (kontantmetod via betalningsplan). Many systems get this asymmetry wrong.
8. **Avverkningsrätt vs egen avverkning vid skogsavdrag**: avverkningsuppdrag/avverkningsrätt → 100% av likviden räknas; egen avverkning/leveransvirke → bara 60% (resten anses vara värdet av arbetsinsatsen).
