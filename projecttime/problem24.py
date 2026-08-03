try:
    salary = float(input("Enter salary: "))

    if salary < 0:
        raise Exception("Salary cannot be negative.")

    print("Salary:", salary)

except Exception as e:
    print(e)