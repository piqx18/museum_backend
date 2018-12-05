import mysql.connector
import logging


class ClientMysql(object):

    def __init__(self, host, port, user, passwd, database):
        """
        :param host: host MySQL server
        :param port: port MySQL server
        :param user: login for authorization
        :param passwd: passwd for authorization
        :param database: name database
        """
        logging.basicConfig(level=logging.INFO)
        try:
            logging.info(msg="Try to connect to MySQL database")
            self.db = mysql.connector.connect(
                host=host,
                port=port,
                user=user,
                passwd=passwd,
                database=database
            )
            logging.info(msg="Successful connect to database")
        except Exception as e:
            logging.error(msg="Error while connect to database, {}".format(e))

    def request(self, command):
        try:
            logging.info(msg="Try {command} to database".format(command=command))
            cursor = self.db.cursor()
            cursor.execute("{}".format(command))
            data = self.db.commit()
            logging.info(msg="receive data - {} from database".format(data))
            return data
        except Exception as ex:
            logging.error(msg="error - {}".format(ex))