# Desc: Python 210 Final DataModel
# ChangeLog: (When,Who,What)
# 2/28/19,RRoot,Created Script
# 3/17/2019, RLarge, Modified Script

import re as rex
from sqlite3 import Error as sqlErr


class Product(object):

    def __init__(self, product_id: int, product_name: str):
        self.product_id = product_id
        self.product_name = product_name

    @property
    def product_id(self):
        return self.__product_id

    @product_id.setter
    def product_id(self, product_id):
        if type(product_id) is not int: raise TypeError("Requires integer!")
        if product_id <= 0: raise ValueError("Requires value greater than zero!")
        else: self.__product_id = product_id

    @property
    def product_name(self):
        return self.__product_name

    @product_name.setter
    def product_name(self, product_name):
        self.__product_name = str(product_name).strip()

    def __str__(self):
        return '{0}         {1}'.format(self.product_id, self.product_name)


class InventoryCount(object):

    def __init__(self, product_inventory_count: int, inventory_id: int, product_id: int):
        self.inventory_id = inventory_id
        self.__product_id = product_id
        self.__count = product_inventory_count


    @property
    def inventory_id(self):
        return self.__inventory_id

    @inventory_id.setter
    def inventory_id(self, inventory_id):
        if type(inventory_id) is not int: raise TypeError("Requires integer!")
        if inventory_id <= 0:
            raise ValueError("Requires a value greater than zero!")
        else:
            self.__inventory_id = inventory_id

    @property
    def product_id(self):
        return self.__product_id

    @product_id.setter
    def product_id(self, product_id: int):
        self.__product = product_id

    @property
    def product_inventory_count(self):
        return self.__count

    @product_inventory_count.setter
    def product_inventory_count(self, count: int):
        __count = count

    def __str__(self):
        return "{0}              {1}              {2}".format(self.product_inventory_count, self.inventory_id, self.product_id)

class Inventory(object):

    def __init__(self, inventory_id, inventory_date):
        self.inventory_date = inventory_date
        self.inventory_id = inventory_id

    @property
    def inventory_date(self):
        return self.__inventory_date

    @inventory_date.setter
    def inventory_date(self, inventory_date):
        if rex.match("\d\d\d\d-\d\d-\d\d", str(inventory_date)) is None:
            raise sqlErr("Not a Date!")
        else:
            self.__inventory_date = inventory_date

    @property
    def inventory_id(self):
        return self.__inventory_id

    @inventory_id.setter
    def inventory_id(self, inventory_id):
        if type(inventory_id) is not int: raise TypeError("Requires integer!")
        if inventory_id <= 0:
            raise ValueError("Requires a value greater than zero!")
        else:
            self.__inventory_id = inventory_id

    def __str__(self):
        return '{0}             {1}'.format(self.inventory_id, self.inventory_date)
