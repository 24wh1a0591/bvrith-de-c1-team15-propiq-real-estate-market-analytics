# Week 03 Log — Data Exploration & Source Validation

**Week:** 3  
**Date range:** [Add dates]  
**Team:** Team 15  
**Project:** PropIQ – Real Estate Market Analytics

---

## 1. Sprint Goal

The objective of this sprint was to explore the PropIQ source datasets in Databricks, understand their structure, validate data quality, and prepare the foundation for the Bronze layer. We also created temporary SQL views, performed relationship and integrity checks, and demonstrated a simple Bronze ingestion workflow.

---

## 2. Work Completed

| Task | Owner | Status | Evidence |
|---|---|---|---|
| Uploaded PropIQ source files to Databricks Volume | Team 15 | Done | Databricks Volume |
| Explored all Week-3 source datasets | Team 15 | Done | notebooks/01_data_exploration.ipynb |
| Created PySpark DataFrames for Listings, Leads, Brokers and Localities | Team 15 | Done | 01_data_exploration.ipynb |
| Created temporary Spark SQL views | Team 15 | Done | Databricks Notebook |
| Explored schemas and business keys | Team 15 | Done | Notebook screenshots |
| Performed physical row count validation | Team 15 | Done | SQL Queries |
| Performed distinct business-key validation | Team 15 | Done | SQL Queries |
| Checked missing values and invalid records | Team 15 | Done | Notebook |
| Validated parent-child relationships between Listings and Leads | Team 15 | Done | SQL Join Validation |
| Created Bronze demonstration table | Team 15 | Done | workspace.default.propiq_week03_bronze_demo_listings |
| Performed source-to-demo row count validation | Team 15 | Done | SQL Result |
| Created lineage demonstration view | Team 15 | Done | workspace.default.propiq_week03_lineage_demo_view |
| Added notebook documentation and explanations | Team 15 | Done | GitHub Repository |

---

## 3. Key Decisions

- Used Spark SQL as the primary language for exploratory analysis.
- Created only one Bronze demonstration table as required for Week 3 instead of implementing the complete Bronze layer.
- Limited implementation strictly to Week-3 activities without introducing Silver, Gold, or production ingestion logic.
- Used temporary SQL views for exploration before Bronze demonstration.

---

## 4. Blockers / Risks

| Blocker | Impact | Help Needed |
|---|---|---|
| PageLoop notebook contained library-domain field names that had to be converted to PropIQ fields | Required additional notebook corrections | Verified mappings using Project Playbook and Data Dictionary |
| Dataset path mismatches during Databricks execution | Initial execution failures | Corrected Volume paths and source file formats |
| Schema differences between PageLoop and PropIQ | Multiple SQL query modifications | Validated all queries using the actual dataset schema |

---

## 5. Evidence Added to GitHub

- Updated `notebooks/01_data_exploration.ipynb`
- Added Week-3 exploration screenshots
- Added SQL exploration queries
- Added Bronze demonstration table implementation
- Added lineage demonstration view
- Updated project documentation

---

## 6. AI Transparency Note

| Question | Response |
|---|---|
| Where AI helped | Assisted in converting the PageLoop Week-3 notebook into the PropIQ project context, improving markdown explanations, and adapting SQL and PySpark examples to the project schema. |
| What we changed after AI suggestion | Updated dataset paths, replaced PageLoop-specific fields with PropIQ fields, corrected SQL queries, and aligned notebook documentation with the assigned project. |
| What we verified manually | Verified dataset schemas, file locations, query execution, temporary views, Bronze demonstration table, lineage view, and relationship checks in Databricks. |
| What we can explain without AI | Complete Week-3 exploration workflow, source ingestion process, Spark SQL exploration, data validation checks, Bronze demonstration implementation, and notebook execution. |

---

## 7. Next Week Preparation

- Begin Bronze layer implementation for all source datasets.
- Implement standardized ingestion into Delta tables.
- Introduce data quality and reconciliation framework.
- Prepare Silver layer planning and transformation strategy.
- Continue maintaining project documentation and GitHub evidence.