from abc import ABC, abstractmethod

# ---------------------------------------------------------
# Abstract Base Class
# ---------------------------------------------------------
class Payment(ABC):
    """
    Abstract base class representing a generic payment.
    Every payment method must implement the pay() method.
    """

    def __init__(self, amount):
        self.amount = amount

    @abstractmethod
    def pay(self):
        """Process the payment. Must be implemented by subclasses."""
        pass


# ---------------------------------------------------------
# Concrete Implementations (Polymorphism)
# ---------------------------------------------------------
class CreditCardPayment(Payment):
    def pay(self):
        print(f"[CreditCard] Processing credit card payment of ${self.amount}")


class UPIPayment(Payment):
    def pay(self):
        print(f"[UPI] Processing UPI payment of ${self.amount}")


class NetBankingPayment(Payment):
    def pay(self):
        print(f"[NetBanking] Processing net banking payment of ${self.amount}")


# ---------------------------------------------------------
# Runtime Polymorphism Demonstration
# ---------------------------------------------------------
def process_payment(payment_method: Payment):
    """
    Demonstrates runtime polymorphism.
    The same function calls pay() on different payment objects.
    """
    payment_method.pay()


# ---------------------------------------------------------
# Main Execution Block
# ---------------------------------------------------------
def main():
    # Create instances of different payment methods
    credit_card = CreditCardPayment(100)
    upi = UPIPayment(200)
    net_banking = NetBankingPayment(300)

    # Store all payment instances in a list
    payments = [credit_card, upi, net_banking]

    print("Processing payments...\n")

    # Runtime polymorphism: same method name, different behavior
    for method in payments:
        process_payment(method)


# Ensures demo runs only when file is executed directly
if __name__ == "__main__":
    main()
