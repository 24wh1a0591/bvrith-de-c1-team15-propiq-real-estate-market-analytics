# Week 03 Log — Data Exploration, Relationships and Join Safety

**Week:** 3  
**Date range:** 25 July 2026 – 30 July 2026  
**Team:** Team 15  
**Project:** PropIQ – Real Estate Market Analytics

## 1. Sprint Goal

Profile the four PropIQ source datasets, establish physical grain and business keys, validate source relationships, identify join and fan-out risks, and create only the approved Week-03 Bronze demonstration.

## 2. Work Completed

| Task | Ownership | Status | Evidence |
|---|---|---|---|
| Profile Listings, Leads, Localities and Brokers schemas | Thota Madhulika; P. Lakshmi Naga Sree; Vadlamuru Rishitha | Done | `screenshots/week03_exploration_profiling_validation_01.png` |
| Identify physical reconciliation keys and business keys | Thota Madhulika; P. Lakshmi Naga Sree; Vadlamuru Rishitha | Done | `screenshots/week03_exploration_profiling_validation_01.png` |
| Validate Listings → Localities relationship | Thota Madhulika; P. Lakshmi Naga Sree; Vadlamuru Rishitha | Done | `screenshots/week03_exploration_relationship_validation_02.png` |
| Validate Listings → Brokers relationship | Thota Madhulika; P. Lakshmi Naga Sree; Vadlamuru Rishitha | Done | `screenshots/week03_exploration_relationship_validation_02.png` |
| Validate Leads → Listings relationship | Thota Madhulika; P. Lakshmi Naga Sree; Vadlamuru Rishitha | Done | `screenshots/week03_exploration_relationship_validation_02.png` |
| Check listing/lead fan-out risk | Thota Madhulika; P. Lakshmi Naga Sree; Vadlamuru Rishitha | Done | `screenshots/week03_exploration_join_safety_validation_03.png` |
| Profile categorical domains | Thota Madhulika; P. Lakshmi Naga Sree; Vadlamuru Rishitha | Done | `screenshots/week03_exploration_profiling_validation_01.png` |
| Create small Bronze demonstration | Thota Madhulika; P. Lakshmi Naga Sree; Vadlamuru Rishitha | Done | `notebooks/01_data_exploration.ipynb` |
| Create lineage demonstration view | Thota Madhulika; P. Lakshmi Naga Sree; Vadlamuru Rishitha | Done | `notebooks/01_data_exploration.ipynb` |

## 3. Key Decisions

1. `record_uid` is retained as the physical reconciliation key.
2. Business keys are used for relationship validation and downstream modelling.
3. One-to-many lead relationships must not change the intended listing grain.
4. Categorical domains are profiled from available source data without inventing an approved governance dictionary.
5. Week 03 is limited to source profiling, relationship validation, join-safety checks and the approved Bronze demonstration.
6. Full Bronze ingestion remains within Week 04 scope.

## 4. Blockers / Risks

The original exploration notebook contained PageLoop/loan-related remnants that were not applicable to PropIQ.

The notebook was reworked to use PropIQ-specific exploration and validation logic.

The reworked scope covers:

- Source profiling.
- Physical and business-key validation.
- Relationship integrity.
- Anti-join checks.
- Listing/lead fan-out safety.
- Limited Bronze demonstration.

No full Bronze, Silver, Gold, Power BI or streaming implementation was included in Week 03.

## 5. Evidence Added to GitHub

### Implementation

- `notebooks/01_data_exploration.ipynb`
- `weekly_logs/week03_log.md`

### Exploration and validation evidence

- `screenshots/week03_exploration_profiling_validation_01.png`
- `screenshots/week03_exploration_relationship_validation_02.png`
- `screenshots/week03_exploration_join_safety_validation_03.png`

### Repository evidence

- `screenshots/week03_evidence_commit_history.png`
- `screenshots/week03_evidence_overall_commit_history.png`

### Evidence mapping

| Validation area | Repository evidence |
|---|---|
| Source profiling | `screenshots/week03_exploration_profiling_validation_01.png` |
| Physical/business-key validation | `screenshots/week03_exploration_profiling_validation_01.png` |
| Listings → Localities | `screenshots/week03_exploration_relationship_validation_02.png` |
| Listings → Brokers | `screenshots/week03_exploration_relationship_validation_02.png` |
| Leads → Listings | `screenshots/week03_exploration_relationship_validation_02.png` |
| Listing/lead fan-out | `screenshots/week03_exploration_join_safety_validation_03.png` |
| Bronze demonstration / implementation | `notebooks/01_data_exploration.ipynb` |
| Commit evidence | `screenshots/week03_evidence_commit_history.png` and `screenshots/week03_evidence_overall_commit_history.png` |

## 6. AI Transparency Note

AI assisted with restructuring and reviewing the Week-03 exploration workflow and documentation.

The team verified the dataset paths, source fields, physical/business keys, relationship checks, grain decisions and Week-03 scope against the project artifacts.

AI assistance did not replace the validation evidence contained in the exploration notebook and repository screenshots.

## 7. Next Week Preparation

The validated source structure and relationship findings provide the basis for Week-04 Bronze ingestion.

Week 04 should build the complete Bronze layer from the validated source inputs while preserving physical lineage and source-level records.
