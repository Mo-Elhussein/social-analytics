-- fct_daily_metrics.sql
-- -----------------------------------------------
-- Fact table: aggregate engagement & comments 
-- for each post.
-- -----------------------------------------------

select
    post_id,
    title,
    sum(engagement) as total_engagement,
    sum(comments) as total_comments
from {{ ref('stg_posts') }}
group by post_id, title;
