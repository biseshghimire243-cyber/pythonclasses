class InsufficientBalanceError(Exception):
    pass


class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def withdraw(self, amount):

        if amount > self.balance:
            raise InsufficientBalanceError(
                "Insufficient balance!"
            )

        if amount <= 0:
            raise ValueError(
                "Amount must be greater than zero."
            )

        self.balance -= amount

        print("Withdrawal successful.")
        print("Remaining Balance:", self.balance)


account = BankAccount("Bishesh", 10000)

try:

    amount = float(
        input("Enter withdrawal amount: ")
    )

    account.withdraw(amount)

except InsufficientBalanceError as error:

    print("Error:", error)

except ValueError as error:

    print("Error:", error)