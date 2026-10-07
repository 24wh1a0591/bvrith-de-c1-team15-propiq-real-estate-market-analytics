# Gold Metrics Definition

**Week:** 7  
**Input:** Trusted Silver only  
**Layer:** Gold  
**Purpose:** Define the governed Gold objects, their grain, KPI contracts, denominator behaviour and join-safety rules used by downstream reporting and Power BI.

---

## 1. Gold Layer Contract

The Gold layer is built exclusively from Trusted Silver inputs.

Gold objects must preserve their declared grain and must not introduce row multiplication through uncontrolled one-to-many joins.

The Gold layer provides:

- Governed dimensions.
- Listing and lead facts at separate grains.
- Approved analytical summaries.
- KPI definitions with explicit denominator handling.
- Join-safety controls for listing-to-lead relationships.
- Reconciliation points for downstream reporting.

---

## 2. Gold Table Catalog

| Object | Grain | Purpose |
|---|---|---|
| `gold_dim_date` | One calendar date | Calendar/date analysis |
| `gold_dim_locality` | One `locality_id` | Locality-level reporting |
| `gold_dim_property` | One property type + furnishing combination | Property-mix analysis |
| `gold_dim_broker` | One `broker_id` | Broker analysis |
| `gold_dim_listing_status` | One `listing_status` | Listing-status analysis |
| `gold_dim_price_band` | One documented price band | Price-band analysis |
| `gold_dim_lead_channel` | One `lead_channel` | Lead-channel analysis |
| `gold_fact_listing` | One Trusted physical listing / `record_uid` | Listing-grain measures |
| `gold_fact_lead` | One Trusted physical lead / `record_uid` | Lead-grain measures |
| `gold_locality_price_summary` | One `locality_id` | Locality pricing metrics |
| `gold_listing_performance_summary` | One `locality_id` | Listing performance metrics |
| `gold_lead_conversion_summary` | One `locality_id` | Lead conversion metrics |
| `gold_broker_performance_summary` | One `broker_id` | Broker performance metrics |
| `gold_inventory_age_summary` | One `locality_id` | Inventory-age metrics |

---

## 3. Fact-Grain Contract

### `gold_fact_listing`

**Grain:** One Trusted physical listing identified by `record_uid`.

Listing-level measures must be calculated at listing grain.

The listing fact must not be joined directly to lead records for listing-grain calculations.

### `gold_fact_lead`

**Grain:** One Trusted physical lead identified by `record_uid`.

Lead-level measures remain at lead grain.

Lead records must not be treated as additional listing rows.

### Grain rule

The listing and lead facts remain separate because the relationship between listings and leads can be one-to-many.

Directly joining these facts for listing-level calculations can multiply listing rows and produce inflated metrics.

---

## 4. Eight KPI Contracts

### 1. Active Listings

**Definition:** Distinct Trusted listings with active status.

**Grain:** Listing.

**Denominator:** Not applicable.

The calculation must use distinct Trusted listing records and the governed active-status definition.

---

### 2. Median Listing Price

**Definition:** Median Trusted asking price calculated at listing grain.

**Grain:** Listing.

Only the governed Trusted listing population is included.

The metric must not be calculated after a lead join or any other operation that can duplicate listing rows.

---

### 3. Median Price per Sq Ft

**Definition:** Median Trusted `price_per_sqft`.

**Grain:** Listing.

`price_per_sqft` is evaluated from the governed listing-level data.

The metric must never be calculated after lead fan-out.

---

### 4. Lead Conversion Rate

**Definition:**

```text
closed listings after qualified lead
------------------------------------ × 100
listings with qualified leads
