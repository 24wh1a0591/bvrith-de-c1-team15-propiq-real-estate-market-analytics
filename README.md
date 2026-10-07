# PropIQ — Real Estate Market Analytics

**Program:** ZENAIZ x BVRIT Hyderabad Data Engineering Internship Program  
**Track:** Data Engineering  
**Team:** Team 15  
**Members:** Thota Madhulika; P. Lakshmi Naga Sree; Vadlamuru Rishitha

## Project
PropIQ turns synthetic property listings, locality masters, broker data, CRM leads and controlled status events into trusted market analytics.

## Architecture
Raw Sources → Bronze → Silver Candidate → Data Quality → Trusted/Quarantine → Gold → Power BI → Streaming Simulation.

## Final dashboard
The final Power BI dashboard is a **3-page Gold-only dashboard**:
1. Market Overview
2. Locality & Pricing Intelligence
3. Listing / Broker / Lead

## Repository navigation
- `docs/` — data, DQ, Gold, dashboard and pipeline contracts.
- `src/` — data generation/helpers.
- `notebooks/` — exploration through streaming.
- `dashboard/` — PBIX and dashboard documentation.
- `streaming/` — event schema/design.
- `screenshots/` — weekly visual evidence.
- `weekly_logs/` — execution and AI transparency logs.
- `final_submission/` — final report, demo and contribution.

## 12-week map
| Week | Focus |
|---:|---|
| 1 | Project framing |
| 2 | Dataset design |
| 3 | Exploration, relationships and join safety |
| 4 | Bronze ingestion |
| 5 | Silver Candidate |
| 6 | Data quality |
| 7 | Gold metrics |
| 8 | Power BI foundation |
| 9 | Dashboard refinement |
| 10 | Streaming simulation |
| 11 | Integration and traceability |
| 12 | Final submission |

## Rules
- Power BI uses Gold outputs only.
- `record_uid` is the physical reconciliation key.
- Do not invent DQ domains or KPI thresholds not supplied by the project authority.
- AI-assisted content must be verified and explainable.
- Large generated datasets should not be committed to GitHub.

## Evidence
Notebooks, logs, screenshots and final-submission files are the primary project evidence. Known governance limitations remain explicit.
