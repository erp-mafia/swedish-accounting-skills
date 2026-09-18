# E-handel: Operations, Stock, Returns and Reconciliation

The day-to-day accounting of a Swedish webshop: where the stock sits, what happens when goods come
back, how shipping and vouchers are taxed, and what has to tie out at month end.

Cross-border VAT and the OSS/IOSS schemes live in `eu-sales-and-oss.md`; stock valuation, lägsta
värdets princip and inkurans in `swedish-inventory`; generic provider reconciliation in
`swedish-daily-bookkeeping/references/payment-providers.md`; credit-note content in
`swedish-invoice-compliance`; general VAT mechanics in `swedish-vat`.

All account numbers and names verified against BAS 2026 (bas.se, `BAS_kontoplan_2026_v2`,
downloaded 2026-09-17). All amounts are the figures in force on **2026-09-17**; see Sources.

**2026 change that touches almost every line below:** VAT on livsmedel fell from 12 % to 6 % on
**1 April 2026** (Skatteverket, *Momssatser och undantag från moms*, checked 2026-09-17). A
webshop selling groceries, takeaway, non-alcoholic drinks or bottled water has two rates in one
financial year, which affects freight apportionment (section 3), credit notes on pre-April orders
(section 2) and vouchers issued before April (section 4). A credit note carries the rate of the
**original** sale, not the rate on the day of the refund.

---

<!-- toc -->
**Contents**

- [1. Stock held in another country](#1-stock-held-in-another-country)
- [2. Returns, credit notes and refunds](#2-returns-credit-notes-and-refunds)
- [3. Shipping and handling fees](#3-shipping-and-handling-fees)
- [4. Presentkort och rabattkoder](#4-presentkort-och-rabattkoder)
- [5. Dropshipping](#5-dropshipping)
- [6. Payment providers](#6-payment-providers)
- [7. Kundförluster and fraud losses](#7-kundförluster-and-fraud-losses)
- [8. Kassaregister](#8-kassaregister)
- [9. Month-end reconciliation checklist](#9-month-end-reconciliation-checklist)
- [10. Ask the user](#10-ask-the-user)
- [Sources](#sources)

<!-- /toc -->

## 1. Stock held in another country

### Why moving your own goods creates a VAT event

Moving goods you own from Sweden to a warehouse in another EU country is not a sale, but VAT
treats it as one. It is an **överföring av varor**: a deemed exempt intra-EU supply in Sweden and
a deemed intra-EU acquisition in the destination country. The consequence is a **registration
duty in that country**, in the company's own name.

| Step | Sweden | Destination country |
|---|---|---|
| Transfer out | Exempt intra-EU supply, **ruta 35**, and a line in the periodisk sammanställning against the company's own foreign VAT number | Intra-EU acquisition, output VAT self-assessed on the local return, input VAT deducted there |
| Later sale from that stock to a local consumer | Nothing — the goods were never in Sweden | Domestic supply in that country, on the **local** return, **not** in OSS |
| Later sale from that stock to a consumer in a third EU country | Nothing | Distance sale from that country — **this one can go in OSS** |

This is the single most expensive mistake in FBA bookkeeping. Amazon's pan-European programmes,
EFN and similar arrangements move inventory between fulfilment centres without asking, so the
registration duty can arise in a country the client has never heard of, months before anyone
notices. **Ask the user** which fulfilment programme is switched on and pull the marketplace's
own inventory-movement report before concluding anything.

### Call-off stock (avropslager) — and why FBA does not qualify

ML 5 kap. 15–21 §§ give a simplification: goods may be moved to a warehouse in another EU country
without triggering a transfer, provided the eventual buyer is **identified in advance** and
VAT-registered there, the seller keeps a register of the goods moved, and the buyer takes the
goods within **12 months**. The supply is then reported only when the buyer calls the goods off.
If the 12 months run out, or the goods are destroyed or stolen, the transfer is deemed to happen
and the registration duty appears retroactively; the options at that point are to bring the goods
back, substitute another pre-identified buyer, or register locally.

FBA stock fails the first condition outright — nobody knows who will buy it. Call-off stock is for
a named B2B customer's consignment warehouse, not a fulfilment centre. Do not offer it as a way
out of an FBA registration.

### What the Swedish books show

| Event | Swedish entry |
|---|---|
| Goods moved to a foreign warehouse | **No revenue, no cost.** The goods stay on **1460 Lager av handelsvaror**. Move them to a per-location sub-account (1461 SE, 1462 DE, 1463 PL …) so the stock count can be reconciled per warehouse |
| Freight of the transfer | **5711 Fraktkostnader**, or into inventory cost if the company capitalises freight (see `swedish-inventory`) |
| Local output VAT owed in that country | A liability sub-account of **2890 Övriga kortfristiga skulder**, one per country. Do **not** use 2611–2635, which map to Swedish rutor, and do **not** use **2670**, which is OSS only |
| Local input VAT recoverable there | A receivable sub-account of **1689 Övriga kortfristiga fordringar**, one per country |
| Foreign VAT that cannot be recovered | **6998 Utländsk moms** |
| Sale out of that stock | Revenue as normal; use a per-country sub-account of **3106** so the local return and OSS can be separated |

Valuation of the foreign stock is unchanged — same anskaffningsvärde, same lägsta värdets princip,
same inkurans assessment (`swedish-inventory`). What changes is that the count comes from the
fulfilment provider rather than from a physical count, so the verification behind the year-end
stock figure is the provider's inventory report plus a reconciliation of units shipped and sold.

---

## 2. Returns, credit notes and refunds

### The VAT correction

A return reduces the beskattningsunderlag. The seller issues an **ändringsfaktura** (credit note)
meeting the requirements in `swedish-invoice-compliance` — it must reference the original invoice
— and reverses output VAT at the **rate that applied to the original sale**.

The correction belongs to the period in which the change occurs, not to the period of the
original sale (ML 7 kap., *Ändring av tidigare redovisad utgående skatt*). A December sale
returned in February is a February correction. Do not reopen the original period, and do not
adjust the original invoice.

**Osäkert:** the exact paragraph numbers in ML 7 kap. (43–47 §§) for the change of previously
reported output VAT come from the consolidated law text only; Skatteverket's rättslig vägledning
blocks automated fetches and could not be consulted to confirm them.

### Worked entry — full return of a Swedish order

Original order 1 000 kr net + 250 kr VAT, cost of goods 400 kr, refunded in full and the item
goes back into sellable stock:

| Account | Debit | Credit |
|---|---|---|
| **3001** Försäljning inom Sverige, 25 % moms | 1 000 | |
| **2611** Utgående moms på försäljning inom Sverige, 25 % | 250 | |
| **1686** Fordringar för kontokort och kuponger (or **1930**) | | 1 250 |

and, if the company uses a perpetual inventory method, the goods go back with debit **1460 Lager
av handelsvaror** 400, credit **4960 Förändring av lager av handelsvaror** 400. Under a periodic
method nothing is booked here and the return is captured by the year-end stock count.

### The cases that go wrong

| Case | Treatment |
|---|---|
| Refund issued, goods never arrive | The supply was not undone. **Osäkert:** no primary source found stating whether output VAT may still be reduced. The defensible position is to reverse revenue and VAT only once the return is accepted, and otherwise to book the refund as a cost (**6990 Övriga externa kostnader**) with VAT retained. Escalate to the user before taking the reduction |
| Goods returned damaged and scrapped | Revenue and VAT reversed in full; the inventory loss goes to **4960** (or a scrapping account per the company's kontoplan), not against revenue |
| Partial refund / goodwill discount, goods kept | A price reduction, not a return: **3730 Lämnade rabatter** or **3790 Övriga intäktskorrigeringar**, with the VAT reduced proportionally and an ändringsfaktura issued |
| Return shipping charged to the customer | A separate taxable supply by the shop, not a negative cost — see section 3 |
| Return received after year end on a December sale | Correction in the new year. If material, consider a provision for expected returns at closing and discuss it with the user; K2 and K3 differ on whether a returns provision is recognised, so check `swedish-year-end-closing` before booking one |
| Original sale was at 12 % livsmedel moms before 1 April 2026, returned after | Reverse at **12 %** using **2621**, not at the 6 % rate now in force |

Reconcile the credit-note total to the provider's refund total every month. A refund that appears
in the settlement without a matching credit note is either a chargeback (section 7) or an
unbooked return.

---

## 3. Shipping and handling fees

### The rate on freight

Freight charged to the customer is part of the beskattningsunderlag, not a separate exempt item.
Skatteverket, *Så tar du ut moms*: "Frakt och portokostnader" are included in the tax base. In
practice the freight line carries the **same rate as the goods it carries**, because it is an
ancillary element of a single supply.

| Basket | Freight rate |
|---|---|
| All 25 % goods | 25 % |
| All 6 % goods (books, and livsmedel from 1 April 2026) | 6 % |
| Mixed rates | Apportion the freight across the rates |

**Osäkert:** no primary source was found prescribing a specific apportionment key for a
mixed-rate basket. Value of goods per rate is the common and defensible key; weight is arguably
better for physical transport. Pick one, apply it consistently, document it, and tell the user
which key the shop platform actually uses — many apply value and cannot be changed.

Revenue accounts: **3520 Fakturerade frakter**, with **3521 Fakturerade frakter, EU-land** and
**3522 Fakturerade frakter, export** for cross-border orders. Handling or small-order fees go to
**3540 Faktureringsavgifter**, with **3541** and **3542** for the EU and export variants.

### Free shipping

Free shipping is not a supply at nil value. The customer pays one inclusive price for goods
delivered, the whole amount is revenue on the goods accounts, and the shop's own carrier cost is
a cost. There is no output VAT to account for on a zero-rated freight line, and no uttagsbeskattning.
Book the carrier invoice to **5711 Fraktkostnader**, with transport insurance to **5712
Försäkringar vid frakter**.

Do not net the carrier cost against freight revenue. Gross presentation is what lets the user see
that a 49 kr shipping charge does not cover an 82 kr carrier cost.

### Buying the postage

| Purchase | Account | VAT |
|---|---|---|
| Parcel contract with PostNord, DHL, Budbee, Instabox | **5711 Fraktkostnader** | Swedish VAT, deduct as normal |
| Stamps and single letters | **6250 Porto** | See the Osäkert note below |
| Customs duty on imported consignments | **5721 Tullkostnader** | Not VAT |
| Broker / forwarder fee | **5722 Speditionskostnader** | Swedish VAT if a Swedish supplier |
| Shipping-broker platform (Sendify, Shipmondo and similar) | **5711** | Follow the broker's invoice, not the carrier's |

**Osäkert:** whether a given postal product is exempt could not be confirmed — Skatteverket's
*Momssatser och undantag från moms* page (checked 2026-09-17) does not list posttjänster among
the exemptions it enumerates, and rättslig vägledning is not reachable. Read the rate off the
supplier's own invoice rather than assuming, and do not claim input VAT that the invoice does not
show.

A shipping broker's invoice is the shop's purchase invoice. The carrier's own document is not a
verifikation for the shop, because the shop has no contractual relationship with the carrier.
Where the broker charges in a foreign currency or is established abroad, the purchase may be a
reverse-charge service — see `swedish-vat`.

---

## 4. Presentkort och rabattkoder

### Which kind of voucher

ML 2 kap. 27 § splits vouchers in two, and 5 kap. 40–44 §§ set the treatment.

| | Enfunktionsvoucher | Flerfunktionsvoucher |
|---|---|---|
| Test | The place of supply **and** the VAT due are known when it is issued | Anything else |
| Typical webshop case | A gift card valid only for one product category at one rate, in one country | An open-value gift card usable on the whole assortment |
| VAT due | On **issue**. ML 5 kap. 40 §: each transfer of an enfunktionsvoucher by a taxable person *"ska anses som en leverans av de varor eller ett tillhandahållande av de tjänster som vouchern avser"* | On **redemption**, on the underlying supply |
| Redemption | Not a further taxable transaction, unless the redeeming supplier is not the issuer | The taxable transaction |

A shop selling a mix of 25 % and 6 % goods almost always issues a **flerfunktionsvoucher**,
because the rate is not known at issue. A shop that sells only books, or only livsmedel, issues a
single-purpose voucher and owes the VAT immediately. The 1 April 2026 food rate change can move a
shop from one category to the other — a grocery webshop whose whole assortment sits at 6 % now
issues single-purpose vouchers where before it may have had two rates in play.

### Booking

Multi-purpose gift card sold for 500 kr:

| Account | Debit | Credit |
|---|---|---|
| **1686** Fordringar för kontokort och kuponger | 500 | |
| **2421** Ej inlösta presentkort | | 500 |

No VAT. On redemption against 500 kr of 25 % goods: debit **2421** 500, credit **3001** 400,
credit **2611** 100.

Single-purpose gift card sold for 500 kr against 6 % goods: VAT is due at sale, so debit **1686**
(or **1930**) 500, credit **2421 Förskott från kunder** 471,70 and credit **2631 Utgående moms på
försäljning inom Sverige, 6 %** 28,30. On redemption, debit **2421** 471,70 and credit **3003
Försäljning inom Sverige, 6 % moms** 471,70; no further VAT arises.

### Breakage

An expired or never-redeemed multi-purpose gift card is released from **2421** to income —
**3990 Övriga ersättningar, bidrag och intäkter** or a dedicated intäktskonto — when the legal
obligation to honour it ends.

**Osäkert:** whether output VAT falls due on breakage for a multi-purpose voucher could not be
confirmed in a primary source; no supply ever takes place, which argues no VAT, but the position
should be confirmed before the first material release. Also check the civil-law expiry: a
presentkort's validity is a contract and consumer-law question, not a tax one, and a shop that
has set no expiry cannot break the liability at all. Raise both with the user before releasing
anything to income.

### Rabattkoder

A discount code is a price reduction, not a voucher: the customer pays less, the
beskattningsunderlag is the reduced amount, and VAT is charged on what is actually paid.

| Situation | Account |
|---|---|
| Percentage or amount off at checkout | Reduce revenue directly, or book gross revenue and the discount to **3730 Lämnade rabatter** |
| Early-payment discount | **3731 Lämnade kassarabatter** |
| Volume / bundle discount | **3732 Lämnade mängdrabatter** |
| Influencer or affiliate code where the shop also pays a commission | Discount to **3730**; the commission is a cost to **6050 Försäljningsprovisioner** — two separate events, never netted |

---

## 5. Dropshipping

The shop never touches the goods, but it almost always **owns** them for a legal instant, and
that is what decides the VAT.

| Question | Why it decides the answer |
|---|---|
| Buy and resell, or act as an agent for the supplier? | Reselling makes the shop's revenue the full order value and the supplier's invoice a cost; agency makes the revenue only the commission. Read the supplier agreement — **ask the user** for it |
| Where do the goods physically start? | Sets the place of supply. Goods leaving a Chinese warehouse for a Swedish consumer are an import, not a Swedish sale |
| Who is the importer of record? | Decides who deducts the import VAT and whether the shop needs an EORI number |
| Consignment ≤ 150 EUR? | IOSS may apply — `eu-sales-and-oss.md` section 4 |
| Order placed through a marketplace? | The marketplace may be deemed supplier under ML 5 kap. 5–6 §§ — `eu-sales-and-oss.md` section 5 |

Chain transactions — supplier, shop and customer in three countries with one movement of goods —
are governed by ML 6 kap. (kedjetransaktioner). Only one leg of the chain carries the transport
and gets the zero rate; the others are domestic supplies somewhere. **Osäkert:** the paragraph
numbers (6 kap. 15–17 §§) are taken from the consolidated law text and could not be confirmed
against rättslig vägledning. Get a written analysis before advising on a three-country chain; this
is the area where a wrong answer creates a foreign registration duty retroactively.

The three common traps: booking the supplier's invoice as a cost and the customer's payment as
revenue while never noticing that the goods went from China to Sweden with no import declaration
in the shop's name, leaving no deductible import VAT and no customs entry to support it; charging
25 % Swedish VAT on a sale where the goods went from a German supplier straight to a French
consumer, where nothing about the transaction is Swedish; and treating a supplier's "we handle the
customs" as a tax conclusion rather than a description of their own logistics.

---

## 6. Payment providers

Start from `swedish-daily-bookkeeping/references/payment-providers.md` for the general pattern —
gross sale, provider fee, settlement receivable, payout. Only the e-commerce-specific parts are
here.

### The receivable account

Use **1686 Fordringar för kontokort och kuponger**, one sub-account per provider. BAS 2026 has no
1580; if a client's kontoplan carries 1580 from an older BAS year, map it to 1686 and note the
change. The balance on each sub-account should equal the provider's "pending payout" figure on
the last day of the month, and that is a hard reconciliation, not a soft one.

### Klarna's products

Klarna is not one thing, and the products differ in who carries the credit risk — which is what
decides whether the shop has a kundfordran at all.

| Product | What the shop has after the sale |
|---|---|
| Pay now (card, direct bank) | A settlement receivable on Klarna: **1686** |
| Pay later / invoice, where Klarna purchases the receivable | A settlement receivable on Klarna, not on the consumer. The consumer's default is Klarna's loss, not the shop's |
| Pay later / invoice, where Klarna acts only as an administrator and the shop retains the risk | A receivable on the **consumer**: **1511 Kundfordringar**. A default is the shop's kundförlust (section 7) |
| Instalments (delbetalning) | Normally purchased by Klarna, so **1686**. Revenue and VAT are recognised in full at delivery regardless of the customer's instalment plan |

**Ask the user which contract the shop is on.** The two invoice variants look identical in the
merchant portal and produce completely different balance sheets and completely different bad-debt
treatment. Klarna's own merchant documentation is reliable on settlement mechanics and is not a
source for the tax conclusion.

### Reserved and withheld amounts

Providers hold back a rolling reserve against future refunds and chargebacks. A reserve is **the
shop's money held by a third party** — it stays in **1686** (or a dedicated sub-account) as a
receivable, not a cost and not a provision, and must not be netted against fees. Confirm it to the
provider's statement every month; a reserve that has not moved in a year usually means a release
was booked to the wrong account.

Fees: card and provider transaction fees to **6040 Kontokortsavgifter**, marketplace and affiliate
commissions to **6050 Försäljningsprovisioner**, factoring fees to **6064 Factoringavgifter**, bank
charges to **6570 Bankkostnader**. Where the provider is established abroad the fee is normally a
reverse-charge service (`swedish-vat`).

---

## 7. Kundförluster and fraud losses

### When output VAT may be reduced

Only on a **konstaterad kundförlust** — established, not merely feared. Skatteverket (*Kundförluster
– om kunden inte kan betala*, checked 2026-09-17) accepts a bankruptcy where the shop holds an
unsecured claim in the estate, a Kronofogden report showing the debtor has no assets, or — for a
debt **under 1 000 kr** — at least eight months since the due date plus a payment reminder sent
and a collection demand (inkassokrav) issued. The reduction goes in the period the loss becomes
established; if the customer later pays, output VAT is reported again in the period the payment
arrives.

| Event | Entry |
|---|---|
| Befarad kundförlust at closing | Debit **6352 Befarade förluster på kundfordringar**, credit **1519 Nedskrivning av kundfordringar**. **No VAT reduction** |
| Loss becomes konstaterad | Reverse the befarad entry, then debit **6351 Konstaterade förluster på kundfordringar** with the net amount and **2611** (or **2621**/**2631** at the original rate) with the VAT, crediting **1511 Kundfordringar** with the gross |
| Disputed invoice pending | **1516 Tvistiga kundfordringar**. A dispute is not a loss and gives no VAT reduction |
| Payment arrives after write-off | Credit **3950 Återvunna, tidigare avskrivna kundfordringar** and re-report the output VAT |

A webshop only has kundfordringar where it carried the credit risk — invoice orders on its own
book, B2B orders, and Klarna arrangements where the shop retained the risk (section 6). Where the
provider bought the receivable there is no kundförlust to take, however loudly the provider
reports the consumer's default.

### Fraud, chargebacks and non-delivery

| Loss | Treatment |
|---|---|
| Card chargeback after the goods were delivered | **Osäkert.** No primary source was found confirming whether this reduces the beskattningsunderlag. The defensible position is to book the loss to **6351** or **6380 Förluster på övriga kortfristiga fordringar** and **not** reduce output VAT, unless it can be documented as a kundförlust against an identified debtor. Flag it to the user rather than deciding silently |
| Fraudulent order, goods dispatched, no identifiable customer | Same as above; **6380** is the better fit where there is no kundfordran to write off |
| Parcel lost in transit, shop refunds the customer | A return that never came back — section 2 |
| Provider fraud/chargeback fee | **6040 Kontokortsavgifter** |

Recurring fraud losses are a systems problem, not an accounting one. If the monthly total is
material, say so in the month-end note.

---

## 8. Kassaregister

### Why a pure webshop is exempt

The kassaregister obligation in SFL 39 kap. 4 § applies to cash and card payments taken in the
seller's presence. A webshop falls outside it on two separate grounds: **distans- och
hemförsäljning** is exempt under SFL 39 kap. 5 §, which Skatteverket lists among the activities
exempt without any application, and invoiced sales are outside 39 kap. 4 § altogether rather than
being an exemption — *"Du som fakturerar hela eller delar av din försäljning behöver inte
registrera den fakturerade försäljningen i ett kassaregister."*

There is also a de minimis: *"Du behöver inte ha ett tillverkardeklarerat kassaregister om du
säljer varor eller tjänster kontant eller mot betalning med kontokort för högst fyra prisbasbelopp
inklusive moms under ett räkenskapsår på tolv månader."* Skatteverket states *"Fyra prisbasbelopp
för år 2026 är 236 800 kronor (4 × 59 200 kronor)"* — a 2026 figure that changes every year.

### When the exemption stops

A shop with both a counter and a webshop is **not** exempt for the counter. The distance-selling
exemption covers the distance contracts, not the business. Once cash or card sales taken on the
premises exceed four prisbasbelopp in a twelve-month financial year, a manufacturer-declared
kassaregister is required for those sales.

| Setup | Kassaregister? |
|---|---|
| Webshop only, all orders shipped | No |
| Webshop plus click-and-collect where the customer pays online in advance | No — payment is not taken at the counter |
| Webshop plus click-and-collect where the customer can pay on pickup | Yes for the pickup payments, if over four prisbasbelopp |
| Webshop plus a physical shop, market stall or pop-up | Yes for the physical sales, if over four prisbasbelopp |
| Webshop plus B2B, all invoiced | No |

Skatteverket also notes that app or web ordering in a restaurant where the customer is sitting in
the restaurant does not count as a distance contract — relevant to any webshop client that also
runs a café.

A discretionary exemption can be applied for on form **SKV 1510** where a kassaregister is
impossible to use or the sales can be verified in another reliable way.

---

## 9. Month-end reconciliation checklist

Run in this order; each step feeds the next.

1. **Webshop order report → revenue.** Export gross sales by VAT rate and by destination country
   for the period, on the shop's own accrual (delivery) date, not on the payment date. Tie the
   total to the revenue accounts. A difference is normally orders shipped after month end.
2. **Revenue by rate.** With two food rates live in 2026, split at 1 April and check that no
   post-April order carries 12 % and no pre-April credit note carries 6 %.
3. **Provider settlements → 1686.** One reconciliation per provider: opening balance + gross
   sales − fees − refunds − chargebacks − payouts ± reserve movement = closing balance. Agree the
   closing balance to the provider's pending-payout figure. Investigate any difference before
   closing; a rolling unexplained balance here hides everything else.
4. **Payouts → bank.** Every payout on the settlement report appears on **1930**, with no
   timing difference older than a few days.
5. **Refunds → credit notes.** Every refund in a settlement has an ändringsfaktura. Anything
   unmatched is a chargeback or an unbooked return.
6. **Stock.** Units sold per the order report + returns received = units out of the warehouse per
   the fulfilment provider's report. Reconcile per warehouse if stock sits in more than one
   country. Then value per `swedish-inventory`.
7. **Gift-card liability.** **2421** = the shop platform's outstanding gift-card balance. These
   drift apart silently and are usually only discovered at year end.
8. **VAT per country.** Swedish rutos from the ordinary momsdeklaration; **2670** sub-accounts
   agreed to the OSS return per country; foreign **2890** sub-accounts agreed to each local
   return. The sum of revenue accounts should exceed the sum of the momsdeklaration rutor by
   exactly the OSS and foreign-domestic turnover — check that difference, do not assume it.
9. **Distance-selling threshold.** Update the running calendar-year total of EU consumer sales
   (goods **and** digital services) against 99 680 kr and report the headroom.
10. **Clear 2650.** All 261x–264x accounts clear to **2650 Redovisningskonto för moms**.
    **2670** does not — it is settled separately in euro.

---

## 10. Ask the user

1. Which fulfilment programme is active, and in which countries does stock physically sit?
2. Which Klarna or provider contract — does the shop retain the credit risk on invoice orders?
3. Perpetual or periodic inventory? It decides whether returns move stock accounts monthly.
4. What are the gift-card terms — expiry, restrictions, single or multi-purpose?
5. Is there any physical point of sale, including markets and pop-ups?
6. For dropshipping: the supplier agreement, and who is importer of record.
7. Which freight apportionment key does the shop platform apply on mixed-rate baskets?

---

## Sources

All web pages checked **2026-09-17**.

**Statutes, current consolidated form**

| Statute | Provisions relied on | Used for |
|---|---|---|
| Mervärdesskattelag (2023:200) | 2 kap. 27 §; 5 kap. 15–21 §§; 5 kap. 40–44 §§; 6 kap. (kedjetransaktioner); 7 kap. (ändring av tidigare redovisad utgående skatt); 8 kap. (beskattningsunderlag) | Vouchers, call-off stock, chain transactions, credit-note period, price reductions |
| Skatteförfarandelag (2011:1244) | 39 kap. 4–5 §§ | Kassaregister obligation and exemptions |

Consolidated ML and SFL text read via lagen.nu and riksdagen.se. **Osäkert:** Skatteverket's
*rättslig vägledning* (www4.skatteverket.se) blocks automated fetches and could not be consulted,
so the paragraph numbers in ML 5 kap. 15–21 §§, ML 6 kap. 15–17 §§ and ML 7 kap. 43–47 §§, and the
point numbering within SFL 39 kap. 5 §, come from the consolidated law text alone and are marked
as such where used. The kundförlust provision in ML 8 kap. could not be pinned to a paragraph
number and is therefore cited only to the chapter. No amendment to any of these for financial
years beginning in 2026 was identified, and none is known to be announced for 2027.

**Skatteverket** (skatteverket.se, all checked 2026-09-17)

*Momssatser och undantag från moms* — 6 % on livsmedel from 1 April 2026, verbatim: *"Från och med
den 1 april 2026 ska du ta ut 6 procent moms när du säljer livsmedel"*; restaurant service stays
at 12 %. The page gives no end date and lists no postal exemption · *Så tar du ut moms* — "Frakt
och portokostnader" included in the beskattningsunderlag · *Kundförluster – om kunden inte kan
betala* — konstaterad loss, evidence, the under-1 000 kr conditions, re-reporting on later
payment · *Utlägg och vidarefakturering* — utlägg vs vidarefakturering test · *Överföring av varor
mellan EU-länder* — deemed supply and acquisition, ruta 35, call-off stock and the 12-month limit
· *Vissa verksamheter är undantagna från kravet på kassaregister* — distans- och hemförsäljning,
the invoicing exemption, and verbatim *"Fyra prisbasbelopp för år 2026 är 236 800 kronor (4 ×
59 200 kronor)"*, plus form SKV 1510 · *Kassaregister*.

**BAS 2026 kontoplan**, bas.se, file `BAS_kontoplan_2026_v2.xlsx`, downloaded 2026-09-17. Every
account number and name in this file was matched against that file directly. Note two BAS 2026
facts that older material gets wrong: the settlement receivable is **1686**, not 1580, and there
is no 1515 — doubtful receivables sit in **1516 Tvistiga kundfordringar** and **1519 Nedskrivning
av kundfordringar**.

**Not used as a source for any conclusion:** marketplace, Klarna, carrier and shipping-broker
documentation. Where their settlement mechanics are described above, that is a description of
their own process, never the tax treatment.
