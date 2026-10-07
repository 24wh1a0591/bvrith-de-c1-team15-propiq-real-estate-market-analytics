# Structured Streaming Design — PropIQ Week 10

**Week:** 10  
**Project:** P15 PropIQ — Real Estate Market Analytics  
**Purpose:** Document the controlled six-drop streaming simulation, validation controls, recovery behavior and evidence boundary.

## 1. Objective

Process six controlled JSON Lines drops incrementally without reprocessing old files. The implementation preserves physical arrivals in Streaming Bronze, applies an explicit event schema, uses a two-day event-time watermark, deduplicates `listing_event_id`, validates per-listing sequence, quarantines malformed/late/orphan/invalid records, rescues schema drift and proves a no-new-file rerun.

This is a student streaming simulation, not a production Kafka deployment.

## 2. Source and event contract

**Source:** `data_sample/streaming/`.  
**Runtime landing path:** `/Volumes/workspace/default/propqi_streaming/landing/`.

Six files are processed one at a time:

| Drop | Scenario | Purpose |
|---|---|---|
| 01 | normal | baseline |
| 02 | duplicate | repeated `listing_event_id` |
| 03 | late/out-of-order | watermark and sequence controls |
| 04 | malformed/reference | malformed input and orphan listing |
| 05 | invalid/future | invalid price and future event handling |
| 06 | schema drift | rescued unknown field and schema version change |

Core fields are `listing_event_id`, `listing_id`, `event_type`, `event_timestamp`, `event_sequence`, `listing_status`, `asking_price`, `locality_id`, `broker_id`, `property_type`, `bedrooms`, `area_sqft`, `source_system`, `schema_version` and `ingestion_timestamp`.

## 3. Processing architecture

```
data_sample/streaming/*.json
          |
          v
/Volumes/.../propqi_streaming/landing/
          |
          v
Auto Loader
(explicit schema + rescued/malformed data)
          |
          v
workspace.default.bronze_listing_status_stream
          |
          +---- SQL validation / foreachBatch ----+
          |                                       |
          v                                       v
workspace.default.silver_listing_status_stream_trusted
workspace.default.quarantine_listing_status_stream
```

Bronze is raw-preserving. Business acceptance and quarantine happen after physical arrival has been retained.

## 4. Locked controls

| Control | Implementation |
|---|---|
| Incremental discovery | Auto Loader reads newly arrived files |
| Checkpoint | `/Volumes/workspace/default/propqi_streaming/checkpoints/listing_status_event` |
| Watermark | 2 days on `event_timestamp` |
| Deduplication | `listing_event_id` |
| Sequence | `event_sequence` within `listing_id` |
| Malformed input | `_corrupt_record` / rescued-data fields retained |
| Late event | explicit `late_event_quarantine` reason |
| Schema drift | `_rescued_data` retained; unknown fields not automatically promoted |
| Reference checks | Trusted Silver listing/locality/broker masters |
| Failure retention | all applicable rule IDs/reasons retained |
| Idempotence | checkpoint plus Delta transaction semantics |
| Reconciliation | Bronze physical = Trusted + Quarantine |

## 5. Captured six-drop result

| Drop | Physical | Trusted | Quarantine |
|---|---:|---:|---:|
| 01 | 4 | 4 | 0 |
| 02 | 3 | 2 | 1 |
| 03 | 3 | 1 | 2 |
| 04 | 3 | 1 | 2 |
| 05 | 3 | 1 | 2 |
| 06 | 3 | 3 | 0 |
| **Total** | **19** | **12** | **7** |

Final validation reported 0 unaccounted physical records, 0 duplicate trusted event IDs, 0 orphan listings in Trusted, 0 late events in Trusted, 0 sequence violations, 0 invalid price/area rows in Trusted and 0 future-dated events in Trusted.

The no-new-file rerun kept Bronze at 19, Trusted at 12, Quarantine at 7 and distinct trusted event IDs at 12.

## 6. Supplemental live-event demonstration

The notebook also contains a small PropIQ live-event demonstration using `workspace.default.stream_propiq_live_events` and `workspace.default.stream_propiq_live_bronze`. The executed run generated 20 initial source events and 10 additional events during the stop/restart demonstration, reaching 30 source rows and 30 distinct event IDs.

This section is supplemental learning evidence. It does not replace the six-drop acceptance gate or claim a production continuous streaming deployment.

## 7. Recovery / reset

Stop the stream, remove only controlled demo state, reset landing to the intended starting state, then rerun Drop 01 through Drop 06 and the reconciliation/no-new-file checks. Record any mismatch in the Week Log. Never manufacture a PASS result after a reset.

## 8. Evidence boundary

Required artifacts:
- `notebooks/07_streaming_simulation.ipynb`
- `data_sample/streaming/`
- `streaming/kafka_event_schema.json`
- `streaming/structured_streaming_design.md`
- `weekly_logs/week10_log.md`
- `screenshots/week10_*`

The repository currently contains four Week-10 screenshots covering the Auto Loader evidence. The supplemental live-event evidence is retained in the executed notebook; missing screenshots are not fabricated.

## 9. Boundary

No Kafka broker installation, topic/partition setup, consumer-group administration, production tuning, Gold redesign or Power BI changes are part of Week 10.
