import sqlite3


class DB:
    path = ''

    _db_connection = None
    _db_cur = None

    def __init__(self, path):
        self.path = path
        self._db_connection = sqlite3.connect(self.path)
        self._db_cur = self._db_connection.cursor()

    def query(self, query):
        return self._db_cur.execute(query)

    def fetch(self, query):
        return self._db_cur.execute(query).fetchall()

    def save(self):
        self._db_connection.commit()

    def __del__(self):
        self._db_connection.close()