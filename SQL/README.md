Playing around with Relational Databases and SQL; focusing on PostgreSQL and SQLite.

SQLite is serverless and is a good choice for small projects. PostgreSQL is a powerful, open source object-relational database system.


# SQLite
There are no users, roles, or permissions in SQLite. It is a serverless database, meaning that it is not a client-server database engine. It is embedded into the end program.

You can pipe .SQL files into SQLite using the following command:
```bash
sqlite3 < query.sql
```

You can also use the following command to create a new database:
```bash
sqlite3 database.db
```

To create a new table in SQLite, use the following command:
```sql
CREATE TABLE table_name (
    column1_name column1_type,
    column2_name column2_type,
    ...
);
``` 

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

# Importing CSV Files

To convert a `.csv` file to a `.db` file in SQLite, you can use the `.import` command provided by SQLite. Here's a step-by-step guide:

1. Open your terminal.
2. Start the SQLite shell with the name of the new database file. If the file doesn't exist, SQLite will create it:

```bash
sqlite3 new_database.db
```

3. Once you're in the SQLite shell, set the mode to CSV:

```sql
.mode csv
```

4. Import your CSV file into a new table. Replace `TableName` with the name you want for your table, and `file.csv` with the path to your CSV file:

```sql
.import file.csv TableName
```

5. Now your CSV data is imported into a SQLite database. You can verify it by selecting data from the table:

```sql
SELECT * FROM TableName;
```

6. To exit the SQLite shell, use the `.exit` command:

```sql
.exit
```

Remember to replace `new_database.db`, `TableName`, and `file.csv` with your actual database name, table name, and CSV file path.