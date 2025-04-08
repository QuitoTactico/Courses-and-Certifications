# Source

- (video kinda deprecated) https://youtu.be/K9AnJ9_ZAXE
- https://globant.udemy.com/course/the-complete-hands-on-course-to-master-apache-airflow
- https://marclamberti.com/

# Install (linux only) (it didn’t work neither)

## Instalar Python 3.12 en ubuntu

```bash
sudo apt update
sudo apt upgrade
sudo apt install -y software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install -y python3.12
python3.12 --version  # Verificar instalación
sudo apt install python3.12 python3.12-venv
sudo apt install python3-pip
# (Opcional) Crear un enlace simbólico
sudo ln -s /usr/bin/python3.12 /usr/bin/python
```

## Instalar Airflow

https://github.com/apache/airflow?tab=readme-ov-file#installing-from-pypi

Tienes que copiar el comando de pip y pues ejecutarlo adentro de un entorno virtual. Ubuntu solo te deja usar entornos virtuales.

```bash
# Crear un entorno virtual
python3.12 -m venv venv

# Activar el entorno virtual
source venv/bin/activate

# Instalar Apache Airflow
pip install 'apache-airflow==2.10.5' --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.10.5/constraints-3.12.txt"

# Verificar la instalación
airflow version

# Desactivar el entorno virtual cuando termines
deactivate
```

- Windows again, deprecated
    
    Al final del comando, puedes especificar tu versión de python.
    
    ```bash
    py -3.12 -m venv .venv
    .\.venv\Scripts\activate
    ```
    
    El pc de la empresa no deja crear venvs así que vale verga
    
    Digámosle a pip que instale la wea en específicamente mi python 3.12 (el máximo que se pudo cuando hice esto)
    
    ```bash
    py -3.12 -m pip install 'apache-airflow==2.10.5' --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.10.5/constraints-3.12.txt"
    ```
    
    El equivalente de `py -3.12` que es de windows, en linux, sería `python3.12`
    
    Recuerda poner el directorio de los scripts de PIP de tu python 3.12 en el PATH. `C:\Users\esteban.vergara\AppData\Local\Programs\Python\Python312\Scripts`
    

## AIRFLOW_HOME (Deprecated, windows)

En Windows, la forma de establecer variables de entorno es diferente a la de Unix/Linux. Si deseas establecer la variable de entorno `AIRFLOW_HOME` en Windows, puedes hacerlo de varias maneras. Aquí te muestro dos métodos: usando la línea de comandos (CMD) y PowerShell.

### Opción 1: Usando la línea de comandos (CMD)

1. Abre el símbolo del sistema (CMD).
2. Ejecuta el siguiente comando para establecer la variable de entorno:
    
    ```bash
    set AIRFLOW_HOME=.
    
    ```
    
    Este comando establece `AIRFLOW_HOME` en el directorio actual. Sin embargo, esta variable solo estará activa en la ventana de CMD actual.
    
3. Si deseas que esta variable persista incluso después de cerrar la ventana, puedes establecerla de forma permanente con:
    
    ```bash
    setx AIRFLOW_HOME "."
    
    ```
    

### Opción 2: Usando PowerShell

1. Abre PowerShell.
2. Ejecuta el siguiente comando para establecer la variable de entorno:
    
    ```powershell
    $env:AIRFLOW_HOME="."
    
    ```
    
    Al igual que en CMD, esta variable solo estará activa en la sesión actual de PowerShell.
    
3. Para establecerla de forma permanente en PowerShell, utiliza el siguiente comando:
    
    ```powershell
    [System.Environment]::SetEnvironmentVariable("AIRFLOW_HOME", ".", "User")
    
    ```
    

### Verificar la Variable de Entorno

Para asegurarte de que la variable se ha establecido correctamente, puedes usar el siguiente comando en CMD:

```bash
echo %AIRFLOW_HOME%

```

O en PowerShell:

```powershell
echo $env:AIRFLOW_HOME

```

### Resumen

- **CMD**: Usa `set` para variables temporales y `setx` para variables permanentes.
- **PowerShell**: Usa `$env:` para variables temporales y `[System.Environment]::SetEnvironmentVariable` para variables permanentes.

Siguiendo estos pasos, podrás establecer la variable `AIRFLOW_HOME` en tu entorno de Windows.

## AIRFLOW_HOME

La idea era hacer `export AIRFLOW_HOME=.` y luego correr `airflow db init` , el problema es que todo eso parece viejo y deprecado, y sqlite tira problema por usar rutas relativas, y básicamente no te deja usarlo descargando todo en local, así que yo prefiero tirar todo esto del video a la basura y mejor hacerlo con Docker desde el inicio.

# Install using Docker, no matter where

https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html

https://airflow.apache.org/docs/apache-airflow/2.5.1/docker-compose.yaml

https://airflow.apache.org/docs/apache-airflow/2.10.5/docker-compose.yaml

Hi there 👋

It's time to install Apache Airflow. As you are going to see, it's very simple.

**Prerequisites**

First, make sure you have installed Docker Desktop and Visual Studio. If not, take a look at these links:

- [Get Docker](https://docs.docker.com/get-docker/)
- [Get Visual Studio Code](https://code.visualstudio.com/download)

Docker needs privilege rights to work, make sure you have them.

**Follow the documentation first.**

If you have trouble to install these tools, here are some videos to help you

- [Install Docker on Windows 10](https://www.youtube.com/watch?v=lIkxbE_We1I&ab_channel=JamesStormes)
- [Install Docker on Windows 10 with WSL 2](https://www.youtube.com/watch?v=h0Lwtcje-Jo&ab_channel=BeachcastsProgrammingVideos)
- [Install Docker on Windows 11](https://youtu.be/6k1CyA5zYgg?t=249)

**Install Apache Airflow with Docker**

1. Create a folder **materials** in your **Documents**
2. In this folder, download the following file: [docker compose file](https://airflow.apache.org/docs/apache-airflow/2.5.1/docker-compose.yaml)
3. If you right-click on the file and save it, you will end up with docker-compose.yaml.txt. Remove the .txt and keep docker-compose.yaml
4. Open your terminal or CMD and go into **Documents/materials**
5. Open Visual Studio Code by typing the command: `code .`
6. You should have something like this
    
    ![](https://img-c.udemycdn.com/redactor/raw/article_lecture/2022-05-19_08-58-14-75ad4de4f9c3fa386546708ce86db04a.png)
    
7. Right click below docker-compose.yml and create a new file `.env` (don't forget the dot before env)
8. In this file add the following lines
    
    
        `1. AIRFLOW_IMAGE_NAME=apache/airflow:2.4.2
        2. AIRFLOW_UID=50000`
    
    1. 1. AIRFLOW_IMAGE_NAME=apache/airflow:2.4.2
    2. 2. AIRFLOW_UID=50000
    
    and save the file
    
    ![](https://img-c.udemycdn.com/redactor/raw/article_lecture/2022-05-19_08-58-15-94fb1fff7e92c0ca1378ec7421e0f650.png)
    
9. Go at the top bar of Visual Studio Code -> Terminal -> New Terminal
    
    ![](https://img-c.udemycdn.com/redactor/raw/article_lecture/2022-05-19_08-58-15-c82d370ca2d8cf4b8eecc5337650dca6.png)
    
10. In your new terminal at the bottom of Visual Studio Code, type the command `docker-compose up -d` and hit `ENTER`
    
    ![](https://img-c.udemycdn.com/redactor/raw/article_lecture/2022-05-19_08-58-15-8a8428697d23ce89a6cd8af85881523c.png)
    
11. You will see many lines scrolled, wait until it's done. Docker is downloading Airflow to run it. It can take up to 5 mins depending on your connection. If Docker raises an error saying it can't download the docker image, ensure you are not behind a proxy/vpn or corporate network. You may need to use your personal connection to make it work. At the end, you should end up with something like this:
    
    ![](https://img-c.udemycdn.com/redactor/raw/article_lecture/2022-05-19_08-58-15-1d0b2c401e8b14e1d23ec2024eaf0eef.png)
    

Well done, you've just installed Apache Airflow with Docker! 🎉

Open your web browser and go to `localhost:8080`

![](https://img-c.udemycdn.com/redactor/raw/article_lecture/2022-05-19_08-58-15-8e7bab039ef558f46a3263d851649e95.png)

### Troubleshoots

- > If you don't see this page, make sure you have nothing already running on the port 8080

Also, go back to your terminal on Visual Studio Code and check your application with `docker-compose ps`

All of your "containers" should be healthy as follow:

![](https://img-c.udemycdn.com/redactor/raw/article_lecture/2022-05-19_08-58-15-414bbbd37e901753ea738f68380ef573.png)

If a container is not healthy. You can check the logs with `docker logs materials_name_of_the_container`

Try to spot the error; once you fix it, restart Airflow with `docker-compose down` then `docker-compose up -d`

and wait until your container states move from starting to healthy.

- > If you see this error

![](https://img-c.udemycdn.com/redactor/raw/article_lecture/2023-03-06_08-28-42-9884e885f01d16f91bd4a0f03ed267db.png)

remove your volumes with `docker volume prune` and run `docker-compose up -d` again

- > If you see that airflow-init docker container has exited, that's normal :)

If you still have trouble, reach me on the Q/A with your error.

# Components

Apache Airflow es una plataforma de orquestación de flujos de trabajo que permite programar y monitorizar tareas. A continuación, se presenta un resumen de sus componentes principales:

### 1. UI (Interfaz de Usuario)

La UI es la interfaz gráfica donde los usuarios pueden visualizar y gestionar los flujos de trabajo (DAGs). Permite a los usuarios iniciar, detener y monitorear la ejecución de las tareas, así como revisar registros y estados de ejecución. La UI es fundamental para la interacción del usuario con Airflow.

### 2. Scheduler

El Scheduler es el componente responsable de programar las tareas en los DAGs. Monitorea los DAGs y determina cuándo deben ejecutarse las tareas basándose en sus dependencias y cronogramas. El Scheduler es crucial para asegurar que las tareas se ejecuten en el orden correcto y en el momento adecuado.

### 3. Meta Database

La Meta Database es donde Airflow almacena la información sobre los DAGs, las tareas, los estados de ejecución y otros metadatos. Esta base de datos es fundamental para el funcionamiento de Airflow, ya que permite el seguimiento del estado de las tareas y su programación. Generalmente se utiliza una base de datos relacional como PostgreSQL o MySQL.

### 4. Triggerer

El Triggerer es un componente que permite ejecutar tareas basadas en eventos. Se utiliza para manejar tareas que dependen de condiciones externas o eventos, como esperar a que un archivo llegue a un sistema de archivos o a que se complete una tarea en otro sistema. Esto permite una mayor flexibilidad y control sobre la ejecución de flujos de trabajo.

### 5. The Executor

El Executor es responsable de ejecutar las tareas programadas. Airflow ofrece diferentes tipos de ejecutores (como LocalExecutor, CeleryExecutor, entre otros) que gestionan cómo y dónde se ejecutan las tareas. La elección del ejecutor puede afectar el rendimiento y la escalabilidad del flujo de trabajo.

### 6. The Queue

La Queue es un sistema de mensajería que permite a los componentes de Airflow comunicarse entre sí. Las tareas se envían a la cola para ser ejecutadas por los workers. Es un elemento clave en arquitecturas distribuidas, ya que permite la separación de las tareas y la ejecución en paralelo.

### 7. The Worker

Los Workers son los procesos que ejecutan las tareas. Dependiendo del ejecutor utilizado, pueden ser procesos locales o distribuidos en un clúster. Los workers toman las tareas de la cola y las ejecutan, reportando el estado de la ejecución de vuelta al Scheduler y a la Meta Database.

Estos componentes trabajan en conjunto para facilitar la orquestación de flujos de trabajo, asegurando que las tareas se ejecuten de manera eficiente y en el orden correcto.

# Concepts

Página para ver los operators disponibles: https://www.astronomer.io/

[Astronomer: The Best Place to Run Apache Airflow®](https://www.astronomer.io/)

Aquí tienes un resumen de los conceptos clave en Apache Airflow:

### 1. DAG (Directed Acyclic Graph)

Un DAG es una representación gráfica de un flujo de trabajo en Airflow. Consiste en un conjunto de tareas (tasks) organizadas en un gráfico acíclico dirigido, lo que significa que no hay ciclos y cada tarea puede depender de otras. Los DAGs definen la estructura y el orden en el que se deben ejecutar las tareas, así como sus dependencias y condiciones de programación.

### 2. Operator

Un Operator es un componente que define una tarea específica dentro de un DAG. En Airflow, los Operators son clases que encapsulan la lógica de ejecución de una tarea, y pueden ser de diferentes tipos según la acción que realizan, como ejecutar un script, realizar una consulta a una base de datos, enviar un correo electrónico, entre otros. Algunos ejemplos de Operators son `BashOperator`, `PythonOperator`, `EmailOperator`, etc.

### 3. Task / Task Instance

- **Task**: Una tarea es una unidad de trabajo en un DAG. Cada tarea se define utilizando un Operator y tiene un nombre único dentro del DAG. Las tareas son los bloques de construcción que se ejecutan durante la orquestación del flujo de trabajo.
- **Task Instance**: Una instancia de tarea es una representación específica de una tarea en un momento dado. Cada vez que se ejecuta una tarea en un DAG, se crea una nueva instancia de tarea que tiene un estado asociado (por ejemplo, "en ejecución", "completada", "fallida"). Las instancias de tarea permiten a Airflow hacer un seguimiento del estado y la ejecución de cada tarea en diferentes ejecuciones del DAG.

### 4. Workflow

Un workflow (flujo de trabajo) en Airflow es el conjunto completo de tareas y sus interacciones definidas en un DAG. Representa el proceso completo que se debe llevar a cabo para lograr un objetivo específico. Los workflows pueden incluir una secuencia de tareas dependientes, tareas paralelas, y lógica condicional, lo que permite construir flujos de trabajo complejos y robustos para la orquestación de datos y tareas.

Estos conceptos son fundamentales para entender cómo se estructuran y ejecutan los flujos de trabajo en Apache Airflow.

## Resúmen

*What should you keep in mind after what you've learned?*

- Airflow is an orchestrator, not a processing framework. Process your gigabytes of data outside of Airflow (i.e. You have a Spark cluster, you use an operator to execute a Spark job, and the data is processed in Spark).
- A DAG is a data pipeline, an Operator is a task.
- An Executor defines how your tasks are executed, whereas a worker is a process executing your task
- The Scheduler schedules your tasks, the web server serves the UI, and the database stores the metadata of Airflow.

# Airflow NO

## No es…

Tienes razón; Apache Airflow no es un sistema de procesamiento de datos, un sistema de streaming ni un sistema de almacenamiento de datos. A continuación, explico estas diferencias y el enfoque de Airflow en la orquestación de flujos de trabajo por lotes (batch):

### 1. No es un Sistema de Procesamiento de Datos

Apache Airflow es una herramienta de orquestación que permite gestionar y programar tareas, pero no realiza el procesamiento de datos en sí. En cambio, se utiliza para coordinar tareas que pueden incluir el procesamiento de datos mediante otras herramientas o sistemas. Por ejemplo, puedes usar Airflow para orquestar un flujo de trabajo que incluya tareas de extracción, transformación y carga (ETL) que se ejecutan en sistemas de procesamiento de datos como Apache Spark, Hadoop o bases de datos SQL.

### 2. Enfoque en Batch

Airflow está diseñado principalmente para flujos de trabajo por lotes (batch processing). Esto significa que se utiliza para programar y ejecutar tareas en intervalos regulares o en función de eventos específicos, en lugar de procesar datos en tiempo real. Los flujos de trabajo en Airflow se ejecutan en función de una programación establecida, lo que permite a los usuarios manejar grandes cantidades de datos en lotes, en lugar de procesar datos continuamente como en un sistema de streaming.

### 3. No es un Sistema de Almacenamiento de Datos

Airflow no está destinado a almacenar datos. En su lugar, actúa como un coordinador que gestiona la ejecución de tareas que pueden leer o escribir en sistemas de almacenamiento. Por ejemplo, un flujo de trabajo de Airflow podría incluir tareas que extraen datos de una base de datos, procesan esos datos y luego los escriben en un sistema de almacenamiento como Amazon S3, Google Cloud Storage o una base de datos. La Meta Database de Airflow solo se utiliza para almacenar metadatos sobre las ejecuciones de los flujos de trabajo y el estado de las tareas, no para almacenar los datos que se procesan en esos flujos de trabajo.

### Conclusión

En resumen, Apache Airflow es una herramienta de orquestación de flujos de trabajo que permite a los usuarios coordinar y programar tareas de procesamiento de datos por lotes, pero no realiza el procesamiento de datos en sí, no opera en tiempo real (streaming) y no almacena datos. Su enfoque en la orquestación le permite integrarse fácilmente con diversas herramientas y sistemas que sí se encargan del procesamiento y almacenamiento de datos.

## No es bueno para…

Es correcto, Apache Airflow tiene limitaciones en ciertos escenarios y no siempre es la mejor solución. A continuación, se detallan algunos casos en los que Airflow puede no ser la opción más adecuada:

### 1. **High-Frequency Sub-Minute Frequency**

Airflow no está diseñado para manejar flujos de trabajo de alta frecuencia que requieran ejecuciones sub-minuto. Su arquitectura y modelo de programación están más enfocados en tareas que se ejecutan en intervalos más largos, como minutos, horas o incluso días. Para tareas que necesitan ejecutarse con una frecuencia tan alta, se podrían considerar otras soluciones más adecuadas, como sistemas de procesamiento de eventos en tiempo real, por ejemplo, Apache Kafka o Apache Flink.

### 2. **Processing Large Datasets Directly**

Airflow no es un sistema de procesamiento de datos. No está diseñado para manejar directamente grandes volúmenes de datos. En su lugar, se utiliza para orquestar tareas que pueden procesar datos en sistemas externos. Si el procesamiento de grandes conjuntos de datos es una prioridad, se deben utilizar herramientas específicas como Apache Spark, Hadoop, o sistemas de bases de datos que estén optimizados para manejar y procesar grandes volúmenes de datos de manera eficiente.

### 3. **Real-Time Data Streaming**

Airflow no está diseñado para el procesamiento de datos en tiempo real (streaming). Su enfoque está más orientado a flujos de trabajo por lotes, donde las tareas se ejecutan en función de una programación establecida. Para aplicaciones que requieren un procesamiento continuo de flujos de datos en tiempo real, es mejor utilizar plataformas de streaming de datos como Apache Kafka, Apache Pulsar o Apache Flink, que están diseñadas para manejar datos en movimiento y proporcionar latencias bajas.

### 4. **Simple and Linear Workflows with Few Dependencies**

Airflow es más beneficioso en flujos de trabajo complejos que involucran múltiples tareas y dependencias. Para flujos de trabajo simples y lineales con pocas o ninguna dependencia, la sobrecarga de configurar un DAG y gestionar las tareas puede ser innecesaria. En estos casos, el uso de scripts simples o herramientas más ligeras podría ser suficiente y más eficiente.

### Conclusión

En resumen, aunque Apache Airflow es una herramienta poderosa para la orquestación de flujos de trabajo, no es la mejor solución para todos los casos. En situaciones que requieren alta frecuencia, procesamiento directo de grandes conjuntos de datos, streaming en tiempo real o flujos de trabajo simples, es recomendable evaluar otras herramientas y enfoques que se adapten mejor a las necesidades específicas del proyecto.

# Architectures

Claro, aquí tienes una versión mejorada de la respuesta que incluye tus observaciones:

## 1. Single Node Architecture

### Ubicación de los Componentes

En una arquitectura de un solo nodo, todos los componentes de Airflow se ejecutan en una única máquina. Esto incluye:

- **Web Server (UI)**: Proporciona la interfaz gráfica para gestionar DAGs y tareas.
- **Scheduler**: Se encarga de programar las tareas.
- **Executor**: Puede ser un `LocalExecutor` o un `SequentialExecutor` que ejecuta las tareas en el mismo nodo. El Executor siempre está junto al Scheduler y determina cómo se ejecutan las tareas.
- **Meta Database**: Almacena los metadatos sobre los DAGs y el estado de las tareas. En entornos de desarrollo, suele ser una base de datos liviana como SQLite, mientras que en producción se utilizan bases de datos más robustas como PostgreSQL o MySQL.
- **Worker**: En el caso de usar `LocalExecutor`, las tareas se ejecutan como procesos hijos del Scheduler; si se usa `SequentialExecutor`, se ejecutan una a la vez.

### Comportamiento y Relación de los Componentes

- Todos los componentes se comunican a través de la **Meta Database**, que orquesta el flujo de información entre ellos.
- La UI puede acceder a la base de datos para mostrar el estado y los registros de las tareas, mientras que el Scheduler utiliza la misma base de datos para programar las tareas.
- Las tareas se ejecutan localmente y, debido a la naturaleza de un solo nodo, es posible que el rendimiento se vea afectado si hay múltiples tareas que requieren recursos intensivos.

## 2. Multi Node Architecture

### Ubicación de los Componentes

En una arquitectura de múltiples nodos, los componentes de Airflow se distribuyen en varias máquinas. Esta arquitectura a menudo utiliza:

- **Web Server (UI)**: Puede estar en un nodo separado, permitiendo acceso remoto a múltiples usuarios. Se pueden implementar **load balancers** para gestionar la carga y permitir que múltiples instancias del Web Server manejen solicitudes simultáneamente.
- **Scheduler**: Se puede ejecutar en un nodo separado para manejar la programación de tareas de manera más eficiente.
- **Executor**: Frecuentemente se usa `CeleryExecutor`, que permite la ejecución de tareas en múltiples workers distribuidos en varios nodos. Al igual que en la arquitectura de un solo nodo, el Executor siempre está junto al Scheduler y determina cómo se ejecutan las tareas.
- **Meta Database**: Almacena los metadatos y puede estar en un nodo dedicado, utilizando una base de datos robusta como PostgreSQL o MySQL.
- **Workers**: Se distribuyen en múltiples nodos, permitiendo la ejecución paralela de tareas.

### Comportamiento y Relación de los Componentes

- La UI se comunica con la base de datos para mostrar información y permite a los usuarios gestionar los DAGs y las tareas desde cualquier lugar.
- El Scheduler, que puede estar en un nodo separado, se encarga de programar las tareas y enviar mensajes a la cola (queue) o al **message broker** (como Redis o RabbitMQ), que será consumida por los Workers.
- Los Workers están distribuidos, lo que permite que múltiples tareas se ejecuten en paralelo, mejorando la eficiencia y la escalabilidad.
- La separación de componentes permite un mejor rendimiento y la posibilidad de escalar horizontalmente agregando más nodos de workers según sea necesario.

### Conclusión

Ambas arquitecturas tienen sus usos y beneficios. La arquitectura de **single node** es adecuada para entornos de desarrollo y pruebas, donde la simplicidad es clave. Por otro lado, la arquitectura de **multi node** es ideal para entornos de producción donde se requiere escalabilidad, rendimiento y la capacidad de manejar flujos de trabajo más complejos con múltiples tareas. La elección entre estas arquitecturas dependerá de los requisitos específicos de la carga de trabajo y del entorno en el que se implementará Airflow.

# Operators types

Apache Airflow tiene varios tipos de operadores que se utilizan para realizar diferentes tipos de tareas en un flujo de trabajo (DAG). Aquí te muestro una clasificación de algunos de los operadores más comunes en Airflow, incluyendo **Action**, **Transfer** y **Wait**:

### 1. Action Operators

Los **Action Operators** se utilizan para realizar acciones específicas, como ejecutar scripts, enviar correos electrónicos o interactuar con otras aplicaciones. Algunos ejemplos son:

- **BashOperator**: Ejecuta comandos de Bash.
- **PythonOperator**: Ejecuta funciones de Python.
- **EmailOperator**: Envía correos electrónicos.
- **DockerOperator**: Ejecuta comandos dentro de un contenedor Docker.
- **PostgresOperator**: Ejecuta comandos SQL en una base de datos PostgreSQL.

### 2. Transfer Operators

Los **Transfer Operators** se utilizan para mover datos entre diferentes sistemas, como bases de datos o servicios. Algunos ejemplos son:

- **S3ToRedshiftOperator**: Transfiere datos desde Amazon S3 a Amazon Redshift.
- **MySqlToGoogleCloudStorageOperator**: Transfiere datos desde MySQL a Google Cloud Storage.
- **GoogleCloudStorageToBigQueryOperator**: Transfiere datos desde Google Cloud Storage a BigQuery.
- **CsvToHiveOperator**: Carga archivos CSV en una tabla de Hive.

### 3. Wait Operators

Los **Wait Operators** se utilizan para pausar la ejecución de un flujo de trabajo hasta que se cumplan ciertas condiciones. Algunos ejemplos son:

- **TimeDeltaSensor**: Espera un tiempo específico antes de continuar.
- **ExternalTaskSensor**: Espera a que un task específico en otro DAG se complete.
- **SqlSensor**: Espera a que se cumpla una condición en una consulta SQL.
- **FileSensor**: Espera a que un archivo esté disponible en un sistema de archivos.

### Resumen

- **Action Operators**: Realizan acciones específicas (ej. ejecutar comandos, enviar correos electrónicos).
- **Transfer Operators**: Mueven datos entre diferentes sistemas (ej. entre bases de datos, servicios en la nube).
- **Wait Operators**: Pausan la ejecución hasta que se cumplan ciertas condiciones (ej. esperar a que un archivo esté disponible o que un task en otro DAG se complete).

Estos operadores son fundamentales para construir flujos de trabajo complejos y eficientes en Apache Airflow. Si tienes alguna pregunta específica sobre alguno de estos operadores o su uso, ¡no dudes en preguntar!

# Troubleshooting con PIP

**RECUERDA QUE LA ÚLTIMA VERSIÓN DE PYTHON COMPATIBLE ES LA 3.12, NO VAYAS A USAR LA 3.13, USA EL PIP DE LA 3.12.**

Al instalar airflow y sus providers con esto (por ejemplo)

```bash
py -3.12 -m pip install apache-airflow
```

Antes necesitas instalar rust (viene con cargo) **y meter a cargo en el path, luego volver a abrir VSC**

Descarga el instalador de rust con estas opciones:

- https://rustup.rs/
- `curl --proto '=https' --tlsv1.2 -sSf [https://sh.rustup.rs](https://sh.rustup.rs/) | sh`

Luego también instala las herramientas de desarrollo con C++ si es que una librería de google da problemas.

Asegúrate de tener instalado el compilador de C++ y las herramientas necesarias para compilar extensiones. Dado que estás usando Visual Studio, asegúrate de que tienes instalada la "C++ Build Tools". Puedes hacerlo siguiendo estos pasos:

- Abre Visual Studio Installer.
- Selecciona la instalación de Visual Studio que tienes y haz clic en "Modificar".
- Asegúrate de seleccionar "Desarrollo de escritorio con C++" o "Herramientas de desarrollo de C++".
- Completa la instalación si es necesario.

# Connections

Las creas desde el dropdown de Admin, le metes la info que cada conexión específica necesite. Unas necesitan puerto, otras URL, y así.

# Testing

Mira el nombre del containder del scheduler con

```bash
docker-compose ps
```

Métete al bash del container del scheduler con

```bash
docker exec -it <nombre_scheduler> /bin/bash
```

Y luego ejecuta esto para ejecutar la tarea

```bash
airflow tasks test <DAG_id> <task_id> <past_date YYYY-MM-DD>
```

Puedes meterte al cmd de postgres estando adentro de su container con 

```bash
psql -U airflow
```

Sales de ese bash de Docker con `ctrl+D`

# Dataset y Triggers

```bash
from airflow import Dataset

my_file = Dataset(
	"s3://dataset/file.csv",
	extra={'owner': 'james'},
)
```

Puedes usarlos como trigger, así cada que otra task los modifica, se ejecutará a sí misma.

Hay toda una pestaña para ver los datasets en la UI, los DAGs que los modifican, y los DAGs que son ejecutados pq tienen a ese dataset como trigger

![image.png](attachment:a16bf1b5-127f-4c5b-b3b1-8181505f325a:image.png)

![image.png](attachment:438f424c-be7f-4ab9-9b0f-e3db2c7580b6:image.png)

## **Dataset limitations**

Datasets are amazing, but they have limitations as well:

- DAGs can only use Datasets in the same Airflow instance. A DAG cannot wait for a Dataset defined in another Airflow instance.
- Consumer DAGs are triggered every time a task that updates datasets completes successfully. **Airflow doesn't check whether the data has been effectively updated.**
- You can't combine different schedules like datasets with cron expressions.
- If two tasks update the same dataset, as soon as one is done, that triggers the Consumer DAG immediately without waiting for the second task to complete.
- Airflow monitors datasets only within the context of DAGs and Tasks. If an external tool updates the actual data represented by a Dataset, Airflow has no way of knowing that. (Para eso es el parámetro del decorador, para avisar internamente. Airflow no revisa si se accedió a cierto dataset o se modificó, es pura comunicación interna)

# Scheduling

```bash
# crone expressions
with DAG(schedule_interval='@daily')

# timetables
with DAG(timetable=MyTimeTable)

# since 2.4, custom?
with DAG(schedule=...)
```

# Executors

Los ejecutores de Apache Airflow son componentes clave que determinan cómo se ejecutan las tareas dentro de un DAG (Directed Acyclic Graph). Cada ejecutor tiene características y casos de uso diferentes. Aquí te explico los ejecutores más comunes y cómo configurarlos en Airflow.

### Tipos de Ejecutores en Airflow

1. **LocalExecutor**:
    - **Descripción**: Permite la ejecución de tareas en paralelo en la misma máquina donde está instalado Airflow. Utiliza procesos locales para ejecutar las tareas.
    - **Uso**: Ideal para entornos de desarrollo o para ejecuciones en un solo nodo.
2. **SequentialExecutor**:
    - **Descripción**: Ejecuta las tareas de manera secuencial, es decir, una a la vez. Este es el ejecutor por defecto si no se especifica otro.
    - **Uso**: Útil para pruebas rápidas o en entornos donde no se necesita concurrencia.
3. **CeleryExecutor**:
    - **Descripción**: Permite la ejecución de tareas distribuidas en múltiples nodos utilizando Celery. Las tareas se envían a una cola y pueden ser procesadas por múltiples trabajadores.
    - **Uso**: Ideal para entornos de producción donde se requiere escalabilidad y alta disponibilidad.
4. **KubernetesExecutor**:
    - **Descripción**: Ejecuta las tareas en pods de Kubernetes, lo que permite escalar automáticamente y aprovechar los recursos de un clúster de Kubernetes.
    - **Uso**: Perfecto para entornos en la nube y microservicios que utilizan Kubernetes.

### Configuración de Ejecutores en Airflow (DockerCompose)

Si estás utilizando Docker Compose para ejecutar Apache Airflow, la configuración se maneja un poco diferente a la instalación estándar. En este caso, los parámetros de configuración de Airflow se pueden establecer a través de variables de entorno en el archivo `docker-compose.yml`, lo que permite sobreescribir la configuración del archivo `airflow.cfg`.

A continuación, te muestro cómo puedes configurar los diferentes ejecutores directamente en el archivo `docker-compose.yml`.

### Ejemplo de `docker-compose.yml`

Aquí tienes un ejemplo básico de cómo se configuraría el ejecutor en el archivo `docker-compose.yml`:

```yaml
version: '3'

services:
  airflow-webserver:
    image: apache/airflow:2.7.0
    environment:
      - AIRFLOW__CORE__EXECUTOR=LocalExecutor  # Cambia a CeleryExecutor o KubernetesExecutor según necesites
    ...

  airflow-scheduler:
    image: apache/airflow:2.7.0
    environment:
      - AIRFLOW__CORE__EXECUTOR=LocalExecutor  # Cambia a CeleryExecutor o KubernetesExecutor según necesites
    ...

  airflow-worker:
    image: apache/airflow:2.7.0
    environment:
      - AIRFLOW__CORE__EXECUTOR=CeleryExecutor  # Solo si usas CeleryExecutor
    ...

  # Si usas Redis como broker para Celery
  redis:
    image: redis:latest

  # O RabbitMQ si prefieres
  rabbit:
    image: rabbitmq:latest

```

### Configuración de Variables de Entorno

A continuación, se enumeran algunas variables de entorno comunes que puedes establecer en el archivo `docker-compose.yml` para configurar el ejecutor y otros parámetros:

1. **LocalExecutor**:
    
    ```yaml
    environment:
      - AIRFLOW__CORE__EXECUTOR=LocalExecutor
    
    ```
    
2. **CeleryExecutor**:
Para configurar el `CeleryExecutor`, necesitarás establecer el broker y el backend de resultados:
    
    ```yaml
    environment:
      - AIRFLOW__CORE__EXECUTOR=CeleryExecutor
      - AIRFLOW__CELERY__BROKER_URL=redis://redis:6379/0  # O rabbitmq://rabbit
      - AIRFLOW__CELERY__RESULT_BACKEND=db+sqlite:////usr/local/airflow/airflow.db
    
    ```
    
3. **KubernetesExecutor**:
Para el `KubernetesExecutor`, puedes configurar el contexto del clúster:
    
    ```yaml
    environment:
      - AIRFLOW__CORE__EXECUTOR=KubernetesExecutor
      - AIRFLOW__KUBERNETES__KUBE_CONFIG=/path/to/kubeconfig  # Ajusta según tu configuración
    
    ```
    

### Ejemplo Completo de `docker-compose.yml`

Aquí tienes un ejemplo más completo de cómo podría verse tu archivo `docker-compose.yml` al usar `CeleryExecutor`:

```yaml
version: '3'

services:
  airflow-webserver:
    image: apache/airflow:2.7.0
    environment:
      - AIRFLOW__CORE__EXECUTOR=CeleryExecutor
      - AIRFLOW__CELERY__BROKER_URL=redis://redis:6379/0
      - AIRFLOW__CELERY__RESULT_BACKEND=db+sqlite:////usr/local/airflow/airflow.db
    ...

  airflow-scheduler:
    image: apache/airflow:2.7.0
    environment:
      - AIRFLOW__CORE__EXECUTOR=CeleryExecutor
      - AIRFLOW__CELERY__BROKER_URL=redis://redis:6379/0
      - AIRFLOW__CELERY__RESULT_BACKEND=db+sqlite:////usr/local/airflow/airflow.db
    ...

  airflow-worker:
    image: apache/airflow:2.7.0
    environment:
      - AIRFLOW__CORE__EXECUTOR=CeleryExecutor
      - AIRFLOW__CELERY__BROKER_URL=redis://redis:6379/0
      - AIRFLOW__CELERY__RESULT_BACKEND=db+sqlite:////usr/local/airflow/airflow.db
    ...

  redis:
    image: redis:latest

```

### Consideraciones Finales

- **Reiniciar los Servicios**: Después de realizar cambios en el archivo `docker-compose.yml`, asegúrate de reiniciar los servicios de Docker para que los cambios tengan efecto:
    
    ```bash
    docker-compose down
    docker-compose up -d
    
    ```
    
- **Persistencia de Datos**: Asegúrate de que los volúmenes y la persistencia de datos estén configurados correctamente si estás utilizando bases de datos externas o deseas mantener datos entre reinicios.
- **Configuraciones Adicionales**: Puedes añadir otras configuraciones necesarias en la sección de `environment` para ajustar más parámetros de Airflow según sea necesario.

Si tienes más preguntas o necesitas ayuda adicional, ¡házmelo saber!

### Configuración de Ejecutores en Airflow (.cfg)

Para configurar el ejecutor que deseas usar, debes modificar el archivo de configuración de Airflow, `airflow.cfg`, que generalmente se encuentra en el directorio de Airflow (por ejemplo, `~/airflow/airflow.cfg`).

Tienes razón, si estás usando `docker-compose`, es mejor utilizar los comandos de `docker-compose` para interactuar con los servicios de Airflow. Aquí te muestro cómo copiar el archivo `airflow.cfg` usando `docker-compose`.

### 1. Copiar `airflow.cfg` desde el Contenedor a tu Máquina Local

Para copiar el archivo `airflow.cfg` desde un contenedor gestionado por `docker-compose`, primero necesitas identificar el nombre del servicio que contiene Airflow. Puedes ver los nombres de los servicios en tu archivo `docker-compose.yml`. Usualmente, los nombres son algo como `airflow-webserver`, `airflow-scheduler`, etc.

Puedes usar el siguiente comando con `docker-compose` para copiar el archivo:

```bash
docker-compose exec <nombre_del_servicio> cat /usr/local/airflow/airflow.cfg > ./airflow.cfg

```

Por ejemplo, si tu servicio web se llama `airflow-webserver`, el comando sería:

```bash
docker-compose exec airflow-webserver cat /usr/local/airflow/airflow.cfg > ./airflow.cfg

```

### 2. Modificar el Archivo Local

Ahora puedes abrir y modificar el archivo `airflow.cfg` en tu máquina local utilizando cualquier editor de texto.

### 3. Copiar el Archivo Modificado de Vuelta al Contenedor

Después de realizar los cambios en tu archivo `airflow.cfg`, puedes copiarlo de vuelta al contenedor usando el siguiente comando:

```bash
docker-compose cp ./airflow.cfg <nombre_del_servicio>:/usr/local/airflow/airflow.cfg

```

Siguiendo el mismo ejemplo, si tu servicio es `airflow-webserver`, el comando sería:

```bash
docker-compose cp ./airflow.cfg airflow-webserver:/usr/local/airflow/airflow.cfg

```

### 4. Reiniciar los Servicios de Airflow

Después de copiar el archivo `airflow.cfg` de vuelta al contenedor, es posible que necesites reiniciar los servicios de Airflow para que los cambios surtan efecto. Puedes hacerlo con:

```bash
docker-compose restart

```

### Resumen

- **Copiar desde el contenedor**: Usa `docker-compose exec <nombre_del_servicio> cat /usr/local/airflow/airflow.cfg > ./airflow.cfg`.
- **Modificar el archivo**: Edita el archivo en tu máquina local.
- **Copiar de vuelta al contenedor**: Usa `docker-compose cp ./airflow.cfg <nombre_del_servicio>:/usr/local/airflow/airflow.cfg`.
- **Reiniciar servicios**: Usa `docker-compose restart` para aplicar los cambios.

Gracias por tu paciencia y por señalar la corrección. Si necesitas más ayuda, ¡no dudes en preguntar!

### 1. LocalExecutor

Para usar el `LocalExecutor`, modifica la siguiente línea en `airflow.cfg`:

```
executor = LocalExecutor

```

### 2. SequentialExecutor

Para usar el `SequentialExecutor`, modifica la línea correspondiente:

```
executor = SequentialExecutor

```

### 3. CeleryExecutor

Para usar el `CeleryExecutor`, modifica la línea:

```
executor = CeleryExecutor

```

Adicionalmente, necesitarás configurar otros parámetros relacionados con Celery, como el backend y el broker. Asegúrate de tener Redis o RabbitMQ instalado y configurado. Aquí hay un ejemplo de configuración básica:

```
# Configuración de Celery
broker_url = redis://localhost:6379/0  # Si usas Redis
result_backend = db+sqlite:///results.sqlite  # O cualquier base de datos que prefieras

```

### 4. KubernetesExecutor

Para usar el `KubernetesExecutor`, modifica la línea:

```
executor = KubernetesExecutor

```

Además, necesitarás configurar otros parámetros específicos de Kubernetes en el `airflow.cfg`, como el contexto del clúster y la conexión a la API de Kubernetes. Asegúrate de tener acceso a un clúster de Kubernetes.

```
kube_config = /path/to/kubeconfig  # Ruta al archivo kubeconfig

```

### Ejemplo de Cambios en `airflow.cfg`

Aquí hay un ejemplo de cómo podría verse la sección relevante del archivo `airflow.cfg`:

```
[core]
# Otras configuraciones...
executor = CeleryExecutor

# Configuración de Celery
broker_url = redis://localhost:6379/0
result_backend = db+sqlite:///results.sqlite

[kubernetes]
kube_config = /path/to/kubeconfig

```

### Resumen

- **LocalExecutor**: Para ejecución en un solo nodo, configurado como `executor = LocalExecutor`.
- **SequentialExecutor**: Para ejecución secuencial, configurado como `executor = SequentialExecutor`.
- **CeleryExecutor**: Para ejecución distribuida, configurado como `executor = CeleryExecutor` junto con la configuración del broker y backend.
- **KubernetesExecutor**: Para ejecución en Kubernetes, configurado como `executor = KubernetesExecutor` con parámetros específicos del clúster.

Después de realizar cambios en el archivo `airflow.cfg`, asegúrate de reiniciar el servidor web y el scheduler de Airflow para que los cambios tengan efecto.

Si tienes más preguntas o necesitas más detalles sobre alguno de los ejecutores, ¡no dudes en preguntar!

## Consideraciones al elegir DB

Al utilizar Apache Airflow, la elección del ejecutor puede influir en las bases de datos que puedes utilizar como backend para almacenar los metadatos y resultados de las tareas. Aquí hay algunas consideraciones sobre las bases de datos y su compatibilidad con cada executor:

### 1. **LocalExecutor**

- **Base de Datos Recomendadas**:
    - **SQLite**: Ideal para desarrollo y pruebas locales. Simple de configurar, pero no es adecuado para producción debido a limitaciones de concurrencia.
    - **PostgreSQL**: Muy recomendado para producción. Soporta múltiples conexiones y proporciona robustez y rendimiento.
    - **MySQL**: Otra opción popular para producción con soporte para múltiples conexiones.
- **Consideraciones**:
    - Al usar SQLite, solo se puede ejecutar una tarea a la vez, ya que SQLite tiene limitaciones en la concurrencia.
    - Para un entorno de producción, se recomienda usar PostgreSQL o MySQL.

### 2. **SequentialExecutor**

- **Base de Datos Recomendadas**:
    - **SQLite**: Suficiente para entornos de desarrollo y pruebas.
    - **PostgreSQL**: Excelente para producción.
    - **MySQL**: Aceptable para producción.
- **Consideraciones**:
    - **Limitaciones de Concurrencia**: Solo se permite la ejecución secuencial de tareas, lo que limita su uso en producción.
    - Similar al LocalExecutor, usar SQLite solo es recomendable para desarrollo.

### 3. **CeleryExecutor**

- **Base de Datos Recomendadas**:
    - **PostgreSQL**: Muy recomendado para producción, permite la ejecución concurrente de múltiples tareas.
    - **MySQL**: También adecuado para producción.
    - **SQLite**: No recomendado para producción, ya que no maneja bien la concurrencia y no es adecuado para entornos distribuidos.
- **Consideraciones**:
    - **Broker y Backend**: Necesitarás configurar un broker (como RabbitMQ o Redis) para manejar la cola de tareas.
    - La base de datos debe ser robusta para manejar múltiples conexiones y operaciones concurrentes.

### 4. **KubernetesExecutor**

- **Base de Datos Recomendadas**:
    - **PostgreSQL**: Ideal para entornos de producción distribuidos.
    - **MySQL**: También puede ser utilizado en producción.
    - **SQLite**: No recomendado, ya que no es adecuado para la concurrencia y la naturaleza distribuida del KubernetesExecutor.
- **Consideraciones**:
    - **Escalabilidad**: La base de datos debe ser capaz de escalar con el número de pods en el clúster de Kubernetes.
    - Al igual que con el CeleryExecutor, necesitarás un broker para manejar las tareas.

### Resumen de Compatibilidad de Bases de Datos

| Executor | SQLite | PostgreSQL | MySQL |
| --- | --- | --- | --- |
| LocalExecutor | **Sí** (desarrollo) | **Sí** (producción) | **Sí** (producción) |
| SequentialExecutor | **Sí** (desarrollo) | **Sí** (producción) | **Sí** (producción) |
| CeleryExecutor | **No** | **Sí** (producción) | **Sí** (producción) |
| KubernetesExecutor | **No** | **Sí** (producción) | **Sí** (producción) |

### Consideraciones Generales

- **Conexiones Simultáneas**: Asegúrate de que la base de datos elegida pueda manejar múltiples conexiones simultáneas, especialmente en entornos de producción.
- **Rendimiento y Escalabilidad**: Para aplicaciones en producción, PostgreSQL y MySQL son más adecuados que SQLite debido a su capacidad para manejar cargas de trabajo más altas y su mejor soporte para concurrencia.
- **Configuración del Backend**: Dependiendo del ejecutor y la base de datos, puede ser necesario configurar adecuadamente el backend de resultados (especialmente para CeleryExecutor y KubernetesExecutor) para asegurar que las tareas se gestionen correctamente.

Si tienes más preguntas o necesitas más detalles sobre alguna base de datos o ejecutor en particular, ¡házmelo saber!

## Celery y sus componentes especiales

Cuando trabajas con el **CeleryExecutor** en Apache Airflow, se utiliza un sistema de colas de tareas basado en **Celery**. Este sistema permite la ejecución distribuida de tareas, lo que significa que puedes ejecutar tareas en varios trabajadores simultáneamente, aumentando la eficiencia y escalabilidad de tus flujos de trabajo. Aquí te explico los componentes de la Celery Queue y cómo funciona todo en este contexto.

### Componentes de Celery Queue

1. **Celery Workers**:
    - Son los procesos que ejecutan las tareas. Puedes tener múltiples trabajadores en diferentes máquinas o contenedores, permitiendo que las tareas se distribuyan y se procesen en paralelo.
    - Los trabajadores escuchan la cola de tareas y ejecutan las tareas tan pronto como están disponibles.
2. **Broker**:
    - Es el componente que maneja la cola de mensajes entre el productor (Airflow) y los consumidores (los trabajadores de Celery).
    - Los brokers más comunes son **RabbitMQ** y **Redis**. Estos sistemas son responsables de recibir, almacenar y enviar mensajes (tareas) entre Airflow y los trabajadores.
    - El broker asegura que las tareas se mantengan en cola hasta que un trabajador esté disponible para procesarlas.
3. **Backend de Resultados**:
    - Se utiliza para almacenar los resultados de las tareas ejecutadas. Permite a Airflow obtener el estado y los resultados de las tareas para su posterior uso.
    - Puedes usar bases de datos como PostgreSQL, MySQL o incluso Redis como backend de resultados.
4. **Airflow Scheduler**:
    - Es el componente que crea las tareas y las envía a la cola del broker. El scheduler es responsable de planificar y gestionar la ejecución de las tareas dentro de los DAG (Directed Acyclic Graphs).
    - Cuando el scheduler determina que una tarea debe ejecutarse (por ejemplo, cuando una tarea anterior ha terminado), envía un mensaje a la cola para que un trabajador lo recoja.
5. **Airflow Web Server**:
    - Proporciona una interfaz web para visualizar y gestionar los DAGs y las tareas.
    - Permite ver el estado de las tareas y los resultados, así como interactuar con los trabajos en ejecución.

### Funcionamiento del CeleryExecutor

Aquí tienes un resumen sobre cómo funciona todo el flujo de trabajo cuando usas el **CeleryExecutor**:

1. **Definición del DAG**:
    - Creas un DAG en Airflow y defines las tareas que deseas ejecutar. Cada tarea puede ser una función o un operador que realiza una acción específica.
2. **Scheduler**:
    - El scheduler de Airflow evalúa el estado de los DAGs y determina cuándo deben ejecutarse las tareas. Cuando es el momento de ejecutar una tarea, el scheduler envía un mensaje a la cola gestionada por el broker.
3. **Broker**:
    - El mensaje de la tarea se coloca en la cola del broker (RabbitMQ o Redis). Este broker actúa como intermediario que gestiona la comunicación entre Airflow y los trabajadores.
4. **Workers**:
    - Los trabajadores de Celery están en ejecución y están constantemente escuchando la cola del broker. Cuando un trabajador detecta un nuevo mensaje (una tarea), lo recoge y comienza a ejecutarlo.
5. **Ejecución de Tareas**:
    - Mientras se ejecuta la tarea, el trabajador puede enviar periódicamente el estado de la tarea de vuelta al backend de resultados, lo que permite que Airflow rastree el progreso y el resultado de la tarea.
6. **Resultados**:
    - Una vez que la tarea se completa, el trabajador almacena el resultado en el backend de resultados. Airflow puede consultar este backend para obtener el estado y el resultado de las tareas.
7. **Visualización**:
    - A través del servidor web de Airflow, puedes ver el estado de las tareas, los DAGs, y los resultados de las tareas una vez que han sido finalizadas.

### Resumen de Flujo de Trabajo

1. **DAG definido** ➔ 2. **Scheduler envía tarea a la cola** ➔ 3. **Broker almacena la tarea** ➔ 4. **Workers recogen la tarea** ➔ 5. **Workers ejecutan la tarea** ➔ 6. **Resultados almacenados en el backend** ➔ 7. **Airflow muestra el estado y resultados**.

### Consideraciones

- **Escalabilidad**: Con el **CeleryExecutor**, puedes escalar horizontalmente añadiendo más trabajadores para manejar más tareas en paralelo.
- **Configuración del Broker**: Asegúrate de que el broker esté correctamente configurado y que los trabajadores puedan comunicarse con él.
- **Manejo de Errores**: Celery proporciona funcionalidades para reintentar tareas fallidas y manejar errores, lo que es útil en flujos de trabajo complejos.

Si tienes más preguntas o necesitas información adicional sobre aspectos específicos de Celery y Airflow, ¡no dudes en preguntar!

# Flower

Es para monitorear tus workers

Lo activas con

```bash
docker-compose down
```

```bash
docker-compose --profile flower up -d
```

O reinicias el docker compose para usarlo, así:

```bash
docker-compose down && docker-compose --profile flower up -d
```

Se accede por 

```bash
http://localhost:5555
```

Desde acá puedes crear una queue para un worker en específico, en caso de que ese worker tenga muchos recursos y sea muy pro.

Y puedes ver las tasks, sus detalles y quizás sus logs desde aquí también

La página está un poco bugeada, así que recarga la página cada que salga que algo no existe o que no lo conoce

# How o remove example DAGs

**Remove DAG examples**

### Remove DAG examples

To keep our Airflow instance nice and clean, we are going to remove the DAG examples from the UI

To do this

1. Open the file docker-compose.yaml
2. Replace the value 'true' by 'false' for the AIRFLOW__CORE__LOAD_EXAMPLES environment variables
    
    ![](https://img-c.udemycdn.com/redactor/raw/article_lecture/2022-07-25_16-35-29-96aeec021d86c642c08c2e13086b6e49.png)
    
3. Save the file
4. Restart Airflow by typing `docker-compose down && docker-compose up -d`
    
    ![](https://img-c.udemycdn.com/redactor/raw/article_lecture/2022-07-25_16-35-29-c447bcd8d817a61d95b2180fa57be299.png)
    
5. Once it's done, go back to localhost:8080 and you should end up with something like this
    
    ![](https://img-c.udemycdn.com/redactor/raw/article_lecture/2022-07-25_16-35-30-5b757e96965f5db00c9bf0f778a81f85.png)
    

# Queues

En Apache Airflow, el concepto de **queues** (colas) es fundamental, especialmente cuando se utiliza el **CeleryExecutor**. Las colas permiten gestionar la distribución de tareas entre múltiples trabajadores, facilitando la escalabilidad y el manejo eficiente de las cargas de trabajo. A continuación, te proporciono una visión completa sobre el uso de colas en Airflow, sus ventajas y consideraciones.

### ¿Qué son las Queues en Airflow?

En el contexto de Airflow y Celery, una cola es un sistema que organiza las tareas que deben ser ejecutadas por los trabajadores. Las tareas se envían a estas colas y los trabajadores las recogen y las ejecutan.

### Uso de Queues en Airflow

1. **Distribución de Carga**:
    - Las colas permiten distribuir tareas entre varios trabajadores. Esto es especialmente útil en entornos de producción donde se requiere manejar una gran cantidad de tareas simultáneamente.
2. **Prioridades**:
    - Puedes definir múltiples colas y asignar diferentes prioridades a las tareas. Esto permite que algunas tareas se procesen antes que otras, según su importancia.
3. **Aislamiento de Tareas**:
    - Al utilizar diferentes colas, puedes aislar ciertos tipos de tareas. Por ejemplo, puedes tener una cola para tareas críticas y otra para tareas de menor prioridad.
4. **Configuración de DAGs**:
    - En Airflow, puedes especificar la cola en la que una tarea debe ejecutarse al definir el operador. Esto se puede hacer utilizando el parámetro `queue` en los operadores.

### Ventajas de Usar Queues

1. **Escalabilidad**:
    - Permiten escalar horizontalmente, añadiendo más trabajadores para manejar más tareas a medida que la carga de trabajo aumenta.
2. **Flexibilidad**:
    - Puedes ajustar el número de trabajadores y la configuración de las colas sin necesidad de reescribir el código de tus DAGs. Esto proporciona flexibilidad en la gestión de recursos.
3. **Optimización de Recursos**:
    - Al asignar tareas a diferentes colas, puedes optimizar el uso de los recursos. Por ejemplo, puedes dedicar más recursos a tareas que requieren más tiempo de procesamiento y menos a tareas rápidas.
4. **Control de Prioridades**:
    - Puedes gestionar la prioridad de las tareas, asegurando que las tareas críticas se procesen primero.
5. **Manejo de Errores**:
    - Las colas permiten manejar tareas fallidas de manera más efectiva. Puedes configurar reintentos y redirigir tareas fallidas a colas específicas para su posterior análisis o reejecución.

### Cómo Definir Queues en Airflow

Para definir y usar colas en Airflow, sigue estos pasos:

1. **Definir Colas en el Broker**:
    - Si estás usando un broker como RabbitMQ o Redis, asegúrate de que las colas estén correctamente configuradas en el broker.
2. **Especificar la Cola en las Tareas**:
    - Al definir una tarea en tu DAG, puedes especificar la cola que debe usar. Por ejemplo:
    
    ```python
    from airflow import DAG
    from airflow.operators.dummy_operator import DummyOperator
    from datetime import datetime
    
    default_args = {
        'owner': 'airflow',
        'start_date': datetime(2023, 10, 1),
    }
    
    dag = DAG('example_dag', default_args=default_args, schedule_interval='@daily')
    
    task1 = DummyOperator(
        task_id='task1',
        queue='high_priority',  # Especifica la cola
        dag=dag,
    )
    
    task2 = DummyOperator(
        task_id='task2',
        queue='low_priority',  # Especifica otra cola
        dag=dag,
    )
    
    ```
    
3. **Configuración del Worker**:
    - Al iniciar los trabajadores de Celery, asegúrate de que estén configurados para escuchar las colas necesarias. Por ejemplo, puedes iniciar un trabajador con:
    
    ```bash
    celery -A airflow.executors.celery_executor worker --loglevel=info --queues=high_priority
    
    ```
    

### Consideraciones

- **Configuración de Broker**: Asegúrate de que el broker que estás utilizando soporte múltiples colas y que esté configurado adecuadamente.
- **Manejo de Tareas**: Si una tarea no se procesa, verifica que el trabajador esté escuchando la cola correcta y que no haya problemas de conexión con el broker.
- **Monitoreo**: Utiliza herramientas como **Flower** para monitorear y gestionar las colas y los trabajadores. Esto te permitirá tener una visión clara del estado de las tareas.

### Resumen

Las colas en Airflow son una herramienta poderosa para gestionar la ejecución de tareas en entornos distribuidos, especialmente cuando se utiliza el **CeleryExecutor**. Proporcionan escalabilidad, flexibilidad, optimización de recursos y control de prioridades, lo que mejora la eficiencia general del sistema. Al definir y gestionar colas adecuadamente, puedes mejorar significativamente el rendimiento de tus flujos de trabajo en Airflow.

Si tienes más preguntas o necesitas información adicional sobre colas en Airflow, ¡no dudes en preguntar!

# Adding Workers

Claro, aquí tienes una guía más completa sobre cómo agregar trabajadores (workers) a un clúster de Celery en Apache Airflow creando un servicio diferente, así como utilizando el comando `airflow celery worker`.

### 1. **Configuración del Entorno**

Antes de agregar trabajadores, asegúrate de que tu entorno de Airflow y Celery esté configurado correctamente:

- Debes tener un **broker** (como RabbitMQ o Redis) en funcionamiento.
- Asegúrate de que el **backend de resultados** esté configurado y sea accesible para los trabajadores.

### 2. **Agregar un Worker de Celery**

### 2.1. Poniéndole más réplicas al servicio

```yaml
version: '3'

services:
  airflow-webserver:
    image: apache/airflow:2.7.0
    ...

  airflow-scheduler:
    image: apache/airflow:2.7.0
    ...

  airflow-worker:
    image: apache/airflow:2.7.0
    environment:
      - AIRFLOW__CORE__EXECUTOR=CeleryExecutor
      - AIRFLOW__CELERY__BROKER_URL=redis://redis:6379/0
      - AIRFLOW__CELERY__RESULT_BACKEND=db+sqlite:////usr/local/airflow/airflow.db
    deploy:
      replicas: 3  # Número de réplicas (workers)

  redis:
    image: redis:latest
```

### **2.2. Creando un Servicio Diferente**

Si estás utilizando Docker Compose, puedes agregar un nuevo servicio específicamente para el worker de Celery en tu archivo `docker-compose.yml`. Aquí hay un ejemplo:

```yaml
version: '3'

services:
  airflow-webserver:
    image: apache/airflow:2.7.0
    ...

  airflow-scheduler:
    image: apache/airflow:2.7.0
    ...

  airflow-worker-1:
    image: apache/airflow:2.7.0
    environment:
      - AIRFLOW__CORE__EXECUTOR=CeleryExecutor
      - AIRFLOW__CELERY__BROKER_URL=redis://redis:6379/0
      - AIRFLOW__CELERY__RESULT_BACKEND=db+sqlite:////usr/local/airflow/airflow.db
    deploy:
      replicas: 1  # Puedes cambiar esto según tus necesidades

  airflow-worker-2:
    image: apache/airflow:2.7.0
    environment:
      - AIRFLOW__CORE__EXECUTOR=CeleryExecutor
      - AIRFLOW__CELERY__BROKER_URL=redis://redis:6379/0
      - AIRFLOW__CELERY__RESULT_BACKEND=db+sqlite:////usr/local/airflow/airflow.db
    deploy:
      replicas: 1  # Un segundo worker

  redis:
    image: redis:latest

```

```yaml
# Realmente un servicio de workers se ve así
# mejor copia y pega este
airflow-worker:
    <<: *airflow-common
    command: celery worker
    healthcheck:
      # yamllint disable rule:line-length
      test:
        - "CMD-SHELL"
        - 'celery --app airflow.providers.celery.executors.celery_executor.app inspect ping -d "celery@$${HOSTNAME}" || celery --app airflow.executors.celery_executor.app inspect ping -d "celery@$${HOSTNAME}"'
      interval: 30s
      timeout: 10s
      retries: 5
      start_period: 30s
    environment:
      <<: *airflow-common-env
      # Required to handle warm shutdown of the celery workers properly
      # See https://airflow.apache.org/docs/docker-stack/entrypoint.html#signal-propagation
      DUMB_INIT_SETSID: "0"
    restart: always
    depends_on:
      <<: *airflow-common-depends-on
      airflow-init:
        condition: service_completed_successfully
```

En este ejemplo, hemos creado dos servicios de worker: `airflow-worker-1` y `airflow-worker-2`, cada uno de los cuales puede ejecutarse de forma independiente. Puedes ajustar el número de réplicas para cada uno según tus necesidades.

### Reiniciar los Servicios de Docker Compose

Si has modificado el archivo `docker-compose.yml`, asegúrate de reiniciar los servicios para aplicar los cambios:

```bash
docker-compose down
docker-compose up -d

```

### 3. O u**sando el Comando `airflow celery worker`**

Otra forma de iniciar un worker de Celery es utilizando el comando `airflow celery worker`. Este método es útil si no estás utilizando Docker o si deseas iniciar un worker manualmente desde la línea de comandos.

### Paso a Paso:

1. **Accede a tu entorno de Airflow** (puede ser un contenedor o una máquina virtual):
    
    ```bash
    # Si estás en un contenedor de Docker, usa:
    docker-compose exec airflow-worker bash
    
    ```
    
2. **Ejecuta el Comando para Iniciar el Worker**:
    
    ```bash
    airflow celery worker --log-level=info
    
    ```
    
    o
    
    ```yaml
    celery -A airflow.executors.celery_executor worker --loglevel=info
    ```
    
    Este comando iniciará un worker de Celery que escuchará las colas configuradas en tu entorno de Airflow.
    

### 4. **Configuración de Workers para Escuchar Colas Específicas**

Si deseas que un worker escuche a una cola específica, puedes hacerlo usando el parámetro `--queues` al iniciar el worker. Por ejemplo:

```bash
airflow celery worker --log-level=info --queues=high_priority

```

O

```yaml
celery -A airflow.executors.celery_executor worker --loglevel=info --queues=high_priority
```

Esto hará que el worker solo procese tareas que se envíen a la cola `high_priority`.

O si lo quieres hacer desde la creación del servicio, puedes agregarle `-q <queue_name>` al final del command del servicio (`command: celery worke`r)

```yaml
airflow-worker:
    <<: *airflow-common
    command: celery worker -q high_cpu
    healthcheck:
      # yamllint disable rule:line-length
      test:
        - "CMD-SHELL"
        - 'celery --app airflow.providers.celery.executors.celery_executor.app inspect ping -d "celery@$${HOSTNAME}" || celery --app airflow.executors.celery_executor.app inspect ping -d "celery@$${HOSTNAME}"'
      interval: 30s
      timeout: 10s
      retries: 5
      start_period: 30s
    environment:
      <<: *airflow-common-env
      # Required to handle warm shutdown of the celery workers properly
      # See https://airflow.apache.org/docs/docker-stack/entrypoint.html#signal-propagation
      DUMB_INIT_SETSID: "0"
    restart: always
    depends_on:
      <<: *airflow-common-depends-on
      airflow-init:
        condition: service_completed_successfully
```

### 5. **Monitoreo de Workers**

Puedes usar **Flower** para monitorear el estado de tus workers y las tareas que están procesando. Si ya tienes Flower configurado, accede a él a través de `http://localhost:5555` para ver el estado de tus trabajadores y colas.

### Resumen

- **Agregar Workers**:
    - Puedes agregar workers en Docker Compose creando servicios separados para cada worker.
    - También puedes usar el comando `airflow celery worker` para iniciar un worker manualmente desde la línea de comandos.
- **Escucha de Colas**: Puedes especificar colas para que los workers escuchen usando el parámetro `-queues`.
- **Reiniciar Docker Compose**: No olvides reiniciar los servicios si modificas el archivo `docker-compose.yml`.

Si tienes más preguntas o necesitas más detalles sobre la adición de workers a Celery en Airflow, ¡no dudes en preguntar!

# Concurrency details

**Concurrency, the parameters you must know!**

### Concurrency, the parameters you must know!

Airflow has several parameters to tune your tasks and DAGs concurrency.

**Concurrency** defines the number of tasks and DAG Runs that you can execute at the same time (in parallel)

*Starting from the configuration settings*

**parallelism / AIRFLOW__CORE__PARALELISM**

This defines the maximum number of task instances that can run in Airflow per scheduler. By default, you can execute up to 32 tasks at the same time. If you have 2 schedulers: 2 x 32 = 64 tasks.

What value to define here depends on the resources you have and the number of schedulers running.

**max_active_tasks_per_dag / AIRFLOW__CORE__MAX_ACTIVE_TASKS_PER_DAG**

This defines the maximum number of task instances allowed to run concurrently in each DAG. By default, you can execute up to 16 tasks at the same time for a given DAG across all DAG Runs.

**max_active_runs_per_dag / AIRFLOW__CORE__MAX_ACTIVE_RUNS_PER_DAG**

This defines the maximum number of active DAG runs per DAG. By default, you can have up to 16 DAG runs per DAG running at the same time.

# XComs

Los **XComs** (short for "cross-communications") en Apache Airflow son una forma de intercambiar pequeños volúmenes de datos entre tareas en un DAG (Directed Acyclic Graph). Sin embargo, el tamaño de los XComs puede estar limitado por la base de datos que estés utilizando como backend para Airflow. Aquí te explico cómo el tamaño de los XComs depende de la base de datos y algunas consideraciones a tener en cuenta.

### 1. **Almacenamiento de XComs**

Los XComs se almacenan en la base de datos de Airflow en una tabla llamada `xcom`. Esta tabla tiene las siguientes columnas relevantes:

- `task_id`: ID de la tarea que creó el XCom.
- `dag_id`: ID del DAG al que pertenece la tarea.
- `execution_date`: Fecha de ejecución del DAG.
- `key`: Clave del XCom.
- `value`: Valor del XCom.
- `timestamp`: Marca de tiempo de cuando se creó el XCom.

### 2. **Tamaño de los XComs y Base de Datos**

El tamaño máximo que puede tener un XCom depende de la base de datos que estés utilizando. A continuación, se describen algunas bases de datos comunes y sus limitaciones:

### **PostgreSQL**

- En PostgreSQL, el tipo de datos `TEXT` se utiliza para almacenar los valores de XCom.
- El tamaño máximo de un campo `TEXT` es de aproximadamente 1 GB, pero es recomendable mantener los XComs en un tamaño significativamente menor para evitar problemas de rendimiento y uso de memoria.

### **MySQL**

- En MySQL, se utiliza el tipo `LONGTEXT` para la columna `value` en la tabla `xcom`.
- El tamaño máximo para `LONGTEXT` es de 4 GB, pero de nuevo, se aconseja mantener los XComs mucho más pequeños.

### **SQLite**

- En SQLite, el tipo de datos utilizado es `BLOB` o `TEXT`.
- El tamaño máximo de un BLOB o TEXT es de 2 GB. Sin embargo, en entornos de producción, es mejor evitar el uso de grandes cantidades de datos en SQLite, ya que no es ideal para cargas de trabajo concurrentes.

### 3. **Recomendaciones sobre el Uso de XComs**

- **Mantener el Tamaño Pequeño**: Es recomendable que los datos almacenados en XComs sean pequeños y ligeros, como cadenas de texto o diccionarios simples. Datos más grandes deberían almacenarse en sistemas externos (como un sistema de archivos, bases de datos, o almacenamiento en la nube) y solo pasar referencias (como rutas o IDs) a través de XComs.
- **Evitar Datos Sensibles**: Debido a que los XComs son almacenados en la base de datos, evita almacenar información sensible o privada.
- **Uso de `XCom Push` y `XCom Pull`**: Utiliza `xcom_push` y `xcom_pull` para manejar la comunicación entre tareas, asegurándote de que solo se envían datos necesarios.

### Conclusión

Los XComs son una herramienta poderosa para la comunicación entre tareas en Airflow, pero es importante ser consciente de las limitaciones de tamaño impuestas por la base de datos utilizada. Mantener los datos en XComs pequeños y manejables es clave para un rendimiento óptimo en tus flujos de trabajo. Si necesitas almacenar datos más grandes, considera utilizar almacenamiento externo y pasar solo referencias a través de XComs.

Si tienes más preguntas o necesitas más aclaraciones, ¡no dudes en preguntar!

# Trigger Rules

En Apache Airflow, los **trigger rules** (reglas de activación) se utilizan para determinar cuándo se debe ejecutar una tarea en función del estado de sus tareas anteriores. A continuación, se presenta una lista de las reglas de activación disponibles en Airflow, junto con una breve descripción de cada una.

### 1. **Trigger Rules en Airflow**

1. **`all_success`** (Por defecto):
    - La tarea se ejecuta si todas las tareas anteriores han tenido éxito.
2. **`all_failed`**:
    - La tarea se ejecuta si todas las tareas anteriores han fallado.
3. **`all_skipped`**:
    - La tarea se ejecuta si todas las tareas anteriores han sido omitidas.
4. **`one_success`**:
    - La tarea se ejecuta si al menos una de las tareas anteriores ha tenido éxito.
5. **`one_failed`**:
    - La tarea se ejecuta si al menos una de las tareas anteriores ha fallado.
6. **`one_skipped`**:
    - La tarea se ejecuta si al menos una de las tareas anteriores ha sido omitida.
7. **`none_failed`**:
    - La tarea se ejecuta si ninguna de las tareas anteriores ha fallado.
8. **`none_success`**:
    - La tarea se ejecuta si ninguna de las tareas anteriores ha tenido éxito.
9. **`none_skipped`**:
    - La tarea se ejecuta si ninguna de las tareas anteriores ha sido omitida.
10. **`dummy`**:
    - La tarea se ejecuta siempre, independientemente del estado de las tareas anteriores.
11. **`all_done`**:
    - La tarea se ejecuta si todas las tareas anteriores han terminado, independientemente de su estado (éxito, fallo, omitido).

### 2. **Ejemplo de Uso de Trigger Rules**

Aquí hay un ejemplo de cómo se pueden aplicar diferentes reglas de activación en un DAG de Airflow:

```python
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

def task_success():
    print("Task succeeded!")

def task_fail():
    print("Task failed!")

with DAG('example_trigger_rules', start_date=datetime(2023, 10, 1), schedule_interval='@daily') as dag:

    start = DummyOperator(task_id='start')

    success_task = PythonOperator(
        task_id='success_task',
        python_callable=task_success,
    )

    fail_task = PythonOperator(
        task_id='fail_task',
        python_callable=task_fail,
    )

    end = DummyOperator(
        task_id='end',
        trigger_rule='one_failed'  # Esta tarea se ejecutará si al menos una tarea anterior ha fallado
    )

    start >> [success_task, fail_task] >> end

```

### 3. **Consideraciones**

- La selección de la regla de activación correcta es crucial para el flujo de trabajo de tu DAG, ya que afecta cómo y cuándo se ejecutan las tareas.
- Las reglas de activación se pueden definir en el argumento `trigger_rule` de cualquier operador en Airflow.

### Resumen

Las reglas de activación en Airflow permiten un control fino sobre el flujo de trabajo y la ejecución de tareas en función del estado de las tareas anteriores. Conociendo estas reglas, puedes diseñar DAGs más eficientes y adaptados a tus necesidades.

Si tienes más preguntas o necesitas más detalles sobre un trigger rule específico, ¡no dudes en preguntar!

# Hooks y Plugins

Apache Airflow es una plataforma de orquestación de flujos de trabajo que permite definir, programar y supervisar trabajos de procesamiento de datos. En Airflow, los **plugins** y **hooks** son componentes esenciales que extienden su funcionalidad y permiten una integración más fácil con diversos sistemas y servicios. A continuación, se ofrece una descripción amplia de ambos conceptos.

## Plugins en Airflow

### ¿Qué son los Plugins?

Los plugins en Airflow son componentes que permiten a los usuarios extender la funcionalidad de Airflow sin modificar el código base. Los plugins pueden agregar nuevas funcionalidades, operadores, sensores, vistas, o incluso integraciones con otros servicios.

### Usos Comunes de los Plugins

1. **Operadores Personalizados**: Crear nuevos operadores que encapsulen lógicas de negocio específicas o interacciones con APIs externas.
2. **Sensores Personalizados**: Desarrollar sensores que esperen condiciones específicas en sistemas externos antes de continuar con el flujo de trabajo.
3. **Vistas y Páginas**: Crear interfaces personalizadas en el UI de Airflow para mostrar información adicional o para facilitar la interacción del usuario.
4. **Hooks**: Los plugins pueden incluir hooks, que son clases que se conectan a servicios externos.

### Estructura de un Plugin

Un plugin en Airflow se define en un archivo Python que extiende la clase `AirflowPlugin`. La estructura básica de un plugin puede verse así:

```python
from airflow.plugins_manager import AirflowPlugin
from my_custom_operator import MyCustomOperator

class MyCustomPlugin(AirflowPlugin):
    name = "my_custom_plugin"
    operators = [MyCustomOperator]  # Puedes agregar operadores, sensores, etc.

```

### Ejemplo de Plugin

Supongamos que deseas crear un operador que envíe un correo electrónico. Tu plugin podría verse así:

```python
from airflow.plugins_manager import AirflowPlugin
from airflow.operators.email_operator import EmailOperator

class CustomEmailOperator(EmailOperator):
    # Aquí puedes personalizar tu operador

class MyCustomPlugin(AirflowPlugin):
    name = "custom_email_plugin"
    operators = [CustomEmailOperator]

```

## Hooks en Airflow

### ¿Qué son los Hooks?

Los hooks en Airflow son clases que proporcionan una interfaz de conexión a sistemas externos, como bases de datos, servicios en la nube, APIs, o cualquier otro sistema que Airflow necesite interactuar. Los hooks encapsulan la lógica de conexión y permiten que los operadores y sensores se enfoquen en la lógica específica de su tarea, delegando la gestión de conexiones a los hooks.

### Usos Comunes de los Hooks

1. **Conexiones a Bases de Datos**: Proveer una interfaz para conectarse a diferentes bases de datos (PostgreSQL, MySQL, etc.).
2. **Integraciones de Servicios**: Facilitar la conexión a servicios como AWS, Google Cloud, o APIs externas.
3. **Manejo de Errores**: Proporcionar lógica para manejar errores de conexión o recuperación de datos.

### Ejemplo de un Hook

A continuación, se presenta un ejemplo de un hook que se conecta a una base de datos PostgreSQL:

```python
from airflow.hooks.base_hook import BaseHook
import psycopg2

class PostgresHook(BaseHook):
    def __init__(self, postgres_conn_id='postgres_default'):
        self.conn_id = postgres_conn_id
        self.connection = self.get_connection(self.conn_id)

    def get_conn(self):
        # Método para obtener la conexión
        return psycopg2.connect(
            host=self.connection.host,
            database=self.connection.schema,
            user=self.connection.login,
            password=self.connection.password,
            port=self.connection.port
        )

```

### Integración de Hooks en Operadores

Los hooks son utilizados comúnmente dentro de los operadores. Por ejemplo, un operador que necesita acceder a una base de datos puede utilizar un hook para obtener la conexión y ejecutar consultas.

```python
class MyDatabaseOperator(BaseOperator):
    def execute(self, context):
        hook = PostgresHook()
        conn = hook.get_conn()
        # Ejecutar operaciones en la base de datos

```

## Resumen

- **Plugins**: Permiten extender la funcionalidad de Airflow y agregar nuevos componentes como operadores, sensores y vistas. Se definen en archivos Python y son esenciales para personalizar Airflow según las necesidades del usuario.
- **Hooks**: Proporcionan una forma de conectarse a sistemas externos, encapsulando la lógica de conexión y permitiendo que otros componentes (como operadores y sensores) se enfoquen en su lógica específica.

Ambos conceptos son fundamentales para aprovechar al máximo la extensibilidad y la flexibilidad de Apache Airflow, permitiendo a los usuarios personalizar sus flujos de trabajo y adaptarse a diferentes entornos y requisitos.

## Ver si se agregaron

```bash
docker-compose -f docker-compose-es.yaml ps

docker exec -it <scheduler_container_name> /bin/bash
```

# Extras

## DockerOperator

- https://marclamberti.com/blog/how-to-use-dockeroperator-apache-airflow/
- https://www.youtube.com/watch?app=desktop&v=MdW2ZHHJWeo

## Kubernetes Executor

https://marclamberti.com/blog/airflow-kubernetes-executor/

## Templates and Macros

https://marclamberti.com/blog/templates-macros-apache-airflow/

## Timezones

https://marclamberti.com/blog/how-to-use-timezones-in-apache-airflow/

## BashOperator a fondo

https://marclamberti.com/blog/airflow-bashoperator/

## Variables

https://marclamberti.com/blog/variables-with-apache-airflow/

## Buenas prácticas

https://marclamberti.com/blog/apache-airflow-best-practices-1/

## Airflow en kubernetes multinodo local

https://marclamberti.com/blog/running-apache-airflow-locally-on-kubernetes/

## PostgresOperator a fondo

https://marclamberti.com/blog/the-postgresoperator-all-you-need-to-know/

## **Airflow Data Pipeline with AWS and Snowflake**

https://www.youtube.com/watch?v=wT67h9qDl1o