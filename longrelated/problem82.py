accounts = {}

while True:

    try:

        print("\n===== BANK ACCOUNT =====")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. View Accounts")
        print("5. Exit")

        choice = int(input("Choice: "))

        if choice == 1:

            acc = input("Account Number: ")

            accounts[acc] = 0

            print("Account Created.")

        elif choice == 2:

            acc = input("Account Number: ")

            amount = float(input("Amount: "))

            accounts[acc] += amount

            print("Deposit Successful.")

        elif choice == 3:

            acc = input("Account Number: ")

            amount = float(input("Amount: "))

            if amount > accounts[acc]:
                raise Exception("Insufficient Balance.")

            accounts[acc] -= amount

            print("Withdrawal Successful.")

        elif choice == 4:

            for acc, balance in accounts.items():

                print(acc, ":", balance)

        elif choice == 5:
            break

    except Exception as e:
        print(e)