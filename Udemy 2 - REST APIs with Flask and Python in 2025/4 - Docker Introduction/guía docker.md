Lo demás está aquí:
https://rest-apis-flask.teclado.com/docs/docker_intro/in_depth_docker_tutorial/

---

Crear imagen desde un Dockerfile
```docker build -t rest-apis-flask-python .```

Crear container a partir de una imagen, -p es para reenvío de puerto <externo>:<interno>
```docker run -p 5001:5000 rest-apis-flask-python```

Y el -d es para que corra en segundo plano, como daemon, y podrás usar tu terminal para algo más
```docker run -d -p 5001:5000 rest-apis-flask-python```

Para usar el compose del docker-compose.yaml
```docker compose up```

Para recrear:
```docker compose up --build --force-recreate --no-deps <service-name>```

Correr archivos específicos y que se vayan sobreescribiendo según cambios en los archivos de adelante:  
```docker compose -f docker-compose.yml -f docker-compose.debug.yml up```