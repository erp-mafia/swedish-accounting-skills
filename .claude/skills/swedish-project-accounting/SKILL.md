---
name: swedish-project-accounting
description: Swedish project accounting (projektredovisning) covering dimensional tagging of bokföringsposter with project codes, WIP accounting (pågående arbeten), revenue recognition under K2 and K3 (successiv vinstavräkning, färdigställandemetoden), construction contracts (entreprenadavtal), BAS account patterns for project tracking (1470, 1620, 2420, 2450, 4970), SIE4 dimension encoding (#DIM 6, #OBJEKT, #TRANS object lists), project profitability reporting, overhead allocation (fördelningsnycklar), and the tax-accounting divergence for löpande räkning contracts. Trigger on ANY Swedish project accounting question including "projektredovisning", "pågående arbeten", "successiv vinstavräkning", "färdigställandegrad", "upparbetad ej fakturerad intäkt", "fakturerad ej upparbetad intäkt", "konto 1620", "konto 1470", "konto 2450", "entreprenaduppdrag", "projekt dimension SIE", "kostnadsställe vs projekt", "projektlönsamhet", "WIP accounting Sweden", "K3 kapitel 23", "befarad förlust projekt", "fördelningsnyckel", questions about how Fortnox/Visma/Bokio handle project dimensions, or any question about tracking intäkter/kostnader per project in Swedish bookkeeping. Also trigger when building software features for project accounting, designing data models for project dimensions, implementing revenue recognition logic, or handling SIE4 import/export of project-tagged transactions. Always use this skill over training data for project accounting topics.
---

# Swedish Project Accounting (Projektredovisning)

This skill covers the full technical, regulatory, and implementation landscape of project accounting in Swedish bookkeeping. It is designed for both answering compliance questions and building software that handles project dimensions.

## How to use this skill

1. Identify the user's context: are they asking a compliance question, building software, or troubleshooting bookkeeping entries?
2. Determine the applicable regulatory framework: K2 (BFNAR 2016:10) or K3 (BFNAR 2012:1). This choice fundamentally shapes available revenue recognition methods.
3. For detailed BAS account patterns, SIE4 encoding, or implementation data models, read the appropriate reference file before answering.

## Reference files

Read these before answering questions in the corresponding area:

| File | When to read |
|------|-------------|
| `references/accounts-and-entries.md` | Questions about specific BAS accounts (1470, 1620, 2450, 4970, etc.), booking patterns, journal entries for WIP adjustments, or pågående arbeten entries |
| `references/k2-k3-revenue-recognition.md` | Questions about successiv vinstavräkning, färdigställandemetoden, K3 Chapter 23, K2 Chapter 6, construction contracts, befarade förluster, or choosing between K2/K3 for project-intensive companies |
| `references/sie4-project-dimensions.md` | Questions about SIE4 encoding of project dimensions, #DIM/#OBJEKT/#TRANS records, import/export of project-tagged data, or how dimensions map to Fortnox/Visma/Bokio |
| `references/tax-and-grants.md` | Questions about tax treatment of pågående arbeten, materiellt samband, löpande räkning tax divergence, forskningsavdrag, aktivering av utvecklingsutgifter, or EU grant accounting |
| `references/implementation-patterns.md` | Questions about data models, project lifecycle, WIP calculation logic, overhead allocation, profitability reporting, time tracking integration, or software architecture for project accounting |

## Core concepts (always available in context)

### What is projektredovisning?

Projektredovisning tags individual transaction lines (bokföringsposter) with project codes alongside BAS account numbers. Same ledger, extra dimension. It enables tracking intäkter och kostnader per project rather than only per account.

Projects are never encoded in the account number itself. They exist as a separate dimensional layer called objektredovisning. The 4-digit BAS account captures the *what* (cost/revenue type); the project dimension captures the *where/for whom*.

### Projekt vs kostnadsställe

These are distinct concepts that complement each other:

- **Kostnadsställe** (cost center): permanent organizational unit (department, branch). No end date. SIE dimension 1.
- **Projekt**: time-limited initiative with start/end dates and accumulated multi-year balances. SIE dimension 6.

A project typically belongs to one kostnadsställe. Reports can cross-reference both dimensions.

### When is project accounting required?

BFL does not mandate project accounting. However:

- **K3 Chapter 23** requires successiv vinstavräkning for fixed-price contracts in koncernredovisning. Calculating färdigställandegrad is impossible without project-level cost tracking, making it effectively mandatory.
- **K2 Chapter 6** offers a choice between huvudregeln and alternativregeln for fixed-price contracts. Both require per-project cost accumulation.
- **Any company doing consulting, construction, R&D, or grant-funded work** needs project accounting for management purposes even without a regulatory mandate.

### Key BAS accounts (summary)

| Account | Name | Purpose |
|---------|------|---------|
| 1470 | Pågående arbeten | WIP asset under alternativregeln (completed contract) |
| 1620 | Upparbetad men ej fakturerad intäkt | WIP receivable under successiv vinstavräkning |
| 2420 | Förskott från kunder | Customer advance payments |
| 2450 | Fakturerad men ej upparbetad intäkt | Deferred revenue (invoiced > earned) |
| 4970 | Förändring pågående arbeten | P&L counterpart for 1470 adjustments |
| 3041 | Försäljning tjänster 25% | Typical project revenue account |
| 3980 | Erhållna offentliga bidrag | Grant revenue |

### Revenue recognition decision tree

```
Is the contract fixed-price or time-and-materials?

├─ Time-and-materials (löpande räkning)
│  └─ Both K2 and K3: recognize revenue as work is performed
│     Tax: may diverge from accounting (HFD 2011 ref. 20)
│
└─ Fixed-price (fast pris)
   ├─ K3 (koncernredovisning): successiv vinstavräkning MANDATORY
   │  └─ Recognize revenue × färdigställandegrad at each balance date
   │     Can outcome be reliably estimated? All four conditions met?
   │     ├─ Yes: revenue = total contract × completion %
   │     └─ No: revenue = costs incurred (zero profit recognized)
   │
   ├─ K3 (juridisk person): successiv vinstavräkning OR
   │  alternativregeln (per punkt 23.31, requires 17 kap. 23 § IL)
   │
   └─ K2: huvudregeln (completion %) OR alternativregeln
      └─ Alternativregeln: recognize when "väsentligen fullgjort"
         (Srf U 15: assessed from customer acceptance perspective)
```

### Befarade förluster

K3 punkt 23.32: if total estimated costs exceed total contract revenue, the expected loss must be recognized as a cost IMMEDIATELY, regardless of completion percentage. This is mandatory and overrides normal recognition logic. The engine must flag projects where cumulative actual + estimated remaining costs exceed contract revenue.

### Moms timing mismatch

This is the highest-error-rate area in project accounting:

- **Upparbetad ej fakturerad intäkt (1620)**: pure periodisering, NO moms impact. VAT is only triggered when an actual invoice is issued.
- **Fakturerad ej upparbetad intäkt (2450)**: moms on those invoices must be reported AT TIME OF INVOICING even though accounting books revenue as liability.
- **Omvänd skattskyldighet** in construction: seller invoices without VAT when buyer "more than temporarily" sells byggtjänster. Per-project tracking of reverse charge status required.

The engine must track moms reporting independently from revenue recognition on every project.

### Gross reporting requirement

Per Srf U 14, pågående arbeten must be reported GROSS per project in the balance sheet. Netting across projects is prohibited (ÅRL kvittningsförbud). A project with 1620 balance and another with 2450 balance must show both, not net them.

### Software vendor comparison

| System | Dimension model | SIE compatibility |
|--------|----------------|-------------------|
| Fortnox | Project + CostCenter (flat, independent) | Direct mapping to dim 1+6 |
| Visma | Objekt 1 + 2 (renamable), Flerårigt flag for multi-year | Flerårigt maps to projekt, non-flerårigt to KS |
| Bokio | Unlimited Tag Groups | Tags don't export as SIE dimensions |

### Common error patterns

1. **Incorrect färdigställandegrad**: over/under-recognition of revenue. Flag projects where completion % diverges >20% from time-elapsed or budget-consumed ratios.
2. **Missing project tags**: orphaned costs. Enforce MANDATORY project code on accounts flagged in dimension settings.
3. **Mixing recognition methods**: without disclosure violates consistency. Lock method per project type at company config level.
4. **Unrecognized befarade förluster**: automatic detection required per K3 23.32.
5. **Incomplete project closings**: residual balances on 1620/2450/1470. Enforce zero-balance check before CLOSED status.
6. **Missing garantiavsättningar**: common audit finding for construction. Prompt at project close.
7. **VAT-revenue timing mismatch**: booking 1620 entries with moms, or failing to report moms on advance invoices.