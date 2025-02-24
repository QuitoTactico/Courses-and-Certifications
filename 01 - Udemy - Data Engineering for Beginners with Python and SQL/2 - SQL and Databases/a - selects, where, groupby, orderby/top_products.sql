-- sí, usar `nombre` si vas a usar esa columna para algo luego, como ordenar. o no da, trust me
SELECT product_name AS `Product Name`, COUNT(*) AS `Order Count`
FROM orders
GROUP BY product_name
ORDER BY 'Order Count' DESC
LIMIT 10;