from abc import ABC, abstractmethod

"""
this is using a composition approach for principle 4

"""

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

class SMSAuth:
    
    authorized = False

    def verify_code(self, code):
        # no logic, juas assume code is valid for testing only
        print(f"Verifying code {code}")
        self.authorized = True

    def is_authorized(self) -> bool:
        return self.authorized

class PaymentProcessor(ABC):

    @abstractmethod
    def pay(self, order):
        pass


class DebitPaymentProcessor(PaymentProcessor):

    def __init__(self, security_code, authorizer: SMSAuth):
        self.security_code = security_code
        self.authorizer = authorizer


    def pay(self, order):
        if not self.authorizer.is_authorized():
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

class PaypalPaymentProcessor(PaymentProcessor):

    def __init__(self, email_add, authorizer: SMSAuth):
        self.authorizer = authorizer
        self.email_add = email_add

    def auth_sms(self, code):
        print(f"Verifying SMS code {code}")
        self.verified = True

    def pay(self, order):
        if not self.authorizer.is_authorized():
            raise Exception("Not Authorized")
        print("Processing paypal payment type")
        print(f"Verifying email_add: {self.email_add}")
        order.status = "paid"

order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)

print(order.total_price())
authorizer = SMSAuth()
payment_processor = CreditPaymentProcessor("7011111")
payment_processor.pay(order)

authorizer.verify_code('40044')
payment_processor = DebitPaymentProcessor("7011111", authorizer)
payment_processor.pay(order)

authorizer.verify_code('40044')
payment_processor = PaypalPaymentProcessor("batman@gmail.com", authorizer)
payment_processor.pay(order)


