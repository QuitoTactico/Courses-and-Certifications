USE test;
 
-- How to add a unique constraint to a column
 
ALTER TABLE <table name>
ADD CONSTRAINT <constraint name> UNIQUE (<column name>);
 
-- How to remove a unique constraint from a column
 
ALTER TABLE <table name>
DROP INDEX <constraint name>;
 
DESCRIBE pets;

ALTER TABLE pets
ADD CONSTRAINT u_species UNIQUE (species);

ALTER TABLE pets
DROP INDEX u_species;













