# E-handel: Cross-Border Sales, OSS and IOSS

Where VAT is due on a webshop sale, which special scheme carries it, and how each case is booked
in BAS 2026.

General VAT mechanics (rutor, reverse charge, import VAT, deduction) live in `swedish-vat`;
invoice content and kreditfaktura in `swedish-invoice-compliance`; stock valuation in
`swedish-inventory`; bank and provider reconciliation in `swedish-daily-bookkeeping`. This file
carries only what is specific to selling online across borders.

All account numbers and names verified against BAS 2026 (bas.se, `BAS_kontoplan_2026_v2`,
downloaded 2026-09-17). None of the accounts below carry the `#` marker, so all are usable
under K2. Every threshold and amount below is the figure in force on **2026-09-17**; the Sources
section records where each was checked.

### What changed for a Swedish webshop during 2026

| Change | In force | Status | Source |
|---|---|---|---|
| Swedish VAT on livsmedel cut from 12 % to 6 % — groceries, takeaway, non-alcoholic drinks and bottled water; restaurant service stays at 12 % | **1 April 2026** | Law, in force | Skatteverket, *Momssatser och undantag från moms*, checked 2026-09-17 |
| Customs duty relief for consignments ≤ 150 EUR abolished; flat **EUR 3 per item** transitional duty | **1 July 2026** to 1 July 2028 | Law, in force | Council Reg. (EU) 2026/382; Comm. Del. Reg. (EU) 2026/1022 |
| Wider EU customs reform (Data Hub, four duty categories, platform as deemed importer) | from 2028 | Political agreement 26 March 2026, **not yet in force** | European Commission, *EU customs reform*, checked 2026-09-17 |
| EU-wide handling fee on directly delivered imported goods | announced for ~1 Nov 2026 | **Osäkert** — see section 4 | Tullverket, *Handla på nätet*, checked 2026-09-17 |

**Osäkert:** Skatteverket's page states the 6 % food rate without an end date. The repo's
`swedish-vat` skill records it as temporary to 2027-12-31 (SFS 2026:118) with a reversion to
12 % on 2028-01-01 (SFS 2026:119). Both SFS numbers are verified: the 6 % rate runs
2026-04-01 to 2027-12-31 (prop. 2025/26:55).

**Announced for 2027 and later.** Skatteverket's ViDA page states that smaller OSS rule changes
apply from **2027-01-01**, and that the platform and single-VAT-registration rules follow on
**2028-07-01**, including a transfer-of-own-goods scheme that replaces the call-off-stock
simplification described below.

---

<!-- toc -->
**Contents**

- [1. Master decision table](#1-master-decision-table)
- [2. Distansförsäljning to consumers in other EU countries](#2-distansförsäljning-to-consumers-in-other-eu-countries)
- [3. OSS — the union scheme](#3-oss--the-union-scheme)
- [4. Goods imported from outside the EU and sold to consumers](#4-goods-imported-from-outside-the-eu-and-sold-to-consumers)
- [5. Marketplaces as deemed supplier](#5-marketplaces-as-deemed-supplier)
- [6. Sales to consumers outside the EU (export)](#6-sales-to-consumers-outside-the-eu-export)
- [7. B2B sales within the EU](#7-b2b-sales-within-the-eu)
- [8. Digital products and services to consumers](#8-digital-products-and-services-to-consumers)
- [9. Ask the user — always, before booking](#9-ask-the-user--always-before-booking)
- [Sources](#sources)

<!-- /toc -->

## 1. Master decision table

Read the row that matches the order. `Ship from` means where the goods physically start.

| Buyer | Buyer country | Goods / digital | Channel | Ship from | VAT due where | Scheme | Revenue account |
|---|---|---|---|---|---|---|---|
| Consumer | Sweden | Goods | Own shop | SE | Sweden | Ordinary momsdeklaration | **3001 / 3002 / 3003** |
| Consumer | Other EU | Goods | Own shop | SE | Sweden **while under the threshold** | Ordinary momsdeklaration, ruta 05 | **3001 / 3002 / 3003** |
| Consumer | Other EU | Goods | Own shop | SE | Buyer's country once the threshold is passed or the option is taken | OSS union scheme (or local registration) | **3106** |
| Consumer | Other EU | Goods | Own shop | Stock in that same EU country | That country | Local registration, **not** OSS | Sub-account of **3106** per country |
| Consumer | Other EU | Goods | Own shop | Stock in a third EU country | Buyer's country | OSS union scheme | **3106** |
| Consumer | Other EU | Digital service | Own shop | n/a | Same threshold logic as goods | Ordinary, then OSS | **3001/3002/3003** by rate below threshold (Swedish VAT, ruta 05), **3308** or a company sub-account above |
| Consumer | Other EU | Goods or digital | Marketplace that is deemed supplier | Any EU | The marketplace owes it, not you | You make a zero-rated supply to the marketplace | **3108** (goods to the marketplace, ML 5 kap. 6 §) |
| Consumer | Sweden or EU | Goods ≤ 150 EUR | Own shop | Outside EU, direct to buyer | Buyer's country | IOSS import scheme, or import VAT at the border | **3106** (IOSS) |
| Consumer | Sweden or EU | Goods > 150 EUR | Own shop | Outside EU, direct to buyer | Buyer's country at import | Ordinary import, no IOSS | Depends on Incoterms — ask the user |
| Consumer | Outside EU | Goods | Any | SE | No Swedish VAT (export) | Ruta 36 | **3105** |
| Business with valid VAT no. | Other EU | Goods | Any | SE | Buyer self-assesses | Ruta 35 + periodisk sammanställning | **3108** |
| Business with valid VAT no. | Other EU | Digital service | Any | n/a | Buyer self-assesses (huvudregeln) | Ruta 39 + periodisk sammanställning | **3308** |
| Business without valid VAT no. | Other EU | Goods | Any | SE | Treat as a consumer | See consumer rows | As consumer rows |
| Business | Outside EU | Goods | Any | SE | Export | Ruta 36 | **3105** |
| Business or consumer | Outside EU | Service | Any | n/a | Outside Sweden | Ruta 40 | **3305** |

**Ask the user** before applying a row when any of these is unknown: where the goods physically
ship from, whether the marketplace collected VAT on the order, whether the buyer gave a VAT
number that was validated, and whether the company already holds a foreign VAT registration.

---

## 2. Distansförsäljning to consumers in other EU countries

**Definition.** ML 2 kap. 7 §: *"Med unionsintern distansförsäljning av varor avses leverans av
varor som sänds eller transporteras av leverantören eller för dennes räkning från ett annat
EU-land än det där försändningen eller transporten till förvärvaren avslutas…"* The seller (or
someone acting for the seller) arranges the transport, and the buyer is a non-taxable person.
A customer who collects the goods in Sweden themselves is not distance selling.

### The threshold

One EU-wide threshold, not one per country: **10 000 EUR, expressed in Sweden as 99 680 kr**
(Skatteverket, *Tröskelvärde vid försäljning till icke beskattningsbara personer i andra
EU-länder*; ML 6 kap. 62–65 §§).

**Counts towards it:** unionsintern distansförsäljning of goods to consumers in all other EU
countries added together, plus telekommunikationstjänster, radio- och tv-sändningstjänster and
elektroniska tjänster to EU consumers. **Does not count:** sales to Swedish customers, sales to
VAT-registered EU businesses, exports outside the EU, and goods shipped from stock already
located in the buyer's own country.

Goods and digital services share one bucket. A shop with 70 000 kr of parcels to Denmark and
40 000 kr of downloads to Germany has passed it.

### Crossing it mid-year

There is no grace period and no pro-rating. The sale that takes the running total past
99 680 kr is itself taxed in the buyer's country, and **every subsequent sale** that year and the
following calendar year is too. Track the running total per calendar year in one report covering
all destination countries and both goods and digital services; apply for OSS *before* the quarter
you expect to cross in, because OSS reporting starts on the first day of the calendar quarter
after approval and a late application leaves a gap that must be settled by registering locally
in each country. From the crossing sale onwards, charge the destination rate, book to **3106**
and the VAT to **2670**.

**Osäkert:** whether an order placed before and delivered after the crossing point follows the
delivery date is not settled on Skatteverket's public pages; use the date of leverans
(beskattningsgrundande händelse) and flag it if the amounts are material.

### Choosing destination VAT voluntarily

A seller under the threshold may apply to Skatteverket to be taxed in the destination country
anyway; the decision runs until revoked. Worth doing when destination rates are below 25 %
(books, food, children's clothing in several countries) or when crossing mid-year is certain and
a clean break beats switching rates in October. It is a judgment call — present both options to
the user rather than choosing silently.

### Alternative: the SME cross-border exemption (EX-number)

A separate route for small sellers. A business established in Sweden with EU-wide annual turnover
of at most **100 000 EUR** in both the current and the previous calendar year, and below the
national small-business threshold of each country it sells to, can apply to Skatteverket for an
identification decision and an **EX-number** and sell VAT-free in those countries (Skatteverket,
*Momsundantag när du säljer till andra EU-länder*). Reporting is a quarterly statement per
country in euro at the ECB rate of 1 January. Mutually exclusive with charging destination VAT
on the same supplies — ask the user which route the company is on before booking anything.

---

## 3. OSS — the union scheme

### What it does

One registration with Skatteverket, one quarterly return, one payment, covering VAT owed to every
other EU country on unionsintern distansförsäljning of goods to consumers; on services to
consumers in other EU countries (all services, not only digital); and, **only for an electronic
interface that is a deemed supplier under ML 5 kap. 6 §**, domestic supplies inside another EU
country (ML 22 kap. 4 § 2 p. and 13 § 2 p.). An ordinary Swedish seller shipping from its own FBA
stock in Poland to a Polish consumer makes a **domestic Polish sale that belongs on a Polish VAT
return**, not in OSS.

### What it does not cover

| Not in OSS | Handle instead by |
|---|---|
| Sales to Swedish consumers | Ordinary momsdeklaration |
| B2B sales in any country | Ruta 35 / 39 + periodisk sammanställning |
| Input VAT incurred abroad | Local VAT registration, or the 8th/13th Directive refund procedure (`swedish-vat`) |
| Imported goods ≤ 150 EUR sold direct to consumers | IOSS import scheme (section 5) |
| Any supply in a country where the seller **is** VAT-registered for other reasons and the goods start and end there | That country's local return |

The last row is the one that bites FBA sellers. Holding stock in a country usually forces a
local registration there, and the domestic supplies out of that stock then belong on the local
return, not in OSS. See `ehandel-operations.md` section 2.

### Filing, payment and corrections

| Item | Rule |
|---|---|
| Period | Calendar quarter |
| Deadline | Last day of the month after the quarter — Q1 by 30 April, Q2 by 31 July, Q3 by 31 October, Q4 by 31 January |
| Nil return | Still required for every quarter the registration is live |
| Currency | Euro, two decimals |
| Payment | Separate account, **not** the skattekonto: IBAN SE0512000000012810112134, BIC DABASESX, Skatteverket, SE-831 87 Östersund. Paying into the skattekonto is treated as non-payment |
| Reminder | Skatteverket sends an electronic reminder 10 days after a missed deadline |
| Corrections | In a later OSS return, within **three years** of the original deadline. Do not refile the old quarter |
| Registration changes | Report by the 10th of the month after the change |
| Deregistration | Notify at least 15 days before the end of the quarter |

Check every quarter: the euro conversion (the e-service does it, but the ledger is in SEK, so a
difference to **3960 Valutakursvinster** or **7960 Valutakursförluster** is normal, since it is a
currency difference on a rörelseskuld rather than öresavrundning) and the separate payment,
which is missed often enough to deserve its own line on the month-end checklist.

### OSS and the Swedish momsdeklaration

Sales reported in OSS are **not** reported in the ordinary momsdeklaration — not in ruta 05, not
in ruta 35, not in ruta 41 or 42, not anywhere. Skatteverket states this explicitly on *Fylla i
momsdeklarationen*: *"Försäljning av tjänster som du redovisar i den särskilda momsdeklarationen
i e-tjänsten OSS … ska du inte redovisa i den vanliga momsdeklarationen."*

Consequences: turnover in the income statement will exceed the sum of the momsdeklaration rutor,
which is correct and belongs in the month-end note rather than being "fixed"; input VAT on
Swedish costs relating to OSS sales is still fully deductible in ruta 48; and the revenue still
flows into INK2 / NE as ordinary net sales.

### BAS treatment of output VAT owed to another country

| Account | Name (BAS 2026) | Use |
|---|---|---|
| **3106** | Försäljning varor till annat EU-land, momspliktig | Distance sales of goods taxed in the buyer's country |
| **2670** | Utgående moms på försäljning inom EU, OSS | Output VAT owed to other EU countries under OSS |
| **3960** / **7960** | Valutakursvinster respektive -förluster på rörelsefordringar och -skulder | The EUR/SEK difference on the OSS payment |
| **6998** | Utländsk moms | Foreign VAT that is a cost, e.g. non-recoverable input VAT abroad |

BAS 2026 gives **2670** as a single huvudkonto with no sub-accounts. Open one company sub-account
per destination country (2671 Denmark, 2672 Germany, …) — the quarterly return is per country and
reconciling a single aggregated balance to it is painful. BAS 2026 also has **no** dedicated
revenue account for OSS *services*; use **3308** with a per-country sub-account, or open
sub-accounts under **3300**, and document the choice in the kontoplan.

### Worked entry — distance sale above the threshold

Order to a German consumer, 1 000 kr net, German rate 19 %:

| Account | Debit | Credit |
|---|---|---|
| **1686** Fordringar för kontokort och kuponger | 1 190 | |
| **3106** Försäljning varor till annat EU-land, momspliktig | | 1 000 |
| **2670** Utgående moms på försäljning inom EU, OSS (sub-account DE) | | 190 |

At the quarterly OSS payment of EUR 1 850,00 from the euro account: debit **2670** (all country
sub-accounts) 21 004, credit **1980 Valutakonton** 21 000, credit **3960 Valutakursvinster på
fordringar och skulder av rörelsekaraktär** 4.

Nothing touches **2650 Redovisningskonto för moms**. Keeping OSS VAT out of 2650 is what stops it
leaking into the ordinary momsdeklaration.

---

## 4. Goods imported from outside the EU and sold to consumers

### IOSS, the import scheme

For **distansförsäljning of goods imported from a place outside the EU in consignments of an
intrinsic value of at most 150 EUR** (defined in ML 2 kap. 8 §; the scheme itself in ML 22 kap.,
and the marketplace deemed-supplier rule in ML 5 kap. 5 §). The seller charges the
destination country's VAT at checkout, quotes the IOSS identification number in the customs
declaration, and the consignment is released without import VAT. The buyer sees no surprise
charge on delivery — which is the commercial reason to use it.

Value limit 150 EUR intrinsic value per consignment, excluding transport and insurance shown
separately; excise goods (alcohol, tobacco) are excluded. The period is the calendar **month**,
due the last day of the following month. Reporting starts when the identification number is
assigned; deregistration needs 15 days' notice before month end; corrections use the same
three-year window as the union scheme.

A consignment deliberately split to stay under 150 EUR is still one consignment. Above 150 EUR,
IOSS cannot be used for that order at all — it goes through ordinary import and who pays the
import VAT follows the Incoterms. **Ask the user** which Incoterm the shop sells on: DDP means
the shop imports and deducts the import VAT, DAP means the customer is the importer and the
shop's sale falls outside Swedish VAT entirely.

### The customs change from 1 July 2026 — enacted

Until 30 June 2026, consignments of 150 EUR or less were relieved of **customs duty** (VAT was
always due; only duty was relieved). That relief has been removed.

- **In force since 1 July 2026:** duty is charged on consignments regardless of value. Tullverket:
  *"Från den 1 juli 2026 gäller nya regler när du handlar varor för 150 euro eller mindre från ett
  land utanför EU."* The transitional measure is a flat **EUR 3 per item**, agreed by the Council
  in November 2025 and running until **1 July 2028**. Legal instruments: **Council Regulation (EU)
  2026/382** and **Commission Delegated Regulation (EU) 2026/1022**.
- **Agreed but not in force:** the broader reform — EU Customs Data Hub, duty categories reduced
  to four, deemed-importer role for platforms — reached political agreement on **26 March 2026**
  and phases in from 2028.
- **Osäkert:** Tullverket flags an EU-wide **handling fee** on directly delivered imported goods
  from around **1 November 2026**, but states neither the amount nor the legal instrument; confirm
  before quoting a figure.

Nothing about VAT changed — the 150 EUR IOSS ceiling is a **VAT** rule and is untouched. What
changed is landed cost: duty now applies to every consignment, so cost of goods sold on imported
inventory rises. Book duty to **5721 Tullkostnader** (or into inventory cost per
`swedish-inventory` if the company capitalises freight and duty) and broker fees to **5722
Speditionskostnader**.

Keep IOSS and union-scheme VAT in separate sub-accounts of **2670**: different returns,
different periods, different deadlines.

---

## 5. Marketplaces as deemed supplier

### When the marketplace, not the seller, owes the VAT

Two cases, both in ML 5 kap. (implementing Articles 14a of the VAT Directive):

| Rule | Text | Situation |
|---|---|---|
| **ML 5 kap. 5 §** | *"Om en beskattningsbar person genom användning av ett elektroniskt gränssnitt möjliggör distansförsäljning av varor importerade från en plats utanför EU i försändelser med ett verkligt värde på högst 150 euro, ska den beskattningsbara personen anses själv ha förvärvat och levererat dessa varor."* | Any seller, goods imported from outside the EU, consignment ≤ 150 EUR |
| **ML 5 kap. 6 §** | *"Om en beskattningsbar person genom användning av ett elektroniskt gränssnitt möjliggör leverans av varor inom EU från en beskattningsbar person som inte är etablerad i EU till någon som inte är en beskattningsbar person, ska den som möjliggör leveransen anses själv ha förvärvat och levererat dessa varor."* | Goods already in the EU, but the underlying seller is **not established in the EU** |

The legal fiction splits one sale into two: seller → marketplace, and marketplace → consumer.

**The case that matters most for a Swedish shop:** neither rule catches an EU-established seller
selling EU-located goods. A Swedish AB selling from Swedish stock through Amazon.de to a German
consumer is **still the taxable person** — Amazon is not the deemed supplier, the Swedish company
owes German VAT and reports it in OSS. Treat "the marketplace handles the VAT" as a claim to
verify against the settlement report, never as an assumption.

### What the seller books when the marketplace is deemed supplier

The seller's supply to the marketplace is a supply of goods, exempt in the seller's country: debit
**1511 Kundfordringar** (or **1686**) and credit **3108 Försäljning varor till annat EU-land,
momsfri** with the gross order value ex VAT. No output VAT.

**Osäkert:** Skatteverket's public pages do not state a single reporting ruta for the
deemed-supplier leg, nor whether it belongs in the periodisk sammanställning; confirm with
Skatteverket or rättslig vägledning before the first filing and document the position.

### The payout is not the sale

The marketplace settlement is always smaller than the sale, and often has a different VAT
character on each line. Never book the payout as revenue.

| Settlement line | Account |
|---|---|
| Gross order value | **3001 / 3106 / 3108** as the decision table requires |
| VAT collected by the marketplace (deemed supplier cases) | Not the seller's VAT — excluded from the seller's revenue entirely |
| Referral / commission fee | **6050** Försäljningsprovisioner |
| Fulfilment and storage fee | **6050** or **5710** Frakter och försäkringar vid varudistribution, consistently |
| Advertising / sponsored products | **5900**-series marketing account per the company's kontoplan |
| Payment processing fee | **6040** Kontokortsavgifter |
| Refunds passed through | Reverse the original revenue and VAT, not a cost |
| Reserved / withheld amount | Stays in **1686**; a receivable, not a fee |
| Net payout | **1930 Företagskonto** |

Marketplace fees from a non-Swedish marketplace entity are usually B2B services under huvudregeln
— the Swedish shop self-assesses: cost to **6050**, purchase to ruta 21/22, output VAT to
**2614**, input VAT to **2645** (`swedish-vat`). Marketplace documentation is reliable on its own
settlement mechanics and is never a source for the tax conclusion.

---

## 6. Sales to consumers outside the EU (export)

No Swedish VAT when the goods are transported out of the EU. Report in **ruta 36**, book to
**3105 Försäljning varor till land utanför EU**.

**The seller carries the burden of proof** that the goods left the EU. Skatteverket: *"Du ska
kunna visa att varan har levererats till en plats utanför EU."* Accepted evidence: tullhandlingar
(export declaration, MRN, customs stamp from the country of exit), frakthandlingar and the
carrier's invoice, a postal receipt showing a destination outside the EU, or the transport
company's confirmation of the delivery address. Explicitly **not** sufficient: payment arriving
from outside the EU.

Two traps. **Åland is outside the EU VAT territory although Finland is in it** — check the
ship-to region, not the country name. And **a consumer who collects in Sweden and carries the
goods out** is not an export at the point of sale: Swedish VAT is charged, and the tax-free
refund route applies only under the traveller rules — departure within three months, minimum
200 kr including VAT, a certificate from an approved intermediary (Global Blue Sverige AB or
Planet Payment Sweden AB), and a passport copy proving residence outside the EU. For residents
of Norway and Åland: minimum 1 000 kr excluding VAT, import within 14 days, evidenced by that
country's customs documentation.

---

## 7. B2B sales within the EU

Zero-rated intra-EU supply (**ML 10 kap. 42 §**, Article 138 of the VAT Directive) requires all
four: a buyer VAT-registered in another EU country who supplies a valid number, physical
transport from Sweden to another EU country, transport evidence held by the seller, and
inclusion in the periodisk sammanställning.

**VAT number validation.** Only the European Commission's **VIES** service counts. Skatteverket:
*"Använd endast Europeiska kommissionens VIES-tjänst för att kontrollera VAT-nummer."* A check
through a third-party service or a shop plugin is not accepted as proof of diligence if the
number turns out to be false. Store the VIES response (date, number, result, consultation ID)
with the order — a boolean flag in the shop database is not evidence. If the buyer cannot produce
a valid number, treat the sale as a sale to a consumer: Swedish VAT below the distance-selling
threshold, destination VAT above it.

**Transport evidence.** The presumtionsregel needs at least two non-contradictory documents from
two parties independent of each other and of buyer and seller: signed CMR, bill of lading,
carrier's invoice, insurance certificate, a bank record of payment for the transport, an official
confirmation from the destination country, or a warehouse receipt there. Not available when the
seller transports the goods in its own vehicle.

**Invoice and reporting.** Invoice by the 15th of the month after delivery, with the buyer's VAT
number and one of "Undantagen från skatteplikt", "10 kap. 42 § ML" or "Article 138 of the VAT
directive" (`swedish-invoice-compliance`). Report in **ruta 35**, book to **3108**.

### Periodisk sammanställning and the quarterly option for goods

| Content | Default period |
|---|---|
| Goods only | Calendar month |
| Services only | Calendar quarter |
| Goods and services | Calendar month |

A seller of **goods only** may apply for quarterly filing if goods supplies do not exceed
**500 000 kr excluding VAT** in the quarter applied for or in any of the four preceding quarters
(SFL 35 kap.). A webshop that adds a single service line — installation, an extended warranty
sold separately — loses the quarterly option and drops to monthly.

Deadline: the 25th of the month after the period through the e-service, the 20th on paper. Late
filing costs 1 250 kr per report and no extension is available. The totals must agree with ruta
35 (goods) and ruta 39 (services).

---

## 8. Digital products and services to consumers

Elektroniska tjänster are, per Skatteverket, services that are mainly automated, need minimal
human involvement and cannot be delivered without IT: downloads, SaaS subscriptions, e-books
sold as files, streaming, online courses without a live teacher, in-app purchases, stock photos.

| | Goods | Digital service to a consumer |
|---|---|---|
| Place of supply | Where the transport to the buyer ends | Where the consumer is located (ML 6 kap. 56–57 §§) |
| Threshold | Shared 99 680 kr bucket | Same shared 99 680 kr bucket |
| Below threshold | Swedish VAT, ruta 05 | Swedish VAT, ruta 05 |
| Above threshold | Destination VAT via OSS | Destination VAT via OSS |
| Evidence of location | Ship-to address | Two non-contradictory pieces: billing address, IP, bank BIN, SIM country code |
| Marketplace deemed supplier | ML 5 kap. 5–6 §§ | App stores and platforms operate their own deemed-supplier regimes — verify per platform |
| Export outside EU | Ruta 36, **3105** | Outside Swedish VAT, ruta 40, **3305** |
| Rate | Often reduced for books and food | Usually the standard rate in each country; e-books are reduced in several |

A digital product does not cross a border physically, so the only evidence of where the customer
is comes from the checkout — the shop must capture and store two pieces of location evidence per
order or it cannot defend its rate. And a service bundled with a physical good (a printed book
plus its audiobook download) may be a single composite supply at one rate or two separate
supplies; **ask the user** how it is priced and marketed before splitting or merging.

---

## 9. Ask the user — always, before booking

1. Where does each order ship from — Sweden, a foreign 3PL, an FBA warehouse, or the supplier?
2. Is the company already VAT-registered in any other country, and for what?
3. Registered for OSS, for IOSS, or for the SME EX-number scheme?
4. For marketplace orders: does the settlement report show VAT collected by the marketplace, and
   on which order lines?
5. Which Incoterm does the shop sell on for imported goods?
6. Any service sold alongside goods (installation, warranty, subscription)? It changes the
   periodisk sammanställning period from quarterly to monthly.
7. Has the 99 680 kr running total been tracked this calendar year, and from which report?

---

## Sources

All web pages checked **2026-09-17**.

**Statutes, current consolidated form**

| Statute | Provisions relied on | Used for |
|---|---|---|
| Mervärdesskattelag (2023:200) | 2 kap. 7 §; 2 kap. 27 §; 5 kap. 5–6 §§; 5 kap. 40–44 §§; 6 kap. 56–57 §§; 6 kap. 62–65 §§; 10 kap. 42 §; 22 kap.; 23 kap. | Distance-selling definition, deemed supplier, vouchers, place of supply, thresholds, OSS/IOSS, import scheme |
| Skatteförfarandelag (2011:1244) | 35 kap. | Periodisk sammanställning, periods, deadlines, penalty |
| Council Regulation (EU) 2026/382 | — | Abolition of the ≤ 150 EUR duty relief |
| Commission Delegated Regulation (EU) 2026/1022 | — | Transitional EUR 3 per-item duty |

Consolidated ML text read via lagen.nu and riksdagen.se. **Osäkert:** Skatteverket's *rättslig
vägledning* (www4.skatteverket.se) blocks automated fetches and could not be consulted; the
paragraph numbers in 5 kap. 15–21 §§ (call-off stock), 6 kap. 62–65 §§ (threshold), 6 kap. 56–57
§§ (electronic services) and 7 kap. 43–47 §§ (change of previously reported output VAT) come
from the consolidated law text only and should be re-checked against rättslig vägledning before
being quoted in advice. No amendment to any of them for financial years beginning in 2026 was
identified, and none is known to be announced for 2027.

**Skatteverket** (skatteverket.se, all checked 2026-09-17)

*Tröskelvärde vid försäljning till icke beskattningsbara personer i andra EU-länder* (10 000 EUR
/ 99 680 kr) · *Momsundantag när du säljer till andra EU-länder* (SME scheme, 100 000 EUR,
EX-number) · *Ansök om att redovisa distansförsäljning i One Stop Shop (OSS)* · *Deklarera och
betala moms i One Stop Shop* (periods, deadlines, IBAN, three-year correction window) · *Fylla i
momsdeklarationen* (rutor; OSS excluded) · *Sälja varor till andra EU-länder* · *Sälja tjänster
till andra EU-länder* · *Sälja varor till länder utanför EU* (export evidence, traveller rules) ·
*Kontrollera momsregistreringsnummer (VAT-nummer)* (VIES) · *Periodisk sammanställning för varor
och tjänster* (500 000 kr quarterly option, 1 250 kr penalty) · *Momssatser och undantag från
moms* (6 % on livsmedel from 1 April 2026) · *Så tar du ut moms* (frakt in the beskattningsunderlag)

**Tullverket** (checked 2026-09-17): *Handla på nätet*; *Ny tullavgift från den 1 juli 2026*.
**Osäkert:** the body text of Tullverket's detailed pages is JavaScript-rendered and could not be
retrieved in full; the EUR 3 amount and the 1 July 2028 end date are taken from the European
Commission page below, not from Tullverket, and the November 2026 handling fee is reported by
Tullverket without an amount or a legal instrument.

**European Commission**, Taxation and Customs Union: *EU customs reform*; *Goods bought online*
(checked 2026-09-17). **Osäkert:** EUR-Lex returned empty documents for CELEX 32026R0382 and
32026R1022, so the two regulations were not read in full text; their numbers and effect are taken
from the Commission page.

**BAS 2026 kontoplan**, bas.se, file `BAS_kontoplan_2026_v2.xlsx`, downloaded 2026-09-17. Every
account number and name in this file was matched against that file directly.
