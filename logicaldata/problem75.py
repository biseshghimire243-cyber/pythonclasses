employees = {
    "Bishesh": 50000,
    "Ram": 45000,
    "Sita": 65000,
    "Hari": 40000
}

highest_name = ""
highest_salary = 0

for name, salary in employees.items():

    if salary > highest_salary:
        highest_salary = salary
        highest_name = name

print("Employee Salary Data:")

for name, salary in employees.items():
    print(name, ":", salary)

print("\nHighest Paid Employee:", highest_name)
print("Salary:", highest_salary)