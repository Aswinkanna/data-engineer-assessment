-- models/marts/mart_first_click.sql
select
    user_pseudo_id,
    min(event_timestamp) as first_event_time,
    array_agg(
        struct(event_name, source, medium)
        order by event_timestamp asc limit 1
    )[offset(0)] as first_touch
from {{ ref('int_user_events') }}
group by user_pseudo_id
