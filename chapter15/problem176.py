class ATM:

    def __init__(self, pin, balance):

        self.pin = pin
        self.balance = balance

    def check_pin(self, entered_pin):

        if entered_pin != self.pin:

            raise ValueError("Incorrect PIN.")

    def deposit(self, amount):

        if amount <= 0:

            raise ValueError(
                "Invalid deposit amount."
            )

        self.balance += amount

    def withdraw(self, amount):

        if amount <= 0:

            raise ValueError(
                "Invalid withdrawal amount."
            )

        if amount > self.balance:

            raise ValueError(
                "Insufficient balance."
            )

        self.balance -= amount

    def show_balance(self):

        print(
            "Current Balance: Rs.",
            self.balance
        )


atm = ATM("1234", 10000)

try:

    pin = input("Enter PIN: ")

    atm.check_pin(pin)

    while True:

        print("\n1. Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Choice: ")

        if choice == "1":

            atm.show_balance()

        elif choice == "2":

            amount = float(
                input("Amount: ")
            )

            atm.deposit(amount)

        elif choice == "3":

            amount = float(
                input("Amount: ")
            )

            atm.withdraw(amount)

        elif choice == "4":

            break

        else:

            print("Invalid choice.")

except ValueError as error:

    print("Error:", error)