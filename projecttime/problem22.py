try:
    value = input("Enter a number: ")
    number = int(value)

    print("Integer Value:", number)

except ValueError:
    print("Conversion failed.")