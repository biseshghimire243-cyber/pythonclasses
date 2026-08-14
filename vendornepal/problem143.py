class ATM:

    def __init__(self, account_holder, pin, balance=0):

        self.account_holder = account_holder
        self.__pin = pin
        self.__balance = balance

    def verify_pin(self, pin):

        return pin == self.__pin

    def deposit(self, amount):

        if amount <= 0:
            raise ValueError(
                "Amount must be positive."
            )

        self.__balance += amount

    def withdraw(self, amount):

        if amount <= 0:
            raise ValueError(
                "Amount must be positive."
            )

        if amount > self.__balance:
            raise ValueError(
                "Insufficient balance."
            )

        self.__balance -= amount

    def show_balance(self):

        print(
            "Current Balance: Rs.",
            self.__balance
        )


atm = ATM(
    "Bishesh Ghimire",
    "1234",
    10000
)

print("========== ATM ==========")

attempts = 3

while attempts > 0:

    pin = input("Enter PIN: ")

    if atm.verify_pin(pin):
        print("Login successful.")
        break

    attempts -= 1

    print(
        "Wrong PIN.",
        attempts,
        "attempts remaining."
    )

else:

    print("Account locked.")
    exit()


while True:

    try:

        print("\n========== ATM MENU ==========")
        print("1. Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = int(input("Choice: "))

        if choice == 1:

            atm.show_balance()

        elif choice == 2:

            amount = float(
                input("Deposit amount: ")
            )

            atm.deposit(amount)

            print("Deposit successful.")

        elif choice == 3:

            amount = float(
                input("Withdrawal amount: ")
            )

            atm.withdraw(amount)

            print("Withdrawal successful.")

        elif choice == 4:

            print("Thank you for using ATM.")
            break

        else:

            print("Invalid choice.")

    except ValueError as e:

        print("Error:", e)