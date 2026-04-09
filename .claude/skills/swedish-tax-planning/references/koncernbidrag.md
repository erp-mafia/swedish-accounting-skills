# Koncernbidrag (Group Contributions)

## Legal basis
IL 35 kap

## Core function

Koncernbidrag transfers taxable income between group companies. Avdragsgillt for the giver, skattepliktigt for the receiver. Enables the koncern to pay tax only on net aggregate profit.

## Requirements (35 kap. 2-3 §§)

All of these must be met:
1. Moderföretaget owns **>90% of andelarna** (capital shares, not votes)
2. Ownership has existed for the **entire tax year** of both giver and receiver (or since subsidiary began any business)
3. Both are qualifying Swedish entities (AB, ekonomisk förening, sparbank, etc.)
4. Neither is a privatbostadsföretag or investmentföretag
5. Both **openly report** (öppet redovisa) the bidrag in income declarations filed at the same deadline
6. An actual **value transfer** must occur no later than the giver's declaration filing date

## Directions

- Parent to subsidiary (nedåtriktat) -- most common
- Subsidiary to parent (uppåtriktat)
- Between systerbolag (sidledes) -- requires common parent owning >90% of both

## Öppna vs dolda koncernbidrag

**Öppna**: Explicitly reported, regulated by IL 35 kap. Booked as bokslutsdisposition.

**Dolda**: Through mispriced intra-group transactions, below-market sales, debt forgiveness. Fall outside IL 35 kap. Trigger uttagsbeskattning and transfer pricing scrutiny under 14 kap. 19 § IL (korrigeringsregeln). Avoid.

## BAS accounts

| Account | Name |
|---------|------|
| 8820 | Mottagna/Erhållna koncernbidrag (receiver) |
| 8830 | Lämnade koncernbidrag (giver) |
| 2860 | Kortfristig skuld till koncernföretag (giver's balance sheet) |
| 1660 | Kortfristig fordran på koncernföretag (receiver's balance sheet) |

**CORRECTION**: Account 8840 is NOT for koncernbidrag. It is "Lämnade gottgörelser." The old accounts 8893/8894 were replaced by 8820/8830 in BAS 2009.

## Underskottsspärr (40 kap. 18-19 §§)

After an ownership change (ägarförändring), the acquired company's old tax losses CANNOT be offset against received koncernbidrag during a spärrtid. This prevents abuse of loss-making shell companies.

## Planning considerations

- Instant resultatutjämning across the group. No 6-year deferral like periodiseringsfond.
- Requires formal bolagsstämmobeslut
- No koncernbidragsrätt in the year a subsidiary is acquired (if it had prior operations) or sold. The "hela beskattningsåret" rule is strict.
- Koncernbidrag REDUCES the giver's EBITDA for ränteavdragsbegränsningar (negative interaction)
- The giver must have sufficient free equity (fritt eget kapital) per ABL to make the transfer without triggering "olovlig värdeöverföring"

## Example

Moder AB: taxable income 5 MSEK. Dotter AB: deficit 3 MSEK.
- Moder gives 3 MSEK koncernbidrag
- Moder: Debit 8830 / Credit 2860. Taxable income: 2 MSEK -> tax 412,000 kr
- Dotter: Debit 1660 / Credit 8820. Taxable income: 0
- Without koncernbidrag, group pays 1,030,000 kr. Saving: 618,000 kr.