# Sources: 

- https://www.udacity.com/course/intro-to-relational-databases--ud197
- https://www.udacity.com/course/sql-for-data-analysis--ud198 (MOSTLY)
- https://globant.udemy.com/course/sql-for-beginners-course/learn/lecture/40417882?learning_path_id=9400125#overview

# Data Types

![image.png](attachment:d55a69a2-7bd6-41a5-bac1-3fecfa8e1b72:image.png)

## En SQLite

### 1. **Tipos de Datos Numéricos**

- **Enteros:**
    - `INTEGER`: Almacena enteros de hasta 8 bytes.
- **Decimales:**
    - `REAL`: Almacena números de punto flotante de 8 bytes.
    - `NUMERIC`: Almacena números en formato decimal.

### 2. **Tipos de Datos de Cadenas de Texto**

- `TEXT`: Almacena cadenas de texto de longitud variable.

### 3. **Tipos de Datos de Fecha y Hora**

- SQLite no tiene un tipo de dato específico para fechas y horas. Sin embargo, puedes almacenar fechas y horas como `TEXT`, `REAL`, o `INTEGER`.

### 4. **Tipos de Datos Binarios**

- `BLOB`: Almacena datos binarios de longitud variable.

### 5. **Tipos de Datos Booleanos**

- No hay un tipo booleano explícito. Normalmente se utilizan `INTEGER` (0 para `FALSE`, 1 para `TRUE`).

---

## En MySQL

### 1. **Tipos de Datos Numéricos**

- **Enteros:**
    - `TINYINT`: -128 a 127 (1 byte)
    - `SMALLINT`: -32,768 a 32,767 (2 bytes)
    - `MEDIUMINT`: -8,388,608 a 8,388,607 (3 bytes)
    - `INT` o `INTEGER`: -2,147,483,648 a 2,147,483,647 (4 bytes)
    - `BIGINT`: -9,223,372,036,854,775,808 a 9,223,372,036,854,775,807 (8 bytes)
- **Decimales:**
    - `FLOAT`: Número de punto flotante (4 bytes)
    - `DOUBLE`: Número de punto flotante de doble precisión (8 bytes)
    - `DECIMAL` o `NUMERIC`: Precisión exacta (almacena números exactos, se define con precisión y escala).

### 2. **Tipos de Datos de Cadenas de Texto**

- **Cadenas de longitud variable:**
    - `VARCHAR(n)`: Hasta 65,535 caracteres, donde `n` es el tamaño máximo.
    - `TEXT`: Hasta 65,535 caracteres.
- **Cadenas de longitud fija:**
    - `CHAR(n)`: Hasta 255 caracteres, donde `n` es el tamaño fijo.
    - `BINARY`: Almacena datos binarios, longitud fija.
- **Cadenas de texto largo:**
    - `MEDIUMTEXT`: Hasta 16,777,215 caracteres.
    - `LONGTEXT`: Hasta 4,294,967,295 caracteres.

### 3. **Tipos de Datos de Fecha y Hora**

- `DATE`: Almacena fechas (YYYY-MM-DD).
- `TIME`: Almacena horas (HH:MM:SS).
- `DATETIME`: Almacena fechas y horas (YYYY-MM-DD HH:MM:SS).
- `TIMESTAMP`: Almacena un valor que representa un punto en el tiempo (desde 1970-01-01 00:00:01 UTC).
- `YEAR`: Almacena un año en formato de 4 dígitos.

### 4. **Tipos de Datos Booleanos**

- `BOOLEAN`: Se utiliza para almacenar valores booleanos, es un alias para `TINYINT(1)`.

### 5. **Tipos de Datos Binarios**

- `BLOB`: Almacena datos binarios de hasta 65,535 bytes.
- `MEDIUMBLOB`: Hasta 16,777,215 bytes.
- `LONGBLOB`: Hasta 4,294,967,295 bytes.

### 6. **Tipos de Datos Espaciales**

- **Geometría:**
    - `GEOMETRY`: Almacena datos espaciales de cualquier tipo.
    - `POINT`, `LINESTRING`, `POLYGON`: Tipos específicos para representar geometrías.

---

## En PostgreSQL

### 1. **Tipos de Datos Numéricos**

- **Enteros:**
    - `SMALLINT`: -32,768 a 32,767 (2 bytes)
    - `INTEGER`: -2,147,483,648 a 2,147,483,647 (4 bytes)
    - `BIGINT`: -9,223,372,036,854,775,808 a 9,223,372,036,854,775,807 (8 bytes)
- **Decimales:**
    - `NUMERIC`: Precisión exacta (almacena números exactos, se define con precisión y escala).
    - `REAL`: Número de punto flotante (4 bytes).
    - `DOUBLE PRECISION`: Número de punto flotante de doble precisión (8 bytes).

### 2. **Tipos de Datos de Cadenas de Texto**

- `CHAR(n)`: Longitud fija de hasta 1 a 8,000 caracteres.
- `VARCHAR(n)`: Longitud variable de hasta 1 a 65,535 caracteres.
- `TEXT`: Longitud variable de hasta 1 GB.

### 3. **Tipos de Datos de Fecha y Hora**

- `DATE`: Almacena fechas (YYYY-MM-DD).
- `TIME`: Almacena horas (HH:MM:SS).
- `TIMESTAMP`: Almacena fechas y horas (YYYY-MM-DD HH:MM:SS).
- `TIMESTAMPTZ`: Almacena fechas y horas con zona horaria.
- `INTERVAL`: Almacena un intervalo de tiempo.

### 4. **Tipos de Datos Booleanos**

- `BOOLEAN`: Almacena valores booleanos (`TRUE`, `FALSE`, `NULL`).

### 5. **Tipos de Datos Binarios**

- `BYTEA`: Almacena datos binarios de longitud variable.

### 6. **Tipos de Datos JSON**

- `JSON`: Almacena datos en formato JSON.
- `JSONB`: Almacena datos en formato JSON binario (más eficiente para consultas).

### 7. **Tipos de Datos de Geometría**

- `POINT`, `LINE`, `LSEG`, `BOX`, `PATH`, `POLYGON`, `CIRCLE`: Tipos para representar formas geométricas.

### 8. **Tipos de Datos de Array**

- PostgreSQL permite almacenar arrays de cualquier tipo de dato.

# **1. CREATE**

## 1.1. **DATABASE**

```sql
CREATE DATABASE forum;

```

## 1.2. **TABLE**

```sql
CREATE TABLE posts (
    content TEXT,
    time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    id SERIAL
);

```

## 1.3. **PRIMARY KEY**

### 1.3.1. **Simple**

```sql
CREATE TABLE clientes (
    id_cliente INT PRIMARY KEY,
    nombre VARCHAR(100),
    email VARCHAR(100)
);

```

### 1.3.2. **Compuesta**

```sql
CREATE TABLE inscripciones (
    id_estudiante INT,
    id_curso INT,
    fecha_inscripcion DATE,
    PRIMARY KEY (id_estudiante, id_curso)
);

```

## 1.4. **FOREIGN KEY**

```sql
CREATE TABLE cursos (
    id_curso INT PRIMARY KEY,
    nombre_curso VARCHAR(100)
);

```

```sql
CREATE TABLE inscripciones (
    id_estudiante INT,
    id_curso INT,
    fecha_inscripcion DATE,
    PRIMARY KEY (id_estudiante, id_curso),
    FOREIGN KEY (id_estudiante) REFERENCES clientes(id_cliente),
    FOREIGN KEY (id_curso) REFERENCES cursos(id_curso)
);

```

### 1.4.1. Columas con igual nombre

```sql
CREATE TABLE sales (
    sku TEXT REFERENCES products, -- columna products.sku
    sale_date DATE,
    count INT
);
```

# 2. **MODIFY**

## 2.1. **ALTER TABLE - Agregar y Eliminar Columnas**

### 2.1.1. Agregar una columna

```sql
ALTER TABLE clientes ADD telefono VARCHAR(15);
```

### 2.1.2. Eliminar una columna

```sql
ALTER TABLE clientes DROP COLUMN telefono;
```

## 2.2. **Renombrar Columnas**

```sql
ALTER TABLE clientes RENAME COLUMN email TO correo_electronico;

```

## 2.3. **Modificar Tipos de Datos de Columnas**

- **CHANGE**: Cambia el nombre de la columna y puede cambiar su tipo de datos. Se requiere especificar tanto el nombre antiguo como el nuevo.
- **RENAME COLUMN**: Cambia solo el nombre de la columna sin afectar el tipo de datos. Es más simple y directo.
- **MODIFY**: Cambia el tipo de datos de la columna y otras propiedades (como `NOT NULL` o `DEFAULT`), pero no renombra la columna.

### 2.3.1. **ALTER TABLE ... CHANGE**

- Estructura

```sql
ALTER TABLE <nombre_tabla>
CHANGE <nombre_columna> <nuevo_nombre_columna> <nuevo_tipo>;

```

- Función

**CHANGE** se utiliza para cambiar el nombre de una columna y, opcionalmente, su tipo de datos en una sola instrucción.

Debes especificar el nombre antiguo de la columna, el nuevo nombre y, si lo deseas, también puedes cambiar el tipo de dato de la columna.

- Ejemplo

```sql
ALTER TABLE empleados
CHANGE nombre nombre_completo VARCHAR(150);

```

- En este ejemplo, la columna `nombre` se renombra a `nombre_completo` y se cambia su tipo de datos a `VARCHAR(150)`.

### 2.3.2. **ALTER TABLE ... RENAME COLUMN**

- Estructura

```sql
ALTER TABLE <nombre_tabla>
RENAME COLUMN <nombre_columna_antiguo> TO <nuevo_nombre_columna>;

```

- Función

**RENAME COLUMN** se utiliza exclusivamente para cambiar el nombre de una columna sin modificar su tipo de datos ni otras propiedades.

Es más simple que **CHANGE**, ya que solo necesitas proporcionar el nombre antiguo y el nuevo.

- Ejemplo

```sql
ALTER TABLE empleados
RENAME COLUMN nombre TO nombre_completo;

```

- En este ejemplo, la columna `nombre` se renombra a `nombre_completo`, pero su tipo y otras propiedades permanecen sin cambios.

### 2.3.3. **ALTER TABLE ... MODIFY**

- Estructura

```sql
ALTER TABLE <nombre_tabla>
MODIFY <nombre_columna> <nuevo_tipo> [<opciones_adicionales>];

```

- Función

**MODIFY** se utiliza para cambiar el tipo de datos de una columna existente y/o ajustar otras propiedades, como `NOT NULL`, `DEFAULT`, etc.

No se utiliza para renombrar columnas, solo para modificar sus atributos.

- Ejemplo

```sql
ALTER TABLE empleados
MODIFY salario DECIMAL(10, 2) NOT NULL;

```

- En este ejemplo, la columna `salario` se modifica para ser de tipo `DECIMAL(10, 2)` y se establece como `NOT NULL`, lo que significa que no puede contener valores nulos.

## 2.4. **Agregar y Eliminar PRIMARY KEYS**

### 2.4.1. Agregar una clave primaria

```sql
ALTER TABLE clientes ADD PRIMARY KEY (id_cliente);
```

### 2.4.2. Eliminar una clave primaria

```sql
ALTER TABLE clientes DROP CONSTRAINT clientes_pkey; -- nombre de la restricción
```

## 2.5. **Agregar y Eliminar FOREIGN KEYS**

### 2.5.1. Agregar una clave foránea

```sql
ALTER TABLE inscripciones ADD FOREIGN KEY (id_curso) REFERENCES cursos(id_curso);
```

### 2.5.2. Eliminar una clave foránea

```sql
ALTER TABLE inscripciones DROP CONSTRAINT inscripciones_id_curso_fkey; -- nombre de la restricción
```

## 2.6. **Implementar Constraints**

### 2.6.1. **PRIMARY KEY**

Forma de Creación de Tabla

```sql
CREATE TABLE clientes (
    id_cliente INT PRIMARY KEY,
    nombre VARCHAR(100)
);
```

Forma de ALTER TABLE

```sql
ALTER TABLE clientes ADD CONSTRAINT pk_clientes PRIMARY KEY (id_cliente);
```

### 2.6.2. **FOREIGN KEY**

Forma de Creación de Tabla

```sql
CREATE TABLE inscripciones (
    id_estudiante INT,
    id_curso INT,
    PRIMARY KEY (id_estudiante, id_curso),
    FOREIGN KEY (id_estudiante) REFERENCES clientes(id_cliente)
);
```

Forma de ALTER TABLE

```sql
ALTER TABLE inscripciones ADD CONSTRAINT fk_estudiante FOREIGN KEY (id_estudiante) REFERENCES clientes(id_cliente);
```

### 2.6.3. **UNIQUE**

Forma de Creación de Tabla

```sql
CREATE TABLE usuarios (
    id_usuario INT PRIMARY KEY,
    email VARCHAR(100) UNIQUE
);
```

Forma de ALTER TABLE

```sql
ALTER TABLE usuarios ADD CONSTRAINT unique_email UNIQUE (email);
```

### 2.6.4. **NOT NULL**

Forma de Creación de Tabla

```sql
CREATE TABLE productos (
    id_producto INT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    precio DECIMAL(10, 2) NOT NULL
);
```

Forma de ALTER TABLE

```sql
ALTER TABLE productos ALTER COLUMN nombre SET NOT NULL;
```

### 2.6.5. **CHECK**

Forma de Creación de Tabla

```sql
CREATE TABLE empleados (
    id_empleado INT PRIMARY KEY,
    salario DECIMAL(10, 2),
    CHECK (salario > 0) -- el salario debe ser mayor que cero
);
```

Forma de ALTER TABLE

```sql
ALTER TABLE empleados ADD CONSTRAINT chk_salario CHECK (salario > 0);
```

### 2.6.6. **DEFAULT**

Forma de Creación de Tabla

```sql
CREATE TABLE pedidos (
    id_pedido INT PRIMARY KEY,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

Forma de ALTER TABLE

```sql
ALTER TABLE pedidos ALTER COLUMN fecha SET DEFAULT CURRENT_TIMESTAMP;
```

### 2.6.7. **INDEX**

Forma de Creación de Tabla

```sql
CREATE TABLE clientes (
    id_cliente INT PRIMARY KEY,
    nombre VARCHAR(100)
);
CREATE INDEX idx_nombre ON clientes(nombre);
```

Forma de ALTER TABLE

```sql
ALTER TABLE clientes ADD INDEX idx_nombre (nombre);
```

### 2.6.8. **AUTO_INCREMENT**

Forma de Creación de Tabla

```sql
CREATE TABLE clientes (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100)
);
```

Forma de ALTER TABLE

```sql
ALTER TABLE clientes MODIFY id_cliente INT AUTO_INCREMENT;
```

### 2.6.9. **COMPOSITE KEY**

Forma de Creación de Tabla

```sql
CREATE TABLE inscripciones (
    id_estudiante INT,
    id_curso INT,
    PRIMARY KEY (id_estudiante, id_curso)
);
```

Forma de ALTER TABLE

```sql
ALTER TABLE inscripciones ADD CONSTRAINT pk_inscripciones PRIMARY KEY (id_estudiante, id_curso);
```

### 2.6.10. **REFERENCES**

Forma de ALTER TABLE (parte del FOREIGN KEY)

```sql
ALTER TABLE inscripciones ADD CONSTRAINT fk_curso FOREIGN KEY (id_curso) REFERENCES cursos(id_curso);
```

# 3. **DATA MANIPULATION LANGUAGE (DML)**

## 3.1. **INSERT**

### 3.1.1. Insertar datos en una tabla

```sql
INSERT INTO clientes (id_cliente, nombre, email) VALUES (1, 'Juan Pérez', 'juan.perez@ejemplo.com');
```

### 3.1.2. Insertar múltiples registros

```sql
INSERT INTO clientes (id_cliente, nombre, email) VALUES
(2, 'Ana Gómez', 'ana.gomez@ejemplo.com'),
(3, 'Luis Martínez', 'luis.martinez@ejemplo.com');
```

## 3.2. **UPDATE**

```sql
UPDATE usuarios
SET correo = 'juan.perez@ejemplo.com', edad = 30
WHERE id = 1;
```

## 3.3. **DELETE**

### 3.3.1. Borrar un registro específico

```sql
DELETE FROM usuarios
WHERE id = 1;
```

### 3.3.2. Borrar múltiples registros

```sql
DELETE FROM usuarios
WHERE edad < 18;
```

### 3.3.3. Borrar todos los registros de una tabla

```sql
TRUNCATE TABLE usuarios; -- Elimina todos los registros, pero no la tabla
```

## 4. **Comandos Avanzados y Buenas Prácticas**

### 4.1. **Transacciones**

- Las transacciones permiten agrupar varios comandos en una sola unidad de trabajo que se puede confirmar (commit) o deshacer (rollback).

```sql
BEGIN;

INSERT INTO clientes (id_cliente, nombre, email) VALUES (4, 'Carlos Ruiz', 'carlos.ruiz@ejemplo.com');

-- Si algo falla, se puede revertir
ROLLBACK;

-- Si todo va bien
COMMIT;

```

### 4.2. **Comandos para Población de Datos**

```sql
-- Población de la base de datos de la tienda de café
INSERT INTO productos (id_producto, nombre, precio) VALUES (1, 'Café', 5.00);
INSERT INTO productos (id_producto, nombre, precio) VALUES (2, 'Té', 3.50);

```

### 4.3. **Guía Completa para Actualizar Datos Existentes**

- Instrucciones detalladas sobre cómo modificar datos en tablas SQL.
- Ejemplo de actualización condicional:

```sql
UPDATE productos
SET precio = precio * 0.9 -- aplicar un 10% de descuento
WHERE nombre = 'Café';
```

### 4.4. **Guía Completa de Eliminación de Datos**

- Métodos para eliminar datos de tablas, incluyendo el uso de condiciones específicas.
- Ejemplo de eliminación con condiciones:

```sql
DELETE FROM productos
WHERE precio < 2.00; -- eliminar productos que cuesten menos de 2
```

### 4.5. **Funciones Agregadas y Agrupamientos**

```sql
SELECT COUNT(*) FROM clientes; -- contar total de clientes
SELECT AVG(precio) FROM productos; -- promedio de precios
SELECT nombre_curso, COUNT(*) FROM inscripciones GROUP BY nombre_curso; -- contar inscripciones por curso
```

### 4.6. **Combinación de Tablas (JOIN)**

```sql
SELECT clientes.nombre, inscripciones.fecha_inscripcion
FROM clientes
JOIN inscripciones ON clientes.id_cliente = inscripciones.id_estudiante;
```

### 4.7. **Subconsultas**

```sql
SELECT nombre FROM clientes
WHERE id_cliente IN (SELECT id_estudiante FROM inscripciones WHERE id_curso = 1);
```

# Principios de Diseño de Base de Datos

## 1. Introducción a los Conceptos de Diseño de Base de Datos

El diseño de bases de datos es esencial para la organización eficiente de la información. Un buen diseño asegura que los datos sean accesibles, consistentes y fáciles de gestionar. Se enfoca en la estructura, las relaciones y las reglas que rigen la información.

---

## 2. Normalización de Bases de Datos

La normalización es el proceso de estructurar una base de datos para reducir la redundancia y mejorar la integridad de los datos. Consiste en dividir una base de datos en tablas más pequeñas y definir relaciones entre ellas. Las principales formas normales son:

### 2.1. Primera Forma Normal (1NF)

- **Definición**: Una tabla está en 1NF si:
    - No contiene grupos repetitivos o arrays.
    - Todos los atributos contienen solo valores atómicos (indivisibles).
- **Objetivo**: Eliminar duplicaciones de datos y asegurar que cada campo almacene un solo valor.

### 2.2. Segunda Forma Normal (2NF)

- **Definición**: Una tabla está en 2NF si:
    - Está en 1NF.
    - Todos los atributos no clave son completamente dependientes de la clave primaria.
- **Objetivo**: Eliminar dependencias parciales, donde un atributo depende solo de una parte de la clave primaria.

### 2.3. Tercera Forma Normal (3NF)

- **Definición**: Una tabla está en 3NF si:
    - Está en 2NF.
    - No hay dependencias transitivas, es decir, un atributo no clave no debe depender de otro atributo no clave.
- **Objetivo**: Optimizar las relaciones de datos y reducir la redundancia aún más.

---

## 3. Relaciones Entre Tablas en Bases de Datos Relacionales

Las relaciones entre tablas permiten conectar datos en diferentes tablas, lo que facilita la organización y consulta de información.

### 3.1. Relaciones Uno a Uno

- **Definición**: Cada registro en una tabla se relaciona con un único registro en otra tabla.
- **Ejemplo**: Un usuario puede tener un único perfil, y un perfil pertenece a un único usuario.
- **Diagrama**:
    
    ```
    Usuario <-> Perfil
    
    ```
    

### 3.2. Relaciones Uno a Muchos

- **Definición**: Un registro en una tabla puede estar relacionado con múltiples registros en otra tabla.
- **Ejemplo**: Un autor puede haber escrito varios libros, pero cada libro tiene un único autor.
- **Diagrama**:
    
    ```
    Autor <----> Libros
    
    ```
    

### 3.3. Relaciones Muchos a Muchos

- **Definición**: Un registro en una tabla puede estar relacionado con múltiples registros en otra tabla y viceversa.
- **Ejemplo**: Estudiantes y cursos; un estudiante puede inscribirse en varios cursos y un curso puede tener varios estudiantes.
- **Implementación**: Se utiliza una tabla de unión (o tabla intermedia) para gestionar estas relaciones.
- **Diagrama**:
    
    ```
    Estudiantes <----> Inscripciones <----> Cursos
    
    ```
    

---

## 4. Uso de Restricciones

Las restricciones son reglas aplicadas a las columnas de una tabla para asegurar la integridad de los datos.

Su uso está en: [2.6. **Implementar Constraints**](https://www.notion.so/2-6-Implementar-Constraints-1b2450a7153c803eb55fdf7beb853e94?pvs=21) 

### 4.1. Not Null

- **Definición**: La columna no puede tener valores nulos. Es obligatoria.

### 4.2. Unique

- **Definición**: Los valores en la columna deben ser únicos, sin duplicados.

### 4.3. Primary Key

- **Definición**: Identificador único para cada registro en una tabla. No puede ser nulo y debe ser único.

### 4.4. Foreign Key

- **Definición**: Establece una relación entre dos tablas. Los valores en esta columna deben coincidir con los valores en la clave primaria de otra tabla.

### 4.5. Check

- **Definición**: Permite establecer condiciones que los valores de una columna deben cumplir (por ejemplo, un rango de valores).

# EMR

![image.png](attachment:164aebaf-8778-4012-ad1f-dae7c1f61ade:image.png)