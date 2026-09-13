salary = float(input("Enter salary: "))
years = int(input("Enter years of service: "))

if years >= 10:
    bonus = salary * 0.20
elif years >= 5:
    bonus = salary * 0.10
elif years >= 2:
    bonus = salary * 0.05
else:
    bonus = 0

final_salary = salary + bonus

print("Bonus:", bonus)
print("Final salary:", final_salary)