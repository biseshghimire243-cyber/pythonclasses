numbers = list(map(int, input("Enter numbers: ").split()))

longest = 0
current = 0

for number in numbers:
    if number > 0:
        current += 1
        longest = max(longest, current)
    else:
        current = 0

print("Longest positive sequence:", longest)