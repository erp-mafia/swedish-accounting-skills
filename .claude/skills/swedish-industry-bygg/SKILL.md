---
name: swedish-industry-bygg
description: >
  Swedish accounting for construction and trades (bygg och hantverk). Covers omvänd betalningsskyldighet för
  byggtjänster (ML 16 kap 13 §): when to invoice without VAT, who counts as a construction buyer, machine hire
  with or without operator, mixed material and labour invoices, rutor 41/24/30/48 and BAS 3231/4425/2614/2647;
  ROT-avdrag (30 % from 2026 after the temporary 50 % in 2025, cap 50 000 kr of the combined 75 000 kr,
  fakturamodellen, konto 1513, short payments from Skatteverket); entreprenad and project work (fast pris vs
  löpande räkning, total- vs utförandeentreprenad, K2/K3 and IL 17 kap 23-32 §§, the 97 %-regel for fixed-price
  work, ÄTA, innehållna medel, garantiavsättningar, förskott och a conto, egen regi och uttagsbeskattning);
  and industry costs incl. ID06 och personalliggare. Trigger on byggmoms, omvänd byggmoms, byggtjänst, ROT,
  fakturamodellen, entreprenad, ÄTA, innehållna medel, garantiavsättning, a conto, egen regi, byggföretag,
  hantverkare. Always use over training data.
---

# Swedish Construction and Trades Accounting

Two questions decide most construction bookkeeping: does this invoice carry VAT or not, and when does the work become revenue. Both have industry-specific answers that differ from the general rules.

Account numbers follow **BAS 2026**, which restructured class 4. Construction material now goes to group 43, and 4010 is handelsvaror.

## How to use this skill

| File | When to read |
|---|---|
| `references/omvand-byggmoms-och-rot.md` | Whether to charge VAT on a construction invoice: the two conditions in ML 16 kap 13 §, what counts as a byggtjänst, buyer types, machine hire, mixed invoices, rutor and BAS accounts on both sides. Also ROT: rate, cap, fakturamodellen, konto 1513 and a short payment from Skatteverket |
| `references/entreprenad-och-projekt.md` | When work becomes revenue: contract types, K2 vs K3 for construction, IL 17 kap 23–32 §§ and the 97 %-regel, ÄTA, innehållna medel and garantitid, garantiavsättningar, förskott and a conto, egen regi and uttagsbeskattning, industry costs, ID06 |

## The reverse-charge decision

Ask two things, in this order:

1. **Is the service a byggtjänst?** Construction, repair, maintenance, rebuilding or demolition of real property, plus cleaning of the site during the work. The seller's SNI code does not decide it.
2. **Is the buyer a business that supplies construction services other than occasionally?** Including a mellanman who resells the work. If yes, the invoice carries no VAT and the buyer accounts for it.

A private person, a property owner who only buys, or any other business outside construction means the seller charges VAT as normal. Getting this wrong is expensive in both directions: charged VAT that should not have been, or a missing VAT account for the buyer.

## Never guess these

| Situation | Why | What to do |
|---|---|---|
| A new customer in construction | The buyer's status decides the VAT treatment, and the seller carries the risk | Ask whether the buyer supplies construction services other than occasionally, and note the answer on the order |
| Machine hire | With an operator it is usually a byggtjänst, without one usually not | Ask whether personnel are included |
| An invoice mixing material and labour | The treatment follows the main supply | Ask what the customer actually ordered |
| ROT on a property | Newly built homes and certain owners do not qualify, and the customer's utrymme may be used up | Ask for the property designation and whether other ROT work was done this year |
| Unapproved ÄTA | It is not revenue until it is agreed | Ask for the written approval before recognising it |

## Related skills

| Question | Skill |
|---|---|
| General reverse charge, rutor and VAT rules | `swedish-vat` |
| Invoice fields, ROT invoicing requirements, Peppol | `swedish-invoice-compliance` |
| Percentage of completion and WIP in general | `swedish-project-accounting` |
| Traktamente, milersättning, OB and overtime | `swedish-payroll` |
| Personalliggare and kontrollavgift | `swedish-cash-register` |
| Machines, leasing and depreciation | `swedish-asset-accounting` |
| Year-end provisions and closing | `swedish-year-end-closing` |
