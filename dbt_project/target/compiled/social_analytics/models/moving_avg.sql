


with base as (
    select
        platform,
        date_trunc('day', posted_at_utc) as post_date,
        (like_count + comment_count + share_count) as engagement
    from "social_analytics"."analytics_analytics"."stg_posts"
),

daily as (
    select
        platform,
        post_date,
        sum(engagement) as daily_engagement
    from base
    group by platform, post_date
)

select
    platform,
    post_date,
    daily_engagement,
    avg(daily_engagement) over (
        partition by platform
        order by post_date
        rows between 6 preceding and current row
    ) as engagement_7d_moving_avg
from daily
order by platform, post_date