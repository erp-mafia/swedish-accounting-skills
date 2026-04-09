# SIE4 File Format Reference

SIE (Standard Import Export) is the Swedish standard for exchanging accounting data between systems. SIE4 is the current version used in practice.

## Table of Contents
1. SIE versions overview
2. SIE4 file structure
3. Record types (poster)
4. Mandatory vs optional fields
5. Character encoding and formatting
6. Implementation notes
7. Validation rules

---

## 1. SIE versions overview

| Version | Content | Use case |
|---|---|---|
| SIE1 | Yearly balances | Simple balance transfer |
| SIE2 | Periodic balances | Periodic balance transfer |
| SIE3 | Object balances | Dimensional balances |
| SIE4 | Full transaction data | Complete bokföring export/import |
| SIE4E | SIE4 + dimensions | Extended with kostnadsställe etc. |

SIE4 is the workhorse. It contains the complete bokföring: kontoplan, verifikationer, and all transactions. Use SIE4 for import/export of full bokföring data.

## 2. SIE4 file structure

A SIE4 file is a plain text file with records, one per line. Each record starts with a # tag.

### File layout (order matters)
```
#FLAGGA 0
#FORMAT PC8
#SIETYP 4
#PROGRAM "ProgramName" "Version"
#GEN datum sign
#FNR företagsnummer
#ORGNR organisationsnummer
#FNAMN "Företagsnamn"
#RAR 0 start slut          (current räkenskapsår)
#RAR -1 start slut         (previous räkenskapsår)
#KPTYP BAS2024             (kontoplantyp)
#KONTO kontonr "kontonamn"
#SRU kontonr srukod
#IB 0 kontonr belopp       (ingående balans current year)
#UB 0 kontonr belopp       (utgående balans current year)
#UB -1 kontonr belopp      (utgående balans previous year)
#RES 0 kontonr belopp      (resultat current year)
#VER serie vernr verdatum vertext regdatum sign
{
    #TRANS kontonr {} belopp transdat transtext kvantitet sign
    #TRANS kontonr {} belopp transdat transtext kvantitet sign
}
```

## 3. Record types (poster)

### Header records
| Tag | Description | Required |
|---|---|---|
| #FLAGGA | 0 = not read, 1 = read | Yes |
| #FORMAT | Character encoding (PC8 = CP437) | Yes |
| #SIETYP | SIE version (4 for SIE4) | Yes |
| #PROGRAM | Software name and version | Yes |
| #GEN | Generation date and user signature | Yes |
| #FNR | Company number (internal) | No |
| #ORGNR | Organisationsnummer | Yes |
| #FNAMN | Company name | Yes |
| #ADRESS | Company address | No |
| #RAR | Räkenskapsår period (0 = current, -1 = previous) | Yes |
| #TAXAR | Taxeringsår | No |
| #KPTYP | Kontoplan type (e.g., BAS2024) | Yes |
| #VALUTA | Currency (SEK default) | No |

### Account records
| Tag | Description |
|---|---|
| #KONTO | Account number and name |
| #KTYP | Account type (T=tillgång, S=skuld, K=kostnad, I=intäkt) |
| #SRU | SRU mapping (for tax declaration) |
| #ENHET | Unit for account |

### Balance records
| Tag | Description |
|---|---|
| #IB | Ingående balans (opening balance) |
| #UB | Utgående balans (closing balance) |
| #OIB | Object ingående balans |
| #OUB | Object utgående balans |
| #RES | Resultat (P&L account balance) |

### Transaction records
| Tag | Description |
|---|---|
| #VER | Verifikation header |
| #TRANS | Transaction line within a verifikation |
| #RTRANS | Reversed transaction (rättelse) |
| #BTRANS | Added transaction (tillägg) |

### Dimension records (SIE4E)
| Tag | Description |
|---|---|
| #DIM | Dimension definition |
| #UNDERDIM | Sub-dimension |
| #OBJEKT | Object within a dimension |

## 4. Mandatory vs optional

### Minimum valid SIE4 file must have:
1. #FLAGGA
2. #FORMAT
3. #SIETYP
4. #PROGRAM
5. #GEN
6. #ORGNR
7. #FNAMN
8. #RAR (at least current year)
9. #KPTYP
10. #KONTO (all used accounts)
11. #VER + #TRANS (all verifikationer and transactions)

### Balance records
- #IB and #UB are expected but some systems omit them
- #RES records summarize resultaträkning accounts
- Best practice: always include IB/UB for balansräkning accounts and RES for resultaträkning accounts

## 5. Character encoding and formatting

### Encoding
- Traditional: PC8 (Code Page 437) declared with #FORMAT PC8
- Modern alternative: UTF-8, no #FORMAT tag or custom declaration
- Most Swedish systems still expect PC8. If you produce UTF-8, document it clearly.
- When importing: detect encoding, handle both

### Number format
- Decimal separator: period (.)
- Negative numbers: minus sign prefix
- No thousands separator
- Amounts in full currency units (SEK, not öre)

### Date format
- YYYYMMDD (no separators)
- Example: 20260401

### String quoting
- Strings containing spaces must be enclosed in double quotes
- Empty strings: ""
- Escape double quotes inside strings with backslash: \"

### Curly braces
- {} denotes an empty object list (used in #TRANS when no dimension objects)
- {1 "100" 2 "PROJ1"} for dimension objects

## 6. Implementation notes

### Producing SIE4
1. Export all verifikationer for the räkenskapsår
2. Include all accounts in the kontoplan that have been used
3. Calculate IB (from previous year's UB or from opening balances)
4. Calculate UB and RES from transactions
5. Ensure verifikationer are complete (debits = credits within each #VER block)
6. Set #FLAGGA to 0

### Consuming SIE4
1. Parse header to get company info and period
2. Build kontoplan from #KONTO records
3. Import balances from #IB/#UB/#RES
4. Import verifikationer and transactions
5. Validate: sum of all #TRANS within each #VER must be 0 (balanced)
6. Handle encoding conversion if needed

### Common pitfalls
- Forgetting to handle PC8 encoding (Swedish characters å, ä, ö)
- Not validating that verifikationer balance (sum of TRANS = 0)
- Assuming date fields are always populated (some are optional)
- Not handling #RTRANS and #BTRANS (corrections and additions to existing verifikationer)
- Missing #SRU codes (needed for tax declaration mapping)

## 7. Validation rules

### Per verifikation (#VER block)
- Sum of all #TRANS debit amounts must equal sum of credit amounts (i.e., total nets to 0)
- Verifikationsnummer must be unique within its serie
- Verifikationsdatum must fall within the declared #RAR period

### Per file
- All account numbers in #TRANS must have a corresponding #KONTO record
- #IB for year 0 should match #UB for year -1 (if both present)
- #ORGNR should be a valid Swedish organisationsnummer (10 digits, Luhn check on last digit)

### SRU mapping
SRU (Standardiserat RäkenskapsUtdrag) codes map BAS accounts to positions in the tax declaration (INK2, INK4, etc.). Your system should maintain SRU mappings and include them in SIE exports. This enables automatic population of tax forms.
