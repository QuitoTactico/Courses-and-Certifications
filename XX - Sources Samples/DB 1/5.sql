-- Employees and Their Sales (Total Amount From Orders)

-- Summarize the total payments amount for each employee 
-- by evaluating the sum of payments received from customers they oversee.

with cte_total_per_customer as (
  select customernumber, sum(amount) as amountPerCustomer
  from payments
  group by customerNumber
), cte_total_per_employee as (
  select salesrepemployeenumber, sum(amountPerCustomer) as amountPerEmployee
  from cte_total_per_customer 
  join customers
  on cte_total_per_customer.customernumber = customers.customernumber
  group by salesrepemployeenumber
)


select employeeNumber, firstname, lastname, amountPerEmployee
from cte_total_per_employee
join employees
on cte_total_per_employee.salesrepemployeenumber = employees.employeeNumber
  