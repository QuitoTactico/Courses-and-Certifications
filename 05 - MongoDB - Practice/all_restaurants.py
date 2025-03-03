from mongodb_connection import MongoDB_Connection

collection = MongoDB_Connection("sample_restaurants", "restaurants").connect()

# Realizar la consulta para obtener todos los nombres de restaurantes
nombres_restaurantes = collection.find({}, {"name": 1, "_id": 0})

print(list(nombres_restaurantes)[:100])

# Imprimir los nombres
# for restaurante in nombres_restaurantes[:100]:
#    print(restaurante['name'])
