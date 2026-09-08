numbers = list(map(float, input("Enter numbers: ").split()))

total = sum(numbers)

if total == 0:
    print("Cannot calculate percentages")
else:
    for number in numbers:
        percentage = (number / total) * 100
        print(number, "=", round(percentage, 2), "%")