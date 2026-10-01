numbers = list(map(int, input("Enter numbers: ").split()))

result = None

for number in numbers:
    if number < 0:
        result = number
        break

if result is not None:
    print("First negative number:", result)
else:
    print("No negative number found")