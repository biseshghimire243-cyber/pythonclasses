class Employee:

    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def calculate_bonus(self):
        return self.salary * 0.10

    def display(self):

        print("\n========== EMPLOYEE ==========")
        print("Name:", self.name)
        print("ID:", self.employee_id)
        print("Salary: Rs.", self.salary)
        print("Bonus: Rs.", self.calculate_bonus())
        print("Total: Rs.", self.salary + self.calculate_bonus())


name = input("Employee Name: ")
employee_id = input("Employee ID: ")
salary = float(input("Salary: "))

employee = Employee(name, employee_id, salary)

employee.display()