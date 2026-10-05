# Final Project Report

**Project:** P15 PropIQ — Real Estate Market Analytics  
**Team:** Team 15  
**Students:** Thota Madhulika; P. Lakshmi Naga Sree; Vadlamuru Rishitha

## 1. Executive summary
PropIQ builds a trusted educational real-estate analytics pipeline from synthetic listings, leads, locality and broker data. It profiles source grain, ingests Bronze, creates Silver Candidate data, routes records through eight DQ rules into Trusted/Quarantine, builds Gold dimensions/facts/summaries, and exposes the Gold layer through a three-page Power BI dashboard. A controlled file-based Structured Streaming simulation demonstrates event-time, deduplication, sequence, schema-drift and quarantine controls.

## 2. Architecture
Raw Sources → Bronze → Silver Candidate → Data Quality → Trusted/Quarantine → Gold → Power BI.

Streaming: JSON drops → Auto Loader → streaming Bronze → classification → Trusted streaming Silver / Quarantine.

## 3. DQ evidence
Week 06 captured 50,200 listing Candidate records, 120,800 lead Candidate records, 80 locality records and 320 broker records. Reconciliation variance was zero for every entity; Trusted/Quarantine overlap was zero.

Rule failures: DQ-01 500; DQ-02 200; DQ-03 200; DQ-04 350; DQ-05 150; DQ-06 1,200; DQ-07 0 in the executed run; DQ-08 1,600.

## 4. Gold
Seven dimensions, two facts and five summaries are built from Trusted Silver only. Listing and lead facts remain separate to prevent fan-out. Eight KPI contracts use explicit numerator/denominator and zero-denominator behavior.

## 5. Power BI
The dashboard has three pages: Market Overview; Locality & Pricing Intelligence; Listing / Broker / Lead. Power BI consumes Gold outputs only.

## 6. Streaming
Six controlled drops produced 19 physical Bronze records, 12 Trusted and 7 Quarantine. Final reconciliation reported zero unaccounted records and zero required control violations. The no-new-file rerun preserved 19/12/7 and 12 distinct trusted event IDs.

## 7. Limitations
- Data is synthetic and educational.
- The stale-listing threshold is a documented 90-day working parameter; mentor approval is not recorded.
- Full P15-DQ-07 governed-domain validation requires an approved domain table unavailable in the execution environment.
- Streaming is a controlled simulation, not production Kafka.

## 8. Evidence
`notebooks/`, `docs/`, `dashboard/`, `streaming/`, `screenshots/`, `weekly_logs/` and `final_submission/`.

## 9. Reflection
The project demonstrates that analytical numbers are traceable to governed data, explicit grain, validation and reconciliation rather than being produced only as dashboard visuals.
