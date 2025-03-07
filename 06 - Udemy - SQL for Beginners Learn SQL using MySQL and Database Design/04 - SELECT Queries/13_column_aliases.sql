USE coffee_store;

SELECT DISTINCT last_name FROM customers
ORDER BY last_name;

SELECT * FROM orders
WHERE order_time BETWEEN '2023-02-01' AND '2023-02-28 23:59:59.999999'
AND product_id = 3
ORDER BY order_time
LIMIT 4;

SELECT name, price AS retail_price, coffee_origin FROM products;