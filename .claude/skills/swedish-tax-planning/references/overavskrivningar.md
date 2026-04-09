# Överavskrivningar (Accelerated Depreciation)

## Legal basis
IL 18 kap (inventarier), IL 19 kap (byggnader)

## Core concept

When skattemässig avskrivning exceeds bokföringsmässig avskrivning (planned depreciation per ÅRL/K2/K3), the difference is an överavskrivning, booked as obeskattad reserv.

## Two methods for inventarier (räkenskapsenlig avskrivning)

### 30-regeln / Restvärdemetoden (IL 18 kap. 13 §)
- Tax book value of all pooled inventarier can be written down to **70%** of avskrivningsunderlag
- Avskrivningsunderlag = prior-year tax residual value + new acquisitions - sales proceeds of items acquired in prior years
- Yields up to 30% deduction annually on declining balance
- Applied on the entire pool collectively

### 20-regeln / Kompletteringsregeln (IL 18 kap. 17 §)
- 20% straight-line depreciation from acquisition year
- Full depreciation in 5 years
- Applied per individual asset, then summed
- Each asset's remaining tax value = max(anskaffningsvärde x (1 - 0.20 x antal år), 0)

### Choosing between methods
- Companies may switch between the two methods each year
- Choose whichever yields the **lowest tax book value** (largest total deduction)
- 20-regeln typically wins for older assets; 30-regeln for newer large acquisitions

## Direktavdrag (IL 18 kap. 4 §)
Assets costing less than **half a prisbasbelopp** or with expected useful life ≤ 3 years:
- 2025: < 29,400 kr
- 2026: < 29,600 kr

## BAS accounts

| Account | Name |
|---------|------|
| 2150 | Ackumulerade överavskrivningar (group) |
| 2153 | Ack. överavskrivningar, maskiner och inventarier |
| 8850 | Förändring av överavskrivningar (group) |
| 8853 | Förändring av överavskrivningar, maskiner och inventarier |
| 7831-7835 | Avskrivningar enligt plan (per asset category) |
| 1220/1229 | Inventarier: anskaffningsvärde / ack. avskrivningar |

## Obeskattade reserver split

Obeskattade reserver from överavskrivningar consist of:
- ~79.4% eget kapital
- ~20.6% latent skatteskuld (deferred tax liability)

Under K3 consolidated accounts, these are split explicitly. Under K2, they appear as gross line item.

## Interaction with periodiseringsfond

Both create obeskattade reserver and can be used simultaneously. Optimal year-end sequence:
1. Maximize överavskrivningar (limited by asset base)
2. Calculate remaining taxable income
3. Set aside up to 25% to periodiseringsfond

## Critical pitfall

Skatteverket ställningstagande 2024-10-15, dnr 8-3120349: If a company systematically (more than one year) books depreciation exceeding the skattemässigt maximum, it **loses the right to räkenskapsenlig avskrivning entirely** and is forced onto restvärdesavskrivning (25% of residual value). A one-time error does not forfeit the right.

## Planning considerations

- Most valuable for capital-intensive businesses with large inventarier bases
- Combined with periodiseringsfond, an asset-heavy AB can defer the vast majority of its tax bill
- Monitor the gap between plan and tax depreciation to avoid unintended over-depreciation
- In a sale scenario, överavskrivningar are reversed (creating taxable income), so plan exit timing carefully