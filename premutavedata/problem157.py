number = int(input("Enter a number: "))

seen = set()

while number != 1 and number not in seen:

    seen.add(number)
    total = 0

    for digit in str(number):
        total += int(digit) ** 2

    number = total

if number == 1:
    print("Happy number")
else:
    print("Not a happy number")