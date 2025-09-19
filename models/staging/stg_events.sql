with raw as (

    -- Historical GA4 data
    select
        event_date,
        event_timestamp,
        user_pseudo_id,
        event_name,
        traffic_source.source as source,
        traffic_source.medium as medium
    from `dbtproject-395506.ga4_demo.events_20210131`

    union all

    -- Real-time streaming data
    select
        event_date,
        event_timestamp,
        user_pseudo_id,
        event_name,
        source,
        medium
    from `dbtproject-395506.ga4_demo.events_stream`
)

select *
from raw
