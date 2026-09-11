numbers = list(map(int, input("Enter numbers: ").split()))
n = int(input("Enter n: "))

result = []

for i, number in enumerate(numbers, start=1):
    if i % n != 0:
        result.append(number)

print("Result:", result)