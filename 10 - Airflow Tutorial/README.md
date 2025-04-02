# Run

Correr con esto:
docker-compose up -d

Check container health con esto:
docker-compose ps

Puedes ver el resultado en:
localhost:8080

---

# Troubleshooting

Si uno está mal, ver el log con esto:
docker logs name_of_the_container

Luego de arreglar el problema, tumba el compose
docker-compose down

Y vuelve a montar con
docker-compose up -d