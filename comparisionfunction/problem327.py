def decimal_to_binary(number):
    if number == 0:
        return ""
    return decimal_to_binary(number // 2) + str(number % 2)

number = int(input("Enter a positive number: "))

if number == 0:
    print("Binary: 0")
else:
    print("Binary:", decimal_to_binary(number))