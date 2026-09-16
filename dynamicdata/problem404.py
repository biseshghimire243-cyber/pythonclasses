numbers = list(map(int, input("Enter numbers: ").split()))

count = 0

for number in numbers:
    digit_sum = sum(int(digit) for digit in str(abs(number)))

    if digit_sum % 2 == 0:
        count += 1

print("Count:", count)