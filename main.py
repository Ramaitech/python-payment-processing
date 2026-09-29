from abc import ABC, abstractmethod

# abstract parent class
class payment(ABC):

    def __init__(self, amount):
        self.amount = amount

    @abstractmethod
    def pay(self):
        pass

# Child class for credit card payments
class CreditCardPayment(payment):
    def pay(self):
        print(f"Processing credit card payment of ${self.amount}")


# Child class for UPI payments
class UPIPayment(payment):
    def pay(self):
        print(f"Processing UPI payment of ${self.amount}")


# Child class for net banking payments
class NetBankingPayment(payment):
    def pay(self):
        print(f"Processing net banking payment of ${self.amount}")



# Main program

if __name__ == "__main__":
    # Create instances of different payment methods
    credit_card_payment = CreditCardPayment(100)
    upi_payment = UPIPayment(200)
    net_banking_payment = NetBankingPayment(300)

# store all payment instances in a list
    payments = [credit_card_payment, upi_payment, net_banking_payment]


print("Processing payments...")

for payment in payments:
    payment.pay()
