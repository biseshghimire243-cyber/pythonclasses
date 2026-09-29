numbers = list(map(int, input("Enter numbers: ").split()))

result = None

for number in numbers:
    digit_count = len(str(abs(number)))

    if digit_count % 2 == 0:
        if result is None or number > result:
            result = number

if result is not None:
    print("Largest number:", result)
else:
    print("No number has an even digit count")