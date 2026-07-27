try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    print("Division =", a / b)

except ZeroDivisionError:
    print("Division by zero is not allowed.")

except ValueError:
    print("Please enter valid numbers.")