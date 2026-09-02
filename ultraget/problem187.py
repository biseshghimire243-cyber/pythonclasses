salaries = list(map(float, input("Enter salaries separated by spaces: ").split()))

average = sum(salaries) / len(salaries)

print("Average salary:", average)
print("Employees above average:")

for salary in salaries:
    if salary > average:
        print(salary)