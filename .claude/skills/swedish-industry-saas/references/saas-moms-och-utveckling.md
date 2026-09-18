# VAT, Development Costs and Incentives for SaaS Companies

Scope: what is specific to software businesses. General VAT rules, momsdeklaration mechanics and EU trade live in `swedish-vat`; AGI and payroll mechanics in `swedish-payroll`; owner-side option and dividend planning in `swedish-tax-planning`; revenue recognition in `intaktsredovisning-saas.md`.

**Which year this describes.** ML is cited from the consolidated text t.o.m. SFS 2026:1025, IL t.o.m. SFS 2026:1393, SFL t.o.m. SFS 2026:1305. K2 and K3 points are from the consolidated vägledningar for räkenskapsår beginning after 2025-12-31 (K2 as amended by BFNAR 2025:2, K3 by BFNAR 2025:3 and 2025:4). Rates and amounts are the 2026 figures. Proposals are labelled as such. Sources and check dates in section 11.



## Table of contents

1. VAT on sales: the checkout decision
2. Evidence of the customer's location
3. Electronically supplied services: what qualifies
4. VAT on purchases
5. Development costs: K2, K3 and ÅRL
6. Development costs: tax
7. FoU-avdrag
8. Personaloptioner
9. Typical cost questions
10. Ask the user
11. Sources

---

## 1. VAT on sales: the checkout decision

The place-of-supply rules for services are in ML 2023:200 6 kap. For a SaaS seller established only in Sweden, four branches cover almost everything.

| Customer | Rule | Swedish VAT? | Account | Fält |
|----------|------|--------------|---------|------|
| Swedish, any status | 6 kap 33 § / 35 § | Yes, 25 % | **3001** / **2611** | 05 + 10 |
| Beskattningsbar person in another EU country, valid VAT number | 6 kap 33 § — supplied where the buyer is established | No; buyer accounts for it | **3308** | 39, plus periodisk sammanställning |
| Non-taxable person in another EU country | 6 kap 56 § — supplied where the customer is established, resident or habitually stays | Destination-country VAT via OSS, **unless** under the 6 kap 62 § threshold | see below | Excluded from the ordinary momsdeklaration when declared in OSS |
| Customer outside the EU | 6 kap 33 § (B2B) or 6 kap 56 § (B2C electronic services); not supplied inom landet, so gjord utomlands per 6 kap 3 § | No | **3305** | 40 |

### B2B within the EU

The invoice must carry the buyer's VAT number and the wording **"omvänd betalningsskyldighet"** — ML 17 kap 24 § första stycket 14: "när förvärvaren är skyldig att betala mervärdesskatten, uppgiften omvänd betalningsskyldighet". "Reverse charge" is accepted alongside it. Invoice content rules are in `swedish-invoice-compliance`.

**VAT number validation.** Skatteverket requires the number to be checked in the European Commission's VIES service at the time of sale, and states that a check made through any other service is not accepted as proof if the number later turns out to be wrong. Store the VIES response with the invoice.

If the seller cannot show that the buyer is a beskattningsbar person, Skatteverket's position is that the buyer is treated as a non-taxable person — which means Swedish VAT in fält 05 and 10. Taxable-person status can be shown by other means than a VAT number; where it is, the sale goes in fält 39 but **not** in the periodisk sammanställning. EU backstop: Implementing Regulation (EU) 282/2011 art. 18, under which the supplier may treat an EU customer as non-taxable for as long as the customer has not communicated a VAT identification number.

**Periodisk sammanställning.** SFL 35 kap 2 § första stycket 2 imposes the duty for services taxable in the customer's EU country where the buyer is liable under art. 196 of the VAT Directive. SFL 35 kap 3 §: **kalenderkvartal for services**, kalendermånad for goods, and monthly if both are reported in the same period. A services-only SaaS seller therefore files **quarterly**. Deadline per SFL 35 kap 9 §: the **25th** of the month after the period if filed electronically, the 20th otherwise. No sales in a period means no sammanställning.

### B2C within the EU and the threshold

**ML 6 kap 62 §** keeps the supply in Sweden — Swedish VAT, fält 05 and 10 — where all of the following hold: the seller is established in Sweden and has no establishment in another EU country; the customer is established, resident or habitually staying in another EU country; and the combined value excluding VAT of the TBE services under 6 kap 56 § **and** the unionsintern distansförsäljning of goods under 6 kap 8 § does not exceed **99 680 kronor** in the current calendar year and did not exceed it in the immediately preceding calendar year. That is the Swedish figure for the EU's 10 000 EUR threshold, and it is one combined amount for goods and services, not two.

Once exceeded, **6 kap 63 §** moves the place of supply abroad "från och med det tillhandahållande eller den leverans som medför att beloppet överskrids" — from the transaction that breaks the limit, not from the next month. The checkout must therefore watch a running total and switch mid-year.

**6 kap 64–65 §**: a seller under the threshold may ask Skatteverket to treat the supplies as made in the customer's country anyway. The decision "gäller tills vidare", and 6 kap 62 § may not be applied again until after the end of the second calendar year following the year of the decision. Choose this deliberately — it is a two-year commitment at minimum.

**OSS.** The union scheme is in ML 22 kap (the old lagen 2011:1245 was repealed when ML 2023:200 came into force). A redovisningsperiod is a **kalenderkvartal** (22 kap 35 §); the särskild mervärdesskattedeklaration must reach Skatteverket by the **last day of the month after the period** (22 kap 43 §), and the VAT must be paid by the same day (22 kap 44 §). Sales declared in OSS are excluded from the ordinary momsdeklaration. BAS 2026 has **2670 Utgående moms på försäljning inom EU, OSS** for the output VAT but no revenue account for these sales; define free sub-accounts in kontogrupp 33 per destination country, because OSS reports per country.

### What a self-serve checkout must decide, in order

1. **In Sweden?** → 25 %, **3001**/**2611**, fält 05 + 10.
2. **In another EU country with a VIES-verified VAT number?** → no VAT, "omvänd betalningsskyldighet", **3308**, fält 39, periodisk sammanställning. No valid number → treat as B2C.
3. **B2C in the EU:** still within the 6 kap 62 § threshold? → Swedish 25 %, fält 05 + 10. Over it, or opted in under 6 kap 64 § → destination rate, **2670**, OSS.
4. **Outside the EU** → no Swedish VAT, **3305**, fält 40.

Store per transaction: the evidence in section 2, the VIES response, and the running threshold total. Without those the classification cannot be defended later.

---

## 2. Evidence of the customer's location

Council Implementing Regulation (EU) 282/2011, as amended by Regulation (EU) 1042/2013 and Regulation (EU) 2017/2459, sets presumptions for TBE services.

| Article | Rule |
|---------|------|
| **24a** | Physical-presence supplies (wi-fi hotspot, internet café, hotel lobby, telephone box): the customer is presumed to be at that location. On board a ship, aircraft or train in intra-Community passenger transport: the country of departure |
| **24b(a)–(c)** | Fixed land line → place of installation. Mobile network → the country of the SIM card's mobile country code. Decoder or viewing card → where it is located or was sent |
| **24b(d)** | All other cases — which is where ordinary SaaS sits: the place identified by the supplier on the basis of **two items of non-contradictory evidence** from the article 24f list |
| **24b, second paragraph** | Simplification: where the supplier's total such supplies, excluding VAT, do not exceed **EUR 100 000** in the current and the preceding calendar year, **one** item of evidence suffices — but it must come from a person involved in the supply **other than the supplier or the customer**, and must be from points (a)–(e) of article 24f. The simplification stops applying from the moment the threshold is exceeded |
| **24d(1)** | The supplier may rebut a 24a or 24b(a)–(c) presumption with **three** items of non-contradictory evidence |
| **24f** | The evidence list: (a) billing address; (b) IP address or other geolocation; (c) bank details, such as the location of the account used for payment or the billing address held by that bank; (d) the mobile country code of the IMSI on the SIM card; (e) the location of the fixed land line; (f) other commercially relevant information |

For a self-serve checkout the practical pair is the billing address plus the IP address or the payment card's issuing country. A self-declared country on its own is not evidence under 24f, and under the EUR 100 000 simplification the single item must come from a third party — so the customer's own statement can never be the sole basis.

---

## 3. Electronically supplied services: what qualifies

**ML 6 kap 57 §**: "Med elektroniska tjänster avses bland annat tillhandahållande av
1. webbplatser, webbhotell samt distansunderhåll av programvara och utrustning, 2. programvara och uppdatering av denna, 3. bilder, texter och uppgifter samt databasåtkomst, 4. musik, filmer och spel … och 5. distansundervisning." The second stycke is the one agents forget: **"Om en tjänst tillhandahålls via e-post, ska detta i sig inte innebära att tjänsten är en elektronisk tjänst."**

The EU definition adds the operative test. Regulation 282/2011 art. 7(1): services "delivered over the Internet or an electronic network and the nature of which renders their supply essentially automated and involving minimal human intervention, and impossible to ensure in the absence of information technology". Annex I lists website and webpage hosting, automated online and distance maintenance of programmes, remote systems administration, online data warehousing, on-demand disc space, and accessing or downloading software including updates.

Art. 7(3) lists what is **not** an electronically supplied service. Two entries decide most software-company cases:

| Not an electronic service | Where it falls instead |
|---------------------------|------------------------|
| Art. 7(3)(i): "services of professionals such as lawyers and financial consultants, who advise clients by e-mail" | The ordinary huvudregler, ML 6 kap 33 § (B2B) and 35 § (B2C) |
| Art. 7(3)(j): "teaching services, where the course content is delivered by a teacher over the Internet or an electronic network (namely via a remote link)" | Same. Annex I(5)(a) covers automated distance teaching but excludes cases where the internet is "used as a tool simply for communication between the teacher and student" |
| Art. 7(3)(n): telephone helpdesk services | Same |

So: a standardised self-serve SaaS subscription is an electronically supplied service. Consultancy delivered by email, a live human-led training session, and a phone helpdesk are not, even when the company also sells SaaS. The difference matters because the B2C place-of-supply rule in 6 kap 56 § (customer's country, OSS) applies only to the electronic part; a human service to a non-taxable EU customer falls back to 6 kap 35 § and is taxed where the supplier is established.

Osäkert: how a single bundled supply of SaaS plus heavy human implementation is classified — one composite supply or two — and which element dominates. Skatteverket's rättslig vägledning would address this, but www4.skatteverket.se rejects automated retrieval and could not be checked. Ask the user for the contract and price split, and verify this point by hand before advising.

---

## 4. VAT on purchases

Foreign SaaS and cloud costs are the mirror image of section 1: the Swedish buyer accounts for the VAT under omvänd betalningsskyldighet, books it to **2614** and **2645**, and deducts it in the same return where the activity is fully VAT-liable — so the net effect is nil but the boxes must still be filled.

Do not restate the mechanics here. See `swedish-vat/references/vat-compliance-reference.md` for the full treatment of förvärvsbeskattning, the momsdeklaration boxes and the BAS 26xx series, and `swedish-daily-bookkeeping/references/foreign-purchases.md` where that skill is present in the workspace.

Two software-specific reminders: an invoice from a non-EU vendor with no VAT number is still subject to förvärvsbeskattning if the service is supplied inom landet under ML 6 kap 33 §; and VAT charged by a foreign supplier that should not have been charged is **not** deductible in Sweden — book it to **6998 Utländsk moms** and reclaim it from the foreign tax authority, or get the invoice corrected.

---

## 5. Development costs: K2, K3 and ÅRL

### The K2 ban

**K2 punkt 10.4**: "En egenupparbetad immateriell anläggningstillgång får inte redovisas som tillgång trots att 4 kap. 2 § årsredovisningslagen (1995:1554) ger viss möjlighet till det. Utgifter som kan hänföras till en sådan tillgång ska redovisas som kostnad." The second stycke extends this to a hybrid asset: an asset made up of an acquired and a self-developed part counts as egenupparbetad if the purpose at acquisition was that the acquired part would, through the company's own development work, form part of a new unique asset. Punkt 10.4 was **not** amended by BFNAR 2025:2.

Two consequences agents get wrong. The ban does not turn on who did the work — consultants' invoices for building the company's own product are as unusable as internal salaries; what matters is self-developed versus acquired from an external party. And a purchased framework, library or plug-in licence bought solely to become part of a new unique product is pulled into the ban, while a purchased standard system merely configured for internal use is not.

BAS marks **1010**, **1011**, **1012**, **1018**, **1019** and **2089** with "#", meaning they are not to be used when K2 is applied.

### The K3 choice

**K3 punkt 18.7**: the company chooses **kostnadsföringsmodellen** or **aktiveringsmodellen**, and the choice must be applied consistently to all internally generated intangible fixed assets. Under punkt 18.30 a juridisk person may use kostnadsföringsmodellen even where the group accounts use aktiveringsmodellen.

Under the aktiveringsmodell, **punkt 18.9** splits the work into a research and a development phase — if they cannot be separated, the whole thing is research — and **punkt 18.11** expenses all research-phase expenditure as incurred. **Punkt 18.12** capitalises development expenditure **only** where the company can demonstrate all six: (a) technical feasibility of completing the asset for use or sale, (b) intent to complete and use or sell it, (c) ability to use or sell it, (d) probable future economic benefits, (e) adequate technical, financial and other resources to complete and use or sell it, and (f) ability to measure the attributable expenditure reliably.

**Punkt 18.5** bars capitalisation of internally generated brands, customer lists, start-up costs, training, advertising, reorganisation and internal goodwill. **Punkt 18.14** excludes selling, administration and other general overheads unless directly attributable, plus identified inefficiencies, operating losses before planned performance, and training; its kommentar lists what does belong — material and services, employee remuneration arising in the work, registration fees for a legal right, and amortisation of patents and licences used in the work. **Punkt 18.15** forbids bringing expenditure expensed in an earlier räkenskapsår back into the anskaffningsvärde.

BFNAR 2025:3 did **not** amend K3 chapter 18.

### The fond för utvecklingsutgifter

The requirement is in **ÅRL 4 kap 2 § andra stycket**, not 4 kap 7 §: "Första stycket gäller även utgifter för företagets eget utvecklingsarbete. För **aktiebolag och ekonomiska föreningar** gäller detta dock endast under förutsättning att motsvarande belopp överförs från fritt eget kapital till en fond för utvecklingsutgifter."

It binds **aktiebolag and ekonomiska föreningar** only, and **K3 punkt 18.3A** requires the transfer even where the company has an ansamlad förlust. **ÅRL 4 kap 7 §**: an aktiebolag may use the fund for a fondemission or nyemission, or to cover a loss per the adopted balansräkning where fritt eget kapital is insufficient. **ÅRL 4 kap 8 §**: on amortisation, impairment, disposal or scrapping the fund must be reduced correspondingly, by transfer back to fritt eget kapital. A K2 company never has this fund, because punkt 10.4 blocks the capitalisation.

The practical effect is that capitalised development reduces distributable equity krona for krona: a K3 SaaS company with 4 MSEK capitalised has 4 MSEK less utdelningsbart fritt eget kapital than its balance sheet total suggests.

### Entries

**K2 (and K3 kostnadsföringsmodellen):** nothing special. Salaries to **7210**/**7510**, consultants to **6556 Köpta tjänster avseende forskning och utveckling** or **6550**, cloud to **6540**. No asset, no fund.

**K3 aktiveringsmodellen**, capitalising 1 200 000 kr of own development in 2026 of which 900 000 is personnel, 200 000 other overheads and 100 000 material:

| Konto | Namn | Debet | Kredit |
|-------|------|-------|--------|
| 1012 | Balanserade utgifter för programvaror | 1 200 000 | |
| 3870 | Aktiverat arbete (personal) | | 900 000 |
| 3850 | Aktiverat arbete (omkostnader) | | 200 000 |
| 3840 | Aktiverat arbete (material) | | 100 000 |

Then the fund transfer, within eget kapital:

| Konto | Namn | Debet | Kredit |
|-------|------|-------|--------|
| 2091 | Balanserad vinst eller förlust | 1 200 000 | |
| 2089 | Fond för utvecklingsutgifter | | 1 200 000 |

Work still in progress at balansdagen sits on **1081 Pågående projekt för immateriella anläggningstillgångar** and is not amortised.

### Amortisation

**ÅRL 4 kap 4 § andra stycket**: "Om nyttjandeperioden för immateriella anläggningstillgångar som utgörs av utgifter för företagets eget utvecklingsarbete inte kan fastställas med en rimlig grad av säkerhet, **ska perioden anses uppgå till fem år**." This is a presumption when the life cannot be reliably determined, not a ceiling. K3 punkt 18.18 caps the life at the contractual or legal-rights period where the asset arises from such rights, and its kommentar adds that for assets not based on contract or legal rights a life longer than five years can only rarely be established, and only with supporting material. K3 punkt 18.20 presumes a residual value of zero; punkt 18.22 starts amortisation when the asset is available for use.

Five-year straight line on the example, per year:

| Konto | Namn | Debet | Kredit |
|-------|------|-------|--------|
| 7811 | Avskrivningar på balanserade utgifter | 240 000 | |
| 1019 | Ackumulerade avskrivningar på balanserade utgifter | | 240 000 |
| 2089 | Fond för utvecklingsutgifter | 240 000 | |
| 2091 | Balanserad vinst eller förlust | | 240 000 |

Impairment goes to **7710 Nedskrivningar av immateriella anläggningstillgångar** with the same release from **2089** per ÅRL 4 kap 8 §.

---

## 6. Development costs: tax

**IL 16 kap 9 §**: "Utgifter för forskning och utveckling som har eller kan antas få betydelse för den huvudsakliga näringsverksamheten eller verksamheten i övrigt ska dras av. Detta gäller även utgifter för att få information om sådan forskning och utveckling." The second stycke keeps the värdeminskningsavdrag rules applicable to such expenditure.

**16 kap 9 § widens what is deductible, not when.** It is what lets a company deduct, for example, contributions to research carried out by someone else in which it has a reasonable interest. It is not a periodisation rule. The Government's own statement of gällande rätt in the lagrådsremiss *Ett nytt skatteincitament för forskning och utveckling* (2026-08-13) is explicit: "För FoU-utgifter finns det ingen särskild periodiseringsregel vilket innebär att sådana utgifter behandlas på samma sätt som enligt god redovisningssed."

**IL 14 kap 2 §** therefore governs the timing: the result is computed enligt bokföringsmässiga grunder and expenditure is deducted in the beskattningsår it belongs to enligt god redovisningssed, unless something else is specifically prescribed.

| Framework | Accounting | Tax |
|-----------|-----------|-----|
| K2 | Expensed (punkt 10.4) | Deducted in the same year |
| K3 kostnadsföringsmodellen | Expensed (punkt 18.8) | Deducted in the same year |
| K3 aktiveringsmodellen | Capitalised, amortised over the nyttjandeperiod | Deduction follows the accounting amortisation |

So capitalising under K3 does **not** buy a deferred-tax asset or a skattemässig justering in INK2 from the capitalisation itself. The real cost of capitalising is the fond för utvecklingsutgifter locking up distributable equity; the real benefit is the reported result and equity.

**IL 18 kap 1 § andra stycket 1** treats as inventarier only "koncessioner, patent, licenser, varumärken, hyresrätter, goodwill och liknande rättigheter **som förvärvats från någon annan**". A self-developed intangible is therefore not an inventarium, and the 30- and 20-reglerna do not apply to it. A *purchased* software system or licence is an inventarium and follows räkenskapsenlig or restvärdesavskrivning — see `swedish-asset-accounting`.

---

## 7. FoU-avdrag

**The law moved.** Socialavgiftslagen 2 kap 29–31 §§ were repealed by SFS 2023:750. Since 2024-01-01 the relief is in **lagen (2023:747) om särskilt avdrag vid beräkning av arbetsgivaravgifter och allmän löneavgift för personer som arbetar med forskning eller utveckling**, which has not been amended. Any material citing SAL 2 kap 29–31 §§ is stale.

| Item | 2026 rule | Cite |
|------|-----------|------|
| Forskning | "systematiskt och kvalificerat arbete med att i kommersiellt syfte ta fram ny kunskap" | 3 § |
| Utveckling | "systematiskt och kvalificerat arbete med att i kommersiellt syfte använda **resultatet av forskning** för att utveckla nya varor, tjänster eller produktionsprocesser eller väsentligt förbättra redan existerande sådana" | 4 § |
| Time test | At least **half** of, and at least **15 hours** of, the person's actual working time in the calendar month | 7 § första stycket |
| Carry-over | The deduction may still be taken if the test was met in each of the **four preceding calendar months** — unless the reason it failed is that the person's duties changed | 7 § andra–tredje styckena |
| Deduction | **20 % of the avgiftsunderlag**, taken from arbetsgivaravgifter first | 8 § första stycket |
| Floor | The avgifter may not fall below the **ålderspensionsavgift**, 10,21 % | 8 §, SAL 2 kap 26 § |
| Cap | Combined deduction for all qualifying persons max **3 000 000 kr per calendar month** | 8 § första stycket |
| Group | Companies in the same koncern count as **one avgiftsskyldig**; the moderföretag takes the deduction first, the remainder going to subsidiaries in the order the parent decides | 8 § andra stycket |
| Over 67 | Excluded — only ålderspensionsavgift is payable on them anyway | 6 §, SAL 2 kap 27 § |

2026 rates: arbetsgivaravgifter **18,80 %** (SAL 2 kap 26 §, Lag 2025:1362) and allmän löneavgift **12,62 %** (lagen 1994:1920 3 §, Lag 2025:1360). The total is still 31,42 %, but the split moved from 19,80/11,62 in 2024–2025. The headroom above the 10,21 % floor is 21,21 percentage points, so a 20 % deduction is normally usable in full — but the floor can bind where another nedsättning already applies to the same person. See `swedish-payroll` for the AGI mechanics; Skatteverket's arbetsgivar- deklaration takes the underlag in **ruta 470** and the avdrag in **ruta 475**, filed every month the condition is met.

**Worked example.** Four developers qualify in a month; combined avgiftsunderlag 300 000 kr. Avgifter before the deduction 31,42 % × 300 000 = 94 260 kr; deduction 20 % × 300 000 = 60 000 kr; floor 10,21 % × 300 000 = 30 630 kr. Since 94 260 − 60 000 = 34 260 ≥ 30 630, the full deduction is available, and the 3 000 000 kr group cap is nowhere near.

| Konto | Namn | Debet | Kredit |
|-------|------|-------|--------|
| 7510 | Arbetsgivaravgifter | 34 260 | |
| 2731 | Avräkning lagstadgade sociala avgifter | | 34 260 |

**Does ordinary software development qualify? Usually not.** The requirement in 4 § is that the work uses *the result of research*. Skatteverket's public guidance states that research results must be a decisive precondition for the development work, and that the test exists to separate it from ordinary continuous development of an existing product; work on management, support, service, maintenance, quality assurance or marketing does not count as "kvalificerat". SOU 2025:3, the official review, found around sixty förvaltningsrätt and kammarrätt decisions on the relief with the deduction allowed in only two final judgments, and observed that "det i praktiken är svårt att få FoU-avdrag för mjukvaruutveckling", noting that agile working makes after-the-fact documentation harder and that writing new code is not in itself innovative in the required sense. There is no HFD precedent on the relief.

Advise a software client accordingly: claim only where there is documented work tied to a specific research result, keep per-person monthly time records against the 50 %/15-hour test, and expect to defend it.

### Proposals for 2027 — none of these is law

2026 is an election year. The budgetproposition för 2027 had **not** been presented as of 2026-09-17 and is due by 2026-11-12. Three Finansdepartementet proposals are at **lagrådsremiss** stage with no proposition and no riksdag decision. Treat all three as proposals only, and do not compute anything on them.

| Proposal | Stage and date | Content, proposed from 2027-01-01 |
|----------|----------------|------------------------------------|
| Indexering av taket i FoU-avdraget | Promemoria 2026-05-18, lagrådsremiss 2026-08-27 | Replaces the 3 000 000 kr monthly cap with **36 inkomstbasbelopp per calendar month**. At the 2026 ibb of 83 400 kr that is about 3 002 400 kr, i.e. the current cap made self-indexing |
| Skatteincitament för forskning och utveckling | SOU 2025:3, lagrådsremiss 2026-06-11 | New wording of 3, 4 and 7 §§ of lagen (2023:747): **the requirement that development build on research results is removed**, and the **15-hour test is scrapped** (the 50 % test and the four-month carry-over survive). New 9 §: Skatteverket must obtain an opinion from another authority where needed to judge whether work is FoU |
| Ett nytt skatteincitament för forskning och utveckling | Lagrådsremiss 2026-08-13 | New **IL 16 kap 9 a–9 b §§**: a voluntary **200 % förhöjt kostnadsavdrag** for avgiftspliktig remuneration to employees working on FoU in an EES state, on top of the ordinary deduction, tied to the 7 § time test. **9 b §** requires the uplift in the same beskattningsår as the underlying cost is deducted **or added to an asset's anskaffningsvärde** — so a company capitalising development wages would take the uplift immediately rather than over the amortisation |

The first of these would leave software companies roughly where they are. The second would be the material change: removing the "must build on research" requirement is precisely the condition that has defeated most software claims.

---

## 8. Personaloptioner

IL 11 a kap is titled "Särskilda bestämmelser om personaloptioner"; "kvalificerad personaloption" is the working term, not the statutory one. The chapter has been unchanged since Lag (2022:987); the 2021 expansion (Lag 2021:1161) applies to options acquired after 2021-12-31.

Where the conditions are met, the förmån "ska inte tas upp" as intäkt in inkomstslaget tjänst (11 a kap 5 §). Two consequences follow automatically: **no arbetsgivaravgifter** (SAL 2 kap 12 § 1 makes an ersättning avgiftsfri if it is skattefri enligt IL), and **no corporate deduction** (IL 16 kap 37 §: "Förmån av personaloption som inte ska tas upp som intäkt enligt 11 a kap. får inte dras av").

| Condition | § | 2026 content |
|-----------|---|--------------|
| Company | 2 § | Svenskt aktiebolag, or a foreign equivalent with fast driftställe in Sweden, resident in an EES state or a treaty state with an information-exchange article |
| Intjänandetid | 4 § | **Three years** from acquisition of the option |
| Exercise window | 5 § | Earliest **three** and at most **ten** years after acquisition, for an andel or a teckningsoption in the company or in a company that was in the same group at acquisition |
| Size | 6 § | In the räkenskapsår immediately preceding the year of acquisition: **medelantalet anställda och delägare som arbetar i företaget under 150**, and **nettoomsättning or balansomslutning at most 280 000 000 kr** |
| Ownership and listing | 7 § | Not 25 % or more of capital or votes controlled by public bodies; no share admitted to trading on a regulated market or equivalent |
| Excluded business | 8 § | During the intjänandetid the company must mainly carry on business other than banking or financing, insurance, coal or steel production, trading in land, property, commodities or financial instruments, long-term letting of premises or housing, or **legal advice, accounting or audit services** |
| Age | 9 § | Not more than **ten years** of activity after the end of the year activity began, with a look-back where 25 % or more of the business was acquired |
| Distress | 10 § | Not obliged to prepare a kontrollbalansräkning per ABL 25 kap 13 §, not in företagsrekonstruktion, not insolvent, not subject to a Commission state-aid recovery order |
| Cap per holder | 11 § | Value of all the holder's personaloptioner in the company at most **3 000 000 kr** at acquisition |
| Cap per company | 12 § | Combined value at most **75 000 000 kr** at acquisition |
| Valuation | 13 § | Value of the underlying andelar, from arm's-length transactions in the preceding twelve months; failing that, net assets per the latest adopted balansräkning; failing that, kvotvärde |
| Holder and hours | 14 § | Employee, or styrelseledamot/styrelsesuppleant, during the intjänandetid. An employee must work **at least 30 hours per week on average**; paid holiday and socially insured absence count as working time |
| Minimum pay, employee | 15 § | Tjänste-taxable remuneration from the company of at least **13 inkomstbasbelopp** over the intjänandetid, pro-rated for part-period employment. At the 2026 ibb of **83 400 kr** that is **1 084 200 kr** |
| Minimum pay, board member | 15 a § | At least **1,5 inkomstbasbelopp** — **125 100 kr** for 2026 |
| Which ibb | 15 b § | The ibb for the year the option is **acquired**. Kostnadsersättning and amounts taxed under IL 11 kap 45 § or 57 kap do not count |
| Related-party holding | 16 § | The holder together with närstående must not, in either of the two years before the year of acquisition or the earlier part of that year, control more than **5 %** of capital or votes |

Group application: 11 a kap 5 § andra stycket sets which conditions are tested for the group as a whole (6, 8, 11 and 12 §§ among them) and which per company (7, 9, 10 and 16 §§).

### Accounting

**From räkenskapsår beginning after 2025-12-31, a company that has granted an option programme may not apply K2 at all.** K2 punkt 1.1A g) (BFNAR 2025:2) bars "företag som under räkenskapsåret har förvärvat varor eller tjänster mot aktierelaterade ersättningar", and K3 punkt 26.2 defines aktierelaterade ersättningar as covering ersättningar to parties "inklusive anställda". ikraftträdandebestämmelse punkt 2 to BFNAR 2025:3 gives such a company relief from the punkt 35.1 limitation when it first applies K3 chapter 35. K2 has no equivalent of K3 chapter 26, so before FY2026 there were simply no K2 rules on the subject; from FY2026 the question is moot because K2 is closed to these companies.

Under **K3 chapter 26**: punkt 26.1 covers aktierelaterade ersättningar and the sociala avgifter attributable to them; punkt 26.5 recognises the goods or services when received, against **eget kapital** for equity-settled awards and a **skuld** for cash-settled ones, expensed where they do not qualify as an asset; punkterna 26.6–26.7 recognise immediately if vested at grant, otherwise over the intjänandeperiod; punkterna 26.9–26.11 measure employee services at the fair value of the equity instruments at the tilldelningstidpunkt, without later remeasurement, with punkt 26.13 giving the option valuation rules; punkt 26.20 accrues social charges the same way but remeasures that provision each balansdag — nil for a qualified personaloption, since there are no arbetsgivaravgifter; punkterna 26.21–26.27 are disclosures for större företag only.

So a K3 SaaS company with a qualified option programme carries a personnel cost in the resultaträkning against equity, no social charges, and no tax deduction — a permanent book-to-tax difference, not a temporary one.

### Reporting duty

**SFL 26 kap 19 b § första stycket 7**: the arbetsgivardeklaration must contain "uppgift om att en sådan personaloption som avses i 11 a kap. inkomstskattelagen har utnyttjats, om personaloptionen har förvärvats i den deklarationsskyldiges tjänst". In Skatteverket's AGI this is **ruta 059**, a tick box with no amount. If a condition fails, do not tick 059 — report the benefit's value in **ruta 012 Skattepliktiga förmåner utom bil och drivmedel** and pay arbetsgivaravgifter on it.

**SFL 22 kap 26 §** keeps a kontrolluppgift duty for the same event, but expressly disapplies it where the information "har redovisats eller skulle ha redovisats … i en arbetsgivardeklaration". A normal Swedish employer therefore files nothing beyond the monthly AGI. **SFL 34 kap 6 §** obliges the option holder to give the employer the information it needs, and **SFL 37 kap 13 §** lets Skatteverket require the region at NUTS 2 level and the verksamhetsområde at Nace group level afterwards.

Owner-side planning — 3:12, gränsbelopp, the interaction with löneuttag — is in `swedish-tax-planning`.

---

## 9. Typical cost questions

| Cost | Treatment |
|------|-----------|
| Cloud hosting and infrastructure (AWS, Azure, GCP) | Operating cost, **6540 IT-tjänster**. Never an asset: the company controls no resource. Foreign supplier ⇒ förvärvsbeskattning, section 4 |
| SaaS subscriptions used internally | Operating cost, **6540**; **5420 Programvaror** where the ledger separates licences |
| Purchased standard software licence, perpetual | Acquired intangible. Capitalise if the value and useful life justify it; for tax it is an inventarium under IL 18 kap 1 § andra stycket 1. See `swedish-asset-accounting` |
| Purchased framework or library bought to be built into the company's own product | Pulled into the self-developed asset. K2 punkt 10.4 andra stycket blocks capitalisation entirely; K3 punkt 18.13A includes it in the anskaffningsvärde |
| Subcontracted developers abroad building the company's own product | K2: cost. K3 aktiveringsmodellen: included in the anskaffningsvärde per K3 punkt 18.14's kommentar. VAT: förvärvsbeskattning. Check F-skatt and, for individuals, whether it is really an employment — `swedish-payroll` |
| Subcontracted developers abroad building for a customer | Cost of the uppdrag. Never capitalised as an intangible |
| Domain names, SSL certificates | Operating cost, **6540** or **6230 Datakommunikation**. A domain is rarely of betydande värde for kommande år in the ÅRL 4 kap 2 § sense |
| AI API usage (per-token inference) | Operating cost, **6540**, in the period consumed. Prepaid credits are a förutbetald kostnad on **1790** until consumed. Foreign supplier ⇒ förvärvsbeskattning |
| Model training runs for the company's own product | Same analysis as any development cost: K2 expense, K3 per punkt 18.12 if the six conditions are met and the work is in the development rather than the research phase |
| Open-source sponsorship with no counter-performance | Gåva, **6993 Lämnade bidrag och gåvor**, not deductible. If the company receives something identifiable — logo placement, a support agreement, priority fixes — it is a deductible cost under IL 16 kap 1 §; document what was received |
| Internally built marketing site, brand, customer list | Never capitalised. K2 punkt 10.4; K3 punkt 18.5 lists internally generated brands, customer lists, advertising and start-up costs as always expensed |
| Recruitment and onboarding of developers | Cost. K3 punkt 18.14 c) excludes training costs from the anskaffningsvärde |

---

## 10. Ask the user

1. **K2 or K3, and for which räkenskapsår?** An option programme closes K2 from FY2026 (K2 punkt 1.1A g).
2. **Under K3, aktiveringsmodellen or kostnadsföringsmodellen** — and is the choice applied to all internally generated intangibles?
3. **Where is the research/development boundary drawn**, and is it documented per project and per month?
4. **Does the company claim FoU-avdrag?** Ask for the monthly time records against the 50 %/15-hour test and the documented link to a research result.
5. **Is the company established anywhere outside Sweden?** A fixed establishment in another EU country disables ML 6 kap 62 § and forces OSS or local registration from the first krona.
6. **What does the checkout store** per transaction: VIES response, two items of 24f evidence, the running 99 680 kr total?
7. **Is any part of the offering human-delivered** — implementation, training, consultancy? That part is not an electronically supplied service.
8. **For an option programme**, the grant date, the company's size and age at grant, the holder's hours and cash remuneration over the three-year intjänandetid, and the related-party holdings in the two preceding years.

---

## 11. Sources

All checked 2026-09-17. Primary sources only.

- **ML (2023:200)**, consolidated t.o.m. SFS 2026:1025, riksdagen.se — 6 kap 3 §, 33 §, 35 §, 56 §, 57 §, 58–59 §§, 62–65 §§; 17 kap 24 §; 22 kap 35 §, 43 §, 44 §.
- **IL (1999:1229)**, consolidated t.o.m. SFS 2026:1393, riksdagen.se — 11 a kap 1–18 §§ (latest amendments Lag 2021:1161 and Lag 2022:987); 14 kap 2 §; 16 kap 9 §; 16 kap 37 §; 18 kap 1 §.
- **SFL (2011:1244)**, consolidated t.o.m. SFS 2026:1305, riksdagen.se — 22 kap 26 § (Lag 2021:1163); 26 kap 19 b §; 34 kap 6 §; 35 kap 2 §, 3 §, 9 §; 37 kap 13 § (Lag 2024:1157).
- **SAL (2000:980)**, riksdagen.se — 2 kap 12 §, 26 § (Lag 2025:1362), 27 §; 2 kap 29–31 §§ repealed by **SFS 2023:750**.
- **Lagen (2023:747)** om särskilt avdrag … forskning eller utveckling, riksdagen.se — 3–8 §§. No amendments as at 2026-09-17.
- **Lagen (1994:1920)** om allmän löneavgift, riksdagen.se — 3 § (Lag 2025:1360).
- **Förordning (2025:1002)** om inkomstbasbelopp för år 2026 — 1 §: **83 400 kronor**.
- **ÅRL (1995:1554)**, riksdagen.se — 4 kap 2 §, 4 §, 7 §, 8 §.
- **BFN, K2 vägledning**, consolidated for räkenskapsår beginning after 2025-12-31 (BFNAR 2016:10 as amended by **BFNAR 2025:2**), `bfn.se/wp-content/uploads/vl16-10-k2ar-kons2025.pdf` — punkterna 1.1A, 10.4.
- **BFN, K3 vägledning**, consolidated for räkenskapsår beginning after 2025-12-31 (BFNAR 2012:1 as amended by **BFNAR 2025:3** and **BFNAR 2025:4**), `bfn.se/wp-content/uploads/vl12-1-k3-kons20251215.pdf` — punkterna 18.3A, 18.5, 18.7–18.15, 18.18–18.22, 18.30, 26.1–26.13, 26.20, 26.21–26.27.
- **Council Implementing Regulation (EU) 282/2011**, as amended by **1042/2013** and **2017/2459** — art. 7 and Annex I, art. 18, art. 24a, 24b, 24d, 24f.
- **BAS 2026 v1.1**, `bas.se/wp-content/uploads/2026/04/BAS_kontoplan_2026_v2.xlsx` — every account number and name above, including the "#" markers on 1010–1019 and 2089.
- **Skatteverket (www.skatteverket.se)** — pages on forskningsavdrag (rutor 470/475), på försäljning till andra EU-länder and VIES, OSS deklaration och betalning, ifyllnad av momsdeklarationen (fält 05, 10, 39, 40) and arbetsgivardeklarationen (rutor 059, 012).
- **SOU 2025:3** *Skatteincitament för forskning och utveckling* and Finansdepartementet lagrådsremisser of 2026-06-11, 2026-08-13 and 2026-08-27, regeringen.se — used only for the Government's statement of gällande rätt on IL 16 kap 9 §, the case-law findings on software, and the 2027 proposals in section 7, all labelled as proposals.

Not reached: Skatteverket's rättslig vägledning (www4.skatteverket.se) rejects automated requests. The point that would benefit from it — the classification of a bundled SaaS-plus-implementation supply — is flagged "Osäkert" in section 3.
