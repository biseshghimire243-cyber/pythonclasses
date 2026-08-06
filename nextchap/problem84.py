accounts = {}

while True:
    try:
        print("\n========== ONLINE BANKING SYSTEM ==========")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Delete Account")
        print("6. Exit")

        choice = int(input("Enter Choice: "))

        if choice == 1:
            account = input("Enter Account Number: ")

            if account in accounts:
                raise Exception("Account already exists.")

            name = input("Enter Account Holder Name: ")
            balance = float(input("Enter Initial Deposit: "))

            accounts[account] = {
                "Name": name,
                "Balance": balance
            }

            print("Account Created Successfully.")

        elif choice == 2:

            account = input("Account Number: ")

            if account not in accounts:
                raise Exception("Account Not Found.")

            amount = float(input("Deposit Amount: "))

            accounts[account]["Balance"] += amount

            print("Deposit Successful.")

        elif choice == 3:

            account = input("Account Number: ")

            if account not in accounts:
                raise Exception("Account Not Found.")

            amount = float(input("Withdraw Amount: "))

            if amount > accounts[account]["Balance"]:
                raise Exception("Insufficient Balance.")

            accounts[account]["Balance"] -= amount

            print("Withdrawal Successful.")

        elif choice == 4:

            account = input("Account Number: ")

            if account not in accounts:
                raise Exception("Account Not Found.")

            print(accounts[account])

        elif choice == 5:

            account = input("Account Number: ")

            if account not in accounts:
                raise Exception("Account Not Found.")

            del accounts[account]

            print("Account Deleted.")

        elif choice == 6:
            print("Thank You.")
            break

        else:
            print("Invalid Choice.")

    except ValueError:
        print("Invalid Input.")

    except Exception as e:
        print(e)