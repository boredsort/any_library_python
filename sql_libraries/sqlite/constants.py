CREATE_USERS_TABLE = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    gender TEXT,
    nationality TEXT
);
"""

CREATE_POSTS_TABLE = """
CREATE TABLE IF NOT EXISTS posts(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id)
);
"""

CREATE_COMMMENTS_TABLE = """
CREATE TABLE IF NOT EXISTS comments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    text TEXT NOT NULL,
    user_id INTEGER NOT NULL,
    post_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id) FOREIGN KEY (post_id) REFERENCES posts (id)
);
"""

CREATE_LIKES_TABLE = """
CREATE TABLE IF NOT EXISTS likes(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    post_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id) FOREIGN KEY (post_id) REFERENCES posts (id)
);
"""

CREATE_USERS = """
INSERT INTO
    users (name, age, gender, nationality)
VALUES 
    ('James', 25, 'male', 'USA'),
    ('Leila', 32, 'female', 'France'),
    ('Brigitte', 35, 'female', 'England'),
    ('Mike', 40, 'male', 'Denmark'),
    ('Elizabeth', 21, 'female', 'Canada');
"""

CREATE_POSTS = """
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


CREATE_COMMENTS = """
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

CREATE_LIKES = """
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

SELECT_USERS = "SELECT * FROM users"

SELECT_POSTS = 'SELECT * FROM posts'

SELECT_USERS_POSTS = """
SELECT
    users.id,
    users.name,
    posts.description
FROM
    posts
INNER JOIN users ON users.id = posts.user_id
"""

SELECT_POSTS_COMMENTS_USERS = """
SELECT
    posts.description as post,
    text as comment,
    name
FROM
    posts
INNER JOIN comments ON posts.id = comments.post_id
INNER JOIN users ON users.id = comments.user_id

"""

SELECT_POST_LIKES = """
SELECT
    description as Post,
    COUNT(likes.id) as Likes
FROM
    likes,
    posts
WHERE
    posts.id = likes.post_id
GROUP BY
    likes.post_id
"""

SELECT_POST_DESCRIPTION = "SELECT description FROM posts WHERE id = 5"

DELETE_COMMENT = "DELETE FROM comments WHERE id = 5"

SELECT_COMMENT = "SELECT * FROM comments WHERE id = 5"


UPDATE_POST_DESCRIPTION = """
UPDATE 
    posts
SET
    description = "The weather has become please now"
WHERE
    id = 2
"""
