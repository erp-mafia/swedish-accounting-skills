# Revenue Recognition for SaaS and Software Companies

Scope: subscription and licence revenue in a Swedish AB. Periodisering, bokslut and VAT mechanics in general live in `swedish-year-end-closing`, `swedish-vat` and `swedish-invoice-compliance`. VAT on SaaS sales is in `saas-moms-och-utveckling.md`.

**Which year this describes.** K2 and K3 points are quoted from BFN's consolidated vägledningar for räkenskapsår beginning after 2025-12-31: K2 (BFNAR 2016:10) as amended by **BFNAR 2025:2**, K3 (BFNAR 2012:1) as amended by **BFNAR 2025:3** and **2025:4**. For a calendar-year company FY2026 is already on this text; FY2025 is not, and several points below differ there. Accounts are BAS 2026 v1.1. Sources and check dates in section 13.


## Table of contents

1. The three clocks
2. BAS 2026 accounts
3. Prepaid subscriptions and förutbetald intäkt
4. K2 versus K3 for subscriptions
5. Multi-component contracts
6. Setup fees, usage, credits and free months
7. Refunds, cancellations, churn and provisions
8. Principal versus agent
9. Foreign currency invoicing
10. Metrics versus bokförd intäkt
11. Worked examples
12. Ask the user
13. Sources

---

## 1. The three clocks

| Clock | Triggered by | Ledger effect | Governed by |
|-------|--------------|---------------|-------------|
| Invoicing | Faktura issued | **1510**, **2611** | ML 2023:200 17 kap |
| Cash | Payment settled | **1930**, **1686** | — |
| Revenue | Service delivered over time | **3001** / **3305** / **3308** against **2970** | K2 punkt 6.11, K3 punkt 23.26 |

A prepaid annual subscription invoiced on 1 February hits clock 1 in February, clock 2 in February or March, and clock 3 in twelve slices to January. Booking the invoice straight to revenue applies kontantprincipen to a tjänsteuppdrag and overstates the year's result.

**VAT does not follow the revenue clock.** The beskattningsgrundande händelse normally occurs at the tillhandahållande (ML 7 kap 4 §), but where the seller receives payment for an ordered service first, it occurs when that payment reaches the seller (7 kap 7 §). Output VAT is reported for the redovisningsperiod given by ML 7 kap 14 §, which includes the period a förskotts- or a conto-betalning was received. The whole year's VAT therefore falls in one period and is never spread to match the periodisering.

---

## 2. BAS 2026 accounts

BAS 2026 does not split domestic sales into goods and services. Kontogrupp 30 is **3000 Försäljning inom Sverige** with only 3001–3004 beneath it, unchanged from BAS 2025. Ledgers showing an account such as 3041 are using a locally defined konto in the same kontogrupp; 3001 is the published account.

| Account | Name (BAS 2026) | Use |
|---------|-----------------|-----|
| **3001** | Försäljning inom Sverige, 25 % moms | Swedish subscription, licence and service revenue |
| **3004** | Försäljning inom Sverige, momsfri | Only for genuinely exempt supplies |
| **3305** | Försäljning tjänster till land utanför EU | Customers outside the EU |
| **3308** | Försäljning tjänster till annat EU-land | B2B reverse charge within the EU |
| **3730** / **3790** | Lämnade rabatter / Övriga intäktskorrigeringar | Discounts and credits after invoicing |
| **3921** / **3922** | Provisionsintäkter / Licensintäkter och royalties | Agent commission; perpetual licence and royalty income |
| **3960** / **7960** | Valutakursvinster / -förluster på fordringar och skulder av rörelsekaraktär | FX on kundfordringar |
| **1510** | Kundfordringar | Receivable |
| **1686** | Fordringar för kontokort och kuponger | Card/processor clearing. New in BAS 2026; replaces 1580, which was removed |
| **1780** | Upplupna avtalsintäkter | Usage consumed, not yet invoiced |
| **2420** / **2421** | Förskott från kunder / Ej inlösta presentkort | Advance before delivery starts; unredeemed credits |
| **2970** / **2979** | Förutbetalda intäkter / Övriga förutbetalda intäkter | **The subscription deferral account** |
| **2450** | Fakturerad men ej upparbetad intäkt | Only for uppdrag measured by färdigställandegrad |
| **2290** / **2220** | Övriga avsättningar / Avsättningar för garantier | Refund and warranty provisions |

In the balansräkning **2970** sits in *Upplupna kostnader och förutbetalda intäkter*, **2420** in *Förskott från kunder*.

Do not use **2450** for subscriptions — it belongs to uppdrag recognised by completion (K3 punkt 23.27, K2 punkterna 6.21/6.24). A subscription recognised linearly produces a förutbetald intäkt, which is **2970**.

BAS 2026 has no revenue account for B2C sales declared through OSS. OSS reports per destination country, so define free sub-accounts in kontogrupp 33 per country and use **2670 Utgående moms på försäljning inom EU, OSS** for the VAT.

---

## 3. Prepaid subscriptions and förutbetald intäkt

```
Invoice issued
Debet  1510  Kundfordringar                    inkl. moms
Kredit 3001  Försäljning inom Sverige, 25 %    exkl. moms
Kredit 2611  Utgående moms 25 %                momsen

Defer the unearned part
Debet  3001  /  Kredit 2970                    unearned portion

Each month thereafter
Debet  2970  /  Kredit 3001                    month's share
```

Crediting 3001 in full and immediately deferring, or crediting 2970 in full and releasing from month one, are both acceptable. The first keeps the billing system's gross invoice value on the revenue account and reconciles more easily.

**Invoicing is not delivery.** K2 exempel 6 k (*Försäljning av gymkort*) states that because the seller has performed no part of its prestation merely by selling the annual card, the payment is a förutbetald intäkt recognised linearly as the usage period runs, with the remainder shown as a liability in *Upplupna kostnader och förutbetalda intäkter*. K2 punkt 6.6 andra stycket generalises it: only the part of the inkomst belonging to the räkenskapsår is an intäkt of that year.

**2970 versus 2420.** Use **2420** where money was taken before any delivery period started — a deposit for an implementation not yet begun, or an annual plan paid in December for a period starting in March. Once the period is running, the unearned balance is **2970**.

The release follows the contract period, not the invoice month. K2 punkt 6.11 requires recognition "linjärt över den överenskomna tidsperioden", and its kommentar defines the intäkt as the part of the agreed price corresponding to the accounting period's length relative to the total agreed period. Pro-rata by days is the faithful reading; a 1/12 convention only where immaterial.

**The 7 000-kronor shortcut generally does not help a subscription business.** From räkenskapsår beginning after 2025-12-31, K2 punkt 2.4 (BFNAR 2025:2) allows skipping periodisering of inkomster and utgifter individually below **7 000 kronor** — raised from 5 000 kronor — and new punkt 2.4A allows an erhållet förskott below 7 000 kronor to be taken to revenue. New punkt 2.4B forbids using 2.4, 2.4A and 7.9 to the extent they would have a väsentlig effect on the company's intäkter, kostnader or ställning, and its kommentar names this case: a company selling årsabonnemang where individual contracts are under 7 000 kronor but most are signed late in the year must periodise them. Punkt 7.9 (återkommande utgifter varying under 20 %) applies to **utgifter** only; there is no recurring-income equivalent.

---

## 4. K2 versus K3 for subscriptions

| Question | K2 (BFNAR 2016:10 as amended by 2025:2) | K3 (BFNAR 2012:1 as amended by 2025:3) |
|----------|------------------------------------------|-----------------------------------------|
| Governing point | punkt 6.11 | punkt 23.26 |
| Definition | Uppdrag med ett obestämt antal aktiviteter under en överenskommen tidsperiod, not provisionsbaserat, not löpande räkning, income for that period | Tjänsteuppdrag med ett obestämt antal aktiviteter under en bestämd tidsperiod |
| Default | Linjärt över tidsperioden | Linjärt över tidsperioden |
| Alternative method | None | Another method if it better reflects färdigställandegraden |
| Dominant activity | Value over **70 %** of the uppdrag's income ⇒ the **whole** intäkt on performance (kommentar to 6.11; the 70 % figure is new in the post-2025 text) | "Mer väsentlig än andra" ⇒ recognised on performance. No quantified threshold |
| Splitting a contract | punkt 6.2 andra stycket: split where necessary to reflect the ekonomiska innebörd and the parts and amounts can be identified separately (new wording, 2025:2) | punkt 23.7, same test; segmenting of uppdrag per 23.13–23.16 |
| Dev cost capitalisation | Prohibited (punkt 10.4) | Policy choice (punkt 18.7) |
| Uppskjuten skatt | Prohibited (punkt 16.4) | Required |

K2's 70 % test is the practical tool. A twelve-month plan where first-month onboarding is genuinely worth more than 70 % of the annual fee is not a subscription under K2 — the whole fee is recognised when onboarding completes.

**BFNAR 2025:2 and 2025:3 are law, not proposals.** Both were decided 2025-06-16, are in force from that date, and apply first to räkenskapsår beginning after 2025-12-31. A company starting business after 2025-06-30 with a förlängt räkenskapsår ending 2026-12-31 or later applies them already for that year. BFNAR 2025:4 (2025-12-15) added transitional provisions to K3. Neither BFNAR 2016:10 nor 2012:1 was replaced; both were amended in place.

Osäkert: early application. The ikraftträdandebestämmelser contain no "får tillämpas tidigare" clause, which reads as unavailable, but there is no express prohibition.

What changed for a SaaS company:

- **K2 punkt 6.11** restated; the 70 % threshold in its kommentar is new.
- **K2 punkt 6.2** gained an explicit splitting rule, aligning K2 with K3 punkt 23.7.
- **K2 punkt 2.4** rose to 7 000 kronor; **2.4A** and **2.4B** are new.
- **K2 punkt 1.1A** now bars company types from K2 outright. Item **g)** bars "företag som under räkenskapsåret har förvärvat varor eller tjänster mot aktierelaterade ersättningar", and K3 punkt 26.2 defines aktierelaterade ersättningar as covering ersättningar to parties "inklusive anställda". A company granting personaloptioner or issuing warrants for services should expect to leave K2 from the first räkenskapsår beginning after 2025-12-31. Item **i)** does the same for kryptotillgångar, **f)** for a filial abroad. New punkt 1.1B adds companies with a väsentlig uppskjuten skatteskuld, with a carve-back in 1.1C for very small companies.
- **K3 punkt 23.7** amended (editorial). **Punkt 23.26 and chapter 18 were not amended** by BFNAR 2025:3.

Flag punkt 1.1A g) before any option programme is designed. Leaving K2 pulls in uppskjuten skatt, fuller noter and K3 chapter 26 valuation work.

---

## 5. Multi-component contracts

A licence plus an implementation project plus annual support is three revenue patterns sold as one.

**K3** applies punkt 23.7: each transaction separately, but "om det är nödvändigt för att rätt återge den ekonomiska innebörden och delarna och beloppen kan identifieras separat, ska en transaktion redovisas i delar". Its kommentar gives exactly this case — a selling price including an identifiable amount for service och underhåll is periodised over the periods the work is performed. Punkterna 23.13–23.16 govern when a tjänsteuppdrag is segmented (separate anbud, separately negotiated with a right to accept or reject, separately identifiable inkomst and utgifter) or combined.

**K2** reaches the same starting point through punkt 6.2 andra stycket, whose kommentar uses the same service-och-underhåll example (exempel 6 c). Beyond the split, the contract is classified under punkterna 6.9–6.12: provisionsbaserat (6.9), löpande räkning (6.10), obestämt antal aktiviteter (6.11), or by elimination fast pris (6.12).

| Component | K2 | K3 |
|-----------|----|----|
| Perpetual licence delivered at start | punkt 6.6 criteria; **3922** | punkt 23.8; royalty/licence timing per 23.28 |
| Subscription access | punkt 6.11, linear; **3001** | punkt 23.26, linear; **3001** |
| Implementation, fixed price | punkterna 6.15–6.25 | punkterna 23.18–23.24 |
| Implementation, time and materials | punkterna 6.10, 6.13–6.14 | punkt 23.17 |
| Support and maintenance | punkt 6.11, linear | punkt 23.26, linear |
| Usage-based or term licence fee | punkt 6.26 table | punkt 23.28, per the agreement's ekonomiska innebörd |

For fixed-price implementation work see `swedish-project-accounting` (färdigställandegrad, **1620**, **2450**, befarade förluster).

---

## 6. Setup fees, usage, credits and free months

**Setup and onboarding fees.**

| Fact pattern | Treatment |
|--------------|-----------|
| Covers migration, integration or configuration the customer could buy separately, separately priced | Separate part under K2 punkt 6.2 / K3 punkt 23.7. Recognise when performed |
| Non-refundable, mandatory, nothing separable | Part of the subscription price. Defer to **2970**, release over the period |
| Value over 70 % of the uppdrag's income (K2) or "mer väsentlig" (K3) | Whole contract income when that activity completes — K2 punkt 6.11 andra stycket, K3 punkt 23.26 andra stycket |

Ask the user which it is. Do not infer it from the invoice line text.

**Usage and overage.** Earned as the usage occurs, not when metered or invoiced. Accrue at period end where invoiced in arrears:

```
Debet  1780  Upplupna avtalsintäkter   /   Kredit 3001    usage earned, excl. moms
```

No moms on the accrual — VAT arises under ML 7 kap. This is the mirror of **2970** and the two are never netted.

**Credits and prepaid balances.** A pot of credits usable against future services is a voucher. ML 2023:200 defines voucher, enfunktionsvoucher and flerfunktionsvoucher in 2 kap 26–27 §§, with timing in 5 kap 40–44 §§: transfer of an enfunktionsvoucher is treated as the underlying supply, a flerfunktionsvoucher is taxed on redemption. Credits redeemable only against the company's own 25 % Swedish services are normally an enfunktionsvoucher, so VAT arises on sale. Book proceeds to **2970** (or **2421** where unredeemed value is tracked separately) and release as credits are consumed. Breakage is recognised when the right to use lapses under the contract, never on an estimate of future lapse.

**Free months and discounts.** "12 months for the price of 10" is a 12-month period at an agreed price of 10 months' fee: under K2 punkt 6.11 and K3 punkt 23.26 that price spreads linearly, so 10/12 of a monthly fee each month, not two months of zero. K3 punkt 23.3 measures revenue at fair value of what will be received, less "handelsrabatter, mängdrabatter och liknande prisavdrag". A free trial before any contract carries no revenue and no receivable. For loyalty or credit-back programmes, K2's kommentar to punkt 6.2 requires both a revenue reduction and an avsättning, measured from the selling price rather than the expected cost of honouring it.

---

## 7. Refunds, cancellations, churn and provisions

**Crediting a prepaid period.** The unused part already sits on **2970**; the kreditfaktura clears that balance rather than reversing earned revenue.

```
Debet  2970  Förutbetalda intäkter     unused portion, excl. moms
Debet  2611  Utgående moms 25 %        moms on the credited amount
Kredit 1510  Kundfordringar            gross credited
```

Where cash was already paid, credit **1930** on settlement. If the credit exceeds the **2970** balance — a goodwill refund covering delivered months — the excess reduces revenue: **3790** (or **3730** if presented as a discount), never a cost account.

**Money-back guarantees: revenue gross, refund as a provision.** K3's kommentar to punkt 23.8 states that a company offering the customer their money back if dissatisfied still recognises the revenue and books an avsättning för returer under chapter 21. K2 exempel 6 a (*Öppet köp*) reaches the same result, citing punkterna 6.6, 6.7, 16.2 and 16.7. Do not net expected refunds against revenue.

| Situation | Provision? |
|-----------|-----------|
| Expected non-renewal next year | No |
| Contractual money-back guarantee open at balansdagen | Yes |
| SLA credits earned by downtime that already occurred | Yes |
| Announced refund programme the company cannot realistically withdraw from | K3 yes (informell förpliktelse, punkt 21.6); **K2 no** — punkt 16.2 requires a legal åtagande, and its kommentar states informella åtaganden får inte redovisas som skuld eller avsättning |
| Expected credit losses on kundfordringar | Not a provision — value the receivable (K2 punkt 13.4, **1519**) |

K3 punkt 21.4 requires a befintlig legal or informell förpliktelse from a past event, a probable outflow and a reliable estimate; punkt 21.9 nuvärde, punkt 21.12 remeasurement each balansdag. K2 punkt 16.2 requires the same three conditions but only for a **legal** åtagande. K2 punkt 16.6 lets a company skip provisions totalling under the lower of 25 000 kronor and 10 % of opening equity, except pensionsåtaganden. Under K2 an outflow that is *expected* rather than merely *sannolikt* is a skuld.

---

## 8. Principal versus agent

K3 punkt 23.2: "Det inflöde av ekonomiska fördelar som företaget erhållit eller kommer att erhålla **för egen räkning** ska redovisas som intäkt." Its kommentar: amounts received for a huvudman's account do not increase equity, and "företagets intäkt är erhållen provision". K2 punkt 6.2 uses the same "för egen räkning" wording, with mervärdesskatt and what a kommissionär receives as the för annans räkning examples. K2 punkt 6.9 defines a provisionsbaserat uppdrag as one where the income is based on the outcome of the sale of someone else's assets or services; the punkt 6.26 table recognises it as the provisionsgrundande sale or service is completed and the remaining contract conditions are met.

**Neither K2 nor K3 gives a list of principal/agent indicators** — the test in both is the single criterion. The factors below are how that criterion is applied in practice, not BFNAR rules: who sets the price, who carries credit and refund risk, who is responsible for delivering and for putting delivery right, who holds the contract with the end customer, and who bears licence or inventory risk.

| Arrangement | Who acts för egen räkning | Revenue |
|-------------|---------------------------|---------|
| Reselling another vendor's software on own contract, own price, own credit risk | You | Gross to **3001**; vendor cost to **6910** or **6540** |
| Referring customers for a commission | The vendor | Net to **3921** |
| Selling your app through a store that is merchant of record | The store | Net payout to **3001** |
| Marketplace that only introduces the customer and bills in your name | You | Gross to **3001**; fee to **6540** |
| Affiliate paying you for traffic | The programme owner | Net to **3921** |

App-store distribution is the case most often booked wrong. Where the store is merchant of record and contracts with the end user in its own name, it sets the price and bears credit and refund risk, so the developer's inflow för egen räkning is the net payout — the store's commission is not the developer's cost, because it was never the developer's revenue. Where the store is only a payment processor and the developer contracts with the end user, the developer reports gross and the commission is a cost. Read the distribution agreement; the same store can run both models in different countries.

One easy misbooking: K2's kommentar to punkt 6.2 states that fakturerade utlägg, for example travel and lodging recharged to a customer, **are** received för egen räkning and belong in the inkomst. They are revenue, not a pass-through.

---

## 9. Foreign currency invoicing

**Rate at invoicing.** Neither K2 nor K3 states this in its allmänna råd; the rule is BFNAR 2013:2 punkt 2.4 — an affärshändelse in another currency is translated at the **avistakurs per dagen för affärshändelsen**. Punkt 2.5 (amended by BFNAR 2024:1) permits instead (a) an approximation of actual rates that does not deviate too far from the avistakurs, or (b) **the rate that applies to the affärshändelse under ML 2023:200**. Option (b) lets the invoice, the VAT and the ledger run on one rate. K3's kommentar to punkt 30.1 says the same. As avistakurs, BFN accepts Riksbanken's daily mittkurs or the ECB's daily rate.

**The moms amount.** ML 17 kap 29 § requires the mervärdesskattebelopp to be stated **also in svenska kronor** where the VAT is payable to the Swedish state (in euro instead for a company with EUR accounting), converted per ML 8 kap 21–23 §§. ML 8 kap 21 § allows either the latest average rate set on the most representative currency market in Sweden or the latest rate published by the ECB, taken at the beskattningsgrundande händelse — for a prepaid subscription the receipt of payment (7 kap 7 §), not the invoice date.

Osäkert: whether the chosen rate source in ML 8 kap 21 § must be used consistently between periods. The statute says "eller" and states no express consistency requirement; Skatteverket's rättslig vägledning (www4.skatteverket.se) blocks automated retrieval and could not be checked. Use one source consistently and verify before advising otherwise.

**Revaluation at balansdagen.** K2 punkt 13.5: kortfristiga fordringar i utländsk valuta **ska** värderas till balansdagens kurs, with a terminssäkrad portion at terminskursen (punkt 11.8 långfristiga fordringar, 14.6 kassa och bank, 17.8 skulder). K2 requires this even though ÅRL 4 kap 13 § only permits it — the kommentar to punkt 13.5 says so in terms. K2 accepts Riksbanken's or the ECB's daily rate as avistakurs, normally the bank's köpkurs for receivables, and allows an average rate only if used for **both** fordringar and skulder and only if it does not deviate too far. K3 punkt 30.3: monetära poster at balansdagens kurs; punkt 30.5 defines them.

**2970 is not revalued.** The kommentar to K3 punkt 30.5 lists **förutbetalda intäkter** and **förskott från kunder** among the icke-monetära poster, alongside varulager and förutbetalda kostnader, while naming kundfordringar and leverantörsskulder as monetära. A deferred subscription liability is settled by delivering a service, not by paying a fixed amount, so it stays at the rate at which it arose. The kundfordran is revalued; the deferral is not. This is the most common FX error in a SaaS ledger.

**Where the difference goes.** K3 punkt 30.6 puts valutakursdifferenser in the resultaträkning in the year they arise; punkt 30.7 classifies them "antingen som en rörelsepost eller som en finansiell post utifrån den underliggande affärshändelsen".

| Item | Gain | Loss |
|------|------|------|
| Kundfordringar, leverantörsskulder (rörelsekaraktär) | **3960** | **7960** |
| Bank and other kortfristiga fordringar of a financial nature | **8331** | **8336** |
| Skulder of a financial nature | **8431** | **8436** |

---

## 10. Metrics versus bokförd intäkt

| Metric | Why it differs from bokförd intäkt |
|--------|-----------------------------------|
| MRR | Normalised run-rate at a point in time. Ignores partial months, usage, one-off fees, credits |
| ARR | MRR × 12. Forward-looking; no accounting meaning |
| Billings | Clock 1. Includes the whole prepaid year |
| Deferred revenue (billing system) | Usually contract periods only, excluding one-off fees and manual invoices, often net of expected churn |
| Nettoomsättning | Clock 3. K2 punkt 6.11 / K3 punkt 23.26, excluding moms |

**The reconciliation to run each period.** Anchor on the deferral account:

```
Opening 2970 + deferred this period − released to revenue − credited = Closing 2970
```

Tie each line to a source: deferred to the billing system's new contract value, released to the sum of the period's revenue schedules, credits to the kreditfakturor. Reconcile **1510** to the open invoice list and **1686** to the processor's payout report, and confirm 3001 + 3305 + 3308 equals the billing system's recognised revenue. A residual on 2970 with no remaining contract period is a missed release or a credit booked to revenue instead of to the deferral.

**Bokföringslagen requirements.** A billing system feeding the revenue entries is sidoordnad bokföring under BFL 5 kap 4 §, and BFL 5 kap 11 § requires systemdokumentation och behandlingshistorik for it. Two mechanisms allow summarised ledger entries:

- **Gemensam verifikation**, BFL 5 kap 6 § tredje stycket. BFNAR 2013:2 punkt 6.1 lists which likartade affärshändelser qualify, and item **b) affärshändelser som genereras automatiskt** covers automated subscription invoicing. The same punkt requires "ett system för intern kontroll av levererade varor och utförda tjänster", and the verifikation must still carry the BFL 5 kap 7 § information per affärshändelse.
- **Bokföring i sammandrag**, BFNAR 2013:2 punkt 2.11: affärshändelser already booked in registreringsordning in a delsystem may be summarised into one bokföringspost in the systematic ordering (punkterna 2.9 and 2.10 cover same-day and received-invoice cases).

Never let the ledger hold only a net payout figure from the payment processor. Gross revenue, processor fees and VAT must remain separable.

---

## 11. Worked examples

### Annual prepaid subscription starting mid-month

Swedish AB, calendar räkenskapsår. Annual plan 24 000 kr excl. moms invoiced 2026-03-12 for 2026-03-12 – 2027-03-11 (365 days), Swedish B2B customer, 25 % moms, paid 2026-03-25. Daily rate 24 000 / 365 = 65,7534 kr. Days in 2026: 20 (March) + 275 (April–December) = 295. Days in 2027: 70.

| Date | Konto | Namn | Debet | Kredit |
|------|-------|------|-------|--------|
| 03-12 | 1510 | Kundfordringar | 30 000,00 | |
| | 3001 | Försäljning inom Sverige, 25 % moms | | 24 000,00 |
| | 2611 | Utgående moms på försäljning inom Sverige, 25 % | | 6 000,00 |
| 03-12 | 3001 | Försäljning inom Sverige, 25 % moms | 24 000,00 | |
| | 2970 | Förutbetalda intäkter | | 24 000,00 |
| 03-31 | 2970 | Förutbetalda intäkter | 1 315,07 | |
| | 3001 | Försäljning inom Sverige, 25 % moms | | 1 315,07 |

April–December release 30 or 31 days each, 18 082,19 in total. Revenue recognised in 2026 is 295 × 65,7534 = **19 397,26 kr**; the 2026-12-31 balance on **2970** is 70 × 65,7534 = **4 602,74 kr**, released January–March 2027.

All 6 000,00 of output VAT falls in one redovisningsperiod — here March 2026, since invoice and payment both fall in March. The periodisering does not touch it.

### Mid-term upgrade

Same contract. On 2026-09-01 the customer upgrades to a plan priced at 36 000 kr per year for the remainder of the term: 2026-09-01 – 2027-03-11 = 192 days.

- Unearned on **2970** at 2026-08-31: 192 × 65,7534 = 12 624,66 kr
- Remaining term at the new price: 192 × (36 000 / 365) = 192 × 98,6301 = 18 936,99 kr
- Incremental amount to invoice: 18 936,99 − 12 624,66 = **6 312,33 kr** excl. moms

| Date | Konto | Namn | Debet | Kredit |
|------|-------|------|-------|--------|
| 09-01 | 1510 | Kundfordringar | 7 890,41 | |
| | 3001 | Försäljning inom Sverige, 25 % moms | | 6 312,33 |
| | 2611 | Utgående moms på försäljning inom Sverige, 25 % | | 1 578,08 |
| 09-01 | 3001 | Försäljning inom Sverige, 25 % moms | 6 312,33 | |
| | 2970 | Förutbetalda intäkter | | 6 312,33 |

The **2970** balance is now 18 936,99 and the release rate for the rest of the term is 98,6301 kr per day; September (30 days) releases 2 958,90 kr.

Note what was **not** done: no revenue reversed, no prior month restated, and March–August revenue on the old plan stands. An upgrade reprices the remaining period prospectively — neither K2 punkt 6.11 nor K3 punkt 23.26 supports retrospective adjustment. A downgrade with a partial refund follows section 7; a downgrade with a credit carried forward reduces the **2970** release rate over the remaining days.

---

## 12. Ask the user

1. **K2 or K3, and for which räkenskapsår?** If K2, check punkt 1.1A — options or warrants for goods or services, a filial abroad, kryptotillgångar or convertible-type instruments all bar K2 from the first räkenskapsår beginning after 2025-12-31.
2. **What is the contract period**, and is it the same as the invoicing period?
3. **Is the setup fee separately identifiable**, or part of the subscription price?
4. **Is there a dominant activity** worth more than 70 % of the uppdrag's income (K2) or materially more significant than the rest (K3)?
5. **Principal or agent** on every reseller, marketplace and app-store channel — ask for the distribution agreement, not the payout report.
6. **Which FX rate source**, and is it the same for the ledger entry and the moms figure?
7. **Are credits refundable in cash, and do they expire?** This decides voucher versus förskott and when breakage may be recognised.
8. **Any contractual money-back guarantee or SLA credit** outstanding at balansdagen?
9. **What is the source of truth** for the revenue schedule, and who reconciles it to the ledger?

---

## 13. Sources

All checked 2026-09-17. Primary sources only; nothing here is sourced to a secondary publisher.

- **BFN, K2 vägledning**, consolidated version for räkenskapsår beginning after 2025-12-31 (BFNAR 2016:10 as amended by **BFNAR 2025:2**), `bfn.se/wp-content/uploads/vl16-10-k2ar-kons2025.pdf` — punkterna 1.1, 1.1A–1.1C, 2.4, 2.4A, 2.4B, 6.2, 6.6, 6.9, 6.11, 6.12, 6.26, 7.9, 10.4, 13.4, 13.5, 16.2, 16.4, 16.6, 17.8, kommentarer, exempel 6 a, 6 c, 6 k, ikraftträdandebestämmelser.
- **BFN, K3 vägledning**, consolidated version for räkenskapsår beginning after 2025-12-31 (BFNAR 2012:1 as amended by **BFNAR 2025:3** and **BFNAR 2025:4**), `bfn.se/wp-content/uploads/vl12-1-k3-kons20251215.pdf` — punkterna 18.7, 21.4, 21.6, 21.9, 21.12, 23.2, 23.3, 23.7, 23.8, 23.13–23.17, 23.26, 23.27, 23.28, 26.2, 30.1, 30.3–30.7, kommentarer, ikraftträdandebestämmelser.
- **BFN, vägledning Bokföring** (**BFNAR 2013:2**, punkt 2.5 as amended by **BFNAR 2024:1**), `bfn.se/wp-content/uploads/vl13-2-bokforing.pdf` — punkterna 2.4, 2.5, 2.9, 2.10, 2.11, 6.1.
- **ML (2023:200)**, rkrattsbaser.gov.se and lagen.nu — 2 kap 26–27 §§, 5 kap 40–44 §§, 7 kap 4 §, 7 kap 7 §, 7 kap 14 §, 8 kap 21–23 §§, 17 kap 29 §.
- **ÅRL (1995:1554)**, riksdagen.se — 4 kap 13 §, bilaga 1.
- **BFL (1999:1078)**, lagen.nu — 5 kap 4 §, 5 kap 6 §, 5 kap 7 §, 5 kap 11 §.
- **BAS 2026 v1.1**, `bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.xlsx` and `bas.se/wp-content/uploads/2026/01/Kontoplansforandringar_2026.xlsx` — every account number and name above, the 1580 → 1686 change, and confirmation that kontogrupp 30–34 is unchanged from BAS 2025.

Not reached: Skatteverket's rättslig vägledning (www4.skatteverket.se) rejects automated requests; the points that would benefit from it are flagged "Osäkert" inline.
