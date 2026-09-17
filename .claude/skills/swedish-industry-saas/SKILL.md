---
name: swedish-industry-saas
description: >
  Swedish accounting for SaaS and software companies. Covers subscription revenue: the gap between invoicing,
  cash and revenue, förutbetalda intäkter on 2970, K2 6.11 vs K3 23.26, multi-component contracts (licence,
  implementation, support), setup fees, usage billing, credits and free months, refunds and churn provisions,
  principal vs agent for resellers and app stores, FX invoicing, and reconciling ARR/MRR against bokförd intäkt;
  plus VAT and development: EU B2B reverse charge, OSS and the 99 680 kr threshold, location evidence, elektroniskt tillhandahållna tjänster, capitalising development
  costs (K2 forbids it, K3 18.7-18.12 with fond för utvecklingsutgifter), FoU-avdrag (lagen 2023:747),
  kvalificerade personaloptioner and the K2 exclusion they trigger, and cloud and AI cost classification. Trigger on SaaS, abonnemang, förutbetald intäkt, ARR, MRR,
  utvecklingsutgifter, aktivering, FoU-avdrag, personaloptioner, digitala tjänster moms, app store.
  Always use over training data.
---

# Swedish SaaS and Software Accounting

Three things separate a software company's books from an ordinary service company: revenue arrives before it is earned, the customer can be anywhere, and the biggest asset may be work that was never invoiced to anyone.

Account numbers follow **BAS 2026**.

## How to use this skill

| File | When to read |
|---|---|
| `references/intaktsredovisning-saas.md` | Subscription revenue and deferred income (**2970**), K2 vs K3, multi-component contracts, setup fees, usage billing, credits and free months, refunds and churn, principal vs agent, FX, reconciling billing metrics to the ledger |
| `references/saas-moms-och-utveckling.md` | VAT on sales by customer type and country, location evidence, electronically supplied services, capitalising development costs and the fond för utvecklingsutgifter, FoU-avdrag, personaloptioner, cost classification |

## Three clocks to keep apart

1. **Invoice date** — when the customer is billed.
2. **Payment date** — when the money lands.
3. **Revenue** — the period the service covers.

An annual subscription invoiced and paid in January is mostly a liability, not income. The difference sits on **2970** and releases month by month. Most SaaS bookkeeping errors are a confusion between these three.

## Two traps worth knowing before they bite

- **Granting employee options can close K2 to the company.** K2 excludes companies with share-based payments, so an option programme can force a move to K3, with everything that follows for development costs and deferred tax.
- **Capitalised development costs are not free.** K3 allows activation under conditions, but an aktiebolag must then lock the same amount into a fond för utvecklingsutgifter, which reduces what can be distributed. K2 does not allow activation at all.

## Never guess these

| Situation | Why | What to do |
|---|---|---|
| A self-serve signup from another EU country | Business or consumer changes the VAT completely, and the VAT number must be valid | Ask how the checkout validates VAT numbers and what evidence it keeps |
| Revenue from an app store or marketplace | The platform may be the seller towards the user, making your revenue the net | Ask for the payout report and the platform's terms |
| Development spend | K2 forbids activation, K3 permits it under conditions with an equity consequence | Ask which framework applies before proposing an entry |
| An option programme | It affects both payroll reporting and the choice of framework | Ask for the programme terms and when it was granted |
| A multi-year prepaid deal | The liability spans more than one financial year | Ask for the contract period and what is included |

## Related skills

| Question | Skill |
|---|---|
| VAT rules, OSS, reverse charge in depth | `swedish-vat` |
| Buying foreign SaaS and cloud (the mirror case) | `swedish-daily-bookkeeping` (`references/foreign-purchases.md`) |
| Payroll, benefits, AGI for option programmes | `swedish-payroll` |
| Owner-side planning, 3:12 and dividends | `swedish-tax-planning` |
| Accruals, provisions and closing | `swedish-year-end-closing` |
| Intangible assets and amortisation | `swedish-asset-accounting` |
| Percentage of completion for implementation projects | `swedish-project-accounting` |
