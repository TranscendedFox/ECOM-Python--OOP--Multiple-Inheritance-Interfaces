from abc import ABC

class Customer(ABC):

    def __init__(self, id, bank_name, money_amount):
        self.id = id
        self.bank_name = bank_name
        self.money_amount = money_amount

    def get_payment(self, salary):
        self.money_amount += salary
