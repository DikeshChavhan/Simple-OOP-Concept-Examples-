from abc import ABC, abstractmethod

# Product Class (Encapsulation)

class Product:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price  # private attribute

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

# Abstract Payment Class (Abstraction)

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


# Payment Methods (Polymorphism)

class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card.")

class PayPalPayment(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using PayPal.")


# User Class (Inheritance Example)

class User:
    def __init__(self, username):
        self.username = username

class Customer(User):
    def __init__(self, username):
        super().__init__(username)
        self.cart = []

    def add_to_cart(self, product):
        self.cart.append(product)
        print(f"{product.get_name()} added to cart.")

    def checkout(self, payment_method: Payment):
        total = sum([p.get_price() for p in self.cart])
        payment_method.pay(total)


# Example Run

if __name__ == "__main__":
    # Create products
    p1 = Product("Laptop", 50000)
    p2 = Product("Headphones", 2000)

    # Create customer
    customer = Customer("Pratik")

    # Add items to cart
    customer.add_to_cart(p1)
    customer.add_to_cart(p2)

    # Pay using Credit Card
    customer.checkout(CreditCardPayment())

    # Pay using PayPal
    customer.checkout(PayPalPayment())
