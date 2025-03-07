USE test;
 
-- How to change a column's data type
 
ALTER TABLE <table name>
CHANGE COLUMN <current column name> <new column name> <data type>;
 
ALTER TABLE <table name>
MODIFY COLUMN <column name> <data type>;
 
DESCRIBE addresses;

ALTER TABLE addresses
CHANGE COLUMN city city VARCHAR(30);

ALTER TABLE addresses
MODIFY COLUMN city CHAR(25);

ALTER TABLE addresses
MODIFY COLUMN city int;












