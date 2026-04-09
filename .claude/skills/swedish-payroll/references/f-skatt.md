# F-skatt vs A-skatt

## Employer obligations by recipient status

| Recipient status | Withhold tax? | Pay arbetsgivaravgifter? |
|---|---|---|
| A-skatt (employee) | Yes, per skattetabell | Yes, 31.42% |
| F-skatt (contractor) | No | No |
| FA-skatt (employment portion) | Yes, on salary | Yes, on salary |
| No F-skatt stated | Yes, must withhold 30% | Yes, full contributions |

## Liability

If an employer pays someone without F-skatt and fails to withhold tax, the employer becomes personally liable for both the missing tax and arbetsgivaravgifter.

## Verification

Currently via Skatteverket's "Hämta företagsinformation" e-tjänst (manual lookup by organisationsnummer). A programmatic Företagsuppgifter API is under development on the Utvecklarportal but not yet fully launched.

### Implementation requirements
- Mandatory verification workflow before first payment to any contractor
- Store verification date and result
- Re-verify periodically

## FA-skatt

Applies to individuals with both employment and business income. The employer handles A-skatt + avgifter on the salary portion; the individual handles F-skatt + egenavgifter on business income. Juridiska personer (AB, HB) cannot have FA-skatt.