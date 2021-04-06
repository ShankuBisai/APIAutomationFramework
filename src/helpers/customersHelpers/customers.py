#from utilities.genericUtility import generateRandomEmailAndPassword
from src.helpers.customersHelpers.customerpayload import CustomersPayload
import logging as logger
from utilities.genericUtility import GenericUtilities
from utilities.requestUtility import RequestUtlity
import json


class Customers(object):
    def __init__(self):
        self.requestUtility = RequestUtlity()
        self.customerPayload = CustomersPayload()


    def createCustomer(self,email = None):
        logger.info("Creating new customer")

        if email == None:
            emailPassword=GenericUtilities.generateRandomEmailAndPassword()
            email = emailPassword["email"]

        else:
            email = email
        payload = self.customerPayload.createCustomerPayload(email=email)  # {'email': 'testuser_hlnrewffek@gmail.com', 'password': 'cqrkWIYiVu'}
        createCustomerResponse = self.requestUtility.post("customers",payload=payload)
        return json.loads(createCustomerResponse.text),createCustomerResponse.status_code


    def getCustomerByID(self,id):
        logger.info("Finding customer by ID")
        getCustomerResponse = self.requestUtility.get("customers/"+str(id))
        return json.loads(getCustomerResponse.text),id








