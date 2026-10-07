# Dashboard Insights

**Purpose:** Define the three-page Power BI story, its Gold lineage, evidence requirements and validation controls.

**Reporting source:** Governed Gold outputs only.

---

## 1. Three-Page Dashboard Story

The Power BI dashboard is organized around three business questions.

### Page 1 — Market Overview

**Business question:** What is happening in the market?

This page provides the overall market view using governed listing, lead, locality pricing and lead-conversion outputs.

Primary analytical focus:

- Overall listing activity.
- Market pricing.
- Lead activity.
- Lead-conversion performance.
- High-level market context.

The page must use approved Gold measures and must not recreate pipeline logic from lower layers.

---

### Page 2 — Locality & Pricing Intelligence

**Business question:** Where is inventory and how does pricing differ?

This page focuses on locality-level market structure and pricing variation.

Primary analytical focus:

- Locality inventory.
- Locality pricing.
- Property mix.
- Price-per-square-foot behaviour.
- Locality-level comparisons.

The page uses the governed locality and listing-grain Gold objects.

---

### Page 3 — Listing / Broker / Lead

**Business question:** Which listings, brokers and lead channels are performing?

This page combines performance views across listing, broker and lead activity while preserving the separate listing and lead fact grains.

Primary analytical focus:

- Listing performance.
- Broker performance.
- Lead conversion.
- Lead-channel performance.
- Inventory age.

---

## 2. Evidence Rule

Numerical claims must not be stated solely from what appears in a dashboard visual.

Before reporting a numerical insight:

1. Identify the Power BI visual and measure.
2. Identify the owning Gold table or summary.
3. Apply the same filter context.
4. Compare the dashboard value with the Gold value.
5. Record or retain sufficient evidence to explain the reconciliation.

A dashboard value is treated as validated only when it can be traced to its governed Gold source under the same filter context.

---

## 3. Gold Traceability

| Page | Primary Gold Objects | Primary Analytical Purpose |
|---|---|---|
| Market Overview | `gold_fact_listing`, `gold_fact_lead`, `gold_locality_price_summary`, `gold_lead_conversion_summary` | Market activity, pricing and lead performance |
| Locality & Pricing Intelligence | `gold_locality_price_summary`, `gold_fact_listing`, governed dimensions | Locality inventory, pricing and property mix |
| Listing / Broker / Lead | `gold_broker_performance_summary`, `gold_lead_conversion_summary`, `gold_listing_performance_summary`, `gold_inventory_age_summary`, governed facts/dimensions | Listing, broker, lead and inventory performance |

---

## 4. KPI Traceability

Dashboard KPIs must match the definitions documented in:

`docs/gold_metrics_definition.md`

The dashboard must not redefine KPI semantics independently.

Relevant governed KPI contracts include:

- Active Listings
- Median Listing Price
- Median Price per Sq Ft
- Lead Conversion Rate
- Average Leads per Listing
- Average Days on Market
- Stale Listing Rate
- DQ Pass Rate

Where a dashboard visual uses a derived measure, the measure must remain consistent with the corresponding Gold KPI contract.

---

## 5. Fact-Grain Controls

The dashboard must preserve the declared Gold fact grains:

### Listing fact

`gold_fact_listing`

**Grain:** One Trusted physical listing / `record_uid`.

### Lead fact

`gold_fact_lead`

**Grain:** One Trusted physical lead / `record_uid`.

The two facts remain separate to prevent one-to-many listing-to-lead relationships from multiplying listing-level rows.

---

## 6. Join-Safety Rule

The dashboard must not introduce lead fan-out.

In particular:

- Listing-level metrics must remain based on listing grain.
- Lead-level metrics must remain based on lead grain.
- Listing-to-lead calculations must use governed re-aggregation where required.
- A direct one-to-many join must not be used to calculate listing-level metrics.
- Relationship behaviour must remain consistent with the Gold model.

Any metric that changes unexpectedly because of a listing-to-lead relationship must be treated as a validation failure.

---

## 7. Page-Level Traceability

### Page 1 — Market Overview

| Analytical area | Primary Gold source |
|---|---|
| Listing activity | `gold_fact_listing` |
| Market pricing | `gold_fact_listing` / `gold_locality_price_summary` |
| Lead activity | `gold_fact_lead` |
| Lead conversion | `gold_lead_conversion_summary` |

### Page 2 — Locality & Pricing Intelligence

| Analytical area | Primary Gold source |
|---|---|
| Locality inventory | `gold_fact_listing` |
| Locality pricing | `gold_locality_price_summary` |
| Property mix | `gold_dim_property` |
| Price analysis | `gold_fact_listing` / `gold_locality_price_summary` |
| Locality filtering | `gold_dim_locality` |

### Page 3 — Listing / Broker / Lead

| Analytical area | Primary Gold source |
|---|---|
| Listing performance | `gold_listing_performance_summary` |
| Broker performance | `gold_broker_performance_summary` |
| Lead conversion | `gold_lead_conversion_summary` |
| Inventory age | `gold_inventory_age_summary` |
| Broker filtering | `gold_dim_broker` |
| Lead-channel analysis | `gold_dim_lead_channel` |
| Listing analysis | `gold_fact_listing` |

---

## 8. Validation Checklist

Before accepting a dashboard page or numerical insight, verify:

- [ ] Gold-only sources are used.
- [ ] Correct fact grain is preserved.
- [ ] No lead fan-out occurs.
- [ ] KPI definitions match `docs/gold_metrics_definition.md`.
- [ ] Power BI relationships match the governed Gold model.
- [ ] Important filtered dashboard values reconcile to Gold.
- [ ] Numerical claims can be traced to their owning Gold object.
- [ ] No lower-layer data is introduced to compensate for a dashboard result.

---

## 9. Numerical Insight Rule

Numerical statements in documentation, presentations or demonstrations should be made only after validation against Gold.

Do not state a numerical insight merely because a dashboard visual displays a value.

Examples of claims requiring reconciliation include:

- Total active listings.
- Median listing price.
- Median price per square foot.
- Lead conversion rate.
- Average leads per listing.
- Average days on market.
- Stale listing rate.
- DQ pass rate.
- Locality-level or broker-level ranking values.

Qualitative observations may describe patterns visible in the dashboard, but numerical values must remain traceable to the governed Gold source.

---

## 10. Filter-Context Rule

Gold reconciliation must use the same effective filter context as the Power BI visual.

Relevant filter context may include:

- Date.
- Locality.
- Property type.
- Furnishing.
- Broker.
- Listing status.
- Price band.
- Lead channel.

A value is not considered reconciled if the Power BI visual and Gold validation query use materially different filters.

---

## 11. Source Boundary

The dashboard consumes Gold outputs only.

The following are not valid direct dashboard sources:

- Raw source files.
- Bronze tables.
- Silver Candidate tables.
- Trusted Silver detail tables.
- Quarantine tables.

Lower-layer inspection may be used for debugging or lineage investigation, but dashboard metrics must be derived from governed Gold outputs.

---

## 12. Metric and Lineage Governance

Every important dashboard measure should be explainable through the following chain:

```text
Power BI visual
      ↓
Power BI measure
      ↓
Gold object / KPI contract
      ↓
Trusted Silver governed input
