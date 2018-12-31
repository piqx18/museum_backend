# -*- coding: utf-8
from bottle import *
from museum_backend.server.list_actions.authorization.authorization import Auth
from museum_backend.server.list_actions.users.Users import Users


class Server(object):

    @staticmethod
    @post("/api/v1/user/authorization")
    def auth():
        data = request.body.read()
        return Auth().auth(data=data)

    @staticmethod
    @post("/api/v1/user/createuser")
    def create_user():
        data = request.body.read()
        return Users().create_user(data=data)

    @staticmethod
    @post("/api/v1/user/updateuser")
    def update_user():
        data = request.body.read()

        return Users().update_user(data=data)

    @staticmethod
    def run(host="0.0.0.0", port=8080):
        run(host=host, port=port)


if __name__ == '__main__':
    Server().run()
