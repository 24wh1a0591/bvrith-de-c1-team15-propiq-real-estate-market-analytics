# Synthetic Data Assumptions

**Week:** 2  
**Purpose:** Document how synthetic real estate market data is created.

---

## 1. Synthetic Data Boundary

This project uses synthetic real estate market data only. It must not be presented as real property listings, brokers, agencies, buyers, customers, companies, or government records. All datasets are fictional and created solely for educational purposes to demonstrate data engineering concepts including ingestion, transformation, data quality validation, and analytics.

---

## 2. Domain Assumptions

| Area | Assumption |
|---|---|
| Geography / scope | Synthetic property market covering multiple Indian cities including Hyderabad, Bengaluru, and Pune through fictional localities. |
| Time period | Listings, broker data, and buyer leads represent activity primarily during 2024–2026, with controlled future timestamps included only for data quality testing. |
| Source systems | Four independent operational source systems: Listings, Localities, Leads, and Brokers, plus controlled listing status event drops for streaming simulation. |
| Event types | Property listing creation, price updates, listing status changes, buyer lead generation, broker management, and controlled streaming events. |
| Reference data | Localities, cities, zones, market segments, brokers, property types, and pricing reference values. |

---

## 3. Data Volume Assumptions

| File | Approximate Rows | Reason |
|---|---:|---|
| `listings.parquet` | 50,200 | Primary property listing dataset used as the central business entity. |
| `leads.csv` | 120,800 | Simulates multiple buyer enquiries for each property listing. |
| `brokers.csv` | 320 | Synthetic broker and agency master data. |
| `localities.json` | 80 | Locality reference data used for enrichment and analytics. |
| `listing_status_event_drop_01–06.json` | Small controlled event batches | Used to simulate streaming scenarios including duplicates, late events, malformed records, invalid payloads, and schema drift. |

---

## 4. Controlled Data Quality Issues

| Issue Type | Approx. Share | Why Include It |
|---|---:|---|
| Duplicate IDs | 0.2%–0.5% | Tests duplicate detection and deduplication logic. |
| Missing values | 1%–3% | Tests completeness and null-value handling. |
| Invalid reference keys | 0.5%–1% | Tests foreign key and referential integrity validation. |
| Negative / impossible values | 0.1%–0.5% | Tests business rule and numeric range validation. |
| Timestamp inconsistencies | 0.1%–0.3% | Tests chronology, late-arriving data, and event ordering. |

---

## 5. Manual Verification

Before using generated data, the team must check:

- Row counts match the expected dataset sizes.
- Primary and foreign key fields exist in every source.
- Dates, prices, areas, ratings, and other numeric values fall within realistic ranges.
- Controlled data quality issues are present only in small quantities and do not dominate the dataset.
- Source files represent different business entities and require proper standardization before integration.
