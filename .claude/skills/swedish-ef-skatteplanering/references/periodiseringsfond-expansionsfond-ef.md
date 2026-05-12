# Periodiseringsfond and Expansionsfond — EF Perspective

## Legal basis

- IL 30 kap — Periodiseringsfond (P-fond)
- IL 34 kap — Expansionsfond
- BFNAR 2006:1 — K1 (förbjuder bokföring av P-fond/expansionsfond för EF)

For an AB-perspective on periodiseringsfond, see `swedish-tax-planning/references/periodiseringsfond.md`. The mechanics differ enough that they should be treated as separate systems.

## Quick comparison: P-fond AB vs P-fond EF

| Property | AB | EF |
|---|---|---|
| Max avsättning | 25% av skattemässigt överskott | **30%** av skattemässigt överskott |
| Booked in räkenskaperna? | YES (8811/21xx) — formellt samband | **NO** (NE-bilaga only) |
| Schablonintäkt | YES (SLR × IB av P-fonder, min 0,5%) | **NO** |
| Antal parallella fonder | 6 | 6 |
| Maximal carry | 6 år (FIFO återföring senast år 7) | 6 år (FIFO) |
| Uppräkning på återföring (pre-2019) | YES (6%) | No equivalent |

The most important EF-specific facts:
1. **30%** (not 25%) — markedly more aggressive than AB
2. **NO schablonintäkt** — the deferred tax sits genuinely 0%-räntefri for 6 years
3. **NEVER booked in räkenskaperna** — only on NE-bilagan. Bokföring av P-fond gör avdraget ogiltigt för EF (omvänt mot AB!)

## Periodiseringsfond EF mechanics

### Avsättning

- Max **30% of resultat efter räntefördelning, efter återföring av tidigare P-fond, och före egen P-fond avsättning och ändring av expansionsfond**
- Each year creates its own fund (e.g., "periodiseringsfond 2025" — separately tracked)
- Up to 6 fonder samtidigt

### Återföring

- Senast **år 7** (= 6:e året efter avsättningsåret) **måste** äldsta fond återföras
- Återföringen är frivillig in earlier years
- Tvingande återföring av samtliga fonder vid:
  - Verksamhetens upphörande
  - Skattskyldighetens upphörande vid utvandring utanför EU/EES
  - Konkurs
  - A-kassa (om man slutar för att få a-kasseersättning, då återförs)

Vid flytt till EU/EES-land kan kontinuitet medges (EU-rätten).

### Reporting on NE

- Ruta **R34** — Återföring av periodiseringsfond
- Ruta **R35** — Avsättning till periodiseringsfond
- Upplysning U1 in förenklat årsbokslut: sammanlagda P-fonder vid årets slut

### Worked example (PDF "Renata")

A coronial example of poor planning: Renata builds 6 × 100 000 kr P-fond over six years, then realizes she's tomma på pengar in retirement and måste likvidera verksamheten. Hon måste återföra 600 000 kr, with tax ~240 000 kr, when hon already har spent the cash flow. Lesson: **always reserve 30–35% of P-fond ingång for the eventual tax bill**, e.g., on a separate bankkonto.

Renata's recovery strategy: continue verksamheten in liten skala, do partial återföring + new avsättning each year (200 000 kr återförs, 30k ny avsättning → 170 000 kr beskattas årligen), spreading the bill over years 7–13.

### Combining with räntefördelning at nedläggning

Sparat fördelningsbelopp (positiv räntefördelning som sparats) may be used at nedläggning to offset återförd P-fond AND expansionsfond. This is the **largest single planning opportunity** for an EF closing down — see worked example "Lennart" in [[rantefordelning-planning]].

### Tillfällig regel 2019 (COVID)

For inkomstår 2019, 100% av vinsten fick avsättas till P-fond (one-time relief). Possible to retroactively use via omprövning of 2019 deklaration within 6 years (= until inkomstår 2025 deklaration filing window) if not already done.

### SOU 2020:50 proposal (not enacted)

- Höjd från 30% till **40%**
- Förlängd carry från 6 till **10 år**
- P-fond äldre than 6 år FÅR INTE överföras till AB vid ombildning (would be återförda direkt at takeover)

## Expansionsfond mechanics

### Purpose

Expansionsfond gives EF the equivalent of an AB's ability to retain earnings at corporate-tax-rate. The fonderade vinsten beskattas with **20,6% expansionsfondsskatt** (same as bolagsskatt) and may be reinvested in verksamheten utan ytterligare beskattning. At återföring, the 20,6% credits back against that year's tax (so the net effect is just regular inkomstskatt on the återförda beloppet).

### Avsättning rules

- Skatt: **20,6%** expansionsfondsskatt
- Tak: expansionsfonden får vara **högst 128,21% av kapitalunderlaget** vid årets utgång
- Ökning av expansionsfond may NOT cause underskott in NV
- Ökning beräknas på resultat efter räntefördelning, efter ändring av P-fond, och före ändring expansionsfond

### Kapitalunderlag for expansionsfond

Conceptually identical to kapitalunderlag for räntefördelning, with one key difference:
- **Räntefördelning**: kapitalunderlag at *föregående* års utgång (= ingång aktuella året)
- **Expansionsfond**: kapitalunderlag at *aktuella* årets utgång

Practical tip: the year 2 expansionsfond kapitalunderlag will be similar to the year 3 räntefördelning kapitalunderlag, so the same beräkning may be reused with a one-year offset.

### Återföring

- May happen voluntarily at any point
- Vid återföring ökar skattemässig inkomst, men 20,6% expansionsfondsskatt återbetalas
- Vid förlustår: återföringen kan vara **skattefri** (the 20,6% återbetalas och resultatet blir 0 eller negativt → no extra inkomstskatt)
- Vid kapitalunderlags-minskning under fondens nivå → tvingande återföring (delvis)
- Vid företagets upphörande → all återförs samma år

### NE-bilaga fields

- Ruta **R36** — Återföring av expansionsfond i NV
- Ruta **R37** — Ökning av expansionsfond
- Sid 2 expansionsfondsbilaga **2196** for kapitalunderlagsberäkning (separately filed)
- Upplysning U2 in förenklat årsbokslut: expansionsfond vid årets slut

### Worked example (PDF "Georg")

50 år, aktiv NV, vinst 800 000 kr, kapitalunderlagstak 400 000 kr för expansionsfond.

Without expansionsfond:
- Skatt och egenavgifter på 800 000 kr ≈ 236 000 kr (≈ 29,5%)

With expansionsfond avsättning 100 000 kr:
- Inkomst beskattad som NV: 700 000 kr → skatt och egenavgifter 189 492 kr
- Expansionsfondsskatt: 20,6% × 100 000 = 20 600 kr
- Total: 210 092 kr
- **Sparat: 25 908 kr** at the cost of setting aside 100 000 kr (returnable later)

### Carry-forward of skatt

The 20,6% expansionsfondsskatt is paid in the year of avsättning. **It is NOT a deferral of inkomstskatt** — it's a final-tax on the avsättning. At återföring, the 20,6% credits back.

### When expansionsfond is *not* worth it

Same logic as räntefördelning:
- Pensionärer (10,21% egenavgifter): low marginal NV tax may already be UNDER 20,6%
- För inkomster under brytpunkten, marginalskatten kan vara så låg att expansionsfondsskatten 20,6% är högre

**Heuristik**: only use expansionsfond when *current year* marginal skatt inkl egenavgifter > 20,6% AND *expected future return year* marginal skatt < current year marginal skatt.

### Två-stegs beskattning vid utlöp

If you build up expansionsfond at 20,6% and later take ut pengarna (instead of reinvesting):
- Recovery → 42% (statlig + kommunal) − 20,6% = **21,4% extra skatt + egenavgifter** at återföringsåret

So total skatt mot vad det vore som direkt löneuttag är samma, **bara om utbetalningen sker över brytpunkten i återföringsåret**. Under brytpunkten the math may favor expansionsfond (cheap retention) or löneuttag (cheap immediate).

### Tvingande återföring

- Vid upphörande av verksamheten (all of it)
- Vid utvandring till icke-EES-land
- Vid konkurs
- Vid kapitalunderlagsminskning under fondens nivå
- Vid byte av företagsform: kan överföras till AB *under förutsättning att samtliga realtillgångar överförs* OCH att tillgångar med skattemässigt värde ≥ 79,4% av expansionsfondens belopp överförs (motsvarar 100% − 20,6%)

### SOU 2020:50 proposal (not enacted)

- Expansionsfond föreslås **slopad** (avskaffad)
- Befintliga fonder återförs med minst 10% per år under högst 10 år
- Återföring beläggs med inkomstskatt men 20,6% återbetalas
- Höjd P-fond (30 → 40%) som kompensation
- Worth flagging as "watch this space"

## Sjukpenninggrundande and pensionsgrundande inkomst effects

This is the most subtle interaction. From the PDF (Sjukpenning section):

> *"Men när Försäkringskassan beräknar din sjukpenninggrundande inkomst (SGI) och din föräldrapenninggrundande inkomst bortser man från de skattemässiga dispositionerna periodiseringsfond och expansionsfond."*

| Disposition | SGI effekt | PGI effekt |
|---|---|---|
| Avsättning P-fond | INGEN (FK adjusts back) | Sänker PGI |
| Återföring P-fond | INGEN (FK adjusts back) | Höjer PGI |
| Avsättning expansionsfond | INGEN | Sänker PGI |
| Återföring expansionsfond | INGEN | Höjer PGI |
| Räntefördelning | Påverkar (positiv sänker, negativ höjer) | Påverkar |
| Avskrivning på inventarier | Påverkar (höjd avskrivning sänker SGI och PGI) | Påverkar |
| Mindre schablonavdrag egenavgifter | Höjer (paradoxalt) | Höjer |

**Implication**: a näringsidkare with ojämn inkomst may use P-fond strategically to **smooth out PGI** (höja den i låga år, sänka i höga år) but NOT to smooth SGI (which Försäkringskassan adjusts back).

Pensionsgrundande inkomst tak: **7,5 inkomstbasbelopp** (604 500 kr 2025). Income above this gives no extra pension but full egenavgifter. Use P-fond to keep PGI just under taket — see worked example "Laura":
- Vinst 800 000 kr, after 25% schablonavdrag egenavgifter = 600 000 kr (nettoinkomst, would exceed PGI-tak 511 500 in 2021)
- Avsättning 118 000 kr till P-fond → nettoinkomst sjunker till 682 000 → 511 500 → matches PGI-tak exactly
- Future låginkomstår: lös upp P-fond för högre PGI då

## Bokföringsförbudet (K1 / BFNAR 2006:1)

EF must **NOT** book P-fond or expansionsfond in räkenskaperna — only as upplysning U1/U2 in förenklat årsbokslut, and via NE-bilagan. This is the **opposite** of AB (which MUST book P-fond).

The reason: K1 is designed to keep redovisning aligned with real ekonomisk ställning, not skattemässig disposition. Latent skatteskuld is disclosed via U-poster, not booked.

BAS 2018 Förenklat årsbokslut nevertheless has accounts available for those who *want* to track (2080 Periodiseringsfonder, 2050 Avsättning till expansionsfond, 2060 Ersättningsfond) — but they are for **informationssyfte only**, must not be debited/krediterad mot resultatkonton.

For ersättningsfond, the situation is different: see [[ersattningsfond]].

## Interactions with each other

P-fond and expansionsfond are computed **in a specific order**:

1. Compute skattemässigt resultat (R11 + R12–R26 justeringar = R31 inkomst före räntefördelning)
2. Apply **räntefördelning** (R30) → result becomes inkomst efter räntefördelning
3. Apply **återföring av P-fond** (R34) → increase result
4. Apply **återföring av expansionsfond** (R36) → increase result
5. Compute **30% cap for new P-fond avsättning** = 30% × (result after steps 1–4)
6. Apply **avsättning ny P-fond** (R35) → decrease result
7. Compute **expansionsfond ökning room** = result after step 6 (may not cause underskott)
8. Apply **ökning expansionsfond** (R37) → decrease result
9. Final: inkomst före schablonavdrag (R38)

The exact ordering is enforced by NE-blankett layout. Note that the result *after* P-fond avsättning is the cap for expansionsfond ökning, so the two tools partly compete (every kr more in P-fond is one kr less expansionsfond room).

### SOU 2020:50 proposes reversing the order — räntefördelning would be applied *last*, after P-fond. Not enacted.

## Common pitfalls

1. **Booking P-fond in EF räkenskaperna** — invaliderar avdraget (oppositional to AB where it's required)
2. **Forgetting tvingande återföring** at upphörande — Skatteverket återför automatiskt and may apply skattetillägg
3. **Calculating expansionsfond tak using prior year kapitalunderlag** — must be *current year's* utgång, not prior year's
4. **Misunderstanding 128,21% multiplier** — it represents 1 / (1 − 0,206) = 100 / 79,4 = the gross-up factor that ensures the net-of-tax expansionsfond equals exactly kapitalunderlaget. Equivalent statement: expansionsfond *net of skatt* ≤ 100% av kapitalunderlag.
5. **Skipping U1/U2 upplysning** in förenklat årsbokslut — formal compliance requirement under BFNAR 2006:1
6. **Forgetting expansionsfond may NOT cause underskott** — software should clip ökning at the level that leaves NV result ≥ 0

## Recommended planning sequence per inkomstår

1. Compute provisional resultat
2. Compute kapitalunderlag for räntefördelning (ingång) and expansionsfond (utgång)
3. Decide whether positiv räntefördelning is net beneficial (see [[rantefordelning-planning]] decision tree)
4. Decide P-fond avsättning to:
   - Hit PGI tak (7,5 IBB ≈ 511 500 / 604 500 depending on year)
   - Reserve for known future förlustår or låginkomstår
5. Decide expansionsfond ökning to:
   - Retain working capital for verksamheten
   - Lower current marginal skatt below brytpunkten
6. Sanity-check: total egenavgifter underlag still > 40 000 kr to qualify for nedsättning 7,5%
7. Compute schablonavdrag egenavgifter (R43) and submit

See also [[ackumulerad-inkomst]] for handling the upphörande year återföring lump sum, [[egenavgifter-sgi-pgi-jsa]] for nedsättning rules, and [[ef-vs-ab-breakeven]] for the comparison with corporate periodiseringsfond.
