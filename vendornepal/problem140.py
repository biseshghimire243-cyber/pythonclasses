class Employee:

    def __init__(self, name, basic_salary):
        self.name = name
        self.basic_salary = basic_salary

    def calculate_salary(self):

        return self.basic_salary


class FullTimeEmployee(Employee):

    def calculate_salary(self):

        bonus = self.basic_salary * 0.10

        return self.basic_salary + bonus


class PartTimeEmployee(Employee):

    def __init__(self, name, hours, rate):
        self.name = name
        self.hours = hours
        self.rate = rate

    def calculate_salary(self):

        return self.hours * self.rate


class ContractEmployee(Employee):

    def calculate_salary(self):

        tax = self.basic_salary * 0.05

        return self.basic_salary - tax


employees = [

    FullTimeEmployee(
        "Ram",
        50000
    ),

    PartTimeEmployee(
        "Sita",
        80,
        500
    ),

    ContractEmployee(
        "Hari",
        60000
    )
]


print("========== SALARY REPORT ==========")

for employee in employees:

    salary = employee.calculate_salary()

    print(
        employee.name,
        "-> Rs.",
        salary
    )