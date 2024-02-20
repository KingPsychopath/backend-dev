import sqlite3

class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
       # self.cursor.execute('''CREATE TABLE IF NOT EXISTS players
        #               (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, sport TEXT)''')
        
        
    def _execute(self, query, params=()):
        self.cursor.execute(query, params)
        self.conn.commit()
        self.conn.close()

    def insert_data(self, table_name, data):
        placeholders = ', '.join('?' * len(data))
        self._execute(f'INSERT INTO {table_name} VALUES ({placeholders})', tuple(data.values()))
        
    def create_table(self, table_name, fields):
        fields_str = ', '.join(f'{name} {type}' for name, type in fields.items())
        self.cursor.execute(f'CREATE TABLE IF NOT EXISTS {table_name} ({fields_str})')

    def insert_data(self, table_name, data):
        placeholders = ', '.join('?' * len(data))
        self.cursor.execute(f'INSERT INTO {table_name} VALUES ({placeholders})', tuple(data.values()))
        self.conn.commit()

    def query_data(self, table_name, condition=None):
        self.cursor.execute(f'SELECT * FROM {table_name}' + (f' WHERE {condition}' if condition else ''))
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()