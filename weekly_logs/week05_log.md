# Week 05 Log — Silver Candidate Transformation

**Week:** 5  
**Date range:** 1 August 2026 – 7 August 2026  
**Team:** Team 15  
**Project:** PropIQ – Real Estate Market Analytics

## Sprint goal

Transform the validated Bronze inputs into typed and normalized Silver Candidate datasets while preserving source lineage, physical grain and reconciliation keys.

## Work completed

| Task | Ownership | Status | Evidence |
|---|---|---|---|
| Standardize Listings Bronze data | Thota Madhulika; P. Lakshmi Naga Sree; Vadlamuru Rishitha | Completed | `notebooks/03_silver_transformations.ipynb` |
| Standardize Leads Bronze data | Thota Madhulika; P. Lakshmi Naga Sree; Vadlamuru Rishitha | Completed | `notebooks/03_silver_transformations.ipynb` |
| Standardize Localities Bronze data | Thota Madhulika; P. Lakshmi Naga Sree; Vadlamuru Rishitha | Completed | `notebooks/03_silver_transformations.ipynb` |
| Standardize Brokers Bronze data | Thota Madhulika; P. Lakshmi Naga Sree; Vadlamuru Rishitha | Completed | `notebooks/03_silver_transformations.ipynb` |
| Apply safe type casting | Thota Madhulika; P. Lakshmi Naga Sree; Vadlamuru Rishitha | Completed | Silver transformation notebook |
| Normalize date and timestamp fields | Thota Madhulika; P. Lakshmi Naga Sree; Vadlamuru Rishitha | Completed | Silver transformation notebook |
| Derive listing-level analytical fields | Thota Madhulika; P. Lakshmi Naga Sree; Vadlamuru Rishitha | Completed | Silver transformation notebook |
| Preserve `record_uid` and source lineage | Thota Madhulika; P. Lakshmi Naga Sree; Vadlamuru Rishitha | Completed | Silver Candidate outputs |
| Produce four Silver Candidate datasets | Thota Madhulika; P. Lakshmi Naga Sree; Vadlamuru Rishitha | Completed | Candidate tables |

## Silver Candidate outputs

The Week-05 transformation produced the following Candidate datasets:

- `silver_propiq_listings_candidate`
- `silver_propiq_leads_candidate`
- `silver_propiq_localities_candidate`
- `silver_propiq_brokers_candidate`

The Candidate layer is intended to provide typed, normalized and lineage-preserving inputs for the subsequent Data Quality stage.

## Listings-derived fields

The Listings Candidate transformation includes the following derived controls and analytical fields:

- `actual_days_on_market`
- `days_since_last_update`
- `is_completed`
- `is_chronology_valid`
- `calculated_price_per_sqft`
- `price_per_sqft_variance`

These fields support later validation and Gold-layer analytical requirements.

## Grain and lineage decisions

The Silver Candidate transformation preserves the physical reconciliation key `record_uid` and source/batch lineage information.

Candidate construction is row-preserving. Week 05 does not perform the final filtering, deduplication or quarantine decisions.

No cross-entity joins are required for Candidate construction.

This separation keeps transformation and Data Quality responsibilities distinct:

**Bronze → Silver Candidate → Data Quality → Trusted/Quarantine**

## Key decisions

1. Candidate tables remain row-preserving.
2. `record_uid` is preserved for physical reconciliation and lineage.
3. Type casting and date/timestamp normalization are performed during Candidate construction.
4. Analytical derived fields are calculated without silently removing invalid records.
5. Invalid or suspicious values remain visible for the Week-06 Data Quality stage.
6. Quarantine decisions are not performed during Week 05.

## Blockers / Risks / Rework

The main control for this stage is avoiding premature filtering.

Candidate transformations therefore do not silently remove records that may later fail Data Quality rules.

The downstream DQ stage is responsible for classifying records into Trusted and Quarantine while preserving failure reasons and reconciliation information.

## GitHub Evidence

Primary implementation evidence:

- `notebooks/03_silver_transformations.ipynb`
- `weekly_logs/week05_log.md`

The Silver transformation notebook contains the Candidate-table construction, type normalization, derived-field logic and lineage-preservation implementation.

## AI Transparency Note

AI assisted with schema mapping, transformation organization and documentation review.

The actual source fields, Candidate table names, derived fields and transformation boundaries were checked against the Silver transformation notebook and PropIQ project data definitions.

## Next Week Preparation

The four Candidate datasets produced in Week 05 are the inputs for the Week-06 Data Quality stage.

Week 06 should validate the Candidate records, apply the approved DQ rules, and route records into Trusted or Quarantine without losing reconciliation or failure information.
