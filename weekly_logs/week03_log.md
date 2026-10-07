# Week 03 Log — Data Exploration, Relationships and Join Safety

**Week:** 3  
**Date range:** 25 July 2026 – 30 July 2026  
**Team:** Team 15  
**Project:** PropIQ – Real Estate Market Analytics

## Sprint goal

Profile the four PropIQ source datasets, establish physical grain and business keys, validate source relationships, identify join and fan-out risks, and create only the approved Week-03 Bronze demonstration.

## Work completed

| Task | Ownership | Status | Evidence |
|---|---|---|---|
| Profile Listings, Leads, Localities and Brokers schemas | Thota Madhulika; P. Lakshmi Naga Sree; Vadlamuru Rishitha | Completed | `notebooks/01_data_exploration.ipynb` |
| Identify physical reconciliation keys and business keys | Thota Madhulika; P. Lakshmi Naga Sree; Vadlamuru Rishitha | Completed | `notebooks/01_data_exploration.ipynb` |
| Validate Listings → Localities relationship | Thota Madhulika; P. Lakshmi Naga Sree; Vadlamuru Rishitha | Completed | Listings-to-Localities anti-join |
| Validate Listings → Brokers relationship | Thota Madhulika; P. Lakshmi Naga Sree; Vadlamuru Rishitha | Completed | Listings-to-Brokers anti-join |
| Validate Leads → Listings relationship | Thota Madhulika; P. Lakshmi Naga Sree; Vadlamuru Rishitha | Completed | Leads-to-Listings anti-join |
| Check listing/lead fan-out risk | Thota Madhulika; P. Lakshmi Naga Sree; Vadlamuru Rishitha | Completed | Join-safety validation in exploration notebook |
| Profile categorical domains | Thota Madhulika; P. Lakshmi Naga Sree; Vadlamuru Rishitha | Completed | Domain profiling queries |
| Create small Bronze demonstration | Thota Madhulika; P. Lakshmi Naga Sree; Vadlamuru Rishitha | Completed | `propiq_week03_bronze_demo_listings` |
| Create lineage demonstration view | Thota Madhulika; P. Lakshmi Naga Sree; Vadlamuru Rishitha | Completed | Lineage demo view in exploration notebook |

## Data and relationship validation

The exploration work established the physical and business-key structure required for downstream processing.

The following relationship checks were implemented:

- Listings → Localities anti-join.
- Listings → Brokers anti-join.
- Leads → Listings anti-join.
- Listing-grain preservation before and after joins.
- Listing/lead fan-out measurement.

`record_uid` is retained as the physical reconciliation key. Business keys are used for relationship validation and downstream modelling rather than being used to hide physical duplicates.

One-to-many lead relationships are not used directly for listing-grain metrics because doing so can multiply listing rows.

## Key decisions

1. `record_uid` is the physical reconciliation key for downstream lineage and reconciliation.
2. Business keys are retained for relationship validation.
3. One-to-many relationships must be handled without changing the intended grain of the consuming dataset.
4. Categorical domains are profiled from the available source data without inventing an approved governance dictionary.
5. Week 03 remains limited to exploration, relationship validation and the small Bronze demonstration.
6. Full Bronze ingestion is kept within the Week 04 scope.

## Blockers / Risks / Rework

The original exploration notebook contained PageLoop/loan-related remnants that were not applicable to PropIQ.

The notebook was reworked so that the exploration scope is PropIQ-specific and focuses on:

- PropIQ source profiling.
- Physical and business-key validation.
- Relationship integrity.
- Anti-join checks.
- Join fan-out safety.
- Limited Bronze demonstration.

No full Bronze, Silver, Gold, Power BI or streaming implementation was included in Week 03.

## GitHub Evidence

Primary implementation evidence:

- `notebooks/01_data_exploration.ipynb`
- `weekly_logs/week03_log.md`

The exploration notebook contains the profiling, relationship, anti-join, fan-out and Bronze demonstration logic used for this week's work.

## AI Transparency Note

AI assisted with restructuring and reviewing the Week-03 exploration workflow and documentation.

Dataset paths, source fields, relationship checks, grain decisions and Week-03 scope boundaries were verified against the PropIQ project artifacts before inclusion in the weekly log.

## Next Week Preparation

The validated source structure and relationship findings provide the basis for the Week-04 Bronze ingestion work.

Week 04 should build the complete Bronze layer from the validated source inputs while preserving physical lineage and source-level records.
