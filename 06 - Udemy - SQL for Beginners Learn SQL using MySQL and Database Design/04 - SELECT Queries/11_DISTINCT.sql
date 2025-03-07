USE coffee_store;
 
SELECT * FROM customers;

SELECT * FROM customers
LIMIT 5;

SELECT * FROM customers
LIMIT 5 OFFSET 5;

SELECT * FROM customers
-- LIMIT 12, 3;
LIMIT 3 OFFSET 12;

SELECT * FROM customers
LIMIT `row_count`;  -- only return row-count rows.

SELECT * FROM customers
LIMIT `offset`, `row_count`;  -- return row_count rows, starting from row 5.

SELECT * FROM customers
LIMIT `row_count` OFFSET `offset`;  -- same as above.

SELECT * FROM customers
LIMIT 10 OFFSET 5;

SELECT * FROM customers
ORDER BY last_name
LIMIT 10;