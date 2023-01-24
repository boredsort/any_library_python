from abc import ABC, abstractmethod


class ConnectionClient(ABC):

    pass


    def execute_query(self, query):
        pass


    def execute_read_query(self, query):
        pass