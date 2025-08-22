
  
    

  create  table "social_analytics"."analytics_analytics"."fct_daily_metrics__dbt_tmp"
  
  
    as
  
  (
    

select
    platform,
    date_trunc('day', posted_at_utc) as post_date,
    count(*) as total_posts,
    sum(like_count) as total_likes,
    sum(comment_count) as total_comments,
    sum(share_count) as total_shares,
    sum(like_count + comment_count + share_count) as engagement_score
from "social_analytics"."analytics_analytics"."stg_posts"
group by platform, date_trunc('day', posted_at_utc)
  );
  