# Week 05 Log — Silver Candidate Transformation

**Week:** 5  
**Team:** Team 15  
**Project:** PropIQ – Real Estate Market Analytics

## Sprint goal
Transform Bronze inputs into typed, normalized Silver Candidate datasets while preserving lineage and physical grain.

## Work completed
- Standardized listings, leads, localities and brokers.
- Applied safe type casting and date/timestamp normalization.
- Derived `calculated_price_per_sqft`, `price_per_sqft_variance`, chronology fields, completion flags and listing-age fields.
- Preserved `record_uid` and source/lineage metadata.
- Produced the four Candidate tables consumed by Week 06.

## Key decisions
No cross-entity joins are required for Candidate construction. Invalid values remain visible for DQ rather than being silently dropped.

## AI transparency
AI assisted with schema mapping and documentation. Actual fields and derived controls were checked against the Silver notebook and project data dictionary.
