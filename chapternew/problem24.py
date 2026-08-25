import math

number = int(input("Enter a number: "))
total = 0

for digit in str(number):
    total += math.factorial(int(digit))

if total == number:
    print("Strong number")
else:
    print("Not a strong number")