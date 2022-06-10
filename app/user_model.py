from flask_login import UserMixin
from app.mysql_service import get_user

class  UserData:
    def __init__(self, username, password, first_name, last_name):
        self.id = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name


class UserModel(UserMixin):
    def __init__(self, user_data):
        self.id = user_data.id
        self.password = user_data.password
        self.first_name = user_data.first_name
        self.last_name = user_data.last_name

    @staticmethod
    def query(username):
        user = get_user(username)
        user_data = UserData(
            username = user.username,
            password = user.password,
            first_name = user.first_name,
            last_name = user.last_name
        )
        return UserModel(user_data)