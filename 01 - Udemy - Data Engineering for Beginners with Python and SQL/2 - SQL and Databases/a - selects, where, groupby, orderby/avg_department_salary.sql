SELECT department as Department, avg(salary) as 'Average Salary'
FROM employees
GROUP BY department
ORDER BY department asc


/*
Employee Database Query
Aim: Calculate the Average Salary by Department

In this SQL coding exercise, you will work with a database table called employees. Your task is to write a SELECT query to calculate the average salary for each department in the company.

Data Description:

You are provided with a table named employees with the following columns:

employee_id (integer) - Primary Key

first_name (varchar(50))

last_name (varchar(50))

job_title (varchar(100))

department (varchar(50))

hire_date (date)

salary (decimal(10, 2))

Instructions:

Write a SQL SELECT query that retrieves the following information:

Department name

Average salary for employees in that department

Group the results by department name.

Sort the results in ascending order based on the department name.

Department      | Average Salary
--------------------------------
Engineering     | 80000.00
Marketing       | 75000.00
Sales           | 60000.00
...
*/