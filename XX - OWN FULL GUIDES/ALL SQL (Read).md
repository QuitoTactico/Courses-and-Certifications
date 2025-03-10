# Sources: 

- https://www.udacity.com/course/intro-to-relational-databases--ud197
- https://www.udacity.com/course/sql-for-data-analysis--ud198 (MOSTLY)
- https://globant.udemy.com/course/sql-for-beginners-course/learn/lecture/40417882?learning_path_id=9400125#overview

# SELECT, ORDER, OFFSET

```sql
SELECT first_name, last_name
FROM students
WHERE age > 20 AND last_name LIKE 'S%';
```

También puedes usar `offset` para saltarte algunos de los primeros resultados

Puedes poner comas en el `order by` para tener varios ordenes y subordenes, cada uno puede ser ascendente o descendente

<aside>
💡

Acostumbra a poner los COMANDOS en mayúscula, a poner underscores en_las_columnas, y terminar las sentencias con  ; 

</aside>

# GROUP BY

Se utiliza junto con funciones de agregación para agrupar resultados por una o más columnas.

*Este ejemplo cuenta el número de empleados en cada departamento:*

```sql
SELECT departamento, COUNT(*) AS total_empleados
  FROM empleados
 GROUP BY departamento;
```

Otro ejemplo

```sql
-- Write your SQL query here to find the top 5 customers by total purchase amount
-- USAR SIEMPRE `<variable>`, aquí tuve suerte por alguna razón
select first_name || ' ' || last_name as 'Customer Name', sum(purchase_amount) as 'Total Purchase Amount'
from customer_purchases
group by customer_id
order by 'Total Purchase Amount' desc
limit 5
```

### GROUP BY n

- **Descripción**: `GROUP BY n` es una forma abreviada de referirse a la n-ésima columna en la lista de selección. En lugar de especificar el nombre de la columna, puedes usar el índice de la columna, donde `n` se refiere a la n-ésima columna seleccionada.
- **Uso**: Se utiliza para agrupar resultados basados en la primera columna de la cláusula `SELECT`.
- **Ejemplo**:
    
    ```sql
    SELECT
        department,
        COUNT(*)
    FROM
        employees
    GROUP BY 1;
    
    ```
    
    En este caso, `GROUP BY 1` agrupa los resultados por la columna `department`.
    

## Having

Se utiliza para filtrar los resultados de un `GROUP BY`, permitiendo condiciones en las funciones de agregación.

Es como un WHERE para los grupos.

```sql
SELECT departamento, AVG(salario) AS salario_promedio
  FROM empleados
 GROUP BY departamento
HAVING AVG(salario) > 50000;
```

*Este ejemplo muestra los departamentos donde el salario promedio es mayor a 50,000.*

# Operadores Lógicos

| Statement | How to Use It | Other Details |
| --- | --- | --- |
| SELECT | SELECT Col1, Col2, ... | Provide the columns you want |
| FROM | FROM Table | Provide the table where the columns exist |
| LIMIT | LIMIT 10 | Limits based number of rows returned |
| ORDER BY | ORDER BY Col | Orders table based on the column. Used with DESC. |
| WHERE | WHERE Col > 5 | A conditional statement to filter your results |
| LIKE | WHERE Col LIKE '%me%' | Only pulls rows where column has 'me' within the text |
| IN | WHERE Col IN ('Y', 'N') | A filter for only rows with column of 'Y' or 'N' |
| NOT | WHERE Col NOT IN ('Y', 'N') | NOT is frequently used with LIKE and IN |
| AND | WHERE Col1 > 5 AND Col2 < 3 | Filter rows where two or more conditions must be true |
| OR | WHERE Col1 > 5 OR Col2 < 3 | Filter rows where at least one condition must be true |
| BETWEEN | WHERE Col BETWEEN 3 AND 5 | Often easier syntax than using an AND |

## 1. AND

El operador `AND` se utiliza para combinar condiciones, y todas las condiciones deben ser verdaderas para que la consulta devuelva resultados.

```sql
SELECT *
FROM empleados
WHERE salario > 50000 AND departamento = 'Ventas';

```

*Este ejemplo selecciona todos los empleados que tienen un salario mayor a 50,000 y que pertenecen al departamento de Ventas.*

## 2. OR

El operador `OR` se utiliza para combinar condiciones, y al menos una de las condiciones debe ser verdadera para que la consulta devuelva resultados.

```sql
SELECT *
FROM empleados
WHERE departamento = 'Ventas' OR departamento = 'Marketing';

```

*Este ejemplo selecciona todos los empleados que pertenecen al departamento de Ventas o al departamento de Marketing.*

## 3. NOT

El operador `NOT` se utiliza para negar una condición. Si la condición es verdadera, `NOT` la convierte en falsa y viceversa.

```sql
SELECT *
FROM empleados
WHERE NOT departamento = 'Recursos Humanos';

```

*Este ejemplo selecciona todos los empleados que no pertenecen al departamento de Recursos Humanos.*

## 4. BETWEEN

El operador `BETWEEN` se utiliza para filtrar resultados dentro de un rango específico, incluyendo los límites.

```sql
SELECT *
FROM empleados
WHERE salario BETWEEN 30000 AND 50000;

```

*Este ejemplo selecciona todos los empleados cuyo salario está entre 30,000 y 50,000, incluyendo ambos valores.*

## 5. LIKE

El operador `LIKE` se utiliza para buscar un patrón específico en una columna de texto. Se puede usar `%` para representar cero o más caracteres y `_` para representar un solo carácter.

```sql
SELECT *
FROM empleados
WHERE nombre LIKE 'A%';

```

*Este ejemplo selecciona todos los empleados cuyos nombres comienzan con la letra "A".*

```sql
SELECT *
FROM empleados
WHERE apellido LIKE '%ez';

```

*Este ejemplo selecciona todos los empleados cuyos apellidos terminan con "ez".*

## 6. IN

El operador `IN` se utiliza para filtrar resultados que coincidan con un conjunto de valores específicos.

```sql
SELECT *
FROM empleados
WHERE departamento IN ('Ventas', 'Marketing', 'IT');

```

*Este ejemplo selecciona todos los empleados que pertenecen a cualquiera de los departamentos: Ventas, Marketing o IT.*

## Combinaciones

- Puedes combinar varios operadores lógicos en una sola consulta.
    
    ```sql
    SELECT *
    FROM empleados
    WHERE (salario > 50000 AND departamento = 'Ventas') OR (salario < 30000 AND departamento = 'Marketing');
    
    ```
    
    *Este ejemplo selecciona todos los empleados que tienen un salario mayor a 50,000 en Ventas, o un salario menor a 30,000 en Marketing.*
    
- Puedes combinar `BETWEEN`, `LIKE` e `IN` con otros operadores lógicos.
    
    ```sql
    SELECT *
    FROM empleados
    WHERE (salario BETWEEN 30000 AND 50000) AND (departamento IN ('Ventas', 'Marketing')) AND (nombre LIKE 'J%');
    
    ```
    
    *Este ejemplo selecciona todos los empleados cuyo salario está entre 30,000 y 50,000, pertenecen a los departamentos de Ventas o Marketing, y sus nombres comienzan con la letra "J".*
    

# CASE (IF): WHEN - THEN - ELSE - END

Hay condicionales para decidir qué poner en el output, sin tener que modificar la db.

Formato: `CASE` -`WHEN` - `THEN` - `ELSE` - `END`

```sql
SELECT 
    id,
    account_id,
    occurred_at,
    channel,
    CASE 
        WHEN channel = 'facebook' OR channel = 'direct' THEN 'yes' 
        ELSE 'no' 
    END AS is_facebook
FROM 
    demo.web_events_full
ORDER BY 
    occurred_at;
```

| **id** | **account_id** | **occurred_at** | **channel** | **is_facebook** |
| --- | --- | --- | --- | --- |
| 1 | 1001 | 2023-10-01 12:30:00 | facebook | yes |
| 2 | 1002 | 2023-10-01 14:45:00 | direct | yes |
| 3 | 1003 | 2023-10-02 09:15:00 | google | no |
| 4 | 1004 | 2023-10-02 11:00:00 | facebook | yes |
| 5 | 1005 | 2023-10-03 08:00:00 | referral | no |
| 6 | 1006 | 2023-10-04 10:00:00 | direct | yes |

# COALESCE

El uso de `COALESCE` en SQL es una función muy útil para manejar valores nulos. Aquí tienes un resumen:

`COALESCE` es una función que evalúa una lista de expresiones y devuelve el primer valor no nulo encontrado. Su sintaxis básica es:

```sql
COALESCE(expr1, expr2, ..., exprN)
```

¿Cuándo usarla?

- **Manejo de Nulos**: Para evitar que los resultados de una consulta contengan valores nulos, puedes proporcionar un valor alternativo.
- **Concatenación de Datos**: Puede ser útil al concatenar columnas donde algunas pueden contener nulos.
- **Reportes y Análisis**: En informes, permite mostrar valores predeterminados en lugar de nulos, mejorando la legibilidad.

Supongamos que tienes una tabla de empleados y quieres mostrar el nombre del empleado, pero si el nombre es nulo, quieres mostrar "No disponible":

```sql
SELECT
    COALESCE(nombre, 'No disponible') AS nombre_empleado
FROM empleados;

```

- **Simplicidad**: Reduce la necesidad de múltiples condiciones `CASE` o `IF`.
- **Eficiencia**: Evalúa las expresiones en orden hasta encontrar la primera no nula, lo que puede ser más eficiente en ciertas situaciones.
- `COALESCE` puede aceptar hasta 255 argumentos, pero si todos son nulos, el resultado será nulo.
- El tipo de datos del resultado es el tipo de datos del primer argumento no nulo.

# Funciones y más funciones!!!!!!!!

## Funciones de Agregación (GROUP BY y Window)

En SQL, las funciones de agregación se utilizan para realizar cálculos en un conjunto de valores y devolver un único valor. Aquí tienes una lista de las funciones de agregación más comunes disponibles en SQL, junto con una breve descripción y ejemplos:

| Función | Descripción |
| --- | --- |
| `COUNT()` | Cuenta el número de filas. |
| `SUM()` | Suma los valores de una columna. |
| `AVG()` | Calcula el promedio de una columna. |
| `MIN()` | Encuentra el valor mínimo. |
| `MAX()` | Encuentra el valor máximo. |
| `GROUP BY` | Agrupa resultados según una o más columnas. |
| `HAVING` | Filtra grupos según condiciones en funciones de agregación. |

### 1. `COUNT()`

Cuenta el número de filas que coinciden con una condición.

```sql
SELECT COUNT(*) AS total_empleados 
  FROM empleados;
```

*Este ejemplo cuenta el total de empleados en la tabla.*

También existe una versión para contar los diferentes valores.

```sql
SELECT COUNT(DISTINCT first_name) AS nombres_diferentes 
  FROM empleados;
```

### 2. `SUM()`

Calcula la suma total de una columna numérica.

```sql
SELECT SUM(salario) AS total_salarios 
  FROM empleados;
```

*Este ejemplo suma todos los salarios de los empleados.*

### 3. `AVG()`

Calcula el promedio de una columna numérica.

```sql
SELECT AVG(salario) AS salario_promedio 
  FROM empleados;
```

*Este ejemplo calcula el salario promedio de los empleados.*

### 4. `MIN()`

Devuelve el valor mínimo de una columna.

```sql
SELECT MIN(salario) AS salario_minimo 
  FROM empleados;
```

*Este ejemplo obtiene el salario más bajo entre los empleados.*

### 5. `MAX()`

Devuelve el valor máximo de una columna.

```sql
SELECT MAX(salario) AS salario_maximo 
  FROM empleados;
```

*Este ejemplo obtiene el salario más alto entre los empleados.*

### **6. `VARIANCE()`**

Calcula la varianza de un conjunto de valores.

### **7. `STDDEV()`**

Calcula la desviación estándar de un conjunto de valores.

## Funciones de Ranking (GROUP BY y Window)

### 1. `NTILE()`

**NTILE(n)**: Divide el conjunto de resultados en `n` grupos (o "tiles") de tamaño aproximadamente igual y asigna un número de grupo a cada fila, basado en el orden especificado. Se utiliza para clasificar datos en cuartiles, quintiles, percentiles, etc.

La columna que se ponga en ORDER BY indica según qué se asignarán esos tiles. En este caso:

- Los valores más altos de `standard_qty` (300, 250) están en los cuartiles y quintiles más altos.
- Los valores más bajos (40, 60, 80) están en los cuartiles y quintiles más bajos.

```sql
SELECT 
    id,
    account_id,
    occurred_at,
    standard_qty,
    NTILE(4) OVER (ORDER BY standard_qty) AS quartile,
    NTILE(5) OVER (ORDER BY standard_qty) AS quintile,
    NTILE(100) OVER (ORDER BY standard_qty) AS percentile
FROM demo.orders
ORDER BY standard_qty DESC
```

| id | account_id | occurred_at | standard_qty | quartile | quintile | percentile |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 100 | 2023-01-01 10:00:00 | 300 | 4 | 5 | 100 |
| 2 | 200 | 2023-01-02 11:00:00 | 250 | 4 | 5 | 90 |
| 3 | 300 | 2023-01-03 12:00:00 | 200 | 3 | 4 | 80 |
| 4 | 400 | 2023-01-04 13:00:00 | 180 | 3 | 4 | 70 |
| 5 | 500 | 2023-01-05 14:00:00 | 150 | 2 | 3 | 60 |
| 6 | 600 | 2023-01-06 15:00:00 | 120 | 2 | 3 | 50 |
| 7 | 700 | 2023-01-07 16:00:00 | 100 | 1 | 2 | 40 |
| 8 | 800 | 2023-01-08 17:00:00 | 80 | 1 | 2 | 30 |
| 9 | 900 | 2023-01-09 18:00:00 | 60 | 1 | 1 | 20 |
| 10 | 1000 | 2023-01-10 19:00:00 | 40 | 1 | 1 | 10 |
- **standard_qty**: Valores aleatorios donde los más altos están en los percentiles, cuartiles y quintiles más altos.
- **quartile**: Indica en qué cuartil se encuentra cada fila (1 a 4), donde 4 es el cuartil más alto.
- **quintile**: Indica en qué quintil se encuentra cada fila (1 a 5), donde 5 es el quintil más alto.
- **percentile**: Indica en qué percentil se encuentra cada fila (1 a 100), donde 100 es el percentil más alto.

### 2. `ROW_NUMBER()`

 Asigna un número único a cada fila dentro de una partición de un conjunto de resultados. Este número es secuencial y no tiene en cuenta duplicados.

`ROW_NUMBER` asigna un número único y secuencial a cada fila dentro de una partición de un conjunto de resultados. No considera duplicados.

**Ejemplo de Código**:

```sql
SELECT
    id,
    account_id,
    DATE_TRUNC('month', occurred_at) AS month,
    ROW_NUMBER() OVER (PARTITION BY account_id ORDER BY DATE_TRUNC('month', occurred_at)) AS row_num
FROM demo.orders

```

- **PARTITION BY**: Divide los resultados por `account_id`.
- **ORDER BY**: Ordena las filas dentro de cada partición por el mes truncado de `occurred_at`.
- **Resultado**: Cada fila recibe un número único, incluso si hay filas con el mismo mes.

**Tabla de Respuesta Ejemplo**:

| id | account_id | month | row_num |
| --- | --- | --- | --- |
| 1 | 100 | 2023-01-01 | 1 |
| 2 | 100 | 2023-01-15 | 2 |
| 3 | 200 | 2023-01-05 | 1 |
| 4 | 200 | 2023-02-01 | 2 |
| 5 | 200 | 2023-02-15 | 3 |

### 3. `RANK()`

Similar a `ROW_NUMBER`, pero asigna el mismo número a filas con valores iguales en la columna especificada. Si hay duplicados, el siguiente número asignado saltará el número de duplicados (el siguiente rango se ajusta en consecuencia).

`RANK` también asigna un número a cada fila, pero si hay filas con valores iguales en la columna especificada, recibirán el mismo rango. El siguiente número asignado saltará el número de duplicados.

**Ejemplo de Código**:

```sql
SELECT
    id,
    account_id,
    DATE_TRUNC('month', occurred_at) AS month,
    RANK() OVER (PARTITION BY account_id ORDER BY DATE_TRUNC('month', occurred_at)) AS rank_num
FROM demo.orders

```

- **PARTITION BY**: Divide los resultados por `account_id`.
- **ORDER BY**: Ordena las filas por el mes truncado de `occurred_at`.
- **Resultado**: Las filas con el mismo mes recibirán el mismo rango, y el siguiente rango saltará el número de duplicados.

**Tabla de Respuesta Ejemplo**:

| id | account_id | month | rank_num |
| --- | --- | --- | --- |
| 1 | 100 | 2023-01-01 | 1 |
| 2 | 100 | 2023-01-15 | 2 |
| 3 | 200 | 2023-01-05 | 1 |
| 4 | 200 | 2023-01-05 | 1 |
| 5 | 200 | 2023-02-01 | 3 |

### 4. `DENSE_RANK()`

También asigna el mismo número a filas con valores iguales, pero no deja huecos en la numeración. El siguiente número asignado será el siguiente en secuencia.

`DENSE_RANK` es similar a `RANK`, pero no deja huecos en la numeración. Si hay duplicados, el siguiente número asignado será el siguiente en secuencia.

**Ejemplo de Código**:

```sql
SELECT
    id,
    account_id,
    DATE_TRUNC('month', occurred_at) AS month,
    DENSE_RANK() OVER (PARTITION BY account_id ORDER BY DATE_TRUNC('month', occurred_at)) AS dense_rank_num
FROM demo.orders

```

- **PARTITION BY**: Divide los resultados por `account_id`.
- **ORDER BY**: Ordena las filas por el mes truncado de `occurred_at`.
- **Resultado**: Las filas con el mismo mes recibirán el mismo rango, y el siguiente rango será el siguiente número en secuencia.

**Tabla de Respuesta Ejemplo**:

| id | account_id | month | dense_rank_num |
| --- | --- | --- | --- |
| 1 | 100 | 2023-01-01 | 1 |
| 2 | 100 | 2023-01-15 | 2 |
| 3 | 200 | 2023-01-05 | 1 |
| 4 | 200 | 2023-01-05 | 1 |
| 5 | 200 | 2023-02-01 | 2 |

### 5. `PERCENT_RANK()`

Calcula el porcentaje de un rango en relación al número total de filas.

### **6. `CUME_DIST()`**

Calcula la distribución acumulativa de un valor en relación con el conjunto de datos.

## Funciones de Valor (GROUP BY y Window)

### 1. `LAG() y LEAD()`

- **LAG()**: Devuelve el valor de una fila anterior en el conjunto de resultados, permitiendo comparar con la fila actual.
- **LEAD()**: Devuelve el valor de una fila siguiente en el conjunto de resultados, permitiendo comparar con la fila actual.

```sql
SELECT
    account_id,
    standard_sum,
    LAG(standard_sum) OVER (ORDER BY standard_sum) AS lag,
    LEAD(standard_sum) OVER (ORDER BY standard_sum) AS lead,
    standard_sum - LAG(standard_sum) OVER (ORDER BY standard_sum) AS lag_difference,
    LEAD(standard_sum) OVER (ORDER BY standard_sum) - standard_sum AS lead_difference
FROM (
    SELECT
        account_id,
        SUM(standard_qty) AS standard_sum
    FROM demo.orders
    GROUP BY account_id
) sub
```

| account_id | standard_sum | lag | lead | lag_difference | lead_difference |
| --- | --- | --- | --- | --- | --- |
| 1901 | 0 | NULL | 79 | NULL | 79 |
| 3371 | 79 | 0 | 102 | 79 | 23 |
| 1961 | 102 | 79 | 116 | 23 | 14 |
| 3401 | 116 | 102 | 117 | 14 | 1 |
| 3741 | 117 | 116 | 123 | 1 | 6 |
| 4321 | 123 | 117 | 149 | 6 | 26 |
| 1671 | 149 | 123 | 167 | 26 | 18 |
| 3521 | 167 | 149 | NULL | 18 | NULL |
- **account_id**: Identificador de la cuenta.
- **standard_sum**: Suma de `standard_qty` para cada `account_id`.
- **lag**: Valor de `standard_sum` de la fila anterior.
- **lead**: Valor de `standard_sum` de la siguiente fila.
- **lag_difference**: Diferencia entre `standard_sum` y el valor de la fila anterior.
- **lead_difference**: Diferencia entre el valor de la siguiente fila y `standard_sum`.

### **2. `FIRST_VALUE() y LAST_VALUE()`**

Devuelven el primer y el último valor en un conjunto de filas respectivamente.

### **3. `NTH_VALUE()`**

Devuelve el n-ésimo valor en un conjunto de filas.

### **4. `CYCLE()`**

Permite crear un ciclo en las filas, repitiendo valores cuando se alcanza el final de la partición.

## Funciones de Texto (TEXT funcs)

### **1. `LENGTH`**

- **Descripción**: Devuelve la longitud de una cadena.
- **Ejemplo**: `LENGTH('Hola')` devuelve `4`.

### **2. `LEFT`**

- **Descripción**: Devuelve un número específico de caracteres desde el inicio de una cadena.
- **Ejemplo**: `LEFT('Hola Mundo', 4)` devuelve `'Hola'`.

### **3. `RIGHT`**

- **Descripción**: Devuelve un número específico de caracteres desde el final de una cadena.
- **Ejemplo**: `RIGHT('Hola Mundo', 5)` devuelve `'Mundo'`.

### **4. `SUBSTRING` o `SUBSTR`**

- **Descripción**: Devuelve una parte de una cadena, comenzando en una posición específica.
- **Ejemplo**: `SUBSTRING('Hola Mundo', 1, 4)` devuelve `'Hola'`.

### **5. `UPPER`**

- **Descripción**: Convierte una cadena a mayúsculas.
- **Ejemplo**: `UPPER('Hola')` devuelve `'HOLA'`.

### **6. `LOWER`**

- **Descripción**: Convierte una cadena a minúsculas.
- **Ejemplo**: `LOWER('Hola')` devuelve `'hola'`.

### **7. `TRIM`**

- **Descripción**: Elimina espacios en blanco al principio y al final de una cadena.
- **Ejemplo**: `TRIM(' Hola ')` devuelve `'Hola'`.

### **8. `CONCAT`**

- **Descripción**: Une dos o más cadenas en una sola.
- **Ejemplo**: `CONCAT('Hola', ' ', 'Mundo')` devuelve `'Hola Mundo'`.

### **9. `REPLACE`**

- **Descripción**: Reemplaza todas las ocurrencias de una subcadena en una cadena por otra subcadena.
- **Ejemplo**: `REPLACE('Hola Mundo', 'Mundo', 'SQL')` devuelve `'Hola SQL'`.

### **10. `POSITION` o `CHARINDEX`**

- **Descripción**: Devuelve la posición de la primera ocurrencia de una subcadena en una cadena.
- **Ejemplo**: `POSITION('Mundo' IN 'Hola Mundo')` devuelve `6`.

### **11. `CHAR_LENGTH` o `CHARACTER_LENGTH`**

- **Descripción**: Devuelve la longitud de una cadena en caracteres.
- **Ejemplo**: `CHAR_LENGTH('Hola Mundo')` devuelve `10`.

### **12. `FORMAT`**

- **Descripción**: Formatea una cadena según un formato específico (varía según el SGBD).
- **Ejemplo**: `FORMAT(12345.6789, 'N2')` devuelve `'12,345.68'`.

### **13. `REVERSE`**

- **Descripción**: Invierte el orden de los caracteres en una cadena.
- **Ejemplo**: `REVERSE('Hola')` devuelve `'aloH'`.

## Funciones de Fecha (DATE funcs)

Las funciones de fecha en SQL se utilizan para manipular y extraer información de valores de fecha y hora. Aquí te presento algunas de las más comunes:

### 1. **`DATE_TRUNC`**

- **Descripción**: `DATE_TRUNC` se utiliza para truncar (eliminar) la parte menos significativa de una fecha, redondeándola a una unidad de tiempo específica (como año, mes, día, etc.).
- **Sintaxis:**
    
    ```sql
    DATE_TRUNC('unidad', fecha)
    ```
    
- **Unidad:** Puede ser `'year'`, `'month'`, `'day'`, etc.
    - **`'microseconds'`**
    - **`'milliseconds'`**
    - **`'seconds'`**
    - **`'minute'`**
    - **`'hour'`**
    - **`'day'`**
    - **`'week'`**
    - **`'month'`**
    - **`'quarter'`**
    - **`'year'`**
    - **`'decade'`**
    - **`'century'`**
    - **`'millennium'`**
- **Fecha**: La fecha que deseas truncar.
- **Ejemplo**:
    
    ```sql
    SELECT 
        DATE_TRUNC('day', occurred_at) AS day,
        SUM(standard_qty) AS standard_qty_sum
    FROM 
        demo.orders
    GROUP BY 
        DATE_TRUNC('day', occurred_at)
    ORDER BY 
        DATE_TRUNC('day', occurred_at);
    ```
    
    **Resultado**:
    
    | **day** | **standard_qty_sum** |
    | --- | --- |
    | 2023-10-01 00:00:00 | 15 |
    | 2023-10-02 00:00:00 | 20 |
    | 2023-10-03 00:00:00 | 20 |
    | 2023-10-04 00:00:00 | 15 |

### 2. **`DATE_PART`**

- **Descripción**: `DATE_PART` se utiliza para extraer una parte específica de una fecha, como el año, mes, día, hora, etc.
- **Sintaxis**:
    
    ```sql
    DATE_PART('parte', fecha)
    ```
    
- **Parte:** Puede ser `'year'`, `'month'`, `'day'`, `'hour'`, etc.
    - **`'epoch'`** - Devuelve el tiempo en segundos desde el 1 de enero de 1970.
    - **`'year'`** - Extrae el año.
    - **`'month'`** - Extrae el mes (1-12).
    - **`'day'`** - Extrae el día del mes (1-31).
    - **`'hour'`** - Extrae la hora (0-23).
    - **`'minute'`** - Extrae el minuto (0-59).
    - **`'second'`** - Extrae el segundo (0-59).
    - **`'week'`** - Extrae el número de la semana del año.
    - **`'quarter'`** - Extrae el trimestre (1-4).
    - **`'dow'`** - Devuelve el día de la semana (0-6, donde 0 es domingo).
    - **`'doy'`** - Devuelve el día del año (1-365 o 1-366 en años bisiestos).
    - **`'isodow'`** - Devuelve el día de la semana (1-7, donde 1 es lunes).
    - **`'timezone'`** - Devuelve la zona horaria.
- **Fecha**: La fecha de la que se desea extraer la parte.
- **Ejemplo**:
    
    ```sql
    SELECT 
        DATE_PART('dow', occurred_at) AS day_of_week,
        SUM(total)
    FROM 
        demo.orders
    GROUP BY 
        day_of_week
    
    ```
    
    **Resultado**
    
    | **day_of_week** | **total** |
    | --- | --- |
    | 0 | 150 |
    | 1 | 225 |
    | 2 | 200 |
    | 3 | 300 |

### **3. `CURRENT_DATE**`

Devuelve la fecha actual.

```sql
SELECT CURRENT_DATE;
```

### **4. `NOW()`**

Devuelve la fecha y hora actual.

```sql
SELECT NOW();
```

### **5. `DATE_ADD / DATE_SUB`**

Se utilizan para sumar o restar intervalos de tiempo a una fecha (dependiendo del sistema de gestión de bases de datos).

```sql
SELECT DATE_ADD('2023-10-15', INTERVAL '1 day');
```

### **6. `EXTRACT`**

Similar a `DATE_PART`, se utiliza para obtener partes específicas de una fecha.

```sql
SELECT EXTRACT(MONTH FROM '2023-10-15'::date) AS mes;
```

# DISTINCT

- `DISTINCT` es un operador en SQL que se utiliza para eliminar filas duplicadas en los resultados de una consulta.
- **Aplicación**: `DISTINCT` se aplica a todas las columnas que se especifican en la cláusula `SELECT`.
- **Unicidad**: Devuelve filas únicas basadas en la combinación de los valores de todas las columnas seleccionadas.
- **Rendimiento**: En ciertas situaciones, `DISTINCT` puede ser más eficiente que `GROUP BY` si no se requiere agregación.
- **Claridad**: `DISTINCT` es más legible cuando solo se busca eliminar duplicados sin realizar cálculos adicionales.

Supongamos una tabla `ventas`:

| id_transaccion | producto | cantidad | precio | cliente |
| --- | --- | --- | --- | --- |
| 1 | Manzana | 10 | 1.00 | Juan |
| 2 | Plátano | 5 | 0.50 | María |
| 3 | Manzana | 20 | 1.00 | Juan |
| 4 | Naranja | 7 | 0.75 | Pedro |
| 5 | Plátano | 10 | 0.50 | María |
| 6 | Manzana | 15 | 1.00 | Ana |

# Combinaciones, full conversion process

 Así estaban estos datos de fecha

| month | day | year | clicks |
| --- | --- | --- | --- |
| January | 1 | 2014 | 1135 |
| January | 2 | 2014 | 602 |
| January | 3 | 2014 | 3704 |
| January | 4 | 2014 | 8781 |
| January | 5 | 2014 | 1021 |
| January | 6 | 2014 | 1341 |
| January | 7 | 2014 | 3395 |
| January | 8 | 2014 | 2973 |

Se usó esto y…

```sql
SELECT *,
    DATE_PART('month', TO_DATE(month, 'month')) AS clean_month,
    year || '-' || DATE_PART(month, TO_DATE(month, 'month')) AS concatenated_date,
    CAST(year || '-' || DATE_PART(month, TO_DATE(month, 'month')) || '-' || day AS date) AS formatted_date,
    (year || '-' || DATE_PART('month', TO_DATE(month, 'month'))) || '-' || day)::date AS formatted_date_alt
FROM demo.ad_clicks
```

Observa la transformación

| clean_month | concatenated_date | formatted_date | formatted_date_alt |
| --- | --- | --- | --- |
| 1 | 2014-1-1 | 2014-01-01 | 2014-01-01 |
| 1 | 2014-1-2 | 2014-01-02 | 2014-01-02 |
| 1 | 2014-1-3 | 2014-01-03 | 2014-01-03 |
| 1 | 2014-1-4 | 2014-01-04 | 2014-01-04 |
| 1 | 2014-1-5 | 2014-01-05 | 2014-01-05 |
| 1 | 2014-1-6 | 2014-01-06 | 2014-01-06 |
| 1 | 2014-1-7 | 2014-01-07 | 2014-01-07 |
| 1 | 2014-1-8 | 2014-01-08 | 2014-01-08 |

## `DISTINCT` VS `GROUP BY`

```sql
SELECT DISTINCT producto, cliente
FROM ventas;
```

| producto | cliente |
| --- | --- |
| Manzana | Ana |
| Manzana | Juan |
| Naranja | Pedro |
| Plátano | María |

```sql
SELECT producto, cliente
FROM ventas
GROUP BY producto, cliente;
```

| producto | cliente |
| --- | --- |
| Manzana | Ana |
| Manzana | Juan |
| Naranja | Pedro |
| Plátano | María |

- **Similitud**: Ambos pueden utilizarse para obtener filas únicas.
- **Diferencia**:
    - `DISTINCT` se usa para eliminar duplicados sin necesidad de funciones de agregación.
    - `GROUP BY` se utiliza para agrupar filas y puede incluir funciones de agregación (como `SUM`, `AVG`, etc.) en la consulta.

# Subqueries

## In FROM

To find the players whose weight is less than the average.

```python
# en vez de hacer dos consultas
def lightweights(cursor):
	cursor.execute("select avg(weight) as av from players;")
	av = cursor.fetchall()[0][0]  # first column of first (and only) row
	cursor.execute("select name, weight from players where weight < " + str(av))
	return cursor.fetchall()

```

```python
# puedes hacerlo en una sola
def lightweights(cursor):
	cursor.execute("""
		select name, weight
		from players, (select avg(weight) as av from players) as avg_table
		where weight < avg_table.av;
		""")
	return cursor.fetchall()
```

```sql
select name, weight
from players, 
		 (select avg(weight) as av from players) as avg_table
where weight < avg_table.av;
```

## In WHERE (and anywhere)

```sql
SELECT *
FROM demo.orders
WHERE DATE_TRUNC('month', occurred_at) = 
    (SELECT DATE_TRUNC('month', MIN(occurred_at)) AS min_month
     FROM demo.orders)
ORDER BY occurred_at;
```

## WITH (CTEs)

```sql
WITH cte_name (column1, column2, ...) AS (
  -- CTE query definition here
)
-- Main query that references the CTE
SELECT ...
FROM ...
WHERE ...;
```

<aside>
💡

Las columnas son nombres opcionales para las columnas que salgan de la subquery guardada btw

</aside>

Para definir varias, es así:

```sql
WITH table1 AS (
          SELECT *
          FROM web_events),

     table2 AS (
          SELECT *
          FROM accounts)

SELECT *
FROM table1
JOIN table2
ON table1.account_id = table2.id;
```

### WITH (CTEs): Recursivas

Para bases de datos jerárquicas:

```sql
WITH RecursiveManagerCTE AS (
  SELECT employee_id, first_name, last_name, manager_id, salary
  FROM employees
  WHERE manager_id IS NULL -- Find top-level managers

  UNION ALL

  SELECT e.employee_id, e.first_name, e.last_name, e.manager_id, e.salary
  FROM employees e

  JOIN RecursiveManagerCTE r ON e.manager_id = r.employee_id
)
 
SELECT manager_id, SUM(salary) AS total_salary_cost
FROM RecursiveManagerCTE
GROUP BY manager_id;
```

## VIEWS

Esto crea una pseudo-tabla a partir de un resultado en caché. No tiene que ser usada en el mismo archivo que como con los CTEs, sino que queda guardada en la db.

```sql
create view topfive as
select species, count(*) as num
from animals
group by species
order by num desc
limit 5

```

Que puede ser usada así:

```sql
select * from topfive;
```

# UNION

son para sumar verticalmente los resulados de dos queries con tipos de datos compatibles

busque precio y marca de la tabla zapatos : 20 resultados
busque precio y marca de la tabla camisas : 40 resultados
tabla final:                                56 resultados

... y eso?

mano pues habían filas repetidas!

y entonces?

pues use UNION ALL

```sql
SELECT first_name, last_name
FROM employees
UNION                          -- o UNION ALL!
SELECT first_name, last_name
FROM contractors;
```

<aside>
💡

Sólo puede existir un order by, y va después del union. O sea, ordena todo.

Si quieres dos órdenes diferentes, te tocará hacer dos CTEs diferentes con sus propios órdenes y no ordenarlos en el union, pegarlos y ya.

</aside>

# JOIN

Los "joins" en SQL se utilizan para combinar filas de dos o más tablas basadas en una relación entre ellas. A continuación, se presenta un resumen de los tipos más comunes de joins, junto con ejemplos ilustrativos.

| Tipo de Join | Resultados |
| --- | --- |
| **INNER JOIN** | Solo filas con coincidencias en ambas tablas. |
| **LEFT JOIN** | Todas las filas de la tabla izquierda + coincidencias de la derecha. |
| **RIGHT JOIN** | Todas las filas de la tabla derecha + coincidencias de la izquierda. |
| **FULL JOIN** | Todas las filas de ambas tablas, con NULL donde no hay coincidencia. |
| **CROSS JOIN** | Producto cartesiano de ambas tablas. |

Los joins son fundamentales en SQL para trabajar con múltiples tablas y extraer información relevante según las relaciones entre ellas. Cada tipo de join tiene su uso específico dependiendo de los requerimientos de la consulta.

## Consejos antes de todo

- NO es bueno usar WHERE después de un Join, porque recorres la pendejada dos veces. Es mejor agregar esa condición con un AND en el mismo JOIN. Que haga parte de la condición del JOIN, Una sola pasada.
    
    ```sql
     SELECT orders.*, 
    	 	    accounts.*,
    	 FROM demo.orders
    	 LEFT JOIN demo.accounts
    		 ON orders.account_id = accounts.id
    --WHERE accounts.sales_rep_id = 321500
    		AND accounts.sales_rep_id = 321500
    ```
    
- Los JOIN son la cosa más horrible, dicen que son lo que más se puede simplificar usando WHEREs.
- No tienen que usar una relación de igualdad necesariamente, pueden usar cualquier comparación. Por ejemplo esta:
    
    ```sql
    SELECT accounts.name as account_name,
           accounts.primary_poc as poc_name,
           sales_reps.name as sales_rep_name
      FROM accounts
      LEFT JOIN sales_reps
        ON accounts.sales_rep_id = sales_reps.id
       AND accounts.primary_poc < sales_reps.name
    ```
    

## **1. INNER JOIN**

- Devuelve solo las filas que tienen coincidencias en ambas tablas.

**Ejemplo:**

```sql
SELECT A.Nombre, B.Pedido
FROM Clientes A
INNER JOIN Pedidos B ON A.ID_Cliente = B.ID_Cliente;

```

**Tablas:**

- **Clientes**
    
    
    | ID_Cliente | Nombre |
    | --- | --- |
    | 1 | Juan |
    | 2 | Maria |
    | 3 | Pedro |
- **Pedidos**
    
    
    | ID_Pedido | ID_Cliente | Pedido |
    | --- | --- | --- |
    | 101 | 1 | Televisor |
    | 102 | 2 | Computadora |
    | 103 | 4 | Smartphone |

**Resultado:**

| Nombre | Pedido |
| --- | --- |
| Juan | Televisor |
| Maria | Computadora |

## **2. LEFT JOIN (o LEFT OUTER JOIN)**

- Devuelve todas las filas de la tabla izquierda y las filas coincidentes de la tabla derecha. Si no hay coincidencia, devuelve NULL en el lado derecho.

**Ejemplo:**

```sql
SELECT A.Nombre, B.Pedido
FROM Clientes A
LEFT JOIN Pedidos B ON A.ID_Cliente = B.ID_Cliente;

```

**Resultado:**

| Nombre | Pedido |
| --- | --- |
| Juan | Televisor |
| Maria | Computadora |
| Pedro | NULL |

## **3. RIGHT JOIN (o RIGHT OUTER JOIN)**

- Devuelve todas las filas de la tabla derecha y las filas coincidentes de la tabla izquierda. Si no hay coincidencia, devuelve NULL en el lado izquierdo.

**Ejemplo:**

```sql
SELECT A.Nombre, B.Pedido
FROM Clientes A
RIGHT JOIN Pedidos B ON A.ID_Cliente = B.ID_Cliente;

```

**Resultado:**

| Nombre | Pedido |
| --- | --- |
| Juan | Televisor |
| Maria | Computadora |
| NULL | Smartphone |

## **4. FULL JOIN (o FULL OUTER JOIN)**

- Devuelve todas las filas de ambas tablas, con coincidencias donde existan. Si no hay coincidencias, devuelve NULL en los lugares donde no hay coincidencia.

**Ejemplo:**

```sql
SELECT A.Nombre, B.Pedido
FROM Clientes A
FULL JOIN Pedidos B ON A.ID_Cliente = B.ID_Cliente;

```

**Resultado:**

| Nombre | Pedido |
| --- | --- |
| Juan | Televisor |
| Maria | Computadora |
| Pedro | NULL |
| NULL | Smartphone |

## **5. CROSS JOIN**

- Devuelve el producto cartesiano de ambas tablas, es decir, combina cada fila de la primera tabla con cada fila de la segunda tabla.

**Ejemplo:**

```sql
SELECT A.Nombre, B.Pedido
FROM Clientes A
CROSS JOIN Pedidos B;

```

**Resultado:**

| Nombre | Pedido |
| --- | --- |
| Juan | Televisor |
| Juan | Computadora |
| Juan | Smartphone |
| Maria | Televisor |
| Maria | Computadora |
| Maria | Smartphone |
| Pedro | Televisor |
| Pedro | Computadora |
| Pedro | Smartphone |

## 6. SELF JOIN

- Devuelve una relación de algunas filas de la tabla con otras filas de la misma tabla

**Ejemplo:**

```sql
-- Para ver quiénes son roomies
select a.id, b.id, a.building, a.room
	 from residences as a, residences as b
	 where a.building = b.building
			and a.room = b.room 
			and a.id != b.id
	 order by a.building, a.room;
```

**Resultado:**

| id1 | id2 | building | room |
| --- | --- | --- | --- |
| 413001 | 881256 | Crosby | 10 |
| 881256 | 413001 | Crosby | 10 |
| 496747 | 741532 | Crosby | 19 |
| 741532 | 496747 | Crosby | 19 |
| 612413 | 931027 | Crosby | 31 |
| 931027 | 612413 | Crosby | 31 |
| 170267 | 958827 | Dolliver | 1 |
| 958827 | 170267 | Dolliver | 1 |
| 104131 | 707536 | Dolliver | 14 |
| 707536 | 104131 | Dolliver | 14 |
| 477801 | 505241 | Dolliver | 8 |
| 505241 | 477801 | Dolliver | 8 |
| 118199 | 824292 | Kendrick | 1A |
| 824292 | 118199 | Kendrick | 1A |
| 105540 | 231742 | Kendrick | 3B |
| 231742 | 105540 | Kendrick | 3B |

O este segundo ejemplo para ver quiénes hicieron más de una compra en menos de 20 días:

```sql
SELECT o1.id AS o1_id,
       o1.account_id AS o1_account_id,
       o1.occurred_at AS o1_occurred_at,
       o2.id AS o2_id,
       o2.account_id AS o2_account_id,
       o2.occurred_at AS o2_occurred_at
  FROM orders o1
 LEFT JOIN orders o2
   ON o1.account_id = o2.account_id
  AND o2.occurred_at > o1.occurred_at
  AND o2.occurred_at <= o1.occurred_at + INTERVAL '28 days'
ORDER BY o1.account_id, o1.occurred_at
```

# Window Functions - OVER(PARTITION … ORDER BY …)

Las window functions permiten realizar cálculos sobre un conjunto de filas que están relacionadas con la fila actual, sin tener que agrupar las filas. Esto significa que puedes calcular agregaciones sin perder la granularidad de los datos originales.

## Partes

`PARTITION BY` establece los límites de los cálculos, mientras que `ORDER BY` determina cómo se procesan las filas dentro de esos límites. Esto permite que las funciones de ventana proporcionen resultados que reflejan tanto la agrupación como el orden de los datos.

### `PARTITION BY`

- **Función**: Divide el conjunto de resultados en grupos (particiones) basados en una o más columnas. Cada grupo se trata de manera independiente.
- **Reinicio de Cálculos**: Cuando se utiliza `PARTITION BY`, los cálculos (como sumas, conteos, promedios, etc.) se reinician para cada partición. Por ejemplo, si tienes `account_id` como partición, cada `account_id` tendrá sus propios resultados independientes.

### `ORDER BY`

- **Función**: Define el orden en que se procesan las filas dentro de cada partición. Esto es crucial para funciones que dependen del orden, como `ROW_NUMBER`, `RANK`, y `DENSE_RANK`.
- **Agrupación de Resultados**: Aunque `ORDER BY` no agrupa los resultados en el sentido tradicional (como lo haría un `GROUP BY`), sí afecta cómo se calculan los resultados de las funciones de ventana. Por ejemplo, si tienes un `SUM` con `ORDER BY`, el resultado de la suma se calculará acumulativamente hasta la fila actual dentro de la partición.
- **Resultados Equivalentes**: Cuando se utiliza `ORDER BY` en combinación con `PARTITION BY`, las filas que tienen el mismo valor en la columna de ordenación recibirán el mismo resultado para las funciones de agregación. Esto significa que, aunque los cálculos se realicen hasta la fila actual, los resultados para filas equivalentes en el `ORDER BY` serán los mismos.

## Funciones Usables

Las usables son las funciones de agregación, ranking y valor.

Para esto, ver:

- [Funciones de Agregación (GROUP BY y Window)](https://www.notion.so/Funciones-de-Agregaci-n-GROUP-BY-y-Window-1a6450a7153c80cdb4caf40e20c46bdd?pvs=21)
- [Funciones de Ranking (GROUP BY y Window)](https://www.notion.so/Funciones-de-Ranking-GROUP-BY-y-Window-1ae450a7153c80ed95e8c10b9e52a4e3?pvs=21)
- [Funciones de Valor (GROUP BY y Window)](https://www.notion.so/Funciones-de-Valor-GROUP-BY-y-Window-1ae450a7153c80ddb21ce0a41eae0137?pvs=21)

## Ejemplo simple

Si tienes un conjunto de datos con `account_id` y `occurred_at`, y aplicas:

```sql
SUM(standard_qty) OVER (PARTITION BY account_id ORDER BY DATE_TRUNC('month', occurred_at))

```

- **PARTITION BY account_id**: Los cálculos de suma se reinician para cada `account_id`.
- **ORDER BY DATE_TRUNC('month', occurred_at)**: Dentro de cada `account_id`, las filas se ordenan por mes. La suma se calculará acumulativamente hasta la fila actual, pero el resultado se mostrará para cada fila en esa partición.

## Ejemplo completo

```sql
SELECT
    id,
    account_id,
    DATE_TRUNC('month', occurred_at) AS month,
    DENSE_RANK() OVER (PARTITION BY account_id ORDER BY DATE_TRUNC('month', occurred_at)) AS dense_rank,
    SUM(standard_qty) OVER (PARTITION BY account_id ORDER BY DATE_TRUNC('month', occurred_at)) AS sum_standard_qty,
    COUNT(standard_qty) OVER (PARTITION BY account_id ORDER BY DATE_TRUNC('month', occurred_at)) AS count_standard_qty,
    AVG(standard_qty) OVER (PARTITION BY account_id ORDER BY DATE_TRUNC('month', occurred_at)) AS avg_standard_qty,
    MIN(standard_qty) OVER (PARTITION BY account_id ORDER BY DATE_TRUNC('month', occurred_at)) AS min_standard_qty,
    MAX(standard_qty) OVER (PARTITION BY account_id ORDER BY DATE_TRUNC('month', occurred_at)) AS max_standard_qty
FROM demo.orders

```

| id | account_id | month | dense_rank | sum_standard_qty | count_standard_qty | avg_standard_qty | min_standard_qty | max_standard_qty |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 100 | 2023-01-01 | 1 | 150 | 3 | 50 | 30 | 70 |
| 2 | 100 | 2023-02-01 | 2 | 200 | 4 | 50 | 40 | 60 |
| 3 | 200 | 2023-01-01 | 1 | 100 | 2 | 50 | 20 | 80 |
| 4 | 200 | 2023-02-01 | 2 | 120 | 2 | 60 | 60 | 60 |
- **id**: Identificador único de la fila.
- **account_id**: Identificador de la cuenta.
- **month**: Mes truncado de la fecha de ocurrencia.
- **dense_rank**: Rango denso de la fila dentro de cada `account_id` por mes.
- **sum_standard_qty**: Suma de `standard_qty` para cada `account_id` por mes.
- **count_standard_qty**: Conteo de `standard_qty` para cada `account_id` por mes.
- **avg_standard_qty**: Promedio de `standard_qty` para cada `account_id` por mes.
- **min_standard_qty**: Valor mínimo de `standard_qty` para cada `account_id` por mes.
- **max_standard_qty**: Valor máximo de `standard_qty` para cada `account_id` por mes.

## Aliases

Va entre el WHERE y el GROUP BY (pero en este ejemplo no hay ninguno)

```sql
SELECT 
    id,
    account_id,
    DATE_TRUNC('month', occurred_at) AS month,
    DENSE_RANK() OVER main_window AS dense_rank,
    SUM(standard_qty) OVER main_window AS sum_standard_qty,
    COUNT(standard_qty) OVER main_window AS count_standard_qty,
    AVG(standard_qty) OVER main_window AS avg_standard_qty,
    MIN(standard_qty) OVER main_window AS min_standard_qty,
    MAX(standard_qty) OVER main_window AS max_standard_qty
FROM demo.orders
WINDOW main_window AS (PARTITION BY account_id ORDER BY DATE_TRUNC('month', occurred_at))
```

## (Con PARTITION) VS (Sin PARTITION)

### Sin PARTITION

```sql
SELECT standard_amt_usd,
       SUM(standard_amt_usd) OVER (ORDER BY occurred_at) AS running_total
FROM orders
```

Simplemente van haciendo la operación sobre todos los resultados que va encontrando, es bueno haciendo acumulados. 

### Con PARTITION

Reinicia los acumulados cada que termina una partición

```sql
SELECT
    standard_qty,
    DATE_TRUNC('month', occurred_at) AS month,
    SUM(standard_qty) OVER (PARTITION BY DATE_TRUNC('month', occurred_at) ORDER BY occurred_at) AS running_total
FROM
    demo.orders;
```

Esta consulta SQL calcula la cantidad estándar de los pedidos y la suma acumulativa de esas cantidades para cada mes, ordenada por la fecha en que ocurrieron. Esto permite realizar un seguimiento de los pedidos a lo largo del tiempo, mostrando cómo se acumula la cantidad total mes a mes.

1. **SELECT**: Esta cláusula se utiliza para especificar las columnas que queremos recuperar de la tabla.
2. **standard_qty**: Se está seleccionando la columna `standard_qty` de la tabla `orders`. Esta columna probablemente representa la cantidad estándar de algún producto o servicio.
3. **DATE_TRUNC('month', occurred_at) AS month**:
    - **DATE_TRUNC**: Esta función se utiliza para truncar una fecha a una unidad de tiempo específica. En este caso, se trunca la fecha de `occurred_at` al primer día del mes.
    - **AS month**: Esto asigna un alias a la columna truncada, de modo que se puede referir a ella como `month` en el resultado.
4. **SUM(standard_qty) OVER (PARTITION BY DATE_TRUNC('month', occurred_at) ORDER BY occurred_at) AS running_total**:
    - Partes
        - **SUM(standard_qty)**: Esta función suma la cantidad estándar.
        - **OVER**: Esta cláusula permite calcular una función de agregación (en este caso, la suma) sobre un conjunto de filas definido por las cláusulas `PARTITION BY` y `ORDER BY`.
        - **PARTITION BY DATE_TRUNC('month', occurred_at)**: Esto significa que la suma se calculará para cada grupo de filas que comparten el mismo mes (es decir, todas las filas cuyo `occurred_at` caen en el mismo mes).
        - **ORDER BY occurred_at**: Dentro de cada partición (cada mes), las filas se ordenan por la fecha `occurred_at`. Esto es importante para calcular un "running total" (total acumulado) que se actualiza a medida que se avanza en las filas ordenadas.
        - **AS running_total**: Esto asigna un alias a la suma acumulativa, permitiendo referirse a ella como `running_total`.
    - Significado
        - **`SUM(standard_qty) OVER (...)`**: Aquí estamos utilizando la función de agregación **`SUM`** como una window function. Esto significa que la suma se calcula sobre un conjunto de filas definido por la cláusula **`OVER`**.
        - **`PARTITION BY DATE_TRUNC('month', occurred_at)`**: Esto divide (o particiona) los resultados en grupos basados en el mes de la fecha **`occurred_at`**. Por lo tanto, la suma se calcula por separado para cada mes.
        - **`ORDER BY occurred_at`**: Dentro de cada partición (es decir, cada mes), las filas se ordenan por la fecha **`occurred_at`**. Esto es crucial para calcular un total acumulado, ya que la suma se realiza en el orden de las fechas.
5. **FROM demo.orders**: Se está seleccionando de la tabla `orders`, que se encuentra en el esquema `demo`.

Si usaras **`GROUP BY`**, perderías la granularidad de las filas individuales, ya que el resultado mostraría una fila por cada grupo (en este caso, un mes). En cambio, al usar window functions, puedes mantener todas las filas originales y agregar información adicional (como el total acumulado) sin eliminar datos.

# Performance Tuning

## EXPLAIN

Usar `EXPLAIN` es una práctica recomendada para entender y optimizar el rendimiento de las consultas SQL. Te permite identificar áreas de mejora y asegurarte de que las consultas se ejecuten de la manera más eficiente posible.

```sql
EXPLAIN
SELECT *
FROM demo.web_events_full
WHERE occurred_at >= '2016-01-01'
AND occurred_at < '2016-02-01'
LIMIT 100
```

- **Descripción**: `EXPLAIN` se utiliza para mostrar el plan de ejecución de una consulta SQL. Proporciona información sobre cómo el motor de la base de datos planea ejecutar la consulta, incluyendo detalles sobre el acceso a las tablas, el uso de índices, el orden de las operaciones y el costo estimado de cada paso.
- **Uso**: Al ejecutar `EXPLAIN` antes de una consulta, puedes obtener una visión general de la eficiencia de la consulta y detectar posibles cuellos de botella. Esto es útil para optimizar consultas, especialmente en bases de datos grandes.

Da estas cosas:

| Step | Description | Cost | Rows | Width |
| --- | --- | --- | --- | --- |
| Limit | Limit the number of rows to 100 | cost=0.00..83.12 | 100 | 75 |
| Seq Scan | Sequential scan on web_events_full | cost=0.00..226.09 | 272 | 75 |
| Filter | Filter on occurred_at conditions |  |  |  |
|  | (occurred_at >= '2016-01-01' AND |  |  |  |
|  | occurred_at < '2016-02-01') |  |  |  |
- **Tipo de acceso**: Indica cómo se accede a los datos (por ejemplo, si se utiliza un índice o un escaneo completo de la tabla).
- **Costo estimado**: Proporciona un costo estimado para ejecutar la consulta, que puede ayudar a comparar diferentes enfoques.
- **Número de filas**: Estima cuántas filas se procesarán en cada etapa de la consulta.
- **Orden de ejecución**: Muestra el orden en que se ejecutarán las operaciones.

## JOINs

- NO es bueno usar WHERE después de un JOIN, porque recorres la pendejada dos veces. Es mejor agregar esa condición con un AND en el mismo JOIN. Que haga parte de la condición del JOIN, Una sola pasada.
    
    ```sql
     SELECT orders.*, 
    	 	    accounts.*,
    	 FROM demo.orders
    	 LEFT JOIN demo.accounts
    		 ON orders.account_id = accounts.id
    --WHERE accounts.sales_rep_id = 321500
    		AND accounts.sales_rep_id = 321500
    ```
    
- Cuando tengas JOINs, no les hagas agregaciones. Mejor haz las agregaciones antes de hacer el JOIN, usando subquerys.
    
    Lo que pasa es que ejecuta las agregaciones después del JOIN pero antes/durante el GROUP BY, así que tiene que hacer agregaciones de tablas enoooormes. Es mejor hacer agregaciones antes cuando se pueda, si es que no dependen de cosas del JOIN sino de tablas individuales.
    
    ```sql
    -- NO, LENTO
    SELECT account_id,
           COUNT(*) AS web_events
      FROM demo.accounts accounts
      JOIN demo.web_events_full events
        ON events.account_id = accounts.id
     GROUP BY 1
     ORDER BY 2 DESC
    ```
    
    ```sql
    -- MEJOR, DESDE ANTES
    SELECT a.name,
           sub.web_events
      FROM (
    	     SELECT account_id,
    	            COUNT(*) AS web_events
    	       FROM demo.web_events_full
    	      GROUP BY account_id
         ) sub
      JOIN demo.accounts a ON a.id = sub.account_id
     ORDER BY sub.web_events DESC
    ```
    
    Otro ejemplo más extremo es este, en donde la agregación se haría en 79.000 filas, para un resultado de cerca de 1.000:
    
    ```sql
    SELECT DATE_TRUNC('day', o.occurred_at) AS date,
           COUNT(DISTINCT a.sales_rep_id) AS active_sales_reps,
           COUNT(DISTINCT o.id) AS orders,
           COUNT(DISTInct we.id) AS web_visits
      FROM accounts a
      JOIN orders o
        ON o.account_id = a.id
      JOIN web_events we
        ON DATE_TRUNC('day', we.occurred_at) = DATE_TRUNC('day', o.occurred_at)
     GROUP BY 1
     ORDER BY 1 DESC
    ```
    
    ```sql
    -- Mejor separado así. (Pudo ser con WITHs o vistas)
    SELECT COALESCE(orders.date, web_events.date) AS date,
           orders.active_sales_reps,
    	     orders.orders,
    	     web_events.web_visits
      FROM (
    		    SELECT DATE_TRUNC('day', o.occurred_at) AS date,
    			         COUNT(a.sales_rep_id) AS active_sales_reps,
    			         COUNT(o.id) AS orders
    			    FROM demo.accounts a
    			    JOIN demo.orders o ON o.account_id = a.id
    		     GROUP BY 1
           ) orders
      FULL JOIN
           (
    				SELECT DATE_TRUNC('day', we.occurred_at) AS date,
    					     COUNT(we.id) AS web_visits
    				  FROM demo.web_events_full we
    				 GROUP BY 1
            ) web_events
      FULL JOIN orders
        ON web_events.date = orders.date
     ORDER BY 1 DESC
    ```