# Week 07 Log — Gold Model, KPIs and Reconciliation

**Week:** 7  
**Date range:** August 31 – September 6, 2026  
**Team:** Team 15  
**Project:** P15 PropIQ — Real Estate Market Analytics  

---

## 1. Sprint Goal

Build the Gold-layer data model for PropIQ using only Trusted Silver data.

Implement the governed dimensions, listing and lead facts, approved summary tables, and KPI definitions while validating data grain, join safety, reconciliation, and rerun consistency.

---

## 2. Work Completed

| Task | Owner | Status | Evidence |
|---|---|---|---|
| Confirmed Week-6 Trusted Silver handoff | Thota Madhulika | Done | `notebooks/05_gold_aggregations.ipynb` |
| Reconciled Candidate, Trusted, and Quarantine records | Thota Madhulika | Done | Notebook Section 3.1 |
| Validated lookup-key uniqueness before joins | Thota Madhulika | Done | Notebook Section 4 |
| Built 7 governed dimensions | P. Lakshmi Naga Sree | Done | Gold dimension tables |
| Built `fact_listing` at `record_uid` grain | P. Lakshmi Naga Sree | Done | Notebook Section 6 |
| Built `fact_lead` at `record_uid` grain | P. Lakshmi Naga Sree | Done | Notebook Section 7 |
| Implemented 8 approved KPI definitions | Vadlamuru Rishitha | Done | Notebook Sections 8–9 |
| Built 5 Gold summary tables | Vadlamuru Rishitha | Done | Notebook Section 12 |
| Performed Gold-to-Trusted reconciliation | Thota Madhulika | Done | Notebook Section 11 |
| Performed controlled rerun validation | Vadlamuru Rishitha | Done | Notebook Section 14 |
| Added Gold-layer validation and evidence queries | All Members | In Progress | Notebook Sections 13–16 |

### Week-6 Handoff Reconciliation

| Entity | Candidate Rows | Trusted Rows | Quarantine Rows | Status |
|---|---:|---:|---:|---|
| Listings | 50,200 | 49,000 | 1,200 | PASS |
| Leads | 120,800 | 118,000 | 2,800 | PASS |
| Localities | 80 | 80 | 0 | PASS |
| Brokers | 320 | 320 | 0 | PASS |

---

## 3. Key Decisions

- Gold tables use **Trusted Silver only**; Quarantine tables are not used as Gold inputs.
- `fact_listing` and `fact_lead` remain separate to prevent lead-level fan-out from inflating listing-level measures.
- `fact_listing` uses one row per physical listing identified by `record_uid`.
- `fact_lead` uses one row per physical lead identified by `record_uid`.
- Join-safety checks are performed before aggregations.
- Median Price per Sq Ft is calculated from listing-level data without introducing lead fan-out.
- Average Days on Market uses a status-aware end date.
- Zero-denominator cases are handled explicitly.
- The stale-listing threshold and price-band boundaries are treated as documented parameters rather than silently assumed as final.
- Summary tables are aggregated at their declared grains and validated against the underlying fact tables.
- Controlled rerun validation is used to confirm deterministic Gold outputs.
- KPI definitions and Gold table structures are maintained consistently with the PropIQ data model and approved project requirements.

---

## 4. Blockers / Risks

| Blocker / Risk | Impact | Help Needed |
|---|---|---|
| Stale-listing age threshold requires confirmation | KPI output may change if the approved threshold differs | Mentor confirmation |
| Price-band boundaries require confirmation | `dim_price_band` and related analysis may require adjustment | Mentor confirmation |
| Summary-table grains are documented design choices | Final reporting grain may change if a different grain is approved | Mentor confirmation |
| Manual spot-check queries contain placeholder IDs | Final manual traceability evidence is incomplete | Replace with actual listing/locality/broker IDs |

---

## 5. Evidence Added to GitHub

- `notebooks/05_gold_aggregations.ipynb`
- `docs/gold_metrics_definition.md`
- `P15-D05.png`
- `weekly_logs/week07_log.md`
- Gold dimension tables
- `fact_listing`
- `fact_lead`
- Five approved Gold summary tables
- Gold validation and reconciliation queries
- Controlled rerun validation evidence

---

## 6. AI Transparency Note

| Question | Response |
|---|---|
| **Where AI helped** | AI was used to support the structuring of the Gold-layer workflow, KPI-contract organization, validation logic, and technical documentation. |
| **What we changed after AI suggestion** | The suggested approach was adapted to the PropIQ playbook, actual Trusted Silver table names, approved KPI definitions, declared grains, join-safety requirements, and Gold object names. |
| **What we verified manually** | Trusted input availability, Week-6 reconciliation, lookup-key uniqueness, fact grain preservation, lead-to-listing references, Gold reconciliation, and controlled rerun results were verified using executed SQL queries. |
| **What we can explain without AI** | We can explain fact and dimension design, grain preservation, join fan-out, KPI denominators, aggregation logic, reconciliation, and rerun validation. |

---

## 7. Next Week Preparation

- Obtain mentor confirmation for the stale-listing threshold.
- Obtain mentor confirmation for price-band boundaries.
- Confirm the approved grains for the Gold summary tables.
- Replace placeholder IDs with real listing, locality, and broker IDs for manual spot checks.
- Finalize `docs/gold_metrics_definition.md`.
- Complete the remaining Week-7 exit-checklist evidence.
- Prepare the validated Gold-layer outputs for the Power BI handoff.
- Prepare the approved Gold tables for Week-8 export and dashboard integration.

---

## Week 07 Outcome

The Gold-layer implementation was developed from **Trusted Silver data only**, with separate listing and lead facts, governed dimensions, approved summary tables, KPI definitions, reconciliation checks, and controlled rerun validation.

The Week-6 source reconciliation passed for listings, leads, localities, and brokers. The Gold layer is prepared for the next phase, with the remaining documented items focused on mentor confirmation of KPI parameters and completion of manual traceability spot checks.
