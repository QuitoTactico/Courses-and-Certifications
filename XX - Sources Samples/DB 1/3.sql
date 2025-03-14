-- Most and Least Expensive Product in Each Product Line

-- Identify and list the most and least expensive buy prices 
-- within each product line, showcasing the price range of products.

WITH cte_max AS (
    SELECT productLine, 
           productcode AS mostExpensiveProductCode, 
           productname AS mostExpensiveProductName, 
           buyprice AS mostExpensiveBuyPrice
    FROM products
    WHERE buyprice = (
        SELECT MAX(buyprice)
        FROM products AS p2
        WHERE p2.productLine = products.productLine
    )
), cte_min AS (
    SELECT productLine, 
           productcode AS leastExpensiveProductCode, 
           productname AS leastExpensiveProductName, 
           buyprice AS leastExpensiveBuyPrice
    FROM products
    WHERE buyprice = (
        SELECT MIN(buyprice)
        FROM products AS p2
        WHERE p2.productLine = products.productLine
    )
)  

SELECT *
FROM cte_max
JOIN cte_min 
ON cte_max.productLine = cte_min.productLine;



-- ---------------- first try ------------------

with cte_max as (
  select productLine, 
  		 productcode as mostExpensiveProductCode, 
         productname as mostExpensiveProductName, 
         buyprice as mostExpensiveBuyPrice -- did not received the max func correctly
  from products
  GROUP BY productLine
  WHERE buyprice = MAX(buyprice)
), cte_min as (
  select productLine, 
  		 productcode as leastExpensiveProductCode, 
         productname as leastExpensiveProductName, 
         buyprice as leastExpensiveBuyPrice
  from products
  GROUP BY productLine
  WHERE buyprice = MIN(buyprice)
)  

select *
from cte_max
-- JOIN cte_min
-- On cte_max.productLine = cte_min.productLine;
-- from products
-- Where productline = 'Ships';
