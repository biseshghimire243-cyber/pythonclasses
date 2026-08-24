name = input("Enter employee name: ")
salary = float(input("Enter basic salary: "))

bonus = salary * 10 / 100
tax = salary * 5 / 100

net_salary = salary + bonus - tax

print("Employee:", name)
print("Basic Salary:", salary)
print("Bonus:", bonus)
print("Tax:", tax)
print("Net Salary:", net_salary)