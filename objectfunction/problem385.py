numbers = list(map(int, input("Enter numbers: ").split()))
target = int(input("Enter target: "))

current = 0
longest = 0

for number in numbers:
    if number < target:
        current += 1
        longest = max(longest, current)
    else:
        current = 0

print("Longest sequence below target:", longest)