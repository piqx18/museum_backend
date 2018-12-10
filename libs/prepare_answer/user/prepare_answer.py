

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

    @staticmethod
    def prepare_answer_method_not_allowed():

        result = {
            "result": "error",
            "message": "method not allowed"
        }

        return result

    @staticmethod
    def prepare_answer_successful(user):

        result = {
            "result": "successful",
            "data_auth": {
                "login": user.login
            }
        }

        return result
