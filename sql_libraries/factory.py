from sqlite.connection import Connection as Sqlite_connection


def connection_factory(self, db_type):
    if db_type == 'sqlite':
        return Sqlite_connection
