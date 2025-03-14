-- Product Lines with More Than a Specified Number of Products

-- Find product lines that offer a diverse product portfolio 
-- by listing those that have more than five products.

SELECT productline, COUNT(*) AS numberOfProducts
FROM products
GROUP BY productline
HAVING COUNT(*) > 5;

-- ------------------ first try: -----------------------

with cte_products_per_productlines as (
  select productline, count(*) as numberOfProducts
  from products
  GROUP by productline
)

select * 
from cte_products_per_productlines
WHERE numberOfProducts > 5;