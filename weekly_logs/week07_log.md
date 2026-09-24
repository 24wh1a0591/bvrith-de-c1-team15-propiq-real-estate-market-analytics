# Week 07 Log — Gold Model, KPIs and Reconciliation

**Week:** 7  
**Date range:** August 31 – September 6, 2026  
**Team:** Team 15  
**Project:** P15 PropIQ — Real Estate Market Analytics  

---

## 1. Sprint Goal

Build the governed Gold-layer analytical model for PropIQ using Trusted Silver data only.

The primary objectives were to protect listing grain from lead-level fan-out, build the approved dimensions and listing/lead facts, implement the eight governed KPI definitions, create the five approved Gold summaries, and validate the resulting outputs through grain, key, reconciliation and rerun checks.

---

## 2. Work Completed

| Task | Owner | Status | Evidence |
|---|---|---|---|
| Confirmed the accepted Week-6 Trusted Silver handoff | [Student] | Done | `silver_*_trusted` tables / notebook |
| Inspected source grain, keys and lineage before Gold transformations | [Student] | Done | `notebooks/05_gold_aggregations.ipynb` |
| Validated lookup-key uniqueness before applying joins | [Student] | Done | Gold notebook validation queries |
| Built the seven governed dimensions | [Student] | Done | Gold dimension tables |
| Built `fact_listing` at the approved listing grain | [Student] | Done | Gold notebook |
| Built `fact_lead` at the approved lead grain | [Student] | Done | Gold notebook |
| Implemented the eight approved KPI definitions | [Student] | Done | `docs/gold_metrics_definition.md` / notebook |
| Built the five approved Gold summary tables | [Student] | Done | Gold summary tables |
| Performed fact and summary validation | [Student] | Done | Gold validation queries |
| Performed Trusted Silver-to-Gold reconciliation | [Student] | Done | Reconciliation queries |
| Performed manual spot-checks for listing, locality and broker records | [Student] | [Done / In Progress] | Notebook validation evidence |
| Performed controlled rerun validation | [Student] | Done | Notebook rerun evidence |
| Updated Gold KPI and metric documentation | [Student] | Done | `docs/gold_metrics_definition.md` |
| Added Week-7 implementation and validation evidence to GitHub | All Members | Done | GitHub repository |

### Gold Model Scope

The Week-7 implementation follows the approved PropIQ Gold design:

**Dimensions**

- `dim_date`
- `dim_locality`
- `dim_property`
- `dim_broker`
- `dim_listing_status`
- `dim_price_band`
- `dim_lead_channel`

**Core facts developed in the Week-7 build**

- `fact_listing`
- `fact_lead`

**Approved summaries**

- `locality_price_summary`
- `listing_performance_summary`
- `lead_conversion_summary`
- `broker_performance_summary`
- `inventory_age_summary`

The broader PropIQ Gold model also defines status-event and streaming facts for later project phases; they are not claimed here unless implemented and validated in the Week-7 notebook.

---

## 3. Key Decisions

- Gold tables use **Trusted Silver data only**.
- Quarantine data is not used as a Gold analytical input.
- Listing and lead facts remain separate to prevent lead-level fan-out from inflating listing-level measures.
- Fact grains and business keys are validated before aggregation and downstream joins.
- Lookup-key uniqueness is checked before using dimensions in fact construction.
- KPI numerators, denominators and exclusions follow the approved PropIQ KPI definitions.
- Zero-denominator cases are handled explicitly according to the documented KPI policy.
- Median listing price is calculated at listing grain.
- Median price per square foot is calculated from the trusted listing-level `price_per_sqft` values rather than averaging ratios after fan-out.
- Average Days on Market uses a status-aware end date.
- Stale Listing Rate uses a documented age threshold and remains filter-aware.
- Summary tables are maintained at their declared analytical grains.
- Gold outputs are validated against their underlying Trusted Silver inputs and facts.
- Controlled reruns are used to check deterministic output behavior.
- Manual spot-checks are performed for at least one listing, locality and broker to support source-to-Gold traceability.

---

## 4. KPI Definitions Implemented

The approved Week-7 KPI catalogue contains the following eight metrics:

| KPI | Definition / Control |
|---|---|
| Active Listings | Distinct trusted listings with active status; exclude quarantine and unresolved duplicates |
| Median Listing Price | Median normalized asking price calculated at listing grain |
| Median Price per Sq Ft | Median trusted `price_per_sqft`; avoid averaging raw ratios after fan-out |
| Lead Conversion Rate | Closed listings after qualified lead / listings with qualified leads × 100 |
| Average Leads per Listing | Trusted leads / listings receiving leads; exclude zero-lead listings from the denominator |
| Average Days on Market | Completion or current-age days from creation using a status-aware end date |
| Stale Listing Rate | Active listings above the approved age threshold / active listings × 100 |
| DQ Pass Rate | Trusted evaluated rows / total evaluated input rows × 100 |

No KPI answer values are hard-coded into the Gold logic.

---

## 5. Blockers / Risks

| Blocker / Risk | Impact | Help Needed |
|---|---|---|
| Stale-listing age threshold requires confirmation if not yet formally closed | KPI output may change when the approved threshold is finalized | Mentor confirmation |
| Price-band boundaries require confirmation if not yet formally closed | Price-band classification and related summaries may require adjustment | Mentor confirmation |
| Summary-table grain must remain consistent with the approved reporting contract | Incorrect grain could affect downstream Power BI analysis | Mentor/design review |
| Manual spot-check evidence must use actual project records | Placeholder IDs cannot be used as final traceability evidence | Replace placeholders with actual listing, locality and broker records |
| Any unresolved Week-6 rework must be closed before final Gold acceptance | Downstream Gold results could depend on an unaccepted upstream state | Complete and document rework |

---

## 6. Evidence Added to GitHub

- `notebooks/05_gold_aggregations.ipynb`
- `docs/gold_metrics_definition.md`
- `P15-D05.png`
- `weekly_logs/week07_log.md`
- Trusted Silver input references
- Seven Gold dimension outputs
- `fact_listing`
- `fact_lead`
- Five approved Gold summary tables
- Gold KPI validation queries
- Trusted Silver-to-Gold reconciliation evidence
- Grain and key validation evidence
- Controlled rerun validation evidence
- Manual listing, locality and broker spot-check evidence

---

## 7. AI Transparency Note

| Question | Response |
|---|---|
| **Where AI helped** | AI was used to support the structuring of the Gold-layer workflow, KPI documentation, validation logic and technical documentation. |
| **What we changed after AI suggestion** | The suggested approach was adapted to the approved PropIQ playbook, actual Trusted Silver tables, declared Gold grains, KPI definitions and project-specific object names. |
| **What we verified manually** | Trusted Silver availability, source grain, lookup-key uniqueness, fact grain, lead-to-listing references, KPI logic, Gold summaries, reconciliation queries, manual spot-checks and rerun behavior were verified using executed Databricks queries and notebook outputs. |
| **What we can explain without AI** | The team can explain dimension and fact design, grain preservation, lead fan-out, KPI numerators and denominators, summary aggregation, reconciliation, manual traceability and controlled rerun validation. |

---

## 8. Next Week Preparation

- Close any remaining mentor feedback from the Week-7 review.
- Finalize any pending KPI threshold or parameter decisions.
- Complete any remaining manual spot-check evidence.
- Confirm that Gold tables and summaries satisfy their declared grains.
- Preserve the validated Gold outputs for the Power BI hand-off.
- Prepare controlled Gold exports for the next reporting phase.
- Begin the Week-8 Gold-to-Power BI hand-off workflow.
- Ensure every team member can trace an important business metric from Power BI back to its owning Gold table.

---

## Week 07 Outcome

The PropIQ Gold analytical layer was developed from **Trusted Silver data only**.

The Week-7 implementation established the governed dimensions, separate listing and lead facts, five approved Gold summaries and eight KPI definitions while protecting listing grain from lead-level fan-out.

Validation focused on source grain, key uniqueness, fact and summary consistency, KPI logic, Trusted Silver-to-Gold reconciliation, manual spot-checks and controlled rerun behavior.

Any remaining threshold confirmation, mentor rework or manual spot-check items are explicitly recorded as blockers rather than being treated as completed evidence.
