

class PrepareResultUser(object):

    @staticmethod
    def prepare_answer_exist_user(user):

        user = user[0]
        result = {
            "result": "error",
            "message": "USER EXIST",
            "data_auth":
                {
                    "login": user.login,
                    "password": user.password,
                }
        }

        return result