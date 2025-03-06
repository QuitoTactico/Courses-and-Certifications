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

# CREATE

## DATABASE

```sql
CREATE DATABASE forum;
```

## TABLE

```sql
CREATE TABLE posts ( content TEXT,
                     time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                     id SERIAL );
```

## PRIMARY KEY

### Simple

```sql
CREATE TABLE clientes (
id_cliente INT PRIMARY KEY,
nombre VARCHAR(100),
email VARCHAR(100)
);
```

### Compuesta

```sql
CREATE TABLE inscripciones (
id_estudiante INT,
id_curso INT,
fecha_inscripcion DATE,
PRIMARY KEY (id_estudiante, id_curso)
);
```

## FOREAN KEY

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

<aside>
💡

Y hay una forma extra, para cuando la columna se llama igual en ambas tablas:

```sql
CREATE TABLE sales (
sku TEXT REFERENCES products, -- columna products.sku
sale_date DATE,
count INT
);
```

</aside>

# UPDATE

```sql
UPDATE usuarios
SET correo = 'juan.perez@ejemplo.com', edad = 30
WHERE id = 1;
```

# DELETE

```sql
DELETE FROM usuarios
WHERE id = 1;
```

# EMR

![image.png](attachment:164aebaf-8778-4012-ad1f-dae7c1f61ade:image.png)