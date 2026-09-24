# PropIQ — Power BI Dashboard

**Project:** P15 PropIQ — Real Estate Market Analytics  
**Team:** Team 15  
**Week:** 9  
**Platform:** Microsoft Power BI  
**Data Layer:** Gold  

---

## 1. Dashboard Overview

The PropIQ Power BI dashboard provides a Gold-layer analytical view of:

- Real-estate listing activity
- Property pricing
- Price per square foot
- Locality performance
- Property-type distribution
- Broker performance
- Lead channels
- Lead conversion
- Inventory age

The dashboard continues the approved Week-8 Power BI model and is refined during Week 9.

**Source rule:** Power BI uses approved Gold-layer outputs only.

Raw, Bronze, Silver Candidate, Trusted Silver detail, and Quarantine data are not used directly by the dashboard.

---

## 2. Dashboard Pages

| Page | Purpose | Main Visuals |
|---|---|---|
| Page 1: Market Overview | Overall market summary | KPI cards, monthly trend, property/price distribution, locality inventory |
| Page 2: Locality & Pricing Intelligence | Compare pricing and inventory across locations | Median price, price/sqft, locality comparison, property-type pricing |
| Page 3: Listing / Broker / Lead | Analyse listing, broker and lead performance | Broker performance, lead channels, conversion, inventory age, lead analysis |

---

## 3. Gold Tables Used

| Gold Table | Purpose | Dashboard Use |
|---|---|---|
| `gold_dim_date` | Date dimension | Date filtering and trends |
| `gold_dim_locality` | Locality dimension | Locality filtering and comparison |
| `gold_dim_property` | Property dimension | Property-type analysis |
| `gold_dim_broker` | Broker dimension | Broker analysis |
| `gold_dim_listing_status` | Listing status | Listing status analysis |
| `gold_dim_price_band` | Price-band dimension | Price-band analysis |
| `gold_dim_lead_channel` | Lead-channel dimension | Lead-channel analysis |
| `gold_fact_listing` | Listing-level fact | Listings, pricing, inventory and trends |
| `gold_fact_lead` | Lead-level fact | Leads and conversion |
| `gold_locality_price_summary` | Locality pricing summary | Locality and pricing analysis |
| `gold_listing_performance_summary` | Listing performance | Listing KPIs |
| `gold_lead_conversion_summary` | Lead conversion | Conversion KPIs |
| `gold_broker_performance_summary` | Broker performance | Broker comparison |
| `gold_inventory_age_summary` | Inventory age | Days-on-market/inventory analysis |

---

## 4. Page-to-Gold Mapping

| Dashboard Page | Gold Table(s) Used | Important Fields / Metrics |
|---|---|---|
| Market Overview | `gold_fact_listing`, `gold_fact_lead`, `gold_listing_performance_summary`, `gold_lead_conversion_summary` | Active listings, median price, price/sqft, leads, conversion |
| Locality & Pricing Intelligence | `gold_locality_price_summary`, `gold_fact_listing`, `gold_dim_locality`, `gold_dim_property`, `gold_dim_price_band` | Locality, median price, median price/sqft, property type, price band |
| Listing / Broker / Lead | `gold_fact_listing`, `gold_fact_lead`, `gold_broker_performance_summary`, `gold_lead_conversion_summary`, `gold_inventory_age_summary`, `gold_dim_broker`, `gold_dim_lead_channel` | Broker performance, leads, conversion, lead channels, inventory age |

---

## 5. Main KPIs

The dashboard uses approved Gold KPI definitions.

### Market KPIs

- Active Listings
- Median Listing Price
- Median Price / Sq Ft
- Total Trusted Leads
- Lead Conversion Rate

### Operational KPIs

- Listing Performance
- Broker Performance
- Lead Channel Distribution
- Average Leads per Listing
- Average Days on Market
- Inventory Age

KPI definitions are not recreated independently in Power BI when an approved Gold definition already exists.

---

## 6. Power BI Model

The model keeps listing and lead facts separate.

```text
Gold Dimensions
       |
       | 1 : *
       v
gold_fact_listing


Gold Dimensions
       |
       | 1 : *
       v
gold_fact_lead
