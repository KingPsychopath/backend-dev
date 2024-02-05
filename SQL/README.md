Playing around with Relational Databases and SQL; focusing on PostgreSQL and SQLite.

SQLite is serverless and is a good choice for small projects. PostgreSQL is a powerful, open source object-relational database system.


# PostgreSQL and MySQL

To create a new database in PostgreSQL, use the following command:
```sql
CREATE DATABASE database_name;
```

To create a new table in PostgreSQL, use the following command:
```sql
CREATE TABLE table_name (
    column1_name column1_type,
    column2_name column2_type,
    ...
);
```

To create a new user in PostgreSQL, use the following command:
```sql
CREATE USER username WITH PASSWORD 'password';
```

To grant a user all privileges on a database, use the following command:
```sql
GRANT ALL PRIVILEGES ON DATABASE database_name TO username;
```
