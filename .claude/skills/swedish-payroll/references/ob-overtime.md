# OB-tillägg, övertid, mertid

Reference för obekväm arbetstid (OB), övertid, mertid och kompensationsledighet i svensk lönehantering.

<!-- toc -->
**Contents**

- [Legal basis](#legal-basis)
- [Övertid](#övertid)
- [Mertid (för deltid)](#mertid-för-deltid)
- [OB-tillägg (obekväm arbetstid)](#ob-tillägg-obekväm-arbetstid)
- [Skatt och avgifter](#skatt-och-avgifter)
- [BAS-kontering](#bas-kontering)
- [Vanliga implementationsfallgropar](#vanliga-implementationsfallgropar)
- [Cross-references](#cross-references)

<!-- /toc -->

## Legal basis

- **Arbetstidslagen (1982:673)** — tidsgränser för övertid och mertid (semitvingande; kollektivavtal kan avvika).
- **Semesterlagen (1977:480)** — semestervärde av övertidsersättning.
- **Inkomstskattelagen (1999:1229) 11 kap** — skatteplikt på lönetillägg.
- **Kollektivavtal (CBA)** — den faktiska procentsatsen och beräkningsmetoden för OB och övertid kommer nästan uteslutande från branschavtal, inte lag. Lag ger ramarna.

## Övertid

### Definition

Arbete utöver ordinarie arbetstid (heltid = ofta 40 tim/vecka, men kan vara 38 eller 36 enligt avtal). För deltid skiljs **mertid** (upp till heltid) och **övertid** (utöver heltid).

### Arbetstidslagens tak (när inget kollektivavtal gäller)

| Period | Max övertid |
|---|---|
| Per fyraveckorsperiod | 48 timmar |
| eller per kalendermånad | 50 timmar |
| Per kalenderår | **200 timmar** (allmän övertid) |
| Per kalenderår + extra övertid (särskilda skäl) | + 150 timmar = **350 timmar** |

ATL 8 § (allmän övertid) + 8 a § (extra övertid: kräver särskilda skäl och att situationen inte gått att lösa på annat rimligt sätt; ingen dispens behövs). Allmän och extra övertid får tillsammans inte överstiga 48 timmar per fyraveckorsperiod eller 50 timmar per kalendermånad. Nödfallsövertid (ATL 9 §) får tas ut i den utsträckning förhållandena kräver. Den sammanlagda arbetstiden får vara högst 48 timmar per sjudagarsperiod i genomsnitt under högst fyra månader (ATL 10 b §). Kollektivavtal kan höja eller sänka dessa nivåer.

### Övertidsersättning (typiska CBA-nivåer)

Lagen kräver INTE en specifik övertidsersättning — bara att övertid är begränsad. Kompensation följer kollektivavtal eller anställningsavtal:

| Tidsfönster | Vanlig ersättning (Unionen, Handels, Kommunal m.fl.) |
|---|---|
| Måndag–fredag 06.00–20.00, första 2 tim efter ordinarie arbetstid | **50 %** ovanpå timlönen |
| Måndag–fredag övrig tid + lördag/söndag/helg | **100 %** (kvalificerad övertid) |
| Allmänna helgdagar och natt (efter 22.00) | **100 %** ofta + OB-tillägg ovanpå |

### Beräkningsformel

```
timlön = (månadslön × 12) / (52 × ordinarie_arbetstid_per_vecka)
# Vanlig divisor enligt CBA: 175 tim/månad eller 40 × 52 ÷ 12 = 173,33 (varieras)
övertidsersättning_per_tim = timlön × (1 + övertidsprocent)

# Exempel: månadslön 32 000 kr, 40 tim/vecka, övertid 50 %
timlön = 32 000 / 175 = 182,86 kr
övertid_50 = 182,86 × 1,50 = 274,29 kr/tim
```

**Tjänsteman som "köpt bort övertid"** har ofta extra 5 semesterdagar eller högre lön i stället för rätt till övertidsersättning. Anställningsavtalet styr.

### Kompensationsledighet vs övertidsersättning

Övertid kan ersättas med **ledighet i stället för pengar** (komp-tid) om arbetsgivaren och arbetstagaren är överens. Vanliga växlingsfaktorer:

| Övertidstyp | Tim för tim → komp-tid |
|---|---|
| Enkel övertid (50 %) | 1 tim arbetad → 1,5 tim ledig |
| Kvalificerad övertid (100 %) | 1 tim arbetad → 2,0 tim ledig |

Komp-tid är **inte** semesterlönegrundande på samma sätt som pengar; semesterlöneskuld räknas på den faktiska lönen.

## Mertid (för deltid)

### Definition

Arbete utöver avtalad arbetstid men inom ordinarie arbetstidens ram (dvs. inte över heltid). Endast för **deltidsanställda** (under heltid enligt CBA).

### Tak enligt ATL 10–10 a §§

- **Allmän mertid** (10 §): max 200 tim/år
- **Extra mertid** (10 a §, särskilda skäl): + 150 tim → totalt **350 tim/år**. Allmän och extra mertid får tillsammans inte överstiga 48 tim per fyraveckorsperiod eller 50 tim per kalendermånad.

### Ersättning

Mertid betalas normalt med **vanlig timlön** (inget övertidstillägg). I vissa CBA dock 50 %-tillägg vid mertid som överstiger heltid.

## OB-tillägg (obekväm arbetstid)

### Definition

Tillägg utöver grundlön för arbete på obekväma tider — kvällar, nätter, helger, helgdagar. **Inget lagstadgat krav**, men nästan alla branschavtal har OB.

### Typiska OB-nivåer (varierar mellan CBA)

| Tidsfönster | Vanlig OB-nivå |
|---|---|
| Vardagar 18.00–22.00 (OB1) | ~25 % av timlönen som extra |
| Vardagar 22.00–06.00 (OB2/natt-OB) | ~50–75 % |
| Lördag 06.00–24.00 | ~50 % |
| Söndag + helgdag | ~75–100 % |
| Storhelger (jul, midsommar, etc.) | ~150 % |

**Skiftarbete** har ofta separat skifttillägg utöver eller i stället för OB.

### Beredskap (jour)

För personal som har **beredskapstid** (väntar på utkallning, t.ex. IT-jour, läkare i bakjour) gäller ofta:
- Beredskapsersättning per beredskapstimme (t.ex. 20–30 % av timlön)
- Vid utkallning: full timlön + eventuellt övertidstillägg från den minut man påbörjar arbetet

## Skatt och avgifter

### OB och övertid är skattepliktig lön

Båda räknas som **kontant bruttolön** i skattetabellsumma. Arbetsgivaravgifter 31,42 % och eventuell preliminärskatt dras som på vanlig lön. Inga undantag.

### AGI-rapportering

OB och övertid rapporteras inom **fältkod 011 "Kontant ersättning"** i AGI individrad. Ingen separat rad — det är samma bruttolöneflöde.

### Semesterlönegrundande

Övertidsersättning **är** semesterlönegrundande. Den ingår i lönesumman för procentregeln (12 %, SemL 16 b §) och räknas som rörlig lönedel (12 %) vid sammalöneregeln (SemL 16 a § tredje stycket). OB är också semestergrundande.

**Komp-tid (ledighet i stället för pengar) är INTE semesterlönegrundande** på samma sätt — bara den faktiska utbetalda lönen räknas.

## BAS-kontering

| BAS-konto | Användning |
|---|---|
| **7010** | Löner till kollektivanställda (inkl. OB och övertid för dem) |
| **7010** eller ett fritt konto i gruppen (t.ex. 7014) | Rörliga lönedelar — BAS 2026 har inget särskilt OB-konto, många bolag specialnoterar OB och övertid på ett eget konto för analys |
| **7210** | Löner till tjänstemän och företagsledare (inkl. övertid för dem som ej köpt bort) |
| **7210** eller ett fritt konto i gruppen (t.ex. 7214) | OB-tillägg, övertidsersättning tjänstemän (7212 är vinstandelar i BAS 2026, inte OB) |
| **2710** | Personalskatt (kredit, dras vid utbetalning) |
| **2730** | Arbetsgivaravgifter skuld (kredit, beräknas på OB + övertid 31,42 %) |
| **2920** | Upplupna semesterlöner (kredit, växer med 12 % av OB + övertid) |
| **7510** | Arbetsgivaravgifter (debet, kostnadsföring av 31,42 % på OB + övertid) |
| **7090** / **7290** | Förändring av semesterlöneskuld (kollektivanställda / tjänstemän) |

### Exempel-bokning (tjänsteman 32 000 kr/mån + 5 timmar övertid 50 %)

```
Övertid: 5 × 274,29 ≈ 1 371 kr brutto
Bruttolön totalt: 33 371 kr

Bokning (utbetalning):
Debit  7210 Löner tjänstemän         32 000
Debit  7212 Övertidsersättning        1 371
Credit 2710 Personalskatt            (skatteberäkning på 33 371)
Credit 1930 Bank                     (nettolön)

Arbetsgivaravgifter på övertid (31,42 % × 1 371):
Debit  7510 Arbetsgivaravgifter          431
Credit 2730 Arb.giv.avg. skuld           431

Semesterlöneskuld (12 % × 1 371):
Debit  7290 Förändring sem.löneskuld     165
Credit 2920 Upplupna semesterlöner       165
```

## Vanliga implementationsfallgropar

1. **Timlönsdivisorn varierar mellan CBA** — vissa använder 175, andra 173,33, andra månadsbaserad (160 × 12). Hårdkoda inte; konfigurera per anställningsavtal.
2. **OB-tillägg på övertidstillägg** — OB räknas normalt på *grundtimlönen*, inte på övertidsersättningen. Vissa CBA tillåter staplade tillägg.
3. **Komp-tid och semesterlön** — komp-tid är inte semestergrundande i sig, men om komp-tiden tas ut som ledighet och vid uttagstillfället utbetalas semestertillägg så ska systemet räkna rätt på bas-lönen.
4. **ATL-tak per kalenderår** — 200 timmar gäller per kalenderår, inte per anställningsår. Systemet måste hålla löpande räkning.
5. **Extra övertid/mertid** — kräver särskilda skäl (ATL 8 a §/10 a §), ingen dispens. Då gäller 350 tim/år. Kräver explicit konfiguration.
6. **Sjukdom under övertidsbetald period** — sjuklön är 80 % av den lön och de anställningsförmåner som arbetstagaren faktiskt gått miste om (SjLL 6 §), vilket kan omfatta övertid som arbetstagaren skulle ha arbetat. Kollektivavtal får bestämma den närmare beräkningen (SjLL 2 § andra stycket).
7. **Övertid efter semester eller frånvaro** — vissa CBA kräver att den anställde fullgjort full arbetsvecka innan övertidstillägg kan utgå.

## Cross-references

- Semesterlöneskuld på övertid → `vacation-pay.md`
- Sjuklöneberäkning interagerar med övertidshistorik → `sick-pay.md`
- AGI-rapportering av OB/övertid → `agi-filing.md`
- BAS-konton 7xxx → `bas-7xxx.md`
- Skatteavdrag → `tax-tables.md`
