numbers = list(map(int, input("Enter numbers: ").split()))

maximum = numbers[0]
result = []

for number in numbers[1:]:
    if number > maximum:
        result.append(number)
        maximum = number

print("Numbers greater than all previous numbers:", result)