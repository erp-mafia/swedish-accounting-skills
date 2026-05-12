# Egenavgifter, SGI, PGI, Jobbskatteavdrag — Interaction Effects

## Legal basis

- Socialavgiftslagen (SAL) 2000:980 — egenavgifter
- Lagen (1990:659) om särskild löneskatt på vissa förvärvsinkomster
- IL 12 kap 37 § — jobbskatteavdrag (skattereduktion)
- SFB (Socialförsäkringsbalken) 2010:110 — SGI, sjukpenning, föräldrapenning
- IL 59 kap — pensionssparavdrag

This reference covers the **interaction effects** between social charges, SGI, PGI, JSA and de skatteplanerings-instrument (P-fond, expansionsfond, räntefördelning, avskrivningar) som påverkar dessa underlag.

## Egenavgifter — base rates

### Standard rates (2025)

| Group | Rate |
|---|---|
| Active näringsidkare, **7 karensdagar** (standard) | **28,97%** |
| Active, 1 karensdag | ~29,2% (slightly higher) |
| Active, 14 karensdagar | ~28,8% |
| Active, 30 karensdagar | ~28,4% |
| Active, 60 karensdagar | ~27,9% |
| Active, 90 karensdagar | ~27,4% |
| Passive näringsidkare (SLP) | **24,26%** |
| Pensionär (≥ 65 vid årets ingång, eller hel pension hela året) | **10,21%** (bara ålderspensionsavgift) |
| Född 1937 eller tidigare | **0%** |
| Pensionär som är passiv | **24,26%** (SLP, ingen nedsättning till 10,21%) |

### Karensval

- Default: 7 karensdagar
- Val of 1, 14, 30, 60 eller 90 karensdagar görs hos Försäkringskassan på blankett
- Anmälan inom uppsägningstid: ny karens börjar gälla efter motsvarande antal dagar efter anmälan
- Inte tillåtet att byta till kortare karens om man redan är inne i en sjukperiod
- Försäkran krävs att inte ha någon pågående sjukdom (eller upplysa om den)

PDF guidance:
> "Vill du ändra antalet karensdagar ska du kontakta Försäkringskassan."

### Ingen nedsättning för pensionärer eller +65

Pensionärer (som redan betalar 10,21%) får **ingen** generell nedsättning. Likewise +62-åringar som tagit ut hel allmän pension hela året.

### Regional nedsättning (stödområde A — Norrlands inland)

10% extra nedsättning av avgiftsunderlaget upp till 180 000 kr → max 18 000 kr/year.

Stödområdet = mest Norrlands inland. Lista finns hos Tillväxtverket.

### Hel sjuk- eller aktivitetsersättning

Helt eller delvis under året: bara ålderspensionsavgift (10,21%) på överskott av aktiv NV.

## Generell nedsättning av egenavgifter — 7,5%

PDF references describe this as "generell nedsättning":

- **7,5 procentenheter** nedsättning av egenavgifter
- Cap: max **15 000 kr/år** (= 7,5% av 200 000 kr underlag)
- Underlag = överskott av **aktiv** NV (efter schablonavdrag för egenavgifter; exklusive sjukpenning)
- Krav: överskottet **överstiger 40 000 kr** (= ca 50 000–52 000 kr i överskott före schablonavdrag)
- Beräknas automatiskt av Skatteverket — du ska INTE begära den i deklarationen
- Bara aktiva näringsidkare — ej för pensionärer (redan 10,21%) eller passiva (SLP utan nedsättning)

### Marginalkurva i intervallet 40 001 – 200 000 kr

In intervallet 40 001 – 200 000 kr underlag får du nedsättning på 5 procentenheter på **det belopp som överstiger 40 000 kr**. Wait — these numbers don't fully line up because the PDF references different reform versions. Verify with current SKV:

PDF reference for the 5%-version:
- 7,5% × (överskott − 40 000) upp till tak 15 000 kr
- Innebär ~7,5% nedsättning gradvis upp till 200 000 kr underlag (full nedsättning vid 200 000)
- Över 200 000 underlag = full nedsättning på endast den första 200 000 kr; resten utan nedsättning

### Tröskeleffekt vid 40 000 kr

PDF describes this märkliga effekt:
> "Är överskottet 40 001 kr får du nedsättning på hela överskottet"
> "Är överskottet bara 40 000 kr får du ingen nedsättning"

So **omvänd marginalskatt** — going from 40 000 → 40 001 kr underlag triggers a sudden 3 000 kr nedsättning (7,5% × 40 000 = 3 000 kr).

PDF: "Det är en ovanlig tröskeleffekt i skattesystemet, nämligen att en obetydlig höjning av inkomsten kan ge en så pass betydande skattesänkning."

Software borde flagga overskott som ligger precis under 40 000 kr (warn att en kr över triggar bigger nedsättning).

### Maxbelopp 200 000 kr (15 000 kr in nedsättning)

Vid underlag 200 000 kr nås maxavdraget 15 000 kr. Über 200 000 är det ingen marginalfördel.

## Schablonavdrag för egenavgifter på NE-bilaga

- **R43**: avdrag för beräknade egenavgifter
- **Max 25%** av överskott före schablonavdrag (aktiv standard)
- **20%** för passiv (SLP)
- **10%** för pensionärer
- Tipsbart minska avdraget om man vill ha högre pensionsgrundande/sjukpenninggrundande inkomst
- Tip från PDF: vid sista året före nedläggning, gör **exakt** schablonavdrag baklängesberäkning för att slippa avstämningspost nästa år

### Avstämning nästa år

Beräknat schablonavdrag stämmer aldrig exakt med faktiska egenavgifter. Differensen rättas till i nästa års deklaration:
- **R39** = tidigare års schablonavdrag (läggs tillbaka som intäkt)
- **R40** = faktiska egenavgifter / SLP enligt skattebeskedet (dras av)

Net effect: schablonavdraget är ett genuint avdrag för året, men korrigeras nästa år mot verkligheten.

### "Höja inkomsten" via lägre schablonavdrag

PDF tip: ibland vill man höja den deklarerade inkomsten. Skäl:
- Utnyttja rotavdrag / rutavdrag (kräver tillräckligt med skatt)
- Höja PGI för pensionsrätt
- Höja SGI (utan att Försäkringskassan adjusterar bort dispositioner — schablonavdraget är inte en disposition)

Skatteverket kan vägra schablonavdragsändringar som verkar bedrägeriska — PDF: "Om det avsatta beloppet skiljer sig med så stort belopp att det kan antas att näringsidkaren försökt uppnå en obehörig förmån bör avdraget rättas."

But: rimliga adjustments medges. Bara om man yrkar **noll** schablonavdrag eller mycket litet bör SKV granska.

## Underlag för aktivitets-/sjukpenning (SGI)

### Calculation

SGI is computed by **Försäkringskassan** based on årsinkomst av arbete. För enskilda näringsidkare baseras SGI på:
- Beräknad inkomst av aktiv NV
- Bortser från **skattemässiga dispositioner**: avsättning/återföring av P-fond, expansionsfond
- Bortser också från insättning/uttag på skogskonto, upphovsmannakonto
- **Räntefördelning räknas** (men positiv minskar SGI eftersom NV-inkomsten minskar)
- **Avskrivningar räknas** (höjda avskrivningar minskar SGI)
- **Schablonavdrag för egenavgifter räknas** (men FK justerar — om du minskar schablonavdraget, FK ökar tillbaka motsvarande)

### Tak och nedre gräns

| Threshold | 2025 |
|---|---|
| Lägsta SGI (0,24 PBB) | 14 112 kr |
| Lägsta för pensionsintjänande PGI (0,423 PBB) | 24 870 kr |
| Max SGI (8 PBB) | 470 400 kr |
| Max PGI (7,5 IBB) | 604 500 kr |
| Max föräldrapenninggrundande (10 PBB) | 588 000 kr |
| Max för 7,5%-nedsättning (200k underlag) | 200 000 kr |

Sjukpenning = 77,6% (80% × 0,97) av SGI. Föräldrapenning likewise.

### "Framåtriktad" SGI bedömning

Försäkringskassan bedömer SGI **framåt** (vad antar de att näringsidkaren kommer tjäna nästa år), inte bakåt. Vid sjukdom:
- För nystartade EF (inom första 24–36 månaderna, "uppbyggnadsskedet") jämförs med en motsvarande anställd inkomst
- För etablerade EF: senaste års redovisade NV-inkomst används som proxy

### Höjda SGI-strategies (om man har en känd kommande sjukdomsperiod / föräldraledighet)

Saker som höjer SGI (men kostar i annan riktning):
- Avstå från positiv räntefördelning → höjer NV-inkomsten
- Avstå från eller minska avskrivningar på inventarier (de återkommer senare som mindre avskrivningar)
- Mindre schablonavdrag för egenavgifter (FK skulle ofta justera, men inte alltid)
- Negativ räntefördelning räknas full mot SGI (höjer den)

OBS: P-fond avsättning/återföring påverkar INTE SGI (Försäkringskassan bortser).

## Underlag för pensionsgrundande inkomst (PGI)

### Differences from SGI

PGI **påverkas** av:
- Avsättning/återföring P-fond
- Avsättning/återföring expansionsfond
- Insättning/uttag skogskonto, upphovsmannakonto
- Räntefördelning (positiv minskar, negativ höjer)
- Avskrivningar
- Schablonavdrag egenavgifter

Praktisk skillnad: P-fond kan användas för PGI-utjämning (jämna ut PGI över åren), men INTE för SGI-utjämning.

### Tak

- Max: 7,5 inkomstbasbelopp ≈ **604 500 kr 2025** (verify)
- Belopp över taket → ingen extra pension, men full egenavgift för aktiv NV
- PDF kommentar: "den delen av socialavgifterna är en ren skatt och förs inte till pensionssystemet utan till statsbudgeten"

### Lägsta gräns

- 0,423 PBB ≈ 24 870 kr 2025
- Om du når denna gränsen → full PGI från första kronan
- Pension built varje krona under taket → strävan att alltid komma över 24 870 kr

### Pensionärer (≥ 65 år)

- Pensionärer betalar 10,21% egenavgifter på aktiv NV, but **får ändå full pensionsintjäning** (= the 10,21% is dedicated to ålderspensionsavgift, hela summan går till pension)
- Hela livet räknas → man kan fortfarande bygga pensionspoäng efter pension
- → starkt argument att fortsätta jobba aktivt efter 65

## Jobbskatteavdrag (JSA) — skattereduktion för aktiva NV

### Det är en skattereduktion, inte ett avdrag

JSA är inte ett avdrag du gör i din deklaration. Det är en **skattereduktion** som beräknas automatiskt av Skatteverket → minskar din skatt.

Underlag × kommunalskattesats = skattereduktion (jobbskatteavdrag).

### Endast på inkomst av aktiv NV

This is one of the largest specific incentives för aktiv-classification:

- Pension, föräldrapenning, sjukpenning, a-kassa, sjuk-/aktivitetsersättning, livskaderänta → **ger inte rätt till JSA**
- Anställningsinkomster → JA
- Aktiv NV inkomst → JA
- Passiv NV inkomst → NEJ

### Beräkning (för personer under 65 år)

| Inkomstskikt (arbetsinkomst) | Underlag (× kommunalskattesats) |
|---|---|
| ≤ 0,91 PBB | Arbetsinkomsten minus grundavdrag |
| 0,91 – 3,24 PBB | 0,91 PBB + 34,05% av arbetsinkomst i detta skikt, minus grundavdrag |
| 3,24 – 8,08 PBB | 1,703 PBB + 12,8% av arbetsinkomst i detta skikt, minus grundavdrag |
| 8,08 – 13,54 PBB | 2,323 PBB minus grundavdrag |
| > 13,54 PBB | 2,323 PBB minus grundavdrag, sedan reduceras med 3% av arbetsinkomster över 13,54 PBB |

### Värden 2021 (illustrative, anchor for understanding)

| Arbetsinkomst | Totalt JSA | % av inkomsten |
|---|---|---|
| 100 000 | 10 004 | 10,0% |
| 200 000 | 17 442 | 8,7% |
| 300 000 | 24 628 | 8,2% |
| 400 000 | 30 252 | 7,6% |
| 500 000 | 30 252 | 6,0% |
| 600 000 | 30 252 | 5,0% |
| 700 000 | 28 465 | 4,1% |
| 900 000 | 22 466 | 2,5% |
| 1 100 000 | 16 466 | 1,5% |

Top JSA value: ~30 250 kr at inkomster 400 000 – 600 000 kr (= toppen av inkomst-skiktet 3,24 – 8,08 PBB).

### Förhöjt JSA för +65-åringar

Personer som vid årets ingång fyllt 65 år får utökat JSA:
- 20% av arbetsinkomsten upp till 100 000 kr (= max 20 000 kr extra)
- 5% av arbetsinkomster mellan 100 000 – 300 000 kr (= max 10 000 kr extra)
- 30 000 kr på arbetsinkomster mellan 300 000 – 600 000 kr (= max 30 000 kr extra)
- 30 000 kr på arbetsinkomster > 600 000 kr, minus 3% av arbetsinkomster över 600 000 kr

Pensionärer som är aktiva i NV gets a *much* bigger JSA than under-65 människor, but only on aktiv arbetsinkomst (inte pensionen själv).

### Arbetsinkomster — definition

Arbetsinkomster = anställningsinkomster minskade med kostnader för inkomsterna i tjänst, samt allmänna avdrag (t.ex. pensionssparande), samt inkomst av **aktiv NV**.

Inte räknas: pension, sjukpenning, föräldrapenning (även om dessa baseras på din aktiva NV).

### Interaktion med allmänt avdrag (kvittning av underskott)

Allmänt avdrag (kvittning av nystartad NV-underskott mot tjänst) **minskar** underlag för JSA. Net effekt:
- Kvittning sparar marginalskatt + statlig skatt (~32–52%)
- Men minskar JSA-reduktion → marginell motverkning

This is why **rullning ofta är bättre än kvittning** — rullning minskar både egenavgifter och inkomstskatt på framtida intäkt, utan att äta JSA.

## Interaktionsmatris — påverkan på underlag

Quick reference för software:

| Disposition | NV-inkomst | SGI | PGI | JSA-underlag | Egenavgifter | Egenavgifter-nedsättning |
|---|---|---|---|---|---|---|
| Positiv räntefördelning | Sänker | Sänker | Sänker | Sänker | Sänker | Underlag minskar → nedsättning minskar |
| Negativ räntefördelning | Höjer | Höjer | Höjer | Höjer | Höjer | Underlag ökar |
| P-fond avsättning | Sänker | INGEN (FK bortser) | Sänker | Sänker | Sänker | Underlag minskar |
| P-fond återföring | Höjer | INGEN | Höjer | Höjer | Höjer | Underlag ökar |
| Expansionsfond avsättning | Sänker | INGEN | Sänker | Sänker | Sänker (men 20,6% expansionsfondsskatt) | Underlag minskar |
| Expansionsfond återföring | Höjer | INGEN | Höjer | Höjer | Höjer | Underlag ökar |
| Avskrivningar (höjda) | Sänker | Sänker | Sänker | Sänker | Sänker | Underlag minskar |
| Schablonavdrag (mindre) | Höjer | INGEN (FK adjusts back) | Höjer | Höjer | Höjer | Underlag ökar |
| Pensionssparavdrag | Sänker | INGEN | Sänker | Sänker | Inget effekt direkt | Underlag minskar |
| Allmänt avdrag (kvittning) | (utanför NV) | INGEN (FK adjusts) | Sänker (allmänna avdrag) | Sänker | INGEN (tjänsteinkomst) | INGEN |

## Egenavgifter-effekt för aktiv vs passiv vs pensionär

Comparing effective social charges:

| Group | Direkt avgift | Generell nedsättning | Schablonavdrag | Effektiv avgift |
|---|---|---|---|---|
| Active, underlag 200 000 kr | 28,97% | -7,5% (max 15 000 kr) | 25% | ~21,5% effektivt |
| Active, underlag 100 000 kr | 28,97% | -7,5% (15k cap progressive) | 25% | ~24,5% |
| Passive, any underlag | 24,26% | 0% | 20% | ~24,26% |
| Pensionär, aktiv | 10,21% | 0% | 10% | ~10,21% |
| Pensionär, passiv | 24,26% | 0% | 20% | ~24,26% |

Insight: A passive näringsidkare and an active näringsidkare may end up at similar effective rates (~24% each) due to nedsättning-effekten. But aktiv har **JSA on top** (~6–10% reduktion of marginalskatt at 200k income) → aktiv vinner generellt med 15–17 000 kr/år.

## Underlag för nedre och övre PGI-gräns

### Lägsta inkomstgräns (PBB-baserad)

- 0,423 PBB = ca 24 870 kr 2025
- Om du når detta → full PGI **från första kronan**
- Strategy: ALWAYS get up to denna gränsen, even genom att lägre schablonavdrag for egenavgifter

### Skattefri inkomst (för barn)

- 20 135 kr (2021) = 0,423 PBB = same as lägsta PGI-gräns för "vanliga" arbetstagare och näringsidkare
- Inkomst under denna gränsen behöver inte deklareras för fysiska personer (med vissa undantag) and är skattefri
- Frestelse: hålla barnets lön precis under detta → skattefri inkomst
- PDF: BÄTTRE att gå precis över → barnet får full pensionsintjäning (kostar 7% allmän pensionsavgift, men ger pension hela livet)

## Pitfalls

1. **Pensionärer som räntefördelar** — vanligen NEGATIVE planeringsutfall (PDF: "För +65-åringar är det bättre att låta bli räntefördelningen")
2. **Förvirring av nedsättningar** — generell (7,5%, max 15k) ≠ regional (10%, max 18k) ≠ pensionär-rate (10,21% i stället för 28,97%)
3. **P-fond för SGI-höjning** — fungerar INTE; Försäkringskassan bortser från P-fond
4. **P-fond för PGI-höjning vid utbetalningsåret** — DOES work; FK does not adjust for P-fond when computing PGI
5. **JSA-effekt av allmänt avdrag glömd** — kvittning sparar inkomstskatt men äter JSA → net effekt mindre än förväntat
6. **Schablonavdrag för pensionärer** — bara 10% (inte 25%)
7. **Schablonavdrag för SLP/passiv** — 20% (inte 25%)
8. **Glömma att F-skatten redan inkluderar uppskattad egenavgift** — checkA-konto blir negativt om man **också** drar schablonavdrag mentalt utan att förstå att SKV redan beaktar
9. **Tröskeleffekten vid 40 000 kr** — vinst 40 001 ger ~3 000 kr lägre skatt än 40 000 → uppmana till small overshoot om planeringsbart

## Implementation checklist

- [ ] Detect grupp: active under-65, active 65+, pensionär (tagit ut hel pension), passive
- [ ] Apply rätt egenavgift-rate (28,97/24,26/10,21/0%)
- [ ] Apply generell nedsättning 7,5% conditional on aktiv + > 40 000 underlag + cap 15 000 kr
- [ ] Apply regional nedsättning if i stödområde A
- [ ] Compute SGI based on aktiv NV-inkomst, ignoring P-fond/expansionsfond dispositions
- [ ] Compute PGI including all dispositions
- [ ] Compute JSA per skiktreglerna (under-65 vs 65+)
- [ ] Warn vid underlag < 40 001 kr (lose nedsättning) eller < 24 870 kr (lose PGI)
- [ ] Surface advice: "Höja inkomsten över 40 001 kr ger 3 000 kr lägre skatt; rekommendation: minska schablonavdrag eller P-fond avsättning"
- [ ] Track per-year underlag history för SGI bedömning av FK (uppbyggnadsskede inom första 36 mån)

See also [[aktiv-passiv-naringsverksamhet]] (the gateway to all of this), [[rantefordelning-planning]] (the most subtle interaction), [[periodiseringsfond-expansionsfond-ef]] (PGI-leveling tool), and [[ef-vs-ab-breakeven]] (interaction of these med AB-alternativet).
