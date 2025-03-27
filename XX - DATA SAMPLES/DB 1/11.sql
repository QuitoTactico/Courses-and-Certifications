-- Hierarchy of Employees up to the Top

-- Construct an organizational chart that visualizes the 
-- reporting lines of employees, from each individual up 
-- to their top-level manager.

WITH RECURSIVE cte_employee_hierarchy AS (
    SELECT employeeNumber,
           lastName AS employeeLastName,
           firstName AS employeeFirstName,
           reportsTo,
           0 AS supervisorlevel  -- initial level
    FROM employees
    WHERE reportsTo IS NULL  -- TOP supervisor

    UNION ALL

    SELECT employee.employeeNumber,
           employee.lastName AS employeeLastName,
           employee.firstName AS employeeFirstName,
           employee.reportsTo,
           supervisor.supervisorlevel + 1 AS supervisorlevel
    FROM employees employee
    INNER JOIN cte_employee_hierarchy supervisor 
    ON employee.reportsTo = supervisor.employeeNumber
)

SELECT employee.employeeNumber,
       employee.employeeLastName,
       employee.employeeFirstName,
       supervisor.employeeNumber AS supervisorNumber,
       supervisor.lastName AS supervisorLastName,
       supervisor.firstName AS supervisorFirstName,
       employee.supervisorlevel
FROM cte_employee_hierarchy employee
LEFT JOIN employees supervisor 
ON employee.reportsTo = supervisor.employeeNumber
ORDER BY employee.supervisorlevel, employee.employeeNumber;