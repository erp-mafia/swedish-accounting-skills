# Räntefördelning — Planning Reference for Enskild Firma

## Legal basis

- IL 33 kap (Räntefördelning) — full chapter
- IL 33 kap 2 § — applies to enskilda näringsidkare and svenska dödsbon
- IL 33 kap 3 § — gränsbelopp ±50 000 kr
- IL 33 kap 6 § — positiv räntefördelning frivillig
- Prop 1993/94:50 sid 427 — introduced the system

## The fundamental idea

Räntefördelning shifts a *schablon* return on the kapital insatt i verksamheten from inkomstslaget näringsverksamhet (taxed at marginal rates up to ~65% inclusive of egenavgifter) to inkomstslaget kapital (flat 30%). It's a paper allocation only — no money moves.

The intent (1994 reform): align tax treatment of capital invested in EF with capital invested in AB (where a näringsidkare can lend money to the AB and get marknadsmässig ränta taxed at 30% in kapital).

### Positiv räntefördelning (frivillig)

- Kapitalunderlag > **+50 000 kr** at föregående års utgång
- Rate: **SLR + 6 procentenheter**
- Effect: deduct kapitalunderlag × rate from NV income, add same amount as kapitalinkomst (30% tax)

### Negativ räntefördelning (obligatorisk)

- Kapitalunderlag < **−50 000 kr** at föregående års utgång
- Rate: **SLR + 1 procentenhet**
- Effect: add belopp to NV income, deduct same as kapitalkostnad (30% skattereduktion)
- **Cannot be skipped** — it is obligatorisk per IL 33 kap

If kapitalunderlag is between −50 000 and +50 000 kr → **no räntefördelning at all** (absolute, not marginal — if you're at +50 001 you do räntefördelning on the *entire* 50 001 belopp, not on the 1 kr över gränsen).

## Rates by year

Anchored to statslåneräntan (SLR) 30 november the year before income year.

| Inkomstår | SLR Nov 30 prior year | Positiv rate (SLR+6) | Negativ rate (SLR+1) |
|---|---|---|---|
| 2021 | 0,23% | 6,5% | 1,5% (effektivt 1,51%) |
| 2024 | (verify) | ~8% | ~3% |
| 2025 | 1,96% | **7,96%** | **2,96%** |
| 2026 | 2,55% | **8,55%** | **3,55%** |

SLR may not go below 0,5% as floor (same floor as för schablonintäkt on P-fond AB).

## When is positiv räntefördelning *worth* doing?

This is the most consequential planning question, and the answer is "less often than people think". From the PDF:

> *"Idag är det inte så säkert att skatt inklusive egenavgifter överstiger 30 procent, som är kapitalskatten på positivt räntefördelningsbelopp."*

### Decision tree

1. **Pensionärer (≥65 år, full pension hela året)**: Egenavgifter only 10,21%; combined skatt ofta UNDER 30%. → DO NOT räntefördela. Räntefördelning *increases* total skatt for pensionärer in most income brackets.
2. **Under 65, under brytpunkten**: Marginalskatt ~46% inkl egenavgifter. Räntefördelning skattereduktion = (46% − 30%) ≈ 16 procentenheter. Small benefit, but pensions- och sjukpenninggrundande inkomst minskar. → MAYBE NOT worth it for low income; weigh against förlorad SGI/PGI.
3. **Under 65, över brytpunkten**: Marginalskatt 52–65% inkl statlig och egenavgifter. Räntefördelning saves ~22–35 pp. → DO IT.

### Worked examples (from PDF)

#### Astrid, född 1936 (pensionär, no egenavgifter at all)
Vinst 100 000 kr, total skatt utan räntefördelning 2 997 kr.
With räntefördelning on entire 100 000: skatt = 30% × 100 000 = 30 000 kr.
**Extra skatt: 27 003 kr.** → Don't do it.

#### Mimmi, född 1949 (pensionär, egenavgifter 10,21%)
Vinst 100 000 kr, skatt utan räntefördelning 10 654 kr.
With räntefördelning: 30 000 kr.
**Extra skatt: 19 346 kr.** → Don't do it.

#### Mirjam, född 1989 (full egenavgifter, vinst 100 000 kr)
Skatt utan räntefördelning 23 606 kr.
With räntefördelning: 30 000 kr.
**Extra skatt: 6 394 kr.** → Don't do it (even though aktiv non-pensionär).

#### Mirjam, but vinst is 250 000 kr (over brytpunkten because + tjänsteinkomst)
Skatt utan räntefördelning 74 487 kr.
With räntefördelning on entire vinst: 75 000 kr räntefördelningsbelopp + the rest in NV.
**Net benefit: räntefördelning saves money once kapitalbeskattat belopp avoids statlig skatt on top of egenavgifter.**

### Conclusion (PDF slutsatser)

> *"För +65-åringar är det bättre att låta bli räntefördelningen."*
> *"För övriga som inte betalar statlig skatt kan räntefördelningen innebära något lägre skatt än utan räntefördelning. Men även om räntefördelningen bara medför litet lägre skatt kan det ändå vara bättre att låta bli."*
> *"För övriga som ligger över brytpunkten lönar det sig att använda räntefördelning."*

In sum: positiv räntefördelning is only clearly beneficial when the näringsidkare is **below 65, has aktiv verksamhet, and has inkomst over brytpunkten för statlig inkomstskatt**.

## Kapitalunderlag — what counts

Kapitalunderlag = tillgångar minus skulder i verksamheten at föregående års utgång (= ingång of current year).

### Tillgångar that count
- Likvida medel (kassa, bankkonton in SEK or utländsk valuta used in business)
- Specialinlåning på bank (jämställt with bankkonto)
- Insättningar på Riksgäldskonto, realränteobligationer, marknadsnoterade fordringar in korta papper, certifikat och växlar
- Kundfordringar (taken at deklarationsvärde — net of doubtful)
- Varulager (taken at deklarationsvärde — net of inkurans, before any value adjustment)
- Inventarier (taken at **skattemässig restvärde**)
- Immateriella tillgångar (skattemässig restvärde)
- Näringsfastigheter (huvudregeln: anskaffningsutgift minus avskrivningar; alternativregeln: % of taxeringsvärde 1993, see below)
- Näringsbostadsrätter (anskaffningsvärdet)
- Andelar i kooperativa föreningar (insatser; insatsemissioner only if förvärvade)
- Medel på skogskonto, skogsskadekonto, upphovsmannakonto: **halva beloppet** (latent skatt)
- Momsfordran

### Tillgångar that DO NOT count
- Aktier, konvertibla skuldebrev, marknadsnoterade kapitalmarknadspapper (NOT räknas — they belong to inkomstslaget kapital)
- Privatbostadsfastigheter
- Andelar i handelsbolag (always in HB, not the EF underlag)
- Ej förvärvade insatsemissioner (de motsvarar inte skattat kapital)

### Skulder that minska kapitalunderlaget
- Banklån used in verksamheten
- Leverantörsskulder
- Upplupna räntekostnader, pensions-/garantiavsättningar, upplupna löner och arbetsgivaravgifter, förskott från kunder
- Avsättning till ersättningsfond
- Avsättning till periodiseringsfond
- (Expansionsfondsskatten räknas EJ som skuld)

### Items that are NEITHER tillgång NOR skuld
- Inkomstskatt, egenavgifter, SLP, fastighetsskatt, kommunal fastighetsavgift, skattetillägg och förseningsavgifter (skatter i ren mening)

### Justeringar to apply
- **Sparade inrullade underskott** (not kvittade against kapitalvinst på näringsfastighet) → läggs till (acts as tillgång — restores eget kapital)
- **Sparat fördelningsbelopp** from prior years → läggs till
- **Tillfälliga kapitaltillskott** under previous 12 months → drar bort (only varaktiga insättningar count)

## Sparat fördelningsbelopp

Positiv räntefördelning need not be utnyttjat. The unused belopp:
- May be saved → **sparat fördelningsbelopp**
- Carries forward indefinitely
- Adds to kapitalunderlag next year → ränta-på-ränta effect
- May be used at företagets nedläggning to offset återförd P-fond and expansionsfond (powerful exit-planning tool)

Worked example (Ville, ur PDF):
- Skogsinnehav, kapitalunderlag 800 000 kr, ingen lust att räntefördela mot 0-resultat
- Räntefördelningsbelopp år 1: 800 000 × 7,15% = 57 200 kr → sparat
- Kapitalunderlag år 2 grows by sparat belopp → 880 000 kr
- Year 3 räntefördelning belopp = 880 000 × 6,99% = 61 512 kr → also sparas
- Sparat ackumulerat ingång år 3: 118 712 kr
- Year 3 säljer skog för 200 000 kr → resultat = 200 000 kr
- Aktuellt års räntefördelning = 96 800 kr
- Total available: 118 712 + 96 800 = 215 512 kr (cap = resultat = 200 000)
- Use 200 000 kr → 200 000 × 30% = 60 000 kr i kapital (cheap), saving NV income from being taxed at 65%
- Carry forward remaining 15 512 kr

### Overtaking sparat räntefördelning

Sparat fördelningsbelopp may be **överlåtet** at:
- Bodelning (separation/divorce)
- Arv (inheritance)
- Gåva and other **benefika fång** (the recipient pays little or nothing)

The kapitalunderlag must justify the overtagaren in mottagandeåret. Note Skatteverket says the year of takeover may not be the year of utnyttjande unless the recipient already had sufficient kapitalunderlag from prior year.

## Negativ räntefördelning planning

Less flexibility (obligatorisk), but worth considering:
- A pensionär with negativ kapitalunderlag pays 24,26% SLP and gets jämfört 30% skattereduktion — **net 5,74% benefit**, weird but real
- Strategy: avoid running negativ kapitalunderlag if egenavgifter are full (28,97%) — kostar mer än kapitalskattereduktion ger
- Restructuring tip: pay back lån used for private purposes before årsskiftet so de inte räknas som näringsskuld

### Övergångspost (1994)

If kapitalunderlag was negativt 31 dec 1993 (when systemet infördes), a **övergångspost** equal to the negativa belopp was fastställt. This adds to kapitalunderlag every year (effectively acts as a permanent tillgång), preventing onödig negativ räntefördelning from the legacy negativa eget kapital.

Övergångsposten:
- Carries with bodelning, arv, gåva, testamente (helt övertagande)
- Försvinner at *byte av företagsform* (e.g., EF → AB) and at *försäljning*
- SOU 2020:50 proposes abolishing den

### Särskild post (fastigheter erhållna med lån genom gåva)

When you receive a fastighet i gåva and take över a lån that exceeds the fastighet's andel of skattemässigt kapitalunderlag, you may add a **särskild post** at gåvotillfället to undvika negativ räntefördelning. Only valid as long as the kapitalunderlag före den särskilda posten is positiv. Proposed slopad in SOU 2020:50.

## Alternative valuation rule for fastigheter

For fastigheter förvärvade *före 1991*, anskaffningsvärdet may be låg. Alternative: use a % of taxeringsvärde 1993:
- Småhusenheter: **54%**
- Hyreshusenheter: **48%**
- Industrienheter: **64%**
- Lantbruksenheter: **39%** of taxeringsvärdet (for non-småhus parts)

Värdeminskningsavdrag (avskrivningar) 1982–1993 above 10% of det framräknade anskaffningsvärdet → dras av. Avskrivningar 1994+ → dras av oavsett belopp.

Jämkningsregeln: värdet via alternativregel ≤ 75% av byggnadsvärde, mark och markanläggningar' marknadsvärde.

## Makar — fördelning av tillgångar och skulder

If makar driver gemensam EF:
- Each make computes their *own* kapitalunderlag based on *their* andel av tillgångar/skulder
- One make can deliberately own all problematic skulder, so the other has +50 001 räntefördelningsutrymme

Worked example (PDF): makar driva en liten verkstad. Fastighetsvärde 1 000 000 kr, skulder 920 000 kr, mannen äger maskiner 100 000 kr. Default fördelning 50/50 på fastigheten:
- Manns kapitalunderlag: 0,5 × (1M − 920k) + 100k = 140 000 kr → får räntefördela
- Kvinnans: 0,5 × (1M − 920k) = 40 000 kr → får INTE räntefördela (under 50k tröskel)
- If de buy en maskin 15 000 kr och låter kvinnan köpa: hennes underlag blir 40k+15k = 55 000 kr → får räntefördela hela 55k

This kind of fördelningsplanering is legitim under IL 33 kap.

## Pitfalls

1. **Ingen räntefördelning första året** — räntefördelning kräver att kapitalunderlag finns vid ingång av räkenskapsåret, vilket nystartad verksamhet inte har (Skatteverket Dnr 131 315797-06/111)
2. **Forgetting tillfälliga kapitaltillskott reduction** — putting in 50 000 kr i december and taking out 50 000 kr in january does NOT permanently increase kapitalunderlag → måste eliminera tillskott som inte är varaktiga
3. **Jämkning vid förkortat räkenskapsår** — om räkenskapsåret är 8/12 mån, fördelningsbeloppet jämkas till 8/12 av schablonen
4. **Konfundera anskaffningsvärde med deklarationsvärde** för kundfordringar och varulager (correct value is the *skattemässiga* värdet)
5. **Aktier antas vara tillgång i EF** — they are NOT (de hör till inkomstslaget kapital, not näringsverksamheten)
6. **Insatsemissioner i ekonomisk förening** — only counted if förvärvade (not if mottagna gratis), because de motsvarar inte beskattade pengar

## SOU 2020:50 simplification proposal (not enacted)

- Slopad övergångspost
- Slopad särskild post för fastigheter
- Räntesatsen för positiv räntefördelning föreslås sänkas till bara SLR (utan +6 pp)
- Slopad negativ räntefördelning helt
- Kapitalunderlag beräknas på utgång av året (inte ingång)
- 50 000 kr gränsbelopp slopas

Worth flagging in software as a "watch this space" — if enacted, all rules above change materially.

See also [[periodiseringsfond-expansionsfond-ef]] (kapitalunderlag conceptually identical) and [[egenavgifter-sgi-pgi-jsa]] (SGI/PGI consequence of räntefördelning).
