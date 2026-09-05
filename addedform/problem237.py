binary = input("Enter binary number: ")

decimal = 0
power = 0
valid = True

for digit in reversed(binary):
    if digit not in "01":
        valid = False
        break

    decimal += int(digit) * (2 ** power)
    power += 1

if valid:
    print("Decimal:", decimal)
else:
    print("Invalid binary number.")