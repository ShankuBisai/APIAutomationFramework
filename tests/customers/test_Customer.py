
import pytest
import logging as logger
import pprint
from src.helpers.customersHelpers.customers import Customers
from dao.customersDao.customersDao import CustomersDao
import json


@pytest.mark.tcid29
@pytest.mark.customers
def testCreateCustomer():

    logger.info("TEST: Create new customer with the POST call")
    customer = Customers()
    response,statusCode=customer.createCustomer()
    assert statusCode == 201 , "Customer is not created"
    logger.info("TEST: Verify the customer is present in the database")
    customerDao = CustomersDao()
    assert customerDao.isCustomerInDatabase(response["email"]) == True , "Customer is not present in the database"



@pytest.mark.tcid30
@pytest.mark.customers
def testRetrieveCustomer():
    logger.info("TEST: Retrieve a customer by ID")
    customer = Customers()
    response,id = customer.getCustomerByID(10)
    assert response["id"] == id , f"Customer is not present with the id"




@pytest.mark.tcid47
@pytest.mark.customers
def testCreateCustomerExistingEmail():

    #get existing email from DB
    customerDao = CustomersDao()
    responseDB=customerDao.getRandomCustomerfromDatabase()
    responseEmail = responseDB[0]["user_email"]

    #create customer with the same mail by calling the createCustomer api
    customers = Customers()
    response, statusCode = customers.createCustomer(responseEmail)
    assert json.dumps(response["code"]).find("An account is already registered with your email address") == -1





