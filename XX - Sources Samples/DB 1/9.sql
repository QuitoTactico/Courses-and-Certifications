-- Rank Customers by Latest Payment Date

-- Rank customers by the recency of their last payment, 
-- with the most recent payments receiving the highest rank.

-- this will rank while mantaining the granularity of the data
with cte_last_payment as (
  select customerNumber,
  		 max(paymentdate) as lastPayment
  from payments
  group by customerNumber
)

select payments.customerNumber,
       paymentdate,
       lastPayment,
       RANK() OVER (ORDER BY lastPayment DESC) AS rank,
       DENSE_RANK() OVER (ORDER BY lastPayment DESC) AS denseRank
from payments
JOIN cte_last_payment
on payments.customerNumber = cte_last_payment.customerNumber
order by rank;

-- this will "rank the customers" while agrouping their rows
with cte_last_payment as (
  select customerNumber,
  		 max(paymentdate) as lastPayment
  from payments
  group by customerNumber
)

select payments.customerNumber,
       paymentdate,
       lastPayment,
       RANK() OVER (ORDER BY lastPayment DESC) AS rank,
       DENSE_RANK() OVER (ORDER BY lastPayment DESC) AS denseRank
from payments
JOIN cte_last_payment
on payments.customerNumber = cte_last_payment.customerNumber
GROUP by payments.customernumber
order by rank;