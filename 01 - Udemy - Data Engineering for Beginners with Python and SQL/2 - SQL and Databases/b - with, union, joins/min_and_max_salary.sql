-- not useful beta, ultra basura

with cte (cte_department, cte_max_salary, cte_min_salary) as (

    select department, max(salary), min(salary)
    from employees
    group by department
)


select
department as 'Department', 
CONCAT(first_name, ' ', last_name) as 'Highest Earner', 
salary as 'Highest Salary' | Lowest Earner      | Lowest Salary
from employees
where 
order by department asc


-- final ver

WITH cbt_max ('Department', 'Highest Earner', 'Highest Salary') AS (

    select
    department, 
    first_name || ' ' || last_name as maximum, 
    max(salary) -- esto se lleva a todos los demás

    from employees
    group by department
), cbt_min ('Department', 'Lowest Earner', 'Lowest Salary') AS (

    select
    department, 
    first_name || ' ' || last_name as minimum, 
    min(salary) -- queda la fila de donde resulte esto como ganador

    from employees
    group by department
)

select *
from cbt_max join cbt_min on cbt_max.department = cbt_min.department
order by department asc


-- la que me dió chatgpt innecesariamente más complicada, idk why
-- update: ya sé why. gracias por la herramienta nueva, se pueden hacer mejores cosas con ella.

WITH cbt_max AS (
    SELECT 
        department, 
        first_name || ' ' || last_name AS "Highest Earner", 
        salary AS "Highest Salary"
    FROM employees
    WHERE (department, salary) IN (
        SELECT department, MAX(salary)
        FROM employees
        GROUP BY department
    )
),
cbt_min AS (
    SELECT 
        department, 
        first_name || ' ' || last_name AS "Lowest Earner", 
        salary AS "Lowest Salary"
    FROM employees
    WHERE (department, salary) IN (
        SELECT department, MIN(salary)
        FROM employees
        GROUP BY department
    )
)

SELECT *
FROM cbt_max
JOIN cbt_min ON cbt_max.department = cbt_min.department
ORDER BY cbt_max.department ASC;


-- solución del curso:

-- Solution
-- Write your SQL query here to find the highest and lowest salaries by department
WITH HighestSalaries AS (
    SELECT
        department AS "Department",
        first_name || ' ' || last_name AS "Highest Earner",
        MAX(salary) AS "Highest Salary"
    FROM
        employees
    GROUP BY
        department
),
LowestSalaries AS (
    SELECT
        department AS "Department",
        first_name || ' ' || last_name AS "Lowest Earner",
        MIN(salary) AS "Lowest Salary"
    FROM
        employees
    GROUP BY
        department
)
SELECT
    H.Department,
    H."Highest Earner",
    H."Highest Salary",
    L."Lowest Earner",
    L."Lowest Salary"
FROM
    HighestSalaries H
JOIN
    LowestSalaries L
ON
    H.Department = L.Department
ORDER BY
    H.Department ASC;