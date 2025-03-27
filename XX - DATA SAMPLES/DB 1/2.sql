-- Average Buy Price by Product Scale

-- Calculate the average buy price of products grouped by their 
-- scale to understand pricing strategies for different model scales.

select productscale, AVG(buyprice) as averageBuyPrice
from products
GROUP BY productscale;