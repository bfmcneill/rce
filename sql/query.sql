-- CTE that will select created date from JSON
with cte as (
    select c.subreddit_id
    , c.comment_id
    ,(c.data ->> 'created_utc')::bigint as created_utc
    , to_timestamp((c.data ->> 'created_utc')::bigint) as created
     from comment_raw c
 )


select *
from cte
where created_utc >= 1655013600
order by created asc