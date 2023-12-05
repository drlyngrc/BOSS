import mysql.connector

class DatabaseConnection:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="barangay_official",
            connection_timeout=120,  # Increase timeout (in seconds)
        )

    def get_connection(self):
        return self.connection
