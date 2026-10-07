# Week 06 Log — Data Quality, Trusted Silver and Quarantine

**Week:** 6  
**Date range:** 24 August 2026 – 30 August 2026  
**Team:** Team 15  
**Project:** PropIQ – Real Estate Market Analytics

**Executed evidence:** notebook records execution on 2026-08-28

## Sprint goal

Validate the Silver Candidate datasets using the approved PropIQ Data Quality rules, reconcile Candidate-to-Trusted/Quarantine counts, preserve failure reasons and establish Trusted Silver outputs for downstream Gold modelling.

## Work completed

| Task | Ownership | Status | Evidence |
|---|---|---|---|
| Execute approved DQ rules | Thota Madhulika; P. Lakshmi Naga Sree; Vadlamuru Rishitha | Completed | `notebooks/04_data_quality_checks.ipynb` |
| Validate Candidate record counts | Thota Madhulika; P. Lakshmi Naga Sree; Vadlamuru Rishitha | Completed | DQ reconciliation checks |
| Route valid records to Trusted | Thota Madhulika; P. Lakshmi Naga Sree; Vadlamuru Rishitha | Completed | Trusted outputs |
| Route failed records to Quarantine | Thota Madhulika; P. Lakshmi Naga Sree; Vadlamuru Rishitha | Completed | Quarantine outputs |
| Preserve failure IDs/reasons | Thota Madhulika; P. Lakshmi Naga Sree; Vadlamuru Rishitha | Completed | DQ output logic |
| Validate Trusted/Quarantine overlap | Thota Madhulika; P. Lakshmi Naga Sree; Vadlamuru Rishitha | Completed | Reconciliation checks |
| Validate route membership | Thota Madhulika; P. Lakshmi Naga Sree; Vadlamuru Rishitha | Completed | Route-membership checks |
| Document DQ limitations | Thota Madhulika; P. Lakshmi Naga Sree; Vadlamuru Rishitha | Completed | `docs/data_quality_summary.md` |

## Candidate → Trusted + Quarantine reconciliation

The executed reconciliation produced the following results:

| Entity | Candidate | Trusted | Quarantine | Variance |
|---|---:|---:|---:|---:|
| Listings | 50,200 | 49,000 | 1,200 | 0 |
| Localities | 80 | 80 | 0 | 0 |
| Leads | 120,800 | 118,000 | 2,800 | 0 |
| Brokers | 320 | 320 | 0 | 0 |

The Candidate-to-Trusted/Quarantine variance was **0 for all four entities**.

Trusted/Quarantine overlap was also **0 for all four entities**, and route-membership checks returned **0**.

## Rule-failure scorecard

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

The total rule-failure count is 4,200. A physical record may contribute to more than one rule-failure count, so this total must not be interpreted as the number of unique quarantined records.

## DQ routing decisions

The DQ pipeline routes records using `record_uid` and preserves failure information rather than silently removing invalid records.

The routing approach is:

1. Evaluate the approved DQ rules.
2. Identify failed records and their rule/failure information.
3. Route passing records to Trusted.
4. Route failing records to Quarantine.
5. Reconcile Candidate = Trusted + Quarantine.
6. Validate that Trusted and Quarantine do not overlap.

Records are not manually inserted into Trusted after quarantine. Replay should occur upstream from the source through Silver Candidate when corrections are required.

## DQ-07 limitation

P15-DQ-07 is explicitly limited because the complete approved categorical-domain dictionary was not available.

The `propiq_governed_domains` dependency was unavailable in Databricks. Therefore, an invented allowed-value list was not used.

This limitation is documented rather than being hidden or replaced with an unsupported assumption.

## Blockers / Risks / Rework

The primary governance limitation was the unavailable approved domain table required for the complete P15-DQ-07 validation.

The implementation therefore records the limitation explicitly and avoids treating an inferred categorical list as an approved governance rule.

The DQ workflow also preserves the distinction between:

- Rule-failure counts.
- Unique quarantined physical records.
- Trusted records.
- Candidate reconciliation.

## GitHub Evidence

Primary implementation and documentation evidence:

- `notebooks/04_data_quality_checks.ipynb`
- `docs/data_quality_summary.md`
- `weekly_logs/week06_log.md`

The notebook contains the executed DQ validation and reconciliation logic. The data-quality summary documents the scorecard, physical reconciliation, severity classification and DQ-07 limitation.

## AI Transparency Note

AI assisted with rule-to-SQL mapping, validation-query organization and debugging support.

The actual `_record_hash` column, DQ outputs, reconciliation values and unavailable `propiq_governed_domains` dependency were manually verified against the project artifacts.

No unsupported governance values were invented to fill the DQ-07 gap.

## Next Week Preparation

The validated Trusted Silver datasets provide the controlled input boundary for Week 07 Gold modelling.

Gold dimensions, facts, summaries and KPI contracts should consume Trusted Silver only and preserve the approved grain and join-safety rules.
