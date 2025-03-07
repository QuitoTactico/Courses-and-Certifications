USE example;

CREATE TABLE people (
  id INT auto_increment PRIMARY KEY,
  name VARCHAR(30),
  age INT,
  gender ENUM('F', 'M')
);

INSERT INTO people
(name, age, gender)
VALUES ('Emma', 21, 'F'), ('John', 30, 'M'), ('Thomas', 27, 'M'),
('Chris', 44, 'M'), ('Sally', 23, 'F'), ('Frank', 55, 'M');

SELECT * FROM people;
