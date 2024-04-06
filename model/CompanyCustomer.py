from model.Customer import Customer

class CompanyCustomer(Customer):

    def __init__(self, id, name, bank_name, money_amount):
        super().__init__(id, bank_name, money_amount)
        self.name = name