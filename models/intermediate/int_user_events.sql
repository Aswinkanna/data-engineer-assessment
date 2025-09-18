-- models/intermediate/int_user_events.sql
with events as (
    select
        *,
        row_number() over (
            partition by user_pseudo_id, event_name
            order by event_timestamp
        ) as rn
    from {{ ref('stg_events') }}
)

select *
from events
where rn = 1
