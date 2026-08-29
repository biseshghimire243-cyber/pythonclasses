number = int(input("Enter a number: "))

square = number ** 2
total = 0

for digit in str(square):
    total += int(digit)

if total == number:
    print("Neon number")
else:
    print("Not a neon number")