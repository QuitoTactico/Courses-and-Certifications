USE test;
 
-- How to change a column's name
 
ALTER TABLE <table name>
CHANGE <current column name> <new column name> <data type>;
 
ALTER TABLE <tablename>
RENAME COLUMN <current column name> TO <new column name>;
 
DESCRIBE pets;

ALTER TABLE pets
CHANGE species animal_type VARCHAR(20);

ALTER TABLE pets
RENAME COLUMN animal_type TO species;

ALTER TABLE pets
RENAME COLUMN species TO `animal type`;







