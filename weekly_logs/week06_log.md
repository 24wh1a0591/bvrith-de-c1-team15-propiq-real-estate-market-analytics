# Week 06 Log — Data Quality, Trusted Silver and Quarantine

**Week:** 6  
**Executed evidence:** notebook records execution on 2026-08-28  
**Team:** Team 15

## Results
Candidate → Trusted + Quarantine variance was 0:
- Listings: 50,200 → 49,000 Trusted + 1,200 Quarantine.
- Localities: 80 → 80 + 0.
- Leads: 120,800 → 118,000 + 2,800.
- Brokers: 320 → 320 + 0.

Trusted/Quarantine overlap was 0 and route-membership checks returned 0.

## Rule failures
P15-DQ-01 500; DQ-02 200; DQ-03 200; DQ-04 350; DQ-05 150; DQ-06 1,200; DQ-07 0; DQ-08 1,600. Total rule failures: 4,200.

## Decisions
Route by `record_uid`; preserve all failure IDs/reasons; do not invent duplicate winners. DQ-07 is explicitly limited because the approved domain table was unavailable.

## AI transparency
AI assisted with rule-to-SQL mapping and debugging. The actual `_record_hash` column and unavailable governance-table dependency were manually verified.
