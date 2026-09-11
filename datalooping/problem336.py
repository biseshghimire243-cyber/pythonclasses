numbers = list(map(int, input("Enter numbers: ").split()))

pairs = 0
checked = set()

for number in numbers:
    if number not in checked:
        count = numbers.count(number)
        pairs += count * (count - 1) // 2
        checked.add(number)

print("Number of equal pairs:", pairs)