from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class CashPayment(Payment):

    def pay(self, amount):
        print("Paid Rs.", amount, "using cash.")


class CardPayment(Payment):

    def pay(self, amount):
        print("Paid Rs.", amount, "using card.")


class OnlinePayment(Payment):

    def pay(self, amount):
        print("Paid Rs.", amount, "using online payment.")


payments = [
    CashPayment(),
    CardPayment(),
    OnlinePayment()
]

amount = 5000

for payment in payments:
    payment.pay(amount)