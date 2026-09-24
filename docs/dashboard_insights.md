# Dashboard Insights

**Week:** 9  
**Purpose:** Explain what the Power BI dashboard shows.

---

## 1. Dashboard Pages

| Page | Purpose | Main Visuals |
|---|---|---|
| Page 1: Market Overview | High-level real-estate market summary | Active listings, lead metrics, monthly listing trend, property type/price-band distribution, locality inventory, listing-age distribution |
| Page 2: Locality & Pricing Intelligence | Analyse locality-level pricing and inventory patterns | Median listing price, median price/sqft, locality comparison, property-type pricing, locality pricing table |
| Page 3: Listing / Broker / Lead | Analyse listing, broker and lead performance | Broker performance, lead-channel distribution, lead conversion, inventory age, average days on market, average leads per listing, lead funnel |

---

## 2. Key Insights

Write 5–8 insights from the dashboard.

1. **Market Overview:**  
   The Market Overview page provides a consolidated view of active listings, pricing, lead activity, listing trends and inventory age.

2. **Listing Trend:**  
   The monthly listing trend can be used to identify changes in listing activity over the selected reporting period.

3. **Property and Price Distribution:**  
   The property-type and price-band visual shows how listings are distributed across different property configurations and price segments.

4. **Locality Inventory:**  
   The locality inventory visual compares active listing volumes across localities and helps identify differences in available inventory.

5. **Locality Pricing:**  
   The Locality & Pricing Intelligence page compares median listing prices and median price per square foot across localities.

6. **Property-Type Pricing:**  
   Property-type analysis allows differences in price per square foot to be compared across property configurations.

7. **Broker and Lead Performance:**  
   The Listing / Broker / Lead page compares broker-level listing performance together with qualified lead activity.

8. **Lead and Inventory Performance:**  
   Lead conversion, lead-channel distribution, average leads per listing, stale listing rate and average days on market provide an operational view of listing and lead performance.

> **Note:** Any numerical claim, highest/lowest ranking, percentage, or specific locality/broker observation must be added only after verifying the displayed Power BI value against the corresponding Gold table.

---

## 3. How the Dashboard Uses Gold Tables

| Dashboard Page | Gold Table Used | Important Fields |
|---|---|---|
| Market Overview | `gold_locality_price_summary` | `active_listings`, `median_price_per_sqft`, `median_listing_price` |
| Market Overview | `gold_fact_listing` | `listing_id`, `listing_created_date`, `is_completed`, `days_on_market_status_aware` |
| Market Overview | `gold_fact_lead` | `lead_id` |
| Market Overview | `gold_lead_conversion_summary` | `lead_conversion_rate_pct` |
| Market Overview | `gold_dim_date` | `date_key` |
| Market Overview | `gold_dim_locality` | `city`, `locality_name` |
| Market Overview | `gold_dim_property` | `property_type` |
| Market Overview | `gold_dim_price_band` | `price_band` |
| Locality & Pricing Intelligence | `gold_locality_price_summary` | `locality_name`, `total_listings`, `median_listing_price`, `median_price_per_sqft`, `active_listings` |
| Locality & Pricing Intelligence | `gold_fact_listing` | `calculated_price_per_sqft`, `price_per_sqft`, `listing_id` |
| Locality & Pricing Intelligence | `gold_dim_locality` | `locality_name`, `city` |
| Locality & Pricing Intelligence | `gold_dim_property` | `property_type` |
| Locality & Pricing Intelligence | `gold_dim_date` | `date_key` |
| Listing / Broker / Lead | `gold_broker_performance_summary` | `agency_name`, `Qualified Lead Rate`, `total_listings` |
| Listing / Broker / Lead | `gold_dim_lead_channel` | `lead_channel` |
| Listing / Broker / Lead | `gold_fact_lead` | `lead_id`, `lead_timestamp`, `lead_channel_key`, `listing_id`, `lead_status`, `buyer_intent`, `qualified_flag` |
| Listing / Broker / Lead | `gold_lead_conversion_summary` | `lead_conversion_rate_pct`, `avg_leads_per_listing` |
| Listing / Broker / Lead | `gold_inventory_age_summary` | `stale_listing_rate_pct` |
| Listing / Broker / Lead | `gold_listing_performance_summary` | `active_listing_count`, `stale_listing_count`, `avg_days_on_market` |
| Listing / Broker / Lead | `gold_dim_locality` | `locality_name` |
| Listing / Broker / Lead | `gold_dim_property` | `property_type` |
| Listing / Broker / Lead | `gold_dim_date` | `date_key` |

---

## 4. Power BI Validation

- [ ] Dashboard connects to Gold outputs only.
- [ ] Market Overview uses approved Gold listing, lead, locality, property and price-band sources.
- [ ] Locality & Pricing Intelligence uses approved Gold pricing and listing sources.
- [ ] Listing / Broker / Lead uses approved Gold broker, listing, lead and inventory sources.
- [ ] Filters work correctly.
- [ ] Date, locality, city and property-type filters behave as expected.
- [ ] KPI totals match Gold table checks.
- [ ] Lead conversion matches the approved Gold definition.
- [ ] Pricing metrics match the approved Gold definitions.
- [ ] Listing and lead facts are not incorrectly joined in a way that creates fan-out.
- [ ] Important dashboard values reconcile with their owning Gold tables.
- [ ] Screenshots are saved in `screenshots/`.
- [ ] Dashboard story is explainable by all students.

---

## 5. Dashboard Insight Traceability

Each important dashboard observation should be traceable through:

```text
Power BI Visual
      ↓
Power BI Measure / Field
      ↓
Owning Gold Table
      ↓
Gold Validation Query
      ↓
Verified Business Observation
