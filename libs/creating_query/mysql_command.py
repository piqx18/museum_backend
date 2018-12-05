
class CreateCommand(object):

    @staticmethod
    def insert_user(login, password, token):

        command = "INSERT INTO users(login, password, token) VALUES ( '{}', '{}', '{}');".format(login, password, token)
        return command

    @staticmethod
    def check_user(login, password):
        command = "SELECT EXISTS(SELECT * FROM users WHERE login={} and password ={})".format(login, password)
        return command



