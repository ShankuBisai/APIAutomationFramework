import os

class CredentialsUtility(object):
    def __init__(self):
        pass

    @classmethod
    def getWCAPIKeys(cls):
        wcKey = os.getenv("WC_KEY")
        wcSecret = os.getenv("WC_SECRET")

        if not wcKey or not wcSecret:
            raise Exception("The API credentials 'WC_KEY and 'WC_SECRET' must be in env variables")
        else:
            return {"wcKey" : wcKey , "wcSecret" : wcSecret}


    @classmethod
    def getDBCredentials(cls):
        dbUser = os.getenv("DB_USER")
        dbPassword = os.getenv("DB_PASSWORD")

        if not dbUser or not dbPassword:
            raise Exception("The DB credentials 'DB_USER and 'DB_PASSWORD' must be in env variables")
        else:
            return {"dbUser": dbUser, "dbPassword": dbPassword}
