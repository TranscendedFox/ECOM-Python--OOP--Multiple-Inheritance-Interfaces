from abc import ABC, abstractmethod

class Bank(ABC):
    def __init__(self, bank_id, bank_name, num_employees, revenue, expenses, customers):
        self.bank_id = bank_id
        self.bank_name = bank_name
        self.num_employees = num_employees
        self.revenue = revenue
        self.expenses = expenses
        self.customers = customers

    def take_payment(self, customer, payment):
        if customer in self.customers:
            print(f"Taking payment of {payment} from customer {customer.name}")
            customer.get_payment(-1 * payment)
        else:
            print(f"Customer {customer.name} is not a customer of {self.bank_name}")

    def increase_revenue(self, revenue_to_add):
        self.revenue += revenue_to_add
        print(f"Revenue increased by {revenue_to_add}. New revenue: {self.revenue}")

    def increase_expenses(self, expenses_to_increase):
        self.expenses += expenses_to_increase
        print(f"Expenses increased by {expenses_to_increase}. New expenses: {self.expenses}")

    @abstractmethod
    def  calculate_customer_money(self):
        pass