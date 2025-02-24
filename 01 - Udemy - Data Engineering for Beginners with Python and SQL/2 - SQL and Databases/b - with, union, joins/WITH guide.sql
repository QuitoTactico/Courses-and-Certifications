WITH cte_name (column1, column2, ...) AS (
  -- CTE query definition here
)
-- Main query that references the CTE
SELECT ...
FROM ...
WHERE ...;

/*
Las columnas son nombres opcionales para las columnas que salngan de la subquery guardada

Se pueden hacer queries recursivas con esto, para bases de datos jerárquicas

example:*/

WITH RecursiveManagerCTE AS (
  SELECT employee_id, first_name, last_name, manager_id, salary
  FROM employees
  WHERE manager_id IS NULL -- Find top-level managers

  UNION ALL

  SELECT e.employee_id, e.first_name, e.last_name, e.manager_id, e.salary
  FROM employees e

  JOIN RecursiveManagerCTE r ON e.manager_id = r.employee_id
)
 
SELECT manager_id, SUM(salary) AS total_salary_cost
FROM RecursiveManagerCTE
GROUP BY manager_id;