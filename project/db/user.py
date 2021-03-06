from project.db.connect import open_connection_cursor, open_connection
from project.model import User


class UserDaoInterface:
    def get(self, username: str) -> User:
        """Select user by username"""
        pass

    def get_user_token(self, username: str) -> str:
        """Select user token by username"""
        pass

    def save(self, user: User) -> User:
        """Insert new user into DB"""
        pass


class UserDao(UserDaoInterface):

    def get(self, username: str) -> User:
        with open_connection_cursor() as cursor:
            cursor.execute('SELECT name, email, age FROM "user" WHERE username = %(username)s',
                           {'username': username})
            data = cursor.fetchone()
            if not data:
                print(f"User '{username}' not found")  # todo: exception
            else:
                return User(username=username, name=data[0], email=data[1], age=data[2])

    def get_user_token(self, username: str) -> str:
        with open_connection_cursor() as cursor:
            cursor.execute('SELECT token FROM "user" WHERE username = %(username)s',
                           {'username': username})
            data = cursor.fetchone()
            if not data:
                print(f"User '{username}' not found")  # todo: exception
            else:
                return data[0]

    def save(self, user: User) -> User:
        with open_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute('INSERT INTO "user" (username, name, email, age, token) VALUES(%s, %s, %s, %s, %s)',
                               (user.username, user.name, user.email, user.age, user.token))
                conn.commit()
                print(f"Successfully created user with username '{user.username}'")
        return user
