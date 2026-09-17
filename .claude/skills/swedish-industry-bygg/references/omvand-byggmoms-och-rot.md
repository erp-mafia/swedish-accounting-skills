# Omvänd byggmoms och ROT

Industry reference for a Swedish construction company or tradesperson (bygg och hantverk). Two mechanisms dominate the daily bookkeeping: **omvänd betalningsskyldighet för byggtjänster** (B2B) and **ROT-avdrag via fakturamodellen** (B2C). Almost every invoice a byggföretag issues falls into one or the other.

General VAT mechanics live in `swedish-vat`; generic invoice content requirements live in `swedish-invoice-compliance`. This file covers only what differs for construction.

**Legal position stated: as in force 2026-09-17.** Every rate, amount and threshold below is labelled with the year it belongs to. Statutes were read in consolidated form on 2026-09-17 (IL consolidated to SFS 2026:1393, ML 2023:200 consolidated to SFS 2026:1025, HUSFL 2009:194 consolidated to SFS 2025:324). Account numbers and names are verified against the official BAS 2026 kontoplan (v 1.1). See [Sources](#16-sources).

## Table of contents

1. [Omvänd betalningsskyldighet: the two conditions](#1-omvänd-betalningsskyldighet-the-two-conditions)
2. [Which services are covered](#2-which-services-are-covered)
3. [Which buyers trigger it](#3-which-buyers-trigger-it)
4. [Decision table: charge VAT or not](#4-decision-table-charge-vat-or-not)
5. [Invoice, momsdeklaration and BAS on both sides](#5-invoice-momsdeklaration-and-bas-on-both-sides)
6. [Material versus service, mixed invoices, goods with installation](#6-material-versus-service-mixed-invoices-goods-with-installation)
7. [Machine hire and personaluthyrning](#7-machine-hire-and-personaluthyrning)
8. [Construction-specific VAT timing (fakturadatummetoden)](#8-construction-specific-vat-timing-fakturadatummetoden)
9. [ROT: what qualifies and who may claim](#9-rot-what-qualifies-and-who-may-claim)
10. [ROT: rate history, cap and the shared ceiling](#10-rot-rate-history-cap-and-the-shared-ceiling)
11. [ROT: fakturamodellen step by step](#11-rot-fakturamodellen-step-by-step)
12. [ROT: BAS entries, including a short payment from Skatteverket](#12-rot-bas-entries-including-a-short-payment-from-skatteverket)
13. [ROT documentation and an exhausted utrymme](#13-rot-documentation-and-an-exhausted-utrymme)
14. [Ask the user](#14-ask-the-user)
15. [Error patterns](#15-error-patterns)
16. [Sources](#16-sources)

---

## 1. Omvänd betalningsskyldighet: the two conditions

The rule sits in **ML 16 kap. 13 §** (mervärdesskattelagen 2023:200). It replaced 1 kap. 2 § första stycket 4 b in the old ML (1994:200) on 1 July 2023 — any code or note citing "1 kap. 2 §" is stale.

16 kap. 13 § first stycke: if a beskattningsbar person supplies a service listed in the second stycke, **the buyer** is liable for the VAT, provided 16 kap. 9 § (foreign supplier rule) does not apply and the buyer is

1. a beskattningsbar person who **"i sin ekonomiska verksamhet inte bara tillfälligt tillhandahåller sådana tjänster"**, or
2. another beskattningsbar person who supplies such services to a buyer under point 1 (the *mellanman* anti-avoidance limb).

Both tests must hold at the same time:

| Test | Question | Source |
|------|------|------|
| Service test | Is what I sell one of the listed byggtjänster performed on *fastighet*? | ML 16 kap. 13 § andra stycket |
| Buyer test | Does my buyer sell such services more than occasionally, or is it a mellanman reselling to one who does? | ML 16 kap. 13 § första stycket 1–2 |

Both true → invoice without VAT, buyer self-assesses. Either false → normal Swedish VAT (25 %).

The rule is **mandatory**, not optional. There is no election and no de minimis.

---

## 2. Which services are covered

ML 16 kap. 13 § andra stycket lists:

1. Services **avseende fastighet** that can be attributed to
   - mark- och grundarbeten
   - bygg- och anläggningsarbeten
   - bygginstallationer
   - slutbehandling av byggnader
   - uthyrning av bygg- och anläggningsmaskiner **med förare**
2. **Byggstädning**
3. **Tillhandahållande av personal** for the activities in 1 and 2

Skatteverket's published exclusions — these are *not* covered, so charge VAT normally:

- plantering och skötsel av grönytor
- fastighetsskötsel på uppdrag, inklusive mindre reparationer
- arkitektverksamhet, byggkonsultverksamhet, projektledning
- uthyrning av bygg- och anläggningsmaskiner **utan förare**

### SNI: guidance, not a test

Skatteverket states that the SNI headings (SNI 2002 in particular) are *vägledande* for judging which services fall inside the list, but is explicit that **the seller's own registered SNI-kod is irrelevant**: "Det saknar helt betydelse vilken verksamhet ditt företag huvudsakligen bedriver eller vilken näringsgrenskod (SNI-kod) företaget har fått vid registreringen." A plumber registered under SNI 43.22 and a holding company with SNI 70.10 apply exactly the same test to the same job.

Do not reason "we are not a construction company, so this does not apply". Reason from the service and the buyer.

### Must be work on fastighet

The service must be performed on what ML treats as fastighet: land, buildings and constructions fixed to the ground, integrated components without which the building is incomplete (doors, windows, roofs, stairs, lifts), and equipment permanently installed such that removal damages or alters the building.

Work on something that is *not* fastighet is outside the rules — Skatteverket names a ship, a car, an entreprenadmaskin and a **tillfällig manskapsbod** as examples. Repairing a site cabin is a normal VAT-charged service even between two byggföretag.

Installation or montering of a vara **is** a bygg- och anläggningstjänst if the item becomes fastighet through the work. Reparation or underhåll of something that already is fastighet is likewise covered.

---

## 3. Which buyers trigger it

| Buyer | Reverse charge? | Note |
|------|------|------|
| Byggföretag that sells byggtjänster more than occasionally | **Yes** | Even if it is the slutkund and the work is on its own office property |
| Company that resells the purchased byggtjänst to such a byggföretag (mellanman) | **Yes**, both legs | ML 16 kap. 13 § första stycket 2 |
| Private person | **No** | Charge 25 % VAT; consider ROT |
| Bostadsrättsförening (own maintenance, sells no byggtjänster) | **No** | Charge VAT |
| Fastighetsbolag / hyresvärd that only manages its own stock | **No** | Charge VAT |
| Staten (any myndighet) | **Yes** | The state is one legal person and is treated as selling byggtjänster more than occasionally |
| Kommun eller region | **Normally no** | Only if that specific kommun itself sells byggtjänster more than occasionally. Kommunalförbund and kommunala bolag are separate persons — test each |
| Foreign company buying work on a Swedish fastighet | **Yes** | The buyer must then register for Swedish VAT and file momsdeklaration |

"Inte bara tillfälligt" has no statutory threshold. Skatteverket's operational advice: **if you are unsure, ask the buyer whether it sells byggtjänster**, and keep the answer. A written confirmation on the order or in the contract is the practical evidence.

The buyer does not have to resell the purchased service. A byggföretag renovating its own head office still buys under reverse charge.

---

## 4. Decision table: charge VAT or not

| # | Situation | Treatment | Seller account |
|---|------|------|------|
| 1 | Listed byggtjänst on fastighet, buyer sells byggtjänster more than occasionally | No VAT, "omvänd betalningsskyldighet" | **3231** |
| 2 | Same service, buyer is a mellanman reselling to such a buyer | No VAT, both legs | **3231** |
| 3 | Same service, buyer is a private person | 25 % VAT, ROT may apply | **3001** |
| 4 | Same service, buyer is a non-construction company or BRF | 25 % VAT | **3001** |
| 5 | Arkitekt-, konsult- or projektledningstjänst to a byggföretag | 25 % VAT | **3001** |
| 6 | Machine hire **without** operator to a byggföretag | 25 % VAT | **3001** |
| 7 | Machine hire **with** operator to a byggföretag | No VAT | **3231** |
| 8 | Pure sale of material to a byggföretag, no installation | 25 % VAT | **3001** |
| 9 | Byggstädning (slutstädning before inflyttning) to a byggföretag | No VAT | **3231** |
| 10 | Removal of byggavfall as the main content of the assignment | 25 % VAT | **3001** |

Row 10: Skatteverket holds that a service which mainly consists of collecting and hauling away byggavfall is not byggstädning under these rules.

---

## 5. Invoice, momsdeklaration and BAS on both sides

### The seller's invoice

- No VAT amount and no VAT rate on the construction lines.
- The notation **"Omvänd betalningsskyldighet"** must appear (ML 17 kap. 24 § p. 14 — the wording in ML is *uppgiften omvänd betalningsskyldighet*). "Omvänd skattskyldighet" is the pre-2023 phrasing; update templates.
- The **buyer's VAT registration number** must be stated (ML 17 kap. 24 § p. 4).
- **ML 17 kap. 25 §**: where the buyer is liable, the items in 24 § 9–11 (beskattningsunderlag per skattesats, tillämpad skattesats, momsbelopp) may be omitted; the invoice must instead state the beskattningsunderlag for the goods or services with a reference to the description under 24 § 7.
- All other mandatory fields from `swedish-invoice-compliance` still apply.

If VAT was charged by mistake, issue an **ändringsfaktura** for the incorrectly debited VAT. Do not leave it and net it later — felaktigt debiterad moms is payable to the state under ML until the invoice is corrected.

### Momsdeklaration

| Party | Ruta | Content |
|------|------|------|
| Seller | **41** | Försäljning när köparen är betalningsskyldig i Sverige (net amount) |
| Buyer | **24** | Övriga inköp av tjänster i Sverige där köparen är betalningsskyldig (net amount) |
| Buyer | **30** | Utgående moms 25 % on that purchase |
| Buyer | **48** | Ingående moms (full deduction if the buyer has full avdragsrätt) |

The seller reports no output VAT at all on the transaction. The buyer must report **both** ruta 30 and ruta 48 — silent netting of the two is prohibited even though the net effect is zero.

### BAS 2026 accounts

| Side | Account | BAS 2026 name |
|------|------|------|
| Seller, revenue | **3231** | Försäljning inom byggsektorn, omvänd betalningsskyldighet moms |
| Buyer, cost (services) | **4425** | Inköp av tjänster i Sverige, omvänd betalningsskyldighet, 25 % moms |
| Buyer, cost 12 % / 6 % | **4426** / **4427** | Same series, other rates |
| Buyer, cost (goods under reverse charge) | **4415** | Inköp av råvaror och material i Sverige, omvänd betalningsskyldighet, 25 % moms |
| Buyer, output VAT | **2614** | Utgående moms omvänd betalskyldighet, 25 % |
| Buyer, input VAT | **2647** | Ingående moms omvänd betalningsskyldighet varor och tjänster i Sverige |
| Buyer, subcontractor **with** VAT charged | **4610** | Inköp av tjänster och underentreprenader |
| Buyer, material bought normally | **4310** | Inköp av råvaror och material i Sverige |

Two BAS 2026 notes that break naive name matching:

- The official BAS 2026 spreadsheet spells 2614 **"Utgående moms omvänd betalskyldighet, 25 %"** (no "nings"), while 2624 and 2634 are spelled in full. Match on number, not name.
- Class 4 was restructured in BAS 2026. **4000–4099** is now *handelsvaror* (goods for resale), **4300/4310** is the new *Inköp av råvaror och material i Sverige*, and 4415/4425 were renamed. A byggföretag buying timber and plasterboard for a job posts **4310**, not 4010. Legacy charts mapping material to 4010 should be remapped.

### Worked entries

Subcontractor invoices 100 000 SEK for VVS work to a byggföretag, reverse charge.

**Seller (VVS-företaget):**

| Account | Debit | Credit |
|---|---|---|
| **1511** Kundfordringar | 100 000 | |
| **3231** Försäljning inom byggsektorn, omvänd betalningsskyldighet moms | | 100 000 |

Ruta 41: 100 000.

**Buyer (byggföretaget):**

| Account | Debit | Credit |
|---|---|---|
| **4425** Inköp av tjänster i Sverige, omvänd betalningsskyldighet, 25 % moms | 100 000 | |
| **2647** Ingående moms omvänd betalningsskyldighet | 25 000 | |
| **2440** Leverantörsskulder | | 100 000 |
| **2614** Utgående moms omvänd betalskyldighet, 25 % | | 25 000 |

Ruta 24: 100 000. Ruta 30: 25 000. Ruta 48: 25 000. Cash effect zero, but both lines must be filed.

If the buyer has partially deductible VAT (mixed verksamhet), the 2647 side is reduced and the non-deductible part is charged to 4425 — see `swedish-vat` for the proportional rules.

---

## 6. Material versus service, mixed invoices, goods with installation

The rules apply to **services only**. Pure sales of goods never trigger reverse charge.

| Case | Treatment |
|------|------|
| Byggtjänst where the entreprenör also supplies the material | Everything is one byggtjänst — reverse charge on the whole invoice |
| Assignment that is "uteslutande, eller så gott som uteslutande" a delivery of goods | Varuleverans — charge VAT |
| Goods sold with installation where the labour is *obetydlig* relative to the value of the goods | Varuleverans — charge VAT. Skatteverket's examples: spisar, kylskåp |
| Goods installed so that the item becomes fastighet, labour not insignificant | Byggtjänst — reverse charge |
| Assignment containing several services, or goods and services, with one dominant service | If the dominant service is a byggtjänst, reverse charge covers the **entire** assignment, including elements that on their own would fall outside |

Skatteverket's formulation: an assignment that is a byggentreprenad, or a step in one, is a service unless it exclusively or almost exclusively concerns delivery of goods.

Practical consequence for a mixed invoice: do **not** split a single entreprenad into a VAT-bearing material line and a VAT-free labour line. One assignment, one treatment. Splitting is only correct where there genuinely are two separate supplies — for example a builders' merchant that sells material over the counter on Monday and performs an unrelated installation job on Tuesday.

---

## 7. Machine hire and personaluthyrning

| What is supplied | Reverse charge? | Reason |
|------|------|------|
| Grävmaskin **med förare** | Yes | Explicitly listed in ML 16 kap. 13 § andra stycket 1 |
| Grävmaskin **utan förare** | No — charge 25 % VAT | Explicitly excluded by Skatteverket |
| Lift, byggställning, bodar hired out without personnel | No — charge VAT | Uthyrning of equipment, not a byggtjänst |
| Hire of a snickare to work under the customer's direction on a byggarbetsplats | Yes | Tillhandahållande av personal, ML 16 kap. 13 § andra stycket 3 |

Personaluthyrning is treated as **one single service** that is not split. Skatteverket: if a hired person is expected to perform mainly services covered by the rules, and the customer is a byggföretag, reverse charge applies to the whole hire even if some of the tasks fall outside.

Machine hire with operator is where SME bookkeeping most often goes wrong, because the same supplier alternates between the two forms week by week. Read each invoice; the presence or absence of an operator decides the VAT treatment.

Placering: hire of machines is a cost on **5210** (Hyra av maskiner och andra tekniska anläggningar, ej datorer och fordon) or **5220** (Hyra av inventarier och verktyg) on the hirer's side when VAT is charged; when reverse charge applies the cost belongs on **4425** because the supply is a byggtjänst, not a rental.

---

## 8. Construction-specific VAT timing (fakturadatummetoden)

Construction has its own beskattningsgrundande händelse and its own redovisningstidpunkt. This overrides the general rules for a company on faktureringsmetoden.

- **ML 7 kap. 8 §**: for bygg- och anläggningstjänster and goods delivered in connection with them, the beskattningsgrundande händelse occurs **when the invoice is issued**. If no invoice has been issued when payment is received, or the invoice is not issued within the ML 17 kap. 16 § deadline, the ordinary rules in 7 kap. 4 or 7 § apply instead.
- **ML 7 kap. 24 §**: output VAT is reported for the period **the invoice was issued**; if payment in förskott or a conto is received without an invoice, for the period **payment was received**; and **at the latest** for the period covering the **second calendar month after the month the services were supplied**.
- **ML 17 kap. 16 §**: the invoice must be issued **no later than the end of the second calendar month after the month** in which the services were supplied or the goods delivered. This applies even to private customers.

When is the service "supplied"? Skatteverket: for bygg- och anläggningsentreprenader, when the beställare has approved the entreprenad — normally at godkänd slutbesiktning, or when the building is taken into use or inflyttning occurs. Where the contract provides for etappbesiktning, each etapp is assessed separately.

A company on **bokslutsmetoden** follows the ordinary cash rules: output VAT when paid, with unpaid receivables picked up in the last period of the year.

Consequence for bookkeeping automation: a construction invoice dated 3 March for work finished in January belongs in the March VAT period, not January — but if no invoice had been issued by 31 March, the VAT would have been due for March anyway under the two-month backstop.

---

## 9. ROT: what qualifies and who may claim

ROT is a skattereduktion for the **customer**, administered through the company. Legal base: **IL 67 kap. 11–19 §§** and **lagen (2009:194) om förfarandet vid skattereduktion för hushållsarbete** (HUSFL).

### Qualifying work

**IL 67 kap. 13 a §**: reparation, underhåll samt om- och tillbyggnad of a **småhus or ägarlägenhet owned by the person claiming**.

**IL 67 kap. 13 b §**: the same work in a **bostadsrätt** held by the claimant, provided the work is done **inside the lägenhet** and concerns measures the bostadsrättshavare is responsible for. Also applies to a lägenhet in a bostadsförening or bostadsaktiebolag.

**IL 67 kap. 13 c §** excludes, among others:

- work that only concerns installation or service of maskiner och andra inventarier
- work for which försäkringsersättning has been paid
- work for which bidrag or other economic support from staten, kommun or region has been given
- work for which skattereduktion for installation av grön teknik has been granted
- om- eller tillbyggnad of a småhus for which fastighetsavgift has not been levied for the **five first calendar years after the calculated värdeår** ("femårsregeln")
- restaurang- och cateringtjänster (the cross-reference in 13 c § 6 points to **ML 9 kap. 5 §**, the 12 % rate for restaurang och catering). Current lydelse of 13 c § is Lag (2023:206)

### Who may claim (IL 67 kap. 11, 15, 15 a, 16 §§)

- Turned 18 by the end of the beskattningsår, and obegränsat skattskyldig for some part of the year (or begränsat skattskyldig under 3 kap. 18 § with essentially all earned income in Sweden).
- Must **own** the bostad while the work is performed and use it as permanentbostad, fritidsbostad or similar.
- A dödsbo may claim for work performed before the death.
- The performer may not be **närstående** to the customer (15 § andra stycket); Skatteverket's list of närstående runs from spouse and sambo through parents, grandparents, children, grandchildren and siblings with their spouses and descendants.
- The company must be **godkänd för F-skatt** when the contract is made or when the customer pays (16 § 1). Work abroad: an equivalent intyg under 17 §.
- Payment must be made **electronically** (15 a §): forwarded by a betaltjänstleverantör and containing sender, recipient, amount and time. Cash, cheque and presentkort disqualify. In force since 1 January 2020.

### Not ROT

Nyproduktion and färdigställande never qualify. Rented, let out, arrendated bostäder do not qualify. Gemensamhetsutrymmen in a flerfamiljshus (entré, tvättstuga, förråd) are not "bostad". In a bostadsrätt, work on fasad or balkong does not qualify even for a radhus or parhus.

---

## 10. ROT: rate history, cap and the shared ceiling

The mechanically relevant number for a company is the payout formula in **HUSFL 7 §**, not the percentage as such.

| Period | HUSFL 7 § payout for ROT | Effective rate | SFS |
|------|------|------|------|
| Until 11 May 2025 | tre sjundedelar of what the customer paid | 30 % of arbetskostnad inkl. moms | 2024:419 lydelse |
| **12 May – 31 December 2025** | **samma belopp som köparen har betalat** | **50 %** | SFS 2025:323, in force 12 May 2025 (Prop. 2024/25:156, bet. 2024/25:FiU32) |
| **From 1 January 2026** | **tre sjundedelar** of what the customer paid | **30 %** | SFS 2025:324, in force 1 January 2026 |

The corresponding IL amendments are SFS 2025:321 (temporary) and SFS 2025:322 (restoring the ordinary rule from 1 January 2026, applied first to work paid after 31 December 2025).

*Osäkert:* the statute keys the temporary period to ikraftträdande dates rather than to a stated payment window; Prop. 2024/25:156 describes it as a raise "under perioden 12 maj–31 december 2025". Since the customer's payment date determines the beskattningsår (HUSFL 8 §, 12 §), treat the payment date as the cut-off and verify any borderline job against Skatteverket's decision.

### Ceiling and the shared cap

**Income year 2026 (unchanged from 2025; no later amendment enacted as at 2026-09-17):**

| Parameter | ROT | RUT |
|------|------|------|
| Rate on arbetskostnad inkl. moms | 30 % | 50 % |
| Combined ROT+RUT ceiling per person per year | **75 000 SEK** | |
| Of which ROT may be at most | **50 000 SEK** | |

The ceilings are in **IL 67 kap. 19 § andra stycket** (final reduction) and mirrored in **HUSFL 7 § tredje stycket** and **17 § tredje stycket** (preliminary reduction). The ROT cap of 50 000 sits *inside* the 75 000 total: a customer who has used 75 000 of RUT has no ROT left, and a customer who has used 50 000 of ROT can still use 25 000 of RUT.

Historic anomaly worth knowing when reconciling old jobs: for work paid between 1 July 2024 and 31 December 2024 the ceilings were temporarily separated (SFS 2024:416), so a household could reach 75 000 ROT plus 75 000 RUT. SFS 2024:419 restored the shared ceiling from 1 January 2025.

---

## 11. ROT: fakturamodellen step by step

1. **Agree with the customer.** Skatteverket recommends agreeing the terms of the work and the ROT treatment; the avtal may be written or oral. Establish who owns the bostad and who will claim.
2. **Collect the customer's data before starting**: personnummer, and either the **fastighetsbeteckning** (småhus/ägarlägenhet) or the **bostadsrättsföreningens organisationsnummer plus lägenhetsnummer** (four digits). Personnummer is required by HUSFL 9 § p. 2; the fastighetsbeteckning, or the BRF's organisationsnummer plus lägenhetsbeteckning, by 9 a §.
3. **Record hours as you go.** Actual hours per work type must be reported, **also on fixed-price jobs**, and subcontractors' hours too. Only time worked on site at the customer qualifies.
4. **Invoice with the deduction shown.** Deduct up to 30 % of arbetskostnad inkl. moms and reduce "att betala". Separate arbetskostnad, materialkostnad and övriga kostnader as separate lines.
5. **Customer pays electronically**, the reduced amount.
6. **Apply for utbetalning** in the e-tjänst *Rot och rut – företag* (or by XML import from the accounting system) once the work has been **both performed and paid**. Deadline: **31 January of the year after the customer paid** (HUSFL 8 § andra stycket). The company must have registered a bank account with Skatteverket.
7. **Skatteverket decides and pays** (HUSFL 11–12 §§). Decisions can be downloaded as a file for matching against invoices.

### Delfakturering, a conto and förskott

Deduct ROT on **each** invoice — the whole deduction may not be loaded onto the final invoice when arbetskostnad appears on several invoices. If the customer has been invoiced in full but paid only part, apply for the corresponding share: if 40 % of the post-ROT amount has been paid, apply for 40 % of the deducted ROT.

The work must be **performed** before applying; payment alone is not enough. A förskott paid in December of year 1 requires the work to be completed and the application filed by 31 January of year 2.

### Factoring and kreditbolag

If a factoringbolag buys the invoice, wait until the **customer** has paid the factoring company in full before applying. If the customer finances through a kreditbolag, Skatteverket treats the kreditbolag as paying on the customer's behalf, so ROT can be granted when the company has been paid.

### VAT interaction

- **Faktureringsmetoden:** report the full VAT when the invoice is issued and booked.
- **Bokslutsmetoden:** report in two steps. VAT on what the customer pays when the customer pays; VAT on the ROT portion when Skatteverket pays. Skatteverket's own example: on a 19 250 SEK customer payment the VAT is 19 250 × 0,20 = 3 850, and on a 3 750 SEK ROT payout a further 3 750 × 0,20 = 750.

---

## 12. ROT: BAS entries, including a short payment from Skatteverket

Skatteverket's worked figures: arbetskostnad 10 000, material 8 000, resa 400, moms 25 % = 4 600, total 23 000. ROT = 30 % of 10 000 × 1,25 = **3 750**. Customer pays **19 250**.

**Invoice issued:**

| Account | Debit | Credit |
|---|---|---|
| **1511** Kundfordringar | 19 250 | |
| **1513** Kundfordringar – delad faktura | 3 750 | |
| **3001** Försäljning inom Sverige, 25 % moms | | 18 400 |
| **2611** Utgående moms på försäljning inom Sverige, 25 % | | 4 600 |

**1513** is in BAS 2026 under the name *Kundfordringar – delad faktura*; it carries no "#" marker, so it is available under K2. Where a chart omits it, **1519** is not the substitute — use a dedicated fordran account such as **1680** Andra kortfristiga fordringar.

**Customer pays:** Debit **1930**, Credit **1511** 19 250.

**Skatteverket pays in full:** Debit **1930**, Credit **1513** 3 750.

**Skatteverket pays less than applied for.** This is the case worth automating. Say the decision grants 2 250 instead of 3 750, because 1 500 of the claimed arbetskostnad was re-classified as material.

| Account | Debit | Credit |
|---|---|---|
| **1930** Företagskonto | 2 250 | |
| **1511** Kundfordringar (re-invoice the customer) | 1 500 | |
| **1513** Kundfordringar – delad faktura | | 3 750 |

The shortfall is **not** a cost and **not** a VAT adjustment: the customer owes the full contract price, and the ROT reduction was only a deferred means of payment. Issue a supplementary invoice to the customer for 1 500 and chase it as an ordinary receivable. Only if the company chooses not to bill the customer does the amount become a kundförlust (**6350/6351**) — and then a nedsättning of the beskattningsunderlag under ML must be considered separately, because the underlying supply was never reduced.

Two traps:

- Do **not** post the shortfall against revenue or against **2611**. The moms is unchanged; only who pays changed.
- Do **not** book the SKV payout as an intäkt. It is settlement of a receivable. Skatteverket may also **kvitta** the payout against the company's tax debts — in that case Debit **1630** Avräkning för skatter och avgifter (skattekonto), Credit **1513**.

If a ROT amount must be repaid in the same year the customer paid, the **utföraren** makes the repayment (blankett SKV 4533) and the entry reverses: Debit **1511** (re-invoice) / Credit **1930**.

---

## 13. ROT documentation and an exhausted utrymme

### On the invoice

Skatteverket's list of what a ROT invoice should carry:

1. Total invoice amount and the size of the ROT deduction, **calculated inkl. moms**.
2. Cost of worked time, material costs, and övriga kostnader (resor, maskiner, administration) kept apart.
3. What type of work the company performed.
4. Statement that the company has **F-skatt**.
5. Customer's **name and personnummer**.
6. **Fastighetsbeteckning**, or the BRF's **organisationsnummer plus lägenhetsnummer** (four digits).
7. If several people share the deduction, how much each is to receive.

On top of that, all mandatory fields in ML 17 kap. 24 § still apply — see `swedish-invoice-compliance`.

### Documentation the company must be able to produce

- Actual hours worked per work type, including subcontractors' hours, even on fixed-price jobs.
- Evidence that material costs are not embedded in arbetskostnad. The company may not charge the customer **less** than its own purchase price for material.
- Evidence of the electronic payment: sender, recipient, amount, time.
- Travel must be **charged for**. If the company does not bill travel, Skatteverket treats it as included in arbetskostnad and pays out less than applied for.

### When the customer's utrymme is used up

The company cannot see the customer's remaining ROT — **the customer must check it**, via the e-tjänst *Mina skattereduktioner för rot, rut och grön teknik* or a paper intyg. Only decided amounts are visible.

Handling rules:

| Situation | Action |
|------|------|
| Customer's ROT room is fully used | Apply for **another person in the household who also owns the bostad**. Invoice that person, or show the split on the invoice |
| Room partly used | Apply only for what fits; invoice the remainder to the customer as ordinary receivable |
| Several owners | Show on the invoice how much ROT each person is to receive |
| Not known before invoicing | Invoice with the deduction, but make the avtal state that the customer pays the difference if Skatteverket reduces or refuses the payout |

Skatteverket rejects **efterhandskonstruktioner** — corrections made after Skatteverket has started reviewing the case. In particular, a company may not credit an invoice and ask for a new payment where it lacked F-skatt at the payment date, where the invoice was fully paid, where payment was in cash, or where the begäran om utbetalning arrived after the deadline. Genuine corrections should be made in the same year the customer paid, before applying.

---

## 14. Ask the user

Ask before booking, rather than guessing:

1. **"Does this buyer sell byggtjänster more than occasionally?"** — the single question that decides reverse charge. If the user does not know, instruct them to ask the buyer and record the answer.
2. **"Was there an operator with the machine?"** — whenever an invoice mentions maskinhyra, grävmaskin, kranbil, lift.
3. **"Is this one assignment or two separate supplies?"** — whenever an invoice mixes material and labour with different treatments.
4. **"Who owns the bostad, and is it a småhus, ägarlägenhet or bostadsrätt?"** — before any ROT booking.
5. **"What is the värdeår of the småhus?"** — before treating om-/tillbyggnad as ROT; the five-year rule bars it.
6. **"Has the customer checked how much ROT room is left?"** — before invoicing with the deduction.
7. **"Was the invoice paid electronically, in full, by the customer?"** — before applying for utbetalning.
8. **"Is there försäkringsersättning, bidrag or grön teknik on this job?"** — any of these bars ROT.
9. **"Which VAT method does the company use?"** — faktureringsmetoden or bokslutsmetoden changes when the ROT VAT is reported.
10. **"When was the entreprenad approved / slutbesiktigad?"** — needed for the two-month invoicing and VAT backstop.

Never infer a buyer's status from its SNI-kod, and never infer ROT eligibility from the type of work alone.

---

## 15. Error patterns

| Error | Consequence |
|------|------|
| Charging VAT to a byggföretag when reverse charge applies | Felaktigt debiterad moms payable to the state; buyer's deduction denied; ändringsfaktura required |
| Applying reverse charge to a private person or a BRF | Output VAT never reported; skattetillägg 20 % of the underreported amount |
| Booking the buyer's output VAT on **2611** instead of **2614** | Inflates ruta 10 instead of ruta 30; reconciliation fails |
| Reporting only ruta 48 and not ruta 30 | One-sided reverse charge; the declaration is wrong even though cash effect is nil |
| Posting reverse-charge subcontractor cost on **4610** instead of **4425** | Ruta 24 under-reported; VAT-code mapping breaks |
| Posting construction material to **4010** after the BAS 2026 class 4 restructure | 4010 is now *handelsvaror*; use **4310** |
| Splitting one entreprenad into a VAT-bearing material line and a VAT-free labour line | Both treatments wrong on the same invoice |
| Treating machine hire with operator as ordinary rental | VAT charged where reverse charge was mandatory |
| Loading the whole ROT deduction onto the final invoice of a delfakturerad job | Skatteverket reduces or refuses the payout |
| Not charging the customer for travel on a ROT job | Skatteverket re-classifies travel into arbetskostnad and pays out less |
| Booking a short SKV payout as a cost or against 2611 | Understates receivables and misstates VAT; re-invoice the customer instead |
| Accepting cash or Swish-less payment on a ROT job | Disqualifies the reduction entirely (IL 67 kap. 15 a §) |
| Missing the 31 January deadline for begäran om utbetalning | Payout lost; cannot be repaired by crediting and re-invoicing |
| Invoicing a construction job later than the second calendar month after completion | Breach of ML 17 kap. 16 §; VAT falls due anyway under ML 7 kap. 24 § |

---

## 16. Sources

All sources checked **2026-09-17**.

### Statutes (consolidated text)

| Statute | Provisions used | Lydelse relied on |
|------|------|------|
| Mervärdesskattelag (2023:200) | 5 kap. 32–35 §§; 7 kap. 8 §, 23 §, 24 §; 8 kap. 6, 8, 9 §§; 9 kap. 5 §; 16 kap. 13 §; 17 kap. 16 §, 24 §, 25 § | Consolidated to SFS 2026:1025. **16 kap. 13 § carries no later Lag()-marker — original 2023:200 wording, in force since 2023-07-01 and unchanged for 2026** |
| Inkomstskattelag (1999:1229) | 67 kap. 11, 11 a, 12, 13, 13 a, 13 b, 13 c, 14, 15, 15 a, 16, 17, 18, 19 §§ | Consolidated to SFS 2026:1393. 19 § current lydelse **Lag (2025:322)**; 13 c § **Lag (2023:206)** |
| Lag (2009:194) om förfarandet vid skattereduktion för hushållsarbete (HUSFL) | 6–9 a, 11–17, 20–24 §§ | Consolidated to **SFS 2025:324**; no later amendment listed as at 2026-09-17. 17 § current lydelse **Lag (2024:419)** |

### SFS amendments relied on for the rate history

| SFS | Effect | In force |
|------|------|------|
| 2024:416 | Temporarily separated the ROT/RUT ceilings | 2024-07-01 |
| 2024:419 | Restored the shared 75 000 / 50 000 ceiling | 2025-01-01 |
| **2025:321** (IL) / **2025:323** (HUSFL) | ROT payout raised to "samma belopp som köparen har betalat" (50 %) | **2025-05-12** |
| **2025:322** (IL) / **2025:324** (HUSFL) | ROT payout back to "tre sjundedelar" (30 %) | **2026-01-01** |

SFS 2025:323 and 2025:324 were read as the official PDFs on svenskforfattningssamling.se (Regeringskansliet), verbatim. Förarbeten: Prop. 2024/25:156, bet. 2024/25:FiU32, rskr. 2024/25:187.

### Skatteverket (skatteverket.se, read 2026-09-17)

- *Byggverksamhet* — `/foretag/moms/sarskildamomsregler/byggverksamhet.4.dfe345a107ebcc9baf80001255.html` (fastighetsbegrepp, entreprenadverksamhet, utlägg, fakturadatummetoden, when a byggtjänst is regarded as supplied, etapper, egen regi)
- *Omvänd betalningsskyldighet inom byggsektorn* — `.../byggverksamhet/omvandbetalningsskyldighetinombyggsektorn.4.47eb30f51122b1aaad28000545.html` (the buyer test, mellanman, staten, kommuner, utländska företagare, invoice notation, ändringsfaktura)
- *Tjänster där du ska använda omvänd betalningsskyldighet* — `.../tjansterdarduskaanvandaomvandbetalningsskyldighet.4.19b9f599116a9e8ef36800022231.html` (service list, exclusions, SNI as guidance only, vara/tjänst, byggstädning, personaluthyrning)
- *Rot och rut – företag* — `/foretag/skatterochavdrag/rotochrut.4.2ef18e6a125660db8b080002674.html` (30 % / 50 000 / 75 000 for the current year)
- *Så fungerar rotavdraget för företag* — `/foretag/skatterochavdrag/rotochrut/safungerarrotavdraget.4.2ef18e6a125660db8b080002709.html` (qualifying bostad, femårsregeln, närstående, hours, material, travel, electronic payment, delfakturering, factoring, application, worked VAT example)

### BAS

- Official **BAS 2026 kontoplan, v 1.1** (bas.se) plus the official 2026-vs-2025 change file. Every account number **and** name in this file was matched against those two files. New in BAS 2026 and used here: **4300/4310** (Inköp av råvaror och material i Sverige), **4010** redefined to *handelsvaror*. Renamed in BAS 2026: **4415–4417**, **4425–4427**. The spelling of **2614** in the official file is *"Utgående moms omvänd betalskyldighet, 25 %"*.

### Osäkert

- **Skatteverkets rättsliga vägledning (www4.skatteverket.se) blocks automated fetches** ("Request Rejected"). The detailed ställningstaganden behind the SNI-2002 guidance, the fastighetsbegrepp and *"Vilka tjänster omfattas?"* could not be read directly. Everything above on those points comes from skatteverket.se's own guidance pages, which link to the vägledning; a human should open the vägledning before relying on a borderline classification.
- The temporary 50 % ROT period is defined in the statutes by **ikraftträdande dates** (2025-05-12 and 2026-01-01), not by an explicit payment window. Prop. 2024/25:156 describes it as "perioden 12 maj–31 december 2025". The customer's payment date governs the beskattningsår (HUSFL 8 §, IL 67 kap. 12 §); treat it as governing the rate window too, and verify any job straddling those dates against Skatteverket's decision.
- **No change to ROT, RUT or omvänd byggmoms for 2027 could be confirmed from a primary source on 2026-09-17.** regeringen.se's proposition list renders through JavaScript and returned no content to an automated fetch, so a 2027 budget proposal, if one exists, was not read. Do not assume the 2026 figures continue into 2027 without re-checking.
