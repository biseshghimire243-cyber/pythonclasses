try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("Answer =", a / b)

except ZeroDivisionError:
    print("Division by zero is not allowed.")

finally:
    print("Program Ended.")