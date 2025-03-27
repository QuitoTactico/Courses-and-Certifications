# Sources

https://learn.mongodb.com/learn/learning-path/si-associate-certification-program

Laboratorios: [https://learn.mongodb.com/learn/course/getting-started-with-mongodb-atlas/resources/list-of-virtual-labs/all” class=](https://learn.mongodb.com/learn/course/getting-started-with-mongodb-atlas/resources/list-of-virtual-labs/all%E2%80%9D%20class=)

# Generalidades

- [What Is MongoDB?](https://www.mongodb.com/what-is-mongodb?_ga=2.64483046.810066485.1665291537-836515500.1666025886)
- [MongoDB Use Cases](https://www.mongodb.com/use-cases?_ga=2.64483046.810066485.1665291537-836515500.1666025886)
- [MongoDB Docs: Documents](https://www.mongodb.com/docs/manual/core/document/?_ga=2.64483046.810066485.1665291537-836515500.1666025886)

MongoDB es una base de datos NoSQL orientada a documentos que permite almacenar datos en un formato flexible y escalable. Se utiliza ampliamente para aplicaciones que requieren alta disponibilidad, rendimiento y escalabilidad horizontal. MongoDB asegura transacciones ACID (Atomicity, Consistency, Isolation, Durability). Los datos se almacenan en formato BSON (Binary JSON), lo que permite una rica estructura de datos.

- **MongoDB**: Base de datos NoSQL orientada a documentos.
- **Collection**: Conjunto de documentos, similar a una tabla en bases de datos relacionales.
- **Document**: Unidad básica de datos en formato JSON/BSON, que puede ser flexible y jerárquico.

Este enfoque flexible de MongoDB permite adaptarse fácilmente a cambios en los requisitos de datos y facilita el manejo de grandes volúmenes de información.

## Jerarquía

### **1. Organización**

- La unidad más alta en la jerarquía. Representa una entidad que puede agrupar múltiples proyectos, como una empresa o una institución.

### **2. Proyecto**

- Dentro de una organización, un proyecto puede representar un conjunto de aplicaciones o iniciativas que comparten un objetivo común. Un proyecto puede contener múltiples bases de datos.

### **3. Database (Base de datos)**

- Una base de datos es un conjunto de colecciones. En MongoDB, cada base de datos tiene su propio espacio de nombres y puede tener diferentes colecciones y documentos. Las bases de datos permiten organizar los datos de manera lógica y separada por contexto.

### **4. Collection (Colección)**

- Una colección es un conjunto de documentos dentro de una base de datos. Se asemeja a las tablas en bases de datos relacionales, pero no requiere un esquema fijo. Las colecciones agrupan documentos que tienen características similares.
- Una **collection** en MongoDB es un conjunto de documentos. Es similar a una tabla en una base de datos relacional, pero no requiere un esquema fijo, lo que significa que los documentos dentro de una misma colección pueden tener diferentes estructuras. Esto permite una gran flexibilidad en la forma en que se almacenan y organizan los datos.

### **5. Document (Documento)**

- [MongoDB Docs: Documents](https://www.mongodb.com/docs/manual/core/document/?_ga=2.64483046.810066485.1665291537-836515500.1666025886)
- El documento es la unidad básica de almacenamiento en MongoDB. Se representa en formato JSON/BSON y puede contener datos en distintas formas. Cada documento dentro de una colección puede tener una estructura diferente.
- Un **document** es la unidad básica de datos en MongoDB y se representa como un objeto JSON (JavaScript Object Notation). Cada documento tiene un identificador único llamado `_id`, que se genera automáticamente a menos que se especifique uno. Los documentos pueden contener datos en cualquier formato, incluyendo arrays y otros documentos, lo que permite una estructura jerárquica compleja.

## Document Structure

- [MongoDB Docs: Documents](https://www.mongodb.com/docs/manual/core/document/?_ga=2.64483046.810066485.1665291537-836515500.1666025886)
- [MongoDB Docs: BSON Types](https://www.mongodb.com/docs/manual/reference/bson-types/?_ga=2.64483046.810066485.1665291537-836515500.1666025886)

The values in a document can be any data type, including strings, objects, arrays, booleans, nulls, dates, ObjectIds, and more. Here's the syntax for a MongoDB document, followed by an example:

Syntax:

```json
{
"key": value,
"key": value,
"key" : value
}

```

Example:

```json
{
"_id": 1,
"name": "AC3 Phone",
"colors" : ["black", "silver"],
"price" : 200,
"available" : true
}
```

## BSON (Binary JSON)

- [MongoDB Docs: BSON Types](https://www.mongodb.com/docs/manual/reference/bson-types/?_ga=2.64483046.810066485.1665291537-836515500.1666025886)
- [Explaining BSON with Examples](https://www.mongodb.com/basics/bson?_ga=2.64483046.810066485.1665291537-836515500.1666025886)
- [JSON and BSON](https://www.mongodb.com/json-and-bson?_ga=2.64483046.810066485.1665291537-836515500.1666025886)
- **BSON** es un formato binario que extiende JSON, ofreciendo soporte para más tipos de datos, eficiencia en almacenamiento y velocidad de procesamiento.
- MongoDB utiliza BSON para aprovechar estas ventajas, lo que le permite manejar datos complejos de manera efectiva y optimizar el rendimiento de la base de datos.

**BSON** (Binary JSON) es un formato de serialización de datos que es utilizado por MongoDB para almacenar documentos. Es una extensión de JSON (JavaScript Object Notation) que incluye algunas mejoras significativas, las cuales lo hacen más adecuado para su uso en bases de datos. A continuación, se detallan sus características y ventajas:

### Mejoras de BSON respecto a JSON

1. **Tipo de Datos Soportados**:
    - BSON admite más tipos de datos que JSON. Por ejemplo, BSON puede representar tipos como `Date`, `Binary`, `ObjectId`, y `Decimal128`, que no están disponibles en JSON.
2. **Eficiencia de Almacenamiento**:
    - Al ser un formato binario, BSON puede ser más eficiente en términos de espacio en comparación con la representación en texto de JSON. Esto se traduce en un uso más eficiente del almacenamiento en disco.
3. **Velocidad de Procesamiento**:
    - BSON es más rápido de analizar y serializar en comparación con JSON, ya que su estructura binaria permite un acceso más directo a los datos, reduciendo el tiempo de procesamiento.
4. **Estructura de Datos Compleja**:
    - Permite la inclusión de documentos anidados y arrays de forma más eficiente, lo que es útil para modelar datos complejos que se encuentran en aplicaciones modernas.
5. **Facilidad de Indexación**:
    - La estructura binaria de BSON facilita la creación de índices, lo que mejora las consultas y el rendimiento general de la base de datos, especialmente en conjuntos de datos grandes.

## Flexibilidad de Schema en MongoDB

- MongoDB permite un cambio de esquema muy flexible, donde los documentos en una colección pueden tener estructuras diferentes sin necesidad de modificar los registros existentes.
- Se pueden agregar validaciones para controlar la estructura de los documentos tanto en escritura como en lectura.
- MongoDB soporta polimorfismo, lo que permite almacenar diferentes tipos de documentos en una sola colección, facilitando la representación de datos complejos y variados.

Una de las características más destacadas de MongoDB es su flexibilidad en el manejo de esquemas (schemas). Esto permite a los desarrolladores adaptarse rápidamente a cambios en los requisitos de datos sin la necesidad de realizar modificaciones complicadas en los registros existentes. A continuación, se detallan algunas de las características relacionadas con la flexibilidad del esquema en MongoDB:

1. **Esquemas Dinámicos**:
    - Los documentos dentro de una misma colección pueden tener estructuras diferentes. Esto significa que puedes cambiar el modelo de datos sin afectar a los datos existentes. Si decides agregar nuevos campos o cambiar la estructura de los documentos, simplemente puedes empezar a insertar documentos con el nuevo esquema.
2. **Validación de Esquema**:
    - Aunque MongoDB permite una gran flexibilidad, también proporciona capacidades para validar documentos al ser insertados o actualizados. Puedes definir reglas de validación para asegurarte de que los documentos cumplan con ciertos criterios, lo que te permite mantener cierto nivel de control sobre la estructura de los datos.
3. **Polimorfismo**:
    - MongoDB soporta el polimorfismo, lo que significa que puedes almacenar diferentes tipos de documentos en una sola colección. Esto es útil en escenarios donde diferentes objetos pueden compartir algunas propiedades pero también tener sus propias características únicas. Por ejemplo, en una colección de "vehículos", podrías tener documentos que representen coches, camiones y motocicletas, cada uno con sus propias propiedades específicas, pero todos almacenados en la misma colección.

### Ejemplo de Polimorfismo

Supongamos que tienes una colección llamada `productos`, y deseas almacenar tanto `libros` como `revistas`:

```json
// Documento de un libro
{
  "tipo": "libro",
  "titulo": "El gran Gatsby",
  "autor": "F. Scott Fitzgerald",
  "paginas": 180
}

// Documento de una revista
{
  "tipo": "revista",
  "titulo": "National Geographic",
  "fecha": "2023-10",
  "numero": 5
}

```

En este caso, ambos documentos están en la misma colección, pero tienen estructuras diferentes que reflejan sus respectivas características.

### Beneficios de la Flexibilidad de Esquema

- **Agilidad en Desarrollo**: Los equipos pueden iterar rápidamente sobre los modelos de datos sin preocuparse por los costos asociados a la migración de datos.
- **Adaptabilidad**: La capacidad de cambiar el modelo de datos permite a las aplicaciones adaptarse a nuevas necesidades y requisitos de manera eficiente.
- **Facilidad de Uso**: Los desarrolladores pueden trabajar con una estructura de datos que se asemeje a los objetos en código, lo que simplifica la interacción con la base de datos.

## Fun Facts

- **Replica Sets:** Proporcionan alta disponibilidad y evitan el tiempo de inactividad en caso de desastres. Se componen de al menos **3 nodos** en MongoDB Atlas.
- **Ediciones para Empresas:** Se recomienda **Enterprise Advanced** y **Dedicated Atlas Clusters** para clientes empresariales.
- **Características Únicas:** MongoDB se destaca por su capacidad de ser **multi-nube**, poder **ejecutarse en-premise**, y tener **encriptación de campo a nivel de cliente**.
- **Tipos de Encriptación:** MongoDB soporta **encriptación en reposo**, **encriptación en movimiento (TLS/SSL)**, y **encriptación de campo a nivel de cliente**.
- **Pipelines y el Aggregation Framework:** Permiten filtrar y transformar datos en múltiples etapas, con documentos que fluyen a través de la tubería. Los resultados pueden ser persistidos en otras colecciones usando el operador **$out**.
- **Comando para Índice Único:** El comando para crear un índice único en el campo `author` de la colección `posts` es `db.posts.createIndex({"author":1 }, {"unique": true})`.
- **Cumplimiento de HIPAA:** MongoDB Atlas puede ser configurado para ser **HIPAA compliant**.
- **Auditoría de Base de Datos:** Permite a los administradores y usuarios rastrear la actividad del sistema en despliegues con múltiples usuarios y aplicaciones.

# Crear un Clúster

- [MongoDB Docs: Get Started with Atlas](https://www.mongodb.com/docs/atlas/getting-started/?_ga=2.56158050.810066485.1665291537-836515500.1666025886)
- [MongoDB Docs: Deploy a Free Cluster](https://www.mongodb.com/docs/atlas/tutorial/deploy-free-tier-cluster/?_ga=2.56158050.810066485.1665291537-836515500.1666025886)
- [MongoDB Docs: Load Sample Data](https://www.mongodb.com/docs/atlas/sample-data/?_ga=2.56158050.810066485.1665291537-836515500.1666025886)

## Desde terminal (AtlasCLI)

(Ya sea que la descargues o la encuentres en MongoDB Atlas)

[Download MongoDB Atlas CLI](https://www.mongodb.com/try/download/atlascli)

Puedes hacerlo desde MongoDB Atlas Terminal con:

```python
atlas setup --clusterName myAtlasClusterEDU --provider AWS --currentIp --skipSampleData --username myAtlasDBUser --password myatlas-001 --projectId 67d841c394204424add12f54    | tee atlas_cluster_details.txt
```

En caso de querer crear otro exactamente igual, y no te deje porque existen ese usuario y/o ese proyecto, bórralos y vuelve a crearlos con esto:

```python
atlas dbuser delete myAtlasDBUser --force
sleep 15
atlas setup --clusterName myAtlasClusterEDU --provider AWS --currentIp --skipSampleData --username myAtlasDBUser --password myatlas-001 --projectId 67d841c394204424add12f54  | tee atlas_cluster_details.txt
```

Y le ponemos Sample Data así:

```python
atlas clusters sampleData load myAtlasClusterEDU
```

Extra:

Busca ayuda así:

```python
db.help()
```

## Desde UI (MongoDB Atlas)

Es muy fácil.

[nosql_practice_test_1.pdf](attachment:f564e3d9-c513-4450-bacb-6a77c3481b6e:nosql_practice_test_1.pdf)

Y ya después puedes ver los documentos desde Atlas > Deployment > Database > Collections, y pues ya seleccionas la database, su collection, y filtras los documentos y la info mostrada si quieres.

Alternativamente, desde Data Services > Database > Clusters > vas al apartado de tu cluster > Browse Collections.

Desde esa misma interfaz puedes crear databases y collections, y meterle documentos

# Conexión

- [MongoDB Docs: Get Connection String](https://www.mongodb.com/docs/guides/atlas/connection-string/?_ga=2.2826361.818394043.1666026366-33697719.1666026366)
- [MongoDB Docs: Connection String URI Format](https://www.mongodb.com/docs/manual/reference/connection-string/)
- [MongoDB Docs: The MongoDB Shell](https://www.mongodb.com/docs/mongodb-shell/)
- [MongoDB Docs: MongoDB Compass](https://www.mongodb.com/products/compass/)
- [MongoDB Docs: Connect via Your Application](https://www.mongodb.com/docs/atlas/driver-connection/)
- [MongoDB Docs: Troubleshoot Connection Issues](https://www.mongodb.com/docs/atlas/troubleshoot-connection/)

---

[nosql_practice_test_1.pdf](attachment:f564e3d9-c513-4450-bacb-6a77c3481b6e:nosql_practice_test_1.pdf)

Desde la misma terminal (ya tuya) o MongoDB Atlas puedes hacerlo, aunque tienen aplicación de escritorio, se llama MongoDB Compass.

En cualquier caso, recuerda añadir tu IP en las IPs permitidas. Y desde Security > Network Access, podrías incluso permitir la conexión desde cualquier IP.

Y recuerda llenar el campo de `<password>` en la url, pendejo

## Desde terminal (MongoSH)

[MongoDB Shell Download](https://www.mongodb.com/try/download/shell)

Luego de descargarlo, puedes abrir tu CMD como normalmente, y buscar el string de conexión de tu clúster específico para mongo shell

El mío anterior se veía algo así (te pedirá entrar tu contraseña):

```bash
mongosh "mongodb+srv://myatlasclusteredu.oa4gf.mongodb.net/" --apiVersion 1 --username myAtlasDBUser
```

Y aquí hay otra forma de hacerlo

```bash
MY_ATLAS_CONNECTION_STRING=$(atlas clusters connectionStrings describe myAtlasClusterEDU | sed "1 d")
mongosh -u myAtlasDBUser -p myatlas-001 $MY_ATLAS_CONNECTION_STRING
```

Y pruebas su funcionamiento con

```jsx
 db.hello()
```

Curiosamente, desde un shell conectado a un clúster usando MongoSH, se puede correr código javascrypt REPL allí, como esto:

```jsx
const greetingArray = ["hello","world","welcome"];
const loopArray = (array) => array.forEach(el => console.log(el));
loopArray(greetingArray);
```

Es más, se supone que es un Node.js REPL enviroment, daaamn…

## Desde UI (MongoDB Compass)

[MongoDB Compass Download (GUI)](https://www.mongodb.com/try/download/compass)

Lo mismo, lo descargas, copias el string de conexión preparado para Compass, y le das en “Add New Connection” para pegarlo allí y ya

Desde allí, crear databases, collections y documents es super fácil e intuitivo, o al menos lo es desde la UI de Atlas

```bash
mongodb+srv://myAtlasDBUser:<db_password>@myatlasclusteredu.oa4gf.mongodb.net/
```

## Aplicaciones

[MongoDB Developer Center](https://www.mongodb.com/developer/)

[Build A Python Database With MongoDB](https://www.mongodb.com/resources/languages/python)

[MongoDB Courses and Trainings | MongoDB University](https://learn.mongodb.com/learning-paths/mongodb-python-developer-path)

[Start Developing with MongoDB](https://www.mongodb.com/docs/drivers/)

[MongoDB Python Drivers](https://www.mongodb.com/docs/drivers/python-drivers/)

# CRUD Operations

- [MongoDB Docs: Create, View, and Drop Databases](https://www.mongodb.com/docs/atlas/atlas-ui/databases/?_ga=2.64483046.810066485.1665291537-836515500.1666025886)
- [MongoDB Docs: Databases and Collections](https://www.mongodb.com/docs/manual/core/databases-and-collections/?_ga=2.97437654.810066485.1665291537-836515500.1666025886)
    
    [nosql_practice_test_1.pdf](attachment:f564e3d9-c513-4450-bacb-6a77c3481b6e:nosql_practice_test_1.pdf)
    

Y recuerda que puedes ver todos los ejercicios que hice de la otra vez., aquí:

[Courses-and-Certifications/05 - MongoDB - Practice at main · QuitoTactico/Courses-and-Certifications](https://github.com/QuitoTactico/Courses-and-Certifications/tree/main/05%20-%20MongoDB%20-%20Practice)

[Courses-and-Certifications/05 - MongoDB - Practice/restaurant_querys.ipynb at main · QuitoTactico/Courses-and-Certifications](https://github.com/QuitoTactico/Courses-and-Certifications/blob/main/05%20-%20MongoDB%20-%20Practice/restaurant_querys.ipynb)

## Insert and Find Documents

### Teoría

**CRUD** es un acrónimo que se refiere a las cuatro operaciones básicas que se pueden realizar en una base de datos:

- **C**reate (Crear)
- **R**ead (Leer)
- **U**pdate (Actualizar)
- **D**elete (Eliminar)

En MongoDB, los documentos se almacenan en colecciones, y cada documento es un objeto JSON (BSON).

### Práctica

### Instalación y Conexión

Para interactuar con MongoDB desde Python, necesitamos la biblioteca `pymongo`. Puedes instalarla usando:

```bash
pip install pymongo

```

Luego, puedes conectarte a tu base de datos de MongoDB:

```python
from pymongo import MongoClient

# Conexión a la base de datos
client = MongoClient('mongodb://localhost:27017/')
db = client['mi_base_de_datos']
collection = db['mi_coleccion']

```

### Insertar Documentos

Para insertar documentos en MongoDB, usamos el método `insert_one()` o `insert_many()`.

**Ejemplo de `insert_one()`**:

```python
# Insertar un solo documento
documento = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}

resultado = collection.insert_one(documento)
print(f'Documento insertado con ID: {resultado.inserted_id}')

```

**Ejemplo de `insert_many()`**:

```python
# Insertar múltiples documentos
documentos = [
    {"nombre": "Maria", "edad": 25, "ciudad": "Barcelona"},
    {"nombre": "Pedro", "edad": 28, "ciudad": "Valencia"}
]

resultado = collection.insert_many(documentos)
print(f'Documentos insertados con IDs: {resultado.inserted_ids}')

```

### Encontrar Documentos

Para leer documentos, usamos `find_one()` o `find()`.

**Ejemplo de `find_one()`**:

```python
# Encontrar un solo documento
documento = collection.find_one({"nombre": "Juan"})
print(documento)

```

**Ejemplo de `find()`**:

```python
# Encontrar múltiples documentos
resultados = collection.find({"edad": {"$gt": 25}})  # Edad mayor a 25
for doc in resultados:
    print(doc)

```

### Funciones Utilizadas

- `insert_one(document)`: Inserta un solo documento.
    - **Parámetros**: `document` (dict)
- `insert_many(documents)`: Inserta múltiples documentos.
    - **Parámetros**: `documents` (list of dicts)
- `find_one(query)`: Encuentra un solo documento que coincida con la consulta.
    - **Parámetros**: `query` (dict)
- `find(query)`: Encuentra todos los documentos que coincidan con la consulta.
    - **Parámetros**: `query` (dict)

## Replace and Delete Documents

### Teoría

Además de insertar y leer documentos, es crucial poder reemplazar y eliminar documentos en MongoDB.

### Práctica

### Reemplazar Documentos

Para reemplazar un documento, usamos el método `replace_one()`.

**Ejemplo de `replace_one()`**:

```python
# Reemplazar un documento
result = collection.replace_one({"nombre": "Juan"}, {"nombre": "Juan", "edad": 31, "ciudad": "Madrid"})
print(f'Documentos modificados: {result.modified_count}')

```

### Eliminar Documentos

Para eliminar documentos, usamos `delete_one()` o `delete_many()`.

**Ejemplo de `delete_one()`**:

```python
# Eliminar un solo documento
resultado = collection.delete_one({"nombre": "Juan"})
print(f'Documentos eliminados: {resultado.deleted_count}')

```

**Ejemplo de `delete_many()`**:

```python
# Eliminar múltiples documentos
resultado = collection.delete_many({"edad": {"$lt": 30}})  # Edad menor a 30
print(f'Documentos eliminados: {resultado.deleted_count}')

```

### Funciones Utilizadas

- `replace_one(filter, replacement)`: Reemplaza un documento que coincide con el filtro.
    - **Parámetros**:
        - `filter` (dict)
        - `replacement` (dict)
- `delete_one(filter)`: Elimina un solo documento que coincide con el filtro.
    - **Parámetros**: `filter` (dict)
- `delete_many(filter)`: Elimina múltiples documentos que coinciden con el filtro.
    - **Parámetros**: `filter` (dict)

## Modifying Query Results

### Teoría

Modificar los resultados de las consultas puede incluir ordenar, limitar y contar documentos.

### Práctica

### Ordenar Documentos

Utilizamos el método `sort()` para ordenar los resultados.

**Ejemplo de `sort()`**:

```python
# Ordenar documentos por edad
resultados = collection.find().sort("edad", 1)  # 1 para ascendente, -1 para descendente
for doc in resultados:
    print(doc)

```

### Limitar Documentos

Usamos el método `limit()` para limitar la cantidad de documentos retornados.

**Ejemplo de `limit()`**:

```python
# Limitar los resultados
resultados = collection.find().limit(2)
for doc in resultados:
    print(doc)

```

### Contar Documentos

El método `count_documents()` se utiliza para contar documentos que coinciden con una consulta.

**Ejemplo de `count_documents()`**:

```python
# Contar documentos
cantidad = collection.count_documents({"edad": {"$gt": 25}})
print(f'Cantidad de documentos con edad mayor a 25: {cantidad}')

```

### Funciones Utilizadas

- `sort(key_or_list, direction)`: Ordena los resultados de la consulta.
    - **Parámetros**:
        - `key_or_list` (str o list)
        - `direction` (1 para ascendente, -1 para descendente)
- `limit(n)`: Limita la cantidad de documentos retornados.
    - **Parámetros**: `n` (int)
- `count_documents(filter)`: Cuenta documentos que coinciden con el filtro.
    - **Parámetros**: `filter` (dict)

## Aggregations

https://www.mongodb.com/docs/v4.4/aggregation/#aggregation

https://www.mongodb.com/docs/manual/#aggregate-your-data

https://www.mongodb.com/docs/atlas/atlas-ui/agg-pipeline/#run-aggregation-pipelines

https://www.mongodb.com/docs/manual/core/aggregation-pipeline/

https://www.mongodb.com/docs/v4.4/aggregation/#aggregation

### Teoría

La **agregación** en MongoDB permite realizar operaciones más complejas sobre los datos, como agrupaciones y transformaciones.

### Práctica

### Agregación Básica

Utilizamos el método `aggregate()`, que toma una lista de etapas (stages) de agregación.

**Ejemplo de `aggregate()`**:

```python
# Agrupar documentos por ciudad y contar
pipeline = [
    {"$group": {"_id": "$ciudad", "total": {"$sum": 1}}}
]

resultados = collection.aggregate(pipeline)
for doc in resultados:
    print(doc)

```

### Filtrar y Agrupar

Podemos combinar etapas de filtrado y agrupamiento.

**Ejemplo**:

```python
# Filtrar y luego agrupar
pipeline = [
    {"$match": {"edad": {"$gt": 25}}},
    {"$group": {"_id": "$ciudad", "total": {"$sum": 1}}}
]

resultados = collection.aggregate(pipeline)
for doc in resultados:
    print(doc)

```

**Ejemplo 2:**

![image.png](attachment:8753995c-cd8a-4470-af96-ea2f7cdff25a:image.png)

### Todas las demás funciones

- `$match`: Filtra documentos.
- `$group`: Agrupa documentos y realiza cálculos.
- `$sort`: Ordena documentos.
- `$project`: Modifica la forma de los documentos.
- `$limit`: Limita el número de documentos.
- `$skip`: Omite un número de documentos.
- `$unwind`: Descompone arrays.
- `$lookup`: Realiza uniones entre colecciones.
- `$addFields`: Agrega nuevos campos.
- `$set`: Actualiza o agrega campos.
- `$replaceRoot`: Reemplaza el documento raíz.
- `$count`: Cuenta documentos.
- `$facet`: Realiza múltiples agregaciones en paralelo.
- `$bucket`: Agrupa documentos en rangos.
- `$bucketAuto`: Agrupación automática.
- `$geoNear`: Consulta geoespacial.

![image.png](attachment:f074aa66-ccb7-421e-8e93-0d4302c8fdb6:image.png)

1. **$match**
    - Filtra los documentos para pasar solo aquellos que coinciden con las condiciones especificadas.
    - **Ejemplo**:
        
        ```python
        {"$match": {"edad": {"$gt": 25}}}
        
        ```
        
2. **$group**
    - Agrupa documentos por un campo específico y permite realizar operaciones de agregación como `sum`, `avg`, `count`, etc.
    - **Ejemplo**:
        
        ```python
        {"$group": {"_id": "$ciudad", "total": {"$sum": 1}}}
        
        ```
        
3. **$sort**
    - Ordena los documentos en el resultado de la agregación según uno o más campos.
    - **Ejemplo**:
        
        ```python
        {"$sort": {"edad": 1}}  # Ascendente
        
        ```
        
4. **$project**
    - Modifica los documentos en la etapa de salida, permitiendo incluir, excluir o añadir nuevos campos.
    - **Ejemplo**:
        
        ```python
        {"$project": {"nombre": 1, "edad": 1, "ciudad": 1}}  # Incluye solo los campos nombre, edad y ciudad
        
        ```
        
5. **$limit**
    - Restringe el número de documentos en el resultado a un número específico.
    - **Ejemplo**:
        
        ```python
        {"$limit": 5}
        
        ```
        
6. **$skip**
    - Omite el número especificado de documentos en el resultado.
    - **Ejemplo**:
        
        ```python
        {"$skip": 2}
        
        ```
        
7. **$unwind**
    - Descompone un array en documentos individuales, creando un documento separado para cada elemento del array.
    - **Ejemplo**:
        
        ```python
        {"$unwind": "$intereses"}
        
        ```
        
8. **$lookup**
    - Realiza una unión (join) entre dos colecciones, permitiendo combinar documentos de diferentes colecciones.
    - **Ejemplo**:
        
        ```python
        {
            "$lookup": {
                "from": "otra_coleccion",
                "localField": "campo_local",
                "foreignField": "campo_extranjero",
                "as": "resultado"
            }
        }
        
        ```
        
9. **$addFields**
    - Agrega nuevos campos a los documentos, basados en los valores existentes.
    - **Ejemplo**:
        
        ```python
        {"$addFields": {"nuevoCampo": {"$multiply": ["$edad", 2]}}}
        
        ```
        
10. **$set**
    - Similar a `$addFields`, permite agregar o actualizar campos existentes en los documentos.
    - **Ejemplo**:
        
        ```python
        {"$set": {"edad": 30}}
        
        ```
        
11. **$replaceRoot**
    - Reemplaza el documento raíz con un nuevo documento.
    - **Ejemplo**:
        
        ```python
        {"$replaceRoot": {"newRoot": "$direccion"}}
        
        ```
        
12. **$count**
    - Cuenta el número de documentos que pasan a través de la etapa de agregación y devuelve ese número como un documento.
    - **Ejemplo**:
        
        ```python
        {"$count": "total"}
        
        ```
        
13. **$facet**
    - Permite realizar múltiples agregaciones en paralelo en un solo conjunto de documentos.
    - **Ejemplo**:
        
        ```python
        {
            "$facet": {
                "total": [{"$count": "total"}],
                "porCiudad": [{"$group": {"_id": "$ciudad", "total": {"$sum": 1}}}]
            }
        }
        
        ```
        
14. **$bucket**
    - Agrupa documentos en rangos de valores, útiles para crear histogramas.
    - **Ejemplo**:
        
        ```python
        {
            "$bucket": {
                "groupBy": "$edad",
                "boundaries": [0, 20, 30, 40, 50],
                "default": "Otro",
                "output": {
                    "count": {"$sum": 1}
                }
            }
        }
        
        ```
        
15. **$bucketAuto**
    - Similar a `$bucket`, pero automáticamente determina los límites de los grupos en función de la distribución de los datos.
    - **Ejemplo**:
        
        ```python
        {
            "$bucketAuto": {
                "groupBy": "$edad",
                "buckets": 5
            }
        }
        
        ```
        
16. **$geoNear**
    - Proporciona una forma de realizar consultas geoespaciales para encontrar documentos cercanos a un punto geográfico.
    - **Ejemplo**:
        
        ```python
        {
            "$geoNear": {
                "near": {"type": "Point", "coordinates": [0, 0]},
                "distanceField": "distancia",
                "spherical": True
            }
        }
        
        ```
        

## Data Modeling

https://www.mongodb.com/docs/v4.4/core/data-modeling-introduction/#data-modeling-introduction

https://www.mongodb.com/docs/v4.4/core/data-modeling-introduction/#data-modeling-introduction

# MongoDB Indexes

https://www.mongodb.com/docs/v4.4/indexes/#indexes

https://www.mongodb.com/docs/v4.4/indexes/#indexes

### Teoría

Los índices en MongoDB mejoran el rendimiento de las consultas al permitir acceder a los documentos más rápidamente.

### Práctica

### Crear un Índice

Usamos el método `create_index()` para crear índices.

**Ejemplo de `create_index()`**:

```python
# Crear un índice en el campo "edad"
collection.create_index([("edad", 1)])  # 1 para ascendente, -1 para descendente

```

```jsx
# En mongoSH
db.posts.createIndex({"author":1 }, {"unique": true})
```

### Listar Índices

Podemos listar los índices actuales en la colección.

**Ejemplo de `list_indexes()`**:

```python
# Listar índices
for indice in collection.list_indexes():
    print(indice)

```

### Eliminar un Índice

Utilizamos `drop_index()` para eliminar un índice.

**Ejemplo de `drop_index()`**:

```python
# Eliminar un índice
collection.drop_index("edad_1")

```

### Funciones Utilizadas

- `create_index(keys, **kwargs)`: Crea un índice en la colección.
    - **Parámetros**:
        - `keys` (list)
        - `*kwargs` (opciones adicionales)
- `list_indexes()`: Lista todos los índices en la colección.
- `drop_index(index_name)`: Elimina un índice específico.
    - **Parámetros**: `index_name` (str)

# MongoDB Atlas Search

### Teoría

MongoDB Atlas Search proporciona capacidades de búsqueda de texto completo, combinando características de base de datos y motor de búsqueda.

### Práctica

Para utilizar Atlas Search, asegúrate de tener un clúster de MongoDB Atlas y habilitar Atlas Search en tu colección.

### Búsqueda de Texto Completo

Utilizamos `aggregate()` con `$search`.

**Ejemplo de búsqueda**:

```python
pipeline = [
    {
        "$search": {
            "text": {
                "query": "Madrid",
                "path": "ciudad"
            }
        }
    }
]

resultados = collection.aggregate(pipeline)
for doc in resultados:
    print(doc)

```

### Funciones Utilizadas

- `aggregate(pipeline)`: Realiza operaciones de agregación que incluyen búsquedas.
    - **Parámetros**: `pipeline` (list)

# MongoDB Data Modeling Intro

### Teoría

El modelado de datos implica definir cómo se almacena y relaciona la información en la base de datos.

### Práctica

### Ejemplo de Modelado

Supongamos que estamos modelando una base de datos para una biblioteca:

```python
# Colección de libros
libros = [
    {
        "titulo": "El gran Gatsby",
        "autor": {"nombre": "F. Scott Fitzgerald", "nacionalidad": "EE.UU."},
        "genero": "Ficción",
        "anio_publicacion": 1925
    },
    {
        "titulo": "Cien años de soledad",
        "autor": {"nombre": "Gabriel García Márquez", "nacionalidad": "Colombia"},
        "genero": "Ficción",
        "anio_publicacion": 1967
    }
]

collection.insert_many(libros)

```

### Funciones Utilizadas

- `insert_many(documents)`: Inserta múltiples documentos.
    - **Parámetros**: `documents` (list of dicts)

# MongoDB Transactions

### Teoría

Las transacciones en MongoDB garantizan que un conjunto de operaciones se realice de manera atómica, asegurando la integridad de los datos.

### Práctica

### Uso de Transacciones

Para utilizar transacciones, debes iniciar una sesión.

**Ejemplo de transacción**:

```python
with client.start_session() as session:
    with session.start_transaction():
        collection.insert_one({"nombre": "Ana", "edad": 29, "ciudad": "Sevilla"}, session=session)
        collection.insert_one({"nombre": "Luis", "edad": 35, "ciudad": "Bilbao"}, session=session)

```

### Funciones Utilizadas

- `start_session()`: Inicia una nueva sesión.
- `start_transaction()`: Inicia una nueva transacción dentro de una sesión.
- `insert_one(document, session)`: Inserta un documento dentro de una transacción.
    - **Parámetros**:
        - `document` (dict)
        - `session` (Session object)

# ACID

**ACID** es un acrónimo que representa las cuatro propiedades fundamentales que garantizan la confiabilidad de las transacciones en bases de datos. Estas propiedades son:

1. **Atomicidad (Atomicity)**:
    - Una transacción se considera como una unidad indivisible. Esto significa que o bien se ejecuta en su totalidad o no se ejecuta en absoluto. Si alguna parte de la transacción falla, todos los cambios realizados se revierten, dejando la base de datos en su estado original.
2. **Consistencia (Consistency)**:
    - Las transacciones deben llevar a la base de datos de un estado válido a otro estado válido. Esto implica que cualquier regla de integridad definida en la base de datos debe cumplirse después de que se complete la transacción. Si una transacción provoca un estado inconsistente, no se permite que se complete.
3. **Aislamiento (Isolation)**:
    - Las transacciones concurrentes deben ejecutarse de forma que no interfieran entre sí. Esto significa que el resultado de una transacción no debe ser visible para otras transacciones hasta que se haya completado. Esto ayuda a evitar problemas como lecturas sucias, lecturas no repetibles y fantasmas.
4. **Durabilidad (Durability)**:
    - Una vez que una transacción ha sido confirmada (committed), sus cambios son permanentes y persistentes, incluso en caso de fallos del sistema, como un corte de energía. Esto se logra generalmente a través de técnicas de registro en disco que garantizan que los datos no se pierdan.

### ACID en MongoDB

MongoDB, como base de datos NoSQL, tiene un enfoque diferente en comparación con las bases de datos relacionales tradicionales en términos de ACID:

- **Atomicidad**:
    - MongoDB garantiza la atomicidad a nivel de documento. Esto significa que las operaciones de escritura en un único documento son atómicas. Sin embargo, para transacciones que abarcan múltiples documentos o colecciones, MongoDB introdujo soporte para transacciones multi-documento a partir de la versión 4.0, permitiendo así que varias operaciones se realicen de manera atómica.
- **Consistencia**:
    - MongoDB proporciona consistencia a nivel de documento. La validación de esquemas y las reglas de integridad pueden implementarse para ayudar a mantener la consistencia de los datos.
- **Aislamiento**:
    - El aislamiento se logra en MongoDB a través del uso de transacciones, donde las operaciones dentro de una transacción no son visibles para otras hasta que se completan. Esto garantiza que las operaciones simultáneas no interfieran entre sí.
- **Durabilidad**:
    - MongoDB utiliza un sistema de registro en disco (Write Ahead Logging) para asegurarse de que los cambios sean duraderos. Los datos se escriben en el disco antes de que se confirme la transacción, lo que garantiza que no se pierdan en caso de fallo.

### Conclusión

- **ACID** es fundamental para garantizar la integridad y confiabilidad de las transacciones en bases de datos.
- Aunque MongoDB tiene un enfoque diferente debido a su naturaleza NoSQL, ha implementado características que permiten cumplir con las propiedades ACID, especialmente con la introducción de transacciones multi-documento.
- La comprensión de ACID es crucial para el diseño y la implementación de aplicaciones que dependen de la integridad de los datos.

# Documentación Extra

https://www.mongodb.com/docs/

https://www.mongodb.com/docs/

- BI connector
- Charts
- Open Service Broker
- k8s Operator
- Kafka connector
- Preferred driver/s
- Peruse for awareness of other sections in server documents, like transactions, change streams, sharding, replication, security, and storage.
