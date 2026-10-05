# Week 10 Log — Controlled Structured Streaming Simulation

**Week:** 10  
**Team:** Team 15  
**Project:** PropIQ – Real Estate Market Analytics

## Goal
Demonstrate controlled file-based Structured Streaming with explicit schema, checkpointing, watermarking, deduplication, sequence validation, quarantine and reconciliation.

## Captured results
| Drop | Scenario | Physical | Trusted | Quarantine |
|---|---|---:|---:|---:|
| 01 | normal | 4 | 4 | 0 |
| 02 | duplicate | 3 | 2 | 1 |
| 03 | late/out-of-order | 3 | 1 | 2 |
| 04 | malformed/reference | 3 | 1 | 2 |
| 05 | invalid/future | 3 | 1 | 2 |
| 06 | schema drift | 3 | 3 | 0 |
| **Total** | | **19** | **12** | **7** |

Final controls: unaccounted 0; duplicate trusted event IDs 0; orphan listings in Trusted 0; late events in Trusted 0; sequence violations 0; invalid price/area in Trusted 0; future events in Trusted 0.

No-new-file rerun: Bronze 19→19, Trusted 12→12, Quarantine 7→7, distinct trusted event IDs 12→12.

## Decisions
Auto Loader + explicit schema; two-day watermark; `listing_event_id` deduplication; `foreachBatch` routing; quarantine-before-Trusted write order; Delta transaction idempotency.

## AI transparency
AI assisted with control-flow review and documentation. Drop outcomes, reconciliation and rerun behavior were checked from notebook execution evidence.
