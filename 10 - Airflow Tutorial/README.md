# Run

Correr con esto:
```docker-compose up -d```

Check container health con esto:
```docker-compose ps```

Puedes ver el resultado en:
```localhost:8080```

## Flower y ElasticSearch

Correr con flower:
```docker-compose --profile flower up -d```

Y accedes a flower por:
```localhost:5555```

Correr con elasticsearch:
```docker-compose -f docker-compose-es.yaml up -d```
> necesitarás agregar `-f docker-compose-es.yaml` a cada comando que hagas

## Revisar Plugins
Entra al scheduler y ejecuta `airflow plugins`
```bash
docker-compose -f docker-compose-es.yaml ps

docker exec -it <scheduler_container_name> /bin/bash

airflow plugins
```
Sales del bash del contenedor con Ctrl+D

# Troubleshooting

La versión máxima de python es 3.12

Si uno está mal, ver el log con esto:
```docker logs name_of_the_container```

Luego de arreglar el problema, tumba el compose
```docker-compose down```

Y vuelve a montar con
```docker-compose up -d```

# Docker Guide

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
