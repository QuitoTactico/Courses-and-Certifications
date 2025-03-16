-- Running Total of Payments by Customers

-- For each customer, compute a running total of 
-- the payments they have made over time, displaying 
-- each payment with its cumulative total.

select customerNumber,
       paymentdate,
       SUM(amount) OVER (PARTITION BY customerNumber ORDER BY paymentdate asc) as runningTotal
from payments
order by customernumber asc, paymentdate asc