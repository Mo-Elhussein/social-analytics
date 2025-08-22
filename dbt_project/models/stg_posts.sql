-- stg_posts.sql
-- -----------------------------------------------
-- Staging layer: unify YouTube & Reddit posts 
-- into a single view for further transformations.
-- -----------------------------------------------

with youtube as (
    select
        video_id as post_id,
        title,
        views as engagement,
        likes,
        comments
    from youtube_posts
),

reddit as (
    select
        post_id,
        title,
        upvotes as engagement,
        null as likes,
        comments
    from reddit_posts
)

select * from youtube
union all
select * from reddit;
