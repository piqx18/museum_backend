
from collections import namedtuple

UserSpec = namedtuple("UserSpec", "login password")

User = namedtuple("User", "user_id login password")


class ParsingUser(object):

    @staticmethod
    def pasring_user(data):

        login = data.get("login")
        password = data.get("password")

        return UserSpec(login=login, password=password)


class ParsingAnswerUser(object):

    @staticmethod
    def parsing_result(data):

        assert isinstance(data, list)
        user = data[0]

        return User(user_id=user[0], login=user[1], password=user[2])