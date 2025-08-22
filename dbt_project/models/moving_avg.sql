-- moving_avg.sql
-- -----------------------------------------------
-- Analytics table: calculate moving average of 
-- engagement over posts (mock example).
-- -----------------------------------------------

select
    post_id,
    title,
    avg(total_engagement) over (
        order by post_id 
        rows between 2 preceding and current row
    ) as moving_avg_engagement
from {{ ref('fct_daily_metrics') }};
