import pytest
from src.helpers.productsHelpers.products import Products
import pprint
from dao.productsDao.productsDao import ProductDao
import logging as logger


@pytest.mark.products
@pytest.mark.tcid24
def testlistAllProducts():
    products = Products()
    response=products.getAllProducts()
    assert response,f"There are no product"




@pytest.mark.products
@pytest.mark.tcid25
def testGetProductById():
    #get a product testdata from db
    productDao = ProductDao()
    responseDB=productDao.getRandomProductFromDatabase()

    #make a call
    products = Products()
    response=products.getProductByID(responseDB[0]["ID"])

    #verify the response
    assert responseDB[0]["ID"] == response["id"] ,"Wrong Product"



@pytest.mark.products
@pytest.mark.tcid26
def testcreateProduct():

    logger.info("TEST: Create new product with the POST call")
    products = Products()
    createProductResponse,statusCode=products.createProduct()
    assert statusCode == 201, "Product is not created"

    logger.info("TEST: Verify the product is present in the database")
    productDao = ProductDao()
    responseDB = productDao.getProductByNameFromDatabase(createProductResponse["name"])
    assert createProductResponse["name"] == responseDB[0]["post_name"]



@pytest.mark.tcid51
@pytest.mark.products
@pytest.mark.regression
def testListProductsWithAfterFilter():

    logger.info("TEST: Getting Products based on filter with the GET Call")
    products = Products()
    getProductResponseFilter=products.listProductByFilter("after","per_page")
    assert getProductResponseFilter , "There are no products"

    logger.info("TEST: Getting Products from the Database based on the filter")
    productDao = ProductDao()
    responseDB = productDao.getProductByFilterFromDatabase("after")
    assert len(getProductResponseFilter) == len(responseDB)






















