#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0 
        self.items = []
        self.last_transaction = None

    def add_item(self,title,price, quantity = 1):
        self.last_transaction = (title,price,quantity)
        for _ in range(quantity):
            self.items.append(title)
            self.total += price
    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
        else:
            discounted_amount = self.total * (self.discount / 100)
            self.total -= discounted_amount
            print(f"After the discount, the total comes to ${int(self.total)}.")
    def void_last_transaction(self):
        last_transiction_list = list(self.last_transaction)  
        self.total -= last_transiction_list[1]
        if self.total - last_transiction_list[1]:
            return self.total
        else: 
            self.total = 0
            return self.total