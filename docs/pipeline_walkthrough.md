# Pipeline Walkthrough

## Run order
1. `src/generate_synthetic_data.py`
2. `notebooks/01_data_exploration.ipynb`
3. `notebooks/02_bronze_ingestion.ipynb`
4. `notebooks/03_silver_transformations.ipynb`
5. `notebooks/04_data_quality_checks.ipynb`
6. `notebooks/05_gold_aggregations.ipynb`
7. `notebooks/06_powerbi_export.ipynb`
8. Power BI three-page Gold-only dashboard
9. `notebooks/07_streaming_simulation.ipynb`

## Architecture
Raw Sources → Bronze → Silver Candidate → Data Quality → Trusted/Quarantine → Gold → Power BI.

Streaming: JSON landing → Auto Loader → streaming Bronze → classification → Trusted streaming Silver / Quarantine.

## Source-to-dashboard trace
Power BI visual → Gold field/measure → owning Gold table → validation query → Trusted Silver input → source record.

Listing and lead facts remain separate to prevent one-to-many lead fan-out from inflating listing metrics.

## Recovery
Never patch Gold directly to repair upstream data. Re-run from the earliest affected layer, then rerun DQ, Gold validation and the Power BI handoff.

## Limitations
- Data is synthetic and educational.
- The stale-listing threshold is a 90-day working parameter; mentor approval is not recorded in this repository.
- Full governed-domain validation for P15-DQ-07 requires an approved domain table that was unavailable in the execution environment.
- Streaming is a controlled simulation, not production Kafka.

## Review runbook
Read the README/data dictionary; run Week 03 profiling; run Bronze→Silver Candidate; run full DQ and verify zero reconciliation variance/overlap; run Gold and its join/rerun checks; open the three-page dashboard and trace important KPIs; run the Week-10 controlled drops.
