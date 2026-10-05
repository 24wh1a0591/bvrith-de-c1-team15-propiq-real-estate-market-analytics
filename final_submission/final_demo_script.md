# Final Demo Script

**Target:** 10–15 minutes

## 1. Opening — 1 minute
Introduce Team 15 and PropIQ. State the fragmented-data problem and the trusted analytics outcome.

## 2. Architecture — 2 minutes
Show Raw → Bronze → Silver Candidate → DQ → Trusted/Quarantine → Gold → Power BI, with the controlled streaming path alongside it.

## 3. Week 03 — 1 minute
Show the four sources, physical `record_uid`, business keys, anti-joins and listing/lead fan-out check.

## 4. Silver and DQ — 2 minutes
Show Candidate transformations and DQ routing. Highlight 50,200 → 49,000 Trusted + 1,200 Quarantine for listings and zero reconciliation variance.

## 5. Gold — 2 minutes
Show seven dimensions, two facts and five summaries. Explain why listing and lead facts remain separate. Show broker-summary 49,000 vs fact 49,000 PASS and rerun changed-business-rows = 0.

## 6. Power BI — 2 minutes
Open the three pages and trace one KPI to its Gold source.

## 7. Streaming — 2 minutes
Show six event drops, explicit schema, two-day watermark, event-ID deduplication, sequence validation, quarantine and checkpointing. Show 19 → 12 Trusted + 7 Quarantine and the no-new-file rerun.

## 8. Closing — 1 minute
State limitations honestly: synthetic data, working 90-day stale threshold, incomplete governed-domain dictionary and simulated streaming.
