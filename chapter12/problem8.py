try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("Addition =", a + b)
    print("Division =", a / b)

except ZeroDivisionError:
    print("Cannot divide by zero.")

except ValueError:
    print("Please enter valid numbers.")