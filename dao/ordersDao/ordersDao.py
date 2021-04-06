from utilities.dbUtility import DBUtility
import random



class OrdersDao(object):
    def __init__(self):
        self.dbUtility = DBUtility()

    def getOrderByIdFromDatabase(self,id):
        sql = f"SELECT * FROM wp_wc_order_stats WHERE order_id = {id};"
        response = self.dbUtility.executeSelect(sql)
        return response

