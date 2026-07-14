# Problem Charter

**Week:** 1  
**Owner(s):** [Ms.Thota Madhulika], [Ms.P.Lakshmi Naga Sree], [Ms. Vadlamuru Rishitha]   
**Project:** [PropIQ Real Estate Market Analytics]

---
# Problem Charter

## 1. Problem Context

### Domain

PropIQ is a Real Estate Market Analytics project that focuses on transforming synthetic property market data into reliable business insights. The project simulates how a real estate company collects, processes, and analyzes property-related information to support business decisions.

### What real-world process does this project represent?

The project represents the data engineering workflow of a real estate marketplace where property listings, broker information, locality details, buyer leads, and listing status updates are collected from multiple systems and converted into trusted analytics.

### What kinds of data are generated?

The project uses multiple synthetic datasets including:

- Property Listings
- Locality Information
- Broker Details
- Buyer Leads
- Listing Status Events (Streaming)
- Property Price Updates
- Sales Status Information

### Why is raw data not enough?

Raw data often contains missing values, duplicate records, invalid references, unrealistic prices, inconsistent formats, and incomplete information. Such data cannot be used directly for business reporting or decision-making. It must first be cleaned, validated, standardized, and transformed into trusted datasets.

### Who would use the final dashboard or metrics?

The final dashboards and reports will be useful for:

- Sales & Revenue Managers
- Broker Operations Team
- Market Analysts
- Live Sales Desk
- Business Decision Makers

---

## 2. Engineering Problem

The project must convert multiple raw property-market source files into trusted Bronze, Silver, Data Quality, Gold, and dashboard-ready datasets using Databricks, Spark SQL, Structured Streaming, and Power BI.

The pipeline should integrate multiple datasets, detect data quality issues, validate records, generate business metrics, and provide reliable dashboards for decision-making.

---

## 3. Users / Stakeholders

| User / Stakeholder | What they need from the data |
|--------------------|------------------------------|
| Sales & Revenue Manager | Identify high-demand localities, price trends, and successful property sales. |
| Broker Operations Lead | Monitor broker performance, listing activity, follow-ups, and stale inventory. |
| Market Analyst | Analyze property prices, market trends, demand patterns, and locality performance. |
| Live Sales Desk | Monitor live property events such as new listings, price changes, and sold properties without duplicate records. |

---

## 4. Scope Inclusions

The team will build:

- Synthetic property market datasets
- Source data generator
- Bronze data ingestion layer
- Silver data standardization layer
- Data Quality validation framework
- Gold analytical tables
- Power BI dashboards
- Streaming simulation using JSON events
- Documentation
- GitHub repository with weekly evidence
- End-to-end Lakehouse pipeline using Databricks

---

## 5. Scope Exclusions

The project will **not** include:

- Production-ready real estate application
- Property buying or selling portal
- Broker management system
- Real customer or personal data
- Web scraping from real property websites
- Payment gateway integration
- Mobile application development
- Direct reporting from raw datasets
- Fake screenshots or fabricated project evidence
- Unverified AI-generated code or documentation

---

## 6. Success Criteria

By the end of the 12-week internship, the project will be considered successful if:

- Synthetic datasets are generated successfully.
- Bronze layer stores all raw data with metadata.
- Silver layer contains cleaned and standardized data.
- All planned Data Quality rules are implemented and validated.
- Gold tables generate accurate business metrics.
- Power BI dashboard displays insights using only Gold datasets.
- Streaming simulation processes listing events successfully.
- GitHub repository contains organized code, documentation, notebooks, screenshots, and weekly logs.
- Every team member can explain the complete data pipeline and project workflow.
- The final project demonstrates a complete end-to-end Lakehouse Data Engineering solution.

- The pipeline can be explained end to end.
- The team can show Bronze, Silver, DQ, Gold, dashboard, and streaming evidence.
- All three students can explain the full project at a high level.
- GitHub contains weekly evidence and final submission files.
