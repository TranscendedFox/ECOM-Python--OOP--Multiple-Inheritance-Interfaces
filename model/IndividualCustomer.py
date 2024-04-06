from model.Customer import Customer

class IndividualCustomer(Customer):

    def __init__(self, id, first_name, last_name, bank_name, credit_card_number, money_amount):
        super().__init__(id, bank_name, money_amount)
        self.first_name = first_name
        self.last_name = last_name
        self.credit_card_number = credit_card_number
