# Data Quality Summary

**Week:** 6  
**Purpose:** Summarize PropIQ data quality rules, failures, quarantine handling and business impact.

---

## 1. Quality Rule Results

| Rule ID | Rule Name | Severity | Passed Count | Failed Count | Business Impact |
|---|---|---|---:|---:|---|
| P15-DQ-01 | Listing Identity & Duplicate Resolution | Critical | [count] | [count] | Invalid or unresolved listing identities can cause duplicate or incorrect property metrics |
| P15-DQ-02 | Listing Reference Integrity | Critical | [count] | [count] | Invalid locality or broker references can break downstream relationships and reporting |
| P15-DQ-03 | Price & Area Range Validation | Major | [count] | [count] | Invalid price or area values can distort property valuation and market analytics |
| P15-DQ-04 | Price per Sqft Reconciliation | Major | [count] | [count] | Incorrect derived pricing can produce misleading property comparisons and market metrics |
| P15-DQ-05 | Status & Completion Validation | Critical | [count] | [count] | Incorrect status or completion dates can affect sales, rental and inventory reporting |
| P15-DQ-06 | Lead Relationship & Timestamp Validation | Critical | [count] | [count] | Invalid listing relationships or timestamps can distort lead conversion and time-based analytics |
| P15-DQ-07 | Approved Domain Validation | Major | [count] | [count] | Unapproved categorical values can create inconsistent segmentation and dashboard results |
| P15-DQ-08 | Duplicate & Conflict Resolution | Major | [count] | [count] | Unresolved duplicate or conflicting lead/status records can distort lead and status metrics |

> **Note:** Replace `[count]` with the actual Databricks execution results. Do not use estimated or fabricated counts.

---

## 2. Failed Record Examples

| Rule ID | Sample Record ID | Failure Reason | Action / Handling |
|---|---|---|---|
| P15-DQ-01 | `[record_uid]` | Listing ID is NULL/blank or duplicate listing records cannot be resolved deterministically | Route to `quarantine_listings` |
| P15-DQ-02 | `[record_uid]` | Populated `locality_id` or `broker_id` does not resolve to the governed reference data | Route to `quarantine_listings` |
| P15-DQ-03 | `[record_uid]` | Asking price or area is outside the approved range, or required value is invalid | Route to `quarantine_listings` |
| P15-DQ-04 | `[record_uid]` | `price_per_sqft` does not reconcile with `asking_price / area_sqft` within 1% | Route to `quarantine_listings` |
| P15-DQ-05 | `[record_uid]` | Sold/rented listing has missing or invalid completion evidence | Route to `quarantine_listings` |
| P15-DQ-06 | `[record_uid]` | Lead does not reference a Trusted listing or lead timestamp occurs before listing creation | Route to `quarantine_leads` |
| P15-DQ-07 | `[record_uid]` | Categorical value falls outside the documented approved domain | Route to matching entity quarantine |
| P15-DQ-08 | `[record_uid]` | Duplicate/conflicting lead or status records cannot be resolved using deterministic precedence | Route to `quarantine_leads` / affected entity |

### Required Multi-Rule Example

| Record ID | Failed Rules | Failure Reasons | Final Handling |
|---|---|---|---|
| `[record_uid]` | `P15-DQ-02`, `P15-DQ-03` | Invalid reference + invalid price/area | One physical record routed to `quarantine_listings` with both failure IDs retained |

---

## 3. What Should Block Gold Metrics?

Any unresolved DQ failure must prevent the affected physical record from being exposed to Trusted Silver or Gold.

The following **Critical** rules require particular attention:

- **P15-DQ-01** — Invalid or unresolved listing identity can cause duplicate or unreliable property metrics.
- **P15-DQ-02** — Invalid locality/broker references can break downstream relationships.
- **P15-DQ-05** — Invalid status/completion evidence can corrupt sales and rental reporting.
- **P15-DQ-06** — Invalid lead-to-listing relationships or timestamps can affect conversion and time-based analytics.

Major rules should also prevent the affected records from entering Trusted Silver until the issue is resolved:

- **P15-DQ-03** — Invalid price/area values affect property analytics.
- **P15-DQ-04** — Incorrect `price_per_sqft` affects valuation and comparison metrics.
- **P15-DQ-07** — Unapproved categorical values affect segmentation and reporting.
- **P15-DQ-08** — Unresolved duplicates/conflicts affect lead and status metrics.

---

## 4. Quality Summary

Week 06 implemented the PropIQ Data Quality layer across Listings, Localities, Leads and Brokers.

The four Silver Candidate datasets are evaluated at the physical `record_uid` grain against P15-DQ-01 through P15-DQ-08.

Records with zero applicable failures are routed to the corresponding Trusted Silver table, while records with one or more failures are routed to the corresponding Quarantine table.

Multiple failures on the same physical record are retained through `failed_rule_ids`, rather than keeping only the first failure.

The most important dashboard risks are Critical failures involving listing identity, reference integrity, completion evidence and lead relationships.

The final quality assessment must be based on the actual Databricks rule scorecard and reconciliation results.

The mentor should review the multi-rule quarantine example, `record_uid` reconciliation, Trusted/Quarantine overlap and full-suite replay evidence carefully.

---

## 5. Trusted and Quarantine Outputs

| Entity | Trusted Silver Table | Quarantine Table |
|---|---|---|
| Listings | `silver_listings_trusted` | `quarantine_listings` |
| Localities | `silver_localities_trusted` | `quarantine_localities` |
| Leads | `silver_leads_trusted` | `quarantine_leads` |
| Brokers | `silver_brokers_trusted` | `quarantine_brokers` |

---

## 6. Reconciliation Requirement

For each entity and source/batch:

```text
Candidate distinct record_uid
=
Trusted distinct record_uid
+
Quarantine distinct record_uid
