# Entreprenad och projekt

Industry reference for revenue, cost and balance-sheet handling of construction contracts (entreprenader) in a Swedish byggföretag or hantverksföretag.

The general project-accounting method — successiv vinstavräkning, färdigställandegrad, WIP accounts, SIE dimensions, project profitability — lives in `swedish-project-accounting`. Payroll amounts (traktamente, milersättning, OB) live in `swedish-payroll`. Personalliggare mechanics live alongside `swedish-cash-register`. This file covers only what is specific to construction contracts.

**Legal position stated: as in force 2026-09-17.** Figures are labelled with the year they belong to. Statutes were read in consolidated form on 2026-09-17 (IL 1999:1229 consolidated to SFS 2026:1393, ML 2023:200 to SFS 2026:1025, SFL 2011:1244 as cached same day). K2 and K3 were read in BFN's consolidated vägledningar (K2 updated 2025-06-16, K3 updated 2025-12-15). Accounts are verified against the official BAS 2026 kontoplan v 1.1. See [Sources](#13-sources).

## Table of contents

1. [Contract types in practice](#1-contract-types-in-practice)
2. [Revenue recognition: the construction specifics](#2-revenue-recognition-the-construction-specifics)
3. [The tax rule for pågående arbeten](#3-the-tax-rule-for-pågående-arbeten)
4. [ÄTA-arbeten](#4-äta-arbeten)
5. [Innehållna medel and garantitid](#5-innehållna-medel-and-garantitid)
6. [Garantiavsättningar](#6-garantiavsättningar)
7. [Förskott and a conto](#7-förskott-and-a-conto)
8. [Egen regi and uttagsbeskattning](#8-egen-regi-and-uttagsbeskattning)
9. [Industry costs and BAS 2026](#9-industry-costs-and-bas-2026)
10. [ID06 and personalliggare](#10-id06-and-personalliggare)
11. [Ask the user](#11-ask-the-user)
12. [Error patterns](#12-error-patterns)
13. [Sources](#13-sources)

---

## 1. Contract types in practice

### Fast pris versus löpande räkning

The only statutory definition that matters for accounting and tax is **IL 17 kap. 25 §**: work is on löpande räkning if the compensation is *"uteslutande eller så gott som uteslutande"* based on a pre-agreed fee per unit of time, the actual time spent and any actual outlays. **Everything else is fast pris.** K3 23.11–23.12 and K2 6.10/6.12 use the same construction.

Consequences of getting this wrong are large, so test it on the contract wording, not on what the job is called:

| Contract feature | Classification |
|------|------|
| Hourly rate × hours + material at cost | Löpande räkning |
| Hourly rate with a **takpris** or a guaranteed maximum | Fast pris — the compensation is no longer *uteslutande* time-based |
| Fixed sum per m² or per apartment | Fast pris |
| Hourly rate plus a fixed "etableringsavgift" of trivial size | Still löpande räkning if the fixed element is insignificant |
| Riktpris with incitamentsdelning | Fast pris |

### Totalentreprenad versus utförandeentreprenad

This is a division of **design responsibility**, not a pricing model. Either can be priced fast pris or löpande räkning.

| | Utförandeentreprenad | Totalentreprenad |
|------|------|------|
| Who designs | Beställaren (or its consultants) | Entreprenören |
| What the entreprenör owes | To build according to the beställare's handlingar | A finished function |
| Typical risk carried | Quantities and method | Design, function, quantities and method |
| Project cost pattern | Projektering sits with the beställare | Projektering sits in the entreprenör's own cost base and must be captured on the project |
| Common standard agreement | AB 04 | ABT 06 |

For bookkeeping, the practical difference is that in a totalentreprenad the entreprenör's own projektering, konstruktion and ritningar are **uppdragsutgifter on the project** (K3 23.20 a), not general overhead. Tag them to the project dimension from day one; they are also part of the anskaffningsvärde under IL 17 kap. 27 § and of the uttag base if the work is in egen regi.

### What AB 04 / ABT 06 do to the timing of revenue and cost

The standard agreements are not law and are not quoted here. Commercially they structure five things that drive the accounting:

1. **Betalningsplan.** Payment follows an agreed plan or monthly a conto based on work performed, not the transfer of any asset. The invoice therefore drives the VAT (ML 7 kap. 24 §) while the accounting revenue follows the method chosen under K2/K3 — the two are deliberately decoupled.
2. **ÄTA-procedure.** Changes must be ordered and priced through a defined route. Work performed outside that route is contested, which is why unapproved ÄTA is not revenue. See section 4.
3. **Besiktning.** Slutbesiktning is the event that normally marks approval of the entreprenad. Skatteverket uses "beställaren har godkänt entreprenaden" — usually godkänd slutbesiktning, or the building being taken into use — as the point when a bygg- och anläggningstjänst is supplied for VAT purposes.
4. **Innehållna medel.** The beställare retains part of the contract sum until after besiktning and, for a further period, as security during the garantitid. See section 5.
5. **Garantitid and ansvarstid.** After approval the entreprenör carries a defined responsibility for defects for a contractual period, and a longer period of liability for essential defects. This is what creates the legal åtagande behind a garantiavsättning.

*Osäkert:* the retention percentage, the length of garantitiden and ansvarstiden, and the ÄTA notification deadlines differ between AB 04, ABT 06 and any negotiated deviation in the specific contract. They are contractual, not statutory, and were not verified against a primary source here. **Read the contract** before booking a retention or sizing a warranty provision; do not assume standard figures.

---

## 2. Revenue recognition: the construction specifics

Read `swedish-project-accounting` for the method, the WIP accounts (**1470**, **1471**, **1478**, **1620**, **2450**, **4970**) and the netting rules. What follows is only what construction adds.

### The framework in one table

| | K2 (BFNAR 2016:10) | K3 (BFNAR 2012:1) |
|------|------|------|
| Löpande räkning | Revenue as work is performed (6.13); invoicing does not govern | Revenue as work is performed and material delivered or consumed (23.17); "faktureringstidpunkten styr inte" |
| Fast pris, main rule | Huvudregeln — successiv vinstavräkning (6.16) | 23.18/23.21 — successiv vinstavräkning on färdigställandegrad |
| Fast pris, alternative | Alternativregeln — revenue when the work is *väsentligen fullgjort* (6.22) | **23.31**: färdigställandemetoden permitted **in juridisk person only**, and only for the industries in IL 17 kap. 23 § and contracts covered by IL 17 kap. 27 § |
| Consistency requirement | Same method for **all** fixed-price contracts; switching to huvudregeln is free, back only with särskilda skäl (6.15) | 23.31 applies only if **all** contracts covered by IL 17 kap. 27 § are treated the same way |
| Loss contracts | Probable loss reduces the justeringspost, whether or not the work has started (6.23) | Probable loss expensed immediately, whether or not the work has started (23.24) |
| Cost elements in the capitalised amount | Material, lön and arbetsgivaravgifter for producing staff, hired personnel, directly attributable costs; a reasonable share of indirect costs may be included (6.23 with 12.10 and ÅRL 4 kap. 3 § tredje stycket) | Directly attributable costs, allocable general uppdragsutgifter, and other costs chargeable to the beställare under the contract (23.20) |

Both K2 6.23 and the tax rule allow the capitalised amount to be taken up at **97 %** of anskaffningsvärdet for entreprenaduppdrag — a 3 % schabloninkurans. K2's comment is explicit that this does **not** apply to tjänsteuppdrag, only to entreprenaduppdrag.

Both K2 (BFNAR 2025:2) and K3 (BFNAR 2025:3) were amended on 2025-06-16 with first application to **räkenskapsår beginning after 2025-12-31** — that is, calendar-year 2026 onwards. K3 23.21 carries the BFNAR 2025:3 marker. K2 6.24's per-contract gross presentation requirement carries the BFNAR 2025:2 marker.

### "Väsentligen fullgjort" when there are anmärkningar in the besiktningsprotokoll

The single most common construction question under the alternativregel. Both BFN texts answer it the same way:

- The contract governs. If it states that the uppdrag is complete when certain conditions are met, recognise at that point.
- Where the contract is silent, the work is väsentligen fullgjort when the uppdragsgivare has approved it; failing that, when the work has been handed over and can be used as intended, and approval is probable.
- **Minor remarks in a slutbesiktningsprotokoll do not defer recognition.** K2 6.22 comment: "Resultatavräkning ska ändå ske även om mindre justeringar kvarstår. Kostnader för de tillkommande arbetena ska företaget reservera för." K3 23.31 comment is the same, adding that the cost of the tillkommande arbeten is reported as a **skuld**.

So: recognise the contract, and book the cost of clearing the punch list as an upplupen kostnad (**2990** Övriga upplupna kostnader och förutbetalda intäkter), not as a reason to defer the whole project.

---

## 3. The tax rule for pågående arbeten

**IL 17 kap. 23–32 §§.** These apply to pågående arbeten in **byggnads-, anläggnings-, hantverks- eller konsultrörelse** (17 kap. 23 §) — which covers essentially every company in this industry.

| § | Rule | Effect for a byggföretag |
|---|------|------|
| **23 §** | The accounting treatment of pågående arbeten is followed for tax purposes, unless it conflicts with 24–32 §§ | Materiellt samband: the K2/K3 choice drives the tax outcome |
| **24 §** | Income is computed per 26, 31, 32 §§ for löpande räkning and per 27–32 §§ for fast pris. An enskild näringsidkare with förenklat årsbokslut (BFL 6 kap. 6 §) may apply the löpande-räkning rules also to fixed-price work | A one-person hantverksfirma on förenklat årsbokslut can use the simpler regime for all work |
| **25 §** | Definition of löpande räkning | See section 1 |
| **26 §** | Value of pågående arbeten on löpande räkning **need not** be taken up as an asset; instead the amounts **invoiced** during the year are taxed | Upparbetad ej fakturerad intäkt on **1620** for T&M work is a book/tax difference, adjusted in INK2 |
| **27 §** | Fixed-price work not yet slutredovisat may not be valued below the lower of anskaffningsvärde and nettoförsäljningsvärde. **Andra stycket: for byggnads-, anläggnings- och hantverksrörelse the pågående arbeten may be taken up at as low as 97 % of the aggregate anskaffningsvärde** | The **97 % rule**. Note it is *sammanlagda* — a portfolio-level 3 % reduction, not per contract. Lydelse: Lag (2003:1102) |
| **28 §** | Payments received for work under 27 § are **not** income but a **skuld** to the beställare | A conto on a fixed-price job is a liability, not revenue |
| **29 §** | The value of work performed personally by the skattskyldige, their spouse, or children under 16 is **excluded** from anskaffningsvärdet. For a handelsbolag, delägares' own work is excluded | Decisive for enskild firma and HB: the owner's own hours are never capitalised in WIP |
| **30 §** | Fixed-price work for a related party may be re-valued at a reasonable amount where 27–29 §§ have been used for an obehörig skatteförmån | Intra-group entreprenader |
| **31 §** | If the company to a significant extent has failed to slutredovisa or invoice amounts that could have been under god redovisningssed, those amounts are taxed anyway | Cannot defer tax by simply not invoicing a finished job |
| **32 §** | If the taxpayer shows that the amount to be taxed exceeds what god redovisningssed permits, the income is adjusted downwards to a reasonable extent | Safety valve |

Note the 97 % in 17 kap. 27 § andra stycket is a **different rule** from the 97 % lager rule in IL 17 kap. 4 §; do not conflate them.

The corresponding INK2 adjustment logic and the deferred-tax treatment are in `swedish-project-accounting`.

---

## 4. ÄTA-arbeten

ÄTA = **ändrings-, tilläggs- och avgående arbeten**: work added to, removed from or changed in the contracted scope after signature. In practice it is where a construction project's margin is made or lost, and where the bookkeeping most often runs ahead of reality.

### The recognition rule

**K3 23.19** defines uppdragsinkomsten as (a) the originally agreed compensation, and (b) *"ersättningar till följd av ändringar i omfattningen av uppdraget, anspråk och incitamentsersättningar i den utsträckning det är sannolikt att justeringarna kommer att resultera i inkomster som kan mätas på ett tillförlitligt sätt."*

Two cumulative conditions: **probable**, and **reliably measurable**. Both must be met before an ÄTA enters uppdragsinkomsten.

### Why unapproved ÄTA is not revenue yet

- Under the standard agreements, a change only becomes a priced entitlement once it has been ordered and agreed through the contractual ÄTA route. Work performed on a site foreman's verbal say-so, outside that route, is an **anspråk** — a claim — not an agreed price.
- An anspråk fails the "probable" test until the beställare has accepted it, or until there is other objective evidence (a signed ÄTA-order, an agreed price list applied to a documented quantity, a settled negotiation).
- Booking it early inflates **1620** and revenue, creates tax on income that may never arrive (IL 17 kap. 23 § follows the accounts), and leaves a receivable that must later be written off.

| ÄTA status | Revenue? | Cost? | Booking |
|------|------|------|------|
| Signed ÄTA-order with agreed price | Yes | Yes | Normal — include in uppdragsinkomsten and in färdigställandegrad |
| Ordered, price not yet agreed but a price mechanism exists in the contract | Yes, at the reliably measurable amount | Yes | Include at the measurable amount; document the basis |
| Performed, disputed by the beställare | **No** | **Yes** | Cost hits the project; no matching revenue. Margin on the project falls until settled |
| Performed, not yet raised with the beställare | **No** | **Yes** | Same as above, plus a process problem — flag it |
| Settled after year-end but before the annual accounts are finished | Consider as information about conditions at balansdagen | | Treat as a value-affecting event if it evidences what was probable at the balance date |

Under the **alternativregel** (K2 6.22 / K3 23.31) the question is narrower: no revenue is recognised on the contract at all until it is väsentligen fullgjort, so ÄTA costs simply accumulate in the capitalised amount. The 97 % and loss-contract rules still apply — a contract that will make a loss because of unpriced ÄTA must have the loss taken immediately (K2 6.23, K3 23.24).

**Always ask** before period close: *"Is there any performed ÄTA that is not yet approved, and how much cost sits on the project for it?"*

---

## 5. Innehållna medel and garantitid

### What it is

The beställare withholds part of each a conto or of the final invoice as security — commonly split into an amount released at godkänd slutbesiktning and an amount held through the garantitid. The full contract sum is invoiced; only the payment is deferred.

### VAT is not deferred

This is the point most often got wrong. **The retention does not affect VAT.** Under **ML 7 kap. 24 §** output VAT is reported for the period the invoice was issued, on the **full invoiced amount**. A retention is a payment term, not a price reduction, so there is no nedsättning av beskattningsunderlaget and no basis for a kreditfaktura.

The company therefore funds the VAT on money it will not see for a year or more. Flag this in cash-flow advice on large entreprenader.

### Booking

| Event | Entry |
|------|------|
| Final invoice issued, 1 000 000 + moms, 50 000 retained | Debit **1511** Kundfordringar 1 250 000 / Credit **3001** 1 000 000, Credit **2611** 250 000 |
| Reclassify the retained amount | Debit a dedicated *Innehållna medel* account — a free underkonto in the **1510** series, or **1689** Övriga kortfristiga fordringar — 50 000 / Credit **1511** 50 000 |
| Retention released and paid | Debit **1930** 50 000 / Credit the retention account 50 000 |
| Beställaren uses the retention to cover a defect it had rectified | Debit **6360** Garantikostnader (or reverse against **2220**) / Credit the retention account |

Keep the retention **separate from ordinary kundfordringar** so that the aged receivable list and any kundförlust assessment are not polluted by amounts that are not overdue at all. Where release lies more than twelve months after the balance date, present it as a långfristig fordran.

### When it becomes a receivable

The receivable exists from the moment the invoice is issued — the retention is a deferred payment term on an existing claim, not a contingent right. What changes over the garantitid is the **risk of set-off**, not the existence of the fordran. If it becomes doubtful (the beställare asserts defects exceeding the retention, or is insolvent), treat it as any other doubtful receivable: **6350/6351** and, for VAT, the kundförlust rules in `swedish-vat`.

*Osäkert:* whether a given retention is released at slutbesiktning, at the end of garantitiden, or in tranches is purely contractual and was not verified against a primary source. Read the contract.

---

## 6. Garantiavsättningar

### When a provision is required

The trigger is an **åtagande** — the contractual responsibility for defects during the garantitid — not the mere possibility of future rework.

**K2 16.2** requires a provision only when all of its conditions a–c are met; a legal åtagande expected to lead to an outflow is a **skuld**, while one where an outflow is only *sannolikt* is an **avsättning**. K2's commentary names a garanti on delivered work as the textbook example of a legal åtagande arising from a contract. A decision about future maintenance or investment is never an åtagande (K2 16.3).

**K3 21.4** requires all three of: an existing legal or informal förpliktelse on the balance date from a past event; probable outflow; and a reliable estimate. K3 21.5 defines a legal förpliktelse as arising from contract, legislation or other legal ground; **21.6** extends it to informal förpliktelser created by established practice or published undertakings — relevant where a company routinely fixes defects beyond what the contract requires.

### K2 versus K3 measurement

| | K2 | K3 |
|------|------|------|
| Basis | Best estimate; for garantiåtaganden, computed from **previous years' actual costs** for the same type of undertaking. Where no history exists (new company, changed direction), företagsekonomiskt motiverade riktlinjer for the industry may be used (the allmänna rådet in K2 16.7 itself) | Best estimate of the expenditure required to settle the förpliktelse |
| Discounting | Not required | **21.9**: discount to present value **if the timing effect is material**, at a pre-tax rate reflecting the time value of money and the risks |
| Tax-based shortcut | **16.8**: the provision **may** be computed per IL if it can be assumed the result does not deviate by more than **20 %** from the 16.7 best estimate | No equivalent shortcut |

K2 16.7's table was amended by **BFNAR 2025:2**, applicable to räkenskapsår beginning after 2025-12-31.

### Tax treatment

**IL 16 kap. 3–5 §§:**

- **3 §**: framtida garantiutgifter are deducted per 4 or 5 § with the amount **set aside in the accounts** to cover the risk from garantiåtagandena at the end of the beskattningsår. **The deduction must be reversed the following beskattningsår.** The provision is therefore re-computed and re-deducted annually, gross.
- **4 § (schablonregeln)**: the deduction may not exceed the year's actual costs arising from garantiåtaganden, excluding the change in the provision itself. If the garantitid is **shorter than two years**, the deduction is capped at as many twenty-fourths of those costs as the garantitid is in months (part months dropped). Adjusted pro rata for a long or short räkenskapsår.
- **5 § (utredningsregeln)**: a larger deduction must be given where clearly motivated because the business is newly started, the garantiåtaganden concern one or a few very large tillverkningsobjekt or arbeten, the scope of garantiåtaganden increased significantly during the year, **a significant part of the garantiåtaganden concerns a period considerably longer than two years**, or similar grounds. **A single large entreprenad with a long garantitid is precisely the case 5 § exists for.**

### Accounts and entry

| Account | BAS 2026 name |
|------|------|
| **2220** | Avsättningar för garantier |
| **6360** | Garantikostnader |

Year 1, provision of 400 000 recognised:

| Account | Debit | Credit |
|---|---|---|
| **6360** Garantikostnader | 400 000 | |
| **2220** Avsättningar för garantier | | 400 000 |

Year 2: reverse the whole provision (Debit **2220** / Credit **6360** 400 000), book the year's actual garantiarbeten as they occur, and recognise a newly computed provision at year end. This mirrors the tax reversal in IL 16 kap. 3 § and keeps book and tax aligned.

---

## 7. Förskott and a conto

### VAT timing

Construction has its own rule, and it overrides the ordinary advance-payment rules for a company on faktureringsmetoden:

- **ML 7 kap. 8 §**: for bygg- och anläggningstjänster and goods supplied in connection with them, the beskattningsgrundande händelse arises **when the invoice is issued**; if no invoice has been issued when payment is received, or the invoice is issued later than the ML 17 kap. 16 § deadline, the ordinary rules in 7 kap. 4 or 7 § apply.
- **ML 7 kap. 24 §**: output VAT is reported for the period **the invoice was issued**; for **förskott or a conto received without an invoice**, for the period the payment was received; and at the latest for the period covering the **second calendar month after the month of supply**.
- **ML 17 kap. 16 §**: the invoice must be issued no later than the end of the second calendar month after the month of supply. Skatteverket confirms an invoice must also be issued for förskotts- and a conto-betalningar, and to private persons.

So the practical rule: **invoice the a conto and the VAT follows the invoice date.** Take an uninvoiced payment and the VAT falls due in the month of receipt. There is no way to sit on a received advance without VAT.

On **bokslutsmetoden** the ordinary cash rules apply instead.

### Accounting and tax

For **fixed-price** work, **IL 17 kap. 28 §** is explicit: amounts received for such work are **not** income but a **skuld** to the beställare. Under the alternativregel this matches the accounting.

| Account | BAS 2026 name | Use |
|------|------|------|
| **2420** | Förskott från kunder | Payment received before any invoicing or performance |
| **2450** | Fakturerad men ej upparbetad intäkt | Invoiced ahead of the work performed under successiv vinstavräkning |
| **1478** | Pågående arbeten, fakturering | Invoiced amounts on contracts under the alternativregel |
| **1620** | Upparbetad men ej fakturerad intäkt | Work performed ahead of invoicing |

A conto received of 500 000 + moms 125 000 on a fixed-price contract under the alternativregel:

| Account | Debit | Credit |
|---|---|---|
| **1511** Kundfordringar | 625 000 | |
| **1478** Pågående arbeten, fakturering | | 500 000 |
| **2611** Utgående moms på försäljning inom Sverige, 25 % | | 125 000 |

Under successiv vinstavräkning the credit goes to revenue and the excess over upparbetat is reclassified to **2450** at period close. Netting rules per contract (K2 6.24, K3 23.27) are in `swedish-project-accounting`.

---

## 8. Egen regi and uttagsbeskattning

### What egen regi means

Byggverksamhet where there is **no entreprenadavtal**: erecting buildings on your own land or land held with nyttjanderätt or tomträtt; rebuilding or renovating a lägenhet you hold with hyresrätt or bostadsrätt; and repairs, rebuilds and maintenance on buildings you use in your own operations (driftfastigheter) or let out.

Because there is no external customer, there is no VAT-bearing supply — so ML imposes an **uttag** instead.

### Uttag av tjänster i byggnadsrörelse — ML 5 kap. 32 §

A beskattningsbar person **in a byggnadsrörelse** who performs or acquires (1) bygg- och anläggningsarbeten, including repairs and maintenance, or (2) ritning, projektering, konstruktion or similar services, and applies them to its **own fastighet** or to a lägenhet it holds with hyresrätt or bostadsrätt, makes an uttag — but only if **all** of:

1. the person **also supplies services to others** (byggentreprenader),
2. the fastighet or lägenhet is a **lagertillgång** in the byggnadsrörelse under IL, and
3. the services relate to a part of the property **not used in an activity giving avdragsrätt**.

Third stycke extends the rule to property that is another asset in the byggnadsrörelse than lagertillgång, if conditions 1 and 3 are met — but there it applies **only to services the person performs itself** ("i de fall den beskattningsbara personen **utför** tjänsterna"). Purchased byggtjänster on such a property are not uttagspliktiga; Skatteverket: uttagsbeskattning sker då "endast för egenproducerade byggtjänster".

Skatteverket's clarifications: a **byggnadsrörelse** means you build buildings and anläggningar; **hantverksrörelser** (VVS, måleri) and **anläggningsrörelser** (markarbeten, sprängning) are **not** byggnadsrörelser. Uttagsbeskattning only becomes relevant where the property is used in a **non-VAT-liable** activity. Where the property is a lagertillgång and uttagsbeskattning applies, input VAT on both material and purchased byggtjänster is deductible under the ordinary rules. If there is no utåtriktad byggverksamhet, or it is too small a part of the whole, the fastighetsförvaltning rules below apply instead.

### Uttag på fastighetsområdet — ML 5 kap. 33–35 §§

For a **fastighetsägare** (33 §) or a **hyresgäst/bostadsrättshavare** (34 §) performing bygg- och anläggningsarbeten, ritning/projektering, or — for a fastighetsägare — lokalstädning, fönsterputsning, renhållning och annan fastighetsskötsel on its own property, an uttag arises only if all of:

1. the property is an asset in the owner's ekonomiska verksamhet,
2. there would have been **no avdragsrätt** had the services been bought in, and
3. the **nedlagda lönekostnaderna** for the services during the beskattningsår exceed **300 000 SEK**, including taxes and charges based on those wage costs.

**35 §**: where someone is both fastighetsägare and hyresgäst/bostadsrättshavare, the 300 000 limit applies to the **combined** wage cost.

### Beskattningsunderlag

**ML 8 kap. 6 §** (general uttag of services): the cost of performing the service, meaning the share of the business's fixed and running costs attributable to it.

**ML 8 kap. 8 §** (the 5 kap. 32–34 § cases): the beskattningsunderlag is

1. **de nedlagda kostnaderna**,
2. **beräknad ränta** on capital other than borrowed capital invested in the varulager or non-current assets used for the services, and
3. **the value of work performed personally** by the persons in 5 kap. 32, 33 or 34 §.

**ML 8 kap. 9 §**: for the 5 kap. 33–34 § cases the fastighetsägare or hyresgäst may instead **request** that the beskattningsunderlag be the **lönekostnaderna** including taxes and charges on them. Note the consequence in **ML 13 kap. 16 §**: no deduction is allowed for input VAT on costs relating to such uttag where the beskattningsunderlag was computed under 8 kap. 9 §.

Skatteverket's operational breakdown of "nedlagda kostnader": **direct** costs — material, wages and lönebikostnader for staff on site, mätningskostnader, subcontractors — and **indirect** costs — administrative salaries, own transport, tools, insurance. Beräknad ränta may be set at **0,5 % of the direct and indirect costs** where it cannot easily be computed; interest on byggnadskreditiv is excluded. Own personally performed work is valued at what paid staff would have cost, and is only relevant for enskild firma, enkelt bolag or handelsbolag delägare — in an aktiebolag the owner's work is already in the wage costs. Costs normally treated as **utlägg** in an entreprenad — markanskaffning, inteckning, fastighetsbildning, lagfart — are excluded.

Rate: **25 %** of the beskattningsunderlag.

### Timing

**ML 7 kap. 23 §**: where the uttag concerns a service that **to the greater part** relates to ny-, till- eller ombyggnad of the person's own fastighet or lägenhet, the output VAT is reported at the latest for the period in which the property, or the relevant part, **could be taken into use**. Where the services are not mainly ny-, till- eller ombyggnad, report as the uttag occurs, period by period (ML 7 kap. 22 §).

### Egen regi turning into entreprenad

Common in nyproduktion for sale, notably when a property is transferred to a newly formed bostadsrättsförening while the föreningen and the byggföretag simultaneously sign an entreprenadavtal. Skatteverket's treatment:

1. Signing the överlåtelseavtal makes it a **fastighetsförsäljning**; egen-regi-byggande ceases at that moment.
2. **Uttagsbeskatta** the services performed on the property up to the sale, reported in the period the sale occurs.
3. After the sale, the company performs **byggtjänster to the buyer** and invoices **with VAT** — or under omvänd betalningsskyldighet if the buyer meets the ML 16 kap. 13 § test (see `omvand-byggmoms-och-rot.md`).

### Why the boundary matters

Getting egen regi versus entreprenad wrong misstates three things at once: **VAT** (uttag at 25 % on a cost base versus VAT on a contract price, or no VAT at all under reverse charge), **income tax** (a lagerfastighet is stock, so IL 17 kap. applies rather than the anläggningstillgång rules — see `swedish-asset-accounting`), and **revenue recognition** (egen regi generates no uppdragsinkomst at all until the property is sold). A misclassified project can be wrong for several years before anyone notices.

---

## 9. Industry costs and BAS 2026

BAS has no dedicated construction accounts beyond **3231** and the reverse-charge purchase accounts. The mapping below uses the official BAS 2026 accounts; add underkonton per project or per cost type rather than inventing numbers.

| Cost | BAS 2026 account | Name |
|------|------|------|
| Material bought in Sweden (VAT charged) | **4310** | Inköp av råvaror och material i Sverige |
| Material under omvänd betalningsskyldighet | **4415** | Inköp av råvaror och material i Sverige, omvänd betalningsskyldighet, 25 % moms |
| Underentreprenad, VAT charged | **4610** | Inköp av tjänster och underentreprenader |
| Underentreprenad, omvänd betalningsskyldighet | **4425** | Inköp av tjänster i Sverige, omvänd betalningsskyldighet, 25 % moms |
| Hire of maskiner (grävmaskin, kran, lift) | **5210** | Hyra av maskiner och andra tekniska anläggningar, ej datorer och fordon |
| Hire of verktyg, byggställningar, byggbodar | **5220** | Hyra av inventarier och verktyg, ej datorer och fordon |
| Site lokalhyra, etableringsyta | **5010** / **5090** | Lokalhyra / Övriga lokalkostnader |
| Byggstädning and container/renhållning on site | **5060** | Städning och renhållning |
| Own arbetsmaskiner: fuel | **5641** | Drivmedel arbetsmaskiner (**new in BAS 2026**) |
| Own arbetsmaskiner: insurance and tax | **5642** | Försäkring och skatt arbetsmaskiner (**new in BAS 2026**) |
| Own arbetsmaskiner: repairs | **5643** | Reparation och underhåll arbetsmaskiner (**new in BAS 2026**) |
| Leasing of arbetsmaskiner | **5645** | Leasing arbetsmaskiner (**new in BAS 2026**) |
| Small tools expensed | **5410** / **5411** / **5412** | Förbrukningsinventarier (and the >1 year / ≤1 year splits) |
| Consumables (skruv, spik, tejp) | **5460** | Förbrukningsmaterial |
| Arbetskläder and skyddsutrustning | **5480** | Arbetskläder och skyddsmaterial |
| Travel tickets for travelling staff | **5810** | Biljetter |
| Kost och logi on the road | **5831** / **5832** | Kost och logi i Sverige / i utlandet |
| Skattefritt traktamente | **7321** | Skattefria traktamenten, Sverige |
| Skattepliktigt traktamente | **7322** | Skattepliktiga traktamenten, Sverige |
| Milersättning, skattefri | **7331** | Skattefria bilersättningar |
| Företagsförsäkring, entreprenadförsäkring | **6310** | Företagsförsäkringar |
| Owned maskiner, capitalised | **1210**/**1211**, **1216** | Maskiner och andra tekniska anläggningar; **Arbetsfordon** (**new in BAS 2026**) |
| Owned verktyg och inventarier, capitalised | **1220**/**1221** | Inventarier, verktyg och installationer |

**BAS 2026 class 4 restructure — read this before mapping a legacy chart.** 4000–4099 is now *handelsvaror* (goods for resale) and **4010** means *Inköp av handelsvaror i Sverige*. Construction material belongs in the new **4300/4310** group, which did not exist before BAS 2026. 4415–4417 and 4425–4427 were renamed in BAS 2026. Charts that map "material" to 4010 must be remapped.

**Traktamente, milersättning, kost- och logiförmån and OB amounts are not repeated here — use `swedish-payroll`.** Construction only adds the fact pattern: travelling fitters with a stationary place of work at the employer's premises, daily or weekly travel to sites, and free lodging in a byggbod or hotel. Whether a site is a *tjänsteställe* decides everything downstream, so establish it per employee.

**Arbetskläder:** skyddskläder and work clothes that are not suitable for private use are deductible and tax-free to the employee; ordinary clothing is not. Book on **5480** only what genuinely qualifies; route the rest through payroll as a förmån per `swedish-payroll`.

**Byggbodar and ställningar** are not fastighet (Skatteverket names a *tillfällig manskapsbod* as an example of something that is not fastighet). Hiring them in is an ordinary VAT-charged rental on **5220**, not a byggtjänst — and work performed *on* a bod is likewise not covered by omvänd byggmoms.

Capitalisation versus expensing of tools and machines follows the ordinary rules in `swedish-asset-accounting` (förbrukningsinventarier, half a prisbasbelopp).

---

## 10. ID06 and personalliggare

Statutory rules are in **SFL (2011:1244)**; the operational mechanics of registering and retaining liggare are covered alongside `swedish-cash-register`.

| Provision | Rule |
|------|------|
| **SFL 39 kap. 2 §** | *byggverksamhet*: näringsverksamhet concerning om-, till- och nybyggnadsarbeten, reparations- och underhållsarbeten, rivning av byggnadsverk, and other business carried on in support of such activity not already covered by 11 §. *byggarbetsplats*: a place where byggverksamhet is carried on |
| **SFL 39 kap. 11 a §** | A person carrying on byggverksamhet at a byggarbetsplats where the byggherre has provided equipment under 11 b § must keep an **electronic personalliggare** and continuously document identification data for the business and for everyone active in it. Persons who only briefly load or unload material are excluded |
| **SFL 39 kap. 11 b §** | The **byggherre** must provide the equipment. Not required (1) until the total cost of the byggverksamhet at the site can be assumed to exceed **four prisbasbelopp**, or (2) for a byggherre who is a physical person not acting in näringsverksamhet |
| **SFL 39 kap. 11 c §** | The byggherre's obligations may be transferred **in writing** to a näringsidkare who has been given independent responsibility for the work |
| **SFL 39 kap. 12 §** | The byggherre must keep the liggare available to Skatteverket at the site; each contractor must keep its own liggare available to Skatteverket **and to the byggherre** |
| **SFL 7 kap. 2 a §** | Whoever must provide the equipment must **register the byggarbetsplats with Skatteverket before the work starts**, stating when the work begins and where it will be carried on |
| **SFL 50 kap. 3–4 §§** | Kontrollavgift: **12 500 SEK per kontrolltillfälle**, plus **2 500 SEK per person** present at the check and not documented in an available liggare. A repeat within one year of a previous decision raises the first amount to **25 000 SEK**. Failure to register the site under 7 kap. 2 a § is **25 000 SEK**. No avgift where the breach is covered by a vitesföreläggande (50 kap. 5 §), and the defect must be remedied within reasonable time (50 kap. 6 §) |

**Four prisbasbelopp:** prisbasbeloppet for **2026 is 59 200 SEK** (2025: 58 800), so the threshold is **236 800 SEK for 2026** (235 200 for 2025). Recompute it every year.

**ID06 is not law.** It is a private industry system (identity cards, competence registers, electronic liggare) run by the construction sector, widely required by beställare in contracts. Using ID06 is one way to satisfy the SFL personalliggare obligation, not a legal requirement in itself, and ID06 fees are an ordinary external cost (**6990** Övriga externa kostnader, or **6980** Föreningsavgifter where the charge is a membership fee). Do not tell a user that ID06 is legally mandated — tell them the personalliggare is, and that their contract may require ID06 on top.

---

## 11. Ask the user

1. **"Is this contract fast pris or löpande räkning — and is there a takpris?"** A ceiling makes it fast pris (IL 17 kap. 25 §).
2. **"Which method does the company use for all fixed-price contracts?"** Huvudregeln or alternativregeln; the choice must be uniform (K2 6.15, K3 23.31).
3. **"Has slutbesiktning taken place, and what does the protokoll say?"** Minor remarks do not defer recognition; reserve for the punch list instead.
4. **"Is there performed ÄTA that is not yet approved or priced?"** Cost without revenue; needed before any period close.
5. **"How much is retained, and when is it released?"** Retention is contractual; VAT is not deferred.
6. **"What is the garantitid on this contract, and what did garantiarbeten actually cost the last few years?"** Needed for both the K2 16.7 estimate and the IL 16 kap. 4 § cap. A garantitid under two years triggers the twenty-fourths rule.
7. **"Is this a byggnadsrörelse, and is the property a lagertillgång?"** Decides ML 5 kap. 32 § versus 33 §.
8. **"Is any part of the property used in a non-VAT-liable activity?"** Without that, no uttagsbeskattning.
9. **"Did the company perform work on its own property with own staff, and what were the wage costs?"** The 300 000 SEK threshold in ML 5 kap. 33–34 §§.
10. **"Where is each employee's tjänsteställe?"** Decides traktamente and resor — then use `swedish-payroll`.
11. **"Who is byggherre on this site, and has the site been registered with Skatteverket?"** SFL 7 kap. 2 a §; the obligation can have been transferred in writing under 39 kap. 11 c §.
12. **"Is the company enskild firma or handelsbolag?"** The owner's own hours are excluded from WIP anskaffningsvärde (IL 17 kap. 29 §).

---

## 12. Error patterns

| Error | Consequence |
|------|------|
| Treating a fixed-price contract with a takpris as löpande räkning | Wrong recognition method and wrong tax treatment under IL 17 kap. 24–27 §§ |
| Mixing methods across fixed-price contracts | Breaches K2 6.15 / K3 23.31; the alternativregel is lost entirely |
| Deferring the whole contract because of anmärkningar in the besiktningsprotokoll | Revenue recognised a year late; reserve for the punch list instead |
| Recognising unapproved or disputed ÄTA as revenue | Inflated **1620**, tax on income that may never arrive |
| Crediting the retained amount or reducing the VAT because of innehållna medel | No basis for nedsättning; output VAT stands on the full invoice (ML 7 kap. 24 §) |
| Leaving retentions in ordinary **1511** | Aged receivables and kundförlust analysis corrupted |
| Failing to reverse the garantiavsättning the following year | Breaches IL 16 kap. 3 §; double deduction |
| Applying the schablonregel in IL 16 kap. 4 § to one large entreprenad with a long garantitid | Understates the provision; 5 § utredningsregeln is the applicable rule |
| Holding a received a conto without invoicing to postpone VAT | VAT falls due in the period of receipt (ML 7 kap. 24 §) |
| Booking a conto on fixed-price work as revenue | Breaches IL 17 kap. 28 §; it is a skuld |
| Capitalising the owner's own hours in an enskild firma's WIP | Breaches IL 17 kap. 29 § |
| Applying the 97 % rule per contract | 17 kap. 27 § andra stycket works on the **sammanlagda** anskaffningsvärde |
| Applying the 97 % rule to a tjänsteuppdrag | K2 6.23 commentary limits it to entreprenaduppdrag |
| Missing uttagsbeskattning on egen regi | Unreported output VAT plus skattetillägg |
| Posting construction material to **4010** under BAS 2026 | 4010 is now handelsvaror; use **4310** |
| Treating ID06 as the legal obligation | The statutory obligation is the personalliggare in SFL 39 kap.; ID06 is a contractual industry system |
| Starting work without registering the byggarbetsplats | Kontrollavgift 25 000 SEK (SFL 50 kap. 4 §) |

---

## 13. Sources

All sources checked **2026-09-17**.

### Statutes (consolidated text)

| Statute | Provisions used | Lydelse relied on |
|------|------|------|
| Inkomstskattelag (1999:1229) | 16 kap. 3, 4, 5 §§; 17 kap. 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33 §§ | Consolidated to SFS 2026:1393. 17 kap. 27 § andra stycket (the 97 % rule) current lydelse **Lag (2003:1102)**; 23, 26, 28, 29, 30, 31, 32 §§ **Lag (2007:1419)**; 24 § **Lag (2010:1528)**; 16 kap. 3–5 §§ **Lag (2007:1419)**. No 2026 amendment to any of them |
| Mervärdesskattelag (2023:200) | 5 kap. 32, 33, 34, 35 §§; 7 kap. 8, 22, 23, 24 §§; 8 kap. 6, 8, 9 §§; 13 kap. 16 §; 17 kap. 16 § | Consolidated to SFS 2026:1025. None of these paragraphs carries a later Lag()-marker — original 2023:200 wording, in force since 2023-07-01 |
| Skatteförfarandelag (2011:1244) | 7 kap. 2 a §; 39 kap. 2, 11 a, 11 b, 11 c, 12 §§; 50 kap. 3, 4, 5, 6 §§ | 39 kap. 2 § current lydelse **Lag (2023:208)**; 39 kap. 11 a–11 c, 12 §§ and 7 kap. 2 a § **Lag (2014:1474)**; 50 kap. 4 § **Lag (2015:769)** |

### BFN (bfn.se), consolidated vägledningar

- **K2 — Årsredovisning i mindre företag**, vägledning to BFNAR 2016:10, konsoliderad, **uppdaterad 2025-06-16**. Used: 6.10, 6.12, 6.13, 6.15, 6.16, 6.22, 6.23, 6.24, 12.10, 16.2, 16.3, 16.7, 16.8. Amending **BFNAR 2025:2** applies from 2025-06-16 and **first to räkenskapsår beginning after 2025-12-31** (i.e. FY2026), with a special rule for companies started after 2025-06-30 with a förlängt räkenskapsår ending 2026-12-31 or later.
- **K3 — Årsredovisning och koncernredovisning**, vägledning to BFNAR 2012:1, konsoliderad **2025-12-15**. Used: 21.4, 21.5, 21.6, 21.9, 23.9–23.27, 23.31. 23.21 carries the **BFNAR 2025:3** marker; BFNAR 2025:3 has the same 2025-06-16 / FY2026 application rule. **23.31 (färdigställandemetoden in juridisk person) still stands, marker BFNAR 2012:5** — it was not withdrawn.
- ÅRL (1995:1554) 4 kap. 3 § tredje stycket and 4 kap. 10 §, as reproduced in the BFN vägledningar.

### Skatteverket (skatteverket.se, read 2026-09-17)

- *Byggverksamhet* — `/foretag/moms/sarskildamomsregler/byggverksamhet.4.dfe345a107ebcc9baf80001255.html` (definition of byggverksamhet, fastighetsbegreppet, entreprenadverksamhet, utlägg, when a byggtjänst is supplied, etapper, egen regi, egen regi turning into entreprenad)
- *Uttagsbeskattning i byggverksamhet* — `.../byggverksamhet/uttagsbeskattningibyggverksamhet.4.5c1163881590be297b5969d.html` (byggnadsrörelse vs hantverks-/anläggningsrörelse, lagertillgång, requirement of utåtriktad verksamhet, the components of nedlagda kostnader, the 0,5 % ränteschablon, excluded utlägg, reporting timing)
- *Belopp och procent – inkomstår 2026* — `/foretag/skatterochavdrag/beloppochprocent/2026.106.1522bf3f19aea8075ba3294.html` (**prisbasbelopp 2026 = 59 200 SEK**; the 2025 page gives 58 800)

### BAS

- Official **BAS 2026 kontoplan, v 1.1** (bas.se) plus the official 2026-vs-2025 change file. Every account number **and** name above was matched against both. New in BAS 2026 and used here: **1212**, **1216**, **1217**, **4300/4310**, **5641–5646**, **5649**; **4010** redefined to *handelsvaror*; **4415–4417** and **4425–4427** renamed. No accounts were removed in BAS 2026.

### Osäkert

- **Skatteverkets rättsliga vägledning (www4.skatteverket.se) blocks automated fetches** ("Request Rejected"). The ställningstaganden behind the fastighetsbegrepp, *"Vad är en bygg- och anläggningstjänst?"* and the detailed uttagsbeskattning guidance could not be read directly; the statements above rest on skatteverket.se's own guidance pages and on the statutory text. A human should open the vägledning before relying on a borderline classification.
- **AB 04 and ABT 06 are not primary legal sources and were deliberately not consulted or quoted.** Retention percentages, garantitid, ansvarstid and ÄTA notification deadlines are contractual and are stated here only as mechanics, not as figures. Read the specific contract.
- The presentation of innehållna medel as a separate receivable, and the account chosen for it, is a practice recommendation derived from ÅRL's classification requirements — **BAS 2026 contains no account named for innehållna medel, and no primary source prescribes one.** The 1510 series has free underkonton (1514, 1515, 1517) and **1689** Övriga kortfristiga fordringar exists; pick one and document the choice.
- **No change to IL 17 kap., IL 16 kap. 3–5 §§, the ML uttag rules or the SFL personalliggare rules for 2027 could be confirmed from a primary source on 2026-09-17.** regeringen.se's proposition list renders through JavaScript and returned no content to an automated fetch. Prisbasbeloppet changes annually and **must** be re-checked for 2027.
