-- Write your SQL query here to find the top 5 customers by total purchase amount
-- USAR SIEMPRE `<variable>`, aquí tuve suerte por alguna razón
select first_name || ' ' || last_name as 'Customer Name', sum(purchase_amount) as 'Total Purchase Amount'
from customer_purchases
group by customer_id
order by 'Total Purchase Amount' desc
limit 5