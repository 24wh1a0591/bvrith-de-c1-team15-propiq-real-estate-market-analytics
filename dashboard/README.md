# PropIQ — Power BI Dashboard

**Project:** P15 PropIQ — Real Estate Market Analytics  
**Team:** Team 15  
**Data layer:** Gold

## Pages
| Page | Purpose |
|---|---|
| Page 1 — Market Overview | Overall market KPIs, listing trends, pricing/property mix and inventory |
| Page 2 — Locality & Pricing Intelligence | Locality price, price/sqft, inventory and property-type comparisons |
| Page 3 — Listing / Broker / Lead | Broker performance, lead channels/conversion, listing performance and inventory age |

## Gold objects
Dimensions: `gold_dim_date`, `gold_dim_locality`, `gold_dim_property`, `gold_dim_broker`, `gold_dim_listing_status`, `gold_dim_price_band`, `gold_dim_lead_channel`.

Facts: `gold_fact_listing`, `gold_fact_lead`.

Summaries: `gold_locality_price_summary`, `gold_listing_performance_summary`, `gold_lead_conversion_summary`, `gold_broker_performance_summary`, `gold_inventory_age_summary`.

## Source rule
Power BI consumes Gold outputs only. Raw, Bronze, Silver Candidate, Trusted detail and Quarantine tables are not direct dashboard sources.

## Validation
Trace important visuals to their owning Gold object and reconcile under the same filter context. Keep listing and lead facts separate to prevent fan-out.
