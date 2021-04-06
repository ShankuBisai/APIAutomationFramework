import pytest
import pprint
from dao.ordersDao.ordersDao import OrdersDao
from src.helpers.ordersHelpers.orders import Orders


@pytest.mark.orders
@pytest.mark.tcid48
def testCreatePaidOrderGuestUser():
    orders = Orders()
    createOrdeResponse=orders.createOrder()
    getOrderResponse=orders.getOrderById(createOrdeResponse["id"])

    ordersDao = OrdersDao()
    responseDB=ordersDao.getOrderByIdFromDatabase(createOrdeResponse["id"])

    assert getOrderResponse["id"] == responseDB[0]["order_id"]



def testUpdateOrderStatus():
    pass













