# Lantbruksspecifik moms

General moms compliance covered by `swedish-vat`. This file covers only **lantbruksspecifika undantag och specialfall** — particularly hög/låg moms-gränsdragningar, solcellsmoms (HFD 2019), hästverksamhet, avverkningsuppdrag med kontantmetod, förskott, samt momslyft i uppbyggnadsskedet.

## Yrkesmässighet — momsregistrering

Den som har en näringsfastighet (lantbruksenhet) anses **yrkesmässig**, men det räcker INTE enligt Skatteverket. Enbart innehav av en näringsfastighet, utan avsikt att bedriva en verksamhet som medför momspliktig omsättning, är inte tillräckligt för att registrera ägaren till mervärdesskatt och för att medge momslyft.

Skatteverkets ställningstagande **2007-06-29, Dnr 131 604139-06/111** — Yrkesmässighet vid innehav av näringsfastighet mm.

För att vara säker på att få bli momsregistrerad bör du alltså kunna bevisa att du kommer att ha (eller redan har haft) momspliktig försäljning i verksamheten.

## Hög eller låg moms?

Tre momsnivåer i Sverige: **25%, 12%, 6%**.

### Skogsprodukter

Skogen ger **råvaror** som inte är livsmedel → **25% moms** på alla skogsprodukter:
- Virke
- Massaved
- Skogsbränsle (flis)
- Energiskog från skogsbruk
- Julgranar och dekorationsgrönt
- Vid, om från skogsbruk

### Jordbruksprodukter

Jordbruksprodukter avsedda att förtäras av människor → **6 % livsmedelmoms** (tillfälligt sänkt från 12 % under perioden **1 april 2026 – 31 december 2027** enligt prop. 2025/26:55). Övergångsregel: leveransdatum styr satsen, inte fakturadatum.

| Produkt | Moms 2026-04-01 → 2027-12-31 | Moms före 2026-04-01 och fr.o.m. 2028-01-01 |
|---|---|---|
| Levande djur (slakt- och livdjur), när säljs till slakteriet | **25 %** (djuren är ännu inte livsmedel) | 25 % |
| Kött (på gården eller direkt till konsument) | **6 %** | 12 % |
| Mjölk (oavsett mottagare) | **6 %** | 12 % |
| Spannmål, frukt, rotfrukter, grönsaker — avsedda att förtäras av människor | **6 %** | 12 % |
| Spannmål, frukt etc. avsedd för djurfoder | **25 %** | 25 % |
| Energigrödor för energiproduktion | **25 %** | 25 % |
| Fisk och skaldjur (alltid livsmedel) | **6 %** | 12 % |
| Bär, frukter, grönsaker — själv-plock (livsmedel) | **6 %** | 12 % |
| Sädeskärvar för utfodring av fåglar (inte människoföda) | **25 %** | 25 % |

### Direktförsäljning till konsumenter

All försäljning av livsmedel direkt till konsumenter (gårdsbutik, granne, marknad, REKO-ring etc.) → **6 % under perioden 2026-04-01 till 2027-12-31** (annars 12 %), oavsett om man säljer en gris, halv ko eller kvarn.

Det du säljer betraktas då som livsmedel, inte råvara — oavsett om det är spannmål, mjöl, kött eller mjölk.

### Servering / catering

Servering på plats (restaurang/servering, oavsett tillagat eller utlevererat) behåller **12 %** även under sänkningsperioden — den tillfälliga 6 %-sänkningen gäller **inte servering**. Vin, sprit och starköl: 25 % som vanligt.

**Avhämtning / take-away** behandlas som livsmedelsförsäljning → **6 %** under sänkningsperioden (annars 12 %). Gränsdragningen mellan servering och avhämtning blir därför viktig att kunna styrka.

### Egna uttag (uttagsmoms)

Om du tar ut tjänster eller varor för egen del ur lantbruket:
- Uttag av **varor** → momsen beräknas på **inköpspriset** (eller självkostnadspriset om inget inköpspris finns).
- Uttag av **tjänster** → momsen beräknas på kostnaden för att tillhandahålla tjänsten. Om en varas marknadsvärde är lägre än inköpspriset används marknadsvärdet vid uttagsmomsberäkningen.
- I inkomstdeklarationen värderas uttagen till **marknadspris**.
- Uttag av livsmedel från lantbruket till dig själv, din familj och närstående → **6 % moms under 2026-04-01 till 2027-12-31** (annars 12 %).

**Räkneexempel (uttag kött, slaktnöt självrekryterande)**:

Uttag av eget slaktat nötkött, slaktvikt 300 kg, för privat konsumtion.

```
inkomstdeklaration (förmånsvärde):
  marknadsvärde_inkl_moms = 30 kr/kg     # exempelpris
  moms_andel (6 % baklänges) = 6 / 106 = 5,66 %
  förmånsvärde_exkl_moms = 30 × (1 - 0,0566) ≈ 28,30 kr/kg
  totalt_förmånsvärde = 300 × 28,30 = 8 490 kr

uttagsmoms (utgående moms):
  # marknadsvärde används INTE — använd produktionskostnad enligt SKVFS
  # Slaktnöt självrekryterande SKVFS 2025:27: 21,80 kr/kg levande vikt
  levande_vikt = 2 × slaktvikt = 600 kg
  uttagsvärde = 600 × 21,80 = 13 080 kr
  utgående_moms = 13 080 × 0,06 = 785 kr        # 6 % under 2026-04-01 → 2027-12-31
  # (12 % före 2026-04-01 och fr.o.m. 2028-01-01: 13 080 × 0,12 = 1 570 kr)
```

Notera asymmetrin: marknadspris styr **inkomstdeklarationen** (förmånsvärde), medan produktionsutgift från SKVFS styr **uttagsmomsen**. Det är vanligen mer förmånligt för näringsidkaren än ett enhetligt marknadsvärde.

## Att lyfta moms — undantag

Den moms du som momsredovisande jord- och skogsbrukare betalar får du (med vissa undantag) tillbaka från Skatteverket. På vissa utgifter får du INTE lyfta momsen, trots att utgiften hör till skogs- eller jordbruksdriften.

### Undantag

1. **Mangårdsbyggnaden och andra byggnader som är stadigvarande bostäder** även om de är näringsfastigheter (förbudet mot momslyft på stadigvarande bostad).
2. **Personbilsmoms i lantbruket (förmånsbil)** vid inköp: ingen lyft. Bara på löpande utgifter för personbilen (drivmedel, reparationer) får du lyfta momsen. Du ska inte heller redovisa moms när du säljer personbilen. På leasingutgifter för personbil får du lyfta **halva** momsen (om bilen används minst 100 mil/år i företaget).
3. **Köp från privatperson, ideell förening eller någon annan som inte redovisar moms** — ingen ingående moms att lyfta. Men du ska redovisa utgående moms om du senare säljer tillgången.
4. **Ingångsinventarier och ingångslager** — sådant som du först haft i den enskilda firman vid starten och som du tidigare haft privat: ingen ingående moms att lyfta. Men du ska redovisa utgående moms om du senare säljer tillgången.
5. **Hö till privata ridhästar**: om du köper hö till din privata ridhäst får du varken dra av utgiften för höet eller lyfta momsen.

### Säljarens momsregistreringsnummer

För att du ska få lyfta momsen på en utgift måste momsen finnas angiven i kronor på kvittot eller på fakturan. Säljarens momsregistreringsnummer ska finnas med på kvittot eller fakturan.

## Hästverksamhet på lantbruksfastighet — yrkesmässighet

Hästhållning ingår **inte** automatiskt i näringsverksamheten, även om hästen eller hästarna finns på lantbruksfastigheten. Skatteverket bedömer **vinstsyfte** för hästverksamheten separat.

**Utveckling 2024**: HFD slog 2024 fast att tävling med trav-/galopphäst mot **garanterad startpeng** utgör ekonomisk verksamhet, och Skatteverket har sett över sitt ställningstagande. En trav-/galoppverksamhet med betydande garanterade startpengar kan därmed numera vara momspliktig även om den tidigare hade bedömts som hobby. Läs de äldre ställningstagandena nedan mot den bakgrunden.

Räcker det inte (verksamheten räknas som **privat**), kan företaget inte få lyfta moms på den del av verksamheten som hör till privathästeriet, varken på anskaffningar eller löpande utgifter. Inte heller på inredning och reparationer i lantbrukets ekonomibyggnader som används för den privata hästhållningen.

**Skatteverkets ställningstaganden**:
- **Avdrag för hästhållning vid innehav av jordbruksfastighet**, 2007-02-12, Dnr 131 104860-07/111
- **Yrkesmässighet vid innehav av näringsfastighet mm samt fråga om sponsorbidrag**, 2007-06-29, Dnr 131 604139-06/111

### Hästar som utnyttjas både i NV och privat

Två metoder som ger samma slutresultat:
1. **Du lyfter momsen på allt**. Sedan återför du den privata delen av momsen som ett **eget uttag** (uttagsmoms).
2. **Du lyfter bara den del av momsen som hör till NV**. Resten ingår i den privata utgiften. Ingen uttagsbeskattning.

### Hobbyhästar momslyft trots hobbyverksamhet

KR i Jönköping mål 2575-2578-08 — en man som sysslade med grävning som extraarbete, utan vinstsyfte, köpte i en ny traktor. Kammarrätten gjorde bedömningen att det handlade om ekonomisk verksamhet eftersom mannen hade (begränsade) intäkter. Han fick därmed lyfta den ingående momsen på traktorn.

## Solceller på lantbruk — moms

Beskattningen styrs av **vad anläggningen ska leverera el till**.

Skatteverkets ställningstagande **131 44577-17/111**:

| Scenario | Beskrivning | Momslyft |
|---|---|---|
| **All el levereras in på elnätet mot ersättning** | Anläggningen i sin helhet kommer användas i momspliktig verksamhet | **100%** |
| **Leverans av el till både mangårdsbyggnad och ekonomibyggnad** där momspliktig verksamhet bedrivs. Solcellerna är installerade på en ekonomibyggnad. Endast överskottet säljs till ett elhandelsföretag. | Eftersom el inte bara levereras till en byggnad som omfattas av förbudet mot momslyft på stadigvarande bostad, har man rätt att lyfta en del av momsen. Samma bedömning görs om solcellerna installeras på mangårdsbyggnaden för att leverera el till båda byggnaderna. | **DELVIS** — den del som hör till ekonomibyggnaden |
| **Installerad på mangårdsbyggnad** — el levereras enbart till den byggnaden, som är stadigvarande bostad. Endast överskottet ska säljas till ett elhandelsföretag. | Syftet med installationen får anses vara att anläggningen ska leverera el till byggnaden. Eftersom anläggningen kommer att leverera el till en byggnad som avser stadigvarande bostad gäller förbudet för momslyft på stadigvarande bostad. | **INGEN** |

Bedömningen blir densamma om installationen görs på ekonomibyggnaden eller på annan plats på jordbruksfastigheten för att enbart leverera el till mangårdsbyggnaden.

### HFD-domen 2019 — rättsläge för momslyft

**HFD 2019 ref. 50** (HFD 2019-10-25, mål nr 6174-18, 6175-18 och 6177-18) klargjorde att även en mycket liten momspliktig användning (försäljning av överskottsel) kan ge rätt till momslyft på en proportionerlig del av installationen. Målet gällde en bostadsrättsförening; principen tillämpas analogt på solcellsanläggningar på lantbruksfastighet.

Bedömningen kvarstår oförändrad enligt Skatteverkets nuvarande vägledning (Rättslig vägledning utg. 2024.5, dok 394014 — *Beskattningskonsekvenser för den som har en solcellsanläggning på sin jordbruksfastighet*), som **ersätter** tidigare ställningstaganden:
- 2018-03-01, dnr 202 90662-18/111 (avdragsrätt vid inköp och installation)
- 2017-12-20, dnr 202 492055-17/111 (jordbruksfastighet)
- 2017-12-20, dnr 202 492052-17/111 (villa/fritidshus som privatbostad)
- 2020-11-10, dnr 8-112186 (samma rubrik, äldre version)

**ML 1994:200 → ML 2023:200** trädde ikraft 1 juli 2023. Gamla paragrafhänvisningar i ovan ställningstaganden är inaktuella men den rättsliga bedömningen är oförändrad.

### Grönt avdrag på lantbruksfastighet — två elabonnemang krävs

För att privatbostadsdelen ska få **skattereduktion för grön teknik** (grönt avdrag) på en solcellsinstallation måste Skatteverket kunna säkerställa att den egenproducerade elen **i princip endast** kommer småhuset (mangårdsbyggnaden) tillgodo.

**Praktiska kravet (Skatteverket fr.o.m. 2024-03-22)**: **två separata elabonnemang/elmätare** krävs på fastigheten — ett för småhuset, ett för ekonomibyggnad/näringsdelen. Solcellsanläggningen ska vara ansluten till småhusets abonnemang.

Bakgrund: tidigare tillämpade Skatteverket en **schablon på 5 %** — om högst 5 % av producerad el bedömdes "spilla över" till annan byggnad kunde grönt avdrag ändå medges. Denna schablon **upphörde 2024-03-22**. Nuvarande krav är fysisk separation av elnäten.

Konsekvens för typsituationer:

| Scenario | Grönt avdrag möjligt? |
|---|---|
| Solceller på småhus + småhus har eget elabonnemang separat från ekonomibyggnad/stall | **JA** |
| Solceller på småhus, gemensamt elabonnemang för småhus + hönsstall (elvärme i stallet) | **NEJ** — utan separat mätning antas el "spilla över" till näringsdelen |
| Solceller på ekonomibyggnad, levererar bara till näringsverksamhet | Ingen grönt avdrag (näringsfastighet), men momslyft enligt HFD 2019 |
| Solceller med viss leverans till båda byggnader | Proportionerligt momslyft för näringsdelen; **inget grönt avdrag för småhusdelen** utan separat mätning |

### Energiskatt

- Installerad toppeffekt < **500 kW** (gränsen höjdes från 255 kW 2021) → undantag från energiskatt på egenförbrukad el.
- All el som överförs till koncessionspliktiga elnätet → energiskatt ska betalas. Det är dock i regel köparen av den el som överförs till det koncessionspliktiga elnätet som ska redovisa energiskatten på denna del.

### Skattereduktion för såld förnybar el — SLOPAS 2026-01-01

Den s.k. **60-öres-regeln** (skattereduktion för mikroproduktion av förnybar el, max 18 000 kr/år vid utbetalning för upp till 30 000 kWh) **avskaffas 1 januari 2026** (riksdagsbeslut SkU17 2024/25, prop. 2024/25:109).

Praktisk effekt för lantbruk med solcellsanläggning som säljer överskott:
- Tidigare: 60 öre/kWh skattereduktion på upp till 30 000 kWh sålda → max 18 000 kr/år
- 2026 och framåt: 0 kr — endast spotpris från elhandelsföretaget + eventuell elcertifikat-/ursprungsgaranti-ersättning
- Övriga skatteregler (moms enligt tabellerna ovan, inkomstbeskattning som NV om monterat på näringsbyggnad) gäller fortsatt

### Grönt avdrag — sats och tak

Subventionsgrad (lagstadgad):
- Före 2025-07-01: **20 %** av arbets-/materialkostnad
- Fr.o.m. 2025-07-01: **15 %** av arbets-/materialkostnad

Tak: max **50 000 kr/år** per person i grönt avdrag (kombinerat för alla grön-teknik-installationer).

De effektiva procentsatser som ofta citeras (**19,4 % före / 14,55 % efter**) uppstår när bara 97 % av en typisk faktura räknas som kvalificerad — 20 % × 97 % = 19,4 % och 15 % × 97 % = 14,55 %. Detta är effektiva fakturareduktioner, inte lagstadgad sats. Skatteverket har också (2024-08) klargjort att **växelriktare** räknas till de 15 %-kvalificerade kostnaderna, inte separat högre sats som vissa leverantörer marknadsförde.

Avdraget gäller **bara privatpersoner**, inte näringsverksamhet. För **näringsfastighet** finns inget grönt avdrag — istället sker momslyft (per HFD 2019 och dnr 131 44577-17/111) och NV-avdrag för anskaffningen som inventarium eller byggnadsinventarium.

Lantbrukare med privatbostadsdel av lantbruksfastighet kan utnyttja grönt avdrag *för den privata delen* — men endast om kravet på två elabonnemang ovan är uppfyllt.

## Förskott på leveransvirke — moms vs inkomstskatt-asymmetri

När du får förskott för virke som du varken levererat eller fått inmätt:
- **Inkomstskatt**: Du tar upp förskottet som en **skuld**, ej intäkt. Du behöver alltså inte skatta för beloppet förrän du levererar virket eller får det inmätt.
- **Moms**: Du ska däremot redovisa **moms på det** om den som har betalat ut förskottet har specificerat moms på kvittot eller fakturan. Skattskyldighet vid förskott uppkommer enligt momslagen (ML 2023:200, 7 kap.) vid leverans av "**bestämd och beställd vara**" — i skogskontexten är varan *beställd* (avtal med virkesköparen finns) även om volymen/kvaliteten inte är *bestämd* förrän vid avverkning/inmätning. När säljaren har angett moms på fakturan har Skatteverkets praxis varit att betrakta omständigheterna som tillräckligt identifierade för att momsen ska redovisas direkt vid förskottet.
- **Skogsavdrag/skogskonto**: Förskottet är **inte underlag** för skogsavdrag och inte heller underlag för insättning på skogskonto.

Denna asymmetri mellan moms (omedelbar) och inkomstskatt (väntar tills inmätning) är en specialfall som måste hanteras manuellt i bokföringsprogram.

## Avverkningsuppdrag och kontantmetoden

Om du kommer överens med köparen om att likviden för en avverkningsrätt ska fördelas på flera år (**betalningsplan**), får du redovisa inkomsterna **kontantmässigt** för inkomstskatt — du skattar bara för de pengar du fått in under året.

Det är likadant med momsen — **du ska bara redovisa momsen på den likvid du fått under året**. Detta är ett undantag från huvudregeln att moms ska redovisas vid leverans/inmätning.

Detta är en av få fall där moms och inkomstskatt följer varandra (kontantprincipen i båda).

## Arrende och moms

- **Jordbruksarrende**: 25% moms.
- **Jakt- och fiskearrende**: 25% moms.
- **Tomtarrende** (bostadsarrende eller lägenhetsarrende): **MOMSFRITT**.

Arrendatorn (vid jordbruksarrende) får lyfta hela momsen på arrendet, även om värdet av bostad ingår i arrendet. Däremot får arrendatorn inte i inkomstdeklarationen dra av en kostnad för den del av arrende-avgiften som hör till bostaden.

## Momsen i uppbyggnadsskede

Normalt har ett företag rätt att lyfta moms på sina utgifter först från och med att företaget har sin första momspliktiga omsättning, dvs sin första försäljning, och är momsregistrerat.

Du kan dock ansöka om att få återbetalning av moms **innan verksamheten gett några intäkter**. Det måste vara fråga om **nödvändiga utgifter** för att dra igång verksamheten, exempelvis köp av en maskin.

Företaget kan också lyfta momsen på utgifterna när företaget är i uppbyggnadsskedet om företaget är momsregistrerat. Missa därför inte att så snabbt som möjligt lämna in Företagsregistrering till Skatteverket för att få företaget momsregistrerat. Att företaget är i ett uppbyggnadsskede är ett **särskilt skäl** för att en momsregistrering ska beviljas, även om företaget inte har haft eller kommer att ha någon omsättning inom den närmaste tiden.

KR i Jönköping (1115-08, 1170-08): Verksamhet under uppbyggnad kan generera momslyft även när det dröjer flera år innan momspliktiga intäkter uppkommer.

## Momsredovisning för lantbruk

Beskattningsunderlag (totala momsbelagda inkomsterna exklusive moms):
- **≤ 1 MSEK**: helår, momsdeklaration **senast 12 maj** året efter beskattningsåret (eller 26 februari året efter om EU-handel skett).
- **1-40 MSEK**: kvartal eller månad (lantbrukare väljer ofta månad om man har stora investeringar och vill få tillbaka moms snabbare).
- **> 40 MSEK**: månad.

### Faktureringsmetoden vs bokslutsmetoden

För lantbrukare:
- **Faktureringsmetoden**: bokföra fakturorna när de skickas / mottas. Moms redovisas direkt.
- **Bokslutsmetoden** (kontantmetoden): bokföra fakturorna när de **betalas**. Räcker för nettoomsättning ≤ 3 MSEK. Vid räkenskapsårets slut tas obetalda fakturor med (matchning).

De flesta små lantbruk använder bokslutsmetoden + förenklat årsbokslut.

## Privata hästar — momslyft

Privata ridhästar/sporthästar på lantbruksfastigheten räknas som **privat** användning. Konsekvens:

- Ingen momslyft på utgifter som rör hästhållningen (foder, veterinär, etc.).
- Ingen momslyft på inredning och reparationer i lantbrukets ekonomibyggnader som används för privata hästhållningen.
- Om en byggnad används både för momspliktig verksamhet och privat hästhållning: proportionering av momslyften.

Skatteverkets ställningstaganden:
- Dnr 131 104860-07/111
- Dnr 131 604139-06/111

## Cross-references

- General momsregler, rutor 05-62, omvänd skattskyldighet → `swedish-vat`
- Tomtarrende, lägenhetsarrende, fastighetsmoms allmänt → `swedish-vat`
- Solceller på privatbostad (kapital) — inte i denna skill, se kapital-skattning
- Momsfri försäljning vid uttag till anställd kost → `swedish-payroll`
