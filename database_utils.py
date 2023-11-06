# database_utils.py
import sqlite3

class DatabaseUtils:
    def __init__(self):
        self.conn = None

    def sqlite_connection(self):
        db_file = "userdata.db"
        if self.conn is None:
            self.conn = sqlite3.connect(db_file)
        return self.conn
