# Skogsbeskattning (Forestry Taxation)

Special rules for skogsbruk under **IL 21 kap** (Inkomstskattelagen 1999:1229). Skogsbeskattning has three distinct tools that overlap and interact: skogsavdrag, skogskonto, and (via betalningsplan) periodisering of avverkningsrätt-intäkter.

## Intäkternas karaktär — three categories

The category determines how much of the income is *avdragsgrundande* (forming the base for skogsavdrag) and how much of it can be deposited on skogskonto.

| Intäktstyp | What it is | Skogsavdrag base | Skogskonto max insättning |
|---|---|---|---|
| **Avverkningsrätt** (rotpost/avverkningsuppdrag) | Buyer cuts and removes the timber. Seller is paid based on volume + grade. | 100% av likviden | 60% av likviden |
| **Leveransvirke** | Seller fells and delivers timber to the buyer's mätstation. | 60% av likviden (40% anses vara värdet av arbetet) | 40% av likviden |
| **Egna uttag av skogsprodukter** | Owner takes virke for own use, sales not in NV | 60% av marknadsvärdet | 40% av marknadsvärdet |

**Rotpost vs avverkningsuppdrag**:
- *Rotpost*: each tree measured and priced upfront at kontraktsskrivande. Rare today because of buyers' insistence on volume measurement after felling.
- *Avverkningsuppdrag* (leveransrotköp): paid per prislista on inmätt virke after avverkning, minus a fixed kr/m³sk fee for the buyer's avverkning + terrängtransport.

Both are *avverkningsrätt* in skattemässig mening and qualify for the 100%/60% bases above.

## Skogsplantering

Utgifter for anlagging av ny skog — plantsättning, markberedning, viltstängsel — are **direktavdragsgilla** in NV, despite the long-term value. (IL 21 kap 3§)

This is one of the few cases where future-value-creating utgifter are immediately deductible.

## Betalningsplan (IL 21 kap 2§)

Kontantprincipen — undantag från bokföringsmässiga grunder.

When a skogsägare upplåter en avverkningsrätt (avverkningsuppdrag eller rotpost) **och** the parties agree the payment will be split across multiple kalenderår, only the amounts actually received in a given year need to be taken up as inkomst.

Requirements:
1. Upplåtelse av avverkningsrätt (does NOT apply to leveransvirke or self-cut virke).
2. Payment must be split across at least **two kalenderår** (not just two tillfällen — different calendar years).
3. Frivilligt avsteg från huvudregeln — skogsägaren can choose to ta upp hela likviden direct istället.

Length of plan: typically 5-10 år. Some virkesköpare allow modifications during the avtalstid, others lock the schedule.

### Räntekompensation

Virkesköpare typically pay ränta on innestående medel på betalningsplan. Räntan beskattas som intäkt i NV (not kapital), is moms-fri, and follows the same rate as skogskonto-räntan from competing banks.

### Betalningsplan vid räntefördelning och expansionsfond

CRITICAL anomaly (IL 2 kap 31§): A fordran from betalningsplan is **not obeskattad** in skattemässig mening (the intäkt has not yet been beskattad). Therefore:
- Räntefördelning kapitalunderlag: **0%** of the betalningsplan-fordran. The fordran is NOT räknad as tillgång.
- Expansionsfond kapitalunderlag: same — 0%.
- Skogskonto, in contrast, enters kapitalunderlag at **50%** (the depositions ARE obeskattade since the intäkt was beskattad in samband med avräkning/inmätning).

**Implementation note**: A system that lets the user toggle between betalningsplan and skogskonto must recompute both kapitalunderlag — the choice has multi-year capitalunderlag effects.

### Betalningsplan can not be overlåten

IL 21 kap 2§ + Skatteverkets ställningstagande dnr 131 127228-08/111: A betalningsplan-fordran cannot be transferred to another taxpayer — the fordran is personlig till the original upplåtaren. **Exception**: Dödsbo after the upplåtaren can fortsätta tillämpa the betalningsplan.

### When is the intäkt beskattad?

HFD 2017 ref 58, 2017-10-20 (Mål om tidpunkten för beskattning av inkomst från upplåtelse av rätt att avverka skog): När skogsägaren INTE utnyttjar betalningsplan-möjligheten ska ersättningen från ett avverkningsuppdrag redovisas och beskattas **när virket inmäts** — NOT när avtalet skrivs och NOT när dellikvid betalas i förskott. Skälet är att äganderätten övergår när virket mäts in.

Detta innebär att ett förskott före inmätning ska redovisas som en **skuld** (ej inkomst). Likvid efter inmätning men före betalning är en **kundfordran**.

## Förskott på leveransvirke

Mottager skogsägaren förskott för virke som ännu inte levererats eller mätts in:
- **Inkomstskatt**: Förskottet är en **skuld**, ej intäkt. Tas upp som intäkt först när virket mäts in (eller köparen lämnar avräkning).
- **Moms**: Däremot ska moms redovisas på förskottet om den som betalat ut förskottet har specificerat moms på det. Asymmetri: moms redovisas i en period, inkomstskatt i en annan.
- **Skogsavdrag**: Förskott är **inte** underlag för skogsavdrag (och inte heller skogskonto). Endast när virket mäts in räknas det som avdragsgrundande skogsintäkt.

## Skogsavdrag (IL 21 kap 4-19 §§)

The grundläggande tanke: at sale of a skogsfastighet, an unfair tax effect would arise if the seller has been forced to skatta för all virke they sell, without being able to dra av the inköpspris på den rotstående virke they bought. Skogsavdraget addresses this.

### The two pillars

**Avdragsutrymme** (lifetime cap):
- Fysisk person + dödsbo: **50% of anskaffningsvärdet** for skog och skogsmark.
- Juridisk person (AB, HB, ekonomisk förening, stiftelse): **25%** of anskaffningsvärdet.

**Avdragsgrundande skogsintäkt** (per-year base):
- 100% av intäkter from avverkningsuppdrag (incl. avverkningsrätt, rotpost).
- 60% av intäkter from leveransvirke + egna uttag.

**Årets skogsavdrag** = max **50% av avdragsgrundande skogsintäkt** (gäller alla fysiska personer).

Combined effect: max year-skogsavdrag = 50% of (100% of avverkningsuppdrag) + 50% of (60% of leveransvirke) = up to 50% of avverkningsuppdrag-likvid OR 30% of leveransvirke-likvid.

### Anskaffningsvärdet — three methods to calculate

**1. Ren skogsfastighet**: anskaffningsvärdet = vad du betalt för hela fastigheten. Simple.

**2. Blandad fastighet (huvudregel — schablonregeln efter taxeringsvärdet)** (IL 21 kap 12§):
   - anskaffningsvärdet för skogen = (köpeskillingen × skogsbruksvärdet / totala taxeringsvärdet)
   - Example: Fastighet köpt för 800 000 kr. Taxeringsvärde 550 000 kr varav skogsbruksvärde 110 000 kr. Anskaffningsvärde skog = 110 000 / 550 000 × 800 000 = 160 000 kr.

**3. Jämkningsregeln** (IL 21 kap 13§): Om det är uppenbart att schablonregeln ger missvisande värde, tillåts proportionering efter särskild värdering (intyg from Skogsstyrelsen eller registrerad fastighetsmäklare). Värderingen ska vara i kronor, inte procent — men man bedömer hur stor *andel* av totala värdet som ligger i skog och skogsmark.

Justifiable jämkning:
- Brist på avverkning sedan taxeringsvärdet fastställdes (skogen har vuxit) → högre skogsvärde
- Vikande marknad på åkermark eller byggnader
- Felaktigheter i tidigare fastighetstaxering
- Stora framtida återväxtåtgärder ogjorda

### Anskaffningsvärde — what counts?

Anskaffningsvärdet excludes:
- Lagfartskostnader (stämpelskatt 1.5% + expeditionsavgift)
- Mäklarkostnader
- Fastighetsbildningsutgifter
- ...EXCEPT vid rationaliseringsförvärv where lagfartskostnaden FÅR ingå.

Vid omarrondering: utgifter för lantmäteriförrättning som är ett led i yttre rationalisering ska INTE räknas in i anskaffningsvärdet (de är direkt avdragsgilla i NV).

### Arv och gåva

- Vid arv och gåva: mottagaren övertar givarens/arvlåtarens *anskaffningsvärde* (och hur mycket skogsavdrag som redan utnyttjats). No indexuppräkning.
- Vid delöverlåtelse (gåva of part): mottagarens del = (mottagarens fastighetsdel/hela fastigheten) × givarens anskaffningsvärde. Givarens kvarvarande anskaffningsvärde minskas motsvarande.
- Om delen är liten — mindre än 20% av skogsvärdet — ingen anskaffningsvärde alls för mottagaren; givarens anskaffningsvärde är oförändrat.
- Om värdet av all skog och skogsmark i överlåtarens NV är **mindre än 20%** av det överlåtna området, får mottagaren inget anskaffningsvärde alls.

### Arv vs köp — Skatteverkets klassificering

1. Arvinge tillskiftas → arv.
2. Arvinge löser ut alla andra dödsbodelägare och betalar arvskifteslikvid → arv (även om transaktionen kallas köp).
3. Arvinge köper fastigheten av dödsbo där hen är delägare, och köpet INTE görs i samband med arvskifte: andelen som motsvarar arvtagarens andel i dödsboet = arv; resten = köp.
4. Efterlevande make tillskiftas i bodelning, sedan sälja vidare till annan dödsbodelägare: upplägg för skatteflykt → bedöms som arv enligt punkt 3.
5. Arvinge tillskiftas en fastighet med lågt underlag för skogsavdrag och säljer till make med pris under kapitalvinsttaket: godkänns som rent köp.

### Rationaliseringsförvärv (IL 21 kap 10§)

Fysisk person som förvärvar skog som ett led i jord- och skogsbrukets yttre rationalisering får under de **första fem åren** efter förvärvet dra av **100% av avdragsgrundande skogsintäkten** (i stället för 50%).

Conditions (Skatteverket dnr 131 80453-13/111):
- Den tidigare ägda fastigheten får inte redan vara en rationell brukningsenhet (gräns: 400 hektar produktiv skogsmark).
- Det får inte vara för stort avstånd mellan fastigheterna (gräns: vägavstånd högst 3 mil).
- Den tidigare ägda eller den förvärvade fastigheten ska öka arealen produktiv skogsmark med minst **10%**.

NB: rationaliseringseffekten ökar bara *hastigheten* — det totala avdragsutrymmet (50% av anskaffningsvärdet) gäller fortfarande.

Lagfartskostnader **får** ingå i anskaffningsvärdet vid rationaliseringsförvärv.

### Avdragsbelopp — lägsta belopp

- **Egen ägare** (hel fastighet): lägsta avdrag/år **15 000 kr** (IL 21 kap 18§).
- **Delägare** (samägt): lägsta avdrag **3 000 kr** per delägare, men det beräknade avdraget för hela den gemensamt bedrivna verksamheten måste vara minst **15 000 kr**. En delägare får utnyttja skogsavdrag även om de andra avstår.
- Inget tak för enskilt år utöver 50%-regeln.

### Skogsavdrag minskar inte vid uttag från skogskonto

Uttag från skogskonto räknas inte som avdragsgrundande skogsintäkt (det är ju samma pengar som tidigare gett upphov till skogsavdrag). Insättning på skogskonto minskar INTE skogsavdraget i samma år; båda räknas på samma underlag.

### Avveckling av skogsmark — inget kvarvarande utrymme

När hela skogsmarken är avyttrad får inget skogsavdrag göras, även om avverkning sker på grund av förbehållen avverkningsrätt EFTER försäljning. Inget avdragsutrymme kvarstår.

## Framtida återväxtåtgärder

För den som **gör ett vanligt årsbokslut** (inte förenklat): avdragsgill avsättning i räkenskaperna för beräknade utgifter för kommande återväxtåtgärder (markberedning, plantering, skyddsdikning, slyröjning). När utgifterna senare uppkommer, är de redan avdragna och får inte dras av igen.

**Förenklat årsbokslut → INTE rätt till avsättning** för framtida återväxtåtgärder. Detta är den största nackdelen med förenklat årsbokslut för skogsägare. Alternativen för att uppnå samma skattekredit:
- Avsättning till **periodiseringsfond** (6 års skattekredit, max 30% av vinsten)
- Använda **betalningsplan** så att pengar står inne hos köparen — pengarna kan tas ut när återväxtåtgärderna utförs så att intäkter och kostnader möter varandra.

**Inte i samband med betalningsplan**: Om man redan har pengar innestående på betalningsplan, är detta tillräcklig skattekredit — får då inte dessutom göra avdrag för framtida återväxtåtgärder (RÅ 1997 ref 52).

## Energiskog

Försäljning av bränsle från energiskog (pil, sälg mm) på åkermark räknas som försäljning av gröda, inte skogsinkomst. Det innebär:
- INTE skogskontogrundande
- INTE underlag för skogsavdrag
- Beskattas som vanlig inkomst i NV.

## Skogskonto (IL 21 kap 21-37 §§)

Skattekredit på upp till 10 år. Pengar sätts in på ett särskilt bankkonto, avdrag görs i NE-blanketten, källskatt 15% dras av räntan vid utbetalningen, uttag tas upp som intäkt i NV.

### Skogskontots syfte

1. **Skatteutjämning mellan år** — kapa toppinkomster för att jämna ut den progressiva statliga skatten.
2. **Skattekredit** upp till 10 år (även utan progressivt utfall är skattekrediten värd ca 30%-marginalen × räntan).
3. **Skatteskyddat sparande** — 15% källskatt på räntan i stället för 30% på vanlig bankränta.

### Vem får sätta in?

Endast **människor och dödsbon** (IL 21 kap 21§). Aktiebolag, ekonomiska föreningar, handelsbolag → INTE. Anledningen är att skogskontot är konstruerat för att kapa progressivt utfall, vilket inte finns för juridiska personer.

### Lägsta insättningsbelopp

**5 000 kr** per delägare per beskattningsår. Om gemensamt bedriven verksamhet — beloppsgränsen 5 000 kr gäller var och en av delägarna (IL 21 kap 31§).

### Maxinsättning per år (IL 21 kap 25, 29 och 31 §§)

Summan av:
- **60%** av inkomster från avverkningsuppdrag eller avverkningsrätt
- **40%** av inkomster från virkesförsäljning (oavsett om du själv eller annan gör avverkningen)
- **40%** av värdet av egna uttag av skogsprodukter

Plus följande särskilda intäkter får ingå:
- Försäkringsersättning för skog eller virke
- Delutbetalning för avverkningsrätt enligt betalningsplan
- Utdelning från samfällighet som tas upp i skogsbruket

Uttag från skogskonto räknas **inte** som skogskontogrundande intäkt. Förskott för ej levererat eller inmätt virke får **inte** räknas med.

### Skogsskador — förhöjd insättning (skogsskadekonto)

Vid skogsskador (stormfällning, brand, insektsangrepp, kemiska skador eller liknande) som tvingat skogsägaren att avverka tidigare än önskat: förhöjd insättning är möjlig.

- **80%** av inkomster från avverkningsuppdrag/avverkningsrätt
- **50%** av virkesförsäljning, oavsett om du eller någon annan gör avverkningen

Villkor:
- Skadan ska ha gjort att mer än 1/3 av skogen bör avverkas tidigare än tänkt.
- Minst 75% av skogsintäkterna under året (inkl. försäkringsersättning) ska vara på grund av stormfällning, brand eller liknande.

Andra skador som ger förhöjd insättning: torka, svampangrepp, översvämning, skador genom industriutsläpp.

**Intyg krävs** från oberoende sakkunnig (t.ex. Skogsstyrelsen-tjänsteman, virkesköpare). Blankett SKV2464.

### Skogsskadekonto — skillnader mot vanligt skogskonto

- Lägsta insättning per år: **50 000 kr** (mot 5 000 kr för vanligt skogskonto).
- Pengar får stå kvar i **20 år** (mot 10 år för skogskonto).
- IL 21 kap 23, 24 och 31 §§.

### Bara ett konto per år och bank

Per beskattningsår, ett konto per skogsägare per bank. Skulle insättning ske på flera konton räknas bara den första insättningen som godkänd. Resten flyttas till vanligt bankkonto (RÅ 1979 1:52 — varje delägare måste ha eget konto för sin egen del).

Däremot: olika beskattningsår kan ha **olika** skogskonton (max 10 samtidigt eftersom max 10 år).

### Skogskontoräntan — specialbeskattning (källskatt)

**15% källskatt** på räntan. Banken drar av och betalar in till Skatteverket direkt — räntan syns INTE i deklarationen och får inte räknas in i preliminärskatten.

Effektiv skatt på skogskontot är dock högre när uttag sker:
- Vid uttag: hela beloppet (inklusive räntan, sedan banken redan dragit 15%) beskattas som inkomst av NV, alltså 0-60% beroende på age, marginalskatt, aktiv/passiv.
- Exempel: marginalskatt + egenavgifter = 50%. Insatt 100 000 kr, ränta 1% = 1 000 kr. Källskatt 15% × 1 000 = 150 kr. Resterande 850 kr beskattas med 50% = 425 kr vid uttag. Total skatt på räntan: 575 kr = 57.5%.

Räntan vid skogskonto är dock **delvis skatteskyddat sparande** jämfört med 30% kapitalskatt på en vanlig bankränta (om man inte skulle behöva räntan i NV).

### Uttagsregler

- Tidigast **4 månader** efter insättningen får uttag göras.
- Minsta uttag **1 000 kr** (såvida kontot inte avslutas).
- **10 år** från början av det år då senaste insättning gjordes — då måste banken avsluta kontot och betala ut.
- Exempel: insättning 2020 (deklaration 2021) → måste tas ut senast 2030 (deklaration 2031).

### Skogskonto vid fastighetsöverlåtelse

- Vid försäljning: skogskontot finns kvar oberoende av att fastigheten sålts. Uttag deklareras som passiv NV (när annan aktiv NV saknas) — vilket kan ge **24.26% löneskatt** istället för 10.21% egenavgifter för pensionärer (oförmånligt).
- Vid arv/gåva av hela lantbruksenheten: mottagaren får **överta** skogskontot. Insättning förs vidare med samma 10-årsfrist. Mottagaren tar sedan upp uttag till beskattning. Blankett N7 anmäler övertagandet.
- Skogskontot kan **inte** delas mellan flera mottagare vid arv eller gåva — det måste följa lantbruksenheten i sin helhet.
- Vid delöverlåtelse (arealförvärv): övertaget belopp = (kontobehållning × mottagarens ägarandel × taxeringsvärde för övertagen skogsmark / taxeringsvärde för all skogsmark).

### Pantsättning — INTE tillåten

Skogskontot får inte pantsättas eller på annat sätt lämnas som säkerhet. Den som upptäcker pantsättning ska genast beskatta hela kontobehållningen som uttag (IL 21 kap 36-37 §§).

Spärrning från Skogsstyrelsen för skogsvårdsåtgärder räknas inte som pantsättning.

### Felaktig insättning

Om Skatteverket nekar avdrag (för att underskott uppstår eller belopp överstiger 40/60% av intäkten):
- Skatteverket meddelar banken.
- Banken flyttar pengarna till vanligt bankkonto, även räntan (som då räknas som vanlig ränta i kapital).
- Ingen "fångenskap" på kontot om Skatteverket inte godkänner insättningen.

### Skogskonto vid räntefördelning och expansionsfond

Skogskontobehållningen får räknas in i kapitalunderlaget för räntefördelning och expansionsfond — men bara till **50%** av behållningen (medan vanliga bankkonton räknas till 100%).

**Implikation**: Att lägga upp skogspengar på ett likvidkonto i lantbruket är effektivare för räntefördelning än att låsa dem på skogskonto — men då förlorar man källskatten 15% och 10-årig skattekredit. Trade-off.

## Lager av skogsprodukter

Skogsprodukter värderas som andra lagervaror (IL 17 kap). Egenavverkat virke vid bilväg, som ännu inte mätts in för köparens räkning, ska tas upp som lager vid årets slut.

Är virket inmätt vid årsskiftet ingår det INTE i lagret — det är då i *köparens* lager. Likviden tas upp som en **kundfordran** (intäkt).

### BAS-konton lager skogsprodukter

| Konto | Användning |
|---|---|
| 1460 / 1465 | Lager skogsprodukter |
| 1469 | Inkuransavdrag 3% |

## N8-blanketten — Skogs- och substansminskningsavdrag

N8 är en underbilaga till NE (för enskilda näringsidkare), INK2 (AB), INK3 (ekonomiska föreningar) eller INK4 (HB). N8 är **inte** själva beräkningen — Skatteverket räknar inte ut beloppen själva, utan N8 är ett sätt att hålla reda på vilka avdrag som gjorts och på vilka fastigheter.

### N8 A. Skogsavdrag

- **A1. Begärt skogsavdrag för beskattningsåret**: belopp förs till NE R25 (eller motsvarande på INK2/INK3/INK4).
- **A2. Återfört skogsavdrag**: om fastighet sålts under året och skogsavdrag återförs vid kapitalvinstberäkningen. Förs till NE R26 (intäkt).
- **A3. Ökat/minskat avdragsutrymme**: vid förvärv ökas, vid avyttring minskas.

### N8 B. Substansminskningsavdrag

Samma struktur (B1, B2, B3) för naturtillgångar (grus, torv, bergtäkter).

### BSKA — Beräkningsbilaga för skogsavdrag

Egen sammanställning (deklarationsprogram BL SKATT, Visma, m.fl. inkluderar denna). Inte ett officiellt Skatteverketsformulär, men rekommenderat första gången skogsavdrag yrkas. BSKA-bilagan visar:
- Hur anskaffningsvärdet räknats ut (schablonregeln eller jämkningsregeln)
- Hur avdragsutrymmet räknats ut (50% × anskaffningsvärde, minus tidigare skogsavdrag)
- Årets avdragsgrundande skogsintäkter (rotpostförsäljning + 60% × leveransvirke)
- Yrkat skogsavdrag (max 50% av avdragsgrundande intäkten, eller 100% vid rationaliseringsförvärv)
- Kvarvarande avdragsutrymme

### Worked example (BSKA — Enar Gran)

Enar köpte sin skogsfastighet för 1 600 000 kr. Taxeringsvärde 1 100 000 kr, varav skogsbruksvärde 220 000 kr.

Anskaffningsvärde för skog = 1 600 000 × 220 000 / 1 100 000 = **320 000 kr**.

Avdragsutrymme = 320 000 × 50% = **160 000 kr**.

Under året:
- Avverkningsuppdrag 48 000 kr
- Uttag från betalningsplan (tidigare avverkningsuppdrag) 42 000 kr
- Total avdragsgrundande skogsintäkt = 48 000 + 42 000 = 90 000 kr

Maxavdrag = 50% × 90 000 = **45 000 kr**.

Yrkat: 45 000 kr på N8 A1 → NE R25.

Kvarvarande avdragsutrymme = 160 000 − 45 000 = **115 000 kr**.

## Rättsfall & ställningstaganden

| Källa | Innehåll |
|---|---|
| HFD 2017 ref 58 (mål 20 oktober 2017) | Tidpunkten för beskattning av inkomst från upplåtelse av rätt att avverka skog: vid inmätning, inte vid avtalsskrivning |
| RÅ 1979 1:52 | Varje delägare måste ha eget skogskonto — gemensamt konto för flera personer accepteras inte |
| RÅ 1988 ref 72 | Helt avdrag för insättning trots hälftenägare (om kontohavaren brukade hela fastigheten) |
| RÅ 1997 ref 52 | Avdrag för framtida återväxtåtgärder medgavs inte när skogsägaren även hade pengar innestående på betalningsplan |
| Skatteverkets ställningstagande dnr 131 551127-08/111 | Förenklat årsbokslut och betalningsplan på skog |
| Skatteverkets ställningstagande dnr 131 127228-08/111 | Överlåtelse av betalningsplan |
| Skatteverkets ställningstagande dnr 131 265526-07/111, 2007-06-13 | Återföring av skogsavdrag |
| Skatteverkets ställningstagande dnr 131 80453-13/111 | Definition av rationaliseringsförvärv |

## Quick-reference: per-intäktstyp summary

| Intäktstyp | % i skogsavdrag-bas | % på skogskonto | Skogsskadekonto-% | Moms |
|---|---|---|---|---|
| Avverkningsuppdrag (rotpost/avverkningsrätt) | 100% | 60% | 80% | 25% (skog är råvara) |
| Leveransvirke | 60% | 40% | 50% | 25% |
| Egna uttag skogsprodukter | 60% | 40% | (n/a) | 25% (uttagsmoms) |
| Energiskog från åker (pil, sälg) | 0% (inte skogsinkomst) | 0% | 0% | 12% om livsmedel, annars 25% |
| Försäkringsersättning skog | 0% (i regel) | räknas in i underlaget | 50%/80% | momsfri |
| Förskott innan inmätning | 0% (är skuld) | 0% (förskott räknas inte) | 0% | 25% (moms ändå) |
