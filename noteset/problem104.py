balance = 10000
pin = "1234"
transactions = []


def check_balance():
    print("\nCurrent Balance: Rs.", balance)


def deposit():
    global balance

    amount = float(input("Enter deposit amount: "))

    if amount <= 0:
        raise Exception("Amount must be greater than 0.")

    balance += amount

    transactions.append(f"Deposited Rs. {amount}")

    print("Money deposited successfully.")


def withdraw():
    global balance

    amount = float(input("Enter withdrawal amount: "))

    if amount <= 0:
        raise Exception("Amount must be greater than 0.")

    if amount > balance:
        raise Exception("Insufficient balance.")

    balance -= amount

    transactions.append(f"Withdrawn Rs. {amount}")

    print("Please collect your cash.")


def change_pin():
    global pin

    old_pin = input("Enter current PIN: ")

    if old_pin != pin:
        raise Exception("Incorrect PIN.")

    new_pin = input("Enter new PIN: ")

    if len(new_pin) != 4 or not new_pin.isdigit():
        raise Exception("PIN must contain exactly 4 digits.")

    pin = new_pin

    print("PIN changed successfully.")


while True:

    try:

        print("\n========== ATM SYSTEM ==========")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Change PIN")
        print("5. Transaction History")
        print("6. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:

            check_balance()

        elif choice == 2:

            deposit()

        elif choice == 3:

            withdraw()

        elif choice == 4:

            change_pin()

        elif choice == 5:

            print("\n===== TRANSACTION HISTORY =====")

            if len(transactions) == 0:
                print("No transactions yet.")

            else:

                for transaction in transactions:
                    print("-", transaction)

        elif choice == 6:

            print("Thank you for using the ATM.")
            break

        else:

            print("Invalid choice.")

    except ValueError:

        print("Please enter a valid number.")

    except Exception as e:

        print("Error:", e)