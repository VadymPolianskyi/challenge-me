from project.model import User


class UserDaoInterface:
    def get(self, username: str) -> User:
        """Select user by username"""
        pass

    def save(self, user: User) -> User:
        """Insert new user into DB"""
        pass


class MockDB(UserDaoInterface):
    fake_users_db = {
        "johndoe": {
            "username": "johndoe",
            "name": "John Doe",
            "email": "johndoe@example.com",
            "age": 20,
            "token": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
        }
    }

    def get_user(self, username: str):
        if username in self.fake_users_db:
            user_dict = self.fake_users_db[username]
            return User(**user_dict)

    def save_user(self, user: User):
        return user
