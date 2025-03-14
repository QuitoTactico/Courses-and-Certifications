-- Employee Reporting Structure

-- Display a report showing the hierarchical structure of employees, 
-- including their names and the names of their immediate supervisors.

select employee.employeenumber, 
       employee.lastname as employeeLastName, 
       employee.firstname as employeeFirstName,
       supervisor.employeenumber as supervisorNumber,
       supervisor.lastname as supervisorLastName, 
       supervisor.firstname as supervisorFirstName
from employees employee
join employees supervisor
on employee.reportsTo = supervisor.employeeNumber;