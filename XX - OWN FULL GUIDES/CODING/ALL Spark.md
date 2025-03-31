# Sources

- (FREE COURSE) https://www.udemy.com/course/sparkstarterkit
- (LISTA DE REPRODUCCIÓN) https://www.youtube.com/playlist?list=PLYFBiuYObvKB_k0bnkI41biMjD12t44GN
- (CURSO PAGO DE UDEMY) http://globant.udemy.com/course/taming-big-data-with-apache-spark-hands-on/

# Apache Spark vs Hadoop MapReduce

- Hadoop para almacenar cosas tiene HDFS (Hadoop Distributed File System), mientras que Spark no puede almacenar esas grandes cantidades de datos, le toca agarrar los datos de un almacenamiento distribuido como HDFS, una solución en la nube como S3, o bases de datos de big data como HBase o Cassandra, y quizás dejar la solución allá mismo.
- Hadoop tiene su propia wea que ayuda en el procesamiento de datos, Hadoop MapReduce, que es una implementación del modelo/estrategia/concepto de programación MapReduce, hecho por Google, para el mismo fin de procesar datos en clusters. Spark también usa el modelo/estrategia/concepto MapReduce, pero lo implementó a su forma, una mucho más rápida
- Spark es desde 10 a 100 veces más rápido que Hadoop MapReduce, el ejemplo de 100x fue en el caso de regresión logística (usado en ML), pero en los demás casos tradicionales pues sí parece 10x más rapido. Es porque spark usa ram distribuída, mientras hadoop hace todo desde y hacia disco
- Hadoop necesita acceder a los recursos de computación por medio de YARN, mientras Spark tiene ese resource manager integrado

![image.png](attachment:ca8c4058-5da0-4218-9412-194012ef2170:image.png)

Spark NO es un reemplazo de Hadoop. Tú podrías sacar tus datos de un HDFS y tener como gestor de recursos a YARN (si quieres), y así tus datos guardados tendrían un poder de computación mucho mayor, en una herramienta especializada

## Gestor de Recursos

En el ecosistema de Big Data, tanto Hadoop como Spark utilizan diferentes modelos de gestión de recursos, aunque hay una interrelación entre ellos. A continuación, se describen las diferencias clave en la gestión de recursos entre Hadoop y Spark:

| Característica | Hadoop (YARN) | Spark |
| --- | --- | --- |
| Sistema de Gestión | YARN | YARN, Standalone, Mesos, Kubernetes |
| Componentes | ResourceManager, NodeManager, ApplicationMaster | Master, Worker, Driver |
| Enfoque de Procesamiento | Basado en disco (MapReduce) | En memoria (RDD) |
| Eficiencia | Menos eficiente en cargas de trabajo iterativas | Más eficiente en cargas iterativas |
| Escalabilidad | Alta | Alta |

### Hadoop Resource Manager (YARN)

1. **Arquitectura**:
    - Hadoop utiliza YARN (Yet Another Resource Negotiator) como su sistema de gestión de recursos. YARN separa la gestión de recursos de la ejecución de tareas, lo que permite que múltiples aplicaciones se ejecuten en el mismo clúster.
2. **Componentes**:
    - **ResourceManager**: Es el componente maestro que gestiona los recursos del clúster y coordina la ejecución de aplicaciones.
    - **NodeManager**: Es el componente que se ejecuta en cada nodo del clúster y se encarga de la gestión de recursos en ese nodo específico.
    - **ApplicationMaster**: Se encarga de gestionar la ejecución de una sola aplicación dentro del clúster.
3. **Funcionalidad**:
    - YARN permite a diferentes frameworks de procesamiento (como MapReduce, Spark, Tez, etc.) compartir recursos y ejecutarse de manera más eficiente en un entorno de clúster.
4. **Escalabilidad**:
    - YARN está diseñado para escalar a miles de nodos y es capaz de manejar grandes volúmenes de datos.

### Spark Resource Manager

1. **Arquitectura**:
    - Apache Spark puede ejecutarse en varios modos de gestión de recursos, incluido YARN, pero también puede usar su propio gestor de recursos llamado **Standalone Cluster Manager**, así como otros como **Mesos** y **Kubernetes**.
2. **Componentes**:
    - Al ejecutar Spark en modo YARN, utiliza el mismo ResourceManager y NodeManager de YARN. Sin embargo, cuando se ejecuta en su modo standalone, Spark tiene su propio **Master** que actúa como el gestor de recursos.
3. **Funcionalidad**:
    - Spark gestiona la distribución de datos y la ejecución de tareas en paralelo, aprovechando la memoria de manera más eficiente.
    - Spark tiene su propio concepto de **Resilient Distributed Datasets (RDD)** que permite un procesamiento en memoria, lo que mejora significativamente el rendimiento en comparación con el enfoque basado en disco tradicional de Hadoop MapReduce.
4. **Escalabilidad**:
    - Al igual que YARN, Spark también puede escalar a grandes clústeres, pero su capacidad para gestionar tareas en memoria puede ofrecer mejoras de rendimiento en ciertas cargas de trabajo.

### Conclusión

En resumen, tanto Hadoop como Spark tienen sus propios sistemas de gestión de recursos que permiten ejecutar aplicaciones en clústeres. YARN es el principal gestor de recursos utilizado en Hadoop, mientras que Spark puede utilizar YARN o su propio gestor. La elección entre estos sistemas dependerá de las necesidades específicas de procesamiento y los tipos de cargas de trabajo.

# Por qué existe esta vrg?

La idea de crear Spark, era reemplazar la implementación de MapReduce que tenía Hadoop. Hadoop hizo un buen trabajo en dar una primera solución a este procesamiento de datos, y una buenísima solución a lo del almacenamiento distribuido confiable, pero su procesamiento podía mejorar, para eso se creó la herramienta especializada spark.

## MapReduce?

- Los **Map** son filtros, wheres.
- Los **Reducers** parecen funciones de agregación. Agrupan y sacan un resultado
- También existe **Shuffle**, en donde se hace producto cartesiano entre las particiones.

## Problemas/Ineficiencias que intenta solucionar

### Iterative machine learning

Se trata de aplicar una serie de instrucciones, o un mapReduce job múltiples veces, para obtener el resultado

Procesamiento de grafos, page ranking y logical regression son problemas que necesitan iterative machine learning

- El caso es que, en Hadoop, cada resultado de iteración debe de ser guardado en el HDFS, para luego ser recogido de allí y volver a procesarlo, y volver a guardarlo. Cada output intermedio se guardaba, y eso es super sub-óptimo.
- Spark guarda los outputs intermedios en memoria ram!, y así es más fácil volver a sacar las cosas, las variables se guardan en ram, cosa mucho más rápida de usar luego, está cercano al procesador.

### Interactive data mining

Imagina que amazon implementó 8 mejoras en su página, y resulta que las ventas subieron un 10%, ahora tienes que buscar cuál de las 8 mejoras fué la que subió las ventas. Harás una comparación de antes-después en cada una de las partes del proceso de compra, o en cada cosa que se supone que debió mejorar cierto cambio en la página, y seguir comparando datasets dependiendo del resultado de la comparación pasada, para ver si esta comparación actual fué la que marcó la diferencia.

El problema en sí es que debes comparar datasets, y cambiar de datasets o seguir las comparaciones según los resultados anteriores. Necesitas MUCHAS funciones, algo específicas. 

- En el MapReduce tradicional de Hadoop, necesitas meter tus funciones en una lógica de mappers y reducers, y sientes que eso pues te dificulta todo y te limita
- En spark sigues haciéndolo, pero spark también da operadores para meterle a los datos y transformarlos, y no tienes que meter tu lógica en mappers y reducers, Spark lo hace por tí. La velocidad de Spark también lo hace mejor. Y como hay tantos resultados intermedios según los que se sigue procesando, a veces se usan muchas veces, y pues es mejor tenerlos en memoria, cosa que ya hace spark.

## How!?

### Ram distribuida

Esta vaina, además de poder usar ram (que hadoop no puede, sólo usa disco) usa la ram de todos los nodos, o sea, ram distribuida. Y eso es increíblemente difícil, por los problemas de consistencia y resiliencia, el paralelismo ta complejo.

Bueno, se parte el dataset en bloques, y cada parte del plan, cuando se va a ejecutar, se llama Job. Cada bloque se pasará por medio del job, en un nodo diferente. Ese job ejecutado en un nodo se llama task. `Blocks * Jobs = Tasks`.

![image.png](attachment:7c06fbea-45ed-442b-b7c2-6f0433ec4378:image.png)

El nodo que sigue en el siguiente procesamiento de ese bloque, necesita leer directamente de la ram del nodo que lo procesó anteriormente, así que ese nodo NECESITA seguir vivo. En Hadoop no tenían ese problema pues porque guardaban cada resultado intermedio en disco.

Este flujo de tareas y resultados se llama lineage.

![image.png](attachment:4f603cf3-438a-43cb-9f68-a48ebab78c68:image.png)

Si Sam se muere, Riley no podrá saber el resultado anterior. Pero nosotros tenemos guardada la operación que cada nodo tiene que hacer, tenemos las tasks, así que podemos reasignarle esa task a alguien más si es que Sam no responde.

RDD es lo que guarda registro de esas tasks y modificaciones que le haces a tu dataset, para así ser capaces de reasignar, o de volver atrás.

![image.png](attachment:b41edbdb-72b2-47e6-9649-ca8a7627d06f:image.png)

### DAG execution engine (**Directed Acyclic Graph**)

Spark no ejecuta todo lo que le va llegando de una, sino queva a ver tooodas las instrucciones que le diste, y luego hace un plan lógico (ram), desde este plan hace el físico (disco), y luego ejecuta las tareas en múltiples nodos del cluster.

Qué es DAG?, **Directed Acyclic Graph,** is a data structure that represents the logical execution plan of a Spark job, showing the sequence of transformations and actions needed to process data, ensuring no cycles or loops in the data flow. 

Spark transforma los comandos del usuario, en este modelo de ejecución, la idea es hacer tasks de una forma secuencial, una tras otra, pero asegurando que no hayan ciclos entre estas tasks.

Hadoop no tiene idea de lo que haces, no hace ningún pre-procesamiento, y por eso no hay ninguna optimización

![image.png](attachment:50a3ccc4-e775-4a12-81ee-5213f6a98de5:image.png)

### RDD (Resilient Distributed Datasets)

1. **`LIST OF PARTITIONS`**: Un RDD es una lista de particiones Es la operación de un paso intermedio, guardado distribuidamente. Pero no se guarda el resultado (como si fuera una variable), se está guardando son las operaciones, el procedimiento necesario. Cada vez que se ejecute una función, aunque ya se haya ejecutado antes, se volá a ejecutar, no hay data en caché, sino más bien operaciones en caché.
2. **`COMPUTE FUNCTION`**: Un RDD sabe qué función se usó para ser creada, y en qué RDD o dataset inicial fue aplicada
3. **`LIST OF DEPENDENCIES`**: Un RDD tiene una lista de dependencias. Cada partición depende de otra. Así que un RDD debe de saber de qué otros RDDs depende.

Ese es el core de spark. Sin RDD spark no tendría información suficiente sobre las operaciones, y no podría hacer los planes pa nada.

Si quieres transformar o modificar de alguna forma tu dataset, pues usas funciones de spark. Cuando lo haces, spark crea por debajo un RDD, para mantener registro de tus acciones en el dataset. 

RDD es el resultado intermedio, es la variable que creas, distribuida alrededor de las particiones en las que se guarde eso.

Así sabrá todo lo que intentas hacer, las tasks, y así puede reemplazar nodos que fallen como vimos antes, simplemente reasignando la task a alguien más. RDD recuerda las operaciones o transformaciones que le has hecho o intentado hacer a tu dataset, para así ser capaz de volver atrás

![image.png](attachment:4031451b-e6a5-4d34-855e-ff37ef658081:image.png)

![image.png](attachment:6e789b83-9ea1-42fd-9be3-7f46d2585bb2:image.png)

Según el ejemplo de arriba, ¿¿“errors” es RDD (resilient distrobuted dataset)?? 

En caso de que partition 2 de errors se muriera, ¿podríamos recuperarlo?

Sí y sí!, claro!!, porque sabemos exactamente cómo se creó. Simplemente aplicamos filter() en el partition 2 de logfile, y tendremos partition 2 de errors de nuevo, quizás haciendo este procedimiento en un nodo diferente.

Aquí, todos esos pasos intermedios u “operaciones para conseguir las variables” son RDDs, y el contenido está distribuido en varias particiones. Un RDD es una lista de particiones, la función que se usó para crearse, y una lista de RDDs de los que depende para ser creado.

![image.png](attachment:20d47463-bfdd-41ac-b832-fabe888014c1:image.png)

Es imposible cambiar los integrantes o particiones de un RDD, son inmutables, siempre tendrás que crear uno nuevo.

Los RDDs normalmente y de forma default están guardados en memoria, pero tmb pueden estar en disco si eso elijes.

Verás, un RDD y las gráficas que hemos hecho sólo ilustran el plan lógico, no el plan físico de cómo se van a ejecutar y guardar las cosas. En este mismo caso, tener esos RDDs intermedios es muy poco óptimo tanto en memoria como en computación, así que ese lineage no es lo que se ejecutará realmente, sólo es una gráfica. Spark por debajo optimiza esto para no tener que guardar esas 2 TB, 1 TB, y 10 computaciones de nodo intermedias, ya que no son requeridas por un segundo RDD.

![image.png](attachment:653bc415-211e-4b55-aefd-a306e4d1f5dc:image.png)

Realmente es así en este caso, hará cada partición de principio a fin en el mismo nodo, y no necesariamente guardará cada paso intermedio en un RDD, sino que puede juntar dos operaciones, si es que el paso medio entre ambas operaciones no es usado en ninguna otra parte.

![image.png](attachment:95ff78a6-f086-47f3-84c6-d5917c4ceba8:image.png)

### Spark Architecture

Todo está diseñado con la velocidad en mente, y aunque la idea es poder simplemente acomodar tasks en nodos diferentes, encima le mete computación en memoria y de manera pre-procesada para poder hacerlo de la forma más óptima.

# Installing Everything

https://www.youtube.com/watch?v=wt2wM8C2SXA

https://www.youtube.com/watch?v=wt2wM8C2SXA

Asegúrate de ver todo el fokin video atentamente, es absolutamente necesario. Acá descargan java, hadoop y spark, y hacen una carpeta para hive

## Darle permisos a Hive

El comando que se debe correr en `C:\winutils\bin>` desde un CMD con **PERMISOS DE ADMINISTRADOR**, es:

```bash
cd C:\winutils\bin
winutils chmod 777 C:\tmp\hive
```

### Troubleshooting

Si te sale un error tipo `"MSVCR100.dll no encontrado"`, descarga visual C++ (versión nueva, y también la 2010, ambas x64) de aquí: https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170

- **Visual Studio 2015, 2017, 2019, and 2022**: https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170#visual-studio-2015-2017-2019-and-2022
- **Visual Studio 2010 (VC++ 10.0) SP1 (no longer supported):** https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170#visual-studio-2010-vc-100-sp1-no-longer-supported

## Probar Spark Shell

Ve a donde tengas el bin de tu Spark, y pon

```bash
cd C:\spark-3.5.5-bin-hadoop3\bin
spark-shell
```

Y te saldrá tanto el logo de Spark en ascii, como un REPL de Scala, con eso comprobamos que nuestro Spark funciona

### Troubleshooting

Spark normalmente es compatible con versiones de java tipo Java 8 u Java 11, así que usa esas. Yo tenía Java 23, la nuevísima.

Descarga el JDK.

- https://www.oracle.com/co/java/technologies/javase/javase8-archive-downloads.html
- https://www.oracle.com/co/java/technologies/javase/javase8u211-later-archive-downloads.html

## Librerías python necesarias

```bash
pip install pyspark findspark jupyter
```

## Uso de Spark en Jupyter Notebooks

Crea un notebook ya sea usando

```bash
jupyter notebook
```

O VSC, y pon:

```python
import findspark
findspark.init()
# ---
from pyspark.sql import SparkSession
# ---
spark = SparkSession.builder.getOrCreate()
# ---
spark
```

Y te debería de salir esto:

```
SparkSession - in-memory

SparkContext

Spark UI

Version
v3.5.5
Master
local[*]
AppName
pyspark-shell
```

# Enviroment Setup (Deprecated)

## Java and Python Versions

In the next lecture, we'll walk through getting your development environment set up for Apache Spark.

Some of our newer lectures feature new capabilities in Apache Spark 4. You will want to install the [Apache Spark 4.0 preview 2](https://archive.apache.org/dist/spark/spark-4.0.0-preview2/) release or newer, if possible. But most lectures will work fine with Spark 3.5.5.

DO NOT install the latest Java version (21, 22, or newer) if you need to install a JDK on your system.

**Apache Spark 3.x is only compatible with Java 8, Java 11, or Java 17, and Apache Spark 4 is only compatible with Java 17.**

Furthermore, Spark is not compatible with Python 3.12 or newer as of this writing. **Before running pyspark in the next lecture, you must create and activate a Python 3.10 environment, like this:**

`1. conda create -n py310 python=3.10
2. conda activate py310`

1. 1. conda create -n py310 python=3.10
2. 2. conda activate py310

That must be run from your Anaconda prompt, after installing Anaconda. The setup lecture will illustrate this.

Remember to activate your py310 environment prior to running any code in the course.

# A programar pa

## Primer Ejemplo

```scala
--Max volume stocks
val stocks = sc.textFile("/user/osboxes/stocks-dataset")
val splits = stocks.map(record => record.split(","))
val symvol = splits.map(arr => (arr(1), arr(7).toInt))
val maxvol = symvol.reduceByKey((vol1, vol2) => Math.max(vol1, vol2))
maxvol.collect().foreach(println)
```

![image.png](attachment:4fa63bab-4c18-4c83-bd4a-25f03d2515e6:image.png)

La última parte, para sacar el máximo valor de cada símbolo, se hizo un shuffle. Ahora los bloques guardan cierta key (un símbolo) el el que se ponen todos los valores

Por ejemplo en el bloque 1 se puso a Apple y todos sus valores.

Y ya en el bloque 1 se sacó el máximo de los valores de apple

En el bloque 2 se sacó el máximo de los valores de tales y así

Collect sirvió para traer de regreso todos esos valores máximos, ya que se quería iterar en ellos para imprimir.

## Transformaciones y Acciones

Hay dos tipos de funciones

- Las que modifican el dataset son las **transformaciones**, como filtrar o hacer agregaciones (reduce). Transforman un RDD en otro RDD. Hace lazy execution, o sea que cuando Spark se encuentra estas funciones, no las ejecuta sino hasta el final en el procesamiento.
- Las que no modifican el dataset son las **acciones**, como imprimir o recolectar desde los nodos. Estas no tienen lazy execution, se ejecutan cuando spark las ve.

## Dependencias

- **Narrow**: Parece depender de uno y ya, pero significa depender de completamente todo lo que ese tiene. `Child partition depends on entire parent partition.` `You can have a narrow dependency while having multiple parent partitions, while depending on entire parent partitions.`
- **Wide dependency**: Parece depender de varios, pero realmente significa depender de una porción de ellos. Si dependes de todo lo que tengan entonces es Narrow. Así dependas de 2 de 4, si dependes de tooodo lo que tienen esos 2, es Narrow. `Child partition depends on a portion of each parent partition.`

![image.png](attachment:4b398ead-18d8-475b-915e-f65c1b1e792e:image.png)

Por ejemplo estos dos son narrow dependency

![image.png](attachment:70a4f129-3fa9-4712-a49a-8efa5a9974ce:image.png)

![image.png](attachment:e8b0d703-d4a4-4b65-a06f-3f4807399978:image.png)

## Tasks Introduction

Es una operación que lleve los datos de un bloque o partición, a otro. Pero acá hay demasiados

![image.png](attachment:082dfd58-2939-42d2-9172-95903dac932f:image.png)

Acá agrupamos las tasks en Stages. textFile().map().map() será cada tast del Stage 0. y el 1 ya recogerá los datos de symvol

![image.png](attachment:2e75e056-be5c-417c-b953-1b82e5e40e8c:image.png)

En este caso son 6 tasks, y una sola stage

![image.png](attachment:bbed63bb-aa42-4cbb-beff-e46d6594a88e:image.png)

```scala
val a = sc.parallelize(List("A", "B", "C"), 3)
val b = sc.parallelize(List("X", "Y"), 2)
val c = a.cartesian(b)
c.collect().foreach(println)
```

![image.png](attachment:6b740dc3-0e70-4e73-ad56-6c5149646798:image.png)

![image.png](attachment:c94b685e-6b0a-4a46-9b42-7e9db97d6e80:image.png)

![image.png](attachment:0691f49f-f859-49d8-a14c-7c763844f895:image.png)

Last tasks y stages a ejecutar son planeadas por el **DAG Sceduler** (DAG es **Directed Acyclic Graph**), que toma como input el plan lógico. Al distribuir las tareas según jobs y stages, es ya es el plan físico, el de ejecución, que el **Task Scheduler** manda a ejecutar en los workers.

![image.png](attachment:ec20505f-86ec-469b-bb53-02f2b5933b5a:image.png)

Fun Fact: puedes ver el plan lógico si seleccionas un RDD (una variable que tengas, aunque recuerda que RDD se refiere a las operaciones para crearla) y le pones `.toDebugString`  (en Scala)

```scala
maxvol.toDebugString
```

![image.png](attachment:d9a00f4f-8651-408d-81bc-8c0ef0405b3c:image.png)

Tmb puedes verlo en la UI

## Stages introduction

En Apache Spark, un **stage** es una unidad de trabajo que se puede ejecutar de manera paralela. La división de un trabajo en stages se basa en las dependencias de los RDDs y es crucial para la planificación y ejecución de tareas. Aquí tienes un resumen de cómo y cuándo se inician y terminan los stages, así como su relación con las dependencias amplias (wide dependencies):

### Cuándo se inicia un Stage

1. **Acción**: Un stage se inicia cuando se ejecuta una acción (como `count`, `collect`, `saveAsTextFile`, etc.) sobre un RDD.
2. **Dependencias**: Si el RDD tiene dependencias amplias, Spark dividirá el trabajo en múltiples stages. Esto es porque las operaciones que producen dependencias amplias necesitan que todos los datos de las particiones de los RDDs padres se completen antes de que se puedan calcular las particiones del RDD hijo.

### Cuándo se termina un Stage

1. **Compleción de Tareas**: Un stage se considera terminado cuando todas las tareas asociadas a ese stage se han completado exitosamente.
2. **Fallos y Reintentos**: Si alguna tarea falla, Spark puede reintentarla. Un stage no se marca como terminado hasta que todas las tareas se ejecuten correctamente.

### Relación con Wide Dependencies

- **Dependencias Amplias (Wide Dependencies)**: Se producen cuando una operación requiere que todos los datos de un RDD padre se agrupen o se redistribuyan para calcular un RDD hijo. Ejemplos de operaciones que generan dependencias amplias son `reduceByKey`, `groupByKey` y `join`.
- En este contexto, un nuevo stage se inicia antes de la operación de agrupamiento o redistribución, ya que todos los datos deben estar disponibles.

### Operaciones que Desencadenan Stages

1. **Transformaciones**: Las transformaciones como `map`, `filter`, `flatMap`, etc., crean un nuevo RDD, pero no desencadenan la ejecución inmediata ni la creación de un nuevo stage. Solo crean un plan lógico.
2. **Acciones**: Como se mencionó, las acciones como `count`, `collect`, `saveAsTextFile`, etc., desencadenan la ejecución de stages, ya que requieren que se realicen cálculos en los RDDs.

### Resumen

- Un stage se inicia con una acción sobre un RDD.
- Se termina cuando todas las tareas asociadas se completan.
- Las dependencias amplias son clave para determinar la división en stages, ya que requieren que todos los datos de los RDDs padres estén disponibles antes de poder calcular los hijos.

Si necesitas más información o ejemplos específicos, ¡házmelo saber!

## Jobs, Stages y Tasks en Spark

![image.png](attachment:e73af7a9-2db1-489d-a61a-2fa04685f983:image.png)

### 1. **Job**

Un **job** en Spark es una acción que desencadena el procesamiento de datos. Se inicia cuando se invoca una operación que requiere que se ejecute un cálculo, como `count()`, `collect()`, o `saveAsTextFile()`. Un job puede estar compuesto por múltiples etapas.

### 2. **Stage**

Un **stage** es una unidad de trabajo dentro de un job. Spark divide un job en etapas basándose en las transformaciones que pueden ser ejecutadas de manera paralela. Las etapas se dividen en dos tipos:

- **Stage de Shuffle:** Ocurre cuando hay una operación que requiere un intercambio de datos entre diferentes nodos, como `groupByKey()`, `reduceByKey()`, o `join()`.
- **Stage sin Shuffle:** Ocurre cuando las transformaciones pueden ser realizadas sin necesidad de mover datos entre los nodos, como `map()` o `filter()`.

Cada stage se representa como un conjunto de tareas que se pueden ejecutar en paralelo.

### 3. **Task**

Una **task** es la unidad más pequeña de trabajo en Spark. Cada tarea representa una operación que se ejecuta en un conjunto de particiones de datos. Cuando se ejecuta un job, cada stage se divide en múltiples tareas que se distribuyen a través de los nodos del clúster. El número de tareas por stage depende del número de particiones en el RDD (Resilient Distributed Dataset) o DataFrame.

### Flujo de Trabajo de un Job en Spark

1. **Inicialización del Job:** Se inicia cuando se llama a una acción en un RDD o DataFrame.
2. **Planificación del Job:** Spark analiza las transformaciones y decide cómo dividir el trabajo en stages.
3. **Ejecución de Stages:** Los stages se ejecutan en orden. Cada stage se divide en varias tasks.
4. **Ejecución de Tasks:** Las tasks se distribuyen entre los nodos y se ejecutan en paralelo.
5. **Resultados:** Los resultados de las tasks se combinan y se devuelven al driver o se almacenan en un sistema de archivos.

### Ejemplo Simplificado

```python
from pyspark import SparkContext

sc = SparkContext("local", "Ejemplo")
data = sc.parallelize([1, 2, 3, 4, 5])

# Job: count
result = data.filter(lambda x: x > 2).count()

```

En este ejemplo:

- **Job:** `count()`
- **Stage:** Un stage se creará para la transformación `filter()`, ya que no requiere un shuffle.
- **Task:** Cada partición de `data` se procesará en paralelo como una tarea.

### Resumen

- Un **job** es un trabajo completo que se ejecuta en Spark.
- Un **stage** es una subdivisión del job que se puede ejecutar en paralelo.
- Una **task** es la unidad de trabajo más pequeña, correspondiente a un conjunto de datos en una partición.

Estos conceptos son fundamentales para comprender cómo Spark maneja la ejecución distribuida y la paralelización de tareas en clústeres de datos.

## PIPELINE

En vez de iterar en cada elemento para aplicarle una sola operación, e iterar de nuevo en las demás operaciones, ya con estas tasks largas ahora podremos iterar una sola vez entre los elementos

![image.png](attachment:799cc5cc-55e8-4eee-a10d-179b8e28e486:image.png)

## Error/Fault Tolerance

Si este nodo se muere, normal, pues volvemos a ejecutar el proceso pipeline en un nodo diferente, este no depende de nada

![image.png](attachment:bd1ab62b-e4b0-45de-9888-71c594b959b1:image.png)

En cambio si este nodo se muere, necesitaremos tener los nodos 0, 1, 2 y 3 vivos, para que de su ram saquemos sus resultados y así hagamos la operación para volver a sacar la partición 3 en un nodo melo.

![image.png](attachment:aedd7adf-6553-424c-8634-3b37298387ba:image.png)

1. **RDD Inmutable**: Los RDDs (Resilient Distributed Datasets) son inmutables, lo que significa que una vez creados, no se pueden modificar. Esto facilita la reconstrucción de datos en caso de fallos.
2. **Registro de Dependencias**: Spark mantiene un registro de las transformaciones que se aplican a los RDDs. Esto permite reconstruir un RDD perdido a partir de sus RDDs padres.
3. **Reevaluación de Particiones**: Si una partición de un RDD se pierde (por ejemplo, debido a un fallo de nodo), Spark puede reevaluar solo esa partición utilizando el plan de transformación almacenado, en lugar de recomputar todo el RDD.
4. **Checkpointing**: Spark permite el checkpointing, que es el proceso de guardar un RDD en disco para que se pueda recuperar más fácilmente en caso de fallos. Esto es útil para RDDs que se usan en múltiples etapas.
5. **Reintentos Automáticos**: Si una tarea falla, Spark reintentará automáticamente la tarea fallida en otro nodo, lo que ayuda a mantener la ejecución continua del trabajo.
6. **Distribución de Datos**: Al distribuir datos y tareas a través de múltiples nodos, Spark minimiza el impacto de un fallo de nodo, ya que otras partes del trabajo pueden continuar ejecutándose.

### Conclusión

La tolerancia a fallos en Spark se logra a través de la inmutabilidad de los RDDs, el registro de dependencias y la posibilidad de reevaluar particiones perdidas. Estos mecanismos garantizan que, incluso en caso de fallos, el procesamiento de datos pueda continuar sin perder información.

Si necesitas más detalles o ejemplos específicos, ¡hazmelo saber!

## UI

Te metes a la ip del nodo maestro, por el puerto 18080, puedes ver los nodos workers y los executers que tienen

![image.png](attachment:4abf0474-4010-41d3-86a4-915e7afee1c9:image.png)

Si te metes en un worker, acá ves sus executors

![image.png](attachment:dcb239aa-9e90-45f1-8417-a94f434f855d:image.png)

Pero si le das aquí, en Application Detail UI, puedes ver los jobs asignados y si se han cumplido

![image.png](attachment:90d4f046-2379-4727-beba-52b2600a7aee:image.png)

![image.png](attachment:948edc11-0d91-4932-81fd-d25e531cfdfa:image.png)

Al darle click al job podemos ver sus stages

![image.png](attachment:e6ab1d48-aa3a-425d-9669-ba4942ab3bae:image.png)

E ingluso podemos ver su DAG (en DAG visualization), o sea, la wea que planeó (o el plan en sí, que es el DAG) de cómo se hará la ejecución.

![image.png](attachment:2ed281e3-a24e-4c9e-9f92-7ce175722eb0:image.png)

Podemos ver las tasks de una stage, con muchas stats

![image.png](attachment:903718b0-0ff6-4620-aa84-2faabde78c4e:image.png)

![image.png](attachment:ec7bf5e7-06cc-401e-abb5-9777cd3975c7:image.png)

Y su DAG también, con un poco más de detalles

![image.png](attachment:53f293c0-12f9-4c60-bdc3-53ca4fdd6eb8:image.png)

## Executors

Una aplicación que corre en nuestro spark, por ejemplo Spark Shell, necesita ejecutadores. Los executers son procesos que hacen que nuestra aplicación corra en runtime, y seon ubicados en worker nodes. A cada worker se le asigna cierta memoria y ciertos cores/procesadores.

![image.png](attachment:6816549e-659b-47a3-9fe1-78213ccdb76c:image.png)

![image.png](attachment:6600bb25-18dc-4889-ba42-22bd53ef6d36:image.png)

Cada aplicación tiene sus executors reservados en los workers

![image.png](attachment:bcf6c895-7466-4989-855a-45f27b759d0a:image.png)

## Caching & Memory Management

Se guardan los datos que hay al principio de cada Stage. O sea, los datos que hay después de un wide dependency, o en otras palabras los datos que resultan de haber hecho un wide dependency. 

Los datos de maxvol son guardados en ram, se guardó el resultado de su RDD (proceso/operaciones) para cuando alguien vaya a depender de él o sus datos vayan a ser usados. Maxvol RDD fué cacheado.

![image.png](attachment:97b96508-0e37-4abd-b446-cdc76ced14aa:image.png)

Por eso, si usamos maxvol por ejemplo en un count (`maxvol.count()`), el resultado va a ser rapidísimo, porque su RDD fue guardado, los datos suyos fueron guardados en cada nodo, entonces los usa y ya, porque están guardados en la ram de cada nodo.

Pero si usamos `symvol.count()`, sus datos no están guardados, y tampoco los de ninguno de sus dependencias y de las dependencias de esas.

En el caso de symbol, sus dependencias no fueron guardadas porque no era el principio de la stage, y no había wide dependency de la que dependiera, así que le toca sacar de nuevo esos datos.

Sigue estando bien, pues, Hadoop no recuerda una mondá. 

### Cuándo Cachea? (resúmen)

En Apache Spark, se cachea automáticamente el primer RDD de un stage. Esto ocurre cuando el RDD se usa como entrada para una acción (como `count`, `collect`, etc.).

Sin embargo, los RDD que se generan a partir de transformaciones (como `map`, `filter`, etc.) no se cachean automáticamente. Si deseas que un RDD específico se almacene en caché para su uso posterior, debes hacerlo explícitamente utilizando `cache()` o `persist()`.

En resumen:

- **Primer RDD de un stage**: Se cachea automáticamente si se usa en una acción.
- **Último RDD de un stage**: No se cachea automáticamente.

### Obligar caching o de-caching

Si por ejemplo fueras a contar symbol, luego lo quisieras filtrar, y luego lo quisieras ver de nuevo, de hecho estarías leyendo el dataset 3 veces, porque no estás haciéndole caching a Symbol.

```scala
symvol.cache()

symvol.persist(org.apache.spark.storage.StorageLevel.MEMORY_ONLY)
symvol.persist(org.apache.spark.storage.StorageLevel.DISK_ONLY)
symvol.persist(org.apache.spark.storage.StorageLevel.MEMORY_AND_DISK)

symvol.unpersist()
```

1. **`symvol.cache()`**: Almacena el DataFrame o RDD en memoria (sólo en memoria, únicamente allí) para acceso rápido. Es un atajo para el modo MEMORY_ONLY
2. **`symvol.persist(org.apache.spark.storage.StorageLevel.MEMORY_ONLY)`**: Persiste el DataFrame o RDD solo en memoria.
3. **`symvol.persist(org.apache.spark.storage.StorageLevel.DISK_ONLY)`**: Persiste el DataFrame o RDD solo en disco.
4. **`symvol.persist(org.apache.spark.storage.StorageLevel.MEMORY_AND_DISK)`**: Persiste el DataFrame o RDD en memoria y, si no hay suficiente memoria, también en disco.
5. **`symvol.unpersist()`**: Libera el almacenamiento de datos del DataFrame o RDD.

Si necesitas más información o un análisis más detallado, házmelo saber.

### Y si se llena la ram?

Hay una estrategia, la LRU (Least Recently Used)

Lo más viejo que se haya guardado, se saca de la RAM y se mete en disco, pa dejarle espacio a los RDD cacheados nuevos, que es más probable que sean usados.