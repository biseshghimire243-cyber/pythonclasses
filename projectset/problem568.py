numbers = list(map(int, input("Enter numbers: ").split()))

if numbers:
    highest_sum = -1
    result = None

    for number in numbers:
        digit_sum = sum(int(digit) for digit in str(abs(number)))

        if digit_sum > highest_sum:
            highest_sum = digit_sum
            result = number
        elif digit_sum == highest_sum and number < result:
            result = number

    print("Number:", result)
    print("Digit sum:", highest_sum)
else:
    print("No numbers entered.")