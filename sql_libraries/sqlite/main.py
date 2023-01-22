import os
import sqlite3
from sqlite3 import Error

from constants import (
    CREATE_POSTS_TABLE, 
    CREATE_COMMMENTS_TABLE, 
    CREATE_LIKES_TABLE, 
    CREATE_USERS_TABLE,
    CREATE_USERS,
    CREATE_POSTS,
    CREATE_COMMENTS,
    CREATE_LIKES,
    SELECT_USERS,
    SELECT_POSTS,
    SELECT_USERS_POSTS,
    SELECT_POSTS_COMMENTS_USERS,
    SELECT_POST_LIKES,
    SELECT_POST_DESCRIPTION,
    UPDATE_POST_DESCRIPTION,
    DELETE_COMMENT,
    SELECT_COMMENT

)
def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occured")

    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occured")

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")

path = os.path.join(os.getcwd(), 'sql_libraries/sqlite/app_db.db')
connection = create_connection(path)
# USER
execute_query(connection, CREATE_USERS_TABLE)
#POST
execute_query(connection, CREATE_POSTS_TABLE)
# LIKE
execute_query(connection, CREATE_LIKES_TABLE)
# COMMENTS
execute_query(connection, CREATE_COMMMENTS_TABLE)


execute_query(connection, CREATE_USERS)

execute_query(connection, CREATE_POSTS)




execute_query(connection, CREATE_COMMENTS)
execute_query(connection, CREATE_LIKES)

print('--------------------Users-----------------------')


users = execute_read_query(connection, SELECT_USERS)

for user in users:
    print(user)

print('--------------------Posts------------------------')


posts = execute_read_query(connection, SELECT_POSTS)

for post in posts:
    print(post)


users_posts = execute_read_query(connection, SELECT_USERS_POSTS)

print('--------------------user-posts----------------------')

for users_post in users_posts:
    print(users_post)


posts_comments_users = execute_read_query(
    connection, SELECT_POSTS_COMMENTS_USERS
)

print('------------------posts-comments-users--------------------')

for post_comments_user in posts_comments_users:
    print(post_comments_user)


# how to get the column names of a table
# get columna names from the attribute description of the cursor
cursor = connection.cursor()
cursor.execute(SELECT_POSTS_COMMENTS_USERS)
cursor.fetchall()

column_names = [description[0] for description in cursor.description]
print(column_names)



post_likes = execute_read_query(connection, SELECT_POST_LIKES)

for post_like in post_likes:
    print(post_like)



post_description = execute_read_query(connection, SELECT_POST_DESCRIPTION)

for description in post_description:
    print(description)


execute_query(connection, UPDATE_POST_DESCRIPTION)


execute_query(connection, DELETE_COMMENT)


execute_read_query(connection, SELECT_COMMENT)