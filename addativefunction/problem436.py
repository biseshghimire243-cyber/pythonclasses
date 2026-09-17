numbers = list(map(int, input("Enter numbers: ").split()))

best_number = numbers[0]
best_sum = sum(int(d) for d in str(abs(numbers[0])))

for number in numbers[1:]:
    digit_sum = sum(int(d) for d in str(abs(number)))

    if digit_sum < best_sum:
        best_sum = digit_sum
        best_number = number

print("Number with smallest digit sum:", best_number)
print("Digit sum:", best_sum)