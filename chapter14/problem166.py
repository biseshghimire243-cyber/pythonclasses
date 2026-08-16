import json
import os


class Bank:

    def __init__(self, filename="accounts.json"):
        self.filename = filename
        self.accounts = {}

        self.load_data()

    def load_data(self):

        if os.path.exists(self.filename):

            with open(self.filename, "r") as file:
                self.accounts = json.load(file)

    def save_data(self):

        with open(self.filename, "w") as file:

            json.dump(
                self.accounts,
                file,
                indent=4
            )

    def create_account(self, number, name, balance):

        if number in self.accounts:
            print("Account already exists.")
            return

        self.accounts[number] = {
            "name": name,
            "balance": balance
        }

        self.save_data()

        print("Account created.")

    def deposit(self, number, amount):

        if number not in self.accounts:
            print("Account not found.")
            return

        self.accounts[number]["balance"] += amount

        self.save_data()

        print("Deposit successful.")

    def show_account(self, number):

        if number not in self.accounts:
            print("Account not found.")
            return

        account = self.accounts[number]

        print("\n========== ACCOUNT ==========")
        print("Account:", number)
        print("Name:", account["name"])
        print("Balance:", account["balance"])


bank = Bank()

bank.create_account(
    "1001",
    "Bishesh",
    5000
)

bank.deposit("1001", 2000)

bank.show_account("1001")