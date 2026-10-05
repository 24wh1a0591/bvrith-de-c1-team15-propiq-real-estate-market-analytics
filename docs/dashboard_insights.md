# Dashboard Insights

## Three-page story
1. **Market Overview:** What is happening in the market?
2. **Locality & Pricing Intelligence:** Where is inventory and how does pricing differ?
3. **Listing / Broker / Lead:** Which listings, brokers and lead channels are performing?

## Evidence rule
Only make numerical claims after checking the Power BI value against its owning Gold table under the same filter context.

## Gold traceability
| Page | Primary Gold objects |
|---|---|
| Market Overview | `gold_fact_listing`, `gold_fact_lead`, `gold_locality_price_summary`, `gold_lead_conversion_summary` |
| Locality & Pricing Intelligence | `gold_locality_price_summary`, `gold_fact_listing`, dimensions |
| Listing / Broker / Lead | `gold_broker_performance_summary`, `gold_lead_conversion_summary`, `gold_listing_performance_summary`, `gold_inventory_age_summary`, facts/dimensions |

## Validation checklist
- Gold-only sources.
- Correct fact grain.
- No lead fan-out.
- KPI definitions match `docs/gold_metrics_definition.md`.
- Filtered dashboard values reconcile to Gold.
