numbers = list(map(int, input("Enter numbers: ").split()))

result = []

for index, number in enumerate(numbers):
    if number == index:
        result.append(number)

print("Numbers equal to their positions:", result)