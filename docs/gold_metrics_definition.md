# Gold Metrics Definition

**Week:** 7  
**Input:** Trusted Silver only.

## Gold table catalog
| Object | Grain |
|---|---|
| `gold_dim_date` | one calendar date |
| `gold_dim_locality` | one locality_id |
| `gold_dim_property` | one property_type + furnishing combination |
| `gold_dim_broker` | one broker_id |
| `gold_dim_listing_status` | one listing_status |
| `gold_dim_price_band` | one documented price band |
| `gold_dim_lead_channel` | one lead_channel |
| `gold_fact_listing` | one Trusted physical listing / record_uid |
| `gold_fact_lead` | one Trusted physical lead / record_uid |
| `gold_locality_price_summary` | one locality_id |
| `gold_listing_performance_summary` | one locality_id |
| `gold_lead_conversion_summary` | one locality_id |
| `gold_broker_performance_summary` | one broker_id |
| `gold_inventory_age_summary` | one locality_id |

## Eight KPI contracts
1. **Active Listings:** distinct Trusted listings with active status.
2. **Median Listing Price:** median Trusted asking price at listing grain.
3. **Median Price per Sq Ft:** median Trusted `price_per_sqft`; never calculate after lead fan-out.
4. **Lead Conversion Rate:** closed listings after qualified lead ÷ listings with qualified leads × 100.
5. **Average Leads per Listing:** Trusted leads ÷ listings receiving leads; zero-lead listings excluded from denominator.
6. **Average Days on Market:** status-aware days from creation to completion/today.
7. **Stale Listing Rate:** active listings older than the declared threshold ÷ active listings × 100.
8. **DQ Pass Rate:** Trusted evaluated rows ÷ total evaluated input rows × 100.

**Zero denominator:** return NULL/blank via `NULLIF(denominator, 0)`.

**Stale threshold:** the notebook currently uses **90 days as a working parameter**. The approved playbook requires a documented threshold but does not publish a numeric value; the repository does not contain mentor approval for 90 days, so it must not be described as an approved final policy.

## Join safety
- `gold_fact_listing` never joins leads.
- `gold_fact_lead` remains at lead grain.
- Listing-to-lead summaries re-aggregate to listing grain before locality roll-up.
- Lookup keys are checked for uniqueness before joins.
- Summary outputs are reconciled to their owning facts.
