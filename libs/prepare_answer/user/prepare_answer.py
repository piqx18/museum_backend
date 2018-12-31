

class PrepareResultUser(object):

    @staticmethod
    def prepare_answer_exist_user(user):

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
    def prepare_answer_successful(user):

        result = {
            "result": "successful",
            "data_auth": {
                "login": user.login,
                "password": user.password
            }
        }

        return result

    @staticmethod
    def prepate_answer_not_exist_user(user):

        result = {
            "result": "error",
            "message": "USER NOT EXIST",
            "data_auth":
                {
                    "login": user.login,
                    "password": user.password,
                }
        }

        return result
