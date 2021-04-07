from dao.productsDao.productsDao import ProductDao
from utilities.requestUtility import RequestUtlity
from src.helpers.ordersHelpers.orderpayload import OrderPayload
import json
import logging as logger


class Orders(object):
    def __init__(self):
        self.requestUtility = RequestUtlity()
        self.orderPayload = OrderPayload()

    def createOrder(self):
        productDao = ProductDao()
        responseDB = productDao.getRandomProductFromDatabase()
        productId = responseDB[0]["ID"]
        payload = self.orderPayload.createOrderpayload(productId=productId)
        createOrderResponse = self.requestUtility.post("orders", payload=payload)
        return json.loads(createOrderResponse.text)


    def getOrderById(self,id):
        logger.info("Getting order by ID")
        getOrderResponse = self.requestUtility.get(f"orders/{id}")
        return json.loads(getOrderResponse.text)


    def updateOrder(self,id,**kwargs):
        logger.info("Updating order by ID")
        for k,v in kwargs.items():
            if k == "status":
                payload = {"status":v}
        updateOrderResponse=self.requestUtility.put(f"orders/{id}",payload=payload)
        return json.loads(updateOrderResponse.text)












