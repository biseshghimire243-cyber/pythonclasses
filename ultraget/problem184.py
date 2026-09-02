salary = float(input("Enter monthly salary: "))

if salary <= 30000:
    tax = salary * 0.01
elif salary <= 60000:
    tax = salary * 0.10
elif salary <= 100000:
    tax = salary * 0.20
else:
    tax = salary * 0.30

net_salary = salary - tax

print("Tax:", tax)
print("Net salary:", net_salary)