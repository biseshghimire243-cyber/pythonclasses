number = int(input("Enter a number: "))

digits = str(number)
power = len(digits)
total = 0

for digit in digits:
    total += int(digit) ** power

if total == number:
    print("Armstrong number")
else:
    print("Not an Armstrong number")