# PropIQ Data Dictionary

**Purpose:** Govern the source, Silver Candidate/Trusted, Gold and streaming schemas for PropIQ.

**Primary reconciliation key:** `record_uid`

**Gold reporting rule:** Power BI consumes Gold outputs only.

---

## 1. Source Catalog

| Source | Grain | Physical / Business Key | Role |
|---|---|---|---|
| `listings.parquet` | One physical listing row | `record_uid` | Primary listing source |
| `leads.csv` | One physical lead row | `record_uid` | CRM lead source |
| `localities.json` | One locality master row | `locality_id` | Reference source |
| `brokers.csv` | One broker master row | `broker_id` | Reference source |
| `listing_status_event_drop_*.json` | One listing-status event | `listing_event_id` | Week-10 streaming source |

`record_uid` is the physical reconciliation key used to preserve and reconcile physical records across the pipeline.

---

## 2. Core Source Schemas

### 2.1 Listings

**Source:** `listings.parquet`

**Grain:** One physical listing row.

**Physical key:** `record_uid`

| Field | Description |
|---|---|
| `record_uid` | Physical reconciliation key |
| `listing_id` | Listing business identifier |
| `locality_id` | Locality reference |
| `broker_id` | Broker reference |
| `property_type` | Property type |
| `furnishing` | Furnishing category |
| `bedrooms` | Bedroom count |
| `built_up_area_sqft` | Built-up area in square feet |
| `asking_price_inr` | Asking price in INR |
| `price_per_sqft` | Price per square foot |
| `listing_status` | Listing status |
| `listing_created_date` | Listing creation date |
| `completion_date` | Completion date |
| `last_updated_timestamp` | Last update timestamp |

---

### 2.2 Leads

**Source:** `leads.csv`

**Grain:** One physical lead row.

**Physical key:** `record_uid`

| Field | Description |
|---|---|
| `record_uid` | Physical reconciliation key |
| `lead_id` | Lead business identifier |
| `listing_id` | Related listing identifier |
| `lead_channel` | Lead acquisition channel |
| `buyer_intent` | Buyer intent classification |
| `qualified_flag` | Lead qualification indicator |
| `lead_status` | Lead status |
| `budget_band` | Buyer budget band |
| `lead_timestamp` | Lead timestamp |

Leads have a relationship to listings through `listing_id`. Because multiple leads can relate to a listing, lead data must not be used in a way that multiplies listing-grain metrics.

---

### 2.3 Localities

**Source:** `localities.json`

**Grain:** One locality master row.

**Business key:** `locality_id`

| Field | Description |
|---|---|
| `record_uid` | Physical reconciliation key |
| `locality_id` | Locality identifier |
| `locality_name` | Locality name |
| `city` | City |
| `city_zone` | City-zone classification |
| `market_segment` | Market segment |

---

### 2.4 Brokers

**Source:** `brokers.csv`

**Grain:** One broker master row.

**Business key:** `broker_id`

| Field | Description |
|---|---|
| `record_uid` | Physical reconciliation key |
| `broker_id` | Broker identifier |
| `agency_name` | Agency name |
| `city` | Broker city |
| `broker_tier` | Broker tier |
| `active_flag` | Broker active-status indicator |
| `onboarded_date` | Broker onboarding date |
| `service_rating` | Service rating |

---

## 3. Silver Candidate Layer

The Silver Candidate layer provides typed and normalized datasets derived from the Bronze inputs.

### Candidate tables

- `silver_propiq_listings_candidate`
- `silver_propiq_leads_candidate`
- `silver_propiq_localities_candidate`
- `silver_propiq_brokers_candidate`

### Candidate transformation controls

The Candidate layer includes the following derived controls and analytical fields where applicable:

| Field | Purpose |
|---|---|
| `calculated_price_per_sqft` | Calculated listing price-per-square-foot value |
| `price_per_sqft_variance` | Comparison/control for price-per-square-foot values |
| `actual_days_on_market` | Listing duration measure |
| `days_since_last_update` | Age since the latest listing update |
| `is_completed` | Completion-state indicator |
| `is_chronology_valid` | Chronology validation indicator |

Physical lineage is retained through:

- `record_uid`
- Source metadata
- Batch metadata

Candidate construction is separate from final Data Quality routing. Invalid records are not silently removed during Candidate construction.

---

## 4. Trusted Silver and Data Quality Boundary

Silver Candidate data is evaluated using the approved PropIQ Data Quality rules.

The DQ stage routes records into:

- Trusted
- Quarantine

The Candidate-to-Trusted/Quarantine reconciliation must preserve physical records and provide traceable routing.

The following governance rule applies:

> Approved categorical domains must not be invented from observed data.

If an approved governance-domain dependency is unavailable, the limitation must be documented rather than replacing it with an inferred allowed-value list.

---

## 5. Gold Layer Contract

Gold consumes **Trusted Silver only**.

### 5.1 Dimensions

The governed Gold dimensions are:

- `gold_dim_date`
- `gold_dim_locality`
- `gold_dim_property`
- `gold_dim_broker`
- `gold_dim_listing_status`
- `gold_dim_price_band`
- `gold_dim_lead_channel`

### 5.2 Facts

| Object | Grain |
|---|---|
| `gold_fact_listing` | One Trusted physical listing / `record_uid` |
| `gold_fact_lead` | One Trusted physical lead / `record_uid` |

The listing and lead facts remain separate to prevent one-to-many lead relationships from creating listing-grain fan-out.

### 5.3 Summaries

The governed Gold summaries are:

- `gold_locality_price_summary`
- `gold_listing_performance_summary`
- `gold_lead_conversion_summary`
- `gold_broker_performance_summary`
- `gold_inventory_age_summary`

---

## 6. Gold Grain and Join-Safety Rules

The following rules govern Gold construction:

1. `gold_fact_listing` remains at one Trusted physical listing / `record_uid` grain.
2. `gold_fact_lead` remains at one Trusted physical lead / `record_uid` grain.
3. `gold_fact_listing` must not be joined directly to leads for listing-grain metrics.
4. Listing-to-lead summaries must be re-aggregated to the required listing/reporting grain before locality roll-up.
5. Lookup keys must be checked for uniqueness before joins.
6. Summary outputs must be reconciled to their owning facts.
7. Listing-level metrics must not be calculated after lead fan-out.

---

## 7. Gold KPI Contract

The governed Gold layer defines the following eight KPI contracts.

### 7.1 Active Listings

Distinct Trusted listings with active status.

**Grain:** Listing.

---

### 7.2 Median Listing Price

Median Trusted asking price at listing grain.

The calculation must not be performed after a lead join that could duplicate listing rows.

---

### 7.3 Median Price per Sq Ft

Median Trusted `price_per_sqft`.

The metric must remain at listing grain and must not be calculated after lead fan-out.

---

### 7.4 Lead Conversion Rate

```text
closed listings after qualified lead
------------------------------------ × 100
listings with qualified leads
