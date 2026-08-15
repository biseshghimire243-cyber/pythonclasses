class Payment:

    def __init__(self, customer, amount):
        self.customer = customer
        self.amount = amount

    def process(self):
        print("Processing general payment.")


class CashPayment(Payment):

    def process(self):
        print(
            "Cash payment received: Rs.",
            self.amount
        )


class CardPayment(Payment):

    def process(self):
        print(
            "Card payment processed: Rs.",
            self.amount
        )


class OnlinePayment(Payment):

    def process(self):
        print(
            "Online payment completed: Rs.",
            self.amount
        )


payments = [
    CashPayment("Ram", 1000),
    CardPayment("Sita", 2500),
    OnlinePayment("Bishesh", 5000)
]


print("========== PAYMENT SYSTEM ==========")

for payment in payments:

    print(
        "\nCustomer:",
        payment.customer
    )

    payment.process()