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


@pytest.mark.orders
@pytest.mark.regression
@pytest.mark.parametrize("status",
                         [
                             pytest.param("cancelled",marks=[pytest.mark.tcid55,pytest.mark.smoke]),
                             pytest.param("completed",marks=pytest.mark.tcid56),
                             pytest.param("on-hold",marks=pytest.mark.tcid57),

                         ])
def testUpdateOrderStatus(status):
    orders = Orders()
    createOrdeResponse=orders.createOrder()
    currentStatus = createOrdeResponse["status"]
    assert  currentStatus != status, f"current status is already {status} not able to run the testcase"
    response=orders.updateOrder(createOrdeResponse["id"],status=status)
    newOrderStatus = orders.getOrderById(createOrdeResponse["id"])
    assert response["status"]==newOrderStatus["status"]














