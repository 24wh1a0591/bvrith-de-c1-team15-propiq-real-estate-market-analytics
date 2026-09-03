# Week 06 Log — Data Quality, Trusted Silver & Quarantine

**Week:** 6  
**Date range:** [Add dates]  
**Team:** Team 15  
**Project:** PropIQ – Real Estate Market Analytics  

---

## 1. Sprint Goal

Implement the PropIQ Data Quality layer by validating the four Week-05 Silver Candidate datasets against the approved P15-DQ-01 through P15-DQ-08 rules.

Route valid records to Trusted Silver and failed records to Quarantine while preserving `record_uid`, applicable DQ failure IDs, severity, failure reasons, and reconciliation evidence.

---

## 2. Work Completed

| Task | Owner | Status | Evidence |
|------|-------|--------|----------|
| Reviewed and mapped P15-DQ-01 to P15-DQ-08 rules to the Silver Candidate datasets | Team 15 | Done | Team 15 DQ Rules PDF / Notebook |
| Implemented DQ checks for listings including key, reference, range, price-per-sqft, completion-date and domain validations | Team 15 | Done | Week 06 DQ Notebook |
| Implemented DQ checks for localities | Team 15 | Done | Week 06 DQ Notebook |
| Implemented DQ checks for leads including listing reference and timestamp validation | Team 15 | Done | Week 06 DQ Notebook |
| Implemented DQ checks for brokers and categorical-domain validation | Team 15 | Done | Week 06 DQ Notebook |
| Implemented physical-record routing using `record_uid` | Team 15 | Done | Week 06 DQ Notebook |
| Added Trusted Silver and Quarantine outputs for all four entities | Team 15 | Done | Databricks Tables / Notebook |
| Preserved multiple applicable DQ failures for the same physical record | Team 15 | Done | Quarantine Output |
| Added Candidate → Trusted + Quarantine reconciliation checks | Team 15 | Done | Validation Cells |
| Added Trusted/Quarantine overlap validation | Team 15 | Done | Validation Cells |
| Corrected `_bronze_record_hash` reference to the actual `_record_hash` column | Team 15 | Done | Databricks Execution / Corrected Notebook |
| Removed the unavailable `propiq_governed_domains` dependency from the DQ-07 implementation | Team 15 | Done | Corrected Notebook |

---

## 3. Key Decisions

- Used `record_uid` as the physical routing and reconciliation key instead of business keys such as `listing_id`, `lead_id`, `locality_id`, or `broker_id`.
- A record can fail multiple DQ rules, so all applicable failure IDs, severity levels, and failure reasons are retained instead of stopping at the first failure.
- Records that pass the applicable DQ checks are routed to Trusted Silver, while failed records are routed to the corresponding Quarantine table.
- Candidate records must reconcile exactly to Trusted plus Quarantine records so that no failed physical record disappears.
- Used the actual Candidate schema column `_record_hash` instead of the incorrect `_bronze_record_hash` reference.
- Removed the `propiq_governed_domains` dependency because the table was not available in the Databricks environment. The supplied Team 15 DQ specification identifies `unknown-new-code` as an example of an unapproved categorical value but does not provide a complete domain dictionary.

---

## 4. Blockers / Risks

| Blocker | Impact | Help Needed |
|---------|--------|-------------|
| `_bronze_record_hash` column was not present in the Silver Candidate table | Initial notebook execution failed | Corrected to the actual `_record_hash` column |
| `propiq_governed_domains` table was not available in the Databricks workspace | Original DQ-07 governance check failed | Removed the unavailable dependency and retained the DQ-07 implementation supported by the approved DQ specification |
| Complete approved categorical domain values were not provided in the supplied DQ document | Full domain-dictionary validation cannot be implemented without unsupported assumptions | Separate approved domain dictionary is required if complete domain-value enforcement is needed |

---

## 5. Evidence Added to GitHub

- Updated Week 06 Data Quality notebook
- Added DQ validation and routing queries
- Added Trusted Silver and Quarantine validation outputs
- Added Candidate-to-Trusted/Quarantine reconciliation checks
- Added Databricks execution/error screenshots
- Updated `weekly_logs/week06_log.md`
- Documented corrections made during notebook validation

---

## 6. AI Transparency Note

| Question | Response |
|----------|----------|
| Where AI helped | Helped structure the Week 06 DQ notebook, map the approved PropIQ DQ rules to SQL validation logic, and identify issues during notebook debugging. |
| What we changed after AI suggestion | Corrected the invalid `_bronze_record_hash` reference to `_record_hash` after checking the actual Databricks schema. Removed the unavailable `propiq_governed_domains` dependency after Databricks reported that the table could not be found. |
| What we verified manually | Verified the actual column name from the Databricks error output, checked the available schema/search path, and validated that the corrected notebook no longer referenced the unavailable governance table. |
| What we can explain without AI | The purpose of P15-DQ-01 through P15-DQ-08, physical `record_uid` routing, Trusted versus Quarantine logic, multi-rule failure retention, and Candidate-to-Trusted/Quarantine reconciliation. |

---

## 7. Next Week Preparation

- Complete and verify the final Trusted Silver and Quarantine outputs for all four PropIQ entities.
- Validate Candidate = Trusted + Quarantine reconciliation for every required source and batch.
- Confirm there is no overlap between Trusted and Quarantine `record_uid` values.
- Review any remaining DQ-07 domain requirements with the team.
- Prepare the validated Trusted Silver datasets for the next stage of the PropIQ pipeline.
