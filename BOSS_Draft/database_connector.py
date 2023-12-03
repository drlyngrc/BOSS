# database_connector.py

import mysql.connector

class DatabaseConnector:
    def __init__(self, host, user, passwd, database):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            passwd=passwd,
            database=database
        )
        self.mycursor = self.connection.cursor()

    def commit(self):
        self.connection.commit()
        
    def execute_query(self, query, values=None):
        self.mycursor.execute(query, values)
        self.connection.commit()

    def fetch_all(self):
        return self.mycursor.fetchall()

    def get_cursor(self):
        return self.connection.cursor()
    
