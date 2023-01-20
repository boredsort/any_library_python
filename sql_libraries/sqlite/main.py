import os
import sqlite3
from sqlite3 import Error

from constants import CREATE_POSTS_TABLE, CREATE_COMMMENTS_TABLE, CREATE_LIKES_TABLE, CREATE_USERS_TABLE

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

create_users = """
INSERT INTO
    users (name, age, gender, nationality)
VALUES 
    ('James', 25, 'male', 'USA'),
    ('Leila', 32, 'female', 'France'),
    ('Brigitte', 35, 'female', 'England'),
    ('Mike', 40, 'male', 'Denmark'),
    ('Elizabeth', 21, 'female', 'Canada');
"""

execute_query(connection, create_users)

create_posts = """
INSERT INTO 
    posts (title, description, user_id)
VALUES
    ('Happy', 'I am feeling very happy today', 1),
    ('Hot Weather', 'The weather is very hot today', 2),
    ('Help', 'I need some help with my work', 2),
    ('Great News', 'I am getting married', 1),
    ('Interesting Game', 'It was a fantastic game of tennis', 5),
    ('Party', 'Anyone up for a late-night party today?', 3);
"""

execute_query(connection, create_posts)


create_comments = """
INSERT INTO
    comments (text, user_id, post_id)
VALUES 
    ('Count me in', 1, 6),
    ('What sort of help?', 5, 3),
    ('Congrats buddy', 2, 4),
    ('I was rooting for Nadal though', 4, 5),
    ('Help with your thesis?', 2, 3),
    ('Many congratulations', 5, 4);
"""

create_likes = """
INSERT INTO
    likes (user_id, post_id)
VALUES 
    (1, 6),
    (2, 3),
    (1, 5),
    (5, 4),
    (2, 4),
    (4, 2),
    (3, 6);
"""

execute_query(connection, create_comments)
execute_query(connection, create_likes)