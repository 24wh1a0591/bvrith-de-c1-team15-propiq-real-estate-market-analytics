# Week 09 Log — Three-Page Power BI Dashboard

**Week:** 9  
**Date range:**22 sep 2026 - 30 sep 2026
**Team:** Team 15  
**Project:** PropIQ – Real Estate Market Analytics

## Sprint goal

Complete the Gold-only three-page Power BI dashboard, validate the dashboard metrics against the governed Gold layer, test filter and slicer interactions, and ensure that the dashboard presents a consistent business story without bypassing Gold.

## Outcome

The three-page Power BI dashboard was completed using approved Gold outputs.

The dashboard was organized into Market Overview, Locality & Pricing Intelligence, and Listing / Broker / Lead views. Key business metrics were checked against Gold, filter and slicer interactions were tested, and the dashboard was kept aligned with the governed Gold model and KPI definitions.

## Work completed

| Task | Ownership | Status | Evidence |
|---|---|---|---|
| Complete Page 1 — Market Overview | Thota Madhulika; P. Lakshmi Naga Sree; Vadlamuru Rishitha | Completed | `dashboard/` |
| Complete Page 2 — Locality & Pricing Intelligence | Thota Madhulika; P. Lakshmi Naga Sree; Vadlamuru Rishitha | Completed | `dashboard/` |
| Complete Page 3 — Listing / Broker / Lead | Thota Madhulika; P. Lakshmi Naga Sree; Vadlamuru Rishitha | Completed | `dashboard/` |
| Add locality pricing views | Thota Madhulika; P. Lakshmi Naga Sree; Vadlamuru Rishitha | Completed | Dashboard |
| Add property-mix views | Thota Madhulika; P. Lakshmi Naga Sree; Vadlamuru Rishitha | Completed | Dashboard |
| Add broker-performance views | Thota Madhulika; P. Lakshmi Naga Sree; Vadlamuru Rishitha | Completed | Dashboard |
| Add lead-conversion views | Thota Madhulika; P. Lakshmi Naga Sree; Vadlamuru Rishitha | Completed | Dashboard |
| Add inventory-age views | Thota Madhulika; P. Lakshmi Naga Sree; Vadlamuru Rishitha | Completed | Dashboard |
| Test slicers and filter interactions | Thota Madhulika; P. Lakshmi Naga Sree; Vadlamuru Rishitha | Completed | Dashboard validation |
| Reconcile important dashboard metrics to Gold | Thota Madhulika; P. Lakshmi Naga Sree; Vadlamuru Rishitha | Completed | Gold reconciliation evidence |

## Dashboard structure

### Page 1 — Market Overview

The first page provides the overall market-level view using approved Gold metrics and report-facing measures.

### Page 2 — Locality & Pricing Intelligence

The second page focuses on locality-level pricing and property-mix analysis.

The page supports comparison of locality performance and pricing patterns using governed Gold outputs.

### Page 3 — Listing / Broker / Lead

The third page combines listing, broker and lead-performance views while preserving the underlying fact-grain separation.

The page includes:

- Broker performance.
- Lead conversion.
- Listing performance.
- Inventory age.

## Files / Objects

### Dashboard

- `dashboard/`

### Dashboard documentation

- `docs/dashboard_insights.md`

### Evidence

- `P15-D06B.png`
- `P15-D06C.png`

### Weekly log

- `weekly_logs/week09_log.md`

## Gold-only control

The dashboard continues to use the governed Gold layer as its analytical source.

Raw, Bronze, Silver Candidate, Trusted Silver detail and Quarantine data are not used as alternate dashboard sources.

Business metrics are not recreated through uncontrolled joins inside the dashboard.

The listing and lead facts remain separate so that one-to-many relationships do not create fan-out and inflate listing-level metrics.

## Validation

| Validation check | Result | What it proves |
|---|---|---|
| Gold-only source validation | Completed | Dashboard uses governed Gold outputs |
| Listing/lead grain validation | Completed | Separate fact grains are preserved |
| Slicer interaction testing | Completed | Filters behave consistently across dashboard visuals |
| Filter interaction testing | Completed | Dashboard responses remain consistent under filtering |
| Metric reconciliation | Completed | Important dashboard metrics agree with Gold |
| Visual source/measure review | Completed | Dashboard visuals use intended governed measures |

Numerical insights are stated only after checking the corresponding Gold source and measure.

## Key decisions

1. Listing and lead facts remain separate to prevent one-to-many fan-out.
2. Dashboard visuals use governed Gold outputs rather than rebuilding pipeline logic.
3. Numerical business insights are only stated after verification against Gold.
4. Slicers and filters are tested to ensure that displayed metrics remain consistent with the underlying Gold definitions.
5. Dashboard organization is based on business questions rather than simply exposing the underlying table structure.

## Blockers / Rework

The primary control for Week 09 was maintaining consistency between the dashboard presentation layer and the governed Gold model.

Potential metric discrepancies caused by grain, relationship or filter-context differences were checked against the Gold layer before treating dashboard values as valid business insights.

No raw-to-dashboard shortcut was introduced to resolve presentation issues.

## Individual Contribution

### Thota Madhulika

- Participated in three-page dashboard implementation and organization.
- Participated in metric validation and Gold reconciliation.
- Backup responsibility: review dashboard source and grain consistency.
- Speaking responsibility: explain dashboard structure, Gold-only sourcing and metric validation.

### P. Lakshmi Naga Sree

- Participated in dashboard visual development and filter/slicer validation.
- Participated in reviewing dashboard relationships and measures.
- Backup responsibility: review metric behaviour under filtering.
- Speaking responsibility: explain dashboard interactions, relationships and measure behaviour.

### Vadlamuru Rishitha

- Participated in dashboard evidence, documentation and business-story review.
- Participated in validating dashboard insights against Gold.
- Backup responsibility: review evidence and downstream dashboard readiness.
- Speaking responsibility: explain dashboard insights, reconciliation and evidence.

## Mentor Rework Status

**Status:** Review / validation completed for the Week-09 dashboard scope.

The three-page dashboard was reviewed against the Gold-only requirement, metric definitions and relationship/grain controls.

Any further dashboard refinement should preserve the same governed Gold sources and KPI contracts.

## GitHub Evidence

Primary Week-09 evidence paths:

- `dashboard/`
- `docs/dashboard_insights.md`
- `P15-D06B.png`
- `P15-D06C.png`
- `weekly_logs/week09_log.md`

The Week-09 playbook specifically identifies these dashboard and evidence artifacts as the required GitHub evidence. :chatgpt-content-reference{index="1"}

## AI Transparency Note

AI assisted with dashboard organization, documentation structure and review of dashboard logic.

AI-generated suggestions were treated as implementation support and were not accepted without verification.

The team manually checked:

- Visual source tables.
- Measures.
- Relationships.
- Listing and lead fact separation.
- Gold lineage.
- Filter and slicer behaviour.
- Important metric reconciliation.

The students remain responsible for explaining the dashboard structure, measure logic, relationship behaviour and Gold reconciliation.

## Next Week Preparation

The completed three-page dashboard provides the reporting layer for the subsequent project stages.

Future work should preserve the Gold-only source boundary, governed KPI definitions, fact-grain separation and documented reconciliation controls.
