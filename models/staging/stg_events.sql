with raw as (

    -- Historical GA4 data
    select
        event_date,
        event_timestamp,
        user_pseudo_id,
        event_name,
        coalesce(traffic_source.source, 'direct') as source,
        coalesce(traffic_source.medium, 'none') as medium
    from `dbtproject-395506.ga4_demo.events_20210131`

    union all

    -- Real-time streaming data
    select
        cast(event_date as string) as event_date,
        cast(unix_micros(event_timestamp) as int64) as event_timestamp,
        user_pseudo_id,
        event_name,
        'direct' as source,                 
        'none' as medium
    from `dbtproject-395506.ga4_demo.events_stream`
)

select *
from raw
