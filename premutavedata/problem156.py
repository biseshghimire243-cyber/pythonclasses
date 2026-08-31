number = int(input("Enter a number: "))

total = 0
product = 1

for digit in str(number):
    digit = int(digit)
    total += digit
    product *= digit

if total == product:
    print("Spy number")
else:
    print("Not a spy number")