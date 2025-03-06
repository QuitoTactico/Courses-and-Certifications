USE test;
 
-- SQL  to add a primary key to a table.
ALTER TABLE <table name>
ADD PRIMARY KEY (<column name>);
 
-- SQL to remove a primary key from a table.
ALTER TABLE <table name>
DROP PRIMARY KEY;

DESCRIBE addresses;

ALTER TABLE addresses
ADD PRIMARY KEY (id);

ALTER TABLE addresses
DROP PRIMARY KEY;

ALTER TABLE addresses
MODIFY id int;

DESCRIBE people;

ALTER TABLE people
ADD PRIMARY KEY (id);










