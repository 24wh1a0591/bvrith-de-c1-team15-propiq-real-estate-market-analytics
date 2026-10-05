# Data Quality Summary

**Week:** 6  
**Source:** executed `notebooks/04_data_quality_checks.ipynb`.

## Rule-failure scorecard
| Entity | Rule | Failed rows |
|---|---|---:|
| listings | P15-DQ-01 | 500 |
| listings | P15-DQ-02 | 200 |
| listings | P15-DQ-03 | 200 |
| listings | P15-DQ-04 | 350 |
| listings | P15-DQ-05 | 150 |
| listings | P15-DQ-07 | 0 |
| localities | P15-DQ-07 | 0 |
| brokers | P15-DQ-07 | 0 |
| leads | P15-DQ-06 | 1,200 |
| leads | P15-DQ-07 | 0 |
| leads | P15-DQ-08 | 1,600 |

Total rule failures: **4,200**. A physical record can contribute to multiple rule counts.

## Physical reconciliation
| Entity | Candidate | Trusted | Quarantine | Variance |
|---|---:|---:|---:|---:|
| Listings | 50,200 | 49,000 | 1,200 | 0 |
| Localities | 80 | 80 | 0 | 0 |
| Leads | 120,800 | 118,000 | 2,800 | 0 |
| Brokers | 320 | 320 | 0 | 0 |

Trusted/Quarantine overlap was 0 for all four entities and route-membership checks returned 0.

## Severity
Critical: P15-DQ-01, 02, 05, 06. Major: P15-DQ-03, 04, 07, 08.

## DQ-07 limitation
The available project specification did not provide a complete approved categorical-domain dictionary, and `propiq_governed_domains` was unavailable in the Databricks environment. The implementation therefore does not claim full governed-domain validation and does not invent an allowed-value list.

## Replay rule
Corrections must be replayed from the upstream source through Silver Candidate and the full applicable DQ suite. Do not insert Quarantine rows directly into Trusted.
