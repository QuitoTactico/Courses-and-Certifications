https://www.udacity.com/course/intro-to-relational-databases--ud197

# Conexión con varias DB
Desde consola

| SGBD      | Comando de Conexión                                       | Información Adicional                                 |
|-----------|-----------------------------------------------------------|------------------------------------------------------|
| MySQL     | `mysql -u usuario -p`                                    | Después de conectarte, usa `USE nombre_de_la_base_de_datos;` para seleccionar la base de datos. |
| PostgreSQL| `psql -U usuario -d nombre_de_la_base_de_datos`         | Se te pedirá contraseña del usuario. Para la base de datos por defecto, usa `psql -U usuario`. |
| SQL Server| `sqlcmd -S nombre_servidor -U usuario -P contraseña`     | Usa `sqlcmd -S nombre_servidor -E` para autenticación de Windows.              |
| Oracle    | `sqlplus usuario/contraseña@nombre_de_la_base_de_datos`  | Verifica la configuración de `tnsnames.ora` para conexiones de red. |
| SQLite    | `sqlite3 nombre_de_la_base_de_datos.db`                  | Se conecta directamente a la base de datos especificada. |

Si tienes más preguntas o necesitas información adicional, ¡estaré encantado de ayudar!

# Ver propiedades de una tabla:
Comandos para ver las propiedades de una tabla (columnas y tipos).

| SGBD      | Comando para Ver Propiedades de la Tabla                  | Información Adicional                                   |
|-----------|-----------------------------------------------------------|--------------------------------------------------------|
| MySQL     | `DESCRIBE nombre_de_la_tabla;`                           | Alternativamente, puedes usar `SHOW COLUMNS FROM nombre_de_la_tabla;`. |
| PostgreSQL| `\d nombre_de_la_tabla`                                   | O usa la consulta SQL: `SELECT column_name, data_type FROM information_schema.columns WHERE table_name = 'nombre_de_la_tabla';` |
| SQL Server| `SP_HELP 'nombre_de_la_tabla';`                          | O usa la consulta SQL: `SELECT COLUMN_NAME, DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'nombre_de_la_tabla';` |
| Oracle    | `DESC nombre_de_la_tabla;`                               | O usa la consulta SQL: `SELECT COLUMN_NAME, DATA_TYPE FROM ALL_TAB_COLUMNS WHERE TABLE_NAME = 'NOMBRE_DE_LA_TABLA';` |
| SQLite    | `PRAGMA table_info(nombre_de_la_tabla);`                | Devuelve información sobre cada columna de la tabla.  |

# Librerías:
Librerías de conexión que puedes utilizar con cada uno de los sistemas de gestión de bases de datos.

| SGBD      | Biblioteca de Conexión                   | Ejemplo de Importación                   |
|-----------|------------------------------------------|------------------------------------------|
| MySQL     | `mysql-connector-python` (o `PyMySQL`) | `import mysql.connector`                 |
| PostgreSQL| `psycopg2`                              | `import psycopg2`                       |
| SQL Server| `pyodbc`                                | `import pyodbc`                         |
| Oracle    | `cx_Oracle`                             | `import cx_Oracle`                      |
| SQLite    | `sqlite3`                               | `import sqlite3`                        |

### Ejemplos de Conexión en Python

1. **MySQL**
   ```python
   import mysql.connector

   conn = mysql.connector.connect(
       host="localhost",
       user="tu_usuario",
       password="tu_contraseña",
       database="nombre_de_la_base_de_datos"
   )
   ```

2. **PostgreSQL**
   ```python
   import psycopg2

   conn = psycopg2.connect(
       dbname="nombre_de_la_base_de_datos",
       user="tu_usuario",
       password="tu_contraseña",
       host="localhost"
   )
   ```

3. **SQL Server**
   ```python
   import pyodbc

   conn = pyodbc.connect(
       'DRIVER={SQL Server};'
       'SERVER=nombre_servidor;'
       'DATABASE=nombre_de_la_base_de_datos;'
       'UID=tu_usuario;'
       'PWD=tu_contraseña'
   )
   ```

4. **Oracle**
   ```python
   import cx_Oracle

   conn = cx_Oracle.connect(
       "tu_usuario", 
       "tu_contraseña", 
       "nombre_de_la_base_de_datos"
   )
   ```

5. **SQLite**
   ```python
   import sqlite3

   conn = sqlite3.connect("nombre_de_la_base_de_datos.db")
   ```
