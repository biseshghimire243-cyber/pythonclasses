try:
    number = int(input("Enter number: "))
    print(100 / number)

except ValueError:
    print("Invalid number.")

except ZeroDivisionError:
    print("Cannot divide by zero.")