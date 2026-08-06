expenses = []

while True:
    try:
        print("\n========== EXPENSE TRACKER ==========")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Show Total")
        print("4. Delete Expense")
        print("5. Exit")

        choice = int(input("Enter Choice: "))

        if choice == 1:
            title = input("Expense Title: ")
            amount = float(input("Amount: "))

            expenses.append({
                "Title": title,
                "Amount": amount
            })

            print("Expense Added Successfully.")

        elif choice == 2:
            if len(expenses) == 0:
                print("No Expenses Found.")

            for expense in expenses:
                print(expense["Title"], "-", expense["Amount"])

        elif choice == 3:
            total = 0

            for expense in expenses:
                total += expense["Amount"]

            print("Total Expense = Rs.", total)

        elif choice == 4:
            title = input("Expense Title: ")

            found = False

            for expense in expenses:
                if expense["Title"] == title:
                    expenses.remove(expense)
                    found = True
                    print("Expense Deleted.")
                    break

            if not found:
                raise Exception("Expense Not Found.")

        elif choice == 5:
            break

        else:
            print("Invalid Choice.")

    except Exception as e:
        print(e)