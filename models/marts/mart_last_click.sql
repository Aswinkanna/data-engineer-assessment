-- models/marts/mart_last_click.sql
select
    user_pseudo_id,
    max(event_timestamp) as last_event_time,
    array_agg(
        struct(event_name, source, medium)
        order by event_timestamp desc limit 1
    )[offset(0)] as last_touch
from {{ ref('int_user_events') }}
group by user_pseudo_id
