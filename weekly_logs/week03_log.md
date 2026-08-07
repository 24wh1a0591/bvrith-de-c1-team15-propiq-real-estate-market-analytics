# Week 03 Log — Data Exploration & Source Validation

**Week:** 3  
**Date range:** [Add dates]  
**Team:** Team 15  
**Project:** PropIQ – Real Estate Market Analytics  

---

## 1. Sprint Goal

The objective of this sprint was to explore the PropIQ source datasets in Databricks, understand their structure, validate data quality, and prepare the foundation for the Bronze layer. The team created temporary SQL views, performed validation checks, and implemented a Bronze demonstration workflow.

---

## 2. Work Completed

| Task | Owner | Status | Evidence |
|------|------|--------|----------|
| Uploaded PropIQ source files to Databricks Volume | Thota Madhulika | Done | Databricks Volume |
| Explored Listings and Localities datasets | Thota Madhulika | Done | `01_data_exploration.ipynb` |
| Explored Leads and Brokers datasets | P. Lakshmi Naga Sree | Done | Notebook |
| Created PySpark DataFrames for all datasets | Thota Madhulika | Done | Notebook |
| Created temporary Spark SQL views | P. Lakshmi Naga Sree | Done | Databricks Notebook |
| Performed schema exploration and business key identification | Vadlamuru Rishitha | Done | Notebook screenshots |
| Performed row count and distinct key validation | Vadlamuru Rishitha | Done | SQL Queries |
| Checked missing values and invalid records | Vadlamuru Rishitha | Done | Notebook |
| Validated relationships (Listings ↔ Leads) | All Members | Done | SQL Join Validation |
| Created Bronze demonstration table | P. Lakshmi Naga Sree | Done | `propiq_week03_bronze_demo_listings` |
| Performed source-to-demo reconciliation | Vadlamuru Rishitha | Done | SQL Results |
| Created lineage demonstration view | Thota Madhulika | Done | `propiq_week03_lineage_demo_view` |
| Added notebook documentation and explanations | All Members | Done | GitHub Repository |

---

## 3. Key Decisions

- Used Spark SQL as the primary language for structured exploration and validation.
- Implemented only one Bronze demonstration table as per Week-3 scope instead of full ingestion.
- Restricted implementation strictly to exploration and validation without moving into Silver/Gold layers.
- Used temporary SQL views to validate transformations before persistence.

---

## 4. Blockers / Risks

| Blocker | Impact | Help Needed |
|--------|--------|-------------|
| PageLoop notebook mismatch with PropIQ schema | Required significant query modifications | Verified mappings using playbook and data dictionary |
| Dataset path issues in Databricks | Execution failures | Corrected volume paths and file references |
| Schema differences between datasets | Increased debugging time | Manual validation of schemas and keys |

---

## 5. Evidence Added to GitHub

- Updated `notebooks/01_data_exploration.ipynb`  
- Added Week-3 exploration screenshots  
- Added SQL validation queries  
- Added Bronze demonstration table implementation  
- Added lineage demonstration view  
- Updated documentation  

---

## 6. AI Transparency Note

| Question | Response |
|---------|----------|
| Where AI helped | Helped convert PageLoop notebook logic into PropIQ context and improve documentation clarity |
| What we changed after AI suggestion | Corrected dataset paths, replaced schema fields, and fixed SQL queries |
| What we verified manually | Schema validation, query execution, temporary views, Bronze demo table, and lineage checks |
| What we can explain without AI | Full exploration workflow, validation logic, Spark SQL usage, and Bronze demo implementation |

---

## 7. Next Week Preparation

- Implement full Bronze layer ingestion for all datasets  
- Standardize ingestion into Delta tables  
- Begin planning Silver Candidate transformations  
- Prepare for data quality checks and reconciliation  

---