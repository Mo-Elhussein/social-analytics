
  create view "social_analytics"."analytics_analytics"."stg_posts__dbt_tmp"
    
    
  as (
    

select
    id,
    platform,
    platform_post_id,
    author_name,
    content_text,
    content_url,
    coalesce(like_count, 0) as like_count,
    coalesce(comment_count, 0) as comment_count,
    coalesce(share_count, 0) as share_count,
    posted_at_utc,
    collected_at_utc
from public.posts
  );