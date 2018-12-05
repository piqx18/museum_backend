
from parsing.pasring_auth import Parsing
from creating_query.mysql_command import CreateCommand
from mysql_.client_mysql import ClientMysql


class Auth(object):

    def __init__(self):
        self.client = ClientMysql(host="localhost", port=3306, database="museum", user="root", passwd="qwer")

    def auth(self, data):
        user = Parsing.pasring_user(data)
        if self.check_user(user):
            return 1

    def check_user(self, user):
        query = CreateCommand.check_user(login=user.login, password=user.password)
        result = self.client.request(command=query)
        print(result)
