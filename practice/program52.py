salary = float(input("Enter salary: "))

if salary <= 30000:
    tax = 0
elif salary <= 50000:
    tax = salary * 0.10
else:
    tax = salary * 0.20

final_salary = salary - tax

print("Tax:", tax)
print("Salary after tax:", final_salary)