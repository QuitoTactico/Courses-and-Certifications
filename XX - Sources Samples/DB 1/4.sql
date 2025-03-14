-- List All Products and Their Corresponding Order Status

-- Compile a comprehensive list of all products with their names 
-- and corresponding status from orders where they were included.

SELECT products.productcode, products.productname, 
	   orders.orderNumber, orders.status
from products
JOIN 
(
  orderdetails
  JOIN orders
  on orderdetails.orderNumber = orders.orderNumber
)
ON products.productCode = orderdetails.productCode;