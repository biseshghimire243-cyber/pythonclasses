try:
    number = int(input("Enter a positive integer: "))

    if number <= 0:
        raise Exception("Number must be greater than zero.")

    print("Valid Number:", number)

except Exception as e:
    print(e)