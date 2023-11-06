import mysql.connector

class DatabaseManager:
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

    def getConnection(self):
        return self.connection

    def close(self):
        if self.connection is not None and self.connection.is_connected():
            self.connection.close()