# 06_qa-and-monitoring – Data Quality & Tracking Health

This folder contains the quality assurance layer of the Siete Padel Marketing Analytics project.  
Its primary purpose is to ensure that the GA4 data pipeline produces complete, valid, and reliable outputs before any analysis or dashboarding is executed.

The QA layer verifies that the upstream components (client-side tracking + GA4 export pipeline) are functioning correctly.

## Folder Contents

| File | Description |
|------|-------------|
| `event_coverage_check.py` | Validates that all required GA4 export files exist, are readable, and contain non-empty data. |
| `README.md` | Documentation of the QA and monitoring responsibilities within the project. |

## Purpose of This Module

This module ensures **tracking health** and **data completeness** by answering questions like:

- Are all expected funnel events exported from GA4?
- Are the CSVs non-empty?
- Does any export contain only zero counts?
- Can the analysis layer safely proceed?

This prevents broken or incomplete data from silently propagating into KPIs or dashboards.

## Implemented Check: Event Coverage Validation

The script `event_coverage_check.py` performs:

1. **File existence check**  
   Verifies that the following files exist: Input data must be present in: 04_data-pipeline/data/ `view_item.csv` `add_to_cart.csv` `begin_checkout.csv` `purchase.csv`

2. **Empty file detection**  
   Flags exports with zero rows.

3. **Zero event_count detection**  
   Flags exports where event_count exists but sums to zero.

## Example Output


===== Siete Padel – QA: Event Coverage Check =====


✔ OK: view_item.csv (12 rows)

✔ OK: add_to_cart.csv (11 rows)

✔ OK: begin_checkout.csv (7 rows)

⚠️ No event_count values: purchase.csv (all zero)


Event coverage check complete.

### Example usage

```bash
.venv\Scripts\activate
python 06_qa-and-monitoring/event_coverage_check.py






