# Week 10 Log — Controlled Streaming Simulation

**Week:** 10  
**Execution date:** 2026-10-05  
**Team:** Team 15  
**Project:** P15 PropIQ — Real Estate Market Analytics

## 1. Sprint Goal

Process all six PropIQ listing-status JSON drops incrementally and prove explicit schema handling, checkpointing, two-day watermarking, event-ID deduplication, sequence validation, quarantine, schema-drift rescue and no-new-file idempotence.

## 2. Work Completed

| Task | Owner | Status | Evidence |
|---|---|---|---|
| Source grain, parent Trusted tables and runtime setup | Thota Madhulika | Complete | `notebooks/07_streaming_simulation.ipynb` |
| Six-drop Auto Loader execution | P. Lakshmi Naga Sree | Complete | `data_sample/streaming/` + notebook |
| Trusted/Quarantine validation and reconciliation | Vadlamuru Rishitha | Complete | notebook validation sections |
| Event contract and design documentation | Team 15 | Complete | `streaming/kafka_event_schema.json`, `streaming/structured_streaming_design.md` |
| Evidence/repository review | Team 15 | Complete | `screenshots/week10_*`, this log |

These are primary responsibilities for this week; the implementation and review were collaborative.

## 3. Validation Results

| Drop | Scenario | Physical | Trusted | Quarantine |
|---|---|---:|---:|---:|
| 01 | normal | 4 | 4 | 0 |
| 02 | duplicate event ID | 3 | 2 | 1 |
| 03 | late/out-of-order | 3 | 1 | 2 |
| 04 | malformed/reference | 3 | 1 | 2 |
| 05 | invalid/future | 3 | 1 | 2 |
| 06 | schema drift | 3 | 3 | 0 |
| **Total** | | **19** | **12** | **7** |

Final checks: unaccounted physical records **0**; duplicate trusted event IDs **0**; orphan listings in Trusted **0**; late events in Trusted **0**; sequence violations **0**; invalid price/area in Trusted **0**; future events in Trusted **0**.

### No-new-file rerun

**Bronze 19 → 19 | Trusted 12 → 12 | Quarantine 7 → 7 | distinct Trusted event IDs 12 → 12.**

### Supplemental live-event run

The notebook generated 20 initial live source events and 10 additional events during stop/restart, reaching 30 source rows and 30 distinct event IDs. This is supplemental evidence, not the six-drop acceptance gate.

## 4. Key Decisions

- Bronze preserves physical arrivals.
- Watermark is two days on `event_timestamp`.
- Deduplication uses `listing_event_id`.
- Sequence validation uses `event_sequence` within `listing_id`.
- All applicable failure reasons are retained.
- Reference checks use Trusted Silver masters.
- Schema drift is rescued and flagged; unknown fields are not automatically promoted.
- Checkpointing and Delta transaction semantics protect incremental reruns.
- Week 10 does not expand into Kafka infrastructure, Gold redesign or Power BI work.

## 5. Blockers / Risks / Rework

| Issue | Impact | Resolution |
|---|---|---|
| Week-10 docs were template-only | Implementation was not reviewable from repository docs | Filled with exact PropIQ objects, controls and captured results |
| Generic Kafka event schema did not match PropIQ | Event contract was not project-specific | Replaced with PropIQ listing-status contract |
| Supplemental live section contained PageLoop terminology | Cross-project contamination risk | Replaced with PropIQ naming and explicit supplemental boundary |
| Live section is a simple incremental consumer simulation | Must not be presented as production continuous streaming | Documentation states the limitation |
| Only four Week-10 screenshots are committed | Missing evidence must not be fabricated | Existing genuine screenshots retained; notebook remains source for supplemental evidence |

## 6. Evidence Added / Updated

- `notebooks/07_streaming_simulation.ipynb`
- `data_sample/streaming/`
- `streaming/kafka_event_schema.json`
- `streaming/structured_streaming_design.md`
- `weekly_logs/week10_log.md`
- existing `screenshots/week10_*`

## 7. AI Transparency Note

| Question | Response |
|---|---|
| Where AI helped | Playbook review, documentation restructuring, event-contract review and identification of remaining PageLoop/template remnants. |
| What changed after AI review | Week-10 design, schema and log were converted to PropIQ-specific content; remaining PageLoop terminology in the notebook was removed; the live section was explicitly marked supplemental. |
| What was verified manually | Six-drop counts, Trusted/Quarantine reconciliation, zero-unaccounted result, no-new-file rerun and live-event notebook outputs. |
| What the team can explain without AI | Source/landing/checkpoint, watermark, deduplication, sequence validation, quarantine, schema rescue, reconciliation, rerun behavior and Week-10 boundaries. |

## 8. Next Week Preparation

- Keep the Week-10 implementation stable.
- Carry validated Trusted/Quarantine evidence into Week 11 integration.
- Do not redesign Gold or Power BI inside the streaming notebook.
- Capture any additional mentor-requested screenshots from the actual Databricks workspace.
- Use Week 11 for integration, upstream correction/rebuild and end-to-end traceability.
