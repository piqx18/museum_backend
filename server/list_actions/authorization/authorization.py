
from parsing.pasring_auth import Parsing, ParsingAnswer
from creating_query.mysql_command import CreateCommand
from mysql_.client_mysql import ClientMysql
from prepare_answer.auth.prepare_answer import PrepareResult


class Auth(object):

    def __init__(self):
        self.client = ClientMysql(host="localhost", port=3306, database="museum", user="root", passwd="qwer")

    def auth(self, data):
        """"
        ПРоверка если пользователь есть, вернуть ответ
        Если нет с таким логином NOT FOUND
        Если неверный пароль ACCESS DENIED
        {
            status: " successful",
           data_auth{
                        login,
                        password,
                        token"}

            data_access {
                        [ массив правк]
            }

        }
        """
        user = Parsing.pasring_user(data)

        result = self.check_user(user=user)
        if len(result) > 0:
            answer = PrepareResult.prepare_answer_success(user=result)
            return answer
            # Подготовка положительного ответа
        elif len(result) == 0:
            # вернуть негативный ответ NOT FOUND
            answer = PrepareResult.prepare_answer_not_found()
            return answer

    def check_user(self, user):
        query = CreateCommand.check_user(login=user.login, password=user.password)
        result = ParsingAnswer.parsing_result(self.client.request_select(command=query))
        return result
