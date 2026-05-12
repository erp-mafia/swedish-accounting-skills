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
- Lager med totalvärde ≤ 5 000 kr behöver inte tas upp som tillgång.
- Inventarier av mindre värde: halvt PBB-gränsen (29 600 kr för 2026, 28 950 för 2025) → direktavdrag.

Skogskontot tas upp som **tillgång i ruta B9** (vanligt årsbokslut) eller som **obeskattad reserv i ruta U4** (förenklat årsbokslut). I förenklat årsbokslut visas också skogsavdrag och betalningsplan-fordringar som **obeskattade poster** i ruta U-fältet.

## Djur som lager (IL 17 kap 5§)

**Alla djur i jordbruk och renskötsel ska betraktas som lager**, trots att vissa djur (t.ex. mjölkkor, ardennerhästar, avelsdjur) ekonomiskt påminner mer om anläggningstillgångar. Detta är ett **uttryckligt undantag** från huvudregeln.

**Undantag från undantaget**: Djur i andra verksamheter än jordbruk/renskötsel (t.ex. cirkus, djurparker) → **anläggningstillgångar**.

### Värderingsreglerna för djurlager

- Lägst **85% av produktionskostnaden** (specialregel för djurlager — vanlig lager: 97% efter 3%-schablonen).
- Eller lägst **kollektivt beräknat genomsnittligt nettoförsäljningsvärde** för samtliga djur — om detta ger ett **lägre** värde än 85% av produktionskostnaden.

**Skatteverket fastställer årligen schablonvärden** per djurslag, ålder/vikt och kategori. SKVFS 2017:21, allmänna råd SKV A 2017:20 (uppdateras årligen).

### Schablonvärden — exempel (inkomstår 2019, exkl. moms)

**A = genomsnittlig produktionsutgift, B = nettoförsäljningsvärde**

| Djurslag/kategori | A | B |
|---|---|---|
| Yngre draghästar (4-15 år) | 27 700 | 30 000 |
| Äldre draghästar (>15 år) | 24 700 | 15 000 |
| Föl unghäst | 10 200 | 12 500 |
| Ettåringar unghäst | 16 900 | 15 000 |
| Mjölkkor 400 kg | 7 600 | 8 100 |
| Mjölkkor 500 kg | 7 900 | 9 000 |
| Mjölkkor 600 kg | 8 200 | 10 000 |
| Mjölkkor 700 kg | 8 600 | 11 000 |
| Dikor 400 kg | 7 200 | 9 900 |
| Dikor 600 kg | 7 900 | 11 200 |
| Ungnöt under 1 år | 3 800 | 3 200 |
| Ungnöt 1-2 år | 5 900 | 7 800 |
| Ungnöt >2 år | 7 900 | 12 500 |
| Gödnöt (kr/kg levande vikt) | 17 | 18 |
| Galtar och suggor (gyltor) | 2 330 | 4 040 |
| Smågrisar <2 mån | 300 | 490 |
| Gödsvin 2-4 mån | 490 | 550 |
| Gödsvin >6 mån | 1 250 | 1 600 |
| Får 30 kg levande vikt | 720 | 920 |
| Får 90 kg levande vikt | 750 | 1 060 |

(Kontrollera SKV's aktuella föreskrift för innevarande beskattningsår — värdena uppdateras.)

### Tävlings- och ridhästar

**Undantag**: Skatteverkets schablonvärden för produktionsutgifter gäller **inte** för tävlings- eller ridhästar. Värdet får tas upp lägst till **85% av det lägsta av anskaffningsvärdet och allmänna saluvärdet**.

### Två beräkningar — välj det lägsta

För att få fram lägsta lagervärde:
1. Summera produktionskostnaden (Skatteverkets A-värden) för alla djur. Ta 85% av detta.
2. Räkna ut sammanlagda nettoförsäljningsvärdet (B-värden).

Lagervärdet = det **lägre** av de två. Nettoförsäljningsvärdet får INTE skrivas ner till 85%.

**Worked example**: Sven har 6 dikor (500 kg/styck) plus 6 ungnöt under 1 år och 2 ungnöt 1-2 år.

Produktionsutgift:
- 6 × 7 500 = 45 000
- 6 × 3 800 = 22 800
- 2 × 5 900 = 11 800
- Summa = 79 600. 85% = **67 660**.

Nettoförsäljningsvärde:
- 6 × 10 600 = 63 600
- 6 × 3 200 = 19 200
- 2 × 7 800 = 15 600
- Summa = **98 400**.

Lagervärde = **67 660 kr** (det lägre).

### Egenproducerat hö, halm, ensilage, spannmål

Anskaffningsvärdet för egenproducerat foder kan vara svårt att räkna ut exakt. Förslag på schablonvärden (från bokens författare — inte officiella värden):

| Produkt | kr |
|---|---|
| Hö per kg | 1.50 |
| Ensilage, mindre balar | 250 |
| Ensilage, större balar | 300 |
| Foderspannmål per kg | 1.50 |
| Halm per kg | 1.50 |

### Växande gröda

Utsäde, konstgödsel mm som vid slutet av året finns i jorden (s.k. **fältinventarier**) ska **inte** behandlas som lager. Anses höra till **fastigheten**.

Detsamma gäller växande gröda och skog som ännu inte är avverkad eller framkörd till bilväg.

## Inventarier — lantbruks-specifika regler

### Förbrukningsinventarier — halvt PBB

Inventarier med anskaffningsvärde < halvt prisbasbelopp → direktavdrag. 2026: 29 600 kr (PBB 59 200 / 2). 2025: 28 950 kr (PBB 57 900 / 2). 2020: 23 650 kr.

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

### Avskrivning av byggnader

| Byggnadstyp | %/år |
|---|---|
| Bostadshus (småhus och hyreshus) | 2 |
| Växthus, silor och kylhus | 5 |
| Övriga ekonomibyggnader | 4 |

(Skatteverkets allmänna råd för byggnader på lantbruksenhet — kan avvika från ÅRL/K3 som baseras på faktisk livslängd.)

## Skogsavdrag — skattemässig vs bokfört värde

Skogsavdrag **bokförs INTE i räkenskaperna**. Det är en ren skattemässig justering som görs på N8 + NE R25.

**Konsekvens**: Det bokförda värdet på skogsfastigheten (B7a i ruta-2196 räntefördelningsbilagan) blir större än det skattemässiga värdet (B7b). Skillnadsbeloppet (negativt) — sk **B7c** — påverkar kapitalunderlaget.

**Worked example (Enar Gran)**:
- Bokfört värde fastigheten 518 400 kr (B2/B3 på sid 1 NE → B7a på sid 2196)
- Skattemässigt värde 473 400 kr (B7b)
- Skillnad = −45 000 kr (förs in som minskning vid B-beräkningen)
- Detta är **skogsavdraget som gjorts** men ej bokförts → skattemässigt har fastighetens omkostnadsbelopp minskat med 45 000 kr.

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

### Återföring efter 3 år

Ersättningsfonden måste användas inom **3 år** från avsättningen. I annat fall återförs den till beskattning i deklarationen som lämnas för det tredje beskattningsåret efter det att avdraget gjordes.

**Dispens**: Vid sjukdom, lågkonjunktur eller liknande kan Skatteverket medge dispens i ytterligare högst 3 år.

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

Ersättningsfond är **inte** ett obeskattat reservkonto (skiljer sig från periodiseringsfond, expansionsfond, överavskrivningar). Det är en skattemässig konstruktion.

- I förenklat årsbokslut redovisas avsättningen som obeskattad reserv i ruta U-fältet (för transparens).
- I löpande bokföring: ingen specifik kontering — avdraget görs i deklarationen.

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

Övertar förvärvaren expansionsfond i samband med övertagandet, ska den särskilda posten ökas med **72% av den övertagna expansionsfonden** (= 100% − 27.7% expansionsfondsskatt). Den övertagna expansionsfonden räknas inte som vederlag för fastigheten.

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

Alla tre är **inte bokförda i räkenskaperna** för enskilda näringsidkare. De är skattemässiga konstruktioner i NE-bilagan. Däremot bör skogsägare som gör förenklat årsbokslut lämna upplysningar om dem i **ruta U1-U3** i bokslutet (för att visa banken och andra läsare hela bilden).

I ruta U4 lämnas upplysning om bokförda intäkter som helt eller till viss del är obeskattade — det gäller skogskonto, insatsemission och betalningsplan på skog.

## Cross-references

- General räntefördelning, expansionsfond, periodiseringsfond mechanics → `swedish-ef-skatteplanering`
- Anställda i lantbruket → `swedish-payroll`
- Förenklat årsbokslut + öppningsbalansräkning → `swedish-year-end-closing`
- SIE-export för lantbruksbokföring → `swedish-sie-import-export`
- Vanlig moms → `swedish-vat`
