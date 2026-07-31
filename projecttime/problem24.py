try:
    number = int(input("Enter a number: "))

    if number < 0:
        raise Exception("Square root of a negative number is not allowed.")

    print("Square =", number ** 0.5)

except Exception as e:
    print(e)