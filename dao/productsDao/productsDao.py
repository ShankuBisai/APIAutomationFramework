from utilities.dbUtility import DBUtility
import random

from utilities.genericUtility import GenericUtilities


class ProductDao(object):
    def __init__(self):
        self.dbUtility = DBUtility()

    def getRandomProductFromDatabase(self):
        sql = f"SELECT * FROM wp_posts WHERE post_type = 'product' LIMIT 1000;"
        response = self.dbUtility.executeSelect(sql)
        return random.sample(response,k =1)


    def getProductByNameFromDatabase(self,productName):
        sql =f"SELECT * FROM wp_posts WHERE post_name = '{productName}';"
        response = self.dbUtility.executeSelect(sql)
        return response


    def getProductByFilterFromDatabase(self,filter):
        if filter == "after":
            date = GenericUtilities.dateIsoFormat()
            sql = f"SELECT * FROM wp_posts WHERE post_type = 'product' and post_date > '{date}';"
        response = self.dbUtility.executeSelect(sql)
        return response




