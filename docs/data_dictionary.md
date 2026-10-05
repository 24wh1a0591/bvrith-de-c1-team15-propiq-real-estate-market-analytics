# PropIQ Data Dictionary

**Purpose:** Govern the source, Silver Candidate/Trusted, Gold and streaming schemas for PropIQ.

## Source catalog
| Source | Grain | Role |
|---|---|---|
| `listings.parquet` | one physical listing row; `record_uid` is the physical key | Primary listing source |
| `leads.csv` | one physical lead row; `record_uid` is the physical key | CRM lead source |
| `localities.json` | one locality master row | Reference source |
| `brokers.csv` | one broker master row | Reference source |
| `listing_status_event_drop_*.json` | one listing-status event | Week-10 streaming source |

## Core source fields
**Listings:** `record_uid`, `listing_id`, `locality_id`, `broker_id`, `property_type`, `furnishing`, `bedrooms`, `built_up_area_sqft`, `asking_price_inr`, `price_per_sqft`, `listing_status`, `listing_created_date`, `completion_date`, `last_updated_timestamp`.

**Leads:** `record_uid`, `lead_id`, `listing_id`, `lead_channel`, `buyer_intent`, `qualified_flag`, `lead_status`, `budget_band`, `lead_timestamp`.

**Localities:** `record_uid`, `locality_id`, `locality_name`, `city`, `city_zone`, `market_segment`.

**Brokers:** `record_uid`, `broker_id`, `agency_name`, `city`, `broker_tier`, `active_flag`, `onboarded_date`, `service_rating`.

## Silver Candidate
Candidate tables: `silver_propiq_listings_candidate`, `silver_propiq_leads_candidate`, `silver_propiq_localities_candidate`, `silver_propiq_brokers_candidate`.

Derived controls include `calculated_price_per_sqft`, `price_per_sqft_variance`, `actual_days_on_market`, `days_since_last_update`, `is_completed`, and `is_chronology_valid`. Physical lineage is retained through `record_uid` and source/batch metadata.

## Gold contract
**Dimensions:** `gold_dim_date`, `gold_dim_locality`, `gold_dim_property`, `gold_dim_broker`, `gold_dim_listing_status`, `gold_dim_price_band`, `gold_dim_lead_channel`.

**Facts:** `gold_fact_listing` (one Trusted physical listing), `gold_fact_lead` (one Trusted physical lead).

**Summaries:** `gold_locality_price_summary`, `gold_listing_performance_summary`, `gold_lead_conversion_summary`, `gold_broker_performance_summary`, `gold_inventory_age_summary`.

## Streaming event fields
`listing_event_id`, `listing_id`, `event_type`, `event_timestamp`, `event_sequence`, `listing_status`, `asking_price`, `locality_id`, `broker_id`, `property_type`, `bedrooms`, `area_sqft`, `source_system`, `schema_version`, `ingestion_timestamp`, `_rescued_data`, `_corrupt_record`.

## Governance
- Power BI consumes Gold outputs only.
- `record_uid` is the physical reconciliation key.
- Approved categorical domains must not be invented from observed data.
- Week 03 is profiling/relationship validation; full Bronze ingestion is Week 04.
