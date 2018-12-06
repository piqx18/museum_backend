

class PrepareResultAuth(object):

    @staticmethod
    def prepare_answer_success(user, access=None):

        user = user[0]
        result = {
            "result": "successful",
            "data_auth":
                {
                    "user_id": user.user_id,
                    "login": user.login,
                    "password": user.password,
                    "token": "ROOT"
                },
            "data_access": {}
        }

        return result

    @staticmethod
    def prepare_answer_access_denied(user):

        result = {
            "result": "error",
            "message": "ACCESS DENIED",
            "data_auth":
                {
                    "login": user.login,
                    "password": user.password
                }
        }

        return result

    @staticmethod
    def prepare_answer_not_found():
        result = {
            "result": "Error",
            "message": "NOT_FOUND"
        }
        return result
