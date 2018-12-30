
from parsing.pasring_users import ParsingUser, ParsingAnswerUser
from parsing.parsing_rights import ParsingRightsAnswer
from creating_query.mysql_command import CreateCommand
from mysql_.client_mysql import ClientMysql
from prepare_answer.auth.prepare_answer import PrepareResultAuth
import json


class BasicClient(object):

    def __init__(self):
        self.client = ClientMysql(host="localhost", port=3306, database="museum", user="root", passwd="qwer",
                                  charset="utf8")


class Auth(BasicClient):

    def auth(self, data):
        """"
        Проверка если пользователь есть, вернуть ответ с правами
        Если нет с таким логином NOT FOUND
        Если неверный пароль ACCESS DENIED
        """
        data = json.loads(data)
        user = ParsingUser.pasring_user(data)
        result = self.check_user(user=user)
        if len(result) > 0 and result[0].password == user.password:
            # запрашиваем права пользователя
            query = CreateCommand.request_rights(user_id=result[0].user_id)
            rights = ParsingRightsAnswer.prepare_rights_answer(self.client.request_select(command=query))
            answer = PrepareResultAuth.prepare_answer_success(user=result, access=rights)
            return answer
            # Подготовка положительного ответа
        elif len(result) == 0:
            # вернуть негативный ответ NOT FOUND
            answer = PrepareResultAuth.prepare_answer_not_found()
            return answer
        elif len(result) > 0 and result[0].password != user.password:
            # вернуть негативный ответ ACCESS DENIED
            answer = PrepareResultAuth.prepare_answer_access_denied(user=user)
            return answer

    def check_user(self, user):
        query = CreateCommand.check_user(login=user.login)
        result = ParsingAnswerUser.parsing_result(self.client.request_select(command=query))
        return result
