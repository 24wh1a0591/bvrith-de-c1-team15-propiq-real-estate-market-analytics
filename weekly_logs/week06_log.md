# Week 06 Log — Data Quality, Trusted Silver and Quarantine

**Week:** 6  
**Date range:** 24 August 2026 – 30 August 2026  
**Team:** Team 15  
**Project:** PropIQ – Real Estate Market Analytics

**Executed evidence:** notebook records execution on 2026-08-28

## 1. Sprint Goal

Validate the Silver Candidate datasets using the approved PropIQ Data Quality rules, reconcile Candidate-to-Trusted/Quarantine counts, preserve failure information, and establish Trusted Silver outputs for downstream Gold modelling.

## 2. Work Completed

| Task | Ownership | Status | Evidence |
|---|---|---|---|
| Execute approved DQ rules | Thota Madhulika; P. Lakshmi Naga Sree; Vadlamuru Rishitha | Done | `notebooks/04_data_quality_checks.ipynb` |
| Validate Candidate record counts | Thota Madhulika; P. Lakshmi Naga Sree; Vadlamuru Rishitha | Done | `screenshots/week06_dq_initial_record_count_check.jpeg` |
| Validate DQ rule results | Thota Madhulika; P. Lakshmi Naga Sree; Vadlamuru Rishitha | Done | `screenshots/week06_dq_listing_rule_check.jpeg`, `screenshots/week06_dq_lead_rule_check.jpeg`, `screenshots/week06_dq_locality_rule_check.jpeg`, `screenshots/week06_dq_broker_rule_check.jpeg` |
| Route valid records to Trusted | Thota Madhulika; P. Lakshmi Naga Sree; Vadlamuru Rishitha | Done | `screenshots/week06_dq_trusted_quarantine_output_check.jpeg` |
| Route failed records to Quarantine | Thota Madhulika; P. Lakshmi Naga Sree; Vadlamuru Rishitha | Done | `screenshots/week06_dq_trusted_quarantine_output_check.jpeg` |
| Validate failed-record / multi-rule quarantine results | Thota Madhulika; P. Lakshmi Naga Sree; Vadlamuru Rishitha | Done | `screenshots/week06_dq_failed_record_count_check.jpeg`, `screenshots/week06_dq_multi_rule_quarantine_check.jpeg` |
| Validate Trusted/Quarantine reconciliation | Thota Madhulika; P. Lakshmi Naga Sree; Vadlamuru Rishitha | Done | `screenshots/week06_dq_reconciliation_check.jpeg` |
| Validate route separation / membership | Thota Madhulika; P. Lakshmi Naga Sree; Vadlamuru Rishitha | Done | `screenshots/week06_dq_reconciliation_check.jpeg` |
| Document DQ limitation | Thota Madhulika; P. Lakshmi Naga Sree; Vadlamuru Rishitha | Done | `docs/data_quality_summary.md` |

## 3. Key Decisions

1. DQ routing uses `record_uid` for physical reconciliation.
2. Passing records are routed to Trusted and failed records to Quarantine.
3. Candidate records must reconcile to Trusted + Quarantine.
4. Trusted and Quarantine must not overlap.
5. Rule-failure counts are not treated as unique quarantined-record counts because one physical record may fail multiple rules.
6. Failure information is preserved rather than silently dropping invalid records.
7. P15-DQ-07 is limited because the approved categorical-domain dictionary was unavailable.
8. No invented allowed-value list is used to compensate for the unavailable governance dependency.
9. Replay of corrected records should occur upstream through the source and Silver Candidate flow rather than manually inserting records into Trusted.

## 4. Blockers / Risks

The primary governance limitation was the unavailable approved categorical-domain dependency required for complete P15-DQ-07 validation.

The `propiq_governed_domains` dependency was unavailable in Databricks.

Therefore, an inferred categorical list was not treated as an approved governance dictionary.

The limitation is explicitly documented in:

`docs/data_quality_summary.md`

The DQ implementation also distinguishes between:

- Rule-failure counts.
- Unique quarantined physical records.
- Trusted records.
- Candidate reconciliation.
- Trusted/Quarantine overlap.

## 5. Evidence Added to GitHub

### Implementation

- `notebooks/04_data_quality_checks.ipynb`
- `docs/data_quality_summary.md`
- `weekly_logs/week06_log.md`

### DQ evidence screenshots

- `screenshots/week06_dq_initial_record_count_check.jpeg`
- `screenshots/week06_dq_listing_rule_check.jpeg`
- `screenshots/week06_dq_lead_rule_check.jpeg`
- `screenshots/week06_dq_locality_rule_check.jpeg`
- `screenshots/week06_dq_broker_rule_check.jpeg`
- `screenshots/week06_dq_failed_record_count_check.jpeg`
- `screenshots/week06_dq_multi_rule_quarantine_check.jpeg`
- `screenshots/week06_dq_trusted_quarantine_output_check.jpeg`
- `screenshots/week06_dq_reconciliation_check.jpeg`

### Evidence mapping

| Validation area | Repository evidence |
|---|---|
| Initial Candidate counts | `screenshots/week06_dq_initial_record_count_check.jpeg` |
| Listings DQ rules | `screenshots/week06_dq_listing_rule_check.jpeg` |
| Leads DQ rules | `screenshots/week06_dq_lead_rule_check.jpeg` |
| Localities DQ rules | `screenshots/week06_dq_locality_rule_check.jpeg` |
| Brokers DQ rules | `screenshots/week06_dq_broker_rule_check.jpeg` |
| Failed-record count | `screenshots/week06_dq_failed_record_count_check.jpeg` |
| Multi-rule quarantine validation | `screenshots/week06_dq_multi_rule_quarantine_check.jpeg` |
| Trusted/Quarantine outputs | `screenshots/week06_dq_trusted_quarantine_output_check.jpeg` |
| Candidate → Trusted + Quarantine reconciliation | `screenshots/week06_dq_reconciliation_check.jpeg` |
| DQ rule scorecard and limitation | `docs/data_quality_summary.md` |

## DQ Reconciliation

The executed reconciliation produced:

| Entity | Candidate | Trusted | Quarantine | Variance |
|---|---:|---:|---:|---:|
| Listings | 50,200 | 49,000 | 1,200 | 0 |
| Localities | 80 | 80 | 0 | 0 |
| Leads | 120,800 | 118,000 | 2,800 | 0 |
| Brokers | 320 | 320 | 0 | 0 |

Candidate-to-Trusted/Quarantine variance was **0 for all four entities**.

Trusted/Quarantine overlap was **0**, and route-membership checks returned **0**.

## DQ Rule-Failure Results

| Rule | Failed rows |
|---|---:|
| P15-DQ-01 | 500 |
| P15-DQ-02 | 200 |
| P15-DQ-03 | 200 |
| P15-DQ-04 | 350 |
| P15-DQ-05 | 150 |
| P15-DQ-06 | 1,200 |
| P15-DQ-07 | 0 |
| P15-DQ-08 | 1,600 |
| **Total** | **4,200** |

A physical record may contribute to multiple rule-failure counts. Therefore, 4,200 is the total rule-failure count and not the number of unique quarantined records.

## 6. AI Transparency Note

AI assisted with rule-to-SQL mapping, validation-query organization and debugging support.

The team manually verified:

- The actual DQ outputs.
- Candidate-to-Trusted/Quarantine reconciliation.
- `_record_hash` usage.
- Rule-failure counts.
- Trusted/Quarantine routing.
- The unavailable `propiq_governed_domains` dependency.

No unsupported governance values were invented to fill the DQ-07 limitation.

## 7. Next Week Preparation

The validated Trusted Silver datasets provide the controlled input boundary for Week 07 Gold modelling.

Gold dimensions, facts, summaries and KPI contracts should consume Trusted Silver only and preserve the approved grain, reconciliation and join-safety rules.
