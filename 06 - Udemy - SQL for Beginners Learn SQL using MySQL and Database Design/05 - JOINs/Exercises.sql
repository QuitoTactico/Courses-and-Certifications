USE coffee_store;
 
-- 1. Select the order ID and customer's phone number for all orders of product ID 4.
 SELECT o.id, c.phone_number FROM orders o
 JOIN customers c ON o.customer_id = c.id
 WHERE o.product_id = 4;
 
-- 2. Select the product name and order time, for filter coffees sold between
--    January 1st 2023 and March 31st 2023.
 SELECT p.name, o.order_time FROM products p
 JOIN orders o ON p.id = o.product_id
 WHERE p.name = 'Filter'
 AND o.order_time BETWEEN '2023-01-01' AND '2023-03-31 23:59:59.999999';
 
-- 3. Select the product name, price and order time for all orders from females,
--    in January 2023.
SELECT p.name, p.price, o.order_time FROM products p
JOIN orders o ON p.id = o.product_id
JOIN customers c ON o.customer_id = c.id
WHERE c.gender = 'F'
AND o.order_time BETWEEN '2023-01-01' AND '2023-01-31 23:59:59.999999';