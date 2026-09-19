numbers = list(map(int, input("Enter numbers: ").split()))

current = 0
longest = 0

for number in numbers:
    if number % 2 != 0:
        current += 1
        longest = max(longest, current)
    else:
        current = 0

print("Longest odd sequence:", longest)