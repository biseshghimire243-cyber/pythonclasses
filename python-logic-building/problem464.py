numbers = list(map(int, input("Enter numbers: ").split()))

result = []

for number in numbers:
    if number == 0:
        continue

    digit_sum = sum(int(d) for d in str(abs(number)))

    if digit_sum != 0 and number % digit_sum == 0:
        result.append(number)

print("Numbers divisible by their digit sum:", result)