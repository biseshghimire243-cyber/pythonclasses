numbers = list(map(int, input("Enter numbers: ").split()))

longest = 1
current = 1

for i in range(1, len(numbers)):
    if numbers[i] % 2 != numbers[i - 1] % 2:
        current += 1
        longest = max(longest, current)
    else:
        current = 1

print("Longest alternating sequence:", longest)