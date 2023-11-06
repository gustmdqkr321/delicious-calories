import mysql.connector

class DatabaseUtils:
    def __init__(self):
        self.conn = None

    def mysql_connection(self):
        if self.conn is None or not self.conn.is_connected():
            self.conn = mysql.connector.connect(
                host="localhost",
                user="delicious_admin",
                password="123123123",
                database="delicious_calories_db"
            )
        return self.conn
