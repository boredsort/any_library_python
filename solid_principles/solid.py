from abc import ABC, abstractmethod

class Order:
    items = []
    quantities = []
    prices = []
    status = "open"

    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total

class PaymentProcessor(ABC):

    @abstractmethod
    def pay(self, order):
        pass

class PaymentProcessor_SMS(PaymentProcessor):

    @abstractmethod
    def auth_sms(self, code):
        pass

class DebitPaymentProcessor(PaymentProcessor_SMS):

    def __init__(self, security_code):
        self.security_code = security_code
        self.verified = False

    def auth_sms(self, code):
        print(f"Verifying SMS code {code}")
        self.verified = True

    def pay(self, order):
        if not self.verified:
            raise Exception("Not Authorized")
        print("Processing debit payment type") 
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"

class CreditPaymentProcessor(PaymentProcessor):

    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, order):
        print("Processing credit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"

class PaypalPaymentProcessor(PaymentProcessor_SMS):

    def __init__(self, email_add):
        self.email_add = email_add
        self.verified = False

    def auth_sms(self, code):
        print(f"Verifying SMS code {code}")
        self.verified = True

    def pay(self, order):
        if not self.verified:
            raise Exception("Not Authorized")
        print("Processing paypal payment type")
        print(f"Verifying email_add: {self.email_add}")
        order.status = "paid"

order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)

print(order.total_price())

payment_processor = CreditPaymentProcessor("7011111")
payment_processor.pay(order)

payment_processor = DebitPaymentProcessor("7011111")
payment_processor.auth_sms('40044')
payment_processor.pay(order)

payment_processor = PaypalPaymentProcessor("batman@gmail.com")
payment_processor.auth_sms('40044')
payment_processor.pay(order)


