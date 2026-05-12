# EF vs AB — Skattemässig Jämförelse och Brytpunkter

## Purpose

This reference helps decide when an enskild näringsidkare should:
1. Stay as EF
2. Ombilda till AB
3. Run **both EF and AB parallellt** (the "både och" strategy)

The decision involves marginalskatt jämförelser, sociala avgifter, riskhantering, pension/SGI-byggande, och administrativ komplexitet.

For AB-specific skatteplanering (3:12-regler, periodiseringsfond AB, koncernbidrag), use `swedish-tax-planning` (sister skill).

## Den fundamentala olikheten

| Aspekt | EF | AB |
|---|---|---|
| Juridisk person | Nej (= du själv) | Ja |
| Skattesubjekt | Nej (personlig deklaration) | Ja (egen INK2) |
| Ansvar för skulder | Obegränsat personligt | Begränsat till aktiekapital (25k min) |
| Föreningssamhetsstruktur | En person (eller makar gemensamt) | 1+ ägare med skilda andelar |
| Inkomstskatt | Personlig progressiv (29 – 65% inkl egenavgifter) | Bolagsskatt 20,6% + ägarbeskattning |
| Socialavgift | Egenavgifter 28,97% (aktiv) / SLP 24,26% (passiv) | Arbetsgivaravgifter 31,42% på lön |
| Periodiseringsfond | 30%, ingen schablonintäkt, ej bokförd | 25%, schablonintäkt, ska bokföras |
| Expansionsfond | 20,6%, ger lågbeskattad retention | (Inte tillämpligt — använd retention) |
| Räntefördelning | Tillämpligt (IL 33 kap) | Inte tillämpligt |
| Inlåning till AB | (Ej tillämpligt) | Tillåtet, ränta 30% kapital |
| 3:12-regler | (Ej tillämpligt) | Tillämpligt vid kvalificerade andelar |
| Personligt ansvar | Du själv är firman | Knivskarp skiljelinje |
| Förbudet mot lån från företaget | Ja (utan begränsning) | NEJ (förbjudna lån, max kreditbrott) |
| Revisor | Aldrig krav | Krav om 2 av: omsättning > 3 MSEK, 3 anställda, balansomslutning > 1,5 MSEK |
| Bokslut form | Förenklat årsbokslut (K1) om < 3 MSEK | Årsredovisning (K2/K3) alltid |
| Bolagsstämma | Inte tillämpligt | Krav även för enmans-AB |
| Sjukpenning | Direkt från Försäkringskassan dag 15+ | Bolaget måste betala sjuklön dag 1-14 |
| Tantieme | Inte möjligt | Möjligt — flyttar resultat mellan år |

## Marginalskatt + total skatt — TABELLER ur eske

These are the **core numbers** for the EF vs AB beslut. Reproduced from PDF "Marginalskatt och total skatt" kapitlet. Verify against current SKV-rater.

### Icke-pensionärer (aktiv EF, 7 karensdagar, 28,97% egenavgifter, kommunalskatt 32,28%)

| Vinst (kr) | Total skatt (%) | Marginalskatt (%) |
|---|---|---|
| 100 000 | 24 | 32 |
| 200 000 | 28 | 33 |
| 300 000 | 31 | 42 |
| 400 000 | 34 | 43 |
| 500 000 | 36 | 43 |
| 600 000 | 37 | 46 |
| 700 000 | 39 | 46 |
| 800 000 | 41 | **61** |
| 900 000 | 43 | 63 |
| 1 000 000 | 45 | 63 |

Note: marginalskatten *hoppar* uppåt vid 800 000 kr för icke-pensionärer, sedan platsar runt 63%. Detta beror på utfasning av jobbskatteavdraget kombinerat med skiktgränsen för statlig skatt.

### Pensionärer (samma verksamhet, men 10,21% egenavgifter)

| Vinst (kr) | Total skatt (%) | Marginalskatt (%) |
|---|---|---|
| 100 000 | 16 | 19 |
| 200 000 | 16 | 19 |
| 300 000 | 19 | 30 |
| 400 000 | 22 | 32 |
| 500 000 | 25 | 38 |
| 600 000 | 27 | 56 |
| 700 000 | 32 | 59 |
| 800 000 | 35 | 64 |
| 900 000 | 38 | 59 |
| 1 000 000 | 41 | 64 |

Pensionärer betalar markant lägre skatt än icke-pensionärer på samma vinst — en av de **starkaste skälen** att hålla EF i drift även efter pensionsåldern.

### Brytpunkter (för statlig skatt)

| Group | Brytpunkt 2025 |
|---|---|
| Icke-pensionär | ca 643 100 kr (verify) |
| Pensionär (≥ 65 vid årets ingång, hel pension hela året) | ca 707 200 kr (verify) |

Note 2021 baseline values from PDF: 537 200 kr (under 65) / 596 800 kr (pensionär). Verifying needs current SKV-data.

## Tabellen "Kvar efter skatt på 100 kr"

PDF aggregerar de typiska scenarierna so här:

### Aktiv NV i EF (icke-pensionär, vinst under brytpunkten 537 200 kr 2021)

| Inkomstmetod | Kvar efter skatt på 100 kr intjänad |
|---|---|
| Vinst i EF, under brytpunkten (–64 år) | **60–68 kr** |
| Positiv räntefördelning | **70 kr** |

### Löneuttag från AB (icke-pensionär)

| Inkomstmetod | Kvar efter skatt på 100 kr intjänad |
|---|---|
| Löneuttag –64 år | **53–58 kr** |
| Kapitalbeskattad utdelning (inom gränsbelopp K10) | **62 kr** |
| Tjänstebeskattad utdelning (över gränsbelopp) | **50 kr** |

### Tolkning

- **Under brytpunkten**: EF *vinner* över AB-lön (60–68 kr vs 53–58 kr) med ca 7–10 kr per intjänad 100 kr → 7–10% bättre
- **Vid utnyttjande av positiv räntefördelning**: EF ger 70 kr → motsvarar K10-utdelning (62 kr) plus AB-bolagsskatt nedmuttring

### Över brytpunkten

PDF observation: "På inkomster över brytpunkten är vinst-alternativet inte förmånligt utan då är det kapitalbeskattad utdelning som ger bäst skatteeffekt."

So över brytpunkten (statlig skatt 20% extra), AB med kapitalbeskattad K10-utdelning vinner over EF.

### Pensionärer skiljer sig

Pensionärer (10,21% egenavgifter) tjäna upp till ca **75 kr per 100 kr** vid löneuttag från AB, om de utnyttjar utökat JSA för +65-åringar och har en låg pension som komplement. EF för pensionärer ger samma höga retention (eftersom egenavgifterna redan är låga 10,21%). PDF: "Som bäst kan det bli ca 75 kr kvar för ägaren vid löneuttag."

Födda 1937 och tidigare: inga egenavgifter alls → "närmare 80 kr kvar i fickan för privat konsumtion på löner upp till brytpunkten."

## När EF generellt är förmånligare än AB

1. **Vinst under brytpunkten** (icke-pensionär)
2. **Pensionär** med aktiv NV (mycket lägre egenavgifter än AB:s arbetsgivaravgifter)
3. **Kombinerad förlustverksamhet och vinstverksamhet** — automatisk kvittning inom EF (se [[kvittning-underskott]] Bertil-exempel)
4. **Kulturarbetarverksamhet** — fri kvittning av underskott mot tjänst, ingen 5-årsgräns
5. **Ny start** — kvittning mot tjänst första 5 åren (100k/år)
6. **62–64-åringar** — har specialgyl: hel allmän pension under hela året → lägre 10,21% egenavgifter även före 65

## När AB generellt är förmånligare

1. **Vinst över brytpunkten** (statlig skatt 20% extra slår igenom)
2. **Behov av att samla på sig sparat utdelningsutrymme (K10)** — för framtida säljbar verksamhet
3. **Behov av begränsat personligt ansvar** (kommersiella skäl)
4. **Flera ägare som inte är makar/sambor** (EF passar bara en person eller makar)
5. **Behov av extern finansiering** — bank/investerare ser hellre AB
6. **Behov av att kapitalisera ABFP, försäljning av aktier till externa**
7. **Inlåning av privata medel till verksamheten** — ABs kan göra inlåning, ge sig själv marknadsmässig ränta (~SLR+1) som beskattas i kapital (30%); EF har bara räntefördelning, vilket är mindre flexibelt

## "Både och" strategy

PDF rekommendation explicit: 
> "Ett tips är att du samtidigt har enskild firma och aktiebolag; i många fall är detta faktiskt det bästa alternativet."

### Use cases

#### Hybridmodell 1: Bygga gränsbelopp innan AB tas i bruk fullt

- Start verksamheten i EF (utnyttja 5-årsregeln för kvittning, samla på dig kompetens)
- Start AB parallellt → börja samla på dig sparat utdelningsutrymme (K10 förenklingsregeln 2,75 IBB / 4 IBB)
- Om några år: ombilda hela verksamheten till AB med ackumulerat utdelningsutrymme i hand

#### Hybridmodell 2: Konsult i AB + hyresfastighet i EF

- AB driver konsultverksamheten (hög inkomst, K10 + lön kombo)
- EF driver hyresfastighet (passiv → SLP 24,26%, ingen JSA, eller om aktiv-status: full system)
- Inkomstkvittning mellan AB och EF är dock inte möjligt direkt — men:
  - AB:s utgifter och EF:s utgifter är separata; ingen blandning
  - Personlig deklaration kombinerar dock allt → AB-utdelning + EF-vinst slås ihop för progressivskalan
  - **Lägg lågmarginalskatt-aktiviteten i EF**, högmarginalskatt-aktiviteten i AB

#### Hybridmodell 3: Kulturarbetare med sidoverksamhet

- Kulturarbetarverksamheten i EF (för kulturarbetarkvittning)
- Sidoverksamheten (e.g., konsulthantering) i HB → får 5-årsregeln igen
- AB om man har stor andel ägande och flera samarbetspartner

#### Hybridmodell 4: 62+ med komplementverksamhet

- Lön/pension från eget AB
- EF parallellt → drar nytta av låga egenavgifter (10,21% från 62 om hel pension hela året, annars 28,97% till 65)
- Pension är inte JSA-grundande, men aktiv NV-inkomst är → även små belopp aktiv NV ger förhöjt JSA

## Skiljd hantering vid sjukpenning

A subtle but real fördel för EF:

- **AB-ägare**: AB:et måste betala sjuklön första 14 dagarna ur egen ficka. Försäkringskassan tar över dag 15+. Försäkringskassan granskar AB:ens ekonomi för att bedöma rimlig SGI → kan vara restriktiva för hög lön
- **EF-ägare**: Försäkringskassan betalar sjukpenning direkt från dag 8 (efter karenstid 7 dagar). Aldrig sjuklönsperiod ur EF-ekonomin. SGI baseras på NV-inkomsten over senare år.

PDF: "Försäkringskassan kan direkt konstatera vilken månadslön du har och därmed vilken sjukpenning du har rätt till. Men det förekommer att Försäkringskassan granskar bolagets ekonomi för att bedöma om ett visst (högt) löneuttag är en rimlig uthållig nivå."

## Inlåning till AB — and parallel concept i EF

### AB

- Ägaren får låna ut pengar till AB:et
- AB betalar marknadsmässig ränta → beskattas hos ägaren i inkomstslaget kapital (**30% skatt**)
- Marknadsmässig ränta för ett AB med 25 000 kr aktiekapital ≈ SLR + 1 procentenhet (knappast värt besväret)
- Ej lönebeskattning på räntan; ingen arbetsgivaravgift

### EF

- Ingen motsvarighet — det är **du själv** som driver firman; du kan inte låna ut till dig själv
- Närmast: räntefördelning (kapitalbeskattning 30% av schablonräntan på kapitalunderlaget)
- Räntefördelning är dock obligatorisk (alltid beräknas), och kommer med vissa begränsningar (kapitalunderlag-tröskel, etc)

## Uthyrning till AB

EF har en **specifik nackdel** vs AB här:

- Som ägare till ett AB kan du hyra ut **lokal i din bostad** till AB:et och få marknadsmässig hyra som beskattas i inkomstslaget kapital (30%)
- Som EF-ägare får du INTE hyra ut lokal i din bostad till din EF
- Istället: schablonavdrag (2 000 / 4 000 kr per år beroende på upplåtelseform) eller faktiska merkostnader

## Tantieme — inte tillgängligt i EF

I AB kan ägaren styra resultatet genom **tantiemavsättning** (vinstrelaterad löneökning, beskattas hos ägaren året efter bolagsstämman):
- Reducerar AB:ens beskattningsbara resultat aktuella året
- Beskattas hos ägaren först nästa år (vid utdelningstillfället)

I EF: ingen motsvarighet. Resultatet beskattas alltid hos näringsidkaren personligen samma år.

## Föräldraledighet och föräldrapenninggrundande inkomst

- EF: inkomst av aktiv NV → föräldrapenninggrundande (tak 10 PBB = 588 000 kr 2025)
- AB: lön + förmåner → föräldrapenninggrundande
- Hybridfördel: AB-ägare kan dra upp sin lön innan föräldraledighet för att maxa föräldrapenningen (FK kan dock granska)

## Ombildning EF → AB — when to switch

Triggers för att ombilda till AB:
- **Vinst regelbundet över 800 000 kr** — marginalskatten i EF når 61–63% medan AB-bolagsskatt + K10-utdelning ger 36–40% effektiv
- **Verksamhet ska säljas i framtid** — AB-aktier kan säljas; EF kan inte
- **Externa investerare** behöver
- **Personligt ansvar oacceptabelt** — t.ex. byggverksamhet med stora kontrakt
- **Flera ägare som inte är makar** — EF passar bara en person + makar; HB möjligt men ofta inte attraktivt
- **Anställning skapas** — formellt anställningsförhållande lättare i AB
- **Skenmänsklig profilering** — AB ofta uppfattas som mer seriös av kunder

### Praktisk ombildning

Hela verksamheten överförs till AB. Periodiseringsfonder får överföras (om hela verksamheten eller en verksamhetsgren går över) → aktiekapital måste tillskjutas motsvarande P-fondernas sammanlagda storlek. Expansionsfond kan föras över under specifika villkor (79,4% av fondbeloppet i realtillgångar måste föras med).

Underskott i EF kan **INTE** föras över till AB. Restriktion: tillgångarna förs ut till underpris → uttagsbeskattning frångås → slutligt underskott begränsas.

Detaljerade regler för ombildning: se Björn Lundén-bok "BYTE FRÅN ENSKILD FIRMA TILL AKTIEBOLAG".

## Tabell: snabbjämförelse vid olika vinstnivåer

Per intjänad krona, ungefär (under 65, aktiv, kommunalskatt 32%):

| Vinst (årlig) | EF (vinst) | AB (lön) | AB (utdelning inom K10) |
|---|---|---|---|
| 100 000 | 76 kr/100 | 50 kr/100 | (ej K10-möjlighet ofta) |
| 300 000 | 69 kr/100 | 53 kr/100 | 62 kr/100 (om K10 finns) |
| 500 000 | 64 kr/100 | 55 kr/100 | 62 kr/100 |
| 700 000 | 54 kr/100 | 48 kr/100 | 62 kr/100 |
| 900 000 | 37 kr/100 | 42 kr/100 | 62 kr/100 |

(Approximate — actual depends on specific deduction utilizations.)

Crossover for EF advantage: roughly **at brytpunkten** (~640 000 kr 2025). Below it, EF wins. Above it, AB with K10 wins.

## Anställning vs EF + bisyssla

PDF subtle case:

Mannen har anställning (250 000 kr lön) + EF hyresfastighet (passiv).

> "Bertil har också sedan många år en enskild firma (ett hyreshus) som ger en förlust på 100 000 kr varje år. Han tar detta av sina beskattade pengar och har därefter slutligen 299 000 – 100 000 = 199 000 kr kvar av lönen från bolaget."

Bertil's alternative: skrota AB:et, lägg konsultverksamheten i EF + hyreshuset → sammanlagd vinst 520 000 − 100 000 = 420 000 kr, beskattat i en EF → 253 000 kr kvar.

**Sparing: 54 000 kr/år** by collapsing AB into the existing EF, because the EF kvittar inbyggt mellan delverksamheter.

## Pitfalls

1. **Förutsätta att AB alltid är bättre vid hög vinst** — under brytpunkten EF är ALMOST ALWAYS bättre
2. **Glömma "både och" möjligheten** — ofta bästa lösningen
3. **Konvertering till AB innan brytpunkten passerats** — för tidig konvertering kostar K10-uppbyggnad och frivillig administration
4. **Inte överväga 62-årsgyl** — pensionärer (även 62-åringar med hel pension) har drastiskt lägre egenavgifter i EF
5. **Stoppa allt arbete vid 65** — fortsätt aktiv NV → utökat JSA, fortsatt pensionsintjäning
6. **Glömma att EF-underskott från olika delverksamheter automatiskt kvittas** — ofta inte rimligt att sätta upp separata AB
7. **Aktiekapital 25 000 kr som "lätt"** — i praktiken blir AB-ägare ofta personligt ansvariga via borgensavtal → personligt ansvar finns redan
8. **Ansvarsgenombrott** — staten kan kräva betalning från AB-ägare för obetalda skatter/avgifter; ej helt riskfritt

## Implementation checklist for software

If you build software that helps users choose between EF and AB:

- [ ] Ask: vinst-prognos per år nästa 3–5 år
- [ ] Ask: ålder, pension-status
- [ ] Ask: behöver begränsa personligt ansvar?
- [ ] Ask: flera ägare? Make/sambo?
- [ ] Ask: planerar sälja verksamheten framöver?
- [ ] Ask: kulturarbetarverksamhet?
- [ ] Ask: behöver SGI för planerad föräldraledighet?
- [ ] Compute total effektiv skatt per year under EF-alt och under AB-alt med olika löne/utdelning-mixer
- [ ] Surface "både och" som rekommendation om scenariot passar
- [ ] Warn vid premature konvertering (under brytpunkten)
- [ ] Warn att underskott i EF inte kan föras över till AB

See also `swedish-tax-planning` (AB-specifik planering), [[aktiv-passiv-naringsverksamhet]] (gateway), [[periodiseringsfond-expansionsfond-ef]] (jämförelse med AB:s P-fond), [[rantefordelning-planning]] (motsvarighet till AB:s inlåning).
