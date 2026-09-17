numbers = list(map(int, input("Enter numbers: ").split()))

largest_digit_count = 0
result = None

for number in numbers:
    digit_count = len(str(abs(number)))

    if digit_count > largest_digit_count:
        largest_digit_count = digit_count
        result = number

print("Number:", result)
print("Digits:", largest_digit_count)