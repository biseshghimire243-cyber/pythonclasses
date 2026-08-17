import json
import os


class EmployeeManager:

    def __init__(self):

        self.filename = "employee_records.json"
        self.employees = self.load()

    def load(self):

        if not os.path.exists(self.filename):
            return []

        with open(self.filename, "r") as file:

            return json.load(file)

    def save(self):

        with open(self.filename, "w") as file:

            json.dump(
                self.employees,
                file,
                indent=4
            )

    def add_employee(self):

        employee = {

            "id": input("Employee ID: "),
            "name": input("Name: "),
            "department": input("Department: "),
            "salary": float(
                input("Salary: ")
            )
        }

        self.employees.append(employee)

        self.save()

        print("Employee added.")

    def search(self):

        employee_id = input(
            "Employee ID: "
        )

        for employee in self.employees:

            if employee["id"] == employee_id:

                print(employee)
                return

        print("Employee not found.")

    def display(self):

        for employee in self.employees:

            print(
                employee["id"],
                "|",
                employee["name"],
                "|",
                employee["department"],
                "| Rs.",
                employee["salary"]
            )


manager = EmployeeManager()

while True:

    print("\n1. Add Employee")
    print("2. Search Employee")
    print("3. View Employees")
    print("4. Exit")

    choice = input("Choice: ")

    if choice == "1":

        manager.add_employee()

    elif choice == "2":

        manager.search()

    elif choice == "3":

        manager.display()

    elif choice == "4":

        break

    else:

        print("Invalid choice.")