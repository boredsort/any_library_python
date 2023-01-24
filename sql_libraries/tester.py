import factory
import os


path = os.path.join(os.getcwd(), 'sql_libraries/sqlite/app_db.db')
connection = factory.connection_factory('sqlite')
con = connection(path)