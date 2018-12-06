# -*- coding: utf-8 -*-
from museum_backend.libs.creating_query.mysql_command import CreateCommand
from list_actions.authorization.authorization import BasicClient
from parsing.parsing_accaunts import ParsingAccount
from parsing.parsing_rights import ParsingRights
from parsing.pasring_users import ParsingUser, ParsingAnswerUser
from prepare_answer.user.prepare_answer import PrepareResultUser
import json


class Users(BasicClient):

    def create_user(self, data):
        data = json.loads(data)

        # берем данные
        data_auth = data["auth_data"]
        data_user = data["user_data"]
        data_rights = data["rights_data"]

        auth_spec = ParsingUser.pasring_user(data=data_auth)
        user_spec = ParsingAccount.pasring_accounts(data=data_user)
        rigts_spec = ParsingRights.parsing_rigths(data=data_rights)

        # проверяем что пользователя с таким логином нет
        result = self.check_exist_auth(auth_spec)
        if len(result) > 0:
            # возрвращаем ошибку, что пользователь с таким логином существует
            return PrepareResultUser.prepare_answer_exist_user(result)
        elif len(result) == 0:
            # заводим пользователя
            # 1. заводим запись в users
            # 2. добавляем в таблицу права для этого пользователя и личную информацию, переданную в запросе
            id_record = self.insert_users(auth_spec)
            self.insert_account(user_spec=user_spec, _id=id_record)

    def insert_account(self, user_spec, _id):
        query = CreateCommand.insert_accounts(surname=user_spec.surname, patronymic=user_spec.partonymic,
                                              name=user_spec.name, post=user_spec.post, email=user_spec.email,
                                              images=user_spec.image, user_id=_id)
        self.client.request_insert(command=query)

    def insert_rights(self, right_spec, _id):
        pass

    def insert_users(self, auth_data):

        query = CreateCommand.insert_user(login=auth_data.login, password=auth_data.password)
        id_record = self.client.request_insert(command=query)
        return id_record

    def check_exist_auth(self, auth_data):

        query = CreateCommand.check_user(login=auth_data.login)
        result = ParsingAnswerUser.parsing_result(self.client.request_select(command=query))

        return result
