# Structured Streaming Design

**Week:** 10

## Event flow
JSON drops land in the controlled input path. Databricks Auto Loader detects new files, applies the explicit event schema, and writes raw-preserving records to `workspace.default.bronze_listing_status_stream`. `foreachBatch` classifies each physical record into Trusted streaming Silver or Quarantine.

## Objects
| Item | Value |
|---|---|
| Format | JSON |
| Bronze | `workspace.default.bronze_listing_status_stream` |
| Trusted | `workspace.default.silver_listing_status_stream_trusted` |
| Quarantine | `workspace.default.quarantine_listing_status_stream` |
| Trigger | `availableNow=True` |
| Watermark | 2 days from latest accepted event time |

## Controls
- Explicit schema with malformed/rescued-data capture.
- `listing_event_id` deduplication.
- 2-day event-time watermark.
- Per-listing sequence validation.
- Orphan listing/locality/broker checks.
- Invalid price/area and future-event checks.
- Multi-reason quarantine.
- Delta transaction idempotency using `txnAppId` and batch version.
- Bronze physical-row reconciliation against Trusted + Quarantine.
- No-new-file rerun proof.

## Captured six-drop evidence
| Drop | Scenario | Physical | Trusted | Quarantine |
|---|---|---:|---:|---:|
| 01 | normal | 4 | 4 | 0 |
| 02 | duplicate | 3 | 2 | 1 |
| 03 | late/out-of-order | 3 | 1 | 2 |
| 04 | malformed/reference | 3 | 1 | 2 |
| 05 | invalid/future | 3 | 1 | 2 |
| 06 | schema drift | 3 | 3 | 0 |
| **Total** | | **19** | **12** | **7** |

Final controls reported zero unaccounted rows, duplicate trusted event IDs, orphan listings in Trusted, late trusted events, sequence violations, invalid price/area in Trusted and future events in Trusted.

No-new-file rerun remained 19 Bronze / 12 Trusted / 7 Quarantine with 12 distinct trusted event IDs.

## Near-real-time metric
Accepted event count by event type/status from Trusted streaming Silver.

## Limitation
This is an educational file-based streaming simulation; Kafka is production architecture awareness only.
