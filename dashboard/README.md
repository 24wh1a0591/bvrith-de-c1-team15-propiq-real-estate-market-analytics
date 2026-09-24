# PropIQ Power BI Dashboard

## 1. Purpose

This dashboard provides a business-facing view of
real-estate listing, lead, locality, broker and inventory
performance using validated Gold-layer data.

## 2. Gold Sources

| Gold Table | Grain | Purpose |
|---|---|---|
| gold_fact_listing | one row per listing | Listing KPIs |
| gold_fact_lead | one row per lead | Lead/conversion KPIs |
| gold_dim_locality | one row per locality | Locality analysis |
| gold_dim_property | one row per property | Property analysis |
| gold_dim_broker | one row per broker | Broker performance |
| ... | ... | ... |

## 3. Power BI Tables

Document the mapping:

Gold table → Power BI table

## 4. Relationships

Document:

- relationship
- cardinality
- filter direction
- reason

## 5. Measures

List the DAX measures.

## 6. Dashboard Pages

### Page 1 — Market Overview

Business questions:
- How many active listings exist?
- What is the median listing price?
- What is the median price per sq ft?
- How are listings changing monthly?
- Which localities have higher inventory?

## 7. Validation

Power BI values are reconciled against
their owning Gold tables.

## 8. Refresh

Document how the Gold exports are regenerated
and refreshed.

## 9. Known Limitations

Document anything not yet implemented.

## 10. Week 9 Handoff

The same PBIX will continue into Week 9
for dashboard refinement and insight development.
