from order import Order
from db import DB
from constants import update_range


class Workflow:
    def __init__(self, setupconfig):
        self.config = setupconfig

    def workflow(self):
        orderHistory = []
        for i in range(update_range):
            orderHistory.append([Order(config=self.config, currentOrderItr=order) for order in range(self.config.order_range)])
        database = DB(config=self.config)
        database.dbInsert(list=orderHistory)
