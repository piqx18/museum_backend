
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

    # todo Дописать вставку в таблицы  rights

    @staticmethod
    def check_user(login):
        command = "SELECT * FROM users WHERE login='{}'".format(login)
        return command



