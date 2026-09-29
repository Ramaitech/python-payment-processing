Processing payments...
Processing credit card payment of $100
Processing UPI payment of $200
Processing net banking payment of $300
PS C:\Source\python-payment-processing> 

## How It Works

Payment is an abstract base class with an abstract pay() method.
Each child class implements pay() in its own way.

The program stores different payment objects in a list and calls
pay() on each object. Python selects the appropriate implementation
at runtime, demonstrating runtime polymorphism.

## Disclaimer

This is an educational simulation. It does not process real
payments or connect to financial institutions.

## Author
developer

## Detailed Explanation
The base class defines the shared structure. The abstract class payment stores an amount and declares an abstract pay() method. Because pay() is abstract, each concrete payment class must provide its own implementation.

Each child class defines its payment behavior. CreditCardPayment, UPIPayment, and NetBankingPayment inherit from payment. They each implement pay() to print a message for their payment type and amount.

The program creates three objects. It creates a credit-card payment for 100, a UPI payment for 200, and a net-banking payment for 300.

The objects go into one list. The payments list contains different kinds of payment objects. They can be handled together because each object supports the pay() method.

The loop calls the same method on each object. For every item in the list, the program calls payment.pay() using the loop variable payment. Python looks up the method on that object’s actual class and runs the corresponding implementation.

The loop ends when the list is exhausted. Each method prints its own message. After the last object has been processed, the loop finishes.