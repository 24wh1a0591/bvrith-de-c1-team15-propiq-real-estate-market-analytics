# Week 03 Log — Data Exploration, Relationships and Join Safety

**Week:** 3  
**Date range:** 25 July 2026 – 30 July 2026  
**Team:** Team 15  
**Project:** PropIQ – Real Estate Market Analytics

## Sprint goal
Profile the four PropIQ sources, establish grain/business keys, validate relationships and fan-out risks, and create only the Week-3 Bronze demonstration.

## Work completed
- Loaded listings, leads, localities and brokers from the PropIQ Volume.
- Profiled schemas, physical/business keys and domains.
- Added Listings→Localities, Listings→Brokers and Leads→Listings anti-joins.
- Added listing/lead fan-out validation.
- Created `propiq_week03_bronze_demo_listings` and a lineage demo view.
- Kept full Bronze ingestion in Week 04 scope.

## Key decisions
`record_uid` is the physical reconciliation key. Business keys are used for relationships, not to hide physical duplicates. One-to-many lead joins are never used for listing-grain metrics.

## Risk correction
The original notebook contained PageLoop/loan remnants. It has been replaced with PropIQ-specific exploration and relationship checks.

## AI transparency
AI assisted with restructuring and review. Dataset paths, fields, relationship checks and scope boundaries were verified against the project artifacts.
