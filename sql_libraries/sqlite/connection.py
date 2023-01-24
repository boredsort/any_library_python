import os
import sqlite3
from sqlite3 import Error

from ..base import ConnectionClient


class Connection(ConnectionClient):

    def __init__(self, path):
        self._connection = self.create_connection(path)

    def create_connection(self, path):
        connection = None
        try:
            connection = sqlite3.connect(path)
            print("Connection to SQLite DB successful")
        except Error as e:
            print(f"The error '{e}' occured")

        return connection

    def execute_query(self, query):
        cursor = self._connection.cursor()
        try:
            cursor.execute(query)
            self.connection.commit()
            print("Query executed successfully")
        except Error as e:
            print(f"The error '{e}' occured")

    def execute_read_query(self, query):
        cursor = self._connection.cursor()
        result = None
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as e:
            print(f"The error '{e}' occurred")
