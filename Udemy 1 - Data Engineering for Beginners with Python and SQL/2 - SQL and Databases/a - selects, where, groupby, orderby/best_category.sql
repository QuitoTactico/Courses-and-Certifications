-- Write your SQL query here to find the most popular product category
select product_category as `Product Category`, count(*) as `Number of Products`
from products
group by product_category
order by `Number of Products` desc
limit 1