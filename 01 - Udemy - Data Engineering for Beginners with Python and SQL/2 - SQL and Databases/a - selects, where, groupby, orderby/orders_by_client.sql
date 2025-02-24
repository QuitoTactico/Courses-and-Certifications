select client_id, count(*) as orders, avg(order_amount) as avg_order
from orders
group by client_id

/*You have orders table with columns order_id, client_id, order_amount . Output the average order amount and the average order count for each client.*/