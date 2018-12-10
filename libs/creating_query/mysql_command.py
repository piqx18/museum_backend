class CreateCommand(object):

    @staticmethod
    def insert_user(login, password):
        command = "INSERT INTO users(login, password) VALUES ( '{}', '{}');".format(login, password)
        return command

    @staticmethod
    def insert_accounts(surname, name, patronymic, post, email, images, user_id):
        command = "INSERT INTO accounts(user_id, surname, name, patronymic, post, email, image) VALUES (" \
                  "'{user_id}','{surname}', '{name}','{patronymic}','{post}','{email}','{images}')" \
                  "".format(surname=surname, name=name, patronymic=patronymic, post=post, email=email, images=images,
                            user_id=user_id)
        return command

    @staticmethod
    def insert_rights(confirmed, allow_read, allow_write, allow_partial_edit, allow_edit, allow_manage, allow_print,
                      blocked, user_id):
        command = "INSERT INTO rights(user_id, confirmed, allow_read, allow_write, allow_partial_edit, allow_edit," \
                  "allow_manage, allow_print, blocked) VALUES ( '{user_id}', '{confirmed}'," \
                  " '{allow_read}', '{allow_write}', '{allow_partial_edit}', '{allow_edit}', '{allow_manage}', " \
                  "'{allow_print}', " \
                  "'{blocked}')".format(user_id=user_id, confirmed=confirmed, allow_read=allow_read,
                                        allow_write=allow_write,
                                        allow_partial_edit=allow_partial_edit, allow_edit=allow_edit,
                                        allow_manage=allow_manage,
                                        allow_print=allow_print, blocked=blocked)

        return command

    @staticmethod
    def check_user(login):
        command = "SELECT * FROM users WHERE login='{}'".format(login)
        return command
