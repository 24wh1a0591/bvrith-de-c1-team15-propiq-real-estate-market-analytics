# Week 07 Log — Gold Model, KPIs and Reconciliation

**Week:** 7  
**Date range:** 31 August 2026 – 6 September 2026  
**Team:** Team 15  
**Project:** PropIQ – Real Estate Market Analytics

## Sprint goal

Build the governed Gold dimensional model, fact tables, approved summaries and KPI contracts using Trusted Silver only, while maintaining grain, join safety and reconciliation controls.

## Work completed

| Task | Ownership | Status | Evidence |
|---|---|---|---|
| Build seven governed dimensions | Thota Madhulika; P. Lakshmi Naga Sree; Vadlamuru Rishitha | Completed | `notebooks/05_gold_aggregations.ipynb` |
| Build listing fact | Thota Madhulika; P. Lakshmi Naga Sree; Vadlamuru Rishitha | Completed | `gold_fact_listing` |
| Build lead fact | Thota Madhulika; P. Lakshmi Naga Sree; Vadlamuru Rishitha | Completed | `gold_fact_lead` |
| Build five approved summaries | Thota Madhulika; P. Lakshmi Naga Sree; Vadlamuru Rishitha | Completed | Gold aggregation notebook |
| Implement eight KPI contracts | Thota Madhulika; P. Lakshmi Naga Sree; Vadlamuru Rishitha | Completed | `docs/gold_metrics_definition.md` |
| Validate fact/summary reconciliation | Thota Madhulika; P. Lakshmi Naga Sree; Vadlamuru Rishitha | Completed | Broker summary reconciliation |
| Validate join safety | Thota Madhulika; P. Lakshmi Naga Sree; Vadlamuru Rishitha | Completed | Gold modelling logic |
| Perform controlled rerun check | Thota Madhulika; P. Lakshmi Naga Sree; Vadlamuru Rishitha | Completed | Rerun evidence |

## Gold dimensions

The governed Gold model contains seven dimensions:

1. `gold_dim_date`
2. `gold_dim_locality`
3. `gold_dim_property`
4. `gold_dim_broker`
5. `gold_dim_listing_status`
6. `gold_dim_price_band`
7. `gold_dim_lead_channel`

## Gold facts

Two fact tables were implemented:

- `gold_fact_listing`
- `gold_fact_lead`

The listing fact remains at listing/`record_uid` grain, while the lead fact remains at lead grain.

This separation prevents the one-to-many listing-to-lead relationship from multiplying listing-level fact rows.

## Gold summaries

Five approved summary tables were implemented:

1. `gold_locality_price_summary`
2. `gold_listing_performance_summary`
3. `gold_lead_conversion_summary`
4. `gold_broker_performance_summary`
5. `gold_inventory_age_summary`

## KPI contracts

Eight KPI contracts were defined:

| KPI | Contract |
|---|---|
| Active Listings | Active listing count from the governed listing-grain source |
| Median Listing Price | Median listing price |
| Median Price per Sq Ft | Median price per square foot |
| Lead Conversion Rate | Converted leads divided by the defined lead denominator |
| Average Leads per Listing | Lead count evaluated at the listing-grain reporting level |
| Average Days on Market | Average governed listing age / days-on-market measure |
| Stale Listing Rate | Stale listings divided by the applicable active-listing denominator |
| DQ Pass Rate | Trusted records divided by the applicable Candidate population |

Zero denominators are handled as `NULL`/blank using the defined `NULLIF` approach rather than producing misleading numerical values.

## Join-safety controls

The Gold model follows these join-safety rules:

- `gold_fact_listing` does not directly join to the lead fact for listing-grain metrics.
- `gold_fact_lead` remains at lead grain.
- Listing-to-lead metrics are re-aggregated to the required listing/reporting grain before locality or other dimensional roll-ups.
- Lookup keys are checked for uniqueness.
- Summary outputs are reconciled to their owning fact tables.

These controls prevent one-to-many relationships from inflating listing-level metrics.

## Evidence and reconciliation

The broker performance summary reconciled to the listing fact:

- Broker summary total: **49,000**
- Listing fact total: **49,000**
- Reconciliation: **PASS**

A controlled rerun resulted in:

**Changed business rows = 0**

Concrete manual spot-check identifiers captured in the project artifacts include:

- `LOC-001`
- `BRK-0204`
- `LST-0000001`

The notebook's former placeholder manual queries were identified as invalid and their stale outputs were cleared. A fresh rerun is required before treating new manual spot-check output as current execution evidence.

## Stale listing threshold governance

The Gold implementation documents **90 days** as a working parameter for stale-listing analysis.

The approved playbook does not publish a numeric stale threshold as final policy.

Therefore, 90 days must not be represented as a mentor-approved or governance-approved permanent threshold.

## Blockers / Risks / Rework

The primary governance consideration was the distinction between a working analytical parameter and an approved policy threshold.

The 90-day stale threshold is therefore documented as a working parameter only.

A second evidence limitation concerns the manual spot-check queries: previously captured placeholder outputs were not treated as fresh evidence. Fresh execution is required for current manual spot-check results.

## GitHub Evidence

Primary implementation and documentation evidence:

- `notebooks/05_gold_aggregations.ipynb`
- `docs/gold_metrics_definition.md`
- `weekly_logs/week07_log.md`

The notebook contains the Gold dimensions, facts, summaries and validation logic. The Gold metrics definition documents the KPI contracts, denominator handling, grain and join-safety rules.

## AI Transparency Note

AI assisted with KPI-contract organization, validation-query structure and documentation review.

Trusted inputs, fact grain, join safety, reconciliation evidence and rerun controls were checked against the Gold notebook and project documentation.

The 90-day stale threshold is explicitly retained as a working parameter rather than being presented as an approved governance policy.

## Next Week Preparation

The completed Gold model provides the governed analytical layer for downstream reporting.

Future reporting work should consume the approved Gold dimensions, facts and summaries without bypassing the Trusted Silver and Gold grain controls.
