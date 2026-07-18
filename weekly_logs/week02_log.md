# Week 02 Log — Data Pack, Contracts & Assumptions

**Week:** 2  
**Date range:** 18 July 2026 – 24 July 2026  
**Team:** Team 15  
**Project:** PropIQ – Real Estate Market Analytics

---

## 1. Sprint Goal

Understand the supplied PropIQ Data Pack and establish a clear understanding of every source dataset, its schema, relationships, and business purpose. Document the dataset contracts, synthetic data assumptions, and prepare the project repository for subsequent engineering tasks.

---

## 2. Work Completed

| Task | Owner | Status | Evidence |
|---|---|---|---|
| Reviewed PropIQ Project Playbook and Week 2 requirements | Team 15 | Done | Project Playbook |
| Inspected Listings, Leads, Brokers and Localities source datasets | Team 15 | Done | Data Pack |
| Verified dataset formats (Parquet, CSV and JSON) | Team 15 | Done | Source files |
| Documented source datasets and business purpose | Team 15 | Done | `docs/data_dictionary.md` |
| Documented synthetic data assumptions | Team 15 | Done | `docs/synthetic_data_assumptions.md` |
| Created sample raw dataset folder for repository | Team 15 | Done | `data_sample/raw/` |
| Verified primary entities and dataset relationships | Team 15 | Done | Repository documentation |

---

## 3. Key Decisions

- Use the supplied PropIQ synthetic datasets without modifying the original source files.
- Preserve the original source schema and document all field definitions before implementing Bronze ingestion.

---

## 4. Blockers / Risks

| Blocker | Impact | Help Needed |
|---|---|---|
| Understanding the complete source relationships before pipeline implementation | Incorrect joins could produce duplicate business metrics | Verified schema and relationships using the project documentation before development |

---

## 5. Evidence Added to GitHub

- Added `docs/data_dictionary.md`
- Added `docs/synthetic_data_assumptions.md`
- Added sample source datasets under `data_sample/raw/`
- Updated Week 02 documentation
- Repository commit containing Week 02 deliverables

---

## 6. AI Transparency Note

| Question | Response |
|---|---|
| Where AI helped | Assisted in organizing the documentation, improving technical wording, and formatting the Markdown files according to the project templates. |
| What we changed after AI suggestion | Updated documentation to match the actual PropIQ dataset, corrected terminology, and aligned descriptions with the project playbook. |
| What we verified manually | Verified dataset names, row counts, file formats, field names, primary keys, foreign keys, and relationships using the supplied Data Pack and Project Playbook. |
| What we can explain without AI | Source datasets, business purpose, schema, entity relationships, synthetic data assumptions, repository structure, and Week 2 deliverables. |

---

## 7. Next Week Preparation

- Perform detailed data profiling and schema validation for every source dataset.
- Analyse entity relationships, join cardinality, and potential data quality issues before designing the Bronze layer.