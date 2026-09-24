# Week 09 Log — Pricing, Locality and Performance Dashboard

**Week:** 9  
**Date range:** [Add dates]  
**Team:** Team 15  
**Project:** PropIQ – Real Estate Market Analytics  

---

## 1. Sprint Goal

Refine the existing Gold-only Power BI dashboard into a decision-ready three-page report. Complete the Locality and Pricing Intelligence and Listing, Broker and Lead Performance pages, improve interactions and accessibility, and develop evidence-backed insights from the validated Gold metrics.

---

## 2. Work Completed

| Task | Owner | Status | Evidence |
|---|---|---|---|
| Continued development using the Week 08 Power BI model | Thota Madhulika | Done | `dashboard/powerbi_dashboard.pbix` |
| Completed Locality and Pricing Intelligence page | Thota Madhulika | Done | Power BI Page 2 |
| Added locality-level pricing and inventory visuals | Thota Madhulika | Done | Dashboard screenshot |
| Added pricing and property-configuration analysis | P. Lakshmi Naga Sree | Done | Power BI Page 2 |
| Completed Listing, Broker and Lead Performance page | P. Lakshmi Naga Sree | Done | Power BI Page 3 |
| Added lead conversion and average leads per listing analysis | Vadlamuru Rishitha | Done | Dashboard screenshot |
| Added broker performance analysis | Vadlamuru Rishitha | Done | Dashboard screenshot |
| Added listing performance and inventory-age analysis | Vadlamuru Rishitha | Done | Dashboard screenshot |
| Tested slicers, filtering and page interactions | All Members | Done | Interaction evidence |
| Reviewed visual hierarchy, labels and readability | All Members | Done | Final dashboard |
| Reconciled important filtered dashboard values with Gold | All Members | Done | Validation evidence |
| Documented evidence-backed dashboard insights | All Members | Done | `docs/dashboard_insights.md` |
| Updated dashboard documentation and Week 09 evidence | All Members | Done | GitHub repository |

---

## 3. Key Decisions

- Continued using the same Gold-only Power BI model created during Week 08.
- Designed Page 2 around locality, pricing, inventory and property-mix questions.
- Designed Page 3 around listing, broker and lead performance.
- Kept listing and lead facts separate to avoid lead fan-out and incorrect conversion calculations.
- Used approved Gold metrics instead of recreating upstream transformations inside Power BI.
- Tested filters and interactions to ensure displayed metrics remained consistent with the underlying Gold data.
- Improved dashboard presentation without changing the approved Gold KPI definitions.
- Documented insights only when they could be supported by the available Gold metrics.
- Prepared the dashboard for the next engineering phase involving controlled streaming simulation.

---

## 4. Blockers / Risks

| Blocker | Impact | Help Needed |
|---|---|---|
| Different Gold tables represent different grains | Incorrect relationships may multiply measures | Keep tables independent or use documented shared dimensions |
| Filter interactions can change displayed measures | Dashboard values may differ from Gold | Validate important visuals under identical filter states |
| Too many visuals can reduce readability | Business questions become difficult to identify | Prioritize important metrics and simplify layouts |
| KPI denominators require consistent definitions | Conversion metrics may become misleading | Follow the approved KPI definitions |
| Dashboard insights must be data-supported | Unsupported conclusions may be produced | Trace each insight to its relevant Gold table or KPI |

---

## 5. Evidence Added to GitHub

- Updated `dashboard/powerbi_dashboard.pbix`
- Added Page 2 — Locality and Pricing Intelligence screenshot
- Added Page 3 — Listing, Broker and Lead Performance screenshot
- Added slicer and filter interaction evidence
- Added dashboard validation screenshots
- Added filtered measure reconciliation evidence
- Updated `dashboard/README.md`
- Added/updated `docs/dashboard_insights.md`
- Updated `weekly_logs/week09_log.md`

---

## 6. AI Transparency Note

| Question | Response |
|---|---|
| Where AI helped | AI helped suggest dashboard organization, visualization options, Power BI modelling checks, and approaches for explaining Gold-backed business insights. |
| What we changed after AI suggestion | We selected visuals according to the actual PropIQ Gold tables and approved KPI definitions instead of directly using generic dashboard recommendations. |
| What we verified manually | Dashboard values, filters, relationships, measures, Gold sources and important insight calculations were checked against the Databricks Gold layer. |
| What we can explain without AI | The team can explain why each dashboard page exists, which business question each visual addresses, which Gold table provides the metric, how filters affect the report and how values were validated. |

---

## 7. Next Week Preparation

- Freeze and review the refined Power BI dashboard.
- Prepare the repository for the Week 10 controlled streaming simulation.
- Review the six controlled event-drop scenarios.
- Prepare streaming ingestion with explicit schema handling.
- Implement checkpointing and event-time watermarking.
- Implement event-ID deduplication.
- Handle late and out-of-order events.
- Prepare quarantine handling for malformed, orphan and invalid events.
- Review schema-drift and rescued-data handling.
