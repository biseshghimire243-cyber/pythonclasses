balance = 10000

while True:
    print("\n==============================")
    print("      ATM MANAGEMENT SYSTEM")
    print("==============================")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Transfer Money")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            print(f"\nCurrent Balance: Rs. {balance}")

        elif choice == 2:
            amount = float(input("Enter deposit amount: "))

            if amount <= 0:
                raise ValueError("Deposit amount must be greater than zero.")

            balance += amount

            print("Deposit Successful!")
            print(f"New Balance: Rs. {balance}")

        elif choice == 3:
            amount = float(input("Enter withdrawal amount: "))

            if amount <= 0:
                raise ValueError("Amount must be positive.")

            if amount > balance:
                raise Exception("Insufficient Balance.")

            balance -= amount

            print("Withdrawal Successful!")
            print(f"Remaining Balance: Rs. {balance}")

        elif choice == 4:
            account = input("Enter Receiver Account Number: ")
            amount = float(input("Enter transfer amount: "))

            if amount <= 0:
                raise ValueError("Transfer amount must be greater than zero.")

            if amount > balance:
                raise Exception("Insufficient Balance.")

            balance -= amount

            print("\nTransfer Successful!")
            print("Transferred To:", account)
            print("Amount:", amount)
            print("Remaining Balance:", balance)

        elif choice == 5:
            print("\nThank You For Using Our ATM")
            break

        else:
            print("Invalid Choice!")

    except ValueError as e:
        print("Error:", e)

    except Exception as e:
        print("Error:", e)