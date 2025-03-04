from mongodb_connection import MongoDB_Connection

collection = MongoDB_Connection("sample_restaurants", "restaurants").connect()

query_option = int(input("Query de 1 a 11: "))

if query_option == 1:

    # 1. Write a MongoDB query to display all the documents in the collection restaurants for all the documents in the collection restaurant
    response = collection.find(filter={}, projection={})

elif query_option == 2:

    # 2. Write a MongoDB query to display the fields restaurant_id, name, borough and cuisine
    response = collection.find(
        filter={},
        projection={"restaurant_id": 1, "name": 1, "borough": 1, "cuisine": 1},
    )

elif query_option == 3:

    # 3. Write a MongoDB query to display the fields restaurant_id, name, borough and zip code, but exclude the field _id for all the documents in the collection restaurant.
    response = collection.find(filter={}, projection={"name": 1, "_id": 0})

elif query_option == 4:

    # 4. Write a MongoDB query to display all the restaurant which is in the borough Bronx
    response = collection.find(filter={}, projection={"name": 1, "_id": 0})

elif query_option == 5:

    # 5. Write a MongoDB query to display the first 5 restaurants which are in the borough Bronx.
    response = collection.find(filter={}, projection={"name": 1, "_id": 0})

elif query_option == 6:

    # 6. Write a MongoDB query to find the restaurants who achieved a score more than 90.
    response = collection.find(filter={}, projection={"name": 1, "_id": 0})

elif query_option == 7:

    # 7. Write a MongoDB query to find the restaurants that achieved a score, more than 80 but less than 100
    response = collection.find(filter={}, projection={"name": 1, "_id": 0})

elif query_option == 8:

    # 8. Write a MongoDB query to find the restaurants that do not prepare any cuisine of 'American' and their grade score more than 70 and latitude less than -65.754168
    response = collection.find(filter={}, projection={"name": 1, "_id": 0})

elif query_option == 9:

    # 9. Write a MongoDB query to find the restaurants which do not prepare any cuisine of 'American' and achieved a score more than 70 and located in the longitude less than -65.754168.
    response = collection.find(filter={}, projection={"name": 1, "_id": 0})

elif query_option == 10:

    # 10. Write a MongoDB query to find the restaurant Id, name, borough and cuisine for those restaurants which contain 'Wil' as first three letters for its name.
    response = collection.find(filter={}, projection={"name": 1, "_id": 0})

elif query_option == 11:

    # 11. Write a MongoDB query to find the restaurant name, borough, longitude and latitude and cuisine for those restaurants which contain 'Mad' as first three letters of its name.
    response = collection.find(filter={}, projection={"name": 1, "_id": 0})


for restaurante in response[:100]:
    print(restaurante)
