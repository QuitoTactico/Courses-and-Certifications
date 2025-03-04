from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Cargar las variables de entorno desde un archivo .env específico
load_dotenv("ruta/a/tu/archivo.env")  # Reemplaza con la ruta a tu archivo .env

# Obtener la variable CLUSTER_URI
cluster_uri = os.getenv("CLUSTER_URI")

# Conectar a MongoDB
client = MongoClient(cluster_uri)
db = client["nombre_de_tu_base_de_datos"]  # Reemplaza con el nombre de tu base de datos
collection = db["nombre_de_tu_coleccion"]  # Reemplaza con el nombre de tu colección

# Realizar la consulta para obtener todos los nombres de restaurantes
nombres_restaurantes = collection.find({}, {"name": 1, "_id": 0})

# Imprimir los nombres
for restaurante in nombres_restaurantes:
    print(restaurante["name"])
