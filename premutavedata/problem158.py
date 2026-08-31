number = int(input("Enter a number: "))

digit_sum = 0

for digit in str(number):
    digit_sum += int(digit)

if number % digit_sum == 0:
    print("Harshad number")
else:
    print("Not a Harshad number")