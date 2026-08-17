import json
import os


class BankAccount:

    def __init__(self, name):

        self.name = name
        self.balance = 0
        self.transactions = []

    def deposit(self, amount):

        self.balance += amount

        self.transactions.append({
            "type": "Deposit",
            "amount": amount
        })

    def withdraw(self, amount):

        if amount > self.balance:

            raise ValueError(
                "Insufficient balance."
            )

        self.balance -= amount

        self.transactions.append({
            "type": "Withdrawal",
            "amount": amount
        })

    def show_history(self):

        print("\n========== TRANSACTIONS ==========")

        for transaction in self.transactions:

            print(
                transaction["type"],
                "- Rs.",
                transaction["amount"]
            )

        print(
            "Current Balance: Rs.",
            self.balance
        )


account = BankAccount("Bishesh")

try:

    account.deposit(10000)

    account.withdraw(2500)

    account.deposit(5000)

    account.withdraw(1000)

    account.show_history()

except ValueError as error:

    print("Error:", error)