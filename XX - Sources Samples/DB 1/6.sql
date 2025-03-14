-- Customers with Orders Exceeding a Specific Amount

-- Identify customers whose cumulative order values 
-- exceed $10,000 to highlight top spenders.

with cte_total_per_customer as (
  select customernumber, sum(amount) as amountPerCustomer
  from payments
  group by customerNumber
)

select customers.customernumber, customername, amountPerCustomer
from cte_total_per_customer
JOIN customers
on cte_total_per_customer.customernumber = customers.customernumber
where amountPerCustomer >= 10000
order by amountPerCustomer desc