

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
            # todo добавить оставшиеся права
            "data_access": {
                "allow_read": access.allow_read,
                "allow_write": access.allow_write,
                "allow_partial_edit": access.allow_partial_edit,
                "allow_edit": access.allow_edit,
                "allow_manage": access.allow_manage,
                "allow_print": access.allow_print
            }
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
