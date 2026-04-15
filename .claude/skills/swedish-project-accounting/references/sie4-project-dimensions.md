# SIE4 Project Dimensions

## Table of contents

1. Dimension system overview
2. Record types for dimensions
3. Transaction encoding with objects
4. Object balances and budgets
5. Import/export considerations
6. Mapping to Fortnox/Visma/Bokio

---

## 1. Dimension system overview

SIE4 (Version 4B, 2008-09-30) provides a standardized encoding of dimensional data through reserved and user-defined dimensions.

### Reserved dimensions

| Dim # | Name | Multi-year | Notes |
|-------|------|-----------|-------|
| 1 | Kostnadsställe/Resultatenhet | No (resets annually) | Most commonly used |
| 2 | Kostnadsbärare | No | Sub-dimension of 1 (declared with #UNDERDIM) |
| 3-5 | Reserved | - | Not used in practice |
| 6 | Projekt | Yes (accumulates across years) | Second most common |
| 7 | Anställd | - | Employee tracking |
| 8 | Kund | - | Customer tracking |
| 9 | Leverantör | - | Supplier tracking |
| 10 | Faktura | - | Invoice tracking |
| 11-19 | Reserved | - | For future use |
| 20+ | Freely available | User-defined | Custom dimensions |

Dimensions using reserved numbers (1-19) need not be declared with #DIM. Non-reserved dimensions (20+) must be explicitly declared.

---

## 2. Record types for dimensions

### #DIM -- Declare a dimension

Syntax: `#DIM dimension_no "name"`

```
#DIM 6 "Projekt"
#DIM 1 "Kostnadsställe"
```

Reserved dimensions don't need this declaration but it is recommended for clarity.

### #UNDERDIM -- Declare a sub-dimension

Syntax: `#UNDERDIM dimension_no "name" parent_dimension_no`

```
#UNDERDIM 2 "Kostnadsbärare" 1
```

Dimension 2 is a sub-dimension of dimension 1. Each object in dimension 2 belongs to exactly one object in dimension 1.

### #OBJEKT -- Declare an object within a dimension

Syntax: `#OBJEKT dimension_no "object_no" "object_name"`

```
#OBJEKT 6 "P2026-001" "Customer Project Alpha"
#OBJEKT 6 "P2026-002" "Internal R&D Sprint 4"
#OBJEKT 1 "100" "Stockholm Office"
#OBJEKT 1 "200" "Gothenburg Branch"
```

Object numbers are strings (quoted). They can contain alphanumeric characters and hyphens. Maximum length varies by importing system but 20 characters is safe.

---

## 3. Transaction encoding with objects

### #TRANS with object list

Objects are attached to transaction lines via an object list in braces `{}`. The object list contains pairs of `dimension_no "object_no"`.

Syntax: `#TRANS account_no {dim_no "obj_no" dim_no "obj_no" ...} amount [transdate] [transtext] [quantity] [sign]`

### Examples

Single project tag:
```
#TRANS 3041 {6 "P2026-001"} -100000.00
```

Multiple dimensions (project + cost center):
```
#TRANS 3041 {1 "100" 6 "P2026-001"} -100000.00
```

No dimensional tags (empty braces):
```
#TRANS 1510 {} 125000.00
```

### Complete verification example

A consulting invoice for 100,000 SEK (25% moms) on project P2026-001, cost center 100:

```
#VER A 101 20260115 "Konsultarvode Projekt Alpha"
{
  #TRANS 1510 {} 125000.00
  #TRANS 2611 {} -25000.00
  #TRANS 3041 {1 "100" 6 "P2026-001"} -100000.00
}
```

The receivable (1510) and VAT liability (2611) carry no project tags. Only the revenue account (3041) is dimensionally tagged.

### WIP adjustment example (successiv vinstavräkning)

```
#VER E 45 20261231 "Upparbetad ej fakturerad Q4"
{
  #TRANS 1620 {6 "P2026-001"} 200000.00
  #TRANS 3041 {6 "P2026-001"} -200000.00
}
```

### WIP capitalization example (alternativregeln)

```
#VER E 46 20261231 "Pågående arbete period 12"
{
  #TRANS 1470 {6 "P2026-003"} 350000.00
  #TRANS 4970 {6 "P2026-003"} -350000.00
}
```

---

## 4. Object balances and budgets

### #OIB -- Object opening balance

Syntax: `#OIB year_index account_no {dim_no "obj_no"} amount`

```
#OIB 0 1470 {6 "P2026-001"} 450000.00
#OIB 0 1620 {6 "P2026-002"} 85000.00
```

Year index 0 = current year, -1 = previous year.

### #OUB -- Object closing balance

Syntax: `#OUB year_index account_no {dim_no "obj_no"} amount`

```
#OUB 0 1470 {6 "P2026-001"} 580000.00
```

### #PSALDO -- Period object balance

Syntax: `#PSALDO year_index period account_no {dim_no "obj_no"} amount`

```
#PSALDO 0 202601 4010 {6 "P2026-001"} 49655.00
#PSALDO 0 202601 3041 {6 "P2026-001"} -125000.00
```

### #PBUDGET -- Period object budget

Syntax: `#PBUDGET year_index period account_no {dim_no "obj_no"} amount`

```
#PBUDGET 0 202601 4010 {6 "P2026-001"} 55000.00
```

Budget data enables budget vs actual comparison per project.

---

## 5. Import/export considerations

### SIE Type 4E (export, .SE files)

- All verifications with full object specifications are included
- #DIM and #OBJEKT declarations are recommended
- #KONTO declarations should cover all accounts used
- Objects referenced in transactions should all have corresponding #OBJEKT records

### SIE Type 4I (import, .SI files)

- Declarations are optional but recommended
- Transactions referencing undeclared objects: behavior varies by system
  - Fortnox: auto-creates the object
  - Visma: rejects the import with an error
  - BL Administration: prompts the user
- Best practice: always include #OBJEKT declarations for all referenced objects

### Encoding considerations

SIE files use CP437 encoding by default (#FLAGGA 0). UTF-8 is indicated by #FLAGGA 1. Project names with å/ä/ö must be encoded correctly. See the swedish-sie-import-export skill for encoding details.

### Multi-dimensional transactions

A single #TRANS line can carry objects from multiple dimensions simultaneously. The object list is unordered (dimension numbers identify which dimension each object belongs to). Parser implementation should handle:

- Zero objects: `{}`
- Single dimension: `{6 "P001"}`
- Multiple dimensions: `{1 "100" 6 "P001"}`
- Same dimension appearing only once (duplicates are invalid)

---

## 6. Mapping to Fortnox/Visma/Bokio

### Fortnox

Fortnox exposes projects via `/3/projects/{ProjectNumber}` in its API.

Project properties:
- ProjectNumber (string, user-assigned)
- Description
- Status: ONGOING or COMPLETED
- StartDate, EndDate
- ProjectLeader
- ContactPerson

Voucher rows carry independent `Project` and `CostCenter` string fields. Both are optional per row. The VoucherRow object also has `CostCenterSettings` and `ProjectSettings` properties per account: ALLOWED, MANDATORY, or NOT_ALLOWED.

SIE mapping: Project → dimension 6, CostCenter → dimension 1. Direct and unambiguous.

Limitation: voucher search in Fortnox API only indexes header-level project tags, not row-level. A voucher with project P001 on individual rows but no header-level project will not appear in project-filtered searches.

### Visma

Visma uses renamable Objekt 1 and Objekt 2 types. The **Flerårigt** flag determines behavior:
- Flerårigt = true: balances accumulate across fiscal years (project behavior)
- Flerårigt = false: balances reset annually (cost center behavior)

Visma.net adds **project balancing**: objects marked "Balanserat" get income/expense rebooked to balance accounts at year-end. At project close, a "resultatföring" operation transfers accumulated balance to the real P&L.

SIE mapping: Flerårigt objects → dimension 6, non-Flerårigt → dimension 1. The mapping must respect the Flerårigt flag during SIE export.

### Bokio

Bokio uses unlimited **Tags** organized in **Tag Groups** functioning as dimensions. Users can create groups like "Projekt", "Avdelning", "Region" etc.

Key differences:
- A single transaction row can be split across multiple tags by percentage
- Tags are a reporting overlay; they do NOT export to SIE files as standard dimensions
- No built-in WIP accounting or revenue recognition logic

SIE mapping: no direct mapping. If importing Bokio data via SIE and the source had project tags, they are lost. Conversely, SIE imports into Bokio will not carry dimensional data into the tag system.

### Data model implication

For an AI-native bookkeeping engine supporting SIE interchange:
- Use SIE dimension numbers (1 for KS, 6 for project) as the canonical dimension identifiers
- Store object codes as strings (matching SIE format)
- Support per-account dimension enforcement (ALLOWED/MANDATORY/NOT_ALLOWED)
- Maintain multi-year balance accumulation for dimension 6 objects
- Reset dimension 1 balances at fiscal year boundary (unless explicitly overridden)