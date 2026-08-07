# Week 02 Log — Data Pack, Contracts & Assumptions

**Week:** 2  
**Date range:** 18 July 2026 – 24 July 2026  
**Team:** Team 15  
**Project:** PropIQ – Real Estate Market Analytics  

---

## 1. Sprint Goal

Understand the supplied PropIQ Data Pack and establish a clear understanding of every source dataset, its schema, relationships, and business purpose. Document dataset contracts, synthetic data assumptions, and prepare the repository for upcoming data engineering tasks.

---

## 2. Work Completed

| Task | Owner | Status | Evidence |
|------|------|--------|----------|
| Reviewed PropIQ Project Playbook and Week 2 requirements | All Members | Done | Project Playbook |
| Inspected Listings and Localities datasets | Thota Madhulika | Done | Data Pack |
| Inspected Leads and Brokers datasets | P. Lakshmi Naga Sree | Done | Data Pack |
| Verified dataset formats (Parquet, CSV, JSON) | Vadlamuru Rishitha | Done | Source files |
| Documented dataset schema and business purpose | Thota Madhulika | Done | `docs/data_dictionary.md` |
| Documented synthetic data assumptions | P. Lakshmi Naga Sree | Done | `docs/synthetic_data_assumptions.md` |
| Created sample raw dataset folder (`data_sample/raw/`) | Vadlamuru Rishitha | Done | Repository |
| Verified primary entities and dataset relationships | All Members | Done | Documentation |

---

## 3. Key Decisions

- Use the provided PropIQ synthetic datasets without modifying original source files.
- Preserve raw schema exactly and document all field definitions before Bronze ingestion.
- Separate dataset understanding by domain (Listings/Localities vs Leads/Brokers) to improve clarity.

---

## 4. Blockers / Risks

| Blocker | Impact | Help Needed |
|--------|--------|-------------|
| Understanding dataset relationships before pipeline design | Incorrect joins could lead to wrong metrics | Verified relationships using playbook and documentation |
| Schema inconsistencies across formats | Slows documentation and validation | Manual schema comparison and validation |

---

## 5. Evidence Added to GitHub

- Added `docs/data_dictionary.md`  
- Added `docs/synthetic_data_assumptions.md`  
- Added sample datasets in `data_sample/raw/`  
- Updated Week 02 log documentation  
- Repository commit with Week 02 deliverables  

---

## 6. AI Transparency Note

| Question | Response |
|---------|----------|
| Where AI helped | Assisted in structuring documentation, improving clarity, and formatting Markdown files |
| What we changed after AI suggestion | Refined dataset descriptions, corrected terminology, aligned documentation with playbook |
| What we verified manually | Dataset schema, formats, field names, relationships, and assumptions using Data Pack |
| What we can explain without AI | Dataset structure, business purpose, schema relationships, and Week 2 documentation work |

---

## 7. Next Week Preparation

- Perform detailed data profiling and schema validation for all datasets  
- Identify data quality issues and prepare for Bronze layer ingestion  

---