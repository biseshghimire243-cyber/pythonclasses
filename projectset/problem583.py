numbers = list(map(int, input("Enter numbers: ").split()))

result = []

for number in numbers:
    if numbers.count(number) != 2:
        result.append(number)

print("Result:", result)