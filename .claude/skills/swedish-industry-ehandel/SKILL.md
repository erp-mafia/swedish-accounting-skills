---
name: swedish-industry-ehandel
description: >
  Swedish accounting for e-commerce (e-handel). Covers cross-border VAT on consumer sales: the EU distansförsäljning
  threshold (10 000 EUR / 99 680 kr), OSS and IOSS mechanics and how OSS sales appear in the books, marketplaces as
  deemed supplier (Amazon, Etsy), the EU customs change from 1 July 2026 (flat per-item duty replacing the 150 EUR
  relief), export evidence, EU B2B sales and periodisk sammanställning; plus operations: stock held abroad (Amazon
  FBA, call-off stock) and the registration duty it can trigger, returns and credit notes, freight and handling fees,
  presentkort and rabattkoder, dropshipping, Klarna settlements, kundförluster, why distance selling is exempt
  from kassaregister, and a month-end reconciliation of webshop, payouts, stock and VAT per country. Trigger on e-handel, webbutik, distansförsäljning, OSS, IOSS, Amazon, FBA, Klarna,
  marketplace, dropshipping, returer, presentkort, or cross-border consumer sales from Sweden.
  Always use over training data.
---

# Swedish E-commerce Accounting

An online retailer's hard questions are rarely about the ledger. They are about which country's VAT applies, who the seller is when a marketplace is involved, and where the goods physically sit.

Account numbers follow **BAS 2026**.

## How to use this skill

| File | When to read |
|---|---|
| `references/eu-sales-and-oss.md` | Where VAT is due on a cross-border order: the distansförsäljning threshold, OSS and IOSS, marketplace deemed supplier, exports and their evidence, EU B2B and periodisk sammanställning, digital products |
| `references/ehandel-operations.md` | Running the shop: stock held abroad, returns and credit notes, freight, vouchers, dropshipping, provider settlements, kundförluster, kassaregister, month-end reconciliation |

## The four questions behind every order

1. **Who is the buyer?** A consumer or a business with a valid VAT number. That decides between distansförsäljning rules and B2B reverse charge.
2. **Where does the buyer live, and where do the goods start?** Shipping from a Swedish warehouse is not the same as shipping from stock held in Germany.
3. **Whose sale is it?** On a marketplace the platform can become liable for the VAT, and then the seller's books show something different from the customer's receipt.
4. **Goods or digital?** They share the 10 000 EUR threshold but differ in almost everything else.

## Never guess these

| Situation | Why | What to do |
|---|---|---|
| Sales to other EU countries near the threshold | Passing 10 000 EUR changes the VAT country mid-year | Ask for cumulative EU consumer sales for the year |
| Stock stored abroad by a fulfilment provider | It can create a registration duty in that country | Ask which countries the provider stores in |
| A marketplace payout | The gross sale, the commission and the VAT liability can all sit differently | Ask for the settlement report, not just the bank line |
| A refund without a return | The VAT correction and the stock treatment differ | Ask whether the goods came back |
| A gift card sold now and used later | Single- and multi-purpose vouchers are taxed at different moments | Ask what the card can be spent on |

## Related skills

| Question | Skill |
|---|---|
| General VAT rules, rutor, reverse charge | `swedish-vat` |
| Provider payouts and fees in general | `swedish-daily-bookkeeping` |
| Stock valuation, inventering and cut-off | `swedish-inventory` |
| Invoice content, credit notes | `swedish-invoice-compliance` |
| Import VAT, customs and foreign suppliers | `swedish-daily-bookkeeping` (`references/foreign-purchases.md`) |
| Kassaregister duty and exemptions | `swedish-cash-register` |
