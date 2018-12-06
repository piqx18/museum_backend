
from bottle import *
from museum_backend.server.list_actions.authorization.authorization import Auth


class Server(object):

    @staticmethod
    @post("/api/v1/authorization")
    def auth():
        data = request.body.read()
        _auth = Auth().auth(data=data)

    @staticmethod
    @post("/api/v1/getToken")
    def get_token():
        pass

    @staticmethod
    def run(host="0.0.0.0", port=8080):
        run(host=host, port=port)


if __name__ == '__main__':
    Server().run()
