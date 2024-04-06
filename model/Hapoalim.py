import overrides
from model.Bank import Bank

class Hapoalim(Bank):

    @overrides
    def calculate_customer_money(self):

        total = 0
        for customer in self.customers:
            total += customer.money_amount

        self.revenue += total
