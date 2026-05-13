# Bokföring, blanketter och lantbruksspecifika redovisningsregler

Lantbruks-specifika regler för redovisning och deklaration. General BFL/BFNAR compliance covered by `swedish-accounting-compliance`; general bokslut by `swedish-year-end-closing`. This file covers the **deviations** that apply only to jord- och skogsbruk.

## LRF-BAS

LRF (Lantbrukarnas Riksförbund) har tagit fram en speciell **BAS-kontoplan för lantbruk** — en utvidgning av normal BAS med lantbruks-specifika konton. Den används av de flesta bokföringsprogram för lantbruk (BL Skatt, Visma SPCS, m.fl.).

LRF-BAS följer samma huvudstruktur som normal BAS (klasserna 1-8) men adderar:
- Underkonton för lager av djur per djurslag (1431-1438)
- Konton för olika typer av skogslager (1460-1465)
- Speciella intäktskonton för produkter per gren (3010 mjölk, 3020 kött, 3040 spannmål, etc.)

För kompatibilitet med Skatteverkets SIE-import räcker det med normal BAS — LRF-tilläggen är bara strukturhjälp.

## Räkenskapsåret

För enskild näringsverksamhet endast **kalenderår** (januari-december) tillåts som räkenskapsår — **inget brutet räkenskapsår**. (Bokföringslag 1999:1078 6 kap 4§)

Förlängning/förkortning av första räkenskapsåret tillåts upp till 18 månader, så att det slutar 31 december.

## Förenklat årsbokslut (K1)

Lantbrukare med nettoomsättning ≤ **3 MSEK** får upprätta förenklat årsbokslut. Detta är det normala för de flesta lantbruk.

Skillnaderna mot vanligt årsbokslut i lantbrukskontext:
- **Inte rätt** till avsättning för framtida återväxtåtgärder (största nackdelen för skogsägare — se `skogsbeskattning.md`).
- **Inte rätt** till avsättning för återställningskostnader vid substansminskning. Men beräknade återställningskostnader får läggas till anskaffningsvärdet.
- Lager med totalvärde ≤ 5 000 kr behöver inte tas upp som tillgång (BFNAR 2025:1-uppdatering: lagergränsen är nu också halvt PBB för många kategorier — kontrollera).
- Inventarier av mindre värde: halvt PBB-gränsen (**29 400 kr för 2025** (PBB 58 800 / 2), **29 600 kr för 2026** (PBB 59 200 / 2)) → direktavdrag. BFNAR 2025:1 (24 mars 2025) höjde gränsen från tidigare 5 000 kr — gäller från räkenskapsår som inleds efter 31 dec 2024.

Skogskontot tas upp som **tillgång i ruta B9 (Kassa och bank)** — både i vanligt och förenklat årsbokslut. I förenklat årsbokslut lämnas dessutom upplysning i **ruta U4** om att saldot är obeskattat (latent skatt vid uttag). Halva-beloppet-regeln gäller bara räntefördelningens kapitalunderlag, inte B9-värdet.

## Djur som lager (IL 17 kap 5§)

**Alla djur i jordbruk och renskötsel ska betraktas som lager**, trots att vissa djur (t.ex. mjölkkor, ardennerhästar, avelsdjur) ekonomiskt påminner mer om anläggningstillgångar. Detta är ett **uttryckligt undantag** från huvudregeln.

**Undantag från undantaget**: Djur i andra verksamheter än jordbruk/renskötsel (t.ex. cirkus, djurparker) → **anläggningstillgångar**.

### Värderingsreglerna för djurlager

- Lägst **85% av produktionskostnaden** (specialregel för djurlager — vanlig lager: 97% efter 3%-schablonen).
- Eller lägst **kollektivt beräknat genomsnittligt nettoförsäljningsvärde** för samtliga djur — om detta ger ett **lägre** värde än 85% av produktionskostnaden.

### Skatteverkets föreskrifter — uppdateras årligen

**Två separata regelverk:**
1. **Genomsnittlig produktionsutgift** (A-värden) — fastställs i SKVFS-föreskrifter, en per beskattningsår.
2. **Nettoförsäljningsvärde** (B-värden) — fastställs i SKV A allmänna råd.

**Aktuella föreskrifter** (kontrollera senaste vid implementation):

| Föreskrift | Beskattningsår | Ikraft | Tillämpas på deklaration |
|---|---|---|---|
| **SKVFS 2025:27** (A-värden, jordbruk) | 2025 | 2026-01-01 | våren 2026 |
| SKVFS 2025:28 (A-värden, renskötsel) | 2025 | 2026-01-01 | våren 2026 |
| SKVFS 2024:28 (föregående år, jordbruk) | 2024 | 2025-01-01 | våren 2025 |
| **SKV A 2025:8** (B-värden, nettoförsäljningsvärden) | 2025 | 2025 | våren 2026 |
| SKV A 2024:25 (föregående B-värden) | 2024 | 2024 | våren 2025 |

**Implementation:** hämta alltid värdena från aktuell föreskrift för det beskattningsår som hanteras — hårdkoda inte. Värdena justeras varje år och **strukturen kan ändras** mellan föreskrifter (se ändringstabellen nedan).

### A-värden från SKVFS 2025:27 (beskattningsår 2025)

Värden per styck om inte annat anges, kronor exklusive moms.

**Nötkreatur**:

| Kategori | Klass | Kronor |
|---|---|---|
| Mjölkkor | Mjölkras (oavsett vikt) | 14 800 /st |
| Dikor och amkor | Lätt köttras | 13 000 /st |
| Dikor och amkor | Tung köttras | 14 200 /st |
| Ungnöt (kvigor och kvigkalvar) | Under 1 år | 4 300 /st |
| Ungnöt | 1–2 år | 8 900 /st |
| Ungnöt | Över 2 år | 13 500 /st |
| Slaktnöt | Självrekryterande | 21,80 /kg |
| Slaktnöt | Inköpt slaktnöt, köttras | 34,90 /kg |

**Svin**:

| Kategori | Klass | Kronor |
|---|---|---|
| Avelssvin | Galtar och suggor (gyltor) | 3 540 /st |
| Smågrisar | yngre än 2 mån | 420 /st |
| Gödsvin | 2–4 mån | 790 /st |
| Gödsvin | 4–6 mån | 1 650 /st |

**Får**:

| Kategori | Klass | Kronor |
|---|---|---|
| Tackor och baggar | (per styck) | 1 100 /st |
| Lamm | (per kg levande vikt) | 20,20 /kg |

**Renar (SKVFS 2025:28, renskötsel)**: renkalv 1 442 /st, vuxen honren 2 359 /st, vuxen hanren 3 276 /st.

### B-värden från SKV A 2025:8 (beskattningsår 2025)

Nettoförsäljningsvärden (B). Används kollektivt — om totala B-summan ger ett lägre värde än A_summa × 0,85, värderas djurlagret till B-summan. Notera att 85 %-spärren INTE får tillämpas på B-värden.

**Nötkreatur**:

| Kategori | Klass | Kronor |
|---|---|---|
| Mjölkkor | Mjölkras | 22 700 /st |
| Dikor och amkor | Lätt köttras | 22 300 /st |
| Dikor och amkor | Tung köttras | 26 500 /st |
| Ungnöt | Under 1 år | 5 300 /st |
| Ungnöt | 1–2 år | 15 500 /st |
| Ungnöt | Över 2 år | 22 600 /st |
| Slaktnöt | Självrekryterande | 34,80 /kg |
| Slaktnöt | Inköpt slaktnöt, köttras | 37,80 /kg |

**Svin och får**: SKV A 2025:8 innehåller även dessa, men exakta värden bör hämtas från aktuell föreskrift vid implementation (FAR Online / Skatteverket).

### Strukturella ändringar 2024:28 → 2025:27 (viktigt för migrering)

| Område | SKVFS 2024:28 | SKVFS 2025:27 |
|---|---|---|
| Mjölkkor | Uppdelat per kg levande vikt (400/500/600/700 kg) | **En kategori** "Mjölkras" oavsett vikt |
| Dikor/amkor | Uppdelat per kg levande vikt | **Per ras**: lätt köttras / tung köttras |
| Gödnöt → Slaktnöt | "Gödnöt" per kg levande vikt | **Renamed "Slaktnöt"**, två kategorier: självrekryterande / inköpt köttras |
| Draghästar och unghästar | Egna kategorier med viktklasser | **Borttagna** ur föreskriften — värderas enligt allmänna lagerregler IL 17 kap utan SKV-schablon |
| Får | Per kg levande vikt (30/50/70/90 kg) | **Tackor/baggar per styck**, lamm per kg |
| Gödsvin > 6 mån | Egen kategori | **Borttagen** ur föreskriften |

Implementationsråd:
- Versionera lookup-tabellen per beskattningsår i koden — strukturändringar är inte bara värdejusteringar
- Mappa äldre kategorier vid migrering (t.ex. "mjölkko 600 kg 2024" → "mjölkras 2025"; "diko 700 kg 2024" → välj lätt/tung köttras 2025 baserat på rasinformation)
- Hästar och svin > 6 mån är borta ur 2025:27 — fallback till anskaffningsvärde/marknadsvärde med 85 %-spärr enligt IL 17 kap 5 §

### Tävlings- och ridhästar

**Undantag**: Skatteverkets schablonvärden för produktionsutgifter gäller **inte** för tävlings- eller ridhästar. Värdet får tas upp lägst till **85% av det lägsta av anskaffningsvärdet och allmänna saluvärdet**.

### Två beräkningar — välj det lägsta

För att få fram lägsta lagervärde:
1. Summera produktionskostnaden (Skatteverkets A-värden) för alla djur. Ta 85% av detta.
2. Räkna ut sammanlagda nettoförsäljningsvärdet (B-värden).

Lagervärdet = det **lägre** av de två. Nettoförsäljningsvärdet får INTE skrivas ner till 85%.

**Beräkningsmall** (siffror illustrativa, byt mot aktuella SKVFS/SKV A värden):

```
djur[]: lista av (antal, kategori, vikt/ålder)

A_summa = Σ(antal × A_värde(kategori, klass))   # produktionsutgift per SKVFS
B_summa = Σ(antal × B_värde(kategori, klass))   # nettoförsäljningsvärde per SKV A

A_85 = A_summa × 0,85          # nedskrivningsregeln 85 %-tak
B_kollektiv = B_summa          # nettoförsäljningsvärde får INTE skrivas ner till 85 %

lagervärde = min(A_85, B_kollektiv)
```

Exempel-beräkning för 6 dikor (tung köttras) + 6 ungnöt under 1 år + 2 ungnöt 1-2 år (SKVFS 2025:27 A-värden, illustrativa B-värden):
- A_summa = 6 × 14 200 + 6 × 4 300 + 2 × 8 900 = 85 200 + 25 800 + 17 800 = 128 800 kr; A_85 ≈ 109 480 kr
- B_summa ≈ 135 000 kr (kontrollera mot SKV A för aktuellt år)
- Lagervärde = **109 480 kr** (det lägre)

### Egenproducerat hö, halm, ensilage, spannmål

Anskaffningsvärdet för egenproducerat foder är svårt att räkna ut exakt eftersom Skatteverket inte publicerat schablonvärden för dessa lagertillgångar. Praktisk lösning vid bokslut: använd **marknadspris vid produktionstillfället** för respektive produkt och kvalitet (branschnoteringar från LRF, Lantmännen, Hushållningssällskapet eller motsvarande), justerat för det egenproducerades faktiska kvalitet. Värdet får aldrig sättas så lågt att det ger orealistisk vinst.

Eftersom officiella värden saknas är det viktigt att dokumentera **källan** för det använda marknadspriset i bokslutsbilagan, så att SKV kan följa beräkningen vid en eventuell granskning.

### Växande gröda

Utsäde, konstgödsel mm som vid slutet av året finns i jorden (s.k. **fältinventarier**) ska **inte** behandlas som lager. Anses höra till **fastigheten**.

Detsamma gäller växande gröda och skog som ännu inte är avverkad eller framkörd till bilväg.

## Inventarier — lantbruks-specifika regler

### Förbrukningsinventarier — halvt PBB

Inventarier med anskaffningsvärde < halvt prisbasbelopp → direktavdrag. **2026: 29 600 kr (PBB 59 200 / 2). 2025: 29 400 kr (PBB 58 800 / 2)**. 2020: 23 650 kr. *Obs:* PBB för 2025 är **58 800 kr**, inte 57 900 (det var 2024).

För inventarier som **äga gemensamt** av flera näringsidkare (enkelt bolag): beloppsgränsen gäller för inventariet i sin helhet, **inte** delägarens andel.

### Naturligt samband

Inventarier med funktionellt samband, anskaffade tillsammans, räknas som en enda anskaffning. Detta påverkar gränsvärdet på halvt PBB.

Examples:
- En verkstol med tillhörande fångstgrindar
- En maskin med tillhörande kringutrustning
- En skogsvagn med tillhörande kran
- Delleveranser av inventarier
- Grindar för att hägna in en utfodringsplats till nötkreatur

För större lantbruk: verkstadsutrustning + verktyg, kontorsinventarier, inventarier till djurstallar **bedöms för sig** — inte som en enda anskaffning.

### Byggnadsinventarier — viktigt kategoriskt

Viss utrustning i ekonomibyggnaderna skrivs av som inventarier trots att den är mer eller mindre fast monterad i byggnaden:
- Bås, boxar, spiltor, båsavskiljare, foderbord och fodergrindar
- Vattenkoppar
- Spaltgolv samt utrustning för skrap- eller svämutgödsling med gödselplatta och urin- eller svämbrunn
- Mjölkningsanläggningar
- Pumpar
- Ledningar för elektrisk ström, vatten och avlopp som är avsedda för driften (men INTE för vanlig belysning — det är byggnad)
- Fläktar och ventilationsanläggningar
- Silo- och torkanläggningar
- Fasta transportörer och hissar
- Anslutningsavgifter

### Markinventarier

Markinventarier kallas en markanläggning som är avsedd att användas tillsammans med vissa maskiner eller andra inventarier i jordbruksdriften:
- Stängsel, grindar, bommar, räcken och färister
- Vissa utomhusbelägna gödselbassänger, urinbrunnar eller liknande anläggningar som inte har något samband med någon byggnad
- Dagbrunnar med kulvertar
- Bevattningsanläggningar i jord
- Reningsanläggningar och andra anläggningar för vattenvård
- Lantbruksberoende utomhusledningar (el-, vatten- och avloppsledningar)

### Markanläggningar — avskrivningssatser

Markanläggningar skrivs av med fast årlig procent (planenlig, inte restvärdes):
- **10%/år**: täckdiken och skogsvägar
- **5%/år**: övriga markanläggningar (öppna diken, stängsel om de inte är markinventarier, bevattningsanläggningar i jorden, övriga, etc.)

### Avskrivning av byggnader — skattemässiga satser

Skatteverkets vägledande procentsatser för värdeminskningsavdrag (SKV A 2005:5, ej tidsbegränsad) för byggnader på lantbruksenhet:

| Byggnadstyp | Skattemässig %/år | Implicit nyttjandeperiod |
|---|---|---|
| Bostadshus (småhus och hyreshus) | 2 | 50 år |
| Växthus, silor och kylhus | 5 | 20 år |
| Övriga ekonomibyggnader (stall, lador, maskinhallar) | 4 | 25 år |

### Skillnad mot bokföringsmässig avskrivning per K-regelverk

| Regelverk | Avskrivning i räkenskaperna | Avvikelse mot skattemässig |
|---|---|---|
| **K1** (förenklat årsbokslut för EF, BFNAR 2006:1) | Formellt samband: bokföringsmässig = skattemässig sats | **Ingen** — satserna ovan används direkt |
| **K2** (mindre AB, BFNAR 2016:10) | Nyttjandeperiod, men förenkling tillåter SKV-satser | Vanligtvis **ingen** i praktiken |
| **K3** (större AB, BFNAR 2012:1) | Faktisk nyttjandeperiod + obligatorisk komponentavskrivning | **Avviker nästan alltid** — ekonomibyggnad 40–60 års nyttjandeperiod (1,7–2,5 %/år) jämfört med skattemässig 4 %/år → kräver dubbla register och uppskjuten skatt |

## Skogsavdrag — skattemässig vs bokfört värde

Skogsavdrag **bokförs INTE i räkenskaperna**. Det är en ren skattemässig justering som görs på N8 + NE R25.

**Konsekvens**: Det bokförda värdet på skogsfastigheten (B7a i ruta-2196 räntefördelningsbilagan) blir större än det skattemässiga värdet (B7b). Skillnadsbeloppet (negativt) — sk **B7c** — påverkar kapitalunderlaget.

**Räkneexempel (illustrativt)**:
```
bokfört_värde_fastighet = anskaffningsvärde − bokförda_avskrivningar    # → B7a på sid 2196
skattemässigt_värde    = anskaffningsvärde − bokförda_avskrivningar − ack_skogsavdrag    # → B7b
skillnad_B7c           = skattemässigt − bokfört = − ack_skogsavdrag    # negativ post i kapitalunderlaget
```
Exempel: bokfört 518 400 kr, ack_skogsavdrag 45 000 kr → skattemässigt 473 400 kr → B7c = −45 000 kr. Skogsavdraget bokförs aldrig, så B7c korrigerar för att fastighetens skattemässiga omkostnadsbelopp har minskat utan motsvarande bokföringspost.

## Ersättningsfond (IL 31 kap)

Ersättningsfond är en lantbrukspecifik (och delvis generell) skattekredit. Hindrar orimliga skattekonsekvenser för den som får engångsersättning för något som är avdragsgillt genom avskrivning.

### Fyra typer av ersättningsfonder

Avdrag för avsättning till ersättningsfond får göras för:
- **Inventarier** (inte immateriella tillgångar som mjölkkvoter, stödrätter)
- **Byggnader och markanläggningar**
- **Mark**
- **Djurlager i jordbruk och renskötsel**

### Skadeersättning eller tvångsförsäljning som triggrar

Avsättning får göras om ersättningen avser:
- **Skada** genom brand eller annan olyckshändelse på inventarier, byggnader, markanläggningar, mark och djurlager
- **Expropriation** eller liknande tvångsförsäljning
- Avyttring vid förhållanden som måste anses som tvångsavyttring (oligonable conditions for staying)
- Avyttring som ett led i åtgärder för **jordbrukets eller skogsbrukets yttre rationalisering**
- Avyttring till staten på grund av att fastigheten på grund av flygbuller inte går att bo på utan påtaglig olägenhet
- Inskränkning av förfoganderätten för obegränsad tid med stöd av miljöbalken eller motsvarande författningar, förutsatt att ersättningen är en engångsersättning

### Avdragets storlek

Får avsättas högst ett belopp som motsvarar ersättningen som tagits upp i inkomstdeklarationens näringsbilaga.

**Specialfall — fastigheter**: Vid avyttring av näringsfastighet beskattas kapitalvinsten normalt i kapital. Säljaren får dock välja att lägga beskattningen i NV, just för att kunna utnyttja ersättningsfond. RÅ 2010 ref 38 (2010-03-30) klargjorde att man får lägga bara en så stor del av kapitalvinsten i näringsverksamheten som behövs för att täcka avsättningen.

Dock: för ålderspensionärer är inkomstskatt + egenavgifter ofta lägre än 30% kapitalskatt, och då lönar sig inte denna teknik.

### Vad fonderna får tas i anspråk för

| Ersättningsfond för | Får tas i anspråk för |
|---|---|
| **Inventarier** | Avskrivning av och utgifter för underhåll/reparation av inventarier; nedskrivning av djurlager |
| **Byggnader och markanläggningar** | Avskrivning av och utgifter för underhåll/reparation av byggnader och markanläggningar (som är kapitaltillgångar); avskrivning av och utgifter för underhåll/reparation av inventarier; nedskrivning av djurlager |
| **Mark** | Anskaffning av mark som är kapitaltillgång |
| **Djurlager** | Nedskrivning av djurlager. Fonden får tas i anspråk med högst ett belopp som motsvarar utgifterna under beskattningsåret för att anskaffa djur. Nedskrivningen får inte leda till att lagret tas upp till ett lägre värde i dess helhet vid beskattningsårets slut än som annars skulle ha godtagits. |

### Användningstid — förlängd 2026: 3 år → 10 år

**Skogsskattereformen 2026 (prop. 2025/26:69, ikraft 2026-04-01)** förlängde användningstiden för ersättningsfond:
- **Före 2026-04-01**: avsättningen måste användas inom **3 år** från avsättningsåret. Dispens kunde medges i ytterligare högst 3 år.
- **Fr.o.m. 2026-04-01**: avsättningen får användas inom **10 år**. Detta gäller också nya avsättningar gjorda från reformens ikraftträdande. (Övergångsregler för befintliga fonder — kontrollera mot SKV vid behov.)

I annat fall återförs den till beskattning i deklarationen som lämnas för det tionde (tidigare tredje) beskattningsåret efter det att avdraget gjordes.

**Dispens**: Vid sjukdom, lågkonjunktur eller liknande kan Skatteverket medge dispens i ytterligare högst 3 år (oavsett om grundtiden är 3 eller 10 år).

### Tillägg vid återföring av annan orsak

När avdraget återförs ska ett särskilt **tillägg på 30%** av det återförda beloppet tas upp som intäkt i det inkomstslag återföringen görs i. Detta är för att avskräcka från att ta ut skattekredit utan att ha för avsikt att göra investeringen.

Tillägg vid återföring även om:
- Fonden tas i anspråk för något annat än tillåtet
- Den huvudsakliga delen av näringsverksamheten överlåts
- Den huvudsakliga delen av näringsverksamheten tillfaller en eller flera nya ägare genom arv, testamente eller bodelning
- Den som har fonden upphör att driva näringsverksamhet
- Innehavaren av fonden försätts i konkurs

Tillägget gäller **inte** vid expropriation och liknande.

### Inkomstslag för återföringen

| Anledning till fonden | Återföring i inkomstslag |
|---|---|
| Byggnader och markanläggningar i samband med expropriation | NV den del som ursprungligen togs upp i NV; resten i kapital |
| Mark | Normalt **kapital** |
| Övriga | NV |

### BAS-mapping för ersättningsfond

Ersättningsfond skiljer sig från periodiseringsfond och expansionsfond: **den måste bokföras via resultaträkningen för att avdraget ska vara giltigt** (gäller även för EF under K1, undantag mark). Detta är **motsatsen** till P-fond/expansionsfond i EF som aldrig bokförs.

```
Debit  8xxx Avsättning till ersättningsfond  (resultatpåverkande)
Credit 2060 Ersättningsfond                  (skuld-/eget kapitalsida)
```

- **I förenklat årsbokslut**: avsättningen bokförs i resultatet + upplysning i **ruta U3** (Ersättningsfond vid årets slut).
- **Undantag: ersättningsfond för mark** behöver inte bokföras enligt BFNAR 2006:1 9.2 — endast U3-upplysning.
- Detta ändrades **inte** av Skogsskattereformen 2026 — bokföringskravet kvarstår; däremot förlängdes användningstiden från 3 till 10 år (se skogsbeskattning.md).

## Räntefördelning — lantbruksspecifika regler

(General mechanics in `swedish-ef-skatteplanering`. This section covers only the lantbruks-specific deviations.)

### Tillgångar — lantbruksspecifika

Vid beräkning av kapitalunderlag för räntefördelning räknas i lantbrukskontext (IL 33 kap 8-12 §§):

| Tillgångstyp | Hur räknas |
|---|---|
| Inventarier och immateriella tillgångar | Skattemässigt restvärde (efter både planenlig avskrivning OCH överavskrivningar om vanligt årsbokslut) |
| Lager och kundfordringar | Det värde som gäller i inkomstdeklarationen (inkl. utländsk valuta) |
| **Fordringar på betalningsplan** | **0% — räknas INTE in** (eftersom obeskattade pengar, IL 2 kap 31§) |
| Momsfordran | Räknas in |
| **Skogskonto / skogsskadekonto** | **50%** av behållningen |
| Insatsemissioner | Räknas **inte** in |
| Andelar i handelsbolag | Räknas **inte** in (alltid) |
| Medlemsinlåning till producentföreningar | Räknas in (lantbruks-specifikt) |
| Näringsdelen av lantbruksfastigheten | Hela bokförda värdet (huvudregel) ELLER alternativregel (se nedan) |

### Alternativ värderingsregel för fastigheter (IL 33 kap 13§)

Vid äldre fastighetsinnehav är anskaffningsvärdet ofta lågt och svårt att räkna ut skattemässigt restvärde för. Alternativt får anskaffningsvärdet räknas ut som **viss del av taxeringsvärdet för 1993**:

| Fastighetstyp | % av taxeringsvärdet 1993 |
|---|---|
| Småhusenheter | 54% |
| Hyreshusenheter | 48% |
| Industrienheter | 64% |
| **Lantbruksenheter** | **39%** av den del som inte är småhusenhet eller tomtmark till småhusenhet |

Värdeminskningsavdrag och liknande avdrag (t.ex. skogsavdrag, substansminskningsavdrag, avskrivning mot ersättningsfond, investeringsfond) som gjorts i deklarationen åren **1982-1993**: ska dras av från det framräknade anskaffningsvärdet, men bara för de år som det har varit minst 10% av den framräknade delen av taxeringsvärdet.

Värdeminskningsavdrag och liknande som gjorts i deklarationen **1994 och senare**: ska minska anskaffningsvärdet oavsett belopp.

### Övergångspost från negativt kapitalunderlag 31 december 1993

Om man hade negativt kapitalunderlag för räntefördelning 31 december 1993 fastställdes en **övergångspost** som var lika stor som det negativa underlaget. Övergångsposten kan vara hur liten som helst — inget gränsbelopp på 50 000 kr.

Varje år får sedan övergångsposten läggas till (dvs i princip räknas som tillgång) när underlaget för räntefördelning fastställs. Övergångsposten följer med vid bodelning, arv, gåva eller testamente om hela näringsverksamheten överlåts.

### Särskild post vid räntefördelningen

Vid benefika förvärv (gåva, arv, testamente, bodelning) av lantbruksfastighet under taxeringsvärdet → mottagaren tar över givarens (låga) ingångsvärde → lånar för att betala för fastigheten → **negativt kapitalunderlag**.

**Lösning**: Kapitalunderlaget för räntefördelning får ökas med en **särskild tilläggspost** = skillnaden mellan vederlaget för fastigheten och det högsta av fastighetens värde enligt huvudregeln eller alternativregeln tidigare i kapitlet.

Den särskilda posten kan därmed aldrig leda till positiv räntefördelning utan är endast till för att förhindra negativ räntefördelning på grund av fastighetsförvärvet. Så snart kapitalunderlaget utan tillägget blivit noll eller positivt något år, upphör rätten att använda tilläggsposten, även om kapitalunderlaget senare blir negativt.

### Särskild post vid expansionsfond

Övertar förvärvaren expansionsfond i samband med övertagandet, ska den särskilda posten ökas med **79,4 % av den övertagna expansionsfonden** (= 100 % − 20,6 % expansionsfondsskatt; bolagsskatten är 20,6 % sedan 2021). Den övertagna expansionsfonden räknas inte som vederlag för fastigheten. Äldre källor anger 72 % / 27,7 % baserat på den tidigare 21,4 %-bolagsskatten — kontrollera alltid mot aktuell sats.

## N8-blanketten — skogs- och substansminskningsavdrag

Underbilaga till NE (enskilda näringsidkare), INK2 (AB), INK3 (ekonomiska föreningar) eller INK4 (HB). **Inte** själva beräkningen — Skatteverket beräknar inte beloppen. N8 är ett spårverktyg.

### N8 A. Skogsavdrag

**A1. Begärt skogsavdrag för beskattningsåret**: belopp förs till
- NE R25 (enskilda näringsidkare)
- INK2 sid 2 punkt 4.11
- INK3 sid 2 punkt 7.7
- INK4 sid 4 punkt 4.6

**A2. Återfört skogsavdrag**: Om fastighet eller fastighetsdel sålts och skogsavdrag som hör till området återförs vid kapitalvinstberäkningen. Förs till:
- NE R26 (eller NEA R19)
- INK2 punkt 4.12
- INK3 sid 2 punkt 7.8 eller INK4 punkt 4.6

**A3. Ökat/minskat avdragsutrymme på grund av förvärv/överlåtelse**:
- Ökat avdragsutrymme vid förvärv av fastighet/fastighetsdel
- Minskat avdragsutrymme vid avyttring av fastighet/fastighetsdel

Skatteverkets ställningstagande Återföring av skogsavdrag, 2007-06-13, Dnr 131 265526-07/111: Avdragsutrymmet är det högsta belopp som fastighetsägaren får dra av under innehavstiden. Därmed ska gjorda skogsavdrag inte minska avdragsutrymmet. När summan av alla gjorda skogsavdrag är lika stort som avdragsutrymmet finns det inget skogsavdrag kvar att utnyttja.

### N8 B. Substansminskningsavdrag

Samma struktur (B1, B2, B3) men för naturtillgångar.

- **B3** ökar också på grund av exploateringskostnader och kännedom om framtida återställningskostnader.
- Minskning på grund av utvinning under året.

### BSKA — Beräkningsbilaga för skogsavdrag

Egen sammanställning som inkluderas i deklarationsprogrammet BL Skatt och andra. Inte officiell Skatteverketsblankett. Innehåller:

**Sid 1 — Beräkning av avdragsgrundande anskaffningsvärde**:
- Totalt anskaffningsvärde × (skogsbruksvärde / totalt taxeringsvärde) = anskaffningsvärde för skogen
- Korrigering för delöverlåtelser om hela året: ideell andel eller fysisk andel
- Anskaffningsvärde för skogsdelen
- Övertagen andel %
- Anskaffningsvärde efter överlåtelse
- Medgivna avdrag före överlåtelse
- Medgivna avdrag minskas med (övertagen andel %)
- **Avdragsutrymme = anskaffningsvärde × 50%** (eller × 25% för juridisk person)
- Tidigare avdrag − årets avdrag = **kvarvarande avdragsutrymme**

**Sid 2 — Avdragsutrymme vid förvärv genom arv, gåva eller bodelning**:
- Föregående ägares anskaffningsvärde × andel %
- Föregående ägares skogsavdrag
- Avdragsutrymme

**Sid 2 — Beräkning av årets avdragsgrundande skogsintäkt**:
- Rotpostförsäljning / avverkningsuppdrag
- Avyttrade skogsprodukter
- Uttagna skogsprodukter
- ×60% för leveransvirke och uttag
- = Summa avdragsgrundande skogsintäkt

**Sid 2 — Årets skogsavdrag**:
- Rationaliseringsförvärv (kryssruta)? Om JA: max 100% av avdragsgrundande skogsintäkt.
- Annars: max 50% av avdragsgrundande skogsintäkt, dock ej över återstående avdragsutrymme.
- Yrkat skogsavdrag → förs till N8 A1.

### Blankett N7

Används vid övertagande av skogskonto eller skogsskadekonto i samband med arv, gåva eller bodelning. Anmäls till Skatteverket.

## Blankett NEA

Används om man har **flera självständiga näringsverksamheter** och vill särredovisa dem. T.ex. om man har separat bokföring för olika delar av lantbruket.

Slutresultatet från NEA förs över till NE i ruta R18 eller R19 sid 2.

## Bokföring av specialposter

### Skogsavdrag

Skogsavdrag bokförs **inte** i löpande bokföring. Yrkas på N8/BSKA. Beloppet förs sedan till sid 2 på blankett NE ruta R25.

### Insättning på skogskonto

Skogskontot är en tillgång (ruta B9 i förenklat årsbokslut eller balansposten "Bankmedel"). Avdraget för insättningen görs på sid 2 NE ruta R28 — INTE i löpande bokföring.

### Uttag från skogskonto

Uttaget är en intäkt i NV. Tas upp i ruta R27 på sid 2 NE.

### Periodiseringsfond, expansionsfond, ersättningsfond i EF

- **Periodiseringsfond och expansionsfond**: **bokförs INTE** i räkenskaperna för enskilda näringsidkare. De är skattemässiga konstruktioner i NE-bilagan. Upplysning lämnas i ruta U1 (P-fond) respektive U2 (expansionsfond) i förenklat årsbokslut.
- **Ersättningsfond**: **ska bokföras via resultaträkningen** för avdragsrätt (debit 8xxx / credit 2060). Detta är motsatsen till P-fond/expansionsfond. Upplysning i ruta U3. Undantag: ersättningsfond för mark behöver inte bokföras (BFNAR 2006:1 9.2).

I ruta U4 lämnas upplysning om bokförda tillgångar/intäkter som helt eller till viss del är obeskattade — det gäller skogskonto, insatsemission och betalningsplan på skog. Själva saldot på skogskonto bokförs alltid i B9 (Kassa och bank); U4 markerar bara att framtida uttag blir skattepliktig NV-intäkt.

## Cross-references

- General räntefördelning, expansionsfond, periodiseringsfond mechanics → `swedish-ef-skatteplanering`
- Anställda i lantbruket → `swedish-payroll`
- Förenklat årsbokslut + öppningsbalansräkning → `swedish-year-end-closing`
- SIE-export för lantbruksbokföring → `swedish-sie-import-export`
- Vanlig moms → `swedish-vat`
