import logging as logger
from utilities.requestUtility import RequestUtlity
from utilities.genericUtility import GenericUtilities
from src.helpers.productsHelpers.productpayload import ProductsPayload
import json

class Products(object):

    def __init__(self):
        self.requestUtility = RequestUtlity()
        self.productPayload = ProductsPayload()

    def getAllProducts(self):
        logger.info("Getting all Products")
        getProductResponse = self.requestUtility.get("products")
        return json.loads(getProductResponse.text)


    def getProductByID(self,id):
        logger.info("Getting Products by ID")
        getProductResponse =  self.requestUtility.get(f"products/{id}")
        return json.loads(getProductResponse.text)


    def createProduct(self):
        logger.info("Creating a Product")
        randomString = GenericUtilities.generateRandomString(length=12)
        payload = self.productPayload.createProductPayload(productName = randomString)
        createProductResponse = self.requestUtility.post("products", payload=payload)
        return json.loads(createProductResponse.text), createProductResponse.status_code


    def listProductByFilter(self,*args):
        logger.info("Getting product by Filter")
        payload = dict()
        if args[0] == "after":
            payload["after"] = GenericUtilities.dateIsoFormat()
        if args[1] == "per_page":
            payload["per_page"] = 100

        getProductResponseFilter=self.requestUtility.get("products",payload=payload)
        return json.loads(getProductResponseFilter.text)


