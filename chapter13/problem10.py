try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    print("1. Add")
    print("2. Subtract")

    choice = int(input("Enter choice: "))

    if choice == 1:
        print("Answer =", a + b)

    elif choice == 2:
        print("Answer =", a - b)

    else:
        print("Invalid choice.")

except ValueError:
    print("Please enter valid numbers.")