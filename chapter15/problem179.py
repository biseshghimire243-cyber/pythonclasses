import json
import os


class ExpenseTracker:

    def __init__(self):

        self.filename = "expenses.json"
        self.expenses = self.load()

    def load(self):

        if not os.path.exists(self.filename):
            return []

        with open(self.filename, "r") as file:

            return json.load(file)

    def save(self):

        with open(self.filename, "w") as file:

            json.dump(
                self.expenses,
                file,
                indent=4
            )

    def add_expense(self):

        title = input("Expense Title: ")
        amount = float(input("Amount: "))
        category = input("Category: ")

        expense = {
            "title": title,
            "amount": amount,
            "category": category
        }

        self.expenses.append(expense)

        self.save()

        print("Expense added.")

    def total_expense(self):

        total = 0

        for expense in self.expenses:

            total += expense["amount"]

        print(
            "Total Expense: Rs.",
            total
        )

    def display(self):

        print("\n========== EXPENSES ==========")

        for expense in self.expenses:

            print(
                expense["title"],
                "| Rs.",
                expense["amount"],
                "|",
                expense["category"]
            )


tracker = ExpenseTracker()

while True:

    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Exit")

    choice = input("Choice: ")

    if choice == "1":

        tracker.add_expense()

    elif choice == "2":

        tracker.display()

    elif choice == "3":

        tracker.total_expense()

    elif choice == "4":

        break

    else:

        print("Invalid choice.")