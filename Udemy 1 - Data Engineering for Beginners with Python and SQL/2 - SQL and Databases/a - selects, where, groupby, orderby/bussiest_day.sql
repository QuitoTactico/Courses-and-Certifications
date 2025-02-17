-- Write your SQL query here to find the busiest order date
select order_date as `Order Date`, count(*) as `Number of Orders`
from orders
group by order_date
order by `Number of Orders` desc
limit 1