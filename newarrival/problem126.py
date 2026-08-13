expenses = []


def add_expense():

    category = input("Category: ")
    description = input("Description: ")
    amount = float(input("Amount: "))

    if amount <= 0:
        raise Exception("Amount must be positive.")

    expenses.append({
        "Category": category,
        "Description": description,
        "Amount": amount
    })

    print("Expense added.")


def view_expenses():

    if not expenses:
        print("No expenses recorded.")
        return

    total = 0

    print("\n========== EXPENSES ==========")

    for expense in expenses:

        print(
            expense["Category"],
            "|",
            expense["Description"],
            "| Rs.",
            expense["Amount"]
        )

        total += expense["Amount"]

    print("----------------------------")
    print("Total Expenses: Rs.", total)


def category_total():

    category = input("Enter category: ").lower()

    total = 0

    for expense in expenses:

        if expense["Category"].lower() == category:
            total += expense["Amount"]

    print("Total for", category, "=", total)


while True:

    try:

        print("\n========== EXPENSE TRACKER ==========")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Category Total")
        print("4. Exit")

        choice = int(input("Choice: "))

        if choice == 1:
            add_expense()

        elif choice == 2:
            view_expenses()

        elif choice == 3:
            category_total()

        elif choice == 4:
            break

        else:
            print("Invalid choice.")

    except ValueError:
        print("Enter valid input.")

    except Exception as e:
        print("Error:", e)