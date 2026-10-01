numbers = list(map(int, input("Enter numbers: ").split()))

result = None

for number in numbers:
    digits = str(abs(number))

    if len(digits) == len(set(digits)):
        result = number
        break

if result is not None:
    print("First number with unique digits:", result)
else:
    print("No number found")