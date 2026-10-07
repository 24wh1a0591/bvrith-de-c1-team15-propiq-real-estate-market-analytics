# Week 08 Log — Power BI Foundation and Gold Hand-off

**Week:** 8  
**Date range:** 18 sep 2026 -22 sep 2026
**Team:** Team 15  
**Project:** PropIQ – Real Estate Market Analytics

## Sprint goal

Hand the validated Gold layer to Power BI using only approved Gold outputs, preserve the declared listing and lead grains, create the first working Power BI dashboard page, and reconcile selected Power BI values back to their owning Gold sources.

## Outcome

The validated Gold layer was handed off to Power BI without bypassing the governed Gold layer.

The Power BI foundation was established using approved Gold outputs, separate listing and lead fact grains were preserved, selected report-facing values were checked against their Gold sources, and the first working dashboard page/model was established as the foundation for the continued three-page dashboard work in Week 09.

## Work completed

| Task | Ownership | Status | Evidence |
|---|---|---|---|
| Validate approved Gold sources for Power BI hand-off | Thota Madhulika; P. Lakshmi Naga Sree; Vadlamuru Rishitha | Completed | Gold source validation |
| Preserve listing and lead fact grains | Thota Madhulika; P. Lakshmi Naga Sree; Vadlamuru Rishitha | Completed | Power BI model / Gold contracts |
| Prepare controlled Gold-to-Power-BI hand-off | Thota Madhulika; P. Lakshmi Naga Sree; Vadlamuru Rishitha | Completed | `notebooks/06_powerbi_export.ipynb` |
| Validate selected export/model values against Gold | Thota Madhulika; P. Lakshmi Naga Sree; Vadlamuru Rishitha | Completed | Export/read-back and reconciliation checks |
| Establish Power BI model and first working page | Thota Madhulika; P. Lakshmi Naga Sree; Vadlamuru Rishitha | Completed | `dashboard/powerbi_dashboard.pbix` |
| Document dashboard source/model/page mapping | Thota Madhulika; P. Lakshmi Naga Sree; Vadlamuru Rishitha | Completed | `dashboard/README.md` |
| Prepare dashboard continuation for Week 09 | Thota Madhulika; P. Lakshmi Naga Sree; Vadlamuru Rishitha | Completed | Dashboard structure |

## Files / Objects

### Notebook

- `notebooks/06_powerbi_export.ipynb`

### Gold export area

- `data_sample/gold_exports/`

### Power BI dashboard

- `dashboard/powerbi_dashboard.pbix`
- `dashboard/README.md`

### Dashboard documentation

- `docs/dashboard_insights.md`

### Weekly evidence

- `weekly_logs/week08_log.md`

## Power BI source and grain controls

Power BI consumes approved Gold outputs only.

The Power BI hand-off does not bypass the governed pipeline by directly connecting to:

- Raw source data
- Bronze data
- Silver Candidate data
- Trusted Silver detail
- Quarantine data

The listing and lead facts remain at their respective approved grains.

The Power BI model therefore does not use an uncontrolled raw/Silver join to manufacture dashboard metrics.

## Validation

| Validation check | Result | What it proves |
|---|---|---|
| Gold source validation | Completed | Selected Power BI inputs come from approved Gold outputs |
| Grain validation | Completed | Listing and lead fact grains remain separated |
| Export/model value validation | Completed | Selected report-facing values agree with Gold |
| Gold-to-Power-BI reconciliation | Completed | Selected dashboard values can be traced back to their owning Gold sources |
| Power BI source check | Completed | Dashboard does not bypass the governed Gold hand-off |

Selected export/model values were reviewed against the corresponding Gold outputs before being used in the dashboard.

## Blockers / Rework

The main control for Week 08 was preventing Power BI from becoming a second transformation layer.

The dashboard therefore uses the governed Gold outputs rather than rebuilding business logic from raw, Bronze, Silver Candidate or Trusted Silver detail.

Any dashboard-level calculations must remain consistent with the approved Gold KPI definitions and grain contracts.

## Individual Contribution

### Thota Madhulika

- Participated in the Power BI foundation and Gold hand-off work.
- Participated in validation of the selected Gold-to-Power-BI values.
- Backup responsibility: review source/grain consistency and reconciliation.
- Speaking responsibility: explain the Gold-to-Power-BI hand-off, source selection and grain controls.

### P. Lakshmi Naga Sree

- Participated in Power BI modelling and dashboard foundation work.
- Participated in validation of the selected report-facing data.
- Backup responsibility: review dashboard model relationships and downstream impact.
- Speaking responsibility: explain the Power BI model, selected sources and relationship controls.

### Vadlamuru Rishitha

- Participated in dashboard evidence, documentation and downstream readiness work.
- Participated in reviewing the Power BI hand-off and dashboard structure.
- Backup responsibility: review validation evidence and dashboard documentation.
- Speaking responsibility: explain dashboard evidence, reconciliation and downstream readiness.

## Mentor Rework Status

**Status:** Review / validation completed for the Week-08 hand-off.

The Week-08 scope remains limited to the Power BI foundation and first working dashboard page.

Dashboard refinement and the broader insight/story work continue into Week 09.

## GitHub Evidence

The primary Week-08 evidence paths are:

- `notebooks/06_powerbi_export.ipynb`
- `data_sample/gold_exports/`
- `dashboard/powerbi_dashboard.pbix`
- `dashboard/README.md`
- `docs/dashboard_insights.md`
- `weekly_logs/week08_log.md`

These artifacts provide the implementation, hand-off, dashboard and documentation evidence for the week.

## AI Transparency Note

AI assisted with Power BI modelling checks, documentation organization and review of the Gold-to-dashboard hand-off.

The generated suggestions were treated as implementation support rather than authoritative project decisions.

The team manually reviewed:

- Gold source selection.
- Listing and lead grain separation.
- Power BI model relationships.
- Selected export/model values.
- Gold-to-Power-BI reconciliation.
- Dashboard source and documentation.

The students remain responsible for explaining the dashboard model, Gold source contracts, relationship decisions and validation results.

## Next Week Preparation

Week 09 will continue from the established Power BI foundation.

The next stage should focus on dashboard refinement, business insight development, KPI presentation and user-facing analytical storytelling without bypassing the governed Gold layer.
