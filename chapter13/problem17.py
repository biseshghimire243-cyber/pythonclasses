try:
    try:
        number = int(input("Enter number: "))
        print(100 / number)

    except ZeroDivisionError:
        print("Division by zero is not allowed.")

except ValueError:
    print("Invalid input.")