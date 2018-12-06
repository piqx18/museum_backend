
from collections import namedtuple
import json

AccountSpec = namedtuple("AccountSpec", "surname name partonymic post email image")


class ParsingAccount(object):

    @staticmethod
    def pasring_accounts(data):

        surname = data["surname"]
        name = data["name"]
        partonymic = data["partonymic"]
        post = data["post"]
        email = data["email"]
        image = data["image"]

        return AccountSpec(surname=surname, name=name, partonymic=partonymic, post=post, email=email, image=image)


class ParsingAnswerAccount(object):

    @staticmethod
    def parsing_result(data):
        pass