import os

import mysql.connector
from utilities.credentialUtility import CredentialsUtility
import logging as logger
from configs.hosts_config import DB_HOST

class DBUtility:
    def __init__(self):
        self.dbCredentials = CredentialsUtility().getDBCredentials()

        self.machine = os.environ.get("MACHINE")
        assert self.machine,"Environment Variable 'MACHINE' mus be set"

        self.wp_host = os.environ.get("WP_HOST")
        assert self.wp_host,"Environment Variable 'WP_HOST' must be set"

        if self.machine == "docker" and self.wp_host == "local":
            raise Exception("Cannot run tests in docker if WP_HOSTS = local")

        self.env = os.environ.get("ENV")

        self.host = DB_HOST[self.machine][self.env]["host"]
        self.port = DB_HOST[self.machine][self.env]["port"]
        self.database = DB_HOST[self.machine][self.env]["database"]


    def createConnection(self):
        connection = mysql.connector.connect(host=self.host, user = self.dbCredentials["dbUser"],password = self.dbCredentials["dbPassword"],port = self.port,database = self.database)
        return connection


    def executeSelect(self,sql):
        connection = self.createConnection()
        try:
            logger.debug(f"Executing the Query: {sql}")
            cursor = connection.cursor(dictionary=True)
            cursor.execute(sql)
            response = cursor.fetchall()
            cursor.close()
        except Exception as e:
            raise Exception(f"Failed Running the query {sql} \n Error: {str(e)}")
        finally:
            connection.close()
        return response


    def executeSql(self):
        connection = self.createConnection()

