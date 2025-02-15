with cte_min as (

    select product_name, inventory_level
    from products
    order by inventory_level asc
    limit 5

), cte_max as (

    select product_name, inventory_level
    from products
    order by inventory_level desc
    limit 5
)


select product_name as 'Product Name', inventory_level as 'Inventory Level'
from cte_max

UNION ALL

select product_name as 'Product Name', inventory_level as 'Inventory Level'
from cte_min

order by inventory_level desc


-- solución del curso

-- este man le hizo matryoshka al select final para dejarlo en un solo select al que sí le puede hacer orderby fácil, hmm. Y no le gusta usar los nombres paréntesis antes del AS

-- Solution
-- Write your SQL query here to find the products with the highest and lowest inventory levels
WITH highest as (
SELECT
    product_name AS "Product Name",
    inventory_level AS "Inventory Level"
FROM
    products
ORDER BY
    inventory_level DESC
LIMIT 5
 
), lowest as (
 
SELECT
    product_name AS "Product Name",
    inventory_level AS "Inventory Level"
FROM
    products
ORDER BY
    inventory_level ASC
LIMIT 5
)
SELECT *
FROM (
SELECT * FROM highest
UNION ALL
SELECT * FROM lowest
) ORDER BY `Inventory Level` DESC