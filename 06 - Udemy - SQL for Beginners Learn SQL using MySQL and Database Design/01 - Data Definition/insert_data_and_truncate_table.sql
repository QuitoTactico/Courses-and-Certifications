-- HOW TO DELETE TABLES FROM A DATABASE
 
CREATE DATABASE example;
 
USE example;
 
CREATE TABLE test (
id INT auto_increment PRIMARY KEY,
name VARCHAR(30),
age INT
);
 
DESCRIBE test;
SHOW TABLES;

DROP TABLE test;

INSERT INTO test (name, age) VALUES('Ben', 19), ('Simon', 28), ('Claire', 23);
SELECT * FROM test;

TRUNCATE TABLE test;






