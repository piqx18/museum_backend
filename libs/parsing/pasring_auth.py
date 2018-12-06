
from collections import namedtuple
import json

UserSpec = namedtuple("UserSpec", "login password")

User = namedtuple("User", "id login password")

class Parsing(object):

    @staticmethod
    def pasring_user(data):

        data = json.loads(data)
        login = data.get("login")
        password = data.get("password")

        return UserSpec(login=login, password=password)


class ParsingAnswer(object):

    @staticmethod
    def parsing_result(data):

        assert isinstance(data, list)

        result_list = list()
        for user in data:
            result_list.append(User(id=user[0], login=user[1], password=user[2]))

        return result_list