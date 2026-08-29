number = int(input("Enter a decimal number: "))

if number == 0:
    print("Binary: 0")
else:
    binary = ""

    while number > 0:
        remainder = number % 2
        binary = str(remainder) + binary
        number //= 2

    print("Binary:", binary)