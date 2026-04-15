# K2/K3 Revenue Recognition for Project Accounting

## Table of contents

1. K3 Chapter 23: successiv vinstavräkning
2. K2 Chapter 6: uppdrag till fast pris
3. K2 vs K3 comparison
4. Befarade förluster
5. Note disclosures
6. Choosing K2 vs K3 for project-intensive companies

---

## 1. K3 Chapter 23: successiv vinstavräkning

BFNAR 2012:1 Chapter 23 ("Intäkter") governs revenue recognition for tjänsteuppdrag and entreprenadavtal.

### The mandatory main rule (punkt 23.18)

For koncernredovisning: successiv vinstavräkning is MANDATORY for fixed-price contracts.
For juridisk person: successiv vinstavräkning is the default, with an opt-out to alternativregeln per punkt 23.31.

Revenue and expenses shall be recognized based on the färdigställandegrad at each balance sheet date when ALL FOUR conditions are met:

1. Uppdragsinkomsten (contract revenue) can be reliably measured
2. It is probable that economic benefits will flow to the entity
3. Färdigställandegrad at balance date can be reliably determined
4. Uppdragsutgifter incurred and remaining can be reliably measured

If conditions are NOT met: recognize revenue only to the extent of costs incurred (zero profit method) until reliable estimation becomes possible.

### Calculating färdigställandegrad

The cost-to-cost method is dominant in Swedish practice:

```
Färdigställandegrad = Nedlagda kostnader / Totalt beräknade kostnader
```

Other permitted methods (less common):
- Physical measurement of work completed
- Proportion of contract work completed (milestones)

What counts as nedlagda kostnader:
- Direct materials consumed
- Direct labor (timkostnad × hours from time reporting)
- Subcontractor costs
- Directly attributable overhead (allocated per fördelningsnyckel)
- Depreciation on project-specific equipment

What does NOT count:
- Costs for future activity (materials delivered but not installed)
- Prepaid costs not yet consumed
- General overhead not attributable to the project

### Löpande räkning (time-and-materials)

Punkt 23.17: revenue recognized as work is performed. No completion percentage calculation needed. The practical rule: revenue = hours worked × agreed hourly rate + materials at agreed markup.

WIP for löpande räkning: upparbetad ej fakturerad = (work performed at agreed rates) - (invoiced amount). If positive: Debet 1620L / Kredit 3xxx. This is straightforward because the "reliable estimation" conditions are inherently met.

### Alternativregeln in juridisk person (punkt 23.31)

Available only for pågående arbeten in byggnads-, anläggnings-, hantverks- eller konsultrörelse, as referenced to 17 kap. 23 § IL.

Under this method:
- Costs are capitalized on 1470
- Revenue recognized only when the project is substantially complete
- Requires "särskilda skäl" to switch from successiv vinstavräkning (punkt 23.37)
- Once chosen, must be applied consistently to similar contracts

### Contract modifications and claims

Punkt 23.20-23.22: contract modifications (tilläggsarbeten) are included in contract revenue when:
- The customer has approved the modification (formally or through actions)
- The amount can be reliably measured

Incentive payments and claims: included only when the project has progressed far enough that performance targets are probable and measurable.

### Multi-element contracts

Punkt 23.9-23.15: a single contract may be split into separate assignments if each has separate pricing and can be accepted/rejected independently. Conversely, multiple contracts with the same customer should be combined if negotiated as a package and performed concurrently/sequentially.

---

## 2. K2 Chapter 6: uppdrag till fast pris

BFNAR 2016:10 Chapter 6 provides two methods for fixed-price contracts.

### Huvudregeln (punkt 6.14)

Similar to successiv vinstavräkning. Revenue recognized based on degree of completion. Same cost-to-cost calculation applies.

### Alternativregeln (punkt 6.15)

Revenue recognized only when the assignment is "väsentligen fullgjort" (substantially complete).

Per Srf U 15: "väsentligen fullgjort" is assessed from the customer's acceptance and realization perspective, not a volume perspective. The work must be in a state where the customer can derive the intended benefit. Remaining work should be minor corrections, documentation, or warranty-related tasks.

Per Srf U 14: pågående arbeten under alternativregeln must be reported gross per individual project. Netting of projects with surplus (1470) against projects with deficit (liability on 2430-2439) is prohibited.

### Löpande räkning under K2

Punkt 6.12-6.13: revenue recognized as work is performed, identical to K3. The special K2 provision: if a time-and-materials contract includes a price ceiling (takpris), it is still treated as löpande räkning unless the ceiling fundamentally changes the risk profile.

---

## 3. K2 vs K3 comparison for project accounting

| Aspect | K2 | K3 |
|--------|----|----|
| Fixed-price recognition | Main rule OR alternativregeln | Successiv vinstavräkning mandatory (koncern) |
| T&M recognition | As work performed | As work performed |
| Dev cost capitalization | Prohibited (punkt 10.4) | Allowed under aktiveringsmodellen |
| Uppskjuten skatt | Prohibited | Required |
| Revenue recognition standard | Rule-based, simplified | Principle-based (Chapter 23) |
| Resultaträkning format | Kostnadsslagsindelning only | Kostnadsslags- or funktionsindelning |
| Note disclosures | Simplified | Full disclosures per Chapter 23 |
| Multi-element splitting | Limited guidance | Detailed rules (punkt 23.9-23.15) |
| Befarade förluster | Must recognize immediately | Must recognize immediately |

### Key K2 limitation: punkt 10.4

Egenupparbetade immateriella tillgångar får inte aktiveras. ALL internally generated intangible assets (software, patents, development work) must be expensed immediately. Even a partially purchased asset becomes "tainted" as internally generated if incorporated into new development. Companies needing to capitalize development costs MUST use K3.

This is the single most impactful difference for project-intensive tech/R&D companies. A software company spending 2 MSEK/year on development cannot show this as an asset under K2, directly reducing equity and potentially triggering kontrollbalansräkning.

---

## 4. Befarade förluster

### K3 requirement (punkt 23.32)

If total estimated contract costs exceed total contract revenue, the expected loss must be recognized as a cost IMMEDIATELY, regardless of:
- How far the project has progressed
- Whether work has even begun
- The färdigställandegrad

The full expected loss is recognized, not just the loss proportional to completion.

### K2 requirement

Same principle applies under both huvudregeln and alternativregeln. An anticipated loss must be expensed in full when identified.

### Detection logic for software implementation

Flag a project for befarad förlust review when:

```
IF (actual_costs_to_date + estimated_remaining_costs) > total_contract_revenue
THEN expected_loss = total_estimated_costs - total_contract_revenue
     provision_needed = expected_loss - any_existing_provision
```

The system should alert when:
1. Estimated remaining costs are updated upward
2. Contract revenue is revised downward
3. Actual costs exceed the original budget pace by >15%
4. Färdigställandegrad lags behind the time-elapsed ratio by >25%

### Booking pattern

```
Debet 4970 / 78xx {6 "project"}  [loss amount]
Kredit 2290 {6 "project"}        [loss amount]
```

If the loss estimate later decreases, the provision is reversed (but never below zero, and never creating a profit provision).

---

## 5. Note disclosures

### K3 större företag (punkter 23.28-23.30)

The årsredovisning must include notes disclosing:
1. Revenue recognized from construction/service contracts in the period
2. Methods used to determine färdigställandegrad
3. Aggregate amount of costs incurred and recognized profits (less recognized losses) to date
4. Amount of advances received
5. Amount of retentions (innehållna belopp)
6. Gross amount due from customers (tillgång): costs + recognized profits - recognized losses - progress billings, when positive
7. Gross amount due to customers (skuld): same calculation, when negative

### K3 mindre företag

Simplified disclosures. Must disclose:
- Accounting principles for revenue recognition
- Principles for pågående arbeten

### K2

Chapter 18 and 19 note requirements. Must disclose:
- Redovisningsprinciper including method for pågående arbeten
- Whether huvudregeln or alternativregeln is applied

### Balance sheet presentation

Under ÅRL:
- 1620 (upparbetad ej fakturerad intäkt): presented under Kortfristiga fordringar
- 1470 (pågående arbeten): presented under Varulager > Pågående arbete för annans räkning
- 2450 (fakturerad ej upparbetad intäkt): presented under Kortfristiga skulder

---

## 6. Choosing K2 vs K3 for project-intensive companies

### Factors favoring K3

- Need to capitalize development costs (software, R&D)
- Large fixed-price construction contracts spanning multiple years (successiv vinstavräkning gives smoother P&L)
- Want to present both kostnadsslags- and funktionsindelad resultaträkning
- Revenue recognition complexity requires principle-based framework
- Audit requirement makes K3 transition cost marginal

### Factors favoring K2

- Simple project structure (few projects, all löpande räkning)
- No internally generated intangible assets
- Preference for the alternativregeln's simplicity (recognize at completion)
- No audit requirement, small company wanting minimal compliance burden
- Construction company preferring to defer revenue recognition for tax timing

### Tax implications of the choice

Under the materiellt samband principle, accounting choices flow to taxation. A K3 company using successiv vinstavräkning recognizes taxable income earlier than a K2 company using alternativregeln on the same project. However, the alternativregeln provides tax deferral (matched by delayed cost relief via 1470 capitalization), which can be a significant cash flow benefit for growing construction companies.

The exception: löpande räkning contracts where tax treatment can diverge from accounting (HFD 2011 ref. 20). See tax-and-grants.md for details.