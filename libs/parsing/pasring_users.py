
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

        result_list = list()
        for user in data:
            result_list.append(User(user_id=user[0], login=user[1], password=user[2]))

        return result_list
