import json
import os


class EmployeeDatabase:

    def __init__(self, filename="employees.json"):
        self.filename = filename
        self.employees = []

        self.load()

    def load(self):

        if os.path.exists(self.filename):

            with open(self.filename, "r") as file:

                self.employees = json.load(file)

    def save(self):

        with open(self.filename, "w") as file:

            json.dump(
                self.employees,
                file,
                indent=4
            )

    def add_employee(self, name, department, salary):

        employee = {
            "name": name,
            "department": department,
            "salary": salary
        }

        self.employees.append(employee)

        self.save()

        print("Employee added.")

    def display(self):

        print("\n========== EMPLOYEES ==========")

        for employee in self.employees:

            print(
                employee["name"],
                "|",
                employee["department"],
                "| Rs.",
                employee["salary"]
            )


database = EmployeeDatabase()

database.add_employee(
    "Bishesh",
    "IT",
    50000
)

database.add_employee(
    "Ram",
    "HR",
    45000
)

database.display()