import math
import os
import random
import re
import sys


class VendingMachine:
    # Implement the VendingMachine here
    def __init__(self, item, price):
        self.stock = item
        self.price = price

    def buy(self, req_item, money):
        total_price = self.price * req_item
        change = money-total_price
        if self.stock >= req_item and total_price <= money:
            self.stock -= req_item
            return change
        elif self.stock < req_item:
            raise ValueError("Not enough items in the machine")
        elif total_price > money:
            raise ValueError("Not enough coins")



if __name__ == '__main__':

    num_items, item_coins = map(int, input().split())
    machine = VendingMachine(num_items, item_coins)

    n = int(input())
    for _ in range(n):
        num_items, num_coins = map(int, input().split())
        try:
            change = machine.buy(num_items, num_coins)
            print(change)
        except ValueError as e:
            print(e)