-- display air quality parameters

select distinct parameter as pollutant
from measurements;

-- 
select country,
round(avg(value), 2) as avg_value
from measurements
group by country
order by avg_value desc
limit 10;
--- 

with max_val_cte as (
    select country,  max(value) as max_val, parameter,
    dense_rank() over(order by max(value) desc) as rk
    from measurements
    group by country, parameter
)
select country, parameter, max_val
from max_val_cte
where;