try:
    number = int(input("Enter a positive number: "))

    if number < 0:
        raise Exception("Negative numbers are not allowed.")

    print("Number =", number)

except Exception as e:
    print(e)