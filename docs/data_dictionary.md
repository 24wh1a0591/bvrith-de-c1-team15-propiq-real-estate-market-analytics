# Data Dictionary

**Week:** 2  
**Purpose:** Define the source datasets, reference datasets, canonical Silver schema, and streaming event schema used in the PropIQ Real Estate Market Analytics project.

---

## 1. Source File Catalog

| File Name | Grain | Purpose | Approx. Rows | Notes |
|---|---|---|---:|---|
| `listings.parquet` | One row per property listing | Stores property listing details including price, property type, broker, locality, and listing status | As provided | Primary source dataset |
| `leads.csv` | One row per buyer lead | Stores buyer enquiries and lead information associated with property listings | As provided | Transactional dataset |
| `localities.json` | One row per locality | Stores locality master information such as locality name, city, zone, and market segment | As provided | Reference/master dataset |
| `brokers.csv` | One row per broker | Stores broker and agency information including broker tier and service rating | As provided | Reference/master dataset |
| `listing_status_event_drop_*.json` | One row per listing status event | Simulates streaming updates for property listing status changes | Varies | Used for Week 10 streaming implementation |

---

## 2. Raw File Schema: `listings.parquet`

| Field Name | Data Type | Required? | Example | Description |
|---|---|---|---|---|
| `record_uid` | String | Yes | REC000001 | Physical unique record identifier |
| `listing_id` | String | Yes | LIST100001 | Business identifier for the property listing |
| `locality_id` | String | Yes | LOC001 | References the locality where the property is located |
| `broker_id` | String | Yes | BR001 | References the broker managing the listing |
| `property_type` | String | Yes | Apartment | Type of property |
| `bedrooms` | Integer | No | 3 | Number of bedrooms |
| `built_up_area_sqft` | Double | Yes | 1450.5 | Built-up area in square feet |
| `asking_price_inr` | Decimal | Yes | 8500000 | Property asking price in INR |
| `price_per_sqft` | Decimal | Yes | 5862 | Price per square foot |
| `listing_status` | String | Yes | Active | Current listing status |
| `listing_created_date` | Date | Yes | 2026-06-15 | Date when the listing was created |

---

## 3. Raw File Schema: `leads.csv`

| Field Name | Data Type | Required? | Example | Description |
|---|---|---|---|---|
| `record_uid` | String | Yes | REC100001 | Physical unique record identifier |
| `lead_id` | String | Yes | LEAD000001 | Unique lead identifier |
| `listing_id` | String | Yes | LIST100001 | Property listing associated with the lead |
| `lead_channel` | String | Yes | Website | Source from which the lead was generated |
| `buyer_intent` | String | No | High | Buyer's interest level |
| `qualified_flag` | Boolean | Yes | TRUE | Indicates whether the lead is qualified |
| `lead_status` | String | Yes | Contacted | Current status of the lead |

---

## 4. Reference File Schema

### `localities.json`

| Field Name | Data Type | Required? | Example | Description |
|---|---|---|---|---|
| `locality_id` | String | Yes | LOC001 | Unique locality identifier |
| `locality_name` | String | Yes | Gachibowli | Name of the locality |
| `city` | String | Yes | Hyderabad | City where the locality exists |
| `city_zone` | String | Yes | West | Zone within the city |
| `market_segment` | String | Yes | Premium | Market classification |

### `brokers.csv`

| Field Name | Data Type | Required? | Example | Description |
|---|---|---|---|---|
| `broker_id` | String | Yes | BR001 | Unique broker identifier |
| `agency_name` | String | Yes | ABC Realty | Name of the broker agency |
| `broker_tier` | String | Yes | Gold | Broker performance tier |
| `service_rating` | Decimal | No | 4.6 | Customer service rating |

---

## 5. Canonical Silver Table Design

Final Silver tables

```text
silver_listings
silver_leads
silver_localities
silver_brokers
```

### Example: `silver_listings`

| Silver Field | Data Type | Source Mapping | Business Meaning |
|---|---|---|---|
| `record_uid` | String | listings.record_uid | Physical unique record identifier |
| `listing_id` | String | listings.listing_id | Business listing identifier |
| `listing_created_date` | Date | listings.listing_created_date | Listing creation date |
| `locality_id` | String | listings.locality_id | Locality reference |
| `broker_id` | String | listings.broker_id | Broker reference |
| `asking_price_inr` | Decimal | listings.asking_price_inr | Property asking price |
| `price_per_sqft` | Decimal | listings.price_per_sqft | Price per square foot |
| `listing_status` | String | listings.listing_status | Current property listing status |

---

## 6. Streaming Event Schema

| Field Name | Data Type | Required? | Example | Description |
|---|---|---|---|---|
| `event_id` | String | Yes | EVT000001 | Unique streaming event identifier |
| `event_timestamp` | Timestamp | Yes | 2026-07-03T10:15:00+05:30 | Timestamp when the event occurred |
| `listing_id` | String | Yes | LIST100001 | Property listing associated with the event |
| `event_type` | String | Yes | STATUS_UPDATED | Type of streaming event |
| `old_status` | String | No | Active | Previous listing status |
| `new_status` | String | Yes | Sold | Updated listing status |
| `record_uid` | String | Yes | REC000001 | Physical record identifier associated with the event |
