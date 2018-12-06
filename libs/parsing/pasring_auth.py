
from collections import namedtuple
import json

UserSpec = namedtuple("Users", "login password")


class Parsing(object):

    @staticmethod
    def pasring_user(data):

        data = json.loads(data)
        login = data.get("login")
        password = data.get("password")

        return UserSpec(login=login, password=password)


class ParsingAnswer(object):
    pass