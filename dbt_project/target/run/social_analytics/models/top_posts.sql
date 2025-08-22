
  
    

  create  table "social_analytics"."analytics_analytics"."top_posts__dbt_tmp"
  
  
    as
  
  (
    

with ranked as (
    select
        id,
        platform,
        author_name,
        content_text,
        content_url,
        (like_count + comment_count + share_count) as engagement_score,
        row_number() over (order by (like_count + comment_count + share_count) desc) as overall_rank,
        row_number() over (partition by platform order by (like_count + comment_count + share_count) desc) as platform_rank
    from "social_analytics"."analytics_analytics"."stg_posts"
)
select *
from ranked
where overall_rank <= 5
   or platform_rank <= 3
  );
  