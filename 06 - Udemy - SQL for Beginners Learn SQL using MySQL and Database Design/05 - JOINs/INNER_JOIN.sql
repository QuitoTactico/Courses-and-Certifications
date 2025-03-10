USE coffee_store;
 
SELECT * FROM orders;
SELECT * FROM products;

SELECT products.name, orders.order_time FROM orders
INNER JOIN products ON orders.product_id = products.id;

SELECT p.name, o.order_time FROM orders AS o
JOIN products p ON o.product_id = p.id;

SELECT p.name, o.order_time FROM orders AS o
JOIN products p ON o.product_id = p.id
WHERE o.product_id = 5
ORDER BY o.order_time;

-- Inner join syntax
SELECT <table name>.<column name>, ... FROM <table 1>
JOIN <table 2> ON <table 1>.<column name> = <table 2>.<column name>
WHERE clause, if needed
ORDER BY clause, if needed;