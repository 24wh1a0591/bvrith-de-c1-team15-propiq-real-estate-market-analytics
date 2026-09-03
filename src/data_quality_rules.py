"""
PropIQ - Data Quality Rules

Week: 6
Team: Team 15
Project: P15 PropIQ - Real Estate Market Analytics

Purpose:
    Keep reusable PySpark data quality helper functions here.

Note:
    The main Week 06 DQ execution is performed in the Spark SQL notebook.
    These helpers are reusable building blocks for the approved
    P15-DQ-01 through P15-DQ-08 rules.

Important:
    Physical routing and reconciliation must use record_uid.
    Business/reference keys such as listing_id, lead_id, locality_id
    and broker_id must not be used to hide physical records.
"""


# ---------------------------------------------------------------------------
# P15-DQ-01
# Required field / listing identity
# ---------------------------------------------------------------------------

def required_field_rule(df, field_name):
    """
    Return records where a required field is NULL or blank.

    Used for required business/reference fields such as:
        listing_id
        lead_id
        locality_id
        broker_id
    """
    return df.filter(
        df[field_name].isNull() |
        (df[field_name].cast("string") == "")
    )


# ---------------------------------------------------------------------------
# Duplicate-key detection
# ---------------------------------------------------------------------------

def duplicate_key_rule(df, key_field):
    """
    Return duplicate business keys and their physical record counts.

    Duplicate business keys are not automatically removed.
    Physical records must remain visible for DQ evaluation.
    """
    return (
        df.groupBy(key_field)
        .count()
        .filter("count > 1")
    )


# ---------------------------------------------------------------------------
# P15-DQ-02
# Reference integrity
# ---------------------------------------------------------------------------

def valid_reference_rule(
    fact_df,
    reference_df,
    fact_key,
    reference_key
):
    """
    Return fact records whose reference key does not exist
    in the supplied reference/master dataset.

    Uses a left anti-join so orphan records remain visible.

    Example:
        invalid_records = valid_reference_rule(
            listings_df,
            localities_df,
            "locality_id",
            "locality_id"
        )
    """
    return fact_df.join(
        reference_df.select(reference_key).dropDuplicates(),
        fact_df[fact_key] == reference_df[reference_key],
        "left_anti"
    )


# ---------------------------------------------------------------------------
# P15-DQ-03
# Numeric range validation
# ---------------------------------------------------------------------------

def numeric_range_rule(
    df,
    field_name,
    minimum_value,
    maximum_value
):
    """
    Return records where a numeric field is NULL or outside
    the approved inclusive range.
    """
    return df.filter(
        df[field_name].isNull() |
        (df[field_name] < minimum_value) |
        (df[field_name] > maximum_value)
    )


# ---------------------------------------------------------------------------
# P15-DQ-04
# Price-per-square-foot validation
# ---------------------------------------------------------------------------

def price_per_sqft_rule(
    df,
    price_field,
    area_field,
    derived_field,
    tolerance=0.01
):
    """
    Return records where stored/derived price_per_sqft does not
    reconcile with price / area within the approved tolerance.

    A NULL/zero-area guard is applied before division.

    Default tolerance:
        1%
    """

    expected = (
        df[price_field].cast("double") /
        df[area_field].cast("double")
    )

    relative_error = (
        (df[derived_field].cast("double") - expected).abs()
        / expected.abs()
    )

    return df.filter(
        df[price_field].isNull() |
        df[area_field].isNull() |
        (df[area_field] <= 0) |
        df[derived_field].isNull() |
        (relative_error > tolerance)
    )


# ---------------------------------------------------------------------------
# P15-DQ-05 / P15-DQ-06
# Timestamp chronology validation
# ---------------------------------------------------------------------------

def timestamp_order_rule(
    df,
    earlier_field,
    later_field
):
    """
    Return records where the later timestamp occurs before
    the earlier timestamp.

    Example:
        listing creation -> lead timestamp
    """
    return df.filter(
        df[earlier_field].isNull() |
        df[later_field].isNull() |
        (df[later_field] < df[earlier_field])
    )


# ---------------------------------------------------------------------------
# P15-DQ-07
# Documented unapproved-domain sentinel
# ---------------------------------------------------------------------------

UNAPPROVED_DOMAIN_SENTINEL = "unknown-new-code"


def invalid_domain_sentinel_rule(df, field_name):
    """
    Return records containing the explicitly documented
    Team 15 example of an unapproved categorical value.

    The supplied Team 15 DQ guide does not provide a complete
    domain dictionary. Therefore this helper does not invent
    additional allowed values.
    """
    return df.filter(
        df[field_name].isNull() |
        (df[field_name].cast("string") == "") |
        (
            df[field_name]
            .cast("string")
            .lower()
            == UNAPPROVED_DOMAIN_SENTINEL
        )
    )


# ---------------------------------------------------------------------------
# DQ routing
# ---------------------------------------------------------------------------

def add_dq_status(df, failed_rule_column="failed_rule_ids"):
    """
    Add PASS/FAIL routing status.

    Empty failure list:
        PASS -> Trusted Silver

    One or more failures:
        FAIL -> Quarantine
    """
    from pyspark.sql import functions as F

    return df.withColumn(
        "dq_status",
        F.when(
            F.col(failed_rule_column).isNull() |
            (F.trim(F.col(failed_rule_column)) == ""),
            F.lit("PASS")
        ).otherwise(F.lit("FAIL"))
    )


# ---------------------------------------------------------------------------
# Multi-rule failure support
# ---------------------------------------------------------------------------

def add_failed_rule(
    df,
    condition,
    rule_id,
    output_column="failed_rule_ids"
):
    """
    Append a DQ rule ID to the physical record's failure list
    when the supplied condition is true.

    This preserves multiple applicable failures on one record.
    """
    from pyspark.sql import functions as F

    existing = F.coalesce(
        F.col(output_column),
        F.lit("")
    )

    return df.withColumn(
        output_column,
        F.when(
            condition,
            F.when(
                F.trim(existing) == "",
                F.lit(rule_id)
            ).otherwise(
                F.concat(existing, F.lit(", "), F.lit(rule_id))
            )
        ).otherwise(existing)
    )


# ---------------------------------------------------------------------------
# Physical reconciliation helper
# ---------------------------------------------------------------------------

def reconciliation_summary(
    candidate_df,
    trusted_df,
    quarantine_df,
    record_uid="record_uid"
):
    """
    Return physical record counts used for Candidate ->
    Trusted + Quarantine reconciliation.

    Expected condition:

        Candidate distinct record_uid
        =
        Trusted distinct record_uid
        +
        Quarantine distinct record_uid
    """
    from pyspark.sql import functions as F

    candidate_count = (
        candidate_df
        .select(record_uid)
        .distinct()
        .count()
    )

    trusted_count = (
        trusted_df
        .select(record_uid)
        .distinct()
        .count()
    )

    quarantine_count = (
        quarantine_df
        .select(record_uid)
        .distinct()
        .count()
    )

    variance = (
        candidate_count -
        trusted_count -
        quarantine_count
    )

    return {
        "candidate_distinct_record_uid": candidate_count,
        "trusted_distinct_record_uid": trusted_count,
        "quarantine_distinct_record_uid": quarantine_count,
        "variance": variance,
        "reconciliation_pass": variance == 0,
    }


# ---------------------------------------------------------------------------
# Trusted / Quarantine overlap helper
# ---------------------------------------------------------------------------

def trusted_quarantine_overlap(
    trusted_df,
    quarantine_df,
    record_uid="record_uid"
):
    """
    Return the number of physical record_uid values that appear
    in both Trusted Silver and Quarantine.

    Expected result:
        0
    """
    return (
        trusted_df
        .select(record_uid)
        .distinct()
        .join(
            quarantine_df.select(record_uid).distinct(),
            record_uid,
            "inner"
        )
        .count()
    )
