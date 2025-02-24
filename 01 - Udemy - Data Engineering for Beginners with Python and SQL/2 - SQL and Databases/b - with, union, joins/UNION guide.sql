/*
son para sumar verticalmente los resulados de dos queries con tipos de datos compatibles

busque precio y marca de la tabla zapatos : 20 resultados
busque precio y marca de la tabla camisas : 40 resultados
tabla final:                                56 resultados

... y eso?

mano pues habían filas repetidas!

y entonces?

pues use UNION ALL
*/

SELECT first_name, last_name
FROM employees
UNION                          -- o UNION ALL!
SELECT first_name, last_name
FROM contractors;


-- sólo puede existir un order by, y va después del union. O sea, ordena todo.
-- Si quieres dos órdenes diferentes, te tocará hacer dos CTEs diferentes con sus propios órdenes
-- y no ordenarlos en el union, pegarlos y ya.