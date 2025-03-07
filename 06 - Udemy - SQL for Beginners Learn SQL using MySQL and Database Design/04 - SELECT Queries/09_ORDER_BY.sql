USE coffee_store;

SELECT name, price FROM products
WHERE coffee_origin in ('Colombia', 'Indonesia')
ORDER BY name;

SELECT * FROM products ORDER BY name;

SELECT name, price FROM products
WHERE coffee_origin = 'Colombia' OR coffee_origin = 'Indonesia'
ORDER BY name ASC;

SELECT * FROM orders
WHERE order_time BETWEEN '2023-02-01' AND '2023-02-28 23:59:59.999999'
AND customer_id IN (19, 20, 21, 24);

SELECT * FROM orders
WHERE year(order_time) = 2023 AND month(order_time) = 2
AND customer_id IN (19, 20, 21, 24);

SELECT first_name, last_name, phone_number FROM customers
WHERE last_name LIKE '%ar%';