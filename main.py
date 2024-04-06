from model.CompanyCustomer import CompanyCustomer
from model.Discount import Discount
from model.Hapoalim import Hapoalim
from model.IndividualCustomer import IndividualCustomer
from model.Leomi import Leomi

if __name__ == '__main__':

    customer1 = IndividualCustomer(1, "John", "Doe", "Hapoalim", "1234 5678 9012 3456", 5000)
    customer2 = IndividualCustomer(2, "Jane", "Smith", "Hapoalim", "9876 5432 1098 7654", 7000)
    customer3 = IndividualCustomer(3, "Michael", "Johnson", "Hapoalim", "5678 1234 5678 9012", 3000)

    customer4 = IndividualCustomer(4, "Emily", "Brown", "Leomi", "4321 8765 4321 0987", 6000)
    customer5 = IndividualCustomer(5, "David", "Williams", "Leomi", "8765 4321 0987 6543", 4000)
    customer6 = IndividualCustomer(6, "Sarah", "Taylor", "Leomi", "3456 7890 1234 5678", 5500)

    company_customer1 = CompanyCustomer(1, "Tech Solutions Inc.", "Discount", 10000)
    company_customer2 = CompanyCustomer(2, "Global Industries Ltd.", "Discount", 15000)
    company_customer3 = CompanyCustomer(3, "InnovateTech Group", "Discount", 12000)

    hapoalim = Hapoalim(0, "Hapoalim", 10, 10, 10, [customer1,customer2,customer3])
    leomi = Leomi(0, "Leomi", 10, 10, 10, [customer4,customer5,customer6])
    discount = Discount(0, "Discount", 10, 10, 10, [company_customer1,company_customer2,company_customer3])


    hapoalim.calculate_customer_money()

