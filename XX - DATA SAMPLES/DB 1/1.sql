-- Total Stock by Product Line

-- Retrieve the total quantity in stock for each product 
-- line by aggregating the stock quantities of all products within each line.

select productLine, sum(quantityinstock) as totalQuantityInStock
from products
GROUP BY productline;