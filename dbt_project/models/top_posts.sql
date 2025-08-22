-- top_posts.sql
-- -----------------------------------------------
-- Analytics table: select top 5 posts ranked 
-- by total engagement.
-- -----------------------------------------------

select
    post_id,
    title,
    total_engagement,
    total_comments
from {{ ref('fct_daily_metrics') }}
order by total_engagement desc
limit 5;
