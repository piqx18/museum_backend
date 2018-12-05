
from collections import namedtuple
import json

User = namedtuple("Users", "login password")


class Parsing(object):

    @staticmethod
    def pasring_user(data):

        data = json.loads(data)
        login = data.get("login")
        password = data.get("password")

        return User(login=login, password=password)
