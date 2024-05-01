-- 1. Display air quality pollutants 

select distinct parameter as pollutant
from measurements;

-- 2. Display avg value of pollutants 
select country,
round(avg(value), 2) as avg_value
from measurements
group by country
order by avg_value desc
limit 10;
--- 


-- Particulate matter 10, safe levels
with max_val_cte as (
    select distinct country, value, date_utc,
    case when value < 40 then 'Good'
         when value >= 40 and value < 80 then 'Fair' 
         when value >= 80 and value < 120 then 'Poor'
         when value >= 120 and value < 300 then 'Very poor'
         when value >= 300 then 'Extremely poor'
    end as air_quality
    from measurements
    where parameter = 'pm10'
    group by country, value, date_utc
)
select distinct country, value, date_utc
from max_val_cte
where air_quality = 'Good'
limit 10;


-- Guideline value
