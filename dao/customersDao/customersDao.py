from utilities.dbUtility import DBUtility
from utilities.genericUtility import GenericUtilities
import random

class CustomersDao(object):
    def __init__(self):
        self.dbUtility = DBUtility()

    def getCustomerFromDatabase(self,email):
        sql = f"SELECT * FROM wp_users WHERE user_email = '{email}';"
        response = self.dbUtility.executeSelect(sql)

    def  isCustomerInDatabase(self,email):
        sql = f"SELECT * FROM wp_users WHERE user_email = '{email}';"
        response = self.dbUtility.executeSelect(sql)
        isPresent=GenericUtilities.searchValueinListOfDictionary(response,"user_email",email)
        return isPresent

    def getRandomCustomerfromDatabase(self):
        sql = f"SELECT * FROM wp_users ORDER BY id DESC LIMIT 5000;"
        response = self.dbUtility.executeSelect(sql)
        return random.sample(response,k = 1)






