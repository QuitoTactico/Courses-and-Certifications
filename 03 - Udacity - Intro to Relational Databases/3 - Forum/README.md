```bash
psql -U postgres
```

> put the password

Then use this to create the database:

```sql
CREATE DATABASE forum;
```

> This to move into the db:

```bash
\c forum
```

And then, create the table:
```sql
CREATE TABLE posts ( content TEXT,
                     time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                     id SERIAL );
```


Run the app with:
````bash
flask run
```