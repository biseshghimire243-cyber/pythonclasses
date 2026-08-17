import csv
import os

filename = "employees.csv"


def add_employee():

    name = input("Employee Name: ")
    department = input("Department: ")
    salary = float(input("Salary: "))

    file_exists = os.path.exists(filename)

    with open(
        filename,
        "a",
        newline=""
    ) as file:

        writer = csv.writer(file)

        if not file_exists:

            writer.writerow([
                "Name",
                "Department",
                "Salary"
            ])

        writer.writerow([
            name,
            department,
            salary
        ])

    print("Employee added.")


def display_employees():

    try:

        with open(
            filename,
            "r",
            newline=""
        ) as file:

            reader = csv.DictReader(file)

            print("\n========== EMPLOYEES ==========")

            for employee in reader:

                print(
                    employee["Name"],
                    "|",
                    employee["Department"],
                    "| Rs.",
                    employee["Salary"]
                )

    except FileNotFoundError:

        print("Employee file not found.")


while True:

    print("\n1. Add Employee")
    print("2. View Employees")
    print("3. Exit")

    choice = input("Choice: ")

    if choice == "1":

        add_employee()

    elif choice == "2":

        display_employees()

    elif choice == "3":

        break

    else:

        print("Invalid choice.")