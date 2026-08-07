# Week 04 Log — Source-to-Bronze Ingestion

**Week:** 4  
**Date range:** 31.07.2026  
**Team:** Team 15  
**Project:** PropIQ Real Estate Market Analytics  

---

## 1. Sprint Goal

Move all four approved PropIQ batch source files — `listings.parquet`,  
`leads.csv`, `localities.json`, `brokers.csv` — into persistent Bronze Delta  
tables in `workspace.default`, preserving source values and adding ingestion  
metadata. Ensure source-to-Bronze reconciliation and rerun safety.

---

## 2. Work Completed

| Task | Owner | Status | Evidence |
|------|------|--------|----------|
| Confirm catalog/schema and Volume path | Thota Madhulika | Done | Notebook Part 3.2 |
| Verified all 4 source files in Volume | Thota Madhulika | Done | `W04-E01` |
| Built `bronze_propiq_listings` (Parquet ingestion) | Thota Madhulika | Done | Notebook Part 3, `W04-E02` |
| Built `bronze_propiq_leads` (CSV ingestion) | P. Lakshmi Naga Sree | Done | Notebook Part 4, `W04-E03` |
| Built `bronze_propiq_localities` (JSON ingestion) | P. Lakshmi Naga Sree | Done | Notebook Part 5, `W04-E04` |
| Built `bronze_propiq_brokers` (CSV ingestion) | Vadlamuru Rishitha | Done | Notebook Part 6, `W04-E05` |
| Consolidated reconciliation (source vs Bronze) | Vadlamuru Rishitha | Done | `W04-E06` |
| Metadata completeness validation | Vadlamuru Rishitha | Done | Notebook Part 7.3 |
| Rerun proof (before/after counts) | Thota Madhulika | Done | `W04-E07` |
| Captured `DESCRIBE HISTORY` output | Thota Madhulika | Done | `W04-E08` |
| Verified Bronze tables in Catalog Explorer | All Members | Done | `W04-E09` |

---

## 3. Key Decisions

- Streaming event files were excluded from Week 4 and reserved for Week 10 streaming simulation.
- Used Parquet reader for listings and explicit schema with `PERMISSIVE` mode for CSV/JSON sources.
- `_rescued_payload` applied only to CSV/JSON sources; not applicable for Parquet ingestion.
- `_record_hash` constructed using business columns per dataset to maintain lineage tracking.
- Used consistent `ingestion_run_id` and `schema_version` across all datasets.
- Verified all four datasets (including `localities.json`) before ingestion to avoid assumptions.

---

## 4. Blockers / Risks

| Blocker | Impact | Help Needed |
|--------|--------|-------------|
| Initial uncertainty in handling JSON schema for `localities.json` | Delayed ingestion logic | Resolved using playbook and schema validation |
| Path mismatches in Databricks Volume | Execution failures | Corrected file paths manually |
| Handling metadata columns consistently across datasets | Risk of inconsistent lineage tracking | Standardized ingestion logic across all tables |

---

## 5. Evidence Added to GitHub

- `notebooks/02_bronze_ingestion.ipynb` — completed ingestion notebook  
- `W04-E01` — Volume file validation  
- `W04-E02` to `W04-E05` — Bronze table creation evidence  
- `W04-E06` — reconciliation results (all MATCH)  
- `W04-E07` — rerun proof  
- `W04-E08` — `DESCRIBE HISTORY` output  
- `W04-E09` — Catalog Explorer verification  

---

## 6. AI Transparency Note

| Question | Response |
|---------|----------|
| Where AI helped | Assisted in structuring ingestion logic and aligning notebook with Week-4 requirements |
| What we changed after AI suggestion | Corrected dataset paths, refined schema handling, and standardized metadata columns |
| What we verified manually | File existence, ingestion execution, reconciliation counts, rerun safety, and table history |
| What we can explain without AI | Bronze ingestion workflow, metadata purpose, reconciliation logic, and rerun validation |

---

## 7. Next Week Preparation

- Begin Silver Candidate transformations (schema standardization and typing)  
- Review data quality requirements for Week 06  
- Keep Bronze tables unchanged for downstream processing  

---