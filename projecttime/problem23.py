try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    if a > b:
        print("Largest =", a)
    else:
        print("Largest =", b)

except ValueError:
    print("Please enter valid integers.")