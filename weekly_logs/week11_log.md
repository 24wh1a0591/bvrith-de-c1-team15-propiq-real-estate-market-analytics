# Week 11 Log — Integration, Traceability and Rebuild Runbook

**Week:** 11  
**Team:** Team 15  
**Project:** PropIQ – Real Estate Market Analytics

## Goal
Integrate batch and streaming evidence into a defensible end-to-end runbook and trace dashboard outputs to Gold and Trusted inputs.

## Work completed
- Documented exact notebook execution order.
- Documented Gold-only Power BI consumption.
- Documented source-to-dashboard traceability.
- Documented upstream correction/rebuild rules.
- Integrated Week-10 streaming reconciliation and rerun evidence.
- Reviewed repository navigation and final evidence locations.

## Rebuild rule
Never patch Gold to repair an upstream error. Re-run from the earliest affected layer, then rerun DQ, Gold validation and the Power BI handoff.

## AI transparency
AI assisted with runbook structure and traceability wording. Actual notebook/table names and execution evidence were used for the final version.
