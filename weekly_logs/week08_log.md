# Week 08 Log — Power BI Foundation and Gold Hand-off

**Week:** 8  
**Date range:** [Add dates]  
**Team:** Team 15  
**Project:** PropIQ – Real Estate Market Analytics  

---

## 1. Sprint Goal

Validate the approved Gold tables and prepare the governed Gold-to-Power BI hand-off. Export/connect the required Gold datasets, build the initial Power BI data model and first working dashboard page, and reconcile selected dashboard measures against their owning Gold tables.

The Power BI layer uses approved Gold data only, while preserving the grain and meaning of each Gold table.

---

## 2. Work Completed

| Task | Owner | Status | Evidence |
|---|---|---|---|
| Reviewed approved Gold tables required for Power BI | Thota Madhulika | Done | Databricks / Gold source register |
| Validated Gold table grain, keys and KPI purpose | Thota Madhulika | Done | Databricks notebook |
| Created controlled Gold exports/connections for Power BI | Thota Madhulika | Done | `notebooks/06_powerbi_export.ipynb` |
| Validated Gold-to-export row counts and selected fields | P. Lakshmi Naga Sree | Done | Export reconciliation output |
| Imported approved Gold data into Power BI | P. Lakshmi Naga Sree | Done | Power BI model |
| Configured Power BI field data types | Vadlamuru Rishitha | Done | Power BI model screenshot |
| Reviewed relationships and cardinality between Gold tables | Vadlamuru Rishitha | Done | Power BI model |
| Created initial Power BI measures and visuals | Vadlamuru Rishitha | Done | `dashboard/powerbi_dashboard.pbix` |
| Created the first working dashboard page | All Members | Done | Power BI screenshot |
| Reconciled selected Power BI values with Gold queries | All Members | Done | Reconciliation evidence |
| Updated dashboard documentation and Week 08 evidence | All Members | Done | GitHub repository |

---

## 3. Key Decisions

- Power BI was connected only to approved Gold outputs.
- Raw, Bronze, Silver Candidate, Trusted Silver detail and Quarantine data were not used directly in Power BI.
- Gold tables with different grains were kept separate instead of being flattened into a single dataset.
- Relationships were created only when the shared key, cardinality and filter direction were understood and considered safe.
- Dashboard visuals were designed around business questions rather than simply creating one visual for every Gold table.
- Important Power BI measures were traced back to their owning Gold tables.
- Selected dashboard values were reconciled against Databricks Gold queries using the same filter context.
- The Week 08 Power BI model will continue into Week 09 instead of being rebuilt.

---

## 4. Blockers / Risks

| Blocker | Impact | Help Needed |
|---|---|---|
| Gold tables have different grains | Unsafe relationships can cause duplicated totals | Preserve individual table grains and review relationships |
| Exported data must remain consistent with Gold | Power BI values may differ from Databricks | Re-run exports and reconcile with Gold |
| Power BI can infer incorrect field types | Incorrect dates or aggregations may affect visuals | Manually verify field types |
| Large Gold exports may increase repository size | Difficult GitHub management | Commit only small validated exports where appropriate |
| Filter context can change dashboard measures | Visual values may not match Gold | Reconcile important measures using identical filters |

---

## 5. Evidence Added to GitHub

- Updated `notebooks/06_powerbi_export.ipynb`
- Added validated Gold exports under `data_sample/gold_exports/` where applicable
- Added `dashboard/powerbi_dashboard.pbix`
- Updated `dashboard/README.md`
- Added Gold source register evidence
- Added Gold-to-export reconciliation screenshot
- Added Power BI model screenshot
- Added first working dashboard screenshot
- Added measure-to-Gold reconciliation evidence
- Updated `weekly_logs/week08_log.md`

---

## 6. AI Transparency Note

| Question | Response |
|---|---|
| Where AI helped | AI helped structure the Gold export workflow, explain Power BI modelling patterns, identify possible grain and relationship risks, and organize the Week 08 documentation. |
| What we changed after AI suggestion | We adapted the suggested workflow to the actual PropIQ Gold tables, preserved separate table grains, selected only required Gold fields, and reviewed relationship decisions manually. |
| What we verified manually | Gold table existence, grain, exported data, field types, Power BI relationships, measures, dashboard values and reconciliation results were checked manually. |
| What we can explain without AI | The team can explain the Gold-to-Power BI workflow, Gold table grain, relationship risks, Power BI modelling decisions and reconciliation process. |

---

## 7. Next Week Preparation

- Continue with the same Power BI model.
- Complete and refine the remaining dashboard pages.
- Improve visual hierarchy, labels, layout and usability.
- Test slicers and filter interactions.
- Develop evidence-backed dashboard insights.
- Reconcile important filtered dashboard values with their owning Gold tables.
- Prepare presentation-ready dashboard evidence.
