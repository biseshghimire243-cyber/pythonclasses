class BankAccount:

    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.__balance = balance

    def deposit(self, amount):

        if amount <= 0:
            print("Invalid amount.")
            return

        self.__balance += amount

        print("Rs.", amount, "deposited successfully.")

    def withdraw(self, amount):

        if amount <= 0:
            print("Invalid amount.")
            return

        if amount > self.__balance:
            print("Insufficient balance.")
            return

        self.__balance -= amount

        print("Rs.", amount, "withdrawn successfully.")

    def show_balance(self):

        print("\n========== ACCOUNT DETAILS ==========")
        print("Account Number:", self.account_number)
        print("Account Holder:", self.name)
        print("Balance: Rs.", self.__balance)


account_number = input("Enter account number: ")
name = input("Enter account holder name: ")

account = BankAccount(
    account_number,
    name,
    5000
)

while True:

    print("\n========== BANK MENU ==========")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Show Balance")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        amount = float(input("Enter deposit amount: "))

        account.deposit(amount)

    elif choice == "2":

        amount = float(input("Enter withdrawal amount: "))

        account.withdraw(amount)

    elif choice == "3":

        account.show_balance()

    elif choice == "4":

        print("Thank you for using the bank system.")
        break

    else:

        print("Invalid choice.")