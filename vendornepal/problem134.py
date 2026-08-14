class DigitalWallet:

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):

        if amount <= 0:
            raise ValueError("Amount must be positive.")

        self.__balance += amount
        print("Money deposited successfully.")

    def withdraw(self, amount):

        if amount <= 0:
            raise ValueError("Amount must be positive.")

        if amount > self.__balance:
            raise ValueError("Insufficient balance.")

        self.__balance -= amount
        print("Money withdrawn successfully.")

    def show_balance(self):

        print("\n========== WALLET ==========")
        print("Owner:", self.owner)
        print("Balance: Rs.", self.__balance)


wallet = DigitalWallet("Bishesh", 5000)

while True:

    try:

        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Balance")
        print("4. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:

            amount = float(input("Enter amount: "))
            wallet.deposit(amount)

        elif choice == 2:

            amount = float(input("Enter amount: "))
            wallet.withdraw(amount)

        elif choice == 3:

            wallet.show_balance()

        elif choice == 4:
            break

        else:
            print("Invalid choice.")

    except ValueError as e:
        print("Error:", e)