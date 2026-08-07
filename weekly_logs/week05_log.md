# Week 05 Log — Silver Candidate Transformation

**Week:** 5  
**Date range:** [Add dates]  
**Team:** Team 15  
**Project:** PropIQ – Real Estate Market Analytics  

---

## 1. Sprint Goal

Convert Bronze datasets into structured Silver Candidate tables by applying schema standardization, data type casting, and domain-specific transformations. Ensure all datasets are aligned with the PropIQ data dictionary and ready for Data Quality validation in the next phase.

---

## 2. Work Completed

| Task | Owner | Status | Evidence |
|------|------|--------|----------|
| Loaded Bronze datasets (listings, leads, brokers, localities) | Thota Madhulika | Done | Notebook cells |
| Standardized column names and schema for listings & localities | Thota Madhulika | Done | Notebook |
| Transformed leads dataset (timestamp casting, renaming) | P. Lakshmi Naga Sree | Done | Notebook |
| Transformed brokers dataset (schema alignment, type fixes) | P. Lakshmi Naga Sree | Done | Notebook |
| Applied data type casting across all datasets | Vadlamuru Rishitha | Done | Notebook |
| Validated schema consistency and column formats | Vadlamuru Rishitha | Done | Output display |
| Created Silver Candidate tables (`silver_candidate_*`) | All Members | Done | Databricks tables |

---

## 3. Key Decisions

- No joins were performed in the Silver layer to preserve dataset grain and avoid duplication issues.
- Standardized timestamp formats across all datasets to ensure consistency for downstream processing.
- Retained unique identifiers (listing_id, lead_id, broker_id) for traceability and future joins in Gold layer.

---

## 4. Blockers / Risks

| Blocker | Impact | Help Needed |
|--------|--------|-------------|
| Inconsistent column naming in Bronze layer | Slowed transformation logic | Required manual mapping to data dictionary |
| Null values in key attributes | Risk for DQ failures | Will handle in Week 06 validation rules |
| Ambiguity in some field mappings | Possible schema mismatch | Cross-verification with playbook |

---

## 5. Evidence Added to GitHub

- Updated Week 05 Silver Candidate transformation notebook  
- Added schema output screenshots  
- Uploaded sample outputs for all 4 datasets  
- Documented transformation steps in notebook  

---

## 6. AI Transparency Note

| Question | Response |
|---------|----------|
| Where AI helped | Helped convert PageLoop notebook into PropIQ format and guided schema alignment |
| What we changed after AI suggestion | Removed incorrect joins, fixed column names, added proper data type casting |
| What we verified manually | Schema structure, column mappings, data types, and final outputs |
| What we can explain without AI | Entire Silver transformation process and reasoning behind design decisions |

---

## 7. Next Week Preparation

- Implement Data Quality (DQ) rules on Silver Candidate datasets  
- Split data into Trusted and Quarantine layers based on validation results  

---
