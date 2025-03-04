import sqlite3

conn = sqlite3.connect("Cookies")
cursor = conn.cursor()

# o simplemente "select host_key from cookies limit 10"
query = """
    SELECT host_key 
    FROM cookies 
    LIMIT 10;
"""
cursor.execute(query)

results = cursor.fetchall()

print(results)

conn.close()
