try:
    try:
        number = int(input("Enter number: "))
        print(50 / number)

    except ZeroDivisionError:
        print("Cannot divide by zero.")

except ValueError:
    print("Invalid input.")