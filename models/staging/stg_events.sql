WITH raw AS (

    -- Historical GA4 data
    SELECT
        event_date,
        event_timestamp,
        user_pseudo_id,
        event_name,
        COALESCE(traffic_source.source, 'direct') AS source,
        COALESCE(traffic_source.medium, 'none')  AS medium,
        TIMESTAMP_MICROS(event_timestamp) AS event_ts  -- convert INT64 microseconds to TIMESTAMP
    FROM `dbtproject-395506.ga4_demo.events_2021*`

    UNION ALL

    -- Real-time streaming data
    SELECT
        CAST(event_date AS STRING) AS event_date,
        CAST(event_timestamp AS INT64) AS event_timestamp,
        user_pseudo_id,
        event_name,
        'direct' AS source,
        'none'   AS medium,
        TIMESTAMP_MICROS(event_timestamp) AS event_ts  -- convert streaming INT64 microseconds
    FROM `dbtproject-395506.ga4_demo.events_stream`

)

SELECT *
FROM raw
