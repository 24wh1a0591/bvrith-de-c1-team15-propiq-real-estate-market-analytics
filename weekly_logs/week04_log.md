# Week 04 Log — Source-to-Bronze Ingestion

**Week:** 4
**Date range:** [31.07.2026]
**Team:** P15 — PropIQ
**Project:** PropIQ Real Estate Market Analytics

---

## 1. Sprint Goal

Move all four approved PropIQ batch source files — `listings.parquet`,
`leads.csv`, `localities.json`, `brokers.csv` — into persistent Bronze Delta
tables in `workspace.default`, preserving source business values exactly and
adding controlled ingestion/lineage metadata. Prove that source and Bronze
counts reconcile and that rerunning the notebook does not create duplicates.

---

## 2. Work Completed

| Task | Owner | Status | Evidence |
|---|---|---|---|
| Confirm catalog/schema (`workspace.default`) and Volume path (`/Volumes/workspace/default/propiq`) | [Student] | [Done / In progress] | `notebooks/02_bronze_ingestion.ipynb` Part 3.2 |
| Confirm all 4 approved batch files visible in the Volume | [Student] | [Done / In progress] | `evidence/week_04/W04-E01` |
| Build `bronze_propiq_listings` from `listings.parquet` (Parquet reader) | [Student] | [Done / In progress] | `notebooks/02_bronze_ingestion.ipynb` Part 3; `evidence/week_04/W04-E02` |
| Build `bronze_propiq_leads` from `leads.csv` (CSV reader) | [Student] | [Done / In progress] | `notebooks/02_bronze_ingestion.ipynb` Part 4; `evidence/week_04/W04-E03` |
| Build `bronze_propiq_localities` from `localities.json` (JSON Lines reader) | [Student] | [Done / In progress] | `notebooks/02_bronze_ingestion.ipynb` Part 5; `evidence/week_04/W04-E04` |
| Build `bronze_propiq_brokers` from `brokers.csv` (CSV reader) | [Student] | [Done / In progress] | `notebooks/02_bronze_ingestion.ipynb` Part 6; `evidence/week_04/W04-E05` |
| Consolidated source-vs-Bronze reconciliation (4 sources) | [Student] | [Done / In progress] | `evidence/week_04/W04-E06` |
| Metadata completeness check (all Bronze tables) | [Student] | [Done / In progress] | `notebooks/02_bronze_ingestion.ipynb` Part 7.3 |
| Rerun proof on `bronze_propiq_brokers` (before/after counts) | [Student] | [Done / In progress] | `evidence/week_04/W04-E07` |
| `DESCRIBE HISTORY bronze_propiq_brokers` captured | [Student] | [Done / In progress] | `evidence/week_04/W04-E08` |
| Confirm all 4 Bronze tables visible in Catalog Explorer | [Student] | [Done / In progress] | `evidence/week_04/W04-E09` |

---

## 3. Key Decisions

- Streaming files (`listing_status_event_drop_01`–`06.json`) were **excluded**
  from Week 4. Per the Data Pack manifest and README, they are first used in
  Week 10 and belong to the streaming-simulation phase, not controlled batch
  ingestion.
- Used the standard Databricks Parquet reader for `listings.parquet` and
  explicit `STRING`-typed schemas with `PERMISSIVE` mode for the CSV/JSON
  sources, per Section 5 of the Week-4 Student Guide.
- `_rescued_payload` was added only to the CSV and JSON Bronze tables
  (`leads`, `localities`, `brokers`), since only those readers run in
  `PERMISSIVE` mode with a declared corrupt-record column. The Parquet
  reader used for `listings` has no equivalent, so the column is
  intentionally omitted there.
- `_record_hash` is built from each source's own business columns in a fixed
  order (including the physical `record_uid` for `listings` and `leads`,
  which carry it; `localities` and `brokers` are master data without a
  `record_uid`, so their hash uses their full business-column set instead).
- One shared `ingestion_run_id` (`W04_PROPIQ_RUN01`) and `schema_version`
  (`propiq_source_v1.0`) were used across all four sources for this
  controlled run, kept unchanged through the rerun proof.
- Confirmed `localities.json` is present in the Volume before this week's
  run — the Week-3 exploration notebook only loaded 3 of the 4 approved
  files, so this was double-checked rather than assumed.

---

## 4. Blockers / Risks

| Blocker | Impact | Help Needed |
|---|---|---|
| [Blocker, e.g. Volume upload of `localities.json` not yet confirmed] | [Impact] | [Help needed] |

---

## 5. Evidence Added to GitHub

- `notebooks/02_bronze_ingestion.ipynb` — completed Week-4 notebook
- `evidence/week_04/W04-E01` — Volume listing (4 approved files visible)
- `evidence/week_04/W04-E02` – `W04-E05` — Bronze schema/table details per source
- `evidence/week_04/W04-E06` — consolidated reconciliation result (all `MATCH`)
- `evidence/week_04/W04-E07` — rerun before/after count proof
- `evidence/week_04/W04-E08` — `DESCRIBE HISTORY` output for `bronze_propiq_brokers`
- `evidence/week_04/W04-E09` — Catalog Explorer screenshot (4 Bronze tables)

---

## 6. AI Transparency Note

| Question | Response |
|---|---|
| Where AI helped | Claude was used to structure `notebooks/02_bronze_ingestion.ipynb` from the ZENAIZ Week-4 Student Guide, applying it to PropIQ's own `data_dictionary.md` and the Data Pack's `source_manifest.csv` (filenames, formats, business keys, Bronze table names). It also drafted this log template with project-specific content. |
| What we changed after AI suggestion | [Explain any edits the team made after reviewing the generated notebook/log — e.g. corrected paths, added missing file, adjusted metadata fields] |
| What we verified manually | The team ran every cell in Databricks, confirmed the four source files existed in the Volume, checked actual source/Bronze row counts, confirmed reconciliation showed `MATCH`, and independently ran the rerun-proof and `DESCRIBE HISTORY` steps rather than trusting the notebook's claims. |
| What we can explain without AI | Why Bronze preserves untouched source values, what each metadata column proves, how the reconciliation and rerun-safety checks work, and why the streaming files were excluded from Week 4. |

---

## 7. Next Week Preparation

- Review Week-5 scope (Silver standardization) against `dq_requirements.md`.
- Confirm `quarantine_listings`, `quarantine_leads`, `quarantine_brokers`,
  `quarantine_localities` table contracts before DQ work begins.
- Keep `bronze_propiq_*` tables stable as the Week-5 read source; no further
  changes to Bronze once Week 4 evidence is captured.
