try:
    salary = float(input("Enter employee salary: "))

    if salary < 15000:
        raise Exception("Salary is below the minimum wage.")

    print("Salary Accepted")

except Exception as e:
    print(e)