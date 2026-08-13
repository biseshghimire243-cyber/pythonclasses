expenses = []


def add_expense():

    person = input("Person Name: ")
    description = input("Expense Description: ")
    amount = float(input("Amount: "))

    expenses.append({
        "Person": person,
        "Description": description,
        "Amount": amount
    })

    print("Expense recorded.")


def calculate_split():

    if not expenses:
        print("No expenses.")
        return

    people = set()

    total = 0

    for expense in expenses:

        people.add(expense["Person"])
        total += expense["Amount"]

    share = total / len(people)

    print("\nTotal Expense:", total)
    print("Number of People:", len(people))
    print("Each Person Should Pay:", share)

    print("\nPaid Amount:")

    for person in people:

        paid = 0

        for expense in expenses:

            if expense["Person"] == person:
                paid += expense["Amount"]

        difference = paid - share

        if difference > 0:
            print(person, "should receive", difference)

        elif difference < 0:
            print(person, "should pay", abs(difference))

        else:
            print(person, "is settled.")


while True:

    try:

        print("\n========== EXPENSE SPLITTER ==========")
        print("1. Add Expense")
        print("2. Calculate Split")
        print("3. Exit")

        choice = int(input("Choice: "))

        if choice == 1:
            add_expense()

        elif choice == 2:
            calculate_split()

        elif choice == 3:
            break

        else:
            print("Invalid choice.")

    except ValueError:
        print("Enter valid input.")