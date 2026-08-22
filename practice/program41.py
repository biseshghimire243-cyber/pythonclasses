number = int(input("Enter a number: "))

square = number ** 2
total = 0

while square > 0:
    digit = square % 10
    total += digit
    square //= 10

if total == number:
    print("Neon number")
else:
    print("Not a neon number")